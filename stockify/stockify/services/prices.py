from __future__ import annotations

import csv
import io
import json
import time
from pathlib import Path
from typing import Any

try:
    import httpx
except ImportError:  # minimal envs (cron box without venv): cache path still works
    httpx = None  # type: ignore

# Ticker -> Stooq symbol. Crypto rides CoinGecko instead.
# NOTE: Stooq is currently JS-challenged from server networks; the 5-min
# cron (scripts/poll_prices.py) + local cache below is the primary $0 path.
# Stooq/Yahoo-live remain as fallback for cache misses.
STOOQ_SYMBOLS = {
    "GFS": "gfs.us",
    "FORM": "form.us",
    "KEYS": "keys.us",
    "COHR": "cohr.us",
    "LITE": "lite.us",
    "IONQ": "ionq.us",
    "QNT": "qnt.us",
    "RGTI": "rgti.us",
    "QBTS": "qbts.us",
    "OXIG": "oxig.uk",
    # Physical-bottleneck thesis (NVIDIA eats orchestration, not wafers):
    "CEVA": "ceva.us",
    "POWI": "powi.us",
    "SYNA": "syna.us",
    "SLAB": "slab.us",
    "NVDA": "nvda.us",
    "ARM": "arm.us",
    "LSCC": "lscc.us",
    "LPK": "lpk.de",
    "SMHN": "smhn.de",
    "SOI": "soi.pa",
    # Embodiment branch (motors/reducers/encoders) + memory indicator:
    "ALNT": "alnt.us",
    "TKR": "tkr.us",
    "NOVT": "novt.us",
    "MU": "mu.us",
    "DRAM": "dram.us",
}

# Canonical ticker -> Yahoo chart symbol (Yahoo is the live $0 source).
YAHOO_SYMBOLS = {
    "GFS": "GFS", "FORM": "FORM", "KEYS": "KEYS", "COHR": "COHR",
    "LITE": "LITE", "IONQ": "IONQ", "QNT": "QNT", "RGTI": "RGTI",
    "QBTS": "QBTS",
    "CEVA": "CEVA", "POWI": "POWI", "SYNA": "SYNA", "SLAB": "SLAB",
    "NVDA": "NVDA", "ARM": "ARM", "LSCC": "LSCC",
    "LPK": "LPK.DE", "SMHN": "SMHN.DE", "SOI": "SOI.PA",
    "ALNT": "ALNT", "TKR": "TKR", "NOVT": "NOVT", "MU": "MU", "DRAM": "DRAM",
}

# CoinGecko ids for the crypto leg.
COINGECKO_IDS = {
    "ETH": "ethereum",
    "QRL": "quantum-resistant-ledger",
    "QANX": "qanplatform",
    "CELL": "cellframe",
    "MINIMA": "minima",
}

# 5-min cron cache written by scripts/poll_prices.py ($0, Yahoo+CoinGecko).
LOCAL_CACHE_PATHS = ("data/prices_latest.json", "/home/ubuntu/stockify/data/prices_latest.json")
LOCAL_CACHE_MAX_AGE_S = 20 * 60

CACHE_TTL_S = 15 * 60
_cache: dict[str, tuple[float, dict]] = {}


def _cached(key: str, loader):
    now = time.time()
    hit = _cache.get(key)
    if hit and now - hit[0] < CACHE_TTL_S:
        return hit[1]
    try:
        data = loader()
    except Exception:
        return hit[1] if hit else {}
    _cache[key] = (now, data)
    return data


def _local_cache_moves(tickers: list[str]) -> dict[str, dict]:
    """5-min cron cache (data/prices_latest.json). Primary $0 path.

    Written by scripts/poll_prices.py every 5 min via Yahoo+CoinGecko.
    Fresh = younger than LOCAL_CACHE_MAX_AGE_S. Never raises.
    """
    wanted = {t.upper() for t in tickers}
    for p in LOCAL_CACHE_PATHS:
        try:
            path = Path(p)
            if not path.is_file():
                continue
            if time.time() - path.stat().st_mtime > LOCAL_CACHE_MAX_AGE_S:
                continue
            body = json.loads(path.read_text(encoding="utf-8"))
            snap = body.get("tickers", {}) if isinstance(body, dict) else {}
            out: dict[str, dict] = {}
            for t in wanted:
                row = snap.get(t)
                if isinstance(row, dict) and "price" in row:
                    out[t] = {
                        "price": row["price"],
                        "pct_1d": round(float(row.get("pct_1d") or 0), 2),
                        "asof": row.get("asof") or body.get("ts"),
                        "venue": row.get("venue", "cache-5m"),
                    }
            if out:
                return out
        except Exception:
            continue
    return {}


