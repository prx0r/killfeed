# ML-lab plan — LLM-driven possibility-space exploration (pre-pipeline)

Goal, stated exactly: before any ML pipeline correlates variables, figure out
**what the variables are** — including ones no fixed schema would contain,
including ones only an LLM could propose. Then correlate, then triage
causally, with the LLM proposing and code disposing at every gate.

## 0. What the literature says works (arXiv, Sep 2026 cut)

- **HEP** (2607.09195): hypotheses as persistent audited objects; belief moves
  only on attached evidence; de-novo/inspired-by/refine/merge generation;
  lifecycle proposal→supported/refuted/dormant. *We already do this*
  (`lab.py` + claims). Keep it; add refine/merge ops.
- **DiscoPER** (2607.01131): Propose–Evaluate–Reflect; hypotheses as
  EXECUTABLE CODE over real data; held-out validation required (72.7%
  support, 8/9 patterns); second-order reflection over accumulated claims
  redirects search; classical causal discovery only 1/9 (edge spaces can't
  express interactions). *Core loop to copy.*
- **HyGRAIL** (2609.02056): cheap triage (GNN) routes only ambiguous cases
  to expensive LLM review (-54% calls); compact two-sided evidence wins.
  *Our version: stdlib stats triage → agent/LLM review only the frontier.*
- **LLM-FE** (2503.14434): evolutionary program search, island model,
  Boltzmann sampling from a scored memory of (program, score) pairs.
  *Our receipts.jsonl already IS that memory — add island tags + sampling.*
- **REFeat** (2506.20357): 6 reasoning types (inductive, deductive,
  abductive, analogical, counterfactual, causal) as bandit arms, reward =
  validation gain. Fixes LLM repetitiveness. *Adopt verbatim for proposing.*
- **Rogue One** (2511.15074): Scientist/Extractor/Tester agents,
  flooding-then-pruning, justifications REQUIRED per feature, RAG grounding.
  *Adopt flooding + justification rule.*
- **FAMOSE** (2602.17641): ReAct propose→code→evaluate→refine; feature
  SELECTION by algorithm (mRMR), never by LLM. *Adopt: LLM proposes, mRMR
  (stdlib port) disposes.*
- **BioDisco**: dual-mode evidence (KG + literature), Critic scores
  (novelty/verifiability/relevance/significance), temporal evaluation
  (predict post-cutoff discoveries), Bradley–Terry judging with uncertainty.
  *Adopt temporal validation — our daily cron makes it real.*
