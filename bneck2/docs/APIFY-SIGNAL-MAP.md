# Apify Signal Map — data-source marketplace for agents (2026-09-10)

Source: external research memo, saved verbatim-ish near the AI thesis.
Status: discovery-grade. Prices/users as reported in memo, unverified.
Thesis: Apify is a data-source marketplace for agents. Edge = sources exposing
latent demand, competitor behavior, distribution, hiring, installed tech, or
changing attention before summarization. A July 2026 analysis of ~54,000 public
Actors found social media the strongest demand/supply imbalance, then video,
jobs, SEO — usage extremely winner-take-most.

## Ranked actors (alpha use)

| Rank | Actor / family | Why alpha | Use |
|------|---------------|-----------|-----|
| 1 | `apidojo/tweet-scraper` / Tweet Scraper V2 (~$0.40/1K tweets, ~98K users) + cheaper `kaitoeasyapi/twitter-x-data-tweet-scraper-pay-per-result-cheapest` (~$0.18/1K) | Cheap X collection without X API economics | Feedify researchers/traders, thesis propagation, who-called-it-first |
| 2 | `compass/crawler-google-places` (~595K users, 4.7) | Physical-world economic database: category, geo, site, phone, reviews, hours, prices | GeoDrop / service arbitrage; installer counts, review velocity, entrant rate |
| 3 | `curious_coder/facebook-ads-library-scraper` (~$0.75/1K ads, 4.8) + experimental `sukhdipp/meta-ad-library-scraper` (resumable GraphQL) | Revealed spend = revealed belief; creative persistence × geos × variants | Ecommerce/product discovery; supply-demand arbitrage scanner |
| 4 | `apify/google-search-scraper` (~178K users, 4.6) | SERPs incl. AI Overviews/AI Mode/PAA/ads | Agent Visibility Score: P(domain cited by AI \| query) |
| 5 | `apify/google-trends-scraper` (~$0.30/1K results) | Use as derivative, not signal | Demand primitive; cross-source second derivative |
| 6 | `webdatalabs/shopify-store-intelligence` | Refuses to fabricate sales estimates; catalogue + apps + theme + pricing | StallSpy / ecommerce intel |
| 7 | `harvestapi/linkedin-company-employees` + profile/search actors | Company → humans → roles/history | Organizational-flow graph: TalentFlow = incoming − outgoing quality |
| 8 | `streamers/youtube-scraper` | No quota pain | Long-form expert intel |
| 9 | `harshmaur/reddit-scraper` / `trudax/reddit-scraper-lite` | Searchable discussion corpus | Feedify + product pain mining |
| 10 | `apify/website-content-crawler` (~155K users, 4.6) | Arbitrary sites/docs → Markdown | Universal ingestion primitive |
| 11 | `vortex_data/similarweb-scraper` | Traffic + keywords + AI referral share | Agent-mediated discovery market share |
| 12 | `scraper-engine/amazon-product-scraper` | "Bought in past month" + BSR | Demand momentum > reviews |
| 13 | `storedata/appstore-scraper` (~$0.99/1K reviews) | Keyword/category rankings + reviews | Emerging software categories; complaint → build opportunity |
| 14 | `crawlerbros/producthunt-scraper` (~$1/1K) | Maker/hunter/topic/launch graph | Builder discovery pre-obviousness |
| 15 | `apify/rag-web-browser` (~169K users, 4.7) | Search → fetch → Markdown in one call | Autonomous research fallback |

Tweet Scraper V2 → benchmark vs cheapest; alpha = author × topic × horizon
calibration graph (expert_score × novelty × specificity × accuracy × lead time ×
disagreement), not follower counts.

## Hidden-data categories (weird alpha top 20)

