#!/usr/bin/env python3
"""Genius attention snapshot: portfolio + live 5-min prices, side by side.

Reads the Levin corpus attention portfolio (no core-code changes — this only
*imports* stockify.services.genius_corpus and stockify.services.prices),
then prints the current 5-min price snapshot for the tracked basket.

No causal ticker mapping is invented here. Mapping attention topics to
bottlenecks to tickers is a separate, researched artifact (world-state
projector) — this script is the raw material feed for it.

Usage:
    /usr/bin/python3 scripts/genius_attention.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from stockify.services import genius_corpus
from stockify.services.prices import YAHOO_SYMBOLS, get_moves

WATCHLIST = sorted(set(YAHOO_SYMBOLS) | {"IONQ", "RGTI", "QBTS", "ETH"})


def main() -> int:
    entries = genius_corpus.load_corpus()
    if not entries:
        print("no corpus found at data/levin/metadata.json", file=sys.stderr)
        return 1
    portfolio = genius_corpus.attention_portfolio(entries)
    print(genius_corpus.summarize(portfolio))
    print("\nLive 5-min snapshot (tracked basket):")
    moves = get_moves(WATCHLIST)
    for t in WATCHLIST:
        r = moves.get(t)
        if r:
            print(f"  {t:6} {r['price']!s:>12} {r['pct_1d']:+.2f}%  [{r.get('venue')}]")
        else:
            print(f"  {t:6} no data")
    print(f"\n({len(moves)}/{len(WATCHLIST)} priced, $0 Yahoo+CoinGecko cache)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
