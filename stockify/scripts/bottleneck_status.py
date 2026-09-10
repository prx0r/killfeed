#!/usr/bin/env python3
"""Bottleneck status brief: ranked graph + live prices + rebalance actions.

Reads data/bottlenecks/graph_v1.json, scores every node, joins the 5-min
$0 price cache, prints conviction ranking with OVERWEIGHT/HOLD/WATCH/EXIT
actions and the kill-signals that would invalidate each position.

Only *imports* stockify.services.bottlenecks / prices — no core edits.

Usage:
    /usr/bin/python3 scripts/bottleneck_status.py
    /usr/bin/python3 scripts/bottleneck_status.py --trigger memory_hbm:"KV-cache-light architectures at frontier"
        (repeatable; marks a kill signal confirmed — must match graph text)
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from stockify.services.bottlenecks import load_graph, render
from stockify.services.prices import get_moves


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trigger", action="append", default=[],
                    help='node_id:"kill signal text" — repeatable')
    args = ap.parse_args()
    triggered: dict[str, list[str]] = {}
    for item in args.trigger:
        if ":" not in item:
            print(f"bad --trigger (need node:signal): {item}", file=sys.stderr)
            return 1
        node_id, sig = item.split(":", 1)
        triggered.setdefault(node_id.strip(), []).append(sig.strip())
    graph = load_graph()
    tickers = sorted({t for n in graph["nodes"] for t in n.get("tickers", [])})
    moves = get_moves(tickers)
    print(render(graph, moves, triggered))
    print(f"(priced {len(moves)}/{len(tickers)} from 5-min $0 cache)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
