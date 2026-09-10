# Target: day 90 (2026-12-09) — acceptance criteria, then backcast

If the process works, day 90 looks EXACTLY like this. Anything vaguer is hope.

## Acceptance criteria (all checkable from logs)

1. **Backtest significant**: panel ≥12 complete forward dates, walk-forward
   Sharpe with 95% CI excluding 0 (or honestly negative — a clean negative
   retires the scoring variant, which is also convergence).
2. **Support rate tight**: ≥40 disposed runs, Wilson width ≤0.30.
3. **Temporal hit-rate by family** on ≥10 resolved predictions, lower bounds
   reported (not points).
4. **dB/dt nonzero somewhere**: ≥3 nodes with |dB/dt| significant vs
   measurement noise (currently all 0.000 intraday — expected, must move).
5. **Baselines mature**: ≥10 tickers with n≥20 passes (cadence-relative
   gates replace 2 absolute thresholds).
6. **Variables ≥50** with statuses; dead list ≥15 (proof of elimination).
7. **Reflect memos weekly** (12 memos), each with ≥1 redirect that changed
   subsequent receipts.
8. **Rediscovery green**: 3 seeded known-true relations surfaced blind.
9. **Zero silent stops**: heartbeat gap never >30h (monitored, see below).

## Pre-mortem: it's day 90 and we failed. Why? (top causes → fixes TODAY)

1. **Cron died quietly** (most likely). Fix: heartbeat file + staleness
   gate — every pass writes `data/heartbeat.json`; oneclick REFUSES to
   report "all OK" if the previous heartbeat is older than 30h without
   saying so loudly; weekly human checks the log (calendar it).
2. **Thresholds rotted** (regimes moved, gates didn't). Fix: cadence
   baselines already started; extend rule — no absolute gate survives
   past n=20 baseline without a relative twin.
3. **Narrative capture** (lab confirms thesis). Fix: mandatory monthly
   red-team receipt (argue the opposite; scored like any hypothesis) +
   E005-style refutes celebrated in review.
4. **Backtest never matures** (panel stuck at 1 date/window). Fix: backfill
   honestly NOW (reconstructed scores labeled + real Yahoo forwards) so
   day-1 already has 12 dates; live passes extend it.
5. **Single box dies** (disk, ban, outage). Fix: umbrella pushed (done);
   add weekly `stage_zip` + outbox mail artifact so the tree survives the
   box. Data logs are small (JSONL) — include them in the zip (done).

## Backcast: starting conditions to set TODAY

- [x] Heartbeat + staleness gate (this doc → implemented below).
- [x] Honest panel backfill (reconstructed scores, real forwards, graph
  hash per row for audit).
- [x] Red-team hypothesis slot (monthly, scored).
- [ ] Human weekly 10-min review (owner's calendar, not code).
- [ ] Rediscovery seeds planted (3 known-true relations as blind checks).
