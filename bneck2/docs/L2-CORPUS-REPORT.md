# L2 / Microstructure Corpus — crawler report 2026-09-10

Source: external crawl for a legitimate public 2-year LSE Level-2/MBO dump (fish/Mantis).
Bottom line: **no clean public LSE L2/MBO dump exists.** DeepLOB authors state their 1y LSE data is not publicly accessible. Strategy: pretrain on huge public books, calibrate on limited exact-stock UK data.

## Confirmed LSE research corpora (not downloadable — benchmarks only)
- DeepLOB 2017: 10-level LOB, LLOY/BARC/TSCO/BT/VOD, Jan–Dec 2017, ~134M observations. Transfer-tested to HSBC/GLEN/CNA/BP/ITV.
- 2018 follow-up: MBO → reconstructed L10, 169M+ samples, same 5 names.
- Action: contact Zhang/Zohren/Roberts — ask for derived features/embeddings/access, not raw data.

## Downloadable training substrate (free, licensed)
| Dataset | What | Size/License |
|---|---|---|
| China A-share L2 (HF) | full depth | enormous |
| `cooronxon/AShareTickData` (HF) | ≥5-level bid/ask px+size | 64.4M rows, MIT |
| Hyperliquid L4 (Zenodo 18184441) | every book diff BTC/ETH/SOL + orders/trades | 195 GB |
| FI-2010 | Nordic L10 | public copies |
| LOBSTER samples | US L1–L50 | samples |
| Nasdaq ITCH/PCAP samples | true order events | samples |
| Cboe Europe samples | European PITCH | samples |
| `CarlosSilva1/ustech-ticks` (HF) | Nasdaq-100 CFD ms bid/ask | ~376M ticks, CC-BY-4.0 |
| S&P 500 CFD ticks (HF) | ms bid/ask | ~90M ticks, CC-BY-4.0 |
| `Traders-Lab/TroveLedger` (HF) | FTSE100 incl. minute/hour/day OHLC | ⚠️ maintainers warn intraday has open issues — validate before ingest; datasets-server `/rows` returns 501 (needs direct parquet, no libs on box) — BLOCKED for now |
| `cooronxon/AShareTickData` (HF) | ≥5-level bid/ask px+size | 64.4M rows, MIT — ✅ verified via `/rows` 2026-09-10 (keys bid1-5/ask1-5_price+size, ms ts, XSHE codes) |

## UK domain adaptation
- TroveLedger FTSE100 bars (after validation) + IBKR/Cboe live capture of exact names (start now, accumulate) + DeepLOB/MBO papers as domain sanity checks.
- Paid fallback ranking: Cboe Europe PITCH (2011+) > ICE LSE history > LSE Rebuild Order Book (authoritative, likely expensive). Buy history only if ablation proves L2 adds OOS PnL over daily+1m+trades+spread+events.

## Key design confirmations
- DeepLOB transfer learning (5 UK stocks → 5 unseen UK stocks) supports pretrain-then-calibrate over per-stock 2y histories.
- **BDLOB**: Bayesian uncertainty on 2017 LSE data, position size ∝ 1/uncertainty — independent convergence with our `bneck2/advise.py` (NORTHSTAR-5: allocation = signal × confidence). Our Sequence generalizes it from short-horizon classification to multi-horizon replanned trajectories.
- `Al00f/LondonStocks` (HF) is NOT L2 — close+volume matrices only. Skip.
- Next crawler pass: file fingerprints (GitHub blobs/releases/LFS, university storage, abandoned S3/GCS in notebooks, thesis appendices, competition caches, Zhang/Zohren code lineage) — public/licensed only.

## bneck2 wiring
- E049 HF panel (`paperswithbacktest/Stocks-Daily-Price`, coarse daily) covers the days-to-months horizon leg of this plan.
- Candidate next collectors (validate first): TroveLedger FTSE100 minutes, AShareTickData L2 snapshots — both via datasets-server `/rows` (pattern already proven in `scripts/hf_panel.py`).
