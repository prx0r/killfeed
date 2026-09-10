# X scout plan — NVDA 12, adapted from BEAR's August playbook

BEAR's proven flow (crypto, 383 posts → 47 CALLs → 28 outcomes, honest
null-heavy reporting): recon → history (2-wk chunks, full pagination) →
regex extractor with evidence spans (no asset defaults) → next-candle
entry, one outcome per event×asset → baselines always → Wilson CIs →
caveats section. Ported below to equities with the differences marked.

## Adaptations for stocks (vs their crypto flow)

- **Entry**: next TRADING day open (equities aren't 24/7; no Sunday candles).
- **Horizons**: 1d / 5d / 20d (their 1h/4h/24h/7d don't fit equity clocks).
- **Benchmark**: SPY-adjusted abnormal returns (their always-long-BTC equivalent).
- **Assets**: NVDA universe tickers + $cashtags; UNKNOWN allowed, never default.
- **Regime**: our severity/B + VIX-proxy via SPY vol (their BTC regime timeline).

## Steps + exact costs ($0.001/call, balance $34.83)

1. **Recon** (12 × user_info): $0.012. Gate: directional+ticker density >0.3.
2. **History** (passers only, 2-wk chunks, full pagination): ~$0.10–0.20 each.
3. **Extract** (local, free): direction + tickers + levels + evidence spans.
4. **Outcomes** (local, free): next-trading-day entry, SPY-adjusted.
5. **Cards + receipts** (local, free): per-handle source cards, E-series.

Total ask: ~$0.50 cap, ledgered per call (their api_ledger.jsonl pattern
→ our data/x/ledger.jsonl), stop at cap without asking twice.

## Their caveats we inherit (stated upfront)

- Small-n per author is meaningless; report Wilson, not win rate.
- Bullish-regime bias (always-long baseline will flatter).
- Sharpe artifacts at n<30; selection bias from asset-detection misses.
- 70–80% of insider alpha lives pre-disclosure (their finding) — same may
  hold for X posts vs price; test explicitly (post time vs move time).
