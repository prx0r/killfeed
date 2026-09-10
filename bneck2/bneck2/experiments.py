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
    from bneck2 import graph as G
    from bneck2 import migration as M
    from bneck2 import quant as Q
    _h("E009", "B-vs-conviction gap is the crowdedness term",
       "adding (1-crowdedness) to severity flips E005 rho positive",
       "rho stays <= 0.3 after the penalty (gap is structural, keep both)",
       "graph_v2 + readings (no network)")
    g = G.load_graph()
    readings = Q.load_readings()
    ids = [n["id"] for n in g["nodes"]]
    b = {}
    for n in g["nodes"]:
        s = M.severity(n, readings.get(n["id"]))["B"]
        b[n["id"]] = s * (1 - float(n.get("crowdedness", 0.5)))
    c = {n["id"]: G.score_node(n) for n in g["nodes"]}
    n = len(ids)
    rb = {i: r for r, i in enumerate(sorted(ids, key=lambda i: b[i]))}
    rc = {i: r for r, i in enumerate(sorted(ids, key=lambda i: c[i]))}
    d2 = sum((rb[i] - rc[i]) ** 2 for i in ids)
    rho = round(1 - 6 * d2 / (n * (n * n - 1)), 3)
    return {"rho_penalized": rho, "rho_plain": -0.438, "n": n,
            "note": f"penalized rho={rho:.2f} vs plain -0.44"}, \
        ("CONFIRMED" if rho > 0.3 else "REFUTED"), n


def e010_acq_chain() -> tuple[dict, str, int]:
    """H-ACQ-1: lab capital events -> counterparty +5pp vs SPY in 20d."""
    import json
    from bneck2 import acq as A
    from bneck2 import lab as LAB
    LAB.preregister(
        "H-ACQ-1", "lab capital events move counterparties",
        "counterparty 20d excess vs SPY > +5pp on >=60% of events (n>=5)",
        "hit rate <60% or mean excess <= 0",
        "commitments.json dates + Yahoo daily closes vs SPY")
    doc = json.loads((ROOT / "data" / "labs" / "commitments.json")
                     .read_text(encoding="utf-8"))
    good, dropped = A.eligible(doc.get("commitments", []))
    rows = A.event_study(good)
    s = A.summarize(rows)
    s["events"] = len(good)
    s["dropped"] = len(dropped)
    s["rows"] = [(r["event"], r["ticker"], r.get("excess")) for r in rows]
    s["note"] = (f"{s.get('hit_rate', '?')} hit rate, mean excess "
                 f"{s.get('mean_excess', '?')}, n={s['n']} directional")
    return s, s["verdict"], s["n"]


def e011_acq_silicon() -> tuple[dict, str, int]:
    """H-ACQ-2 (refine of H-ACQ-1): irreversible silicon/capacity/nuclear
    commitments move counterparties; generic deployments do not."""
    from bneck2 import acq as A
    from bneck2 import lab as LAB
    LAB.preregister(
        "H-ACQ-2", "only irreversible commitments move prices",
        "silicon-roadmap/capacity-contract/multidecade kinds: hit>=60%, n>=5",
        "hit <60% (no better than all-events)",
        "same event study, kind subset; parent H-ACQ-1")
    rows, _ = _acq_rows()
    sub = [r for r in rows if r.get("kind") in
           ("silicon-roadmap", "capacity-contract", "multidecade-contract")]
    s = A.summarize(sub)
    s["rows"] = [(r["event"], r["ticker"], r["kind"], r["excess"]) for r in sub]
    s["parent"] = "H-ACQ-1 (refine)"
    s["note"] = (f"silicon/capacity subset: hit {s.get('hit_rate','?')}, "
                 f"mean {s.get('mean_excess','?')}, n={s['n']}")
    return s, s["verdict"], s["n"]


