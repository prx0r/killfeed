# Canonical insider + data references — where everything comes from

One table per family: exact source, access, what it yields, status here.
Rule: primary government/venue source first, aggregator only when primary
is blocked; aggregator rows are always labelled as such.

## Insider trading (Form 3/4/5)

| Source | Access | Yields | Status |
|---|---|---|---|
| SEC submissions JSON (`data.sec.gov/submissions/CIK*.json`) | keyless | filing history, forms, dates | LIVE (sec.py) |
| SEC Form 4 XML bodies (Archives) | keyless, **host-blocked here** | Tx codes P/S/A/M/F with prices | via OpenInsider instead |
| OpenInsider screener (plain HTTP) | keyless | buys/sells/clusters/officers, P-code discipline | LIVE (openinsider.py) |
| Nasdaq insider aggregates | keyless | buy/sell counts 3m/12m | LIVE (nasdaq.py) |
| Quiver insider API | key | normalized Form 4 | QUEUED (needs key) |
| Senate PTR (efdsearch) | session-walled | congressional trades | BLOCKED (u-009) |
| House Clerk ZIP index | keyless | filing metadata (1609 rows) | LIVE meta; PDFs queued |
| CongressInvests / Disclosed Capitol / capitol-api | free tier / self-host | normalized congress trades | QUEUED (endpoints 404 / runtime) |

## Institutional holdings (13F world)

| Source | Access | Yields | Status |
|---|---|---|---|
| **Nasdaq holders API** | keyless | 6,157 holders/ticker w/ changes, ownership % | LIVE (nasdaq.py) |
| SEC 13F bulk ZIPs | keyless, **host-blocked here** | full manager×holding panels | QUEUED (needs mirror) |
| NVDA 13F (hand-seed + forward diff) | manual, dated | $63.4B table → tracked basket | LIVE (E032) |
| N-PORT / WhaleWisdom / BamSEC | key / human UI | fund portfolios, filing UX | QUEUED |

## Employees / hiring

| Source | Access | Yields | Status |
|---|---|---|---|
| Greenhouse boards API (per-board slug) | keyless | postings + cluster mix | LIVE (1 board verified; slugs vary) |
| Lever postings | keyless | same (slugs 404'd so far) | QUEUED |
| LinkedIn | walled | — | NOT PURSUED |

## Everything else (pointers; details in RESOURCES-CANONICAL)

Filings full-text: EFTS search-index (LIVE). Fundamentals: XBRL
companyfacts (LIVE). Shorts: FINRA Reg SHO (LIVE) + SI biweekly (queued).
Beliefs: PM/Kalshi/Manifold + CLOB depth + Kalshi candles (LIVE).
Research: OpenAlex group_by (LIVE), bioRxiv/Crossref/HN/HF/OSTI (LIVE),
SemScholar (degraded pool). Money: USAspending/Grants/NSF (LIVE).
Permissions: FedRegister/openFDA/trials/House (LIVE). Macro: BLS/Treasury/
WorldBank (LIVE). Prices: Yahoo/CoinGecko + caches (LIVE). X: keyed
(BEAR patterns adopted; scout proven at $0.131).
