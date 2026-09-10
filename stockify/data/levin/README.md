# Levin Lab local archive

- `metadata.json`: deduped index (title/authors/year/journal/doi/url/topics).
- `levinite.md`: companion synthesis thesis (supported vs plausible vs metaphysics).
- `pages/`: raw HTML snapshots of publications index + topic pages.
- `pdfs/`: directly-fetchable open-access PDFs (`<id>.pdf`).
- `articles/`: EVERY paper's publisher landing page as `<id>.html`
  (+ `<id>.final_url.txt` after redirects/doi.org). HTML is the full
  corpus fallback where PDFs are paywalled — title/abstract/refs are
  on the landing page even when the full text isn't.
  `articles_log.json` tracks ok vs failed (blocked/paywalled/JS-only).
Source: https://drmichaellevin.org/publications/ (personal-use archive).