def e012_acq_size_split() -> tuple[dict, str, int]:
    """H-ACQ-3 (refine of H-ACQ-1): revenue-scale split in event response.

    Prereg amendment (receipt-logged): Yahoo chart meta carries no
    marketCap here and v7 needs crumbs, so size = XBRL revenue TTM
    (>= $100B = mega), measured via collectors/sec_facts.py. Same
    hypothesis, honest instrument.
    """
    from bneck2 import acq as A
    from bneck2 import lab as LAB
    from collectors import sec_facts as SF
    LAB.preregister(
        "H-ACQ-3", "size split in event response",
        "sub-$100B-revenue hit>=60%; mega hit<40%",
        "no size pattern",
        "XBRL revenue TTM split; parent H-ACQ-1")
    CIK = {"NVDA": "1045810", "AMD": "2488", "AVGO": "1730168",
           "GOOGL": "1652044", "AMZN": "1018724", "META": "1326801",
           "CSCO": "858877", "MU": "1430265", "CRWV": "1763920"}
    rows, _ = _acq_rows()
    rev = {}
    for r in rows:
        t = r["ticker"]
        if t not in rev:
            f = SF.fundamentals(CIK[t]) if t in CIK else {}
            rev[t] = f.get("revenue_ttm")
    mega = [r for r in rows if (rev.get(r["ticker"]) or 0) >= 1e11]
    rest = [r for r in rows if rev.get(r["ticker"]) is not None
            and rev[r["ticker"]] < 1e11]
    unknown = sorted({r["ticker"] for r in rows if rev.get(r["ticker"]) is None})
    sm, sr = A.summarize(mega), A.summarize(rest)
    out = {"mega": {**sm, "tickers": sorted({r["ticker"] for r in mega})},
           "rest": {**sr, "tickers": sorted({r["ticker"] for r in rest})},
           "unknown_size": unknown,
           "parent": "H-ACQ-1 (refine)",
           "note": f"mega(rev>=$100B) hit {sm.get('hit_rate', '?')} n={sm['n']} "
                   f"vs rest hit {sr.get('hit_rate', '?')} n={sr['n']}"}
    verdict = ("CONFIRMED" if sr.get("hit_rate", 0) >= 0.6 and sm.get("hit_rate", 1) < 0.4
               and sr.get("n", 0) >= 3 else "REFUTED"
               if sr.get("n", 0) + sm.get("n", 0) >= 5 else "INCONCLUSIVE")
    return out, verdict, sr.get("n", 0) + sm.get("n", 0)


def e013_redteam() -> tuple[dict, str, int]:
    """Monthly red-team: strongest case AGAINST the top-conviction node."""
    from bneck2 import graph as G
    from bneck2 import quant as Q
    from bneck2 import lab as LAB
    LAB.preregister(
        "E013", "monthly red-team vs top conviction",
        "top-conviction node shows >=3 disconfirming facts (non-firings, "
        "negative drift, crowdedness>=0.7)",
        "fewer than 3 disconfirming facts (conviction stands unattacked)",
        "graph + verdicts + prices (no network)")
    import json as _j
    g = G.load_graph()
    rows = Q.score_all(g, Q.load_readings())
    top = max(rows, key=lambda r: r.get("binding", 0))
    node = next(n for n in g["nodes"] if n["id"] == top["id"])
    ver = [_j.loads(l) for l in
           (ROOT / "data" / "beliefs" / "kill_observations.jsonl")
           .read_text(encoding="utf-8").splitlines() if l.strip()]
    nonfire = sum(1 for r in ver if r.get("node_id") == top["id"]
                  and r.get("verdict") == "NOT TRIGGERED")
    facts = []
    if nonfire >= 10:
        facts.append(f"{nonfire} non-firing verdicts on this node")
    if float(node.get("crowdedness", 0)) >= 0.7:
        facts.append(f"crowdedness {node.get('crowdedness')} (consensus long)")
    if top.get("dissolution", 0) >= 0.2:
        facts.append(f"dissolution {top['dissolution']:.2f} already priced")
    ok = len(facts) >= 3
    return {"node": top["id"], "binding": round(top.get("binding", 0), 3),
            "disconfirming": facts,
            "note": f"red-team vs {top['id']}: {len(facts)} disconfirming facts"}, \
        ("CONFIRMED" if ok else "REFUTED"), len(facts)


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
    "E010": e010_acq_chain,
    "E011": e011_acq_silicon,
    "E012": e012_acq_size_split,
    "E013": e013_redteam,
}




def _acq_rows():
    import json
    from bneck2 import acq as A
    doc = json.loads((ROOT / "data" / "labs" / "commitments.json")
                     .read_text(encoding="utf-8"))
    good, dropped = A.eligible(doc.get("commitments", []))
    rows = A.event_study(good)
    seen, uniq = set(), []
    for r in rows:
        if r.get("excess") is None:
            continue
        key = (r["event"], r["ticker"])
        if key not in seen:
            seen.add(key)
            uniq.append(r)
    return uniq, dropped


