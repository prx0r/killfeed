"""bneck2 migration tests — severity, velocity, cross-world X, release,
catalytic hazards, derivatives, alpha_v2, consistency, transfer tiers."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from bneck2 import consistency as CY
from bneck2 import migration as M


class TestSeverity(unittest.TestCase):
    NODE = {"id": "memory_hbm", "revenue_purity": 0.8, "td_years": 3.0}

    def test_formula(self):
        s = M.severity(self.NODE, {"demand_growth": 2.0})
        # 2.0*0.8*0.3*(0.5+0.25)/0.5 = 0.72
        self.assertAlmostEqual(s["B"], 0.72, places=3)
        self.assertTrue(s["permission_estimated"])

    def test_permission_prior(self):
        s = M.severity({"id": "power", "revenue_purity": 0.5, "td_years": 10.0})
        self.assertEqual(s["permission"], 0.85)

    def test_explicit_field_not_estimated(self):
        s = M.severity({"id": "x", "permission_friction": 0.9,
                        "revenue_purity": 0.5, "td_years": 5.0})
        self.assertFalse(s["permission_estimated"])


class TestVelocity(unittest.TestCase):
    def test_needs_two_points(self):
        self.assertEqual(M.velocity("n", [])["n"], 0)

    def test_growth_and_accel(self):
        h = [{"node_id": "n", "B": 1.0, "ts": "2026-01-01T00:00:00Z"},
             {"node_id": "n", "B": 2.0, "ts": "2026-07-01T00:00:00Z"},
             {"node_id": "n", "B": 4.0, "ts": "2027-01-01T00:00:00Z"}]
        v = M.velocity("n", h)
        self.assertGreater(v["dB_dt"], 0)
        self.assertGreater(v["accel"], 0)


class TestCrossWorld(unittest.TestCase):
    def test_exposure(self):
        inc = {"id": "bpo", "survives": {"w1": 0.2, "w2": 1.0}}
        worlds = [{"id": "w1", "p_you": 0.5}, {"id": "w2", "p_you": 0.5}]
        x = M.cross_world_exposure(inc, worlds)
        self.assertAlmostEqual(x["X"], 0.4)


class TestRelease(unittest.TestCase):
    def test_laplace_no_data(self):
        r = M.release_probability("n", [])
        self.assertEqual(r["P_release"], 0.5)

    def test_supply_only(self):
        obs = [{"node_id": "n", "signal": "capacity adds",
                "measured": "cap +20%", "verdict": "TRIGGERED"}]
        r = M.release_probability("n", obs)
        self.assertGreater(r["P_release"], 0.5)


class TestCatalytic(unittest.TestCase):
    def test_hazard_update(self):
        self.assertAlmostEqual(
            M.hazard_update(0.1, [{"strength": 1.0, "event": 1.0}]), 0.2)

    def test_catalytic_filter(self):
        g = {"edges": [{"relation": "DEPENDS_ON"}, {"relation": "CATALYZES"}]}
        self.assertEqual(len(M.catalytic_edges(g)), 1)


class TestDerivative(unittest.TestCase):
    G = {"edges": [
        {"source": "accelerators", "target": "memory_hbm",
         "relation": "DEPENDS_ON"},
        {"source": "memory_hbm", "target": "memory_dram",
         "relation": "CASCADE"}]}

    def test_dependents_and_unlocks(self):
        d = M.bottleneck_derivative("memory_hbm", self.G)
        by = {r["node"]: r["via"] for r in d}
        self.assertEqual(by["accelerators"], "dependent-surge")
        self.assertEqual(by["memory_dram"], "cascade-unlock")


class TestAlphaV2(unittest.TestCase):
    def test_master_equation(self):
        self.assertAlmostEqual(M.alpha_v2(0.5, 1e9, 0.4, 0.7, 0.8, 0.3),
                               0.5 * 1e9 * 0.4 * 0.7 * 0.8 - 0.3)


class TestConsistency(unittest.TestCase):
    DOC = {"worlds": [{"id": "w1", "p_you": 0.1, "p_market": 0.8}],
             "incumbents": [{"id": "bpo", "survives": {"w1": 0.1},
                             "market_survival_p": 0.9}]}

    def test_finds_contradiction(self):
        rows = CY.find_inconsistencies(self.DOC)
        self.assertEqual(len(rows), 1)
        self.assertAlmostEqual(rows[0]["score"], 0.8 * 0.8, places=3)

    def test_render(self):
        self.assertIn("bpo", CY.render(CY.find_inconsistencies(self.DOC)))

    def test_quiet_when_consistent(self):
        doc = {"worlds": [{"id": "w1", "p_you": 0.8, "p_market": 0.8}],
               "incumbents": [{"id": "b", "survives": {"w1": 0.9},
                               "market_survival_p": 0.9}]}
        self.assertEqual(CY.find_inconsistencies(doc), [])


class TestTransfer(unittest.TestCase):
    def test_benchmarks_low(self):
        self.assertLess(M.transfer_weight("benchmark"),
                        M.transfer_weight("verified_cashflow"))
        self.assertEqual(M.transfer_weight("unknown-kind"), 0.5)


class TestGoatedPrimitives(unittest.TestCase):
    def test_deliverable_mw(self):
        d = M.deliverable_mw(5000.0, {"site": 1.0, "interconnect": 0.5,
                                      "transformer": 0.8, "generation": 1.0,
                                      "permit": 0.9})
        self.assertAlmostEqual(d["deliverable_mw"], 5000 * 0.36)
        self.assertEqual(d["estimated_legs"], [])

    def test_deliverable_flags_missing(self):
        d = M.deliverable_mw(100.0, {})
        self.assertEqual(len(d["estimated_legs"]), 5)

    def test_surprise_moves_toward_evidence(self):
        up = M.surprise_update(0.5, 2.0, 1.0)
        self.assertGreater(up["posterior"], 0.5)
        flat = M.surprise_update(0.5, 2.0, 0.0)
        self.assertAlmostEqual(flat["posterior"], 0.5)

    def test_cliff(self):
        self.assertTrue(M.cliff_proximity("assay_sample_usd", 0.5)["crossed"])
        self.assertFalse(M.cliff_proximity("assay_sample_usd", 50.0)["crossed"])
        self.assertIsNone(M.cliff_proximity("nope", 1.0)["proximity"])

    def test_duration_mismatch(self):
        self.assertEqual(
            M.duration_mismatch(6.0, 2.0)["verdict"], "SHORT_CANDIDATE")
        self.assertEqual(M.duration_mismatch(6.0, None)["verdict"],
                         "INSUFFICIENT")
        self.assertEqual(M.tech_half_life(4.0), 2.0)


class TestAtoms(unittest.TestCase):
    def test_universe_loads(self):
        from bneck2 import atoms as A
        cos = A.load_universe()
        self.assertGreaterEqual(len(cos), 10)
        self.assertTrue(all(c.get("ticker") and c.get("nodes") for c in cos))

    def test_small_critical_outranks_giant(self):
        from bneck2 import atoms as A
        cos = [{"ticker": "LPKF-like", "layer": "t", "nodes": ["n1"],
                "rev_usd_m": 125},
               {"ticker": "GIANT", "layer": "t", "nodes": ["n1"],
                "rev_usd_m": 100000}]
        rows = A.screen(cos, severity_by_node={"n1": 1.0})
        self.assertEqual(rows[0]["ticker"], "LPKF-like")

    def test_breadth_bonus(self):
        from bneck2 import atoms as A
        one = {"ticker": "A", "layer": "t", "nodes": ["n1"], "rev_usd_m": 500}
        two = {"ticker": "B", "layer": "t", "nodes": ["n1", "n2"],
               "rev_usd_m": 500}
        sev = {"n1": 1.0, "n2": 1.0}
        self.assertGreater(A.convexity(two, sev)["convexity"],
                           A.convexity(one, sev)["convexity"])


class TestPredict(unittest.TestCase):
    def test_spearman(self):
        from bneck2 import predict as PD
        self.assertAlmostEqual(
            PD.spearman([1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 4.0, 5.0]), 1.0)
        self.assertIsNone(PD.spearman([1.0, 1.0], [1.0, 2.0]))
        self.assertIsNone(PD.spearman([1.0], [1.0]))

    def test_grid_shapes(self):
        from bneck2 import predict as PD
        self.assertEqual(len(PD.grid("monthly", 12)), 12)
        self.assertEqual(len(PD.grid("biweekly", 12)), 24)

    def test_composite_by_date_no_leak(self):
        from bneck2 import predict as PD
        rows = [{"date": "2026-01-01", "ticker": t, "f": float(i),
                 "fwd_20": 0.01} for i, t in enumerate("ABCD")]
        rows += [{"date": "2026-02-01", "ticker": t, "f": 100.0 + i,
                  "fwd_20": 0.01} for i, t in enumerate("ABCD")]
        out = PD.composite_by_date(rows, ["f"], {"f": 1.0})
        jan = sorted(r["score"] for r in out if r["date"] == "2026-01-01")
        feb = sorted(r["score"] for r in out if r["date"] == "2026-02-01")
        # identical within-date ranks despite level shift => per-date norms
        self.assertEqual([round(x, 3) for x in jan], [round(x, 3) for x in feb])

    def test_trailing_forward(self):
        from bneck2 import predict as PD
        cl = [(f"2026-01-{d:02d}", 100.0 + d) for d in range(1, 15)]
        self.assertAlmostEqual(PD.trailing_return(cl, "2026-01-14", 5), 5 / 109, places=3)
        self.assertIsNone(PD.forward_return(cl, "2026-01-14", 5))


class TestDeep(unittest.TestCase):
    def test_biweekly_grid_count(self):
        from bneck2 import predict as PD
        g = PD.grid("biweekly", 12)
        self.assertEqual(len(g), 24)
        self.assertTrue(all(g[i] < g[i + 1] for i in range(len(g) - 1)))

    def test_submissions_cached(self):
        from bneck2 import predict as PD
        PD._SUBMISSIONS_CACHE["TEST"] = {"cached": True}
        self.assertEqual(PD.submissions("TEST"), {"cached": True})
        del PD._SUBMISSIONS_CACHE["TEST"]

    def test_shift(self):
        from bneck2 import predict as PD
        self.assertEqual(PD._shift("2026-09-10", -30), "2026-08-11")

    def test_finra_cache_file(self):
        from collectors import finra
        import tempfile
        self.assertTrue(callable(finra.short_file))


class TestFocusedNames(unittest.TestCase):
    def test_kalshi_series_fields(self):
        from collectors import kalshi as KL
        doc = {"events": [{"title": "T", "series_ticker": "KX",
                           "markets": [{"ticker": "KX-1", "last_price_dollars": "0.4",
                                        "volume_24h_fp": "5", "liquidity_dollars": "6"}]}]}
        rows = KL.parse_events(doc, "whatever txyz")
        self.assertEqual(rows, [])

    def test_universe_expanded(self):
        from bneck2 import predict as PD
        self.assertGreaterEqual(len(PD.UNIVERSE), 25)
        for t in ("ONTO", "SNPS", "TSM"):
            self.assertIn(t, PD.UNIVERSE)

    def test_registry_has_focus(self):
        from bneck2 import experiments as X
        for e in ("E018", "E019", "E020", "E021", "E022", "E023",
                  "E024", "E025", "E026", "E027", "E028", "E032", "E033",
                  "E034"):
            self.assertIn(e, X.REGISTRY)

    def test_crypto_history_shape(self):
        from bneck2 import prices as P
        h = P.crypto_history("bitcoin", 7)
        self.assertIn("closes", h)
        if h["closes"]:
            self.assertIn("date", h["closes"][0])

    def test_xextract_classify(self):
        from bneck2 import xextract as XE
        c = XE.classify("Long $NVDA into earnings, target $250")
        self.assertEqual(c["direction"], "LONG")
        self.assertIn("NVDA", c["tickers"])
        c2 = XE.classify("nice weather today, markets closed")
        self.assertEqual(c2["kind"], "COMMENTARY")
        d = XE.density([{"text": "long NVDA", "isReply": False},
                        {"text": "hello", "isReply": True}])
        self.assertEqual(d["n"], 1)

    def test_beta_math(self):
        br = [0.01, -0.02, 0.03]
        nr = [0.02, -0.04, 0.06]
        mb, mn = sum(br) / 3, sum(nr) / 3
        beta = sum((b - mb) * (n - mn) for b, n in zip(br, nr)) / sum((b - mb) ** 2 for b in br)
        self.assertAlmostEqual(beta, 2.0)


class TestLeads(unittest.TestCase):
    def test_xcorr_peak(self):
        from bneck2 import leads as LD
        x = [0, 0, 0, 1.0, 0, 0, 0, 0, 0, 0]
        y = [0, 0, 0, 0, 0, 1.0, 0, 0, 0, 0]
        ll = LD.lead_lag(x, y, max_lag=4)
        self.assertEqual(ll["peak_lag"], 2)
        self.assertGreater((ll["peak_r"] or 0), 0.5)

    def test_insufficient(self):
        from bneck2 import leads as LD
        ll = LD.lead_lag([1.0], [1.0])
        self.assertEqual(ll["verdict"], "INSUFFICIENT")

    def test_bucketize(self):
        from bneck2 import leads as LD
        starts = ["2026-01-01", "2026-01-08", "2026-01-15"]
        self.assertEqual(LD.bucketize(["2026-01-02", "2026-01-09", "2026-01-09"], starts), [1, 2, 0])


class TestAcq(unittest.TestCase):
    def test_map_and_eligible(self):
        from bneck2 import acq as A
        self.assertEqual(A.map_tickers("OpenAI", "AMD GPUs 6 GW"), ["AMD"])
        self.assertEqual(A.map_tickers("OpenAI", "Cerebras"), [])
        good, dropped = A.eligible([
            {"date": "2026-01-01", "lab": "x", "target": "y", "kind": "k"},
            {"date": "2026-04-06", "lab": "Anthropic",
             "target": "Google/Broadcom", "kind": "deployment"},
            {"date": "2026-01-14", "lab": "OpenAI", "target": "Cerebras",
             "kind": "deployment"}])
        self.assertEqual(len(good), 1)
        self.assertEqual(
            {d["reason"] for d in dropped},
            {"placeholder-date", "private-or-ambiguous-target"})

    def test_summarize_gates(self):
        from bneck2 import acq as A
        rows = [{"excess": 0.20}, {"excess": 0.01},
                {"excess": -0.01}, {"excess": 0.30}, {"excess": 0.10}]
        s = A.summarize(rows)
        self.assertEqual(s["verdict"], "CONFIRMED")
        self.assertEqual(A.summarize([{"excess": None}])["verdict"],
                         "INCONCLUSIVE")


if __name__ == "__main__":
    unittest.main()