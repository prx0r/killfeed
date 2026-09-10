"""FINRA short-data collector — per-symbol short flow, keyless ($0).

Endpoints (recipes ex-third_party/openinsider-mcp):
- Daily short volume (yesterday's tape):
  https://cdn.finra.org/equity/regsho/daily/{venue}shvol{YYYYMMDD}.txt
  venues probed in order: CNMS, NYSE, NMSQ... (first 200 wins).
  Columns: Date|Symbol|ShortVolume|ShortExemptVolume|TotalVolume|Market.
- Biweekly short interest:
  https://cdn.finra.org/equity/otcmarket/biweekly/shrt{YYYYMMDD}.csv
  (OTC leg; NASDAQ/NYSE SI via same CDN family — probed, else queued).

Email-format UA per FINRA CDN norms. CloudFront 403 = file not published
yet (not a ban): walk back trading days. Never raises.
"""
from __future__ import annotations

import datetime
import urllib.request

UA = {"User-Agent": "bneck research contact@localhost",
      "Accept": "text/plain, */*"}

VENUES = ("CNMS", "NYSE", "NMSQ")


def _fetch(url: str, timeout: int = 30) -> str | None:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "bneck research contact@localhost",
            "Accept": "text/plain, */*"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return None


def _recent_dates(n: int = 6) -> list[str]:
    out, d = [], datetime.date.today()
    while len(out) < n:
        d -= datetime.timedelta(days=1)
        if d.weekday() < 5:
            out.append(d.strftime("%Y%m%d"))
    return out


def daily_short(tickers: list[str], timeout: int = 30) -> dict:
    """{ticker: {date, short_ratio, short_vol, total_vol}} latest found day."""
    want = {t.upper() for t in tickers}
    for day in _recent_dates():
        for venue in VENUES:
            body = _fetch(f"https://cdn.finra.org/equity/regsho/daily/"
                          f"{venue}shvol{day}.txt", timeout)
            if not body or "ShortVolume" not in body:
                continue
            agg: dict[str, dict] = {}
            for line in body.splitlines()[1:]:
                parts = line.split("|")
                if len(parts) < 5 or parts[1].upper() not in want:
                    continue
                try:
                    sv = float(parts[2])
                    tv = float(parts[4])
                except ValueError:
                    continue
                a = agg.setdefault(parts[1].upper(),
                                   {"short": 0.0, "total": 0.0})
                a["short"] += sv
                a["total"] += tv
            if agg:
                return {t: {"date": f"{day[:4]}-{day[4:6]}-{day[6:]}",
                            "short_ratio": round(v["short"] / v["total"], 4)
                            if v["total"] else 0.0,
                            "short_vol": int(v["short"]),
                            "total_vol": int(v["total"])}
                        for t, v in agg.items()}
    return {}
