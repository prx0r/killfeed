/* Stockify $0 edge price poller — Cloudflare Workers Cron Trigger.
 * Same basket as scripts/poll_prices.py, same free keyless sources:
 * Yahoo v8 chart (stocks) + CoinGecko simple/price (crypto).
 * No API keys burned. 288 runs/day << 100k free limit.
 */
const YAHOO_MAP = { IONQ: "IONQ", RGTI: "RGTI", QBTS: "QBTS", QNT: "QNT", GFS: "GFS", FORM: "FORM", KEYS: "KEYS", COHR: "COHR", LITE: "LITE", CEVA: "CEVA", POWI: "POWI", SYNA: "SYNA", SLAB: "SLAB", NVDA: "NVDA", ARM: "ARM", LSCC: "LSCC", LPK: "LPK.DE", SMHN: "SMHN.DE", SOI: "SOI.PA", ALNT: "ALNT", TKR: "TKR", NOVT: "NOVT", MU: "MU", DRAM: "DRAM" };
const STOCKS = Object.keys(YAHOO_MAP);
const CRYPTO_IDS = { ETH: "ethereum", QRL: "quantum-resistant-ledger", QANX: "qanplatform", CELL: "cellframe", MINIMA: "minima" };

async function pollStock(t) {
  const symbol = YAHOO_MAP[t] || t;
  const r = await fetch(`https://query1.finance.yahoo.com/v8/finance/chart/${symbol}?interval=5m&range=1d`, {
    headers: { "User-Agent": "Mozilla/5.0 (Stockify-worker)" },
  });
  if (!r.ok) return { ticker: t, error: `yahoo ${r.status}` };
  const meta = (await r.json())?.chart?.result?.[0]?.meta ?? {};
  if (meta.regularMarketPrice == null) return { ticker: t, error: "no price" };
  return {
    ticker: t,
    price: Math.round(meta.regularMarketPrice * 100) / 100,
    pct_1d: Math.round((meta.regularMarketChangePercent ?? 0) * 1000) / 1000,
    prev_close: meta.chartPreviousClose ?? meta.previousClose ?? null,
    volume: meta.regularMarketVolume ?? null,
    venue: "yahoo",
  };
}

async function pollCrypto() {
  const ids = Object.values(CRYPTO_IDS).join(",");
  const r = await fetch(
    `https://api.coingecko.com/api/v3/simple/price?ids=${encodeURIComponent(ids)}&vs_currencies=usd&include_24hr_change=true`
  );
  if (!r.ok) return {};
  const body = await r.json();
  const out = {};
  for (const [t, id] of Object.entries(CRYPTO_IDS)) {
    const row = body[id];
    out[t] = row?.usd == null
      ? { ticker: t, error: "no data", venue: "coingecko" }
      : { ticker: t, price: row.usd, pct_1d: Math.round((row.usd_24h_change ?? 0) * 1000) / 1000, venue: "coingecko" };
  }
  return out;
}

export default {
  async scheduled(event, env, ctx) {
    const tickers = {};
    for (const t of STOCKS) {
      try { tickers[t] = await pollStock(t); }
      catch (e) { tickers[t] = { ticker: t, error: String(e).slice(0, 120) }; }
    }
    Object.assign(tickers, await pollCrypto().catch(() => ({})));
    const snapshot = { ts: new Date().toISOString(), cost: "$0 (yahoo+coingecko)", tickers };

    // Optional sink 1: R2 (uncomment [[r2_buckets]] in wrangler.toml)
    if (env.PRICE_BUCKET) {
      await env.PRICE_BUCKET.put(`snapshots/${snapshot.ts}.json`, JSON.stringify(snapshot));
    }
    // Optional sink 2: POST back to VPS Stockify
    if (env.STOCKIFY_INGEST_URL) {
      await fetch(env.STOCKIFY_INGEST_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(snapshot),
      }).catch(() => {});
    }
    console.log(`poll ok IONQ=${tickers.IONQ?.price} ${tickers.IONQ?.pct_1d}%`);
  },
  // Manual check: GET / on the worker also polls once.
  async fetch() {
    const tickers = {};
    for (const t of STOCKS) tickers[t] = await pollStock(t).catch((e) => ({ ticker: t, error: String(e) }));
    Object.assign(tickers, await pollCrypto().catch(() => ({})));
    return Response.json({ ts: new Date().toISOString(), tickers });
  },
};
