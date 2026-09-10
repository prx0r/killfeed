# Info streams — what each gives us and why (2026-09-10)

One section per stream. Format: GIVES (the observable) → WHY (the mechanism
that makes it predictive, tied to goated.md) → EXTRACT (what we take) →
LIMITS (what it can't say) → STATUS. If a stream lacks a WHY, it doesn't
belong in the loop.

## 1. SEC filings — Form 4 / 13D / 13G / 8-K (collectors/sec.py) — LIVE

GIVES: dated insider + deal events per ticker, machine-readable, T+2.
WHY: insiders transact on private information against personal wealth;
bursts mark regime attention (raises, departures, M&A prep). Thesis §8:
supply-response and regime-change evidence, not sentiment.
EXTRACT: burst counts vs own cadence baseline (killfeed), event-study
anchors (acq.py).
LIMITS: 10b5-1 plans make most sales noise; directors sell into strength
(E018: heavy-sell months +3.4%). Reads bursts, never motives.

## 2. OpenInsider tape (collectors/openinsider.py) — LIVE

GIVES: full insider tape with buy/sell direction, officer flags, cluster
pages (multi-insider same-name buys).
WHY: buys cost basis risk — officers buying ≥$25k with own money is the
highest-conviction insider primitive; clusters remove idiosyncrasy.
Buys predict better than sells (sells are diversification; E018 confirms
the asymmetry direction).
EXTRACT: cluster/officer buys → connection legs; NVDA tape (100 rows, zero
buys — itself a reading: no insider buying at these prices).
LIMITS: 100-row window; no motive; late filings.

## 3. FINRA short flow (collectors/finra.py) — LIVE

GIVES: daily per-symbol short volume ratios; (SI biweekly queued).
WHY: crowded shorts = fuel (squeeze) or informed exit; combined with our
crowdedness it separates "positioned both ways, watch" from consensus.
Thesis: capital-cycle inversion needs the short leg measured, not assumed.
EXTRACT: short_crowded joins (MU 43%×0.8, NVDA 40%×0.9 live).
LIMITS: Reg SHO volume includes market-maker flow; not directional intent.

## 4. Prediction markets — Polymarket/Kalshi/Manifold (+CLOB) — LIVE

GIVES: explicit probability distributions with money behind them, per
question, timestamped; books (depth/spread) on CLOB/Kalshi.
WHY: only venue where beliefs are directly priced — no model needed to
infer expectations. Triangulation across venues (goated §35) catches
mispricing neither venue shows alone; best-book-wins keeps us honest.
Thesis §§36–37 run on this stream (consistency arbitrage needs implied
worlds, and only markets state them numerically).
EXTRACT: best-book (p, tier, venue, reliability); whale consensus on the
book; Kalshi candles for pm velocity.
LIMITS: thin books are coin-flips (tiered as such); queries return noise
without overrides; resolved markets linger; Kalshi has no per-trader data
(structurally — track books, never wallets).

## 5. Whale wallets — Polymarket holders/positions (collectors/polywhale.py) — LIVE

GIVES: who holds what size on which outcome (public chain data).
WHY: persistent winners exist; multi-whale same-side size is conviction
you can't fake cheaply. Stronger than any single pundit because it's
staked. (E004: 2/3 resolved calls.)
EXTRACT: N-whale consensus → WHALE_CONSENSUS signals on best-book markets.
LIMITS: past performance ≠ edge (pmbot vetting queued); copy-lag eats
fills; wallets rotate.

## 6. SEC companyfacts XBRL (collectors/sec_facts.py) — LIVE

GIVES: audited fundamentals — revenue series (tag-rename aware), growth,
R&D intensity.
WHY: valuations embed duration assumptions; XBRL gives the accounting leg
of duration-mismatch shorts (H_val) and the size split for event studies
(E012: sub-$100B revenue counterparties hit 0.75 vs 0.25).
EXTRACT: revenue_ttm/growth/rd_intensity per CIK.
LIMITS: annual cadence, restatements, tag drift (handled, not solved).

## 7. OpenAlex research velocity (collectors/openalex.py) — LIVE

GIVES: true yearly publication counts per direction (group_by, not samples).
WHY: the attack leg — accelerating literature on substitutes measures
technological pressure years before products (TechToken thesis). Growth
needs mass (HIGH = growth AND total) so hype without literature fails.
EXTRACT: AttackIntensity tiers → kill verdicts (optical +130% fired).
LIMITS: yearly granularity; query vocabulary matters (overrides logged).

## 8. Preprints + grants + funders — bioRxiv/Crossref/NSF/NIH-adjacent — LIVE (NIH blocked)

GIVES: pre-journal velocity, funder links, award flows.
WHY: substitution research gets funded before it gets published before it
ships — grants are the earliest dollar-denominated signal of attack
directions. Funders reveal *who believes* (follow lab-adjacent money).
EXTRACT: counts per direction; funder names on attack papers.
LIMITS: noisy keywords (NSF); NIH path 405 (queued).

## 9. HN + HF + GitHub — narrative/implementation (hn.py/hf.py/github.py) — LIVE

GIVES: story points (saturation), model/like counts (builder adoption),
repo events (implementation).
WHY: three different clocks of the same diffusion — talk (HN) →
build (HF/GH) → deploy. Saturation + low crowdedness = stale scores;
implementation heat without narrative = early. Thesis: observe the
pipeline stage, not the headline.
EXTRACT: narrative_heat tiers, implementation_heat, repo signals.
LIMITS: HN is sentiment-prone (cross-check only); GH 60/hr keyless.

## 10. Frontier-lab exhaust — RSS + hiring (labs_rss.py/jobs.py) — LIVE (partial)

GIVES: capability announcements (J_t candidates) + hiring-cluster mix.
WHY: labs reveal constraints by what they announce (capability direction)
and what they staff (research 74 / infra 54 / silicon 13 / energy 8 at
Anthropic = a priced-in-resources readout). Hiring is slow, honest money.
EXTRACT: capability-hit posts × node scan → lab_node joins; cluster mix
deltas (as history accrues).
LIMITS: 2/6 lab feeds resolve; PR-filter anything announced.

## 11. Permissions — FedRegister/openFDA/trials/House (fed.py/bio.py/house.py) — LIVE

GIVES: regulatory flow (docs, clearances, trial counts, filing counts).
WHY: permission scarcity (goated §§5–6) — right-to-deploy gates
deployment regardless of capability. FedRegister rulemaking and 510k
flows are the deployment clock made legible.
EXTRACT: doc counts per term, clearance totals, trial queue depth,
House filing counts (metadata until PDF parsing lands).
LIMITS: counts, not outcomes; Senate session-walled.

## 12. Macro anchors — BLS/Treasury/WorldBank (fed.py/treasury.py/worldbank.py) — LIVE

GIVES: CPI baseline, financing rates ($40T debt clock), country
capability indicators (R&D, hi-tech share, energy access).
WHY: duration-mismatch shorts need the financing leg (rates × asset
life); geo layer needs place-based capability facts. Anchors, not alpha.
EXTRACT: CPI latest, rate curve points, indicator series.
LIMITS: low frequency; never trade on these alone.

## 13. Prices — Yahoo + CoinGecko (+history) — LIVE

GIVES: closes, histories, forward returns — the target variable itself.
WHY: everything above is measured against this. No prices, no calibration,
no backtest, no Skill. The ground truth stream.
EXTRACT: spot, 20d momentum, forward windows, event-study benchmarks (SPY).
LIMITS: prices don't explain themselves (that's the other 12 streams' job).

## 14. X/Twitter — NOT LIVE (needs GetXAPI key + budget)

GIVES (when keyed): primary-source researcher claims, reply-level signal,
engagement velocity, corroboration across handles.
WHY: fastest primary-source layer — researchers post results months before
papers; reply threads contain the falsification attempts. stockify's
SCARCITY_MAP + detector already encode the scarcity-shock mapping; the
missing piece is the firehose, not the theory.
STATUS: stockify X-engine built + tested ($0.01 spend verified); needs key
funding. Until then: HN + RSS + lab blogs cover ~40% of the function slow.
