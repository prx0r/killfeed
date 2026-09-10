# BEAR review — GetXAPI intelligence mined (2026-09-10)

BEAR (`/home/ubuntu/BEAR`, separately owned — READ ONLY, never write there)
runs a crypto X-intelligence operation: GetXAPI gateway (budget-enforced),
evidence extractor, regime/backtest engine, source cards, recon data for 64
accounts, threads ledger. Mined for patterns + coordination, not code theft.

## Balance (checked, not spent)

GetXAPI pro_sub: **$34.83 spendable now** (`balance_total`: $34.50 plan
credits expiring Oct 7 + $0.33 permanent wallet; $5.63 used, 4,643 reqs).
At $0.001/call ≈ **~34,800 calls ≈ ~700k tweets**. Docs: 72 endpoints,
no endpoint quotas, general throttling only. Recon universe disjoint from
ours (theirs crypto, ours semis) — zero re-pay risk overlap.

## Patterns adopted (already match or now encoded)

- Budget-first: balance check + per-call ledger + approval thresholds.
  WE DON'T SPEND without explicit approval (their Rule 6 + our thread B-list).
- Raw-before-filter, author_id keys, filing-date discipline, engagement =
  snapshot, baselines-always, next-candle entry — all already our rules;
  BEAR independently validates each (their AGENTS.md Rules 1-5, backtest.py).
- Scout-cheap discipline: user_info recon ($0.001) before history pulls;
  2-week chunks; complete pagination ("never stop after 2 pages").

## Proposed NVDA scout (needs approval — exact costs)

| Step | Calls | Cost |
|---|---|---|
| user_info × 12 watchlist accounts | 12 | $0.012 |
| 2-week advanced_search × 12 (signal density probe) | 12–24 | $0.012–0.024 |
| Full history, top-3 dense only (~150pp each) | ~450 | ~$0.45 — NOT included |
| **Ask now** | | **≤$0.04** |

On approval: recon → density gate (>0.3 proceed) → history only for
passers → extractor (their v2 patterns: no asset defaults, evidence spans)
→ outcomes vs Yahoo → source cards → E-series receipts. Mirrors their
ONBOARD_SOURCE procedure at ~$0.005/source scout cost.

## Don't import

- Their crypto handles/models (different universe), live-trading executors
  (out of scope), Mongo/Supabase stacks (we're stdlib+JSONL by design).
- Never copy keys: BEAR's Rule-0 incident (hardcoded keys pushed to GitHub)
  is why our tree carries zero secrets — keep it that way.
