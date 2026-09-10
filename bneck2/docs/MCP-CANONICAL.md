# MCP canonical list — encountered, mined, run (2026-09-10)

Honest status first: **we run zero MCP servers.** No MCP client infra on
this box (stdlib discipline, no npm haute). Everything below was mined
for recipes/endpoints and re-implemented as stdlib collectors, or queued.
"USED" means live in our loop; "MINED" means patterns ported; "QUEUED"
means documented, untouched.

## USED (live via stdlib ports, not MCP protocol)

| MCP | What it gave us | Our port |
|---|---|---|
| btopn/OpenInsider-MCP (16 tools) | FINRA CDN paths, CloudFront-403 semantics, email-UA, tinytable parse map | finra.py, openinsider.py |
| pmxt (unified PM+Kalshi wrapper) | already in third_party; venue normalization idea | polymarket.py/kalshi.py shapes |

## MINED (recipes/docs, no code run)

| MCP | What we took | Why not run |
|---|---|---|
| lzinga/us-gov-open-data-mcp (42 APIs/343 tools) | endpoint catalog for Treasury/FRED/Congress/FDA; confirmed keyless half already covered natively | TS/Node stack; our stdlib covers the keyless half |
| cmanohar/mcp-edgar, kevinkda/sec-edgar-mcp, stefanoamorelli/sec-edgar-mcp, guptaprakhariitr/sec-edgar-mcp, ChinmayKhachane/SecEdgarMCP, henrysouchien/edgar-mcp | endpoint map (submissions/XBRL/EFTS/Archives); EFTS GET shape; 10b5-1-agnostic parsing | same public endpoints hit natively; hosted ones need keys |
| birthday-tools/edgarmcp | NPORT-P holdings idea, OpenFIGI mapping, fee math reference | queued (needs key for FRED leg) |
| stefanoamorelli/shanehull fred-mcp | full 37-endpoint FRED map | needs FRED key (api.data.gov signup) |
| worldbank/data360-mcp | OData search pattern | earmarked for geo layer |
| dividor/hdx-mcp | HDX needs app id (confirmed) | queued behind id |
| GovInfo public MCP (preview) | exists; legislative corpus | queued behind api.data.gov key |
| getxapi MCP package (`npx @getxapi/mcp`) | endpoint cost table verified against live billing | we call REST directly with ledger |

## MINED this round (awesome-lists)

- arnavbhatia1/FinancialMCP (33 tools, no keys): CFTC-Socrata path +
  Google-Trends shape (Trends 429-walled) → collectors/cftc.py LIVE.
- adididitagain/finance-mcp (no keys): Frankfurter FX + World Bank macro
  → collectors/fx.py LIVE.
- blockrunai/awesome-finance-mcp index: Maverick/Alpaca/FMP/Finnhub/
  Massive/QuantConnect all need keys — catalogued, not cloned.
- appcypher/awesome-mcp-servers (archived Aug 2026 — stale index, use
  with care): ArXiv MCP, BlueSky MCP (API 403s this box), Congress MCP
  (needs key), Exa/Tavily/Brave (need keys).

## QUEUED (known, untouched)

thsmale/usaspending-mcp (we hit the API natively instead); OctoBot
prediction-market (Kalshi support unshipped); kalshitradingbot.app /
KalshiArb (commercial, unverifiable); any executor MCP (out of scope —
read-only house rule).

## Rule

Before adding an MCP dependency: check whether its underlying endpoints
are keyless HTTP. If yes, port stdlib (this box can't run Node/TS stacks
and shouldn't). MCP servers earn their place only when they add auth,
aggregation, or compute we can't trivially port.
