# Next Steps — Levin / economic-thesis / Stockify / bneck program (2026-09-10)

Scope: everything except `breadup` and `freaktown` (excluded per instruction).
Covers: `stockify`, `bneck`, `bneck2`, plus all import `.zip` files reviewed this session.

## 1. What you want overall (read-back)

One machine that turns **frontier-science evidence into mispriced-cash-flow positions**:

```
papers / patents / benchmarks / GitHub / capex / procurement / supply /
earnings / insider  →  belief over future worlds  →  causal propagation
→  cash-flow exposure  →  minus market-implied pricing  →  rank / backtest
```

With two signature theses:

- **Obsolescence arbitrage** (`bneck2/docs/economic-thesis.md`):
  `Alpha = (P_you − P_market) × cash-flow exposure`.
  Don't pick winners; find incumbent pools that can't survive most plausible worlds.
  Song Ma obsolescence (~7%/yr), Haddad/Ho/Loualiche competitor underreaction.
- **Access-to-reality** (`stockify/data/levin/levinite.md`, 984 lines):
  as intelligence goes abundant, value migrates to MEASURE → WRITE → GROW →
  ACT → VERIFY → CLOSE-THE-LOOP. Levin (bioprompting) + TMO/lab-in-the-loop +
  quantum-scarcity stack (GFS/FORM/KEYS > QPU) are the same thesis in biology
  and quantum.

`Stockify` is the **product surface** (feeds, X-engine, Reality Feed L0–L4).
`bneck/bneck2` are the **research engines** that should eventually score what
Stockify ingests. The two import zips are the newest upstream inputs to that
engine — unpacked and reconciled below.

## 2. Import `.zip` review (this session)

### 2a. `agi_bottleneck_intelligence_resource_pack_2026-09-10.zip` (53 KB, 36 files)

- **Status:** unpacked properly to `bneck2/imported/resource_pack/`
  (was double-nested `imported/resource_pack/<pack>/`; flattened 2026-09-10).
  Pristine copy in `bneck2/imports/`. `MANIFEST.json` sha256 **35/35 verified**.
- **Contents:** resource directory (60 GitHub/data/paper/infra links),
  frontier-lab capital-events config, GitHub repo registry, source registry,
  6 stub collectors (~300–600B URL builders), scoring/proof-ladder/OSINT models,
  schemas (`REQUIRES/ENABLES/SUBSTITUTES/KILLED_BY`), pipeline build order,
  frontier-lab + query watchlists.
- **Already merged (per `docs/IMPORT.md`, verified idempotent +0 on re-run):**
  22 frontier-lab events → `data/labs/commitments.json` (20 new),
  11 diggers → `data/labs/diggers.json` (9 new at CLAIM).
- **Verdict:** keep vendored as reference; do NOT adopt its collectors
  (ours in `collectors/*.py` are full fetch+parse, theirs are stubs).
  Schemas compatible (`KILLED_BY` → our `kill_signals`), no migration needed.

### 2b. `postagi_worldstate_kernel_2026-09-10.zip` (107 KB, 46 files)

- **Status:** unpacked properly to `bneck2/imported/postagi_kernel/`
  (was double-nested; flattened). Pristine copy in `bneck2/imports/`.
  `bneck2/kernel_bridge.py` + `scripts/import_pack.py` paths fixed;
  76/76 tests pass, bridge loads (36 demo companies, 3024 panel rows).
- **Contents:** formal research kernel — `world_graph.py` (typed DAG,
  elasticity×confidence×delay propagation), `scoring.py`
  (`world 0.55 / obsolescence 0.20 / convergence 0.15 / patentomics 0.10`),
  exact Song Ma `−[ln Cit_t − ln Cit_{t−w}]`, TechToken top-1% aggregation,
  Sternfeld convergence (q-gram/Dice 0.85, Louvain 0.85), patentomics,
  MIRAI interface, supply-chain primitives, ridge market-implied inversion,
  walk-forward backtest with costs/turnover. 12 unit tests, demo console,
  BUILD_REPORT. **Needs numpy/pandas/networkx/sklearn/scipy — absent here**,
  so it runs only via `kernel_bridge` CSV fallback (`kernel_available: False`).
- **What's genuinely new vs `bneck2/`:** the only backtest with
  point-in-time discipline; the only market-implied ridge solver; exact paper
  formulas with reproduction boundaries (`docs/papers.md`); production roadmap
  Phases A–F. `bneck2/worlds.py` has the same one-line thesis
  (`Signal_company`) but no backtest, no implied-probability solver, placeholder
  `p_market`.
