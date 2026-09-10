"""bneck2 killfeed — collectors -> verdict writers (build-queue #1-3).

Wires what SYSTEM-SPEC listed as unwired:
  1. kill-observations writer <- SEC filings (burst) + OpenAlex (attack)
  2. OpenAlex velocity per node -> AttackIntensity numbers
  3. polymarket pm-clock reads -> belief claims + evidence signals

Design rules (do not weaken):
  - All evaluation is pure + deterministic on fetched docs. Tests use
    fixtures; no network in tests.
  - Collectors never raise (return [] / {}); killfeed skips missing inputs
    and logs INCONCLUSIVE rather than inventing data.
  - Nothing below digger L4 touches kill verdicts — this module writes
    *observations* (TRIGGERED / NOT TRIGGERED / INCONCLUSIVE). Promotion to
    kill_signals stays in updater/quant gates.
  - SEC UA must stay descriptive (data.sec.gov blocks contact@localhost-style
    anonymity; see collectors/sec.py UA).

Thresholds live in THRESHOLDS (one place, auditable).
"""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from bneck2 import evidence as E
from bneck2 import graph as G

BASELINES_PATH = ROOT / "data" / "beliefs" / "sec_baselines.json"
BASELINE_KEEP = 30

THRESHOLDS = {
    # SEC burst inside one poll window
    "sec_form4_burst": 5,     # >=5 insider Form 4s across node tickers
    "sec_deal_burst": 2,      # >=2 8-K / 13D / 13G across node tickers
    # OpenAlex attack intensity on trailing window
    "attack_growth": 1.0,     # >=100% growth recent-2y avg vs prior-2y avg
    "attack_total": 200,      # and >=200 total works in window
    # Polymarket reliability by book quality (mirrors collectors/polymarket.py)
    "pm_reliability": {"high-liquidity": 0.82, "mid-liquidity": 0.60,
                       "low-liquidity": 0.50},
}

# Ticker -> SEC CIK for node tickers we actually poll. Missing tickers are
# NOT guessed — they go to the unknowns ledger (see ensure_cik_coverage).
CIK_MAP = {
    "MU": "1430265",
    "NVDA": "1045810",
    "INTC": "50863",
    "AMD": "2488",
    "IONQ": "1527467",
    "RGTI": "1524447",
    "FORM": "103939",
    "KEYS": "1601046",
    "GFS": "1709048",
    "COHR": "820479",
    "LITE": "1301239",
    "AVGO": "1730168",
    "GOOGL": "1652044",
    "META": "1326801",
}


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# Nodes whose graph labels are not literature vocabulary get an explicit,
# auditable query override (label kept as-is; only the search string changes).
QUERY_OVERRIDES = {
    "quantum_ip": "quantum computing patents",
}


def short_query(label: str) -> str:
    """Searchable query: strip parentheticals/lists, keep the head clause."""
    head = (label or "").split("(")[0].split(":")[0]
    head = head.split(",")[0] if len(head.split(",")[0].split()) >= 2 else head
    return " ".join(head.split()).strip() or (label or "")


# Polymarket query overrides: node labels return loose earnings-call
# markets, so map to topical liquid queries (probed 2026-09-10; Gamma has
# no full-text search, matching is keyword-side). Re-probe periodically.
PM_QUERY_OVERRIDES = {
    "accelerators": "artificial intelligence",
    "trap_ion_qc": "quantum computer",
    "quantum_ip": "quantum computer",
    "power": "nuclear power",
    "memory_hbm": "semiconductor",
    "memory_dram": "semiconductor",
    "packaging": "semiconductor",
    "storage": "data center",
    "optical_io": "data center",
    "motors": "robot",
    "reducers": "robot",
    "encoders": "robot",
    "bearings": "robot",
    "torque_sensing": "robot",
}


def node_queries(node: dict) -> dict:
    """Live-query strings derived from the node (no hand lists to rot)."""
    nid = node.get("id", "")
    oa = QUERY_OVERRIDES.get(nid,
                             short_query(node.get("label", nid)))
    pm = PM_QUERY_OVERRIDES.get(nid, short_query(node.get("label", nid)))
    return {"openalex": oa, "polymarket": pm}


