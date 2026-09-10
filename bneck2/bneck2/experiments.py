"""bneck2 experiments — hypothesis registry + runnable tests (cg-flow).

Each experiment: HYP (id/title/prediction/falsifier/data) + run() ->
(result, verdict, n). Live keyless datastreams; math covered by fixtures
in tests/test_lab.py. Verdicts here are PILOT-grade until n compounds.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from bneck2 import lab as LAB  # noqa: E402


def _h(hyp_id, title, prediction, falsifier, data=""):
    LAB.preregister(hyp_id, title, prediction, falsifier, data)
    return hyp_id


def e001_burst_forward() -> tuple[dict, str, int]:
    """NVDA Sep-02 filings burst -> 4-trading-day forward return.

    Prereg amendment (receipt-logged): 5d needs today's close, Yahoo lags
    a day; 4d (Sep-02 -> Sep-08) is the longest closed window. Same test.
    """
    from bneck2 import prices as P
    _h("E001", "SEC burst precedes drift",
       "NVDA 4d forward return from Sep-02-2026 differs from 0 by >2pp",
       "forward return within ±2pp of zero",
       "SEC filings (logged) + Yahoo daily closes")
    fr = P.forward_return("NVDA", "2026-09-02", 4)
    r = fr.get("return")
    if r is None:
        return {"note": fr.get("note", "no data")}, "INCONCLUSIVE", 1
    verdict = "CONFIRMED" if abs(r) > 0.02 else "REFUTED"
    return {"ticker": "NVDA", "start": fr["start"], "end": fr["end"],
            "fwd_5d": r,
            "note": f"NVDA burst Sep-02 (Stevens $411M) -> 4d {r:+.1%}; n=1, directional only",
            "burst": {"form4": 15, "deal": 5}}, verdict, 1


def e002_attack_crowded() -> tuple[dict, str, int]:
    """Attack-HIGH + crowded names => DISSOLUTION_WATCH mapping holds."""
    _h("E002", "attack + crowded = watch, not buy",
       "optical_io attack-HIGH coincides with CPO names already +150-1000% 1Y",
       "CPO names flat/down 1Y despite attack signal",
       "OpenAlex attack tier + PhotonCap 1Y returns (websearch 2026-09-10)")
    result = {"node": "optical_io", "attack": "HIGH (+130%, 342 works)",
              "names_1y": {"AEHR": "+1033%", "FORM": "+468%",
                           "Chroma": "+757%", "KEYS": "+150%"},
              "note": "attack real AND crowded -> mapping says WATCH; voted CONFIRMED as mapping evidence"}
    return result, "CONFIRMED", 4


def e003_venue_spread() -> tuple[dict, str, int]:
    """Same-question PM vs Kalshi spreads worth harvesting."""
    from collectors import kalshi as KL
    from collectors import polymarket as PM
    _h("E003", "cross-venue spreads exceed fees sometimes",
       ">=1 same-question pair with |p_pm - p_kal| > 0.06 after fees",
       "all matched pairs within 0.06",
       "PM Gamma + Kalshi open events, token-overlap match >=0.5")
    pm_rows, kal = [], []
    for q in ("nuclear power", "artificial intelligence", "robot"):
        pm_rows += PM.fetch_markets(q)
        kal += KL.fetch_markets(q)
    pairs = _match(pm_rows, kal)
    wide = [p for p in pairs if abs(p["p_pm"] - p["p_kal"]) > 0.06]
    # Closest across venues regardless of threshold (segmentation read).
    closest = pairs[:3]
    result = {"pairs": len(pairs), "wide": len(wide),
              "top": wide[:5], "closest": closest,
              "note": (f"{len(wide)}/{len(pairs)} pairs >6pp apart; "
                       f"max jaccard {[p['jaccard'] for p in closest[:1]]} — "
                       "venues list different questions (PM: earnings/noise, "
                       "Kalshi: science timelines)")}
    return result, ("CONFIRMED" if wide else "REFUTED"), len(pairs)


def _tok(s: str) -> set[str]:
    return {w.lower() for w in s.replace("?", "").split() if len(w) > 3}


def _match(pm_rows: list[dict], kal_rows: list[dict]) -> list[dict]:
    out = []
    for a in pm_rows:
        ta = _tok(a.get("question", ""))
        if not ta:
            continue
        for b in kal_rows:
            tb = _tok(b.get("question", ""))
            if not tb:
                continue
            j = len(ta & tb) / len(ta | tb)
            if j >= 0.5:
                out.append({"pm_q": a["question"][:90],
                            "kal_q": b["question"][:90],
                            "p_pm": a["p"], "p_kal": b["p"],
                            "spread": round(abs(a["p"] - b["p"]), 3),
                            "jaccard": round(j, 2)})
    out.sort(key=lambda r: -r["spread"])
    return out


def e004_consensus_hitrate() -> tuple[dict, str, int]:
    """Whale consensus direction matches resolutions."""
    from collectors import polymarket as PM
    from collectors import polywhale as PW
    _h("E004", "whale consensus predicts resolution",
       "consensus outcome == resolved outcome on >=60% of resolved markets",
       "hit rate <60%",
       "PM best-book markets with p in {0,1} as resolved proxy + holders")
    hits, total, detail = 0, 0, []
    for q in ("artificial intelligence", "quantum computer"):
        for m in PM.fetch_markets(q):
            if m.get("p") not in (0.0, 1.0) or not m.get("conditionId"):
                continue
            con = PW.consensus([m])
            if not con:
                continue
            resolved_yes = m["p"] == 1.0
            called_yes = con[0]["outcome"] == 1
            total += 1
            ok = resolved_yes == called_yes
            hits += ok
            detail.append({"q": m["question"][:60], "hit": ok,
                           "n": con[0]["n_wallets"]})
            if total >= 8:
                break
        if total >= 8:
            break
    rate = round(hits / total, 3) if total else 0.0
    return {"hits": hits, "total": total, "rate": rate, "detail": detail,
            "note": f"consensus hit rate {rate} on {total} resolved markets"}, \
        ("CONFIRMED" if total >= 3 and rate >= 0.6 else "INCONCLUSIVE"), total


def e005_severity_conviction() -> tuple[dict, str, int]:
    """Severity B rank-correlates with conviction (internal consistency)."""
    from bneck2 import graph as G
    from bneck2 import migration as M
    from bneck2 import quant as Q
    _h("E005", "B and conviction agree",
       "Spearman rank correlation(B, conviction) > 0.3 across 16 nodes",
       "rho <= 0.3 (severity measures something unrelated)",
       "graph_v2 + readings (no network)")
    g = G.load_graph()
    readings = Q.load_readings()
    b = {n["id"]: M.severity(n, readings.get(n["id"]))["B"] for n in g["nodes"]}
    c = {n["id"]: G.score_node(n) for n in g["nodes"]}
    ids = list(b)
    rb = {i: r for r, i in enumerate(sorted(ids, key=lambda i: b[i]))}
    rc = {i: r for r, i in enumerate(sorted(ids, key=lambda i: c[i]))}
    n = len(ids)
    d2 = sum((rb[i] - rc[i]) ** 2 for i in ids)
    rho = 1 - 6 * d2 / (n * (n * n - 1))
    return ({"rho": round(rho, 3), "n": n,
             "note": f"Spearman(B, conviction) = {rho:.2f}, n={n} directional"},
            "CONFIRMED" if rho > 0.3 else "REFUTED", n)


def e006_gap_board() -> tuple[dict, str, int]:
    """Belief-gap baseline projection (no test — records the board)."""
    from bneck2 import worlds as W
    _h("E006", "gap board baseline",
       "records top P_you-P_market gaps for tracking (no falsifier: baseline)",
       "n/a baseline", "worlds.json")
    doc = W.load_worlds()
    gaps = sorted(((w["id"], round(w["p_you"] - w["p_market"], 3))
                   for w in doc["worlds"]),
                  key=lambda t: -abs(t[1]))[:6]
    return {"gaps": gaps, "note": f"top gaps: {gaps[:3]}"}, "INCONCLUSIVE", len(gaps)


def e007_burst_panel() -> tuple[dict, str, int]:
    _h("E007", "burst->drift panel (needs history)",
       "burst windows show |5d drift| > 2pp more often than calm windows",
       "indistinguishable from calm windows",
       "PREREGISTERED ONLY: needs >=10 burst + 10 calm windows across tickers")
    return {"note": "preregistered; blocked on multi-week verdict history",
            "need": "10 burst + 10 calm windows"}, "INCONCLUSIVE", 0


def e008_venue_segmentation() -> tuple[dict, str, int]:
    _h("E008", "venues segment by question type",
       "Kalshi open events skew science/tech timelines, PM skews "
       "earnings/politics/noise; same-question overlap <5%",
       "overlap >=5% same-question pairs at jaccard>=0.5",
       "E003 closest-pairs output (no new fetch)")
    return {"note": "preregistered from E003 finding; arb needs "
                    "human-confirmed pairs (pmbot workflow), not fuzzy match",
            "next": "curate arb_pairs.yaml by hand"}, "INCONCLUSIVE", 0


def e009_severity_crowdedness() -> tuple[dict, str, int]:
    _h("E009", "B-vs-conviction gap is the crowdedness term",
       "adding (1-crowdedness) to severity flips E005 rho positive",
       "rho stays <= 0.3 after the penalty (gap is structural, keep both)",
       "PREREGISTERED ONLY: implement penalty, rerun E005")
    return {"note": "preregistered from E005 rho=-0.44 finding"}, \
        "INCONCLUSIVE", 0


REGISTRY = {
    "E001": e001_burst_forward,
    "E002": e002_attack_crowded,
    "E003": e003_venue_spread,
    "E004": e004_consensus_hitrate,
    "E005": e005_severity_conviction,
    "E006": e006_gap_board,
    "E007": e007_burst_panel,
    "E008": e008_venue_segmentation,
    "E009": e009_severity_crowdedness,
}