- **Caveat (kernel's own warning):** demo companies/panel are
  **synthetic fixtures**, not market evidence. No production claim until
  point-in-time prices/fundamentals + survivorship-safe membership + real
  patent/research/supply signals + calibrated probabilities.
- **Verdict:** keep vendored, don't rewrite. Native-port in priority order:
  (1) backtest harness, (2) ridge implied-probabilities, (3) Ma obsolescence
  formula, (4) TechToken/convergence later (needs embeddings + GPU corpora).

### 2c. Other zips found

- `/tmp/bneck-full.zip` (178 KB, 49 files): bneck v1 engine+data+messages,
  clones excluded. Matches live `bneck/`; no action.
- `/tmp/bneck2-full.zip` ≡ `bneck2/outbox/bneck2-full.zip` (317 KB, 137 files,
  IDENTICAL): bneck2 snapshot incl. `imported/`. **Regenerate** — it still
  contains the old double-nested layout (see §4 P0).
- `pogtown/pogtown-mvp-2026-09-09.zip` (62 KB, 126 files): pogtown MVP baseline,
  sha verified `53aa4cbf…`. Not thesis-related; no action here.
- breadup/grailio zips (`/home/ubuntu/breadup/imports/…`, `/tmp/opencode/…`):
  out of scope, listed only so nothing is silently ignored.

## 3. How close each project gets (0–5, 5 = the vision above)

| Project | Score | Why |
|---|---|---|
| `stockify` | 2/5 | Only product surface: working adapters/detectors, X-engine live (<$0.01), Reality Feed L0–L4 scaffold, 675-entry Levin corpus + 118 PDFs + 325 articles, 33 thesis specs. But: rename uncommitted, leaked `sk-A5Q…` key in 3 files, 4 L0 stubs return `[]`, open mutating endpoints, tests unrunnable here. No world-model, no backtest. |
| `bneck` (v1) | 2/5 | Clean stdlib bottleneck board, 45/45 tests, live `--quant`. But: **zero git commits**, Gmail OAuth secret in `messages/`, half the engine unwired to CLI, README stale, precedents n=9. Superseded by v2. |
| `bneck2` (v2) | 3/5 | Closest to the thesis: worlds/signal screen, LabSignal, digger ladder with L4 gate, FTO, CEO ledger, collectors, SYSTEM-SPEC one-table formulas, 76/76 green. But: **not a git repo**, `p_market` placeholders, single-day readings, kill-writer unwired, top commitments score 0.00, no backtest, no TS/toolchain deps. Research prototype, not investable. |
| kernel (vendored) | 3/5 as spec, 1/5 as runnable | Best formalism + only real backtest protocol, but unrunnable here (deps) and demo data synthetic. Use as port spec, not runtime. |
| resource pack (merged) | 4/5 as input, n/a as system | Did its job: 20 commitments + 9 diggers merged, idempotent. Remaining value is the 60-link clone queue in `docs/RESOURCES.md`. |

Nothing today can run the vision end-to-end (evidence → worlds → exposure →
implied-price → rank → backtest) on real point-in-time data. That is the gap.

## 4. Where we go from here

### P0 — stop the bleeding (days)

1. **Secrets:** rotate Gmail OAuth (`bneck/messages/22-*`) + `sk-A5Q…`
   (`stockify/api.py:909,1127`, `services/thesis_engine.py:150`); env-only,
   add secret scan to CI.
2. **Git:** `bneck` initial commit (gitignore token/credential patterns);
   `bneck2` `git init` + first commit (respect SKIP = third_party/__pycache__);
   commit stockify `feedify→stockify` rename; fix Dockerfile, `.env.example`
   watchlist path, `mcp-config.json` URL.
3. **Regenerate `bneck2/outbox/bneck2-full.zip`** from flattened tree
   (current outbox predates §2 fix).
4. **Packaging:** add `bneck2/pyproject.toml` + `pytest.ini`
   (`testpaths=tests`, `norecursedirs=third_party imported outbox`);
   `uv sync`, get `pytest -q` green in stockify; refresh BUILD_REPORT +
   README service map (23 services, not 7).

### P1 — make it a real evidence machine (weeks)

5. **Kill-feed (bneck2 build-queue #1–3):** SEC inventory parser →
   `evidence.log_kill_observation`; OpenAlex velocity per node
   (AttackIntensity); pmxt-based pm clock replacing `p_market` stubs;
   backfill `data/beliefs/claims.json`.
6. **Port kernel in order:** backtest harness (point-in-time, turnover, costs)
   → ridge implied-probabilities → Ma obsolescence → TechToken/convergence.
   Keep `kernel_bridge.describe()` honest until each lands.
7. **Stockify:** implement or delete the 4 L0 stubs; real asserts in
   `test_reality_feed`; fix `ml_routes` import + `insiders_stats` aggregation +
   duplicate MCP routes; gate `ingest/mcp-call/chat` + MCP allowlist; persist
   idempotency; version API under `/v1`.
8. **De-dupe docs:** merge the two 604-line thesis copies; single corpus home
   (today triple-copied 675-entry Levin JSON); archive daily `status --quant`
   briefs to start the 90-day backtest clock.

### P2 — prove it (months)

9. Qlib-style harness + river drift detection once 90 days of briefs exist;
   paper portfolio vs factor/sector baselines before any capital.
10. Postgres-live + Docker + scheduled encrypted backups + restore drill;
    Cloudflare P0 edge items; Nakama JWT replacing header-trust.
11. Levin corpus → queryable evidence graph (citation/claim extraction with
    lineage), not a metadata JSON + PDF pile.

### Explicit non-goals (unchanged)

Live capital, Docker/GPU builds on this box, media rendering, R2 asset
hosting, Unreal/Expo, Audio2Face — scaffolds only until P0–P1 land.
