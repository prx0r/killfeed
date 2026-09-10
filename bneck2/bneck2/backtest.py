"""bneck2 backtest — leakage-safe walk-forward, stdlib port of the vendored
postagi_kernel/backtest.py (which needs numpy/pandas).

Same protocol (Agentic-Trading-survey response): score knowable at `date`,
forward_return realized after; per-date rebalance; turnover-charged costs;
no same-period look-ahead. Rows are plain dicts:
  {date, ticker, score, forward_return}

Live panel accumulation (data/backtest/panel.jsonl): oneclick appends
score snapshots per pass; forward returns fill in once closes exist;
walk_forward runs only on complete dates. Until then: INSUFFICIENT.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PANEL_PATH = ROOT / "data" / "backtest" / "panel.jsonl"


def make_positions(scores: dict[str, float], quantile: float = 0.2,
                   gross: float = 1.0) -> dict[str, float]:
    if not 0 < quantile < 0.5:
        raise ValueError("quantile must be in (0,.5)")
    order = sorted(scores, key=lambda t: scores[t])
    n = max(1, int(len(order) * quantile))
    pos = {t: 0.0 for t in order}
    for t in order[:n]:
        pos[t] = -gross / (2 * n)
    for t in order[-n:]:
        pos[t] = gross / (2 * n)
    return pos


def walk_forward(panel: list[dict], cost_bps: float = 10.0,
                 quantile: float = 0.2) -> tuple[list[dict], dict]:
    dates: dict[str, list[dict]] = {}
    for r in panel:
        dates.setdefault(str(r["date"]), []).append(r)
    prev: dict[str, float] = {}
    rows = []
    for date in sorted(dates):
        g = dates[date]
        pos = make_positions({r["ticker"]: float(r["score"]) for r in g},
                             quantile)
        ret = {r["ticker"]: float(r["forward_return"]) for r in g}
        tickers = set(pos) | set(prev)
        turnover = sum(abs(pos.get(t, 0.0) - prev.get(t, 0.0))
                       for t in tickers)
        gross = sum(pos[t] * ret.get(t, 0.0) for t in pos)
        cost = turnover * cost_bps / 10000
        rows.append({"date": date, "gross_return": round(gross, 6),
                     "turnover": round(turnover, 6), "cost": round(cost, 6),
                     "net_return": round(gross - cost, 6)})
        prev = pos
    nets = [r["net_return"] for r in rows]
    n = len(nets)
    ann = ((math.prod(1 + x for x in nets)) ** (12.0 / max(n, 1)) - 1) if n else 0.0
    mean = sum(nets) / n if n else 0.0
    var = sum((x - mean) ** 2 for x in nets) / (n - 1) if n > 1 else 0.0
    vol = math.sqrt(var) * math.sqrt(12.0) if n > 1 else 0.0
    cum, peak, max_dd = 1.0, 1.0, 0.0
    for x in nets:
        cum *= 1 + x
        peak = max(peak, cum)
        max_dd = min(max_dd, cum / peak - 1)
    return rows, {"annualized_return": round(ann, 6),
                  "annualized_vol": round(vol, 6),
                  "sharpe": round(ann / vol, 4) if vol > 0 else 0.0,
                  "max_drawdown": round(max_dd, 6), "periods": n,
                  "cost_bps": cost_bps}


def load_panel(path: Path = PANEL_PATH) -> list[dict]:
    try:
        return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines()
                if l.strip()]
    except (OSError, ValueError):
        return []


def append_snapshot(date: str, scores: dict[str, float],
                    path: Path = PANEL_PATH) -> int:
    """One score row per ticker. Skips dates already present (idempotent)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    have = {(r.get("date"), r.get("ticker")) for r in load_panel(path)}
    n = 0
    with open(path, "a", encoding="utf-8") as f:
        for t, s in sorted(scores.items()):
            if (date, t) not in have:
                f.write(json.dumps({"date": date, "ticker": t, "score": s,
                                    "forward_return": None}) + "\n")
                n += 1
    return n


def fill_forwards(path: Path = PANEL_PATH, days: int = 5) -> int:
    """Fill forward_return where closes now exist. Returns filled count."""
    from bneck2 import prices as P
    rows = load_panel(path)
    if not rows:
        return 0
    by_ticker: dict[str, list[dict]] = {}
    for r in rows:
        by_ticker.setdefault(r["ticker"], []).append(r)
    filled = 0
    for t, rs in by_ticker.items():
        hist = {c["date"]: c["close"] for c in P.history(t).get("closes", [])}
        dates = sorted(hist)
        for r in rs:
            if r.get("forward_return") is not None or r["date"] not in hist:
                continue
            i = dates.index(r["date"])
            if i + days < len(dates) and hist[dates[i]]:
                r["forward_return"] = round(
                    (hist[dates[i + days]] - hist[dates[i]]) / hist[dates[i]], 4)
                filled += 1
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n",
                    encoding="utf-8")
    return filled


def live_result(path: Path = PANEL_PATH) -> dict:
    """walk_forward on complete dates, else INSUFFICIENT (never faked)."""
    rows = [r for r in load_panel(path) if r.get("forward_return") is not None]
    dates = sorted({r["date"] for r in rows})
    if len(dates) < 2:
        return {"status": "INSUFFICIENT",
                "complete_dates": len(dates),
                "need": ">=2 complete 5d-forward dates"}
    _, stats = walk_forward(rows)
    if stats.get("max_drawdown", 0) is not None and stats["max_drawdown"] <= -0.5:
        return {"status": "BLOCKED", **stats,
                "note": "drawdown gate: review machinery, not a result"}
    return {"status": "OK", **stats}