1. Tender + contract awards (`foxlabs/ted-tenders`, `labrat011/gov-contracts-scraper`, `scrapesage/us-federal-grants-scraper`) → PUBLIC_CAPITAL_COMMITMENT signal family; procurement acceleration by technology.
2. Job ontology changes (Stepstone actor; role-taxonomy drift) → engineering bottleneck migration.
3. LinkedIn talent flows → human capital before narrative.
4. Google Maps review complaints → physical shortages/failures.
5. Chrome manifests + installs (`scraper-engine/chrome-web-store-scraper` + `fabrikit/chrome-web-store-reviews-scraper`) → adoption + permission-change security signals.
6. Freight bids (`crawlerbros/container-shipping-rates-scraper`, `crawlerbros/uship-scraper`) → localized transport scarcity.
7. 1688 supplier graph (`zen-studio/1688-wholesale-scraper`) → upstream product economics.
8. Meta ad persistence → revealed merchant belief.
9. Amazon bought-last-month → transaction-demand proxy.
10. Hotel forward-rate curves (`vittuhy/google-travel-hotel-prices`) → regional demand nowcast.
11. Airline fare curves (Ryanair/easyJet/Google Flights actors) → yield/demand.
12. Salvage auctions (`haketa/iaai-scraper` + Copart) → reliability/residual value, failed physical assets.
13. Patents + inventor migration (`fetch_cat/google-patents-search-scraper` ~$0.03/1K, `crawlergang/uspto-patent-scraper`) → R&D direction; stage-transition tracking (papers→patents→jobs→tenders→products).
14. Kickstarter velocity (`scraper-engine/kickstarter-scraper`) → pre-production willingness-to-pay.
15. Clinical trial transitions (`labrat011`/`scrapesage` actors, ~$0.50/1K) → sponsor analytics, status changes.
16. Delivery-menu history (DoorDash/Uber Eats actors) → hyperlocal CPI; birth/death rates.
17. App/extension review histories → weakness + demand.
18. Government grants → research capital direction.
19. Product Hunt maker graph → early founder emergence.
20. Apify Store itself (`parseforge/smart-apify-actor-scraper`) → developer futures market (automation demand emergence).

Caution (from memo): heavy developer self-promotion around Actors; benchmark 2–4
competing Actors per source on coverage/freshness/duplicates/field-validity/failure-rate/$-per-valid-observation. Don't trust social endorsement.

## Core primitives

OBSERVATION (universal): {subject, predicate, object, time, location, source,
confidence, observed_at, source_actor}. Web gives state; we store MOTION
(price $279→$299→$349→$399). Snapshotting creates the moat.

Signal families (actors are implementations, not the taxonomy):
DEMAND (Trends, Amazon bought-month, Search, Reddit, TikTok) /
COMMERCIAL CONFIRMATION (Meta ads, Shopify, Shopping, seller counts) /
SUPPLY (1688, Alibaba, eBay, Shopify) / COMPANY STATE (LinkedIn, careers,
GitHub, crawler, Similarweb) / ATTENTION (X, Reddit, YouTube, TikTok, PH) /
PUBLIC_CAPITAL_COMMITMENT (tenders, grants) / FRICTION (complaints mined to
{asset, component, failure, constraint, lead_time, location, timestamp}).

Diffusion chain: research → patents → Kickstarter → Reddit → YouTube → TikTok →
Meta Ads → Amazon → retail. Cross-source second derivative is the signal
(T0 Reddit → T1 X → T2 search → T3 TikTok → T4 Shopify → T5 Meta → T6 Amazon).

For the bottleneck thesis: don't scrape markets, scrape constraint evidence —
WAIT TIMES, BACKORDERS, JOB OPENINGS, PRICE INCREASES, GOVERNMENT ORDERS,
FREIGHT PREMIUMS, COMPONENT COMPLAINTS, TENDER VALUES, NEW FACTORIES,
NEW PATENTS, CAPACITY LANGUAGE, REPAIR FAILURES. All manifestations of one
hidden variable: scarcity / constraint pressure.

Next rabbit hole (from memo): ~100 ultra-obscure Actors exposing individual
bottleneck variables (used machinery, spares, distributors, energy/grid,
permits, ports, FCC filings, used lab gear…), ranked by irreconstructability
of the history. Plus: crawl ~70K Actor Store → actor-alpha.json registry
(Actor → primitive → price → users → rating → freshness → schema →
reliability), benchmark top 2–3 per source.