def ensure_cik_coverage(nodes: list[dict]) -> list[str]:
    """Tickers on graph nodes with no CIK entry -> unknowns ledger + return.
    Idempotent: skips subjects already open."""
    known = {u.get("subject", "") for u in E.read_unknowns(open_only=False)}
    open_subjects = {u.get("subject", "") for u in E.read_unknowns()}
    missing: list[str] = []
    for n in nodes:
        for t in n.get("tickers", []):
            if t and t not in CIK_MAP and t not in missing:
                missing.append(t)
    for t in missing:
        if f"SEC CIK for {t}" not in known:
            E.add_unknown(subject=f"SEC CIK for {t}",
                          sought="10-digit CIK for submissions JSON polling",
                          searched="bneck2/killfeed.py CIK_MAP",
                          would_close_it=f"Form 4 / 8-K burst coverage for {t}")
    return missing


def attack_intensity(velocity: dict) -> dict:
    """AttackIntensity numbers from one OpenAlex velocity page.

    growth = recent-2y mean / prior-2y mean - 1 over per_year counts.
    tier HIGH needs both growth and mass (no hype without a literature).
    """
    per_year = velocity.get("per_year", {}) or {}
    years = sorted(int(y) for y in per_year if str(y).isdigit())
    counts = [int(per_year.get(y, per_year.get(str(y), 0))) for y in years]
    growth = 0.0
    if len(counts) >= 4:
        recent = sum(counts[-2:]) / 2.0
        prior = sum(counts[-4:-2]) / 2.0
        growth = (recent / prior - 1.0) if prior > 0 else 0.0
    total = int(velocity.get("total_works", 0))
    tier = ("HIGH" if growth >= THRESHOLDS["attack_growth"]
            and total >= THRESHOLDS["attack_total"] else "normal")
    return {"growth": round(growth, 3), "total": total, "tier": tier,
            "years_seen": len(years)}


def _attack_rows(nid: str, ts: str, velocity: dict) -> list[dict]:
    a = attack_intensity(velocity)
    return [{"ts": ts, "node_id": nid,
             "signal": "openalex-attack(growth>=%.1f,total>=%d)"
             % (THRESHOLDS["attack_growth"], THRESHOLDS["attack_total"]),
             "measured": f"growth={a['growth']} total={a['total']}",
             "threshold": "HIGH needs growth AND mass",
             "verdict": "TRIGGERED" if a["tier"] == "HIGH" else "NOT TRIGGERED",
             "source": "openalex"}]


def sec_burst(all_filings: list[dict], baseline: dict | None = None) -> dict:
    """Burst counts across one node's ticker filings (one poll window).

    Verdict stays absolute (gates depend on it). When a baseline
    {med_form4, med_deal} is supplied, measured carries vs_base ratios so
    routine-cadence names (NVDA files constantly) read differently from
    genuine inflections. Calibration note, not verdict."""
    forms = [f.get("form", "") for f in all_filings]
    n4 = sum(1 for x in forms if x == "4")
    deal = sum(1 for x in forms if x in ("8-K", "13D", "13G"))
    out: dict = {"form4": n4, "deal": deal, "n": len(forms),
                 "form4_burst": n4 >= THRESHOLDS["sec_form4_burst"],
                 "deal_burst": deal >= THRESHOLDS["sec_deal_burst"]}
    if baseline:
        mf = max(float(baseline.get("med_form4", 0)), 0.5)
        md = max(float(baseline.get("med_deal", 0)), 0.5)
        out["vs_base"] = f"{n4 / mf:.1f}x/{deal / md:.1f}x"
    return out


def load_baselines(path: Path = BASELINES_PATH) -> dict:
    try:
        import json as _j
        return _j.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def record_baselines(counts: dict[str, dict], ts: str,
                     path: Path = BASELINES_PATH) -> dict:
    """counts: ticker -> {form4, deal}. Appends, caps history. Returns medians."""
    import json as _j
    try:
        doc = _j.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        doc = {}
    for t, c in counts.items():
        hist = doc.setdefault(t, [])
        hist.append({"ts": ts, "form4": c["form4"], "deal": c["deal"]})
        del hist[:-BASELINE_KEEP]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_j.dumps(doc, indent=1), encoding="utf-8")
    return baseline_medians(doc)


