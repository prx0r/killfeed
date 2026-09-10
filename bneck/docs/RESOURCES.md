# bneck Resource Directory — every free source that makes this project possible

All $0 unless marked. Each entry: what it tells you → how bneck mines it.
Conventions: `bneck/<module>` = built; `third_party/<repo>` = cloned reference
(check license column before copying code — ideas are free, code may not be).

## 0. Live prices (the fast clock)

| Source | URL | Cost | Tells you | bneck use |
|---|---|---|---|---|
| Yahoo Finance chart API | query1.finance.yahoo.com/v8/finance/chart | $0 keyless | Price, 1d %, volume, day range, any global ticker | `bneck/prices.py` primary |
| CoinGecko simple/price | api.coingecko.com | $0 keyless | Crypto spot + 24h change | `bneck/prices.py` crypto leg |
| Stooq daily CSV | stooq.com/q/d/l | $0 (JS-blocked from servers — fallback only) | Daily closes | fallback |
| FRED | fred.stlouisfed.org/docs/api | $0 key needed (free signup) | Rates, commodities, industrial production, macro series | regime context, kill-feed macro |

## 1. Prediction markets (the probability clock)

| Source | URL | Cost | Tells you | bneck use |
|---|---|---|---|---|
| Polymarket Gamma + CLOB + WS | docs.polymarket.com | $0 public | p(E), volume, liquidity, spread, velocity, orderbook | `belief.py` pm clock |
| Kalshi API (trades + WS + history) | docs.kalshi.com | $0 public (+account to trade) | Same + backtestable history | `belief.py` pm clock |
| Polymarket-v1 dataset (HF) | huggingface.co/datasets/TimeSeventeen/Polymarket-v1 | $0 | 1.2B trades, 1.3M markets, $61B volume 2022-2026 | calibrate pm reliability |

## 2. Corporate filings, insiders, shareholders (the hard clock)

| Source | URL | Cost | Tells you | bneck use |
|---|---|---|---|---|
| SEC EDGAR full-text + submissions API | sec.gov/about/developer-resources | $0 (sub-second updates) | Customer/supplier concentration, inventory, backlog, capex, risk-factor diffs, 8-K deals, M&A | kill-feed: inventory +37% patterns |
| XBRL company facts | data.sec.gov | $0 | Machine-readable financials | fundamental cross-checks |
| Form 4 / 13D/G / 13F | EDGAR | $0 | Insider buys/sells, activist stakes, institutional holdings | cluster-buy signals; CEO money moves |
| OpenInsider | openinsider.com | $0 | Pre-structured insider screener | same, faster |
| Proxy DEF 14A | EDGAR | $0 | Exec comp, related-party deals, board ties | CEO incentive mapping |
| Earnings calls + IR decks | company IR pages | $0 | Guidance, capacity plans, order language | confirm/deny bottleneck |
| Shareholder letters | IR pages / EDGAR | $0 | Capital allocation intent | thesis evidence |

## 3. Patents / IP (the tollbooth map)

| Source | URL | Cost | Tells you | bneck use |
|---|---|---|---|---|
| PatentsView / USPTO | search.patentsview.org | $0 (key availability varies) | Patent-level assignee/inventor data, acceleration | AttackIntensity per node; legal betweenness |
| EPO insight reports | epo.org | $0 | Landscapes (quantum, semi) by subfield | IP node evidence (IonQ estate) |
| WIPO landscapes + FAQ | wipo.int | $0 | Ownership maps, compulsory-licensing regimes | tollbooth durability scoring |
| Google Patents | patents.google.com | $0 | Full-text claim search | design-around feasibility |
| The Lens | lens.org | freemium | Patent/licensing networks (CRISPR template) | precedent pattern |

## 4. Government / awards / econ (the slow-money clock)

| Source | URL | Cost | Tells you | bneck use |
|---|---|---|---|---|
| USAspending API | api.usaspending.gov | $0 no auth | Awards, contracts, grants, agencies | DOE/lab money → bottleneck binding probability |
| EIA open data | eia.gov/opendata | $0 | Generation, capacity, demand, grid flows | power node readings |
| BEA IO + API | bea.gov / apps.bea.gov/api/signup | $0 key free | Industry→industry dependencies | edge weights |
| USGS minerals | usgs.gov/nmic/tools | $0 | Production/concentration/reserves (Ga, U, Cu, REE) | geo-concentration kills |
| FRED | (above) | $0 | Macro/prices | regime context |
| CHIPS/DARPA/DOE/NIH/NSF awards | agency sites, press | $0 | Pre-equity strategic capital (Extropic $75M LOI template) | digger funding watch |
| Export-control lists | BIS entity lists | $0 | Who can't buy what | REGULATED_BY edges |

## 5. Research velocity (the attack-intensity clock)

| Source | URL | Cost | Tells you | bneck use |
|---|---|---|---|---|
| OpenAlex | help.openalex.org/api | $0 keyless | Papers/authors/topics/citations/funders/grants | AttackIntensity(b) per node |
| arXiv API | arxiv.org/help/api | $0 | Preprints cs.AI/LG/ET | substitution-paper velocity |
| Semantic Scholar API | semanticscholar.org/product/api | $0 key free | Citations, influential refs | corroboration weight |

## 6. Code / repos (the implementation-evidence clock)

