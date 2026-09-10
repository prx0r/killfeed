# M-QUEUE — money tasks (need EXPLICIT approval + amount)

Rule: no spend without a quoted amount and a yes. Ledger every cent
(data/x/ledger.jsonl pattern for X; costs noted per item otherwise).
Balance context: GetXAPI ~$34.83 (expires Oct 7); everything else $0.

## Proposed (demo of approval format — reply `approve M1` etc.)

- [ ] **M1 — X history pulls for density passers** · ~$0.45 · what:
  full 90d histories for ≤5 gated handles → extractor → outcomes.
  Demo response: `APPROVED M1 up to $0.50 — run recon-density-history, stop at cap, report spend.` ✅ DONE 2026-09-10 (spent $0.131)
- [ ] **M2 — LLM proposer key funding** · variable · what: fund vault
  LLM key with spend caps so cron runs proposer step unattended.
  Demo response: `APPROVED M2 $5 cap — key in vault only, per-pass call budget 10, HyGRAIL routing.` ⏳ awaiting decision
- [ ] **M3 — Backtest compute** · $0 (this box) · no approval needed in
  practice; listed so spend can't hide here. If cloud GPU ever proposed,
  it lands here first with a quote.

## Spent log

| Date | Item | Amount | Result |
|---|---|---|---|
| 2026-09-10 | X scout (1779 tweets, 5 handles) | $0.131 | E033, source cards, density gates |
