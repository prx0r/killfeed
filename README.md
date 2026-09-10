# killfeed — evidence → worlds → mispriced cash flows

Umbrella repo. Thesis: **as intelligence goes abundant, value migrates to
privileged access to reality** — find future worlds whose probabilities are
mispriced, then find today's cash flows that cannot coexist with those worlds.

## Layout

- `bneck2/` — main engine (second-gen bottleneck/obsolescence engine).
  Stdlib-only, $0 data. `scripts/killfeed.py [--live]` runs the
  collect → evaluate → verdict-log loop (SEC / OpenAlex / Polymarket).
  102 tests green. Start with `bneck2/README.md`, then
  `bneck2/docs/SYSTEM-SPEC.md` (all formulas in one table).
- `bneck/` — v1 engine (superseded by bneck2; kept for the message archive
  and precedents). 45 tests.
- `stockify/` — product surface: source adapters → detectors → ranked feeds
  (web/PWA/RSS/MCP), X-engine, Reality Feed L0–L4, Levin corpus
  (`data/levin/`: 675-entry metadata + PDFs + `levinite.md` thesis).
- `NEXT-STEPS.md` — program status, per-project scores, P0/P1/P2 roadmap.
- `HANDOVER.md` — prior session handover (vault, pogtown, freaktown).

## Quick start (engine)

```bash
cd bneck2
/usr/bin/python3 scripts/status.py --quant --belief
/usr/bin/python3 scripts/revealed.py
/usr/bin/python3 scripts/killfeed.py --live --max-nodes 3 --no-write  # dry run
/usr/bin/python3 -m unittest discover -s tests
```

## Hygiene notes

- `third_party/` clones excluded (URL manifests in `docs/RESOURCES.md`).
- Live secrets must never be committed — rotate any exposed keys
  (see NEXT-STEPS.md P0).
