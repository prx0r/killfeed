#!/usr/bin/env python3
"""Scrape drmichaellevin.org publications into local JSON + PDFs.

Why this shape:
  - Papers come as publisher HTML landing pages (most [PDF] links point at
    doi/publisher URLs, NOT direct .pdf files). Many are paywalled.
  - So: metadata.json (title/authors/year/journal/doi/url/topic) is the
    reliable local index; pdfs/ holds whatever is directly fetchable as
    application/pdf; pages/ holds raw HTML snapshots for offline re-parse.

Usage:
  python3 scripts/scrape_levin.py --metadata-only   # ~25 pages, fast
  python3 scripts/scrape_levin.py --pdfs            # attempts PDF fetch per entry
  python3 scripts/scrape_levin.py                   # both

Polite: browser headers (site ModSecurity 406s bare curl), ~1.2s between hits.
"""
from __future__ import annotations

import argparse
import html as htmllib
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "levin"
PAGES = OUT / "pages"
PDFS = OUT / "pdfs"

BASE = "https://drmichaellevin.org"
INDEX = f"{BASE}/publications/"
TOPIC_PAGES = [
    "aging.html", "asymmetry.html", "bacteria.html", "behavior.html",
    "bioelectricity.html", "cancer.html", "computational.html",
    "developmental.html", "evolution.html", "foundations.html",
    "mammalian.html", "neurotransmitters.html", "planaria.html",
    "protocols.html", "regeneration.html", "reviews.html", "special.html",
    "synthetic.html",
]
EXTRA_PAGES = [
    "editorials.html", "preprints.html", "popular.html", "sciforpublic.html",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
PDF_HEADERS = {
    "User-Agent": HEADERS["User-Agent"],
    "Accept": "application/pdf,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
DELAY = 1.2


def fetch(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def slug(text: str, n: int = 80) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:n].strip("-") or "untitled"


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", "", text))).strip()


def parse_entries(page_html: str, source: str) -> list[dict]:
    entries: list[dict] = []
    # Track most recent <h2 id="YYYY"> year header for entries lacking a year.
    year = None
    # Split by <p> blocks; each publication is one <p> containing <strong>title</strong>.
    for m in re.finditer(r"<h2[^>]*>(\d{4})</h2>|<p>(.*?)</p>", page_html, re.S | re.I):
        if m.group(1):
            year = m.group(1)
            continue
        block = m.group(2)
        if "<strong>" not in block:
            continue
        title_m = re.search(r"<strong>(.*?)</strong>", block, re.S)
        if not title_m:
            continue
        title = clean(title_m.group(1))
        if len(title) < 15:
            continue
        before = clean(block.split("<strong>")[0])
        y_m = re.search(r"\((19|20)\d{2}[a-z]?\)", block)
        entry_year = (y_m.group(0).strip("()")[:4] if y_m else year) or "unknown"
        journal_m = re.search(r"</strong>\.?\s*<em>(.*?)</em>", block, re.S)
        journal = clean(journal_m.group(1)) if journal_m else ""
        doi_m = re.search(r"doi:\s*([^\s<,;]+)", block, re.I)
        doi = doi_m.group(1).rstrip(".,)") if doi_m else ""
        pdf_m = re.search(r'<a[^>]+href="([^"]+)"[^>]*>\s*PDF\s*</a>', block, re.I)
        url = ""
        if pdf_m:
            url = htmllib.unescape(pdf_m.group(1)).strip()
            if url.startswith("/"):
                url = BASE + url
            elif not url.startswith("http"):
                url = urllib.parse.urljoin(BASE + "/publications/", url)
        # Fix common typo in their HTML: "hhttps://"
        url = re.sub(r"^h+(https?://)", r"\1", url)
        entries.append({
            "title": title,
            "authors": before,
            "year": entry_year,
            "journal": journal,
            "doi": doi,
            "url": url,
            "source_page": source,
        })
    return entries


def scrape_metadata() -> list[dict]:
    OUT.mkdir(parents=True, exist_ok=True)
    PAGES.mkdir(parents=True, exist_ok=True)
    pages = [("index", INDEX)]
    pages += [(t, f"{BASE}/publications/{t}") for t in TOPIC_PAGES + EXTRA_PAGES]
    all_entries: list[dict] = []
    for name, url in pages:
        try:
            raw = fetch(url)
            fname = name if name.endswith(".html") else f"{name}.html"
            (PAGES / fname).write_bytes(raw)
            html_text = raw.decode("utf-8", "replace")
            found = parse_entries(html_text, name)
            print(f"{name}: {len(found)} entries")
            all_entries.extend(found)
        except Exception as exc:
            print(f"{name}: FETCH FAILED: {exc}", file=sys.stderr)
        time.sleep(DELAY)
    # Dedupe by doi, else normalized title.
    seen: set[str] = set()
    uniq: list[dict] = []
    for e in all_entries:
        key = f"doi:{e['doi'].lower()}" if e["doi"] else f"t:{re.sub(r'[^a-z0-9]', '', e['title'].lower())}"
        if key in seen:
            # merge source pages
            for u in uniq:
                ukey = f"doi:{u['doi'].lower()}" if u["doi"] else f"t:{re.sub(r'[^a-z0-9]', '', u['title'].lower())}"
                if ukey == key and e["source_page"] not in u.get("topics", []):
                    u.setdefault("topics", []).append(e["source_page"])
            continue
        seen.add(key)
        e["topics"] = [e.pop("source_page")]
        e["id"] = f"{e['year']}-{slug(e['title'], 60)}"
        uniq.append(e)
    uniq.sort(key=lambda e: (e["year"], e["title"]), reverse=True)
    (OUT / "metadata.json").write_text(json.dumps(uniq, indent=2), encoding="utf-8")
    print(f"TOTAL unique: {len(uniq)} (raw blocks: {len(all_entries)})")
    return uniq


def looks_pdf_url(url: str) -> bool:
    u = url.lower()
    return any(k in u for k in [".pdf", "/pdf", "epdf", "download", "arxiv.org/pdf"])


def download_pdfs(entries: list[dict], limit: int = 0) -> dict:
    PDFS.mkdir(parents=True, exist_ok=True)
    log = {"ok": [], "skipped_landing": [], "failed": []}
    todo = [e for e in entries if e["url"]]
    if limit:
        todo = todo[:limit]
    for i, e in enumerate(todo, 1):
        dest = PDFS / f"{e['id']}.pdf"
        if dest.exists() and dest.stat().st_size > 5000:
            log["ok"].append(e["id"])
            continue
        if not looks_pdf_url(e["url"]):
            log["skipped_landing"].append({"id": e["id"], "url": e["url"]})
            continue
        try:
            req = urllib.request.Request(e["url"], headers=PDF_HEADERS)
            with urllib.request.urlopen(req, timeout=40) as r:
                ctype = r.headers.get("Content-Type", "")
                body = r.read()
            if "pdf" in ctype.lower() and body[:4] == b"%PDF":
                dest.write_bytes(body)
                log["ok"].append(e["id"])
                print(f"[{i}/{len(todo)}] OK {e['id']} ({len(body)//1024}KB)")
            else:
                log["failed"].append({"id": e["id"], "reason": f"content-type {ctype}"})
        except Exception as exc:
            log["failed"].append({"id": e["id"], "reason": str(exc)[:140]})
        time.sleep(DELAY)
    (OUT / "download_log.json").write_text(json.dumps(log, indent=2), encoding="utf-8")
    print(f"PDFs ok={len(log['ok'])} landing-skipped={len(log['skipped_landing'])} failed={len(log['failed'])}")
    return log


def download_articles(entries: list[dict], limit: int = 0, offset: int = 0) -> dict:
    """Fetch EVERY paper's publisher landing page as HTML (user: html is fine).

    Falls back to https://doi.org/<doi> for entries with no URL on the site.
    Saves articles/<id>.html + sidecar <id>.final_url.txt. Resume-safe:
    skips files already >5KB. Polite delay, browser headers.
    """
    ARTS = OUT / "articles"
    ARTS.mkdir(parents=True, exist_ok=True)
    log_path = OUT / "articles_log.json"
    log: dict = {"ok": [], "failed": []}
    if log_path.exists():
        try:
            log = json.loads(log_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    todo: list[tuple[dict, str]] = []
    for e in entries:
        url = e["url"] or (f"https://doi.org/{e['doi']}" if e["doi"] else "")
        if url:
            todo.append((e, url))
    total = len(todo)
    if offset:
        todo = todo[offset:]
    if limit:
        todo = todo[:limit]
    print(f"articles: {len(todo)} to try (total {total}, offset {offset})")
    for i, (e, url) in enumerate(todo, 1):
        dest = ARTS / f"{e['id']}.html"
        if dest.exists() and dest.stat().st_size > 5000:
            if e["id"] not in log["ok"]:
                log["ok"].append(e["id"])
            continue
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=25) as r:
                ctype = r.headers.get("Content-Type", "")
                final = r.geturl()
                body = r.read()
            cl = (ctype or "").lower()
            if body[:4] == b"%PDF":
                # Publisher served a PDF directly — keep it with the PDFs.
                (PDFS / f"{e['id']}.pdf").write_bytes(body)
                (ARTS / f"{e['id']}.final_url.txt").write_text(final, encoding="utf-8")
                log["ok"].append(e["id"])
            elif b"<html" in body[:300000].lower() or "html" in cl or "text" in cl:
                dest.write_bytes(body)
                (ARTS / f"{e['id']}.final_url.txt").write_text(final, encoding="utf-8")
                log["ok"].append(e["id"])
            else:
                log["failed"].append({"id": e["id"], "reason": f"content-type {ctype}"})
        except Exception as exc:
            log["failed"].append({"id": e["id"], "reason": str(exc)[:140]})
        if i % 20 == 0:
            log_path.write_text(json.dumps(log, indent=2), encoding="utf-8")
            print(f"  [{offset + i}/{total}] ok={len(log['ok'])} failed={len(log['failed'])}", flush=True)
        time.sleep(0.7)
    log_path.write_text(json.dumps(log, indent=2), encoding="utf-8")
    print(f"ARTICLES ok={len(log['ok'])} failed={len(log['failed'])}")
    return log


def download_openalex(entries: list[dict]) -> dict:
    """Upgrade paywalled gaps via OpenAlex (free, keyless OA infrastructure).

    For every entry with a DOI lacking a local PDF, ask
    api.openalex.org for best_oa_location and fetch the OA PDF if any.
    This is the easiest legitimate route past publisher 403s.
    """
    PDFS.mkdir(parents=True, exist_ok=True)
    log_path = OUT / "openalex_log.json"
    log: dict = {"oa_pdfs": [], "oa_landing_only": [], "closed": [], "failed": []}
    if log_path.exists():
        try:
            log = json.loads(log_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    have = {p.stem for p in PDFS.glob("*.pdf")}
    have |= set(log["oa_pdfs"])
    todo = [e for e in entries if e["doi"] and e["id"] not in have]
    print(f"openalex: {len(todo)} without local PDF")
    for i, e in enumerate(todo, 1):
        try:
            url = f"https://api.openalex.org/works/doi:{e['doi'].lower()}"
            req = urllib.request.Request(url, headers={
                "User-Agent": "Stockify-levin-archive (personal research use)",
                "Accept": "application/json",
            })
            with urllib.request.urlopen(req, timeout=25) as r:
                work = json.loads(r.read().decode("utf-8", "replace"))
            loc = work.get("best_oa_location") or {}
            pdf_url = loc.get("pdf_url")
            landing = loc.get("landing_page_url") or work.get("doi")
            if pdf_url:
                preq = urllib.request.Request(pdf_url, headers=PDF_HEADERS)
                with urllib.request.urlopen(preq, timeout=40) as pr:
                    body = pr.read()
                if body[:4] == b"%PDF":
                    (PDFS / f"{e['id']}.pdf").write_bytes(body)
                    log["oa_pdfs"].append(e["id"])
                else:
                    log["failed"].append({"id": e["id"], "reason": "oa url not pdf"})
            elif landing:
                log["oa_landing_only"].append({"id": e["id"], "url": landing})
            else:
                log["closed"].append(e["id"])
        except Exception as exc:
            msg = str(exc)[:120]
            log["failed"].append({"id": e["id"], "reason": msg})
        if i % 25 == 0:
            log_path.write_text(json.dumps(log, indent=2), encoding="utf-8")
            print(f"  [{i}/{len(todo)}] oa_pdfs={len(log['oa_pdfs'])}", flush=True)
        time.sleep(0.3)
    log_path.write_text(json.dumps(log, indent=2), encoding="utf-8")
    print(f"OPENALEX oa_pdfs={len(log['oa_pdfs'])} landing_only={len(log['oa_landing_only'])} "
          f"closed={len(log['closed'])} failed={len(log['failed'])}")
    return log


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--metadata-only", action="store_true")
    ap.add_argument("--pdfs", action="store_true")
    ap.add_argument("--articles", action="store_true")
    ap.add_argument("--openalex", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--offset", type=int, default=0)
    args = ap.parse_args()
    any_mode = args.metadata_only or args.pdfs or args.articles or args.openalex
    do_meta = args.metadata_only or not any_mode
    do_pdf = args.pdfs or (not any_mode)
    do_articles = args.articles
    entries: list[dict] = []
    if do_meta:
        entries = scrape_metadata()
    else:
        meta = OUT / "metadata.json"
        if meta.exists():
            entries = json.loads(meta.read_text(encoding="utf-8"))
    if do_pdf:
        if not entries:
            print("no entries; run --metadata-only first", file=sys.stderr)
            return 1
        download_pdfs(entries, limit=args.limit)
    if do_articles:
        if not entries:
            print("no entries; run --metadata-only first", file=sys.stderr)
            return 1
        PDFS.mkdir(parents=True, exist_ok=True)
        download_articles(entries, limit=args.limit, offset=args.offset)
    if args.openalex:
        if not entries:
            meta = OUT / "metadata.json"
            if meta.exists():
                entries = json.loads(meta.read_text(encoding="utf-8"))
        if not entries:
            print("no entries; run --metadata-only first", file=sys.stderr)
            return 1
        download_openalex(entries)
    (OUT / "README.md").write_text(
        "# Levin Lab local archive\n\n"
        "- `metadata.json`: deduped index (title/authors/year/journal/doi/url/topics).\n"
        "- `levinite.md`: companion synthesis thesis (supported vs plausible vs metaphysics).\n"
        "- `pages/`: raw HTML snapshots of publications index + topic pages.\n"
        "- `pdfs/`: directly-fetchable open-access PDFs (`<id>.pdf`).\n"
        "- `articles/`: EVERY paper's publisher landing page as `<id>.html`\n"
        "  (+ `<id>.final_url.txt` after redirects/doi.org). HTML is the full\n"
        "  corpus fallback where PDFs are paywalled — title/abstract/refs are\n"
        "  on the landing page even when the full text isn't.\n"
        "  `articles_log.json` tracks ok vs failed (blocked/paywalled/JS-only).\n"
        "Source: https://drmichaellevin.org/publications/ (personal-use archive).\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