| Source | URL | Cost | Tells you | bneck use |
|---|---|---|---|---|
| GitHub REST + events | docs.github.com/rest | $0 (rate-limited; token raises) | Branches, commits, releases in dependency repos | KV-compression/SSM/quant/CXL watchlists |
| Hugging Face Hub API | huggingface.co/docs/hub | $0 | Trending models, likes, downloads | architecture-shift velocity |
| Monitored exemplars (cloned) | third_party/ | $0 | See manifest below | pattern library for GitHub monitoring |

## 7. News / events / people

| Source | URL | Cost | Tells you | bneck use |
|---|---|---|---|---|
| GDELT | gdeltproject.org | $0 | Machine-readable world events | disruption + narrative velocity |
| Company blogs / research notes | e.g. normalcomputing.com/blog, extropic.ai/writing | $0 | Milestones (tapeouts, benchmarks) with dates | milestone ledger → substitution_milestone |
| Tech press (DCD, Tom's, SemiAnalysis via audit repo) | — | $0 | Capacity/pricing reporting (TrendForce spot, HBM shares) | readings + kill-feed |
| X forecaster ledger | — | $0 | Who knew first (manual curation → `forecasters.py`) | expert clock weights |
| CEO money moves | Form 4 + 13D/G + proxies + deal news | $0 | What insiders do with cash (labs tracker) | `labs.py` + insider overlay |

## 8. Trade / supply concentration

| Source | URL | Cost | Tells you | bneck use |
|---|---|---|---|---|
| UN Comtrade API | uncomtrade.org/docs | $0 (rate-limited) | Who exports/imports what; concentration | geo edges |
| OECD ICIO / EXIOBASE | oecd.org / exiobase.eu | $0 | Global input-output dependencies | edge weights |
| Wikidata SPARQL | query.wikidata.org | $0 | Entity resolution (subs, facilities, countries) | dedupe |

## Third-party manifest (cloned into third_party/, gitignored)

| Repo | License | Status | Steal |
|---|---|---|---|
| Beltran12138/prophetmap | MIT declared, no file | analysed | falsifier discipline, hysteresis |
| Beltran12138/ai-release-radar | **none found — treat as proprietary** | assessed | ingestion shell pattern only (see below) |
| Skeeter-spec/keystone | AGPL-3.0 | analysed | gaps ledger, gate philosophy (ideas only) |
| eugenehp/supplychain | non-commercial | analysed | tiered BOM pattern (ideas only) |
| atharvahirulkar/chokepoint | MIT claimed, no file | analysed | N-1 removal scoring |
| aminalav/chip-sense | MIT | analysed | scenario sets, cluster-demand formula |
| sflans99/silicon-stack | **unlicensed — clean-room only** | analysed | structure, not data |
| upamanyuacharya/memory-atlas | MIT | analysed | bottleneck cards, roadmap timeline |
| YichengYang-Ethan/ai-supply-chain-research | CC BY 4.0 | analysed | relay framing, power leg (attribute) |
| sushaan-k/alphasig | MIT | analysed | signal schema + decay |
| tunglich/TWSE-KG | **proprietary — do not copy** | analysed | propagation idea only |
| Timeverse/My-TW-Coverage | MIT | analysed | wikilink KG pattern |
| supat-roong/stock-relation | MIT | analysed | SQLite edge store pattern |
| Jumade/sec-graph | MIT | analysed | idempotent upserts |
| Sakshi3027/disruptiq | **none found — ideas only** | analysed | risk-propagation formula shape |
| navyawalia23-bit/Semiconductor-AI-Analysis | **none found — ideas only** | analysed | stress composite idea |
| Intelligent-Internet/Qwen3.8-Inference-MetaZenith | Apache-2.0 | cloned | exemplar: KV-cache/TurboQuant efficiency work = memory-attack monitor target |
| extropic-ai/thrml | (see repo) | cloned | THRML milestones → accelerators substitution_milestone |
| duanyytop/agents-radar | MIT | cloned | multi-source ingestion shell reference |
| mlnjsh-style arXiv radars | various MIT | listed | arXiv poll pattern |

## ai-release-radar assessment (Beltran12138)

Verdict: yes — good foundation, exactly as suspected. The ingestion shell
(5 platforms + Polymarket Gamma + SQLite + Telegram + Flask SSE + 5-min poll
+ `state.json` dedup) is solid and worth mirroring. The scorer is precisely
the static-weights + keyword system msg-18 replaces (`arxiv 5 / github 4 /
hf 4 / polymarket 3 / reddit 2 / twitter 1`, model-name keyword TARGETS,
DeepSeek LLM gate). No LICENSE file found → pattern only, no code copied.
Our `belief.py` (lineage + clocks) + `calibration.py` (learned weights) +
`updater.py` (Bayesian fusion) + `forecasters.py` (Skill_i) are the
drop-in replacement for its `scorer.py`.

## Normal Computing — evidence check (2026-09-10)

Verified: CN101 taped out Aug 2025 (world's first thermodynamic chip claim);
Hot Chips 2026 small-scale generative demos (MNIST/CIFAR, 62x fewer cycles);
up-to-1000x efficiency claims on *targeted* workloads; $85M+ raised ($50M
Samsung Catalyst Mar 2026). Correction: **no head-to-head vs Nvidia on
frontier workloads found** — claims only, early stage. Stays a watch-item
(`substitution_milestone: false`), not a trigger. (OpenAI "Jalapeño beats
GB300" headline seen on a single thin source — unverified, not asserted.)
