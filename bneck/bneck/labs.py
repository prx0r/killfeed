"""bneck labs — frontier-lab moat tracker: what the labs buy.

Labs training frontier models see bottlenecks first (their walls are the
world's early warning). Their acquisitions/investments/JVs reveal which
constraints they believe are binding — and the ABSENCE of buying in a layer
(compute substrates) is itself a signal: they don't yet believe, or they
plan to build.

Tags: deployment-labor | agent-infra | devices | distribution-media |
models-talent | compute-substrate | data-energy | services.

substrate_gap(): share of compute-substrate deals. ~0 means no lab has
moved on novel compute — the Nvidia-coverage event (a lab buying into
thermodynamic/probabilistic/neuromorphic) would be a regime signal.

Seed: data/labs/deals.json (verified 2025-2026 items only). Stdlib only.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEALS_PATH = ROOT / "data" / "labs" / "deals.json"

SUBSTRATE_TAGS = {"compute-substrate"}


def load_deals(path: Path = DEALS_PATH) -> list[dict]:
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("deals", [])
    except (OSError, ValueError):
        return []


def attention_by_tag(deals: list[dict]) -> dict:
    n = Counter()
    amt: dict[str, float] = Counter()
    for d in deals:
        tag = d.get("tag", "unknown")
        n[tag] += 1
        if d.get("amount_usd"):
            amt[tag] += d["amount_usd"]
    return {"by_count": dict(n.most_common()),
            "by_amount_usd": {k: v for k, v in amt.most_common()}}


def substrate_share(deals: list[dict]) -> dict:
    sub = [d for d in deals if d.get("tag") in SUBSTRATE_TAGS]
    return {"substrate_deals": len(sub), "total_deals": len(deals),
            "share": round(len(sub) / len(deals), 3) if deals else 0.0,
            "items": [(d.get("lab"), d.get("target")) for d in sub]}


def gap_report(deals: list[dict]) -> str:
    att = attention_by_tag(deals)
    sub = substrate_share(deals)
    lines = ["# Frontier-lab moat — where the labs put money",
             f"Tracked deals: {sub['total_deals']} | compute-substrate share: {sub['share']:.1%}",
             "\nAttention by count:"]
    for tag, c in att["by_count"].items():
        lines.append(f"  {tag:20} {c}")
    if att["by_amount_usd"]:
        lines.append("Attention by disclosed $:")
        for tag, a in att["by_amount_usd"].items():
            lines.append(f"  {tag:20} ${a:,.0f}")
    lines.append("\nSubstrate gap: " + (
        "NO lab has bought into novel compute substrates — "
        "watch for the first thermodynamic/probabilistic/neuromorphic "
        "acquisition or strategic investment as an Nvidia-coverage signal."
        if sub["substrate_deals"] == 0 else
        f"{sub['substrate_deals']} substrate deal(s): {sub['items']}"))
    return "\n".join(lines)
