# Results ledger — all experiments (rebuilt from receipts)

runs=135 hypotheses=34 support=0.366 95% CI [0.275, 0.467]

## E001: REFUTED (directional-only) (n=1, runs=9)
NVDA burst Sep-02 (Stevens $411M) -> 4d -0.3%; n=1, directional only

## E002: CONFIRMED (directional-only) (n=4, runs=9)
attack real AND crowded -> mapping says WATCH; voted CONFIRMED as mapping evidence

## E003: REFUTED (directional-only) (n=0, runs=9)
0/0 pairs >6pp apart; max jaccard [] — venues list different questions (PM: earnings/noise, Kalshi: science timelines)

## E004: CONFIRMED (directional-only) (n=3, runs=9)
consensus hit rate 0.667 on 3 resolved markets
`{"hits": 2, "total": 3}`

## E005: REFUTED (directional-only) (n=16, runs=9)
Spearman(B, conviction) = -0.44, n=16 directional
`{"rho": -0.438}`

## E006: INCONCLUSIVE (directional-only) (n=6, runs=9)
top gaps: [('slowdown', -0.45), ('agent-openai', 0.11), ('agent-google', 0.11)]

## E007: INCONCLUSIVE (directional-only) (n=0, runs=9)
preregistered; blocked on multi-week verdict history

## E008: INCONCLUSIVE (directional-only) (n=0, runs=9)
preregistered from E003 finding; arb needs human-confirmed pairs (pmbot workflow), not fuzzy match

## E009: REFUTED (directional-only) (n=16, runs=10)
penalized rho=-0.02 vs plain -0.44
`{"rho_penalized": -0.024}`

## E010: REFUTED (directional-only) (n=13, runs=5)
0.308 hit rate, mean excess 0.0624, n=13 directional
`{"mean_excess": 0.0624, "hit_rate": 0.308}`

## E011: INCONCLUSIVE (directional-only) (n=1, runs=5)
silicon/capacity subset: hit 0.0, mean 0.0205, n=1
`{"mean_excess": 0.0205, "hit_rate": 0.0}`

## E012: CONFIRMED (directional-only) (n=9, runs=7)
mega(rev>=$100B) hit 0.2 n=5 vs rest hit 0.75 n=4

## E013: REFUTED (directional-only) (n=2, runs=6)
red-team vs memory_hbm: 2 disconfirming facts

## E014: REFUTED (n=45, runs=3)
composite -4.7844 vs momentum -3.5863 on holdout
`{"composite_sharpe": -4.7844, "momentum_sharpe": -3.5863}`

## E015: CONFIRMED (n=120, runs=4)
composite 2.3449 vs momentum -6.8277 on biweekly holdout
`{"composite_sharpe": 2.3449, "momentum_sharpe": -6.8277}`

## E016: REFUTED (n=80, runs=1)
neg-burst IC=0.075 n=80; long 0.541 vs short -0.244

## E017: CONFIRMED (directional-only) (n=8, runs=2)
top-tercile beats universe by +2.24% per window
`{"mean_excess_vs_universe": 0.0224}`

## E018: REFUTED (directional-only) (n=10, runs=1)
heavy-sell months +3.4% vs rest -0.6%
`{"heavy_mean": 0.0339, "light_mean": -0.0063}`

## E019: REFUTED (n=81, runs=1)
90d BTC-NVDA return rho=0.017, beta=0.014689996179648218
`{"rho": 0.017}`

## E020: INCONCLUSIVE (directional-only) (n=0, runs=1)
1 BTC levels tracked, 0 resolved
`{"hits": 0}`

## E021: CONFIRMED (directional-only) (n=16, runs=1)
SEC->NVDA: X-leads@4w r=-0.317
`{"peak": {"peak_lag": 4, "peak_r": -0.317, "n": 13, "curve": [[-4, 0.206], [-3, 0.138], [-2, 0.014], [-1, -0.198], [0, -0.083], [1, 0.051], [2, -0.068], [3, -0.008], [4, -0.317]], "verdict": "X-leads@4w r=-0.317"}}`

## E022: REFUTED (directional-only) (n=16, runs=1)
HN->NVDA: Y-leads@3w r=0.693
`{"peak": {"peak_lag": -3, "peak_r": 0.693, "n": 14, "curve": [[-4, -0.219], [-3, 0.693], [-2, -0.297], [-1, -0.218], [0, 0.389], [1, 0.203], [2, 0.104], [3, -0.554], [4, 0.121]], "verdict": "Y-leads@3w r=0.693"}}`

## E023: REFUTED (directional-only) (n=16, runs=1)
SEC->HN: Y-leads@4w r=0.754
`{"peak": {"peak_lag": -4, "peak_r": 0.754, "n": 13, "curve": [[-4, 0.754], [-3, 0.182], [-2, -0.131], [-1, -0.057], [0, -0.111], [1, -0.321], [2, -0.273], [3, -0.151], [4, 0.065]], "verdict": "Y-leads@4w r=0.754"}}`

## E024: INCONCLUSIVE (directional-only) (n=0, runs=1)
preregistered; blocked on X key funding

## E025: CONFIRMED (directional-only) (n=16, runs=1)
divergent 0.0538 (n=9) vs convergent 0.0178 (n=7)

## E026: REFUTED (n=40, runs=1)
pre-disclosure +3.08% vs post +4.66% (n=40)

## E027: REFUTED (directional-only) (n=0, runs=2)
0/0 cluster groups look programmatic

## E028: CONFIRMED (directional-only) (n=21, runs=1)
near-high +2.9% vs far -0.6% (n=21)

## E029: REFUTED (n=432, runs=1)
winners=['f_mom_20']

## E030: REFUTED (n=144, runs=3)
comp 1.0682 vs mom 1.0682 vs bh -1.5992
`{"composite_sharpe": 1.0682, "momentum_sharpe": 1.0682, "buyhold_sharpe": -1.5992}`

## E031: CONFIRMED (n=144, runs=1)
mom 1.0682 vs bh -1.5992; halves [4.4789, -0.7984]
`{"momentum_sharpe": 1.0682, "buyhold_sharpe": -1.5992}`

## E032: REFUTED (directional-only) (n=6, runs=1)
13F basket -0.159 vs SPY 0.0209 since 6/30 (n=6)
`{"basket_mean": -0.159, "spy": 0.0209}`

## E033: REFUTED (n=76, runs=1)
X calls 5d mean +0.33% (n=76)

## E034: INCONCLUSIVE (directional-only) (n=2, runs=1)
kalshi momentum 0/2 carry
`{"hits": 0}`

coverage: 48 cells tested, 3 triggered (684 rows)
triggered: accelerators:sec-burst, optical_io:openalex-attack, optical_io:sec-burst
