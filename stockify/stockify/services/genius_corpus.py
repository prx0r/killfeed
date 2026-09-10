"""Genius corpus — attention portfolios from smart people's output.

V0 corpus: Levin Lab (data/levin/metadata.json, 675 entries).
Design: corpus entries share one schema (title/authors/year/journal/doi/url/
topics), so Bach / QRI / Verdon corpora plug into the same functions later.

An attention portfolio answers: what is this mind allocating attention to,
how intensely, and where is the attention *moving*? That movement is the
input to the world-state projector (1/5/10yr), not a stock pick by itself.

Stdlib only. Imports nothing from stockify (join with prices happens in
scripts/genius_attention.py).
"""
from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEVIN_META = ROOT / "data" / "levin" / "metadata.json"


def load_corpus(path: Path = LEVIN_META) -> list[dict]:
    """Load a genius corpus file (list of entry dicts). Missing file -> []."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []


def _year(entry: dict) -> int | None:
    try:
        y = int(str(entry.get("year", ""))[:4])
        return y if 1900 < y < 2100 else None
    except (ValueError, TypeError):
        return None


def attention_portfolio(entries: list[dict], now_year: int | None = None) -> dict:
    """Aggregate attention: topics, journals, rate, and movement.

    Recency weight: w = 0.5 ** (age / half_life), half_life 3yr — recent
    attention counts more, old attention is not forgotten.
    Movement: topic share in recent window (last 2yr) vs prior window.
    """
    now_year = now_year or datetime.now(timezone.utc).year
    half_life = 3.0
    topic_w: Counter = Counter()
    topic_recent: Counter = Counter()
    topic_prior: Counter = Counter()
    journals: Counter = Counter()
    per_year: Counter = Counter()

    for e in entries:
        y = _year(e)
        if y is None:
            continue
        age = max(0, now_year - y)
        w = 0.5 ** (age / half_life)
        topics = e.get("topics") or ["unfiled"]
        for t in topics:
            topic_w[t] += w
            if age <= 2:
                topic_recent[t] += 1
            elif age <= 6:
                topic_prior[t] += 1
        if e.get("journal"):
            journals[e["journal"]] += 1
        per_year[y] += 1

    movement = {}
    for t in set(topic_recent) | set(topic_prior):
        r, p = topic_recent.get(t, 0), topic_prior.get(t, 0)
        movement[t] = {
            "recent_2yr": r,
            "prior_4yr": p,
            "delta": r - p,
            "trend": "rising" if r > p else ("falling" if r < p else "flat"),
        }

    recent_years = sorted(y for y in per_year if y >= now_year - 2)
    rate_recent = sum(per_year[y] for y in recent_years) / max(1, len(recent_years))
    older = [y for y in per_year if now_year - 6 <= y < now_year - 2]
    rate_prior = sum(per_year[y] for y in older) / max(1, len(older))

    return {
        "entries": len(entries),
        "years_covered": [min(per_year), max(per_year)] if per_year else [],
        "papers_per_year_recent": round(rate_recent, 1),
        "papers_per_year_prior": round(rate_prior, 1),
        "top_topics_weighted": topic_w.most_common(15),
        "top_journals": journals.most_common(10),
        "movement": dict(sorted(movement.items(), key=lambda kv: -kv[1]["delta"])[:15]),
        "per_year": dict(sorted(per_year.items())),
    }


def summarize(portfolio: dict, name: str = "Levin Lab") -> str:
    """One-screen text summary for CLI / brief ingestion."""
    lines = [
        f"{name} attention portfolio: {portfolio['entries']} works, "
        f"{portfolio['years_covered'][0] if portfolio['years_covered'] else '?'}-"
        f"{portfolio['years_covered'][1] if portfolio['years_covered'] else '?'}, "
        f"rate {portfolio['papers_per_year_recent']}/yr recent vs "
        f"{portfolio['papers_per_year_prior']}/yr prior.",
        "Weighted attention:",
    ]
    for topic, w in portfolio["top_topics_weighted"][:10]:
        lines.append(f"  {topic:20} {w:6.1f}")
    lines.append("Movement (recent 2yr vs prior 4yr):")
    for topic, m in list(portfolio["movement"].items())[:10]:
        lines.append(f"  {topic:20} {m['trend']:7} ({m['recent_2yr']} vs {m['prior_4yr']})")
    return "\n".join(lines)
