#!/usr/bin/env python3
"""Stockify $0 live price poller — Yahoo (stocks) + CoinGecko (crypto), stdlib only.

Why not Stooq: Stooq now returns a JS browser-check from this network,
so live q/l + daily CSV are blocked. Yahoo v8 chart is free, keyless,
and verified live from this box (IONQ 38.14, -5.7% on 2026-09-09).

Cost: $0 — no API keys, no paid tiers.
Usage (cron every 5 min):
    */5 * * * * cd /home/ubuntu/stockify && /usr/bin/python3 scripts/poll_prices.py >> /tmp/stockify-prices.log 2>&1

Outputs:
    data/prices.jsonl       append-only history (one line per poll)
    data/prices_latest.json latest snapshot (cheap cache for API/UI)
"""
from __future__ import annotations

import datetime
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_HIST = ROOT / "data" / "prices.jsonl"
OUT_LATEST = ROOT / "data" / "prices_latest.json"

# Physical-bottleneck basket: quantum + edge-AI choke points.
# Canonical -> Yahoo symbol (EU names need .DE/.PA suffix on Yahoo).
YAHOO_MAP = {
    "IONQ": "IONQ", "RGTI": "RGTI", "QBTS": "QBTS", "QNT": "QNT",
    "GFS": "GFS", "FORM": "FORM", "KEYS": "KEYS", "COHR": "COHR", "LITE": "LITE",
    "CEVA": "CEVA", "POWI": "POWI", "SYNA": "SYNA", "SLAB": "SLAB",
    "NVDA": "NVDA", "ARM": "ARM", "LSCC": "LSCC",
    "LPK": "LPK.DE", "SMHN": "SMHN.DE", "SOI": "SOI.PA",
    "ALNT": "ALNT", "TKR": "TKR", "NOVT": "NOVT", "MU": "MU", "DRAM": "DRAM",
}
STOCKS = list(YAHOO_MAP)
CRYPTO_IDS = {
    "ETH": "ethereum",
    "QRL": "quantum-resistant-ledger",
    "QANX": "qanplatform",
    "CELL": "cellframe",
    "MINIMA": "minima",
}

UA = {"User-Agent": "Mozilla/5.0 (Stockify-poller; +https://github.com/prx0r/feedify)"}


def fetch_json(url: str, timeout: int = 20) -> dict | list | None:
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8", "replace"))
    except Exception as exc:  # cron-safe: never raise
        print(f"WARN fetch failed {url[:90]}: {exc}", file=sys.stderr)
        return None


def poll_stock(ticker: str) -> dict:
    symbol = YAHOO_MAP.get(ticker, ticker)
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(symbol)}?interval=5m&range=1d"
    body = fetch_json(url)
    try:
        meta = (body or {}).get("chart", {}).get("result", [{}])[0].get("meta", {})
        price = meta.get("regularMarketPrice")
        prev = meta.get("chartPreviousClose") or meta.get("previousClose")
        pct = meta.get("regularMarketChangePercent")
        if price is None:
            return {"ticker": ticker, "error": "no price in meta"}
        if pct is None and prev:
            pct = round((price - prev) / prev * 100, 3) if prev else 0
        return {
            "ticker": ticker,
            "price": round(float(price), 2),
            "pct_1d": round(float(pct or 0), 3),
            "prev_close": prev,
            "day_high": meta.get("regularMarketDayHigh"),
            "day_low": meta.get("regularMarketDayLow"),
            "volume": meta.get("regularMarketVolume"),
            "asof": datetime.datetime.fromtimestamp(
                meta.get("regularMarketTime", 0),
                tz=datetime.timezone.utc,
            ).isoformat() if meta.get("regularMarketTime") else None,
            "venue": "yahoo",
        }
    except Exception as exc:
        return {"ticker": ticker, "error": str(exc)[:120]}


def poll_crypto() -> dict[str, dict]:
    ids = ",".join(CRYPTO_IDS.values())
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        f"?ids={urllib.parse.quote(ids)}&vs_currencies=usd&include_24hr_change=true"
    )
    body = fetch_json(url) or {}
    out: dict[str, dict] = {}
    for ticker, cid in CRYPTO_IDS.items():
        row = body.get(cid) or {}
        if "usd" not in row:
            out[ticker] = {"ticker": ticker, "error": "no data", "venue": "coingecko"}
            continue
        out[ticker] = {
            "ticker": ticker,
            "price": row["usd"],
            "pct_1d": round(float(row.get("usd_24h_change") or 0), 3),
            "venue": "coingecko",
        }
    return out


def main() -> int:
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    tickers: dict[str, dict] = {}
    for t in STOCKS:
        tickers[t] = poll_stock(t)
    tickers.update(poll_crypto())
    ok = sum(1 for v in tickers.values() if "price" in v)
    snapshot = {"ts": now, "cost": "$0 (yahoo+coingecko, keyless)", "tickers": tickers}
    OUT_HIST.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_HIST, "a", encoding="utf-8") as f:
        f.write(json.dumps(snapshot) + "\n")
    with open(OUT_LATEST, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2)
    ionq = tickers.get("IONQ", {})
    print(f"{now} ok={ok}/{len(tickers)} IONQ={ionq.get('price')} {ionq.get('pct_1d')}%")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
