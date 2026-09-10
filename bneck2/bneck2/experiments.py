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


def e014_signal_chain() -> tuple[dict, str, int]:
    """H-SIG-1: factor composite beats momentum bogey on holdout."""
    from bneck2 import backtest as BT
    from bneck2 import lab as LAB
    from bneck2 import predict as PD
    LAB.preregister(
        "H-SIG-1", "composite beats momentum out-of-sample",
        "holdout Sharpe(composite) > Sharpe(momentum), same dates/costs",
        "composite <= momentum (factors add nothing)",
        "12mo monthly panel; train m1-9, holdout m10-12; verdict needs n>=30 rows")
    import json as _j
    prow = sorted((ROOT / "data" / "predict").glob("panel-*.jsonl"))
    rows = []
    for f in prow:
        rows += [_j.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    if not rows:
        return {"note": "no predict panel yet; run scripts/build_predict_panel.py",
                "need": "panel files"}, "INCONCLUSIVE", 0
    dates = sorted({r["date"] for r in rows})
    cut = dates[max(len(dates) - 3, 0)]
    train = [r for r in rows if r["date"] < cut]
    hold = [r for r in rows if r["date"] >= cut]
    scr = PD.screen(train)
    winners = [s["factor"] for s in scr
               if s["IC"] is not None and abs(s["IC"]) > 0.1 and s["n"] >= 20]
    signs = {s["factor"]: 1.0 if (s["IC"] or 0) >= 0 else -1.0 for s in scr}
    if not winners:
        return {"train_screen": scr, "note": "no factor clears IC>0.1 on train"},
    ("REFUTED",  len(train))
    comp_hold = PD.composite_by_date([dict(r) for r in hold], winners,
                                       signs)
    mom_hold = [{"date": r["date"], "ticker": r["ticker"],
                 "score": r.get("f_mom_20") or 0.0,
                 "forward_return": r.get("fwd_20")} for r in hold]
    _, cs = BT.walk_forward([{"date": r["date"], "ticker": r["ticker"],
                              "score": r["score"],
                              "forward_return": r.get("fwd_20") or 0.0}
                             for r in comp_hold if r.get("fwd_20") is not None])
    _, ms = BT.walk_forward([dict(r, forward_return=r.get("forward_return") or 0.0)
                             for r in mom_hold if r.get("forward_return") is not None])
    out = {"train_screen": scr, "winners": winners,
           "composite_sharpe": cs.get("sharpe"), "momentum_sharpe": ms.get("sharpe"),
           "holdout_n": len(hold),
           "note": f"composite {cs.get('sharpe')} vs momentum {ms.get('sharpe')} on holdout"}
    verdict = ("CONFIRMED" if (cs.get("sharpe") or -9) > (ms.get("sharpe") or 9)
               and len(hold) >= 30 else "REFUTED" if len(hold) >= 30 else "INCONCLUSIVE")
    return out, verdict, len(hold)


def e015_signal_biweekly() -> tuple[dict, str, int]:
    """H-SIG-2 (mutate of H-SIG-1): biweekly grid (26 dates) cures the
    3-point-Sharpe noise; same factors, train first 18, holdout last 8."""
    from bneck2 import backtest as BT
    from bneck2 import lab as LAB
    from bneck2 import predict as PD
    LAB.preregister(
        "H-SIG-2", "biweekly grid rescues the signal test",
        "holdout Sharpe(composite) > Sharpe(momentum) on 8 biweekly dates",
        "composite <= momentum (factors add nothing at any grid)",
        "data/predict/biwk-*.jsonl; parent H-SIG-1")
    import json as _j
    rows = []
    for f in sorted((ROOT / "data" / "predict").glob("biwk-*.jsonl")):
        rows += [_j.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    if not rows:
        return {"note": "no biweekly panel; run build_predict_panel.py --biweekly",
                "need": "biweekly panel"}, "INCONCLUSIVE", 0
    dates = sorted({r["date"] for r in rows})
    cut = dates[max(len(dates) - 8, 0)]
    train = [r for r in rows if r["date"] < cut]
    hold = [r for r in rows if r["date"] >= cut]
    scr = PD.screen(train)
    winners = [s["factor"] for s in scr
               if s["IC"] is not None and abs(s["IC"]) > 0.1 and s["n"] >= 40]
    signs = {s["factor"]: 1.0 if (s["IC"] or 0) >= 0 else -1.0 for s in scr}
    if not winners:
        return {"train_screen": scr, "note": "no factor clears IC>0.1 on train"},
    ("REFUTED", len(train))
    comp_hold = PD.composite_by_date([dict(r) for r in hold], winners, signs)
    mom_hold = [{"date": r["date"], "ticker": r["ticker"],
                 "score": r.get("f_mom_20") or 0.0,
                 "forward_return": r.get("fwd_20")} for r in hold]

    def _wf(rs):
        ok = []
        for r in rs:
            fr = r.get("forward_return", r.get("fwd_20"))
            if fr is not None:
                ok.append(dict(r, forward_return=fr))
        return BT.walk_forward(ok)[1] if ok else {"sharpe": None}

    cs, ms = _wf(comp_hold), _wf(mom_hold)
    out = {"train_screen": scr, "winners": winners,
           "composite_sharpe": cs.get("sharpe"),
           "momentum_sharpe": ms.get("sharpe"),
           "holdout_n": len(hold), "holdout_dates": len(dates) - len([d for d in dates if d < cut]),
           "note": f"composite {cs.get('sharpe')} vs momentum {ms.get('sharpe')} on biweekly holdout"}
    verdict = ("CONFIRMED" if (cs.get("sharpe") is not None and ms.get("sharpe") is not None
               and cs["sharpe"] > ms["sharpe"]) and len(hold) >= 60
               else "REFUTED" if len(hold) >= 60 else "INCONCLUSIVE")
    return out, verdict, len(hold)


def e016_burst_reversal() -> tuple[dict, str, int]:
    """H-SIG-3 (mutate of H-SIG-2): insider bursts REVERSE (IC<0), and
    leg attribution tells whether shorts carry the composite."""
    from bneck2 import backtest as BT
    from bneck2 import lab as LAB
    from bneck2 import predict as PD
    LAB.preregister(
        "H-SIG-3", "burst reversal + short-leg carry",
        "negated-burst factor IC>0.15 on full biweekly panel AND "
        "composite short leg Sharpe > long leg Sharpe",
        "burst IC>=0 as long, or long leg carries (no reversal edge)",
        "data/predict/biwk-*.jsonl; parent H-SIG-2")
    import json as _j
    rows = []
    for f in sorted((ROOT / "data" / "predict").glob("biwk-*.jsonl")):
        rows += [_j.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    rows = [r for r in rows if r.get("fwd_20") is not None]
    nb = [dict(r, f_burst_neg=-(r["f_burst"] or 0.0)) for r in rows
          if r.get("f_burst") is not None]
    ic = PD.spearman([r["f_burst_neg"] for r in nb],
                     [r["fwd_20"] for r in nb])
    # leg attribution on composite winners from E015 screen
    by_date = {}
    for r in rows:
        by_date.setdefault(r["date"], []).append(r)
    longs, shorts = [], []
    for d in sorted(by_date):
        g = by_date[d]
        sc = {r["ticker"]: (r.get("f_mom_20") or 0) + (r.get("f_attack") or 0)
              for r in g}
        pos = BT.make_positions(sc, 0.2)
        ret = {r["ticker"]: r["fwd_20"] for r in g}
        longs.append(sum(max(pos[t], 0) * ret.get(t, 0) for t in pos))
        shorts.append(sum(min(pos[t], 0) * ret.get(t, 0) for t in pos))
    import math as _m
    def _sh(xs):
        m = sum(xs) / len(xs)
        v = sum((x - m) ** 2 for x in xs) / max(len(xs) - 1, 1)
        return round(m / (_m.sqrt(v) or 1e-9), 3)
    out = {"burst_neg_IC": ic, "n_burst": len(nb),
           "long_leg_sharpe_like": _sh(longs), "short_leg_sharpe_like": _sh(shorts),
           "note": f"neg-burst IC={ic} n={len(nb)}; long {_sh(longs)} vs short {_sh(shorts)}"}
    verdict = ("CONFIRMED" if (ic or 0) > 0.15 and _sh(shorts) > _sh(longs)
               else "REFUTED")
    return out, verdict, len(nb)


def e017_long_only() -> tuple[dict, str, int]:
    """H-SIG-4: long-only top-tercile beats equal-weight universe.

    The L/S composites lose less but still lose (drawdown regime).
    Test whether the long leg alone carries edge vs holding everything.
    """
    from bneck2 import lab as LAB
    from bneck2 import predict as PD
    LAB.preregister(
        "H-SIG-4", "long-only top tercile beats universe",
        "mean(top-tercile fwd) > mean(all fwd) by >=2pp on holdout",
        "no 2pp edge (ranking adds nothing long-only)",
        "biweekly panel; parent H-SIG-2")
    import json as _j
    rows = []
    for f in sorted((ROOT / "data" / "predict").glob("biwk-*.jsonl")):
        rows += [_j.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    rows = [r for r in rows if r.get("fwd_20") is not None]
    dates = sorted({r["date"] for r in rows})
    cut = dates[max(len(dates) - 8, 0)]
    hold = [r for r in rows if r["date"] >= cut]
    train = [r for r in rows if r["date"] < cut]
    scr = PD.screen(train)
    winners = [s["factor"] for s in scr
               if s["IC"] is not None and abs(s["IC"]) > 0.1 and s["n"] >= 40]
    signs = {s["factor"]: 1.0 if (s["IC"] or 0) >= 0 else -1.0 for s in scr}
    scored = PD.composite_by_date(hold, winners or ["f_mom_20"], signs)
    by_date = {}
    for r in scored:
        by_date.setdefault(r["date"], []).append(r)
    ex, ux = [], []
    for d in sorted(by_date):
        g = sorted(by_date[d], key=lambda r: -r["score"])
        k = max(len(g) // 3, 1)
        ex.append(sum(r["fwd_20"] for r in g[:k]) / k
                  - sum(r["fwd_20"] for r in g) / len(g))
    m = sum(ex) / len(ex) if ex else 0.0
    out = {"winners": winners, "n_dates": len(ex),
           "mean_excess_vs_universe": round(m, 4),
           "note": f"top-tercile beats universe by {m:+.2%} per window"}
    return out, ("CONFIRMED" if m >= 0.02 else "REFUTED"), len(ex)




def utcnow() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def e018_nvda_sell_drift() -> tuple[dict, str, int]:
    """H-NVDA-1: heavy insider SELL months precede negative drift."""
    from bneck2 import lab as LAB
    from bneck2 import prices as P
    from collectors import openinsider as OI
    LAB.preregister(
        "H-NVDA-1", "insider sell intensity precedes drift",
        "top-quartile sell months -> next-month return < median month",
        "no difference (sales are noise/10b5-1)",
        "OpenInsider NVDA tape (100 rows) + Yahoo monthly closes")
    trades = [t for t in OI.by_ticker("NVDA") if t.get("is_sale")]
    closes = {c["date"][:7]: c["close"] for c in P.history("NVDA", "1y").get("closes", [])}
    by_m = {}
    for t in trades:
        by_m.setdefault(t.get("trade_date", "")[:7], 0.0)
        by_m[t.get("trade_date", "")[:7]] += abs(t.get("value_usd", 0))
    months = sorted(m for m in by_m if m in closes)
    if len(months) < 4:
        return {"note": "insufficient months", "months": months}, "INCONCLUSIVE", 0
    vals = sorted(by_m[m] for m in months)
    cut = vals[3 * len(vals) // 4]
    heavy = [m for m in months if by_m[m] >= cut]
    res = []
    for m in months:
        y, mm = map(int, m.split("-"))
        nm = f"{y + (mm == 12)}-{mm % 12 + 1:02d}"
        if m in closes and nm in closes and closes[m]:
            res.append((m, (closes[nm] - closes[m]) / closes[m], m in heavy))
    if len(res) < 4:
        return {"note": "insufficient forward months"}, "INCONCLUSIVE", 0
    hr = [r for _, r, h in res if h]
    lr = [r for _, r, h in res if not h]
    mh = sum(hr) / len(hr)
    ml = sum(lr) / len(lr)
    out = {"heavy_months": len(hr), "light_months": len(lr),
           "heavy_mean": round(mh, 4), "light_mean": round(ml, 4),
           "note": f"heavy-sell months {mh:+.1%} vs rest {ml:+.1%}"}
    return out, ("CONFIRMED" if mh < ml - 0.02 else "REFUTED"), len(res)


def e019_btc_nvda_beta() -> tuple[dict, str, int]:
    """H-BTC-1: BTC-NVDA trailing correlation (pair readout)."""
    from bneck2 import lab as LAB
    from bneck2 import prices as P
    from bneck2 import predict as PD
    LAB.preregister(
        "H-BTC-1", "BTC-NVDA correlation measurable and positive",
        "90d return correlation > 0.3",
        "rho <= 0.3 (decoupled — trade separately)",
        "CoinGecko BTC daily + Yahoo NVDA daily")
    bc = {c["date"]: c["close"] for c in P.crypto_history("bitcoin", 120).get("closes", [])}
    nv = {c["date"]: c["close"] for c in P.history("NVDA", "6mo").get("closes", [])}
    days = sorted(set(bc) & set(nv))[-90:]
    if len(days) < 30:
        return {"note": "insufficient overlap", "n": len(days)}, "INCONCLUSIVE", 0
    br = [(bc[days[i + 1]] - bc[days[i]]) / bc[days[i]] for i in range(len(days) - 1)]
    nr = [(nv[days[i + 1]] - nv[days[i]]) / nv[days[i]] for i in range(len(days) - 1)]
    rho = PD.spearman(br, nr)
    mb, mn = sum(br) / len(br), sum(nr) / len(nr)
    den = sum((b - mb) ** 2 for b in br)
    beta = (sum((b - mb) * (n - mn) for b, n in zip(br, nr)) / den) if den else None
    out = {"rho": rho, "beta_btc_on_nvda": round(beta, 3) if beta else None,
           "n_days": len(days),
           "note": f"90d BTC-NVDA return rho={rho}, beta={beta}"}
    return out, ("CONFIRMED" if (rho or 0) > 0.3 else "REFUTED"), len(days)


def e020_btc_pm_snapshot() -> tuple[dict, str, int]:
    """H-BTC-2: snapshot live BTC price-level markets for 7d resolution."""
    from bneck2 import lab as LAB
    from collectors import polymarket as PM
    LAB.preregister(
        "H-BTC-2", "BTC level markets resolve as priced (calibration)",
        ">=70% resolve in the priced direction",
        "below 70% (miscalibrated levels)",
        "snapshot today, resolve via re-fetch in 7d")
    rows = PM.fetch_markets("bitcoin")
    live = [r for r in rows if 0.05 < r.get("p", 0) < 0.95][:10]
    import json as _j
    snap_path = ROOT / "data" / "predict" / "btc_levels.json"
    try:
        snaps = _j.loads(snap_path.read_text())
    except (OSError, ValueError):
        snaps = []
    have = {(s.get("question"), s.get("p")) for s in snaps}
    new = 0
    for r in live:
        if (r["question"], r["p"]) not in have:
            snaps.append({"question": r["question"], "p": r["p"],
                          "snapshot": utcnow()[:10], "resolved": None})
            new += 1
    (ROOT / "data" / "predict").mkdir(parents=True, exist_ok=True)
    snap_path.write_text(_j.dumps(snaps, indent=1))
    res = [s for s in snaps if s.get("resolved") is not None]
    hits = sum(1 for s in res if s.get("hit"))
    out = {"tracked": len(snaps), "new": new, "resolved": len(res),
           "hits": hits, "note": f"{len(snaps)} BTC levels tracked, {len(res)} resolved"}
    if len(res) < 5:
        return out, "INCONCLUSIVE", len(res)
    return out, ("CONFIRMED" if hits / len(res) >= 0.7 else "REFUTED"), len(res)


def e021_sec_leads_price() -> tuple[dict, str, int]:
    """H-LEAD-1: SEC filings lead price moves (insiders file, then drift)."""
    from bneck2 import lab as LAB
    from bneck2 import leads as LD
    LAB.preregister(
        "H-LEAD-1", "filings lead prices",
        "SEC-weekly xcorr peaks at lag>0 vs NVDA weekly returns",
        "peak at lag<=0 (prices move first / sync noise)",
        "NVDA submissions history + Yahoo weeklies, 17 windows")
    starts, sec, _, rets = _weekly_panel_16w("NVDA", "1045810", "Nvidia")
    ll = LD.lead_lag(sec, rets)
    out = {"windows": len(starts) - 1, "peak": ll, "comparisons": 9,
           "note": f"SEC->NVDA: {ll['verdict']} (9-lag search: discovery-grade)"}
    return out, "EXPLORATORY", len(starts) - 1


def e022_hn_leads_price() -> tuple[dict, str, int]:
    """H-LEAD-2: HN chatter leads price (narrative precedes repricing)."""
    from bneck2 import lab as LAB
    from bneck2 import leads as LD
    LAB.preregister(
        "H-LEAD-2", "chatter leads prices",
        "HN-weekly xcorr peaks at lag>0 vs NVDA weekly returns",
        "peak at lag<=0",
        "HN Algolia date ranges + Yahoo weeklies, 17 windows")
    starts, _, hn, rets = _weekly_panel_16w("NVDA", "1045810", "Nvidia")
    ll = LD.lead_lag(hn, rets)
    out = {"windows": len(starts) - 1, "peak": ll, "comparisons": 9,
           "note": f"HN->NVDA: {ll['verdict']} (9-lag search: discovery-grade)"}
    return out, "EXPLORATORY", len(starts) - 1


def e023_filings_vs_chatter() -> tuple[dict, str, int]:
    """H-LEAD-3: filings vs chatter ordering (who moves first?)."""
    from bneck2 import lab as LAB
    from bneck2 import leads as LD
    LAB.preregister(
        "H-LEAD-3", "filings precede chatter",
        "SEC-weekly xcorr peaks at lag>0 vs HN-weekly",
        "peak at lag<=0 (chatter anticipates or syncs filings)",
        "same 17-window panel, both series")
    starts, sec, hn, _ = _weekly_panel_16w("NVDA", "1045810", "Nvidia")
    ll = LD.lead_lag(sec, hn)
    out = {"windows": len(starts) - 1, "peak": ll, "comparisons": 9,
           "note": f"SEC->HN: {ll['verdict']} (9-lag search: discovery-grade)"}
    return out, "EXPLORATORY", len(starts) - 1


def e024_pm_vs_x_order() -> tuple[dict, str, int]:
    """H-LEAD-4 (structural, preregistered): PMs lead X narrative.

    Mechanism: PM prices update on news in minutes (money at risk);
    X threads develop over days (E022 shows HN lags price +3w, and PM
    tracks news-prices faster than narrative). Test when X keyed:
    for dated X claims, compare claim date vs PM price-move date.
    """
    from bneck2 import lab as LAB
    LAB.preregister(
        "H-LEAD-4", "prediction markets lead X narrative",
        "median(PM-move-date minus X-claim-date) < -3 days on >=10 pairs",
        "median >= -3 days (X anticipates or syncs)",
        "PREREGISTERED ONLY: needs keyed X firehose (stockify X-engine)")
    return {"note": "preregistered; blocked on X key funding",
            "proxy_evidence": "E022 HN lags price +3w r=0.69"}, "INCONCLUSIVE", 0


def e025_divergence() -> tuple[dict, str, int]:
    """H-DIV-1: insider buying into price weakness beats buying strength.

    Frontier (Johnsen 2026): divergent insider-bullish (buy vs bearish
    news) +2.46% next-day; convergent already priced. Our proxy for news:
    trailing-20d momentum sign at FILING date (public-info discipline).
    """
    from bneck2 import lab as LAB
    from bneck2 import prices as P
    LAB.preregister(
        "H-DIV-1", "divergent buys beat convergent buys",
        "buys with mom_20<0 outperform buys with mom_20>=0 by >=3pp fwd-20d",
        "no gap (divergence adds nothing)",
        "OpenInsider market-wide buys + Yahoo (filing-dated)")
    rows = _oi_buys_all()
    groups = {"div": [], "conv": []}
    for r in rows:
        t = r.get("ticker", "")
        fd = (r.get("filing_date", "") or "")[:10]
        if not t or len(fd) != 10:
            continue
        cl = {c["date"]: c["close"] for c in P.history(t, "3mo").get("closes", [])}
        ds = sorted(cl)
        i = next((k for k, d in enumerate(ds) if d >= fd), None)
        if i is None or i < 20 or i + 20 >= len(ds):
            continue
        mom = (cl[ds[i]] - cl[ds[i - 20]]) / cl[ds[i]]
        fwd = (cl[ds[i + 20]] - cl[ds[i]]) / cl[ds[i]]
        groups["div" if mom < 0 else "conv"].append(fwd)
    out = {k: {"n": len(v), "mean": round(sum(v) / len(v), 4) if v else None}
           for k, v in groups.items()}
    dm = out["div"]["mean"] if out["div"]["n"] else None
    cm = out["conv"]["mean"] if out["conv"]["n"] else None
    out["note"] = f"divergent {dm} (n={out['div']['n']}) vs convergent {cm} (n={out['conv']['n']})"
    n = out["div"]["n"] + out["conv"]["n"]
    verdict = ("CONFIRMED" if dm is not None and cm is not None and dm - cm >= 0.03
               else "REFUTED" if n >= 10 else "INCONCLUSIVE")
    return out, verdict, n


def e026_predisclosure_drift() -> tuple[dict, str, int]:
    """H-PRE-1: most of the move happens between trade and filing dates
    (Ozlen & Batumoglu 2026: 70-80% pre-disclosure)."""
    from bneck2 import lab as LAB
    from bneck2 import prices as P
    LAB.preregister(
        "H-PRE-1", "pre-disclosure drift dominates",
        "|trade->filing move| > |filing->+5d move| on >=60% of buys",
        "filing-window moves dominate (disclosure is the event)",
        "OpenInsider buy rows with both dates + Yahoo")
    rows = _oi_buys_all()
    pre, post, n = 0.0, 0.0, 0
    for r in rows:
        t = r.get("ticker", "")
        td, fd = (r.get("trade_date", "") or "")[:10], (r.get("filing_date", "") or "")[:10]
        if not t or len(td) != 10 or len(fd) != 10:
            continue
        cl = {c["date"]: c["close"] for c in P.history(t, "3mo").get("closes", [])}
        ds = sorted(cl)
        try:
            i0 = next(k for k, d in enumerate(ds) if d >= td)
            i1 = next(k for k, d in enumerate(ds) if d >= fd)
        except StopIteration:
            continue
        if i1 + 5 >= len(ds):
            continue
        pre += abs((cl[ds[i1]] - cl[ds[i0]]) / cl[ds[i0]]) if cl[ds[i0]] else 0
        post += abs((cl[ds[min(i1 + 5, len(ds) - 1)]] - cl[ds[i1]]) / cl[ds[i1]]) if cl[ds[i1]] else 0
        n += 1
        if n >= 40:
            break
    out = {"n": n, "pre_mean": round(pre / n, 4) if n else None,
           "post_mean": round(post / n, 4) if n else None,
           "note": f"pre-disclosure {pre / n:+.2%} vs post {post / n:+.2%} (n={n})" if n else "no rows"}
    verdict = ("CONFIRMED" if n >= 10 and pre > post
               else "REFUTED" if n >= 10 else "INCONCLUSIVE")
    return out, verdict, n


def e027_espp_filter() -> tuple[dict, str, int]:
    """H-ESP-1: same-date+price clusters are programmatic (Johnsen gates).

    Audit our cluster feed: flag groups where >=80% of qualifying buys
    share date+price, and <$10k singles. Reports contamination rate."""
    from bneck2 import lab as LAB
    from collectors import openinsider as OI
    LAB.preregister(
        "H-ESP-1", "cluster feed contains programmatic blocks",
        ">=1 cluster group meets ESPP signature (>=80% same date+price)",
        "no group meets it (feed is clean)",
        "cluster_buys page rows")
    rows = OI.cluster_buys()
    from collections import Counter
    flagged, total = 0, 0
    for t in {r.get("ticker", "") for r in rows if r.get("ticker")}:
        g = [r for r in rows if r.get("ticker") == t and r.get("value_usd", 0) >= 10000]
        if len(g) < 3:
            continue  # singletons trivially "match" — not a cluster
        total += 1
        keys = Counter((r.get("trade_date", ""), r.get("price", "")) for r in g)
        if keys and max(keys.values()) / len(g) >= 0.8:
            flagged += 1
    out = {"groups": total, "flagged": flagged,
           "note": f"{flagged}/{total} cluster groups look programmatic"}
    return out, ("CONFIRMED" if flagged > 0 else "REFUTED"), total


def e028_distance_high() -> tuple[dict, str, int]:
    """H-DH-1: buys nearer 52w highs do better (microcap paper: 36% weight).

    Pilot on market-wide buy rows: split by distance-from-high terciles,
    compare forward-20d means."""
    from bneck2 import lab as LAB
    from bneck2 import prices as P
    LAB.preregister(
        "H-DH-1", "distance-from-high sorts buy outcomes",
        "top-tercile (nearest high) beats bottom by >=3pp fwd-20d",
        "no ordering (distance is noise here)",
        "OpenInsider buys + Yahoo 1y highs, filing-dated")
    rows = _oi_buys_all()
    scored = []
    cache = {}
    for r in rows:
        t = r.get("ticker", "")
        fd = (r.get("filing_date", "") or "")[:10]
        if not t or len(fd) != 10:
            continue
        if t not in cache:
            cache[t] = {c["date"]: c["close"] for c in P.history(t, "1y").get("closes", [])}
        cl = cache[t]
        ds = sorted(cl)
        i = next((k for k, d in enumerate(ds) if d >= fd), None)
        if i is None or i + 20 >= len(ds) or i < 200:
            continue
        hi = max(c for d, c in cl.items() if d <= ds[i])
        dist = (cl[ds[i]] - hi) / hi if hi else 0
        fwd = (cl[ds[i + 20]] - cl[ds[i]]) / cl[ds[i]]
        scored.append((dist, fwd))
        if len(scored) >= 60:
            break
    if len(scored) < 9:
        return {"note": "insufficient buy rows with history", "n": len(scored)}, "INCONCLUSIVE", len(scored)
    scored.sort()
    k = max(len(scored) // 3, 1)
    lo = sum(s[1] for s in scored[:k]) / k
    hi = sum(s[1] for s in scored[-k:]) / k
    out = {"n": len(scored), "near_high": round(hi, 4), "far_high": round(lo, 4),
           "note": f"near-high {hi:+.1%} vs far {lo:+.1%} (n={len(scored)})"}
    return out, ("CONFIRMED" if hi - lo >= 0.03 else "REFUTED"), len(scored)


def e029_deep_screen() -> tuple[dict, str, int]:
    """H-DEEP-1: factor ICs on 2y weekly panel (train first 3/4)."""
    from bneck2 import lab as LAB
    from bneck2 import predict as PD
    LAB.preregister(
        "H-DEEP-1", "deep screen finds IC>0.1 factors",
        ">=2 factors clear |IC|>0.1 with n>=100 on train split",
        "fewer than 2 (no structure at weekly grid)",
        "deep-weekly.jsonl; train first 78w, no holdout touch")
    rows = [r for r in _deep_rows() if r.get("fwd_20") is not None]
    dates = sorted({r["date"] for r in rows})
    cut = dates[3 * len(dates) // 4]
    train = [r for r in rows if r["date"] < cut]
    scr = PD.screen(train, DEEP_FACTORS)
    winners = [s["factor"] for s in scr
               if s["IC"] is not None and abs(s["IC"]) > 0.1 and s["n"] >= 100]
    out = {"train_screen": scr, "winners": winners, "n_train": len(train),
           "note": f"winners={winners}"}
    return out, ("CONFIRMED" if len(winners) >= 2 else "REFUTED"), len(train)

def e030_deep_walkforward() -> tuple[dict, str, int]:
    """H-DEEP-2: composite beats buy-hold AND momentum on holdout quarter."""
    from bneck2 import backtest as BT
    from bneck2 import lab as LAB
    from bneck2 import predict as PD
    LAB.preregister(
        "H-DEEP-2", "composite beats bogeys on holdout",
        "composite Sharpe > max(buyhold, momentum) on last 26w",
        "composite <= best bogey",
        "deep-weekly.jsonl; winners/signs from train only")
    rows = [r for r in _deep_rows() if r.get("fwd_20") is not None]
    dates = sorted({r["date"] for r in rows})
    cut = dates[3 * len(dates) // 4]
    train = [r for r in rows if r["date"] < cut]
    hold = [r for r in rows if r["date"] >= cut]
    scr = PD.screen(train, DEEP_FACTORS)
    winners = [s["factor"] for s in scr
               if s["IC"] is not None and abs(s["IC"]) > 0.1 and s["n"] >= 100]
    signs = {s["factor"]: 1.0 if (s["IC"] or 0) >= 0 else -1.0 for s in scr}
    if not winners:
        return {"note": "no winners (see E029)", "winners": []}, "REFUTED", len(train)
    comp = PD.composite_by_date([dict(r) for r in hold], winners, signs)
    mom = [{"date": r["date"], "ticker": r["ticker"],
            "score": r.get("f_mom_20") or 0.0,
            "forward_return": r["fwd_20"]} for r in hold]
    uni = [{"date": r["date"], "ticker": r["ticker"], "score": 1.0,
            "forward_return": r["fwd_20"]} for r in hold]

    def _wf(rs):
        ok = []
        for r in rs:
            fr = r.get("forward_return", r.get("fwd_20"))
            if fr is not None:
                ok.append(dict(r, forward_return=fr))
        return BT.walk_forward(ok, quantile=0.25)[1] if ok else {"sharpe": None}

    cs, ms, us = _wf(comp), _wf(mom), _wf(uni)
    out = {"winners": winners, "holdout_n": len(hold),
           "composite_sharpe": cs.get("sharpe"),
           "momentum_sharpe": ms.get("sharpe"),
           "buyhold_sharpe": us.get("sharpe"),
           "note": f"comp {cs.get('sharpe')} vs mom {ms.get('sharpe')} vs bh {us.get('sharpe')}"}
    ok = (cs.get("sharpe") is not None and ms.get("sharpe") is not None
          and us.get("sharpe") is not None
          and cs["sharpe"] > max(ms["sharpe"], us["sharpe"]) and len(hold) >= 60)
    return out, ("CONFIRMED" if ok else "REFUTED"), len(hold)


def e031_momentum_only() -> tuple[dict, str, int]:
    """H-DEEP-3 (mutate): sole survivor (momentum IC 0.147) vs buy-hold."""
    from bneck2 import backtest as BT
    from bneck2 import lab as LAB
    LAB.preregister(
        "H-DEEP-3", "momentum-only beats buy-hold on holdout",
        "momentum Sharpe > buyhold Sharpe, last 26w, n>=60",
        "momentum <= buyhold (no timing edge at weekly grid)",
        "deep-weekly.jsonl; parent H-DEEP-2 (no composite survived)")
    import json as _j
    rows = [_j.loads(l) for l in
            (ROOT / "data" / "predict" / "deep-weekly.jsonl")
            .read_text(encoding="utf-8").splitlines() if l.strip()]
    rows = [r for r in rows if r.get("fwd_20") is not None]
    dates = sorted({r["date"] for r in rows})
    hold = [r for r in rows if r["date"] >= dates[3 * len(dates) // 4]]
    mom = [{"date": r["date"], "ticker": r["ticker"],
            "score": r.get("f_mom_20") or 0.0,
            "forward_return": r["fwd_20"]} for r in hold]
    uni = [{"date": r["date"], "ticker": r["ticker"], "score": 1.0,
            "forward_return": r["fwd_20"]} for r in hold]

    def _wf(rs):
        return BT.walk_forward(
            [dict(r, forward_return=r["forward_return"]) for r in rs],
            quantile=0.25)[1]

    ms, us = _wf(mom), _wf(uni)
    # subperiod stability: split holdout halves
    ds = sorted({r["date"] for r in hold})
    halves = []
    for part in (ds[:len(ds) // 2], ds[len(ds) // 2:]):
        sub = [r for r in mom if r["date"] in part]
        halves.append(_wf(sub).get("sharpe"))
    out = {"momentum_sharpe": ms.get("sharpe"),
           "buyhold_sharpe": us.get("sharpe"),
           "half_sharpes": halves, "n": len(hold),
           "note": f"mom {ms.get('sharpe')} vs bh {us.get('sharpe')}; halves {halves}"}
    ok = (ms.get("sharpe") is not None and us.get("sharpe") is not None
          and ms["sharpe"] > us["sharpe"] and len(hold) >= 60)
    return out, ("CONFIRMED" if ok else "REFUTED"), len(hold)


def e032_nvda_basket() -> tuple[dict, str, int]:
    """H-NVDA-1b: NVDA 13F basket (equal-weight publics) vs SPY from 6/30."""
    from bneck2 import lab as LAB
    from bneck2 import prices as P
    LAB.preregister(
        "H-NVDA-1b", "NVDA-validated names drift up",
        "13F public basket beats SPY from 2026-06-30 filing window",
        "basket <= SPY (validation followed, not predictive)",
        "hand-seeded 13F (XML host-blocked) + Yahoo")
    import json as _j
    doc = _j.loads((ROOT / "data" / "universe" / "nvda_13f_2026q2.json").read_text())
    names = [p_ for p_ in doc["positions"] if p_.get("ticker")]
    rets = {}
    for p_ in names:
        cl = {c["date"]: c["close"] for c in P.history(p_["ticker"], "6mo").get("closes", [])}
        ds = sorted(cl)
        i = next((k for k, d in enumerate(ds) if d >= "2026-06-30"), None)
        if i is not None and ds:
            j = len(ds) - 1
            rets[p_["ticker"]] = round((cl[ds[j]] - cl[ds[i]]) / cl[ds[i]], 4)
    sp = {c["date"]: c["close"] for c in P.history("SPY", "6mo").get("closes", [])}
    sds = sorted(sp)
    si = next((k for k, d in enumerate(sds) if d >= "2026-06-30"), None)
    spy = round((sp[sds[-1]] - sp[sds[si]]) / sp[sds[si]], 4) if si is not None else None
    vals = list(rets.values())
    m = round(sum(vals) / len(vals), 4) if vals else None
    out = {"basket": rets, "basket_mean": m, "spy": spy, "n": len(vals),
           "note": f"13F basket {m} vs SPY {spy} since 6/30 (n={len(vals)})"}
    verdict = ("CONFIRMED" if m is not None and spy is not None and m - spy >= 0.05
               else "REFUTED" if m is not None and spy is not None else "INCONCLUSIVE")
    return out, verdict, len(vals)


def e033_x_calls() -> tuple[dict, str, int]:
    """H-X-1: X directional calls beat always-long baseline."""
    from bneck2 import lab as LAB
    LAB.preregister(
        "H-X-1", "X calls beat always-long",
        "mean 5d abnormal (vs SPY-matched dates) > 0 with n>=50",
        "mean <= 0 (calls add nothing)",
        "data/x/x_outcomes.json (5 handles, 90d histories)")
    import json as _j
    fp = ROOT / "data" / "x" / "x_outcomes.json"
    try:
        rows = _j.loads(fp.read_text())
    except (OSError, ValueError):
        return {"note": "no outcomes; run scripts/x_backtest.py"}, "INCONCLUSIVE", 0
    d5 = [r for r in rows if r["horizon"] == "d5"]
    n = len(d5)
    m = sum(r["ret"] for r in d5) / n if n else 0.0
    by_h = {}
    for r in d5:
        by_h.setdefault(r["handle"], []).append(r["ret"])
    by_h = {h: (len(v), round(sum(v) / len(v), 4)) for h, v in by_h.items()}
    out = {"n": n, "mean_5d": round(m, 4), "by_handle": by_h,
           "note": f"X calls 5d mean {m:+.2%} (n={n})"}
    verdict = ("CONFIRMED" if n >= 50 and m > 0.005 else "REFUTED"
               if n >= 50 else "INCONCLUSIVE")
    return out, verdict, n


def e034_kalshi_momentum() -> tuple[dict, str, int]:
    """H-KAL-1: Kalshi 7d candle momentum persists next 7d (pm velocity)."""
    from bneck2 import lab as LAB
    from collectors import kalshi as KL
    LAB.preregister(
        "H-KAL-1", "kalshi momentum persists week-over-week",
        "sign(7d momentum) matches sign(next 7d move) on >=60% of windows",
        "hit < 60% (pm prices random-walk at weekly grid)",
        "30d daily candles, top-3 liquid markets")
    import time as _t
    mkts = sorted(KL.fetch_markets("artificial intelligence")
                  + KL.fetch_markets("nuclear power")
                  + KL.fetch_markets("robot"),
                  key=lambda m: -(m.get("liquidity", 0) + m.get("volume", 0)))[:3]
    now = int(_t.time())
    hits, n, detail = 0, 0, []
    for m in mkts:
        if not m.get("series") or not m.get("ticker"):
            continue
        cs = KL.fetch_candles(m["series"], m["ticker"], now - 30 * 86400, now)
        closes = [c["close"] for c in cs if c.get("close") is not None]
        if len(closes) < 21:
            continue
        mom = closes[-8] - closes[-15] if len(closes) >= 15 else 0
        fwd = closes[-1] - closes[-8]
        n += 1
        hit = (mom > 0) == (fwd > 0) and mom != 0
        hits += hit
        detail.append({"q": m["question"][:50], "hit": hit})
    out = {"n": n, "hits": hits, "detail": detail,
           "note": f"kalshi momentum {hits}/{n} carry"}
    verdict = ("CONFIRMED" if n >= 5 and hits / n >= 0.6 else "REFUTED"
               if n >= 5 else "INCONCLUSIVE")
    return out, verdict, n


def e035_attribution() -> tuple[dict, str, int]:
    """H-ATT-1: leave-one-out attribution of the long tilt (E017 flip)."""
    from bneck2 import lab as LAB
    from bneck2 import predict as PD
    LAB.preregister(
        "H-ATT-1", "tilt driven by few names, not a factor",
        "dropping <=3 tickers flips the sign of mean excess",
        "sign survives all single drops (broad factor, not luck)",
        "biweekly 30-ticker panel")
    import json as _j
    rows = []
    for f in sorted((ROOT / "data" / "predict").glob("biwk-*.jsonl")):
        rows += [_j.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    rows = [r for r in rows if r.get("fwd_20") is not None]
    dates = sorted({r["date"] for r in rows})
    cut = dates[max(len(dates) - 8, 0)]
    hold = [r for r in rows if r["date"] >= cut]
    train = [r for r in rows if r["date"] < cut]
    scr = PD.screen(train)
    winners = [s["factor"] for s in scr
               if s["IC"] is not None and abs(s["IC"]) > 0.1 and s["n"] >= 40]
    signs = {s["factor"]: 1.0 if (s["IC"] or 0) >= 0 else -1.0 for s in scr}
    scored = PD.composite_by_date(hold, winners or ["f_mom_20"], signs)
    by_date = {}
    for r in scored:
        by_date.setdefault(r["date"], []).append(r)

    def _excess(rs):
        ex = []
        for d in sorted(by_date):
            g = sorted(by_date[d], key=lambda r: -r["score"]) if rs is None else                 sorted([r for r in by_date[d] if r["ticker"] not in rs],
                       key=lambda r: -r["score"])
            k = max(len(g) // 3, 1)
            ex.append(sum(r["fwd_20"] for r in g[:k]) / k
                      - sum(r["fwd_20"] for r in g) / len(g))
        return round(sum(ex) / len(ex), 4) if ex else None

    base = _excess(None)
    tickers = sorted({r["ticker"] for r in hold})
    drops = {}
    for t in tickers:
        drops[t] = _excess({t})
    out = {"base_excess": base, "n_tickers": len(tickers),
           "worst_drops": sorted(drops.items(), key=lambda kv: kv[1] or 0)[:3],
           "best_drops": sorted(drops.items(), key=lambda kv: kv[1] or 0)[-3:],
           "note": f"base {base}; dropping changes outcomes, see extremes"}
    flip = any((d or 0) > 0 for d in drops.values())
    return out, ("CONFIRMED" if flip else "REFUTED"), len(tickers)


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
    "E014": e014_signal_chain,
    "E015": e015_signal_biweekly,
    "E016": e016_burst_reversal,
    "E017": e017_long_only,
    "E018": e018_nvda_sell_drift,
    "E019": e019_btc_nvda_beta,
    "E020": e020_btc_pm_snapshot,
    "E021": e021_sec_leads_price,
    "E022": e022_hn_leads_price,
    "E023": e023_filings_vs_chatter,
    "E024": e024_pm_vs_x_order,
    "E025": e025_divergence,
    "E026": e026_predisclosure_drift,
    "E027": e027_espp_filter,
    "E028": e028_distance_high,
    "E029": e029_deep_screen,
    "E030": e030_deep_walkforward,
    "E031": e031_momentum_only,
    "E032": e032_nvda_basket,
    "E033": e033_x_calls,
    "E034": e034_kalshi_momentum,
    "E035": e035_attribution,
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








def _weekly_panel_16w(ticker: str, cik: str, hn_query: str):
    """16 weekly buckets ending last Friday: SEC counts, HN counts, returns."""
    import datetime as _dt
    from bneck2 import leads as LD
    from bneck2 import prices as P
    from bneck2 import predict as PD
    from collectors import hn as HN
    today = _dt.date.today()
    fri = today - _dt.timedelta(days=(today.weekday() - 4) % 7)
    starts = [(fri - _dt.timedelta(weeks=k)).isoformat() for k in range(16, -1, -1)]
    doc = PD.submissions(cik)
    fl = (doc.get("filings") or {}).get("recent") or {}
    sec_dates = [d for f, d in zip(fl.get("form", []), fl.get("filingDate", []))
                 if f in ("4", "8-K", "13D", "13G") and d]
    sec = LD.bucketize(sec_dates, starts)
    hn_counts = []
    import calendar
    for i in range(len(starts)):
        lo = starts[i]
        hi = (fri if i == len(starts) - 1 else None)
        try:
            import urllib.parse, urllib.request, json as _j
            lo_ts = calendar.timegm(_dt.datetime.fromisoformat(lo).timetuple())
            hi_s = (fri if i == len(starts) - 1 else
                    _dt.date.fromisoformat(starts[i + 1])).isoformat()
            hi_ts = calendar.timegm(_dt.datetime.fromisoformat(hi_s).timetuple())
            url = ("https://hn.algolia.com/api/v1/search?" + urllib.parse.urlencode(
                {"query": hn_query, "tags": "story",
                 "numericFilters": f"created_at_i>{lo_ts},created_at_i<{hi_ts}",
                 "hitsPerPage": 100}))
            req = urllib.request.Request(url, headers={"User-Agent": "bneck"})
            with urllib.request.urlopen(req, timeout=20) as r:
                hn_counts.append(int(_j.loads(r.read().decode("utf-8", "replace")).get("nbHits", 0)))
        except Exception:
            hn_counts.append(0)
    cl = {c["date"]: c["close"] for c in P.history(ticker, "6mo").get("closes", [])}
    rets = []
    for i in range(len(starts)):
        w = [c for d, c in sorted(cl.items()) if starts[i] <= d < (starts[i + 1] if i + 1 < len(starts) else "9999")]
        rets.append(round((w[-1] - w[0]) / w[0], 4) if len(w) >= 2 and w[0] else 0.0)
    return starts, sec, hn_counts, rets




def _oi_buys_all(limit_pages: int = 1):
    """Market-wide buy rows (cluster + officer + latest), filing-dated."""
    from collectors import openinsider as OI
    rows = []
    for fn in (OI.cluster_buys, OI.officer_buys):
        try:
            rows += fn()
        except Exception:
            pass
    return [r for r in rows if r.get("is_buy")]



DEEP_FACTORS = ["f_mom_20", "f_burst", "f_short", "f_hn"]


def _deep_rows():
    import json as _j
    fp = ROOT / "data" / "predict" / "deep-weekly.jsonl"
    try:
        return [_j.loads(l) for l in fp.read_text(encoding="utf-8").splitlines() if l.strip()]
    except (OSError, ValueError):
        return []




