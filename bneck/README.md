# bneck — bottleneck dependency graph

Thesis: AI makes cognition/design cheaper, so value migrates into whatever
physical resource is hardest to scale next — and every bottleneck eventually
dissolves (usually self-dug: capacity wave + demand miss). The gold is both
sides: own the binding bottleneck while uncrowded, short the crowded
picks-and-shovels when the digger arrives.

Fresh standalone project. Stdlib only — runs on system python3, $0 data
(Yahoo + CoinGecko, keyless).

## Layout

```
bneck/            engine (graph, quant, prices, corpus) — pure + stdlib
data/bottlenecks/ graph_v1.json, precedents.json, readings_*.json
data/corpus/      genius corpora (levin_metadata.json, 675 entries)
scripts/poll.py   5-min price snapshot -> data/prices_latest.json
scripts/status.py ranked board + quant regimes + dissolution board
messages/         verbatim user-message archive (17 + index)
```

## Use

```bash
/usr/bin/python3 scripts/poll.py        # snapshot prices ($0)
/usr/bin/python3 scripts/status.py      # full brief
/usr/bin/python3 scripts/status.py --quant   # + Tk/Td, RedundancyRisk, ShortConvexity
/usr/bin/python3 scripts/status.py --trigger memory_hbm:"KV-cache-light architectures at frontier"
/usr/bin/python3 -m unittest discover -s tests   # 14 tests, stdlib only
```

## Model

- `graph.py` — v2 nodes/temporal edges, conviction, rebalance, short board,
  DESTROY/CONSTRAIN per node
- `quant.py` — recognition gates, base rates, Tk/Td investable quantity,
  RedundancyRisk, ShortConvexity
- `prices.py` — 5-min cache first, Yahoo-live fallback, never raises
- `corpus.py` — genius attention portfolios (what are the smartest
  minds allocating attention to, and where is it moving)
- `belief.py` — claims across 4 clocks (hard/expert/pm/equity) with
  lineage discount + disagreement flags
- `forecasters.py` — Skill_i(topic): calibration, lead, novelty per handle
- `updater.py` — Bayesian edge fusion + event trail + downstream tickers
- `jevons.py` — EfficiencyGain vs DemandElasticity: SUBSTITUTION or EXPANSION trap
- `calibration.py` — source reliability learned from outcomes, not fiat
- `labs.py` — frontier-lab buy-side moat tracker (what labs buy = early warning)
- `evidence.py` — kill_observations (verdict-logged, incl. non-firings),
  unknowns ledger, ticker signals
- Criticality(v) via N-1 removal answers whose removal breaks most value

Regime lifecycle per node:
ACCUMULATE -> HOLD -> DISSOLUTION_WATCH -> SHORT_WATCH -> EXIT

Constraint classes (eliminability by AGI): knowledge .9, human-skill .9,
compute-architecture .75, physical-resources .5, physical-processes .35,
ip-rights .25, regulatory-permission .15.

Base rates (parsed from precedents.json, n=9): median crowded-equity
unwind −85%, commodity leg −80%.

Stolen with attribution in mind: ProphetMap (falsifier discipline),
Keystone (unknowns ledger — AGPL, ideas only), CHOKEPOINT (N-1 removal),
chip-sense (scenarios), memory-atlas (cards, MIT), ai-supply-chain-research
(relay + power leg, CC BY 4.0), alphasig (signals, MIT). No code lifted
from AGPL / non-commercial / proprietary repos.
