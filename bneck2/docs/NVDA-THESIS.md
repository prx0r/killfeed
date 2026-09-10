# Nvidia program thesis (saved verbatim from user message 2026-09-10)

For Nvidia, build differently from the crypto-trader feed: **X is the
interpretation/early-warning layer; SEC + Nvidia + suppliers are the
source-of-truth layer.** That fits our definition of high signal:
timestamped, falsifiable, machine-extractable evidence rather than people
repeating headlines.

Nvidia itself has become an enormous investor. Latest 13F filed August 14,
2026 for June 30 holdings disclosed ~$63.44B across Coherent, CoreWeave,
Generate Biomedicines, Intel, Nebius, Nokia, SpaceX, Synopsys. 10-Q: total
equity investments $99B + $25B commitments as of July 26.

## X watchlist (data/watchlists/nvda_x.json) with signals

1. SemiAnalysis_ (S+): rack/HBM/networking/ODM/BOM/supply constraints.
2. dylan522p (S+): component changes → who wins/loses.
3. dnystedt (S+): Taipei supply chain (Foxconn/Unimicron/PCB/TSMC eco).
4. QuiverQuant (S+ data feed): Form 4, contracts, lobbying, congressional.
5. trendforce (S): HBM/DRAM/NAND/server forecasts.
6. FoolAllTheTime (S): packaging/metrology/networking/semicap (2nd-order).
7. InvestNorthwise (S sleeper): physical sites (MW/substations/cooling).
8. theaustinlyons (A+/S): inference architecture reasoning.
9. mingchikuo (A+): supplier checks, filter for AI server/HBM/TSMC.
10. StockMKTNewz (A latency): announcements trigger, not alpha.
11. capitol2iq (A-): congressional/policy positioning.
12. nvidia (primary source): zero exclusivity, mandatory first-party.

## Primary-source stack (wiring status in bneck2)

- EDGAR submissions JSON NVDA (wired: sec.py) · companyfacts XBRL (wired:
  sec_facts.py) · 13F XML (BLOCKED: www.sec.gov 403 → seeded + tracked) ·
  10-Q Jul-26 (BLOCKED: same host) · NVentures portfolio (queued probe) ·
  OpenInsider NVDA (wired) · Quiver API (needs key) · BamSEC/WhaleWisdom
  (human UIs, queued) · SEC RSS (host-blocked, queued) · **EFTS full-text
  search (WIRED 2026-09-10: collectors/efts.py)**.
- Form-4 code discipline: P=purchase, S=sale, A=award, M=exercise,
  F=tax-withhold. openinsider.py maps explicitly (never treat acquisitions
  column as buys). Quiver: 0 open-market NVDA buys vs 60 sales/6mo.

## The capital feed (nvidia.capital thesis)

Diff 13F + 10-Q footnotes + 8-Ks + NVentures + target filings →
`NVDA → investment → CoreWeave → 5GW → Vera Rubin → HBM4 → SK Hynix/Micron
→ Coherent/Lumentum → power/grid suppliers`. Filing layer = where capital
commits; technical accounts = why; downstream filings = who benefits.