def baseline_medians(doc: dict) -> dict[str, dict]:
    med: dict[str, dict] = {}
    for t, hist in doc.items():
        if not hist:
            continue
        f4 = sorted(h["form4"] for h in hist)
        dl = sorted(h["deal"] for h in hist)
        med[t] = {"med_form4": float(f4[len(f4) // 2]),
                  "med_deal": float(dl[len(dl) // 2]), "n": len(hist)}
    return med


def pm_reading(markets: list[dict]) -> dict | None:
    """Best-book market read: (p, tier, reliability). Never p alone."""
    if not markets:
        return None
    best = max(markets, key=lambda m: (float(m.get("liquidity", 0)),
                                       float(m.get("volume", 0))))
    tier = best.get("tier") or "low-liquidity"
    rel = THRESHOLDS["pm_reliability"].get(tier, 0.50)
    depth_note = ""
    if best.get("venue") == "polymarket" and best.get("conditionId"):
        try:
            from collectors import clob as _CLOB
            import json as _j
            import urllib.request as _u
            req = _u.Request(
                "https://gamma-api.polymarket.com/markets?condition_id="
                + best["conditionId"], headers={"User-Agent": "bneck"})
            with _u.urlopen(req, timeout=15) as _r:
                _det = _j.loads(_r.read().decode("utf-8", "replace"))
            tids = _j.loads((_det[0].get("clobTokenIds") or "[]")) if _det else []
            if tids:
                book = _CLOB.book(str(tids[0]))
                depth_note = (f" depth=${book.get('depth_top5', 0):,.0f}"
                              f" spread={book.get('spread')}")
                if book.get("depth_top5", 0) >= 1_000_000:
                    rel = min(rel + 0.1, 0.95)
                if (book.get("spread") or 0) > 0.2:
                    rel = max(rel - 0.1, 0.3)
        except Exception:
            pass
    return {"question": best.get("question", "")[:160],
            "p": float(best.get("p", 0.0)), "tier": tier,
            "venue": best.get("venue", "?") + depth_note,
            "reliability": rel}


def evaluate(node: dict, sec: list[dict] | None = None,
             velocity: dict | None = None,
             markets: list[dict] | None = None,
             ts: str = "", sec_baseline: dict | None = None) -> list[dict]:
    """Pure evaluation -> verdict rows (NOT yet written)."""
    nid = node.get("id", "?")
    ts = ts or utcnow()
    rows: list[dict] = []
    if sec is not None:
        b = sec_burst(sec, sec_baseline)
        fired = b["form4_burst"] or b["deal_burst"]
        measured = f"form4={b['form4']} deal={b['deal']} n={b['n']}"
        if "vs_base" in b:
            measured += f" vs_base={b['vs_base']}"
        rows.append({"ts": ts, "node_id": nid,
                     "signal": "sec-burst(Form4>=%d,deal>=%d)"
                     % (THRESHOLDS["sec_form4_burst"],
                        THRESHOLDS["sec_deal_burst"]),
                     "measured": measured,
                     "threshold": "burst on either leg",
                     "verdict": "TRIGGERED" if fired else "NOT TRIGGERED",
                     "source": "sec-edgar"})
    if velocity is not None:
        if not velocity.get("ok", True):
            rows.append({"ts": ts, "node_id": nid,
                         "signal": "openalex-attack(growth>=%.1f,total>=%d)"
                         % (THRESHOLDS["attack_growth"],
                            THRESHOLDS["attack_total"]),
                         "measured": "fetch failed",
                         "threshold": "HIGH needs growth AND mass",
                         "verdict": "INCONCLUSIVE",
                         "source": "openalex"})
        else:
            rows.extend(_attack_rows(nid, ts, velocity))
    if markets is not None:
        r = pm_reading(markets)
        if r is None:
            rows.append({"ts": ts, "node_id": nid, "signal": "pm-clock",
                         "measured": "no markets returned",
                         "threshold": "any book", "verdict": "INCONCLUSIVE",
                         "source": "polymarket"})
        else:
            rows.append({"ts": ts, "node_id": nid, "signal": "pm-clock",
                         "measured": f"p={r['p']} {r['tier']} "
                         f"{r.get('venue', '?')} rel={r['reliability']}: "
                         f"{r['question']}",
                         "threshold": "best-book read, never p alone",
                         "verdict": "NOT TRIGGERED",
                         "source": "polymarket",
                         "_emit_signal": {"type": "PM_CLOCK", "direction": 0,
                                          "strength": r["p"],
                                          "confidence": r["reliability"]}})
            # Whale consensus on the best-book market only (1 holders call).
            best_mkt = next((m for m in (markets or [])
                             if (m.get("question") or "")[:160] == r["question"]
                             and m.get("conditionId")), None)
            if best_mkt is not None:
                try:
                    from collectors import polywhale as PW
                    for c in PW.consensus([best_mkt])[:1]:
                        rows[-1].setdefault("_extra_signals", []).append(
                            {"type": "WHALE_CONSENSUS", "direction": 0,
                             "strength": min(1.0, c["total_usd"] / 50000.0),
                             "confidence": round(0.55 + 0.05 * min(c["n_wallets"], 5), 2),
                             "note": f"{c['n_wallets']} whales ${c['total_usd']:,.0f} "
                             f"outcome={c['outcome']}: {c['question']}"})
                except Exception:
                    pass
    return rows


def write_rows(rows: list[dict]) -> int:
    n = 0
    for r in rows:
        E.log_kill_observation(r["node_id"], r["signal"], r["measured"],
                               r["threshold"], r["verdict"],
                               source=r.get("source", ""), ts=r.get("ts", ""))
        n += 1
        sig = r.pop("_emit_signal", None)
        if sig:
            E.log_signal(r["node_id"], sig["type"], sig["direction"],
                         sig["strength"], sig["confidence"],
                         source=r.get("source", ""), ts=r.get("ts", ""))
        for extra in r.pop("_extra_signals", []) or []:
            E.log_signal(r["node_id"], extra["type"], extra["direction"],
                         extra["strength"], extra["confidence"],
                         source=r.get("source", "")
                         + ("|" + extra["note"] if extra.get("note") else ""),
                         ts=r.get("ts", ""))
    return n


def run(live: bool = False, write: bool = True,
        max_nodes: int = 0, sleep_s: float = 1.0) -> dict:
    """The loop. live=False evaluates nothing (no caches yet) but still
    ensures CIK coverage unknowns. live=True collects per node, best-effort,
    then evaluates + writes verdicts. Returns a summary dict."""
    g = G.load_graph()
    nodes = g.get("nodes", [])
    if max_nodes:
        nodes = nodes[:max_nodes]
    missing_ciks = ensure_cik_coverage(g.get("nodes", []))
    summary = {"nodes": len(nodes), "missing_ciks": missing_ciks,
               "verdicts": 0, "triggered": [], "live": live}
    if not live:
        return summary
    from collectors import sec as SEC
    from collectors import openalex as OA
    from collectors import polymarket as PM
    from collectors import kalshi as KL
    from bneck2 import migration as MIG
    from bneck2 import quant as Q
    run_ts = utcnow()
    readings = Q.load_readings()
    medians = baseline_medians(load_baselines())
    ticker_counts: dict[str, dict] = {}
    for n in nodes:
        filings: list[dict] = []
        for t in n.get("tickers", []):
            cik = CIK_MAP.get(t)
            if cik:
                got = SEC.fetch_recent_filings(cik)
                f4 = sum(1 for f in got if f.get("form") == "4")
                dl = sum(1 for f in got if f.get("form") in ("8-K", "13D", "13G"))
                ticker_counts[t] = {"form4": f4, "deal": dl}
                filings.extend(got)
                time.sleep(0.2)
        node_base = None
        tick_meds = [medians[t] for t in n.get("tickers", []) if t in medians]
        if tick_meds:
            node_base = {
                "med_form4": sum(m["med_form4"] for m in tick_meds) / len(tick_meds),
                "med_deal": sum(m["med_deal"] for m in tick_meds) / len(tick_meds)}
        q = node_queries(n)
        vel = OA.fetch_yearly(q["openalex"])
        time.sleep(sleep_s)
        mkts = PM.fetch_markets(q["polymarket"])
        for m in mkts:
            m.setdefault("venue", "polymarket")
        time.sleep(sleep_s)
        try:
            mkts = mkts + KL.fetch_markets(q["polymarket"])
        except Exception:
            pass
        time.sleep(sleep_s)
        rows = evaluate(n, sec=filings, velocity=vel, markets=mkts,
                        sec_baseline=node_base)
        if write:
            summary["verdicts"] += write_rows(rows)
            sev = MIG.severity(n, readings.get(n.get("id", "")))
            MIG.record_severity(n.get("id", "?"), sev["B"], run_ts)
        summary["triggered"].extend(
            f"{n.get('id')}:{r['signal']}" for r in rows
            if r["verdict"] == "TRIGGERED")
    if live and write and ticker_counts:
        summary["baselines"] = record_baselines(ticker_counts, run_ts)
    return summary


def render_summary(summary: dict) -> str:
    lines = [f"# killfeed loop — live={summary['live']} "
             f"nodes={summary['nodes']} verdicts={summary['verdicts']}"]
    if summary["missing_ciks"]:
        lines.append("CIKs missing (unknowns ledger): "
                     + ", ".join(summary["missing_ciks"]))
    if summary["triggered"]:
        lines.append("TRIGGERED:")
        lines.extend(f"  !! {t}" for t in summary["triggered"])
    else:
        lines.append("no TRIGGERED verdicts this pass.")
    return "\n".join(lines)