- **TLVD** (WWW'26): latent-variable discovery via multi-agent proposals +
  web evidence tracing (+32% acc). *Adopt for the residual-clustering phase.*
- **Effect-level validation** (2602.08340): admissibility-first — graphs are
  hypotheses; estimate effects only where identifiable; placebo/subsampling
  refutation; different structures converging on one effect > graph recovery.
  *Adopt as the causal gate.*
- **CIKA** (2605.07600): LLM-as-do-operator for interventional probes.
  *Adopt for concept-level probes, not market claims.*

## 1. The pipeline (5 phases + reflect)

```
Phase 0  VARIABLE TERRAFORMING  (the step before the pipeline)
Phase 1  FLOODING               (many candidates, cheap screen)
Phase 2  REASONING BANDIT       (6 lenses propose compounds)
Phase 3  CAUSAL TRIAGE          (effect-level gates, LLM never verdicts)
Phase 4  TEMPORAL VALIDATION    (preregister → resolve on future passes)
         REFLECT (2nd order, periodic: gaps/confounds/compounds redirect)
```

### Phase 0 — Variable Terraforming (this is the novel bit)

The agent (LLM) proposes candidate OBSERVABLES, not correlations. Each
proposal must state: definition, which collector(s) can measure it (or a
spec for a new one), expected base rate, and what would make it meaningless.
Sources of proposals, in order:
1. Cross-stream residuals (where do our current measures disagree? E005-style).
2. Thesis-derived (goated §§1-18: each alpha extension implies observables).
3. Latent residuals (TLVD-style: cluster unexplained verdicts, name the ghost).
4. Reasoning-lens sweep (§2): same streams, six different questions.
Registry: `experimentation/variables.jsonl` {id, def, measures_via,
status: candidate/active/dead}. Dead variables stay listed (don't re-propose).

### Phase 1 — Flooding + cheap screen

Generate dozens of candidate variables/transforms (Rogue One flooding).
Screen each with stdlib stats vs targets (forward returns, verdict rates,
severity deltas): Spearman + Holm correction for multiple testing.
Prune hard. Justification required per survivor (one sentence, mechanistic).

### Phase 2 — Reasoning bandit (REFeat, no numpy needed)

Arms: inductive / deductive / abductive / analogical / counterfactual /
causal. Each arm = a prompt template proposing compound variables
(ratios, interactions, thresholds, divergences). Reward = Phase-1 gain.
Boltzmann sample arms; track arm means in receipts. This is where
"undefinable correlations only an LLM could figure out" live: analogical
and abductive arms routinely propose relations no schema contains
(literature: 2-3× semantic diversity vs single-prompt).

### Phase 3 — Causal triage (effect-level, admissibility-first)

For each surviving variable→target pair, run gates IN ORDER, stop at first
fail (HyGRAIL routing: only pairs passing cheap gates reach LLM review):
1. Temporal precedence (cause window strictly before effect window).
2. Placebo (randomized timestamps kill it → dead).
3. Subsampling stability (halves agree in sign).
4. Confound check (does node/sector/time explain both? partial Spearman).
5. LLM review ONLY here: propose the mechanism in words; a second pass
   attacks it (Critic). Both recorded. LLM never moves belief — gates do.

### Phase 4 — Temporal validation (our unfair advantage)

Preregister directional predictions with resolution dates (cron resolves):
`predictions.jsonl` {var, target, direction, resolve_after, resolved}.
Hit-rate per variable family compounds into Skill-like weights (cf.
forecasters.py). This is BioDisco's temporal eval, running for free on
our daily loop.

### Reflect (weekly, 2nd order à la DiscoPER)

Meta-pass over receipts: which arms/steams produce? which confounds recur?
which dead variables deserve resurrection under new data? Output: redirect
memo (also receipt-logged) + merged/refined hypotheses (HEP ops).

## 2. How the LLM fits without an LLM key on the box

This box has no pip and no funded LLM key. So: the AGENT (you, the next
session) is the proposer/critic — run one phase per session, code executes
everything checkable. If a vault LLM key appears (OPENCODE_API_KEY exists
in oracle; needs funding/scope check + spend caps), the proposer step can
run inside cron with per-pass call budgets, HyGRAIL-style (stats triage
first, LLM only on the ambiguous frontier). Never LLM-as-verdict.

## 3. Concrete build order (files)

1. `experimentation/variables.jsonl` + `bneck2/variables.py`
   (register/deprecate/sample) — Phase 0 store.
2. `bneck2/stats.py` — Spearman, Holm, partial-rank, mRMR-greedy (stdlib).
3. `bneck2/reason.py` — 6 prompt templates + bandit state in receipts.
4. `bneck2/triage.py` — precedence/placebo/subsampling/confound gates.
5. `predictions.jsonl` + resolver in `scripts/oneclick.py` (resolve-due step).
6. `scripts/reflect.py` — weekly meta-pass → redirect memo.
7. Seed variables from E001–E009 residuals + goated §§1–18 (≥30 day one).

## 4. Evaluation (when is the lab working?)

- Support rate (DiscoPER metric): fraction of proposed variables surviving
  Phase 1 with justification. Target ≥0.5 (below = flooding garbage).
- Temporal hit-rate by family (Phase 4) with n shown, PILOT-labelled.
- Diversity: mean pairwise textual distance of proposals (anti-repetition).
- Cost: LLM calls per survivor (HyGRAIL metric) once keyed; until then,
  agent-minutes per survivor.
- Rediscovery check: seed 3 known-true relations; lab must surface them blind.

## 5. Anti-patterns (literature-backed)

- No graph-recovery worship: different structures, same effect = fine (§effect).
- No LLM selection: mRMR/algorithm prunes, LLM proposes (FAMOSE).
- No benchmark-weighted evidence (transfer tiers stay).
- No p-hacking: preregister + Holm + held-out; receipts immutable.
- No resurrecting dead variables without new data.
- No trading/executors. Ever. (unchanged house rule)