def _stooq_moves(tickers: list[str]) -> dict[str, dict]:
    if httpx is None:
        return {}
    symbols = {t: STOOQ_SYMBOLS[t] for t in tickers if t in STOOQ_SYMBOLS}
    if not symbols:
        return {}

    def load():
        out: dict[str, dict] = {}
        # Daily history per symbol (q/l has no previous close).
        # Free and keyless; 15-min cache keeps briefs cheap.
        for ticker, symbol in symbols.items():
            try:
                resp = httpx.get(
                    "https://stooq.com/q/d/l/",
                    params={"s": symbol, "d1": "20000101",
                            "d2": "21000101", "i": "d"},
                    timeout=20,
                    follow_redirects=True,
                )
                resp.raise_for_status()
                rows = [r for r in csv.DictReader(io.StringIO(resp.text))
                        if r.get("Close")]
                if len(rows) < 2:
                    continue
                prev = float(rows[-2]["Close"])
                row = rows[-1]
                close = float(row["Close"])
                if prev <= 0 or close <= 0:
                    continue
                out[ticker] = {
                    "price": round(close, 2),
                    "pct_1d": round((close - prev) / prev * 100, 2),
                    "asof": row.get("Date"),
                    "venue": "stooq",
                }
            except Exception:
                continue
        return out

    return _cached("stooq:" + ",".join(sorted(symbols)), load)


def _yahoo_moves(tickers: list[str]) -> dict[str, dict]:
    """Live $0 fallback when the 5-min cache is stale/missing.

    Yahoo v8 chart, free + keyless. Uses YAHOO_SYMBOLS for EU suffixes.
    """
    if httpx is None:
        return {}
    symbols = {t.upper(): YAHOO_SYMBOLS[t.upper()] for t in tickers if t.upper() in YAHOO_SYMBOLS}
    if not symbols:
        return {}

    def load():
        out: dict[str, dict] = {}
        for ticker, symbol in symbols.items():
            try:
                resp = httpx.get(
                    "https://query1.finance.yahoo.com/v8/finance/chart/" + symbol,
                    params={"interval": "5m", "range": "1d"},
                    headers={"User-Agent": "Mozilla/5.0 (Stockify-brief)"},
                    timeout=20,
                    follow_redirects=True,
                )
                resp.raise_for_status()
                meta = resp.json().get("chart", {}).get("result", [{}])[0].get("meta", {})
                price = meta.get("regularMarketPrice")
                if price is None:
                    continue
                pct = meta.get("regularMarketChangePercent")
                prev = meta.get("chartPreviousClose") or meta.get("previousClose")
                if pct is None and prev:
                    pct = (price - prev) / prev * 100 if prev else 0
                out[ticker] = {
                    "price": round(float(price), 2),
                    "pct_1d": round(float(pct or 0), 2),
                    "asof": time.strftime(
                        "%Y-%m-%dT%H:%M:%SZ", time.gmtime(meta.get("regularMarketTime", 0))
                    ) if meta.get("regularMarketTime") else "yahoo",
                    "venue": "yahoo-live",
                }
            except Exception:
                continue
        return out

    return _cached("yahoo:" + ",".join(sorted(symbols)), load)


def _coingecko_moves(tickers: list[str]) -> dict[str, dict]:
    if httpx is None:
        return {}
    ids = {t: COINGECKO_IDS[t] for t in tickers if t in COINGECKO_IDS}
    if not ids:
        return {}

    def load():
        out: dict[str, dict] = {}
        resp = httpx.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": ",".join(ids.values()), "vs_currencies": "usd",
                    "include_24hr_change": "true"},
            timeout=20,
        )
        resp.raise_for_status()
        body = resp.json()
        for ticker, cid in ids.items():
            row = body.get(cid) or {}
            if "usd" not in row:
                continue
            out[ticker] = {
                "price": row["usd"],
                "pct_1d": round(float(row.get("usd_24h_change") or 0), 2),
                "asof": "coingecko",
                "venue": "coingecko",
            }
        return out

    return _cached("coingecko:" + ",".join(sorted(ids)), load)


def get_moves(tickers: list[str]) -> dict[str, dict[str, Any]]:
    """Latest price + 1d move per ticker. Never raises; missing = absent.

    Order: 5-min cron cache first ($0, freshest), then live fallbacks for
    anything the cache missed (Yahoo stocks, CoinGecko crypto, Stooq daily).
    """
    tickers = [t.upper() for t in tickers]
    moves: dict[str, dict] = {}
    try:
        moves.update(_local_cache_moves(tickers))
    except Exception:
        pass
    missing = [t for t in tickers if t not in moves]
    if missing:
        try:
            moves.update(_yahoo_moves(missing))
        except Exception:
            pass
    missing = [t for t in tickers if t not in moves]
    if missing:
        try:
            moves.update(_coingecko_moves(missing))
        except Exception:
            pass
    missing = [t for t in tickers if t not in moves]
    if missing:
        try:
            moves.update(_stooq_moves(missing))
        except Exception:
            pass
    return moves


def unmoved(tickers: list[str], threshold_pct: float = 2.0) -> list[str]:
    """Tickers whose 1d move is flat — repricing may not have happened yet."""
    moves = get_moves(tickers)
    return [t for t in tickers if t in moves and abs(moves[t]["pct_1d"]) < threshold_pct]
