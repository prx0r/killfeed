# Convergence plan — logging, possibility accounting, and reading what we have

Companion to `ML-LAB-PLAN.md` (the phases). This doc answers three questions
with numbers, not hope: how every byte is logged, how the space provably
shrinks, and what our existing logs already rule out.

## 1. Logging spec (canonical logs — append-only JSONL unless noted)

| Log | Schema | Writer | Retention/rebuild |
|---|---|---|---|
| `data/beliefs/kill_observations.jsonl` | ts, node_id, signal, measured, threshold, verdict∈{TRIGGERED, NOT TRIGGERED, INCONCLUSIVE}, source | killfeed (live), experiments never | forever; non-firings are data |
| `data/beliefs/signals.jsonl` | ts, ticker, type, direction, strength, confidence, source | killfeed pm/whale legs | forever |
| `data/bottlenecks/severity_history.jsonl` | ts, node_id, B | killfeed live pass | forever (dB/dt needs it) |
| `data/backtest/panel.jsonl` | date, ticker, score, forward_return\|null | oneclick | forever; forwards fill in |
| `experimentation/receipts.jsonl` | ts, hyp, inputs_hash, n, verdict, directional_only, result | lab.receipt | forever, immutable |
| `experimentation/variables.jsonl` | id, def, measures_via, status | agent (LLM) | dead rows kept, never deleted |
| `predictions.jsonl` (Phase 4) | var, target, direction, resolve_after, resolved | agent + cron resolver | forever |
| `data/beliefs/claims.json` | claims + three-clock meta (JSON snapshot) | seed_claims (seed rows only) + hand | hand rows never auto-touched |
| `data/beliefs/sec_baselines.json` | ticker → [{ts, form4, deal}] cap 30 | killfeed live | rolling |
| `docs/ONECLICK-*.md`, `docs/archive/` | run reports | oneclick | keep all (history) |

Rules: collectors never raise (INCONCLUSIVE > invented). INCONCLUSIVE never
counts as elimination. Prereg amendments are new receipt rows, not edits.
Projections (`report`, boards) rebuild purely from logs — deleting one
destroys nothing (cg §56 idea, tested by re-running).

## 2. How convergence actually works (the math, not the vibe)

The possibility space is made countable, then counted down:

1. **Cells.** Unit of search = (node × signal-leg × window) verdict cells
   + hypothesis verdicts + variable statuses. `lab.verdict_coverage()`
   counts tested vs triggered cells; `lab.possibility_ledger()` counts
   hypotheses confirmed/refuted/open.
2. **Elimination is the progress metric**, not confirmation. Each REFUTED
   receipt retires ≥1 possibility permanently (dead variables/hypotheses
   stay listed so we never re-search them). Confirmations promote to
   triage; they don't close anything.
3. **Support rate with Wilson intervals** (`lab.support_rate`,
   `lab.wilson`): fraction of disposed runs CONFIRMED, always with 95%
   bounds. Small n ⇒ wide bounds ⇒ no victory laps (today: 0.38, CI
   [0.21, 0.59] — consistent with coin-flip; said out loud).
4. **Bandit convergence** (Phase 2): arm means + counts in receipts;
   converged = best arm's lower bound clears the rest for k=3 rounds
   (UCB-style, no new code needed — read it off the ledger).
5. **Multiple-testing control**: every screen reports raw n + Holm-adjusted
   threshold; unadjusted screens are labelled exploratory in the receipt.
6. **Temporal hit-rate** (Phase 4): per-family hits/n with Wilson intervals;
   weight = lower bound, not point estimate (a 2/3 is worth ~0.21, not 0.67).
7. **Stopping rules**: variable dead after 3 independent refutations;
   hypothesis resolved at CONFIRMED+triaged or REFUTED×2 methods;
   track converged per (4); track abandoned only by reflect memo with reason.
8. **Anti-hope rules**: n<30 directional-only; INCONCLUSIVE ≠ progress;
   repeats don't inflate n (ledger counts unique hypotheses separately
   from runs); prereg deltas logged, never edited.

Convergence = open count falling while decided count rises with stable or
rising lower bounds. That is checkable every pass from the ledger alone.

## 3. What our logs already prove (computed 2026-09-10, not asserted)

- **48 cells tested, 3 triggered (6.25%)**: accelerators:sec-burst,
  optical_io:sec-burst, optical_io:openalex-attack. 417 non-firings are
  417 ruled-out triples — the quiet majority is the falsifier discipline
  working, and it bounds where NOT to look.
- **Hypotheses: 9 total — 2 confirmed, 4 refuted, 3 open** (37 runs).
  Refuted so far: burst→drift (E001), fuzzy arb (E003), plain severity
  correlation (E005), penalized variant (E009). Each retires a search
  direction permanently.
- **Support 0.38 [0.21, 0.59]** — indistinguishable from chance at this n.
  Correct reading: the lab runs cleanly; it has not yet found edge. Any
  claim otherwise would be hope, not math.
- **E004 2/3 (Wilson lower ~0.21)**: whale consensus worth tracking, not
  betting. E002: attack+crowded mapping holds as mapping evidence (n=4).
- **Panel: 13 scores, 0 complete** — backtest clock started, matures in days.
- **Severity: 116 points, dB/dt compounding** — velocity becomes nonzero
  as readings move; currently static intraday (honest zero, not missing).
- **Open frontier, counted**: 9 open unknowns, 9 candidate variables,
  3 queued feeds (Senate, NIH, SemScholar-pool), placeholders in p_market.

## 4. Reading protocol (every pass, in order)

1. `experiment.py report` → ledger deltas (what retired? what opened?).
2. `verdict_coverage()` → new triggered cells? (alert) / coverage growth?
3. Support rate + Wilson — widening or tightening?
4. Panel completeness → backtest the week it hits 2 dates.
5. Reflect memo weekly: arm means, recurring confounds, resurrection
   candidates. The memo is a receipt, not a chat message.
