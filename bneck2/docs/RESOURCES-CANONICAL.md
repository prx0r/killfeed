# Canonical resources — live vs not, by category (2026-09-10)

Source of truth for what this box can actually pull. Probed live today;
`collectors/*.py` = wired. Statuses: LIVE-WIRED · LIVE-READY (probed OK,
not yet in the loop) · KEY (needs key/signup) · HEAVY (infra/compute/bulk)
· BLOCKED (actively refuses bots) · QUEUED (unprobed).

## Filings, insiders, fundamentals — LIVE-WIRED

- SEC submissions (Form 4/13D/13G/8-K) — `collectors/sec.py` — burst leg live.
- SEC companyfacts (XBRL: revenue TTM, growth, R&D intensity) —
  `collectors/sec_facts.py` — live (NVDA verified).
- Polymarket whale trackers — `collectors/polywhale.py` — holders/positions/
  trades + consensus live. Recipes ex-`third_party/polytrack` (runs here)
  + `polywhale` (needs requests; recipe ported stdlib).
- Yahoo chart (spot + history) + CoinGecko — `bneck2/prices.py` — 29/29 live.

## Filings/insiders — BLOCKED / QUEUED

- Senate PTR search — BLOCKED (efdsearch 403s bots; unknowns u-009).
- House clerk bulk — QUEUED (likely same wall; try browser session).
- OpenInsider — no API; scraping vs source-policy, QUEUED.
- SEC FTD bulk — keyless ZIPs but needs CUSIP→ticker map — QUEUED.
- SEC 13F/N-PORT/Form D bulk — keyless, quarterly cadence — QUEUED (build
  when holdings breadth matters; currently single-name focused).

## Prediction markets — LIVE-WIRED

- Polymarket Gamma search + CLOB book depth — `collectors/polymarket.py`,
  `collectors/clob.py` — live. Docs: `docs/VENUES.md`.
- Kalshi open events + Manifold search — `collectors/kalshi.py`,
  `collectors/manifold.py` — live, best-book-wins.
- Metaculus — KEY/terms. Skip until auth sorted.

## Research velocity — LIVE-WIRED

- OpenAlex group_by yearly counts — `collectors/openalex.py` — attack leg.
- bioRxiv windows — `collectors/biorxiv.py` — live.
- Crossref funder links — `collectors/crossref.py` — live.
- HN Algolia stories — `collectors/hn.py` — narrative heat live.
- HF Hub models — `collectors/hf.py` — implementation heat live.
- OSTI technical reports — `collectors/fed.py` — live.
- Semantic Scholar — LIVE-READY but 429-prone on shared pool; needs
  retry/backoff wrapper before wiring (queued).

## Money trails — LIVE-WIRED

- USAspending awards — `collectors/usaspending.py` — live.
- Grants.gov opps — `collectors/grants.py` — live.
- NSF awards — `collectors/fed.py` — live (noisy keywords; curate terms).
- NIH RePORTER — BLOCKED-ish (405 on documented path; unknowns-worthy,
  queued for path fix).

## Permissions / regulatory — LIVE-WIRED

- Federal Register docs — `collectors/fed.py` — live (export/energy/AI).
- openFDA 510k counts — `collectors/bio.py` — live (176k total baseline).
- ClinicalTrials counts — `collectors/bio.py` — live.
- BLS macro anchor — `collectors/fed.py` — live.
- Congress.gov / GovInfo / Regulations.gov / FRED / EIA / BEA / Census —
  all KEY (free api.data.gov key or agency key). ONE key unlocks five.
  Highest-leverage signup on the list.
- Companies House / USPTO / EPO — registration. USPTO ODP before EPO.
- BIS EAR / OFAC / FTC / DOJ press — free pages, unscraped — QUEUED.

## Frontier labs + diggers — LIVE-WIRED (partial)

- OpenAI news RSS — `collectors/labs_rss.py` — live (30 posts, 2 capability).
- Anthropic Greenhouse board — `collectors/jobs.py` — live (599 posts,
  research 74 / infra 54 / silicon 13 / energy 8).
- Anthropic/DeepMind/Meta/xAI feeds, Lever slugs — QUEUED (404s logged,
  don't guess URLs).
- Normal/Extropic/General Compute — digger ladder already tracks; blogs
  join FEEDS when URLs resolve.

## Code/implementation — LIVE-WIRED (partial)

- GitHub repo events — `collectors/github.py` — live (60/hr keyless).
- Pack `github_repo_registry.json` — 60+ repos mapped, S++ partially
  cloned (`pmxt`, `pm-analysis`, trader set). Clone queue in
  `docs/RESOURCES.md`.
- GH Archive bulk — HEAVY (hourly dumps; BigQuery-scale). Skip until
  backtest needs multi-year implementation history.

## Macro/trade/geo — QUEUED (keyless bulk, pull on demand)

- OECD ICIO / IO tables (free downloads), UN Comtrade (free tier — probe
  key need), IMF Data API (SDMX, complex), World Bank WITS/commodities,
  UNCTADstat, OWID (per-dataset CSV), USGS minerals. None wired — pull
  when geo/trade layer starts (goated §31 queued).

## Trader repos (third_party/) — verdicts in docs/TRADERS.md

- Running here: polytrack. Recipes ported: polywhale. Review-only until
  deps exist: pmbot, pm-arb, kalshi-ai, kalshi-cli, kalshi-deep, copy-sim,
  anthowave, sniperun. Dead upstream: 5 (listed there).

## The one signup that unlocks the most

Free `api.data.gov` key → Congress + GovInfo + Regulations.gov + EIA...
Do that single signup and 4 categories flip KEY→LIVE.
