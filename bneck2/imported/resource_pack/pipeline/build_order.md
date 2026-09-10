# Build order — 80/20

## Phase 0: make today's board autonomous
1. Polymarket + Kalshi histories/order books.
2. SEC filings, Form 4, 13F, 8-K and frontier-company official news.
3. Selected GitHub/Hugging Face + OpenAlex queries.
4. Spot/capacity/inventory series for current bottlenecks.
5. Normalize into `signal_schema.json`; preserve lineage and missingness.

## Phase 1: revealed-preference graph
Track frontier-lab acquisitions, investments, custom chips, capacity reservations, PPAs/power, sites/interconnection, supplier agreements, hiring clusters and patent families. Update edge probabilities, not just a news feed.

## Phase 2: counterfactual bottleneck relay
For each binding node: simulate +25/+50/+100% capacity; identify the next binding node; simulate removal/substitution; propagate revenue exposure to public securities; calculate market awareness and valuation duration; emit actions only when gates fire.

## Phase 3: empirical calibration
Backtest every source and historical corpse. Learn weights and kill thresholds rather than hand-setting them.
