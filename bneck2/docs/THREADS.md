# THREADS — every open thread, one place (auto-checked by scripts/threads.py)

Status key: OPEN (needs action) · WAITING (needs time/data, cron handles) ·
BLOCKED (needs key/session/deps) · WATCH (monitor). Counts verified
2026-09-10; rerun the script — this file rots if counts drift.

## Calibration (engine truthfulness)

- [OPEN] p_market placeholders → pmxt adapter + venue-implied calibration
  (consistency scores decorative until then).
- [OPEN] Form-4 absolute gates → cadence-relative at baseline n≥10
  (baselines seeded, 5 tickers).
- [WAITING] Backtest significance (~12 complete dates; now 3).
- [WAITING] dB/dt nonzero somewhere (static intraday, honest zeros).
- [OPEN] PM queries re-probe periodically (Gamma keyword-side matching).

## Data sources (see RESOURCES-CANONICAL for the full map)

- [OPEN] POWI/TKR/NOVT CIKs (www.sec.gov blocks box; need alt source).
- [BLOCKED] Senate PTR (403), House PDFs (needs pdf lib), NIH path (405),
  SemScholar pool (429s), USPTO/EPO (registration), FTD/CUSIP map.
- [OPEN] api.data.gov signup (1 key flips Congress/GovInfo/Regulations/EIA).
- [OPEN] Lever slugs + 3 lab feeds (404s logged, never guessed).
- [OPEN] SI biweekly, FTD bulk, 13F/N-PORT bulk, GH Archive (queued).
- [WATCH] Kalshi thin books; Manifold triangulation; CLOB depth upgrade.

## Lab / science

- [OPEN] E006 gap board (baseline, needs pm calibration to matter).
- [WAITING] E007 burst panel (needs 10+10 windows), E011 silicon subset
  (Sep-09 forwards mature ~Oct), optical-attack prediction (resolves Sep 20).
- [OPEN] E008 arb pairs curation (human-confirmed, pmbot workflow).
- [OPEN] Phase 2-4 buildout (bandit, triage, predictions volume) per ML-LAB-PLAN.
- [OPEN] Rediscovery blind checks (TARGET-90D #8).
- [WATCH] Support 0.38 [0.21,0.59] — lab clean, no edge yet.

## Product (stockify, own repo)

- [OPEN] Commit/revert feedify→stockify rename; fix ml_routes NameError,
  insiders_stats, dupe MCP routes, version skew, Dockerfile, stale paths.
- [OPEN] 4 dead L0 stubs (port FROM bneck2) or delete; asserts in reality tests.
- [OPEN] Gate mutating endpoints, persist idempotency, /v1 versioning.
- [BLOCKED] Suite needs equipped box (`uv sync`).

## Ops

- [OPEN] Push umbrella (valid token; remote behind local).
- [OPEN] Human weekly 10-min review (calendar, not code).
- [WATCH] Cron heartbeat (alerts >30h gaps itself).
