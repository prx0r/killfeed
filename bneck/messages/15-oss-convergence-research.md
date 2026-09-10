Yes. I found a much stronger set than generic graph libraries. There are several obscure personal projects from 2026 that are already converging on almost exactly our thesis.

The biggest discovery is **ProphetMap**. It is almost comically close to what we're describing: AI demand propagates through physical dependency layers; identify which layer is constrained; score the companies capturing that constraint; explicitly monitor events that falsify the thesis; update pricing daily; migrate when the physical bottleneck changes. It currently maps 87 tickers across 28 layers and five chains, including memory, packaging, substrates, optics, cooling/power, grid, nuclear fuel, critical commodities and embodied AI. It even separates `physicalConstraint`, `moatCapture`, `aiContribution`, `timeToRealize`, and `pricingScore`. ([GitHub][1])

## 1. Projects I would actually steal ideas/code/data from

| Priority | Project                       | Why it matters for us                                                                                                                                                                                                   | Link                                                                                                                                                  |
| -------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **S++**  | **ProphetMap**                | Nearly our investment thesis already implemented. Dependency layers + live valuations + falsifiers + daily GitHub Actions + candidate discovery. **Start here.** ([GitHub][1])                                          | [https://github.com/Beltran12138/prophetmap](https://github.com/Beltran12138/prophetmap?utm_source=chatgpt.com)                                       |
| **S++**  | **Keystone**                  | Explicitly hunts “keystone firms” that a value chain cannot route around. Semiconductor, AI compute, minerals, nuclear, etc. Every dependency edge has provenance and missing evidence is itself tracked. ([GitHub][2]) | [https://github.com/Skeeter-spec/keystone](https://github.com/Skeeter-spec/keystone?utm_source=chatgpt.com)                                           |
| **S++**  | **Supply Chain Intelligence** | Reverse-traces Nvidia/AMD/TPU/Trainium accelerators through foundry → HBM → OSAT → EDA → equipment → materials → raw materials. Generates tiered graphs/Sankeys from SEC evidence. ([GitHub][3])                        | [https://github.com/eugenehp/supplychain](https://github.com/eugenehp/supplychain?utm_source=chatgpt.com)                                             |
| **S+**   | **CHOKEPOINT**                | Brilliant methodology: simulate removal of every supplier and measure how much system capability collapses. This is exactly how we should quantify bottlenecks rather than merely label them. ([GitHub][4])             | [https://github.com/atharvahirulkar/chokepoint](https://github.com/atharvahirulkar/chokepoint?utm_source=chatgpt.com)                                 |
| **S+**   | **Chip Sense**                | Semiconductor companies, fabs, typed supplier arcs, trade flows and stress scenarios. Includes physical calculators for GPU → HBM → packaging → wafers. ([GitHub][5])                                                   | [https://github.com/aminalav/chip-sense](https://github.com/aminalav/chip-sense?utm_source=chatgpt.com)                                               |
| **S+**   | **Silicon Stack**             | Huge semiconductor dependency seed: 239 companies, 115 materials, 1,110 relationships; explicitly maps HBM, ABF, equipment, chemicals, EDA and component chokepoints. ([GitHub][6])                                     | [https://github.com/sflans99/silicon-stack](https://github.com/sflans99/silicon-stack?utm_source=chatgpt.com)                                         |
| **S+**   | **Memory Atlas**              | Dedicated HBM/CXL/photonics/memory-wall dependency graph with bottlenecks such as CoWoS, EUV, ABF and lasers. Perfect seed for our current memory branch. ([GitHub][7])                                                 | [https://github.com/upamanyuacharya/memory-atlas](https://github.com/upamanyuacharya/memory-atlas?utm_source=chatgpt.com)                             |
| **S+**   | **AI Supply Chain Research**  | Ten AI sectors, ~130 theses, ~170 quantified datapoints and explicitly calls the migration phenomenon the **“bottleneck relay.”** Also contains a 119-ticker event study. ([GitHub][8])                                 | [https://github.com/YichengYang-Ethan/ai-supply-chain-research](https://github.com/YichengYang-Ethan/ai-supply-chain-research?utm_source=chatgpt.com) |
| **S**    | **alphasig**                  | SEC → structural dependency extraction → timestamped graph → second-order exposure → DuckDB/Parquet/webhooks. Excellent live ingestion architecture. ([GitHub][9])                                                      | [https://github.com/sushaan-k/alphasig](https://github.com/sushaan-k/alphasig?utm_source=chatgpt.com)                                                 |
| **S**    | **TWSE-KG**                   | 4,512-company KG, 5,509 `SUPPLIES_TO` edges, PageRank/betweenness, two-hop signal propagation and a cost-adjusted backtest. Very relevant for turning graph position into equity signals. ([GitHub][10])                | [https://github.com/tunglich/TWSE-KG](https://github.com/tunglich/TWSE-KG?utm_source=chatgpt.com)                                                     |
| **S**    | **Taiwan Coverage**           | 1,735 Taiwanese companies with supply-chain mappings and cross-links; useful because so many AI dependency chains terminate in obscure Taiwanese suppliers. ([GitHub][11])                                              | [https://github.com/Timeverse/My-TW-Coverage](https://github.com/Timeverse/My-TW-Coverage?utm_source=chatgpt.com)                                     |
| **A+**   | **Stock Relation**            | SEC filings → supplier/customer relationships → interactive D3 corporate graph. Good extraction implementation. ([GitHub][12])                                                                                          | [https://github.com/supat-roong/stock-relation](https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com)                                 |
| **A+**   | **SEC Graph**                 | GraphRAG across 10-K/10-Q/8-K. Explicitly supports queries such as “which suppliers are indirectly dependent on Nvidia?” ([GitHub][13])                                                                                 | [https://github.com/Jumade/sec-graph](https://github.com/Jumade/sec-graph?utm_source=chatgpt.com)                                                     |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |

There is also this smaller semiconductor chokepoint analysis project using NetworkX centrality:

[https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis](https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis?utm_source=chatgpt.com) ([GitHub][15])

### ProphetMap is the one to inspect first

Its conceptual model is remarkably close to ours:

**models → accelerators → EDA → semiconductor materials → equipment → packaging → substrates → HBM → servers → networking → power/cooling → optics → construction → power generation → nuclear fuel → grid → commodities → embodied AI.**

It then scores each ticker by physical constraint, whether the company actually captures the scarcity rent, AI revenue sensitivity, time-to-realization and whether the market has already priced it. Most importantly, it maintains **pre-declared falsifiers** and evaluates them daily. ([GitHub][1])

That last part is exactly what was missing from our discussion:

> HBM is the bottleneck — **until what observable event makes that statement false?**

ProphetMap already thinks this way.

Its live frontend is:

[https://prophetmap.vercel.app/](https://prophetmap.vercel.app/?utm_source=chatgpt.com)

Keystone's live industrial maps:

[https://skeeter-spec.github.io/keystone/](https://skeeter-spec.github.io/keystone/?utm_source=chatgpt.com) ([GitHub][2])

Memory Atlas:

[https://memory.upamanyuacharya.com/](https://memory.upamanyuacharya.com/?utm_source=chatgpt.com) ([The Memory Atlas][16])

## 2. Graph/math projects that give us the quantitative machinery

We shouldn't build our own graph science. These give us nearly everything.

| Tool           | What I'd use it for                                                                                                                          | Link                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **NetworkX**   | betweenness, PageRank, articulation nodes, centrality, shortest paths, min-cut/max-flow and simulated node removal                           | [https://github.com/networkx/networkx](https://github.com/networkx/networkx?utm_source=chatgpt.com)         |
| **Graphiti**   | **temporal knowledge graph** — crucial because dependencies become true/false through time rather than being permanent facts. ([GitHub][17]) | [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti?utm_source=chatgpt.com)             |
| **cuGraph**    | GPU-accelerated graph analysis once the graph gets enormous                                                                                  | [https://github.com/rapidsai/cugraph](https://github.com/rapidsai/cugraph?utm_source=chatgpt.com)           |
| **River**      | online ML + concept/drift detection: detect when a bottleneck regime changes                                                                 | [https://github.com/online-ml/river](https://github.com/online-ml/river?utm_source=chatgpt.com)             |
| **ruptures**   | historical change-point detection                                                                                                            | [https://github.com/deepcharles/ruptures](https://github.com/deepcharles/ruptures?utm_source=chatgpt.com)   |
| **Tigramite**  | causal discovery on time series rather than merely observing correlation                                                                     | [https://github.com/jakobrunge/tigramite](https://github.com/jakobrunge/tigramite?utm_source=chatgpt.com)   |
| **DoWhy**      | intervention/counterfactual analysis: “if HBM capacity rises 50%, what becomes binding?”                                                     | [https://github.com/py-why/dowhy](https://github.com/py-why/dowhy?utm_source=chatgpt.com)                   |
| **Qlib**       | convert bottleneck signals into an actual backtested dynamic portfolio                                                                       | [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib?utm_source=chatgpt.com)               |
| **OpenBB**     | market/fundamental data abstraction layer                                                                                                    | [https://github.com/OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB?utm_source=chatgpt.com) |
| **PyPSA**      | physically model the electricity/grid branch rather than relying on narratives                                                               | [https://github.com/PyPSA/PyPSA](https://github.com/PyPSA/PyPSA?utm_source=chatgpt.com)                     |
| **gridstatus** | live ISO electricity demand, generation and pricing                                                                                          | [https://github.com/gridstatus/gridstatus](https://github.com/gridstatus/gridstatus?utm_source=chatgpt.com) |
| **pymrio**     | global input-output dependency analysis                                                                                                      | [https://github.com/IndEcol/pymrio](https://github.com/IndEcol/pymrio?utm_source=chatgpt.com)               |
| **leontief**   | U.S. BEA input-output tables → direct + indirect dependency multipliers                                                                      | [https://github.com/andenick/leontief](https://github.com/andenick/leontief?utm_source=chatgpt.com)         |

Graphiti is particularly important for our thesis.

Instead of storing:

`AI → REQUIRES → HBM`

we should store something closer to:

`AI architecture X → REQUIRES → HBM bandwidth`

with:

`valid_from`
`valid_to`
`quantity_per_unit_compute`
`confidence`
`evidence`
`architecture`

Because your hypothetical ChatGPT-8 event shouldn't delete historical knowledge. It should turn:

**HBM requirement: high, valid Jan–Sep 2026**

into

**HBM requirement: dramatically lower, valid from Oct 2026**

and immediately propagate that change through the graph.

That's precisely why a temporal KG is superior to a conventional static supply-chain diagram. Graphiti is specifically designed around time-valid facts and incremental graph updates. ([GitHub][17])

## 3. Free raw data we can continuously feed it

This is where it becomes much more powerful than any of those individual projects.

| Dataset                 | What it tells us                                                                      | Full resource                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SEC EDGAR**           | supplier concentration, customers, capex, capacity, risks, contracts, backlog         | [https://www.sec.gov/about/developer-resources](https://www.sec.gov/about/developer-resources?utm_source=chatgpt.com)                                                               |
| **UN Comtrade**         | who actually exports/imports a material/component and geographic concentration        | [https://uncomtrade.org/docs/un-comtrade-api/](https://uncomtrade.org/docs/un-comtrade-api/?utm_source=chatgpt.com)                                                               |
| **BEA Input-Output**    | U.S. industry → industry dependencies                                                 | [https://www.bea.gov/data/industries/input-output-accounts-data](https://www.bea.gov/data/industries/input-output-accounts-data?utm_source=chatgpt.com)                             |
| **BEA API**             | automate the above                                                                    | [https://apps.bea.gov/api/signup/](https://apps.bea.gov/api/signup/?utm_source=chatgpt.com)                                                                                         |
| **OECD ICIO**           | global inter-country input/output dependencies                                        | [https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html](https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html?utm_source=chatgpt.com) |
| **EXIOBASE**            | extremely detailed global multi-regional production network                           | [https://exiobase.eu/](https://exiobase.eu/?utm_source=chatgpt.com)                                                                                                                 |
| **USGS Minerals**       | production/concentration/reserves for gallium, uranium, copper, rare earths etc.      | [https://www.usgs.gov/centers/national-minerals-information-center/tools](https://www.usgs.gov/centers/national-minerals-information-center/tools?utm_source=chatgpt.com)           |
| **EIA API**             | power generation, capacity, demand and grid flows                                     | [https://www.eia.gov/opendata/](https://www.eia.gov/opendata/?utm_source=chatgpt.com)                                                                                               |
| **OpenAlex**            | research velocity — incredibly useful for detecting scientists attacking a bottleneck | [https://help.openalex.org/api/](https://help.openalex.org/api/?utm_source=chatgpt.com)                                                                                             |
| **PatentsView / USPTO** | patent acceleration around substitutes/new architectures                              | [https://www.uspto.gov/ip-policy/economic-research/patentsview](https://www.uspto.gov/ip-policy/economic-research/patentsview?utm_source=chatgpt.com)                               |
| **FRED**                | prices, industrial production, commodities and macro time series                      | [https://fred.stlouisfed.org/docs/api/fred/overview.html](https://fred.stlouisfed.org/docs/api/fred/overview.html?utm_source=chatgpt.com)                                         |
| **Wikidata SPARQL**     | entity resolution: companies, facilities, subsidiaries, countries, products           | [https://query.wikidata.org/](https://query.wikidata.org/?utm_source=chatgpt.com)                                                                                                   |
| **GDELT**               | machine-readable live world news/event stream                                         | [https://www.gdeltproject.org/](https://www.gdeltproject.org/?utm_source=chatgpt.com)                                                                                               |

The **OpenAlex + USPTO** combination is especially interesting because it gives us something normal supply-chain maps completely miss:

### probability that the bottleneck is about to be destroyed.

For every bottleneck node, track:

**papers about reducing requirement for X**
**papers about substitutes for X**
**patent acceleration**
**new architecture announcements**
**startup funding targeting X**
**benchmark improvements reducing X/unit of intelligence**

So while HBM's *current scarcity score* might increase, its *expected persistence* could simultaneously fall.

That is exactly your ChatGPT-8 scenario.

## 4. I think our graph should go deeper than ProphetMap

ProphetMap is primarily:

**sector/layer → ticker**

We want:

**AGI capability**
→ **technical requirement**
→ **system**
→ **process**
→ **component**
→ **material**
→ **equipment**
→ **factory**
→ **company**
→ **geography**
→ **stock**

For example:

**frontier inference**
→ memory bandwidth
→ HBM3E/HBM4
→ stacked DRAM
→ TSV
→ wafer thinning
→ TC/hybrid bonding
→ CoWoS
→ ABF substrate
→ ABF film
→ Ajinomoto
→ chemical/feedstock/equipment dependency...

And every node can itself recursively answer:

> **What constrains increasing the output of this node?**

That creates the graph automatically.

This is actually the simplest definition of our system:

$$
\boxed{
B(x)=\text{What prevents production of }x\text{ increasing?}
}
$$

Apply `B()` recursively.

For HBM:

**HBM**
→ DRAM wafer capacity
→ yields
→ TSV
→ bonding machines
→ packaging capacity
→ substrates
→ electricity
→ ultrapure water
→ specialized labor
→ fab equipment.

Then recursively:

**bonding machines**
→ precision stages
→ optics
→ encoders
→ motors
→ bearings
→ specialty materials...

And suddenly you hit exactly the obscure companies we've been finding.

## 5. The CHOKEPOINT idea gives us the quantitative breakthrough

The most interesting methodology I found outside ProphetMap may actually be this tiny **zero-star/low-star personal repo**:

[https://github.com/atharvahirulkar/chokepoint](https://github.com/atharvahirulkar/chokepoint?utm_source=chatgpt.com)

Instead of asking:

> "Which node looks important?"

it removes each vendor from the graph and calculates **coverage collapse**. It trains against those simulated failures and validates against historical disruptions. It reports a ~49,842-vendor universe in its defense dataset. ([GitHub][18])

We can generalize this beautifully.

For every node \(v\):

$$
Criticality(v)
=
AGIThroughput(G)-AGIThroughput(G-v)
$$

Then instead of simply saying **"HBM is important"**, we could estimate:

> Removing HBM capacity decreases available AI-compute throughput 63%.

And then:

> Increasing HBM capacity 50% only increases total throughput 17%, because CoWoS subsequently becomes binding.

**Boom. That's the next bottleneck.**

Then simulate:

+50% CoWoS.

Maybe substrates bind.

+50% substrates.

Power binds.

You're computationally walking the bottleneck frontier.

That is much better than a static research report.

---

## What I'd actually build

I wouldn't create another massive schema-heavy research platform. I'd combine the clever parts that already exist:

**ProphetMap**
→ thesis/falsification/scoring discipline

**Keystone + Silicon Stack + Memory Atlas**
→ initial dependency graph

**eugenehp/supplychain**
→ recursive upstream tracing pattern

**alphasig + SEC EDGAR**
→ continual evidence extraction

**Graphiti**
→ temporal edges

**NetworkX**
→ centrality/min-cut/removal simulations

**CHOKEPOINT**
→ counterfactual failure scoring

**River**
→ regime-change detection

**OpenAlex + PatentsView**
→ bottleneck-obsolescence score

**Qlib**
→ historical portfolio simulation.

I would keep the underlying storage boring initially: **Parquet + DuckDB + NetworkX**, not Neo4j. Only introduce a graph DB when queries actually demand it.

And the fundamental object doesn't need 200 fields. Something like:

```text
NODE
id
type
name

EDGE
source
target
relation
amount
capacity
utilization
lead_time
substitutability
valid_from
valid_to
confidence
source_url
```

Then derive everything else.

The important calculated quantities become:

$$
Scarcity =
\frac{DemandGrowth}{CapacityGrowth}
$$

$$
Fragility =
Utilization
\times Concentration
\times LeadTime
\times (1-Substitutability)
$$

and roughly:

$$
BottleneckAlpha =
\frac{
Scarcity \times Persistence \times Criticality
\times PricingPower \times MarketSurprise
}{
Valuation \times ObsolescenceRisk
}
$$

But the really powerful output isn't merely the highest score.

It's:

> **Current bottleneck:** HBM
> **Likely next bottleneck if HBM supply expands:** CoWoS
> **Likely next:** ABF / bonding / power
> **Companies with greatest revenue sensitivity:** ...
> **Market awareness:** ...
> **Research attacking this constraint:** accelerating/decelerating
> **Probability constraint remains binding in 3/6/12/24 months:** ...

### The gap

After searching all of this, I **didn't find a project that combines all four**:

**physical AGI dependency graph + recursive bottleneck discovery + temporal/obsolescence detection + systematic equity reallocation.**

ProphetMap comes closest on the investing side. Keystone comes closest on rigorous industrial dependency mapping. CHOKEPOINT has the best quantitative bottleneck-identification mechanism. Graphiti solves temporal facts.

So I don't think we need to invent the primitives. **The novel project is connecting these four things.**

And I would absolutely clone **ProphetMap, Keystone, CHOKEPOINT, Chip Sense, Silicon Stack and Memory Atlas first** and compare their graph representations before writing ours. One caution: the repositories have different licenses—ProphetMap is MIT and Keystone AGPL-3.0, while `eugenehp/supplychain` is free for non-commercial use but requires permission for commercial deployment, and TWSE-KG is publicly visible but marked proprietary. ([GitHub][1])

This is considerably more developed in the wild than I expected. The striking part is that these independent builders have already converged on **“physical constraints,” “chokepoints,” “dependency graphs,” “falsification,” and even “bottleneck relay”** almost simultaneously. Our extension is making the relay itself the object being predicted.

[1]: https://github.com/Beltran12138/prophetmap "GitHub - Beltran12138/prophetmap: AI industry chain transmission map for US equity alpha discovery — 19-layer propagation model with automated daily scoring · GitHub"
[2]: https://github.com/Skeeter-spec/keystone "GitHub - Skeeter-spec/keystone: A living atlas of the world's industrial value chains, mapped to find the chokepoints. Educational research, not investment advice. · GitHub"
[3]: https://github.com/eugenehp/supplychain?utm_source=chatgpt.com "GitHub - eugenehp/supplychain · GitHub"
[4]: https://github.com/atharvahirulkar/chokepoint "GitHub - atharvahirulkar/chokepoint: Graph ML pipeline that scores defense procurement vendors by mission coverage collapse risk - find structural single points of failure in public contract data before disruption does. · GitHub"
[5]: https://github.com/aminalav/chip-sense "GitHub - aminalav/chip-sense: Open-source research board for the semiconductor supply chain — companies, fabs, cited relationship arcs, trade flows, and illustrative stress scenarios. Next.js + MapLibre. · GitHub"
[6]: https://github.com/sflans99/silicon-stack?utm_source=chatgpt.com "GitHub - sflans99/silicon-stack: Interactive semiconductor supply chain visualizer — 239 companies, 1,110 relationships, React + D3 · GitHub"
[7]: https://github.com/upamanyuacharya/memory-atlas "GitHub - upamanyuacharya/memory-atlas: An interactive 3D map of the AI memory supply chain — HBM, CXL, photonics: who makes what, the bottlenecks, and who matters. Single-file Three.js. · GitHub"
[8]: https://github.com/YichengYang-Ethan/ai-supply-chain-research?utm_source=chatgpt.com "GitHub - YichengYang-Ethan/ai-supply-chain-research: Verified ten-sector research on the AI compute build-out, distilled from 311 public SemiAnalysis articles — with an independent credibility audit of the source (664 events, 119 tickers). · GitHub"
[9]: https://github.com/sushaan-k/alphasig?utm_source=chatgpt.com "GitHub - sushaan-k/alphasig: Causal signal extraction from SEC filings using LLMs. · GitHub"
[10]: https://github.com/tunglich/TWSE-KG?utm_source=chatgpt.com "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[11]: https://github.com/Timeverse/My-TW-Coverage "GitHub - Timeverse/My-TW-Coverage: Equity research coverage of 1,735 Taiwan-listed companies (TWSE + OTC). Business overviews, supply chain mapping, and financial data with wikilink cross-referencing. · GitHub"
[12]: https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com "GitHub - supat-roong/stock-relation: Interactive dashboard that maps corporate relationships by parsing financial data and SEC filings into a dynamic knowledge graph of similarity, ownership, and validation. ([GitHub][13])                                                                                 | [https://github.com/Jumade/sec-graph](https://github.com/Jumade/sec-graph?utm_source=chatgpt.com)                                                     |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |

There is also this smaller semiconductor chokepoint analysis project using NetworkX centrality:

[https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis](https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis?utm_source=chatgpt.com) ([GitHub][15])

### ProphetMap is the one to inspect first

Its conceptual model is remarkably close to ours:

**models → accelerators → EDA → semiconductor materials → equipment → packaging → substrates → HBM → servers → networking → power/cooling → optics → construction → power generation → nuclear fuel → grid → commodities → embodied AI.**

It then scores each ticker by physical constraint, whether the company actually captures the scarcity rent, AI revenue sensitivity, time-to-realization and whether the market has already priced it. Most importantly, it maintains **pre-declared falsifiers** and evaluates them daily. ([GitHub][1])

That last part is exactly what was missing from our discussion:

> HBM is the bottleneck — **until what observable event makes that statement false?**

ProphetMap already thinks this way.

Its live frontend is:

[https://prophetmap.vercel.app/](https://prophetmap.vercel.app/?utm_source=chatgpt.com)

Keystone's live industrial maps:

[https://skeeter-spec.github.io/keystone/](https://skeeter-spec.github.io/keystone/?utm_source=chatgpt.com) ([GitHub][2])

Memory Atlas:

[https://memory.upamanyuacharya.com/](https://memory.upamanyuacharya.com/?utm_source=chatgpt.com) ([The Memory Atlas][16])

## 2. Graph/math projects that give us the quantitative machinery

We shouldn't build our own graph science. These give us nearly everything.

| Tool           | What I'd use it for                                                                                                                          | Link                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **NetworkX**   | betweenness, PageRank, articulation nodes, centrality, shortest paths, min-cut/max-flow and simulated node removal                           | [https://github.com/networkx/networkx](https://github.com/networkx/networkx?utm_source=chatgpt.com)         |
| **Graphiti**   | **temporal knowledge graph** — crucial because dependencies become true/false through time rather than being permanent facts. ([GitHub][17]) | [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti?utm_source=chatgpt.com)             |
| **cuGraph**    | GPU-accelerated graph analysis once the graph gets enormous                                                                                  | [https://github.com/rapidsai/cugraph](https://github.com/rapidsai/cugraph?utm_source=chatgpt.com)           |
| **River**      | online ML + concept/drift detection: detect when a bottleneck regime changes                                                                 | [https://github.com/online-ml/river](https://github.com/online-ml/river?utm_source=chatgpt.com)             |
| **ruptures**   | historical change-point detection                                                                                                            | [https://github.com/deepcharles/ruptures](https://github.com/deepcharles/ruptures?utm_source=chatgpt.com)   |
| **Tigramite**  | causal discovery on time series rather than merely observing correlation                                                                     | [https://github.com/jakobrunge/tigramite](https://github.com/jakobrunge/tigramite?utm_source=chatgpt.com)   |
| **DoWhy**      | intervention/counterfactual analysis: “if HBM capacity rises 50%, what becomes binding?”                                                     | [https://github.com/py-why/dowhy](https://github.com/py-why/dowhy?utm_source=chatgpt.com)                   |
| **Qlib**       | convert bottleneck signals into an actual backtested dynamic portfolio                                                                       | [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib?utm_source=chatgpt.com)               |
| **OpenBB**     | market/fundamental data abstraction layer                                                                                                    | [https://github.com/OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB?utm_source=chatgpt.com) |
| **PyPSA**      | physically model the electricity/grid branch rather than relying on narratives                                                               | [https://github.com/PyPSA/PyPSA](https://github.com/PyPSA/PyPSA?utm_source=chatgpt.com)                     |
| **gridstatus** | live ISO electricity demand, generation and pricing                                                                                          | [https://github.com/gridstatus/gridstatus](https://github.com/gridstatus/gridstatus?utm_source=chatgpt.com) |
| **pymrio**     | global input-output dependency analysis                                                                                                      | [https://github.com/IndEcol/pymrio](https://github.com/IndEcol/pymrio?utm_source=chatgpt.com)               |
| **leontief**   | U.S. BEA input-output tables → direct + indirect dependency multipliers                                                                      | [https://github.com/andenick/leontief](https://github.com/andenick/leontief?utm_source=chatgpt.com)         |

Graphiti is particularly important for our thesis.

Instead of storing:

`AI → REQUIRES → HBM`

we should store something closer to:

`AI architecture X → REQUIRES → HBM bandwidth`

with:

`valid_from`
`valid_to`
`quantity_per_unit_compute`
`confidence`
`evidence`
`architecture`

Because your hypothetical ChatGPT-8 event shouldn't delete historical knowledge. It should turn:

**HBM requirement: high, valid Jan–Sep 2026**

into

**HBM requirement: dramatically lower, valid from Oct 2026**

and immediately propagate that change through the graph.

That's precisely why a temporal KG is superior to a conventional static supply-chain diagram. Graphiti is specifically designed around time-valid facts and incremental graph updates. ([GitHub][17])

## 3. Free raw data we can continuously feed it

This is where it becomes much more powerful than any of those individual projects.

| Dataset                 | What it tells us                                                                      | Full resource                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SEC EDGAR**           | supplier concentration, customers, capex, capacity, risks, contracts, backlog         | [https://www.sec.gov/about/developer-resources](https://www.sec.gov/about/developer-resources?utm_source=chatgpt.com)                                                               |
| **UN Comtrade**         | who actually exports/imports a material/component and geographic concentration        | [https://uncomtrade.org/docs/un-comtrade-api/](https://uncomtrade.org/docs/un-comtrade-api/?utm_source=chatgpt.com)                                                               |
| **BEA Input-Output**    | U.S. industry → industry dependencies                                                 | [https://www.bea.gov/data/industries/input-output-accounts-data](https://www.bea.gov/data/industries/input-output-accounts-data?utm_source=chatgpt.com)                             |
| **BEA API**             | automate the above                                                                    | [https://apps.bea.gov/api/signup/](https://apps.bea.gov/api/signup/?utm_source=chatgpt.com)                                                                                         |
| **OECD ICIO**           | global inter-country input/output dependencies                                        | [https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html](https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html?utm_source=chatgpt.com) |
| **EXIOBASE**            | extremely detailed global multi-regional production network                           | [https://exiobase.eu/](https://exiobase.eu/?utm_source=chatgpt.com)                                                                                                                 |
| **USGS Minerals**       | production/concentration/reserves for gallium, uranium, copper, rare earths etc.      | [https://www.usgs.gov/centers/national-minerals-information-center/tools](https://www.usgs.gov/centers/national-minerals-information-center/tools?utm_source=chatgpt.com)           |
| **EIA API**             | power generation, capacity, demand and grid flows                                     | [https://www.eia.gov/opendata/](https://www.eia.gov/opendata/?utm_source=chatgpt.com)                                                                                               |
| **OpenAlex**            | research velocity — incredibly useful for detecting scientists attacking a bottleneck | [https://help.openalex.org/api/](https://help.openalex.org/api/?utm_source=chatgpt.com)                                                                                             |
| **PatentsView / USPTO** | patent acceleration around substitutes/new architectures                              | [https://www.uspto.gov/ip-policy/economic-research/patentsview](https://www.uspto.gov/ip-policy/economic-research/patentsview?utm_source=chatgpt.com)                               |
| **FRED**                | prices, industrial production, commodities and macro time series                      | [https://fred.stlouisfed.org/docs/api/fred/overview.html](https://fred.stlouisfed.org/docs/api/fred/overview.html?utm_source=chatgpt.com)                                         |
| **Wikidata SPARQL**     | entity resolution: companies, facilities, subsidiaries, countries, products           | [https://query.wikidata.org/](https://query.wikidata.org/?utm_source=chatgpt.com)                                                                                                   |
| **GDELT**               | machine-readable live world news/event stream                                         | [https://www.gdeltproject.org/](https://www.gdeltproject.org/?utm_source=chatgpt.com)                                                                                               |

The **OpenAlex + USPTO** combination is especially interesting because it gives us something normal supply-chain maps completely miss:

### probability that the bottleneck is about to be destroyed.

For every bottleneck node, track:

**papers about reducing requirement for X**
**papers about substitutes for X**
**patent acceleration**
**new architecture announcements**
**startup funding targeting X**
**benchmark improvements reducing X/unit of intelligence**

So while HBM's *current scarcity score* might increase, its *expected persistence* could simultaneously fall.

That is exactly your ChatGPT-8 scenario.

## 4. I think our graph should go deeper than ProphetMap

ProphetMap is primarily:

**sector/layer → ticker**

We want:

**AGI capability**
→ **technical requirement**
→ **system**
→ **process**
→ **component**
→ **material**
→ **equipment**
→ **factory**
→ **company**
→ **geography**
→ **stock**

For example:

**frontier inference**
→ memory bandwidth
→ HBM3E/HBM4
→ stacked DRAM
→ TSV
→ wafer thinning
→ TC/hybrid bonding
→ CoWoS
→ ABF substrate
→ ABF film
→ Ajinomoto
→ chemical/feedstock/equipment dependency...

And every node can itself recursively answer:

> **What constrains increasing the output of this node?**

That creates the graph automatically.

This is actually the simplest definition of our system:

$$
\boxed{
B(x)=\text{What prevents production of }x\text{ increasing?}
}
$$

Apply `B()` recursively.

For HBM:

**HBM**
→ DRAM wafer capacity
→ yields
→ TSV
→ bonding machines
→ packaging capacity
→ substrates
→ electricity
→ ultrapure water
→ specialized labor
→ fab equipment.

Then recursively:

**bonding machines**
→ precision stages
→ optics
→ encoders
→ motors
→ bearings
→ specialty materials...

And suddenly you hit exactly the obscure companies we've been finding.

## 5. The CHOKEPOINT idea gives us the quantitative breakthrough

The most interesting methodology I found outside ProphetMap may actually be this tiny **zero-star/low-star personal repo**:

[https://github.com/atharvahirulkar/chokepoint](https://github.com/atharvahirulkar/chokepoint?utm_source=chatgpt.com)

Instead of asking:

> "Which node looks important?"

it removes each vendor from the graph and calculates **coverage collapse**. It trains against those simulated failures and validates against historical disruptions. It reports a ~49,842-vendor universe in its defense dataset. ([GitHub][18])

We can generalize this beautifully.

For every node \(v\):

$$
Criticality(v)
=
AGIThroughput(G)-AGIThroughput(G-v)
$$

Then instead of simply saying **"HBM is important"**, we could estimate:

> Removing HBM capacity decreases available AI-compute throughput 63%.

And then:

> Increasing HBM capacity 50% only increases total throughput 17%, because CoWoS subsequently becomes binding.

**Boom. That's the next bottleneck.**

Then simulate:

+50% CoWoS.

Maybe substrates bind.

+50% substrates.

Power binds.

You're computationally walking the bottleneck frontier.

That is much better than a static research report.

---

## What I'd actually build

I wouldn't create another massive schema-heavy research platform. I'd combine the clever parts that already exist:

**ProphetMap**
→ thesis/falsification/scoring discipline

**Keystone + Silicon Stack + Memory Atlas**
→ initial dependency graph

**eugenehp/supplychain**
→ recursive upstream tracing pattern

**alphasig + SEC EDGAR**
→ continual evidence extraction

**Graphiti**
→ temporal edges

**NetworkX**
→ centrality/min-cut/removal simulations

**CHOKEPOINT**
→ counterfactual failure scoring

**River**
→ regime-change detection

**OpenAlex + PatentsView**
→ bottleneck-obsolescence score

**Qlib**
→ historical portfolio simulation.

I would keep the underlying storage boring initially: **Parquet + DuckDB + NetworkX**, not Neo4j. Only introduce a graph DB when queries actually demand it.

And the fundamental object doesn't need 200 fields. Something like:

```text
NODE
id
type
name

EDGE
source
target
relation
amount
capacity
utilization
lead_time
substitutability
valid_from
valid_to
confidence
source_url
```

Then derive everything else.

The important calculated quantities become:

$$
Scarcity =
\frac{DemandGrowth}{CapacityGrowth}
$$

$$
Fragility =
Utilization
\times Concentration
\times LeadTime
\times (1-Substitutability)
$$

and roughly:

$$
BottleneckAlpha =
\frac{
Scarcity \times Persistence \times Criticality
\times PricingPower \times MarketSurprise
}{
Valuation \times ObsolescenceRisk
}
$$

But the really powerful output isn't merely the highest score.

It's:

> **Current bottleneck:** HBM
> **Likely next bottleneck if HBM supply expands:** CoWoS
> **Likely next:** ABF / bonding / power
> **Companies with greatest revenue sensitivity:** ...
> **Market awareness:** ...
> **Research attacking this constraint:** accelerating/decelerating
> **Probability constraint remains binding in 3/6/12/24 months:** ...

### The gap

After searching all of this, I **didn't find a project that combines all four**:

**physical AGI dependency graph + recursive bottleneck discovery + temporal/obsolescence detection + systematic equity reallocation.**

ProphetMap comes closest on the investing side. Keystone comes closest on rigorous industrial dependency mapping. CHOKEPOINT has the best quantitative bottleneck-identification mechanism. Graphiti solves temporal facts.

So I don't think we need to invent the primitives. **The novel project is connecting these four things.**

And I would absolutely clone **ProphetMap, Keystone, CHOKEPOINT, Chip Sense, Silicon Stack and Memory Atlas first** and compare their graph representations before writing ours. One caution: the repositories have different licenses—ProphetMap is MIT and Keystone AGPL-3.0, while `eugenehp/supplychain` is free for non-commercial use but requires permission for commercial deployment, and TWSE-KG is publicly visible but marked proprietary. ([GitHub][1])

This is considerably more developed in the wild than I expected. The striking part is that these independent builders have already converged on **“physical constraints,” “chokepoints,” “dependency graphs,” “falsification,” and even “bottleneck relay”** almost simultaneously. Our extension is making the relay itself the object being predicted.

[1]: https://github.com/Beltran12138/prophetmap "GitHub - Beltran12138/prophetmap: AI industry chain transmission map for US equity alpha discovery — 19-layer propagation model with automated daily scoring · GitHub"
[2]: https://github.com/Skeeter-spec/keystone "GitHub - Skeeter-spec/keystone: A living atlas of the world's industrial value chains, mapped to find the chokepoints. Educational research, not investment advice. · GitHub"
[3]: https://github.com/eugenehp/supplychain?utm_source=chatgpt.com "GitHub - eugenehp/supplychain · GitHub"
[4]: https://github.com/atharvahirulkar/chokepoint "GitHub - atharvahirulkar/chokepoint: Graph ML pipeline that scores defense procurement vendors by mission coverage collapse risk - find structural single points of failure in public contract data before disruption does. · GitHub"
[5]: https://github.com/aminalav/chip-sense "GitHub - aminalav/chip-sense: Open-source research board for the semiconductor supply chain — companies, fabs, cited relationship arcs, trade flows and illustrative stress scenarios. Next.js + MapLibre. · GitHub"
[6]: https://github.com/sflans99/silicon-stack?utm_source=chatgpt.com "GitHub - sflans99/silicon-stack: Interactive semiconductor supply chain visualizer — 239 companies, 1,110 relationships, React + D3 · GitHub"
[7]: https://github.com/upamanyuacharya/memory-atlas "GitHub - upamanyuacharya/memory-atlas: An interactive 3D map of the AI memory supply chain — HBM, CXL, photonics: who makes what, the bottlenecks, and who matters. Single-file Three.js. · GitHub"
[8]: https://github.com/YichengYang-Ethan/ai-supply-chain-research?utm_source=chatgpt.com "GitHub - YichengYang-Ethan/ai-supply-chain-research: Verified ten-sector research on the AI compute build-out, distilled from 311 public SemiAnalysis articles — with an independent credibility audit of the source (664 events, 119 tickers). · GitHub"
[9]: https://github.com/sushaan-k/alphasig?utm_source=chatgpt.com "GitHub - sushaan-k/alphasig: Causal signal extraction from SEC filings using LLMs. · GitHub"
[10]: https://github.com/tunglich/TWSE-KG?utm_source=chatgpt.com "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[11]: https://github.com/Timeverse/My-TW-Coverage "GitHub - Timeverse/My-TW-Coverage: Equity research coverage of 1,735 Taiwan-listed companies (TWSE + OTC). Business overviews, supply chain mapping, and financial data with wikilink cross-referencing. · GitHub"
[12]: https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com "GitHub - supat-roong/stock-relation: Interactive dashboard that maps corporate relationships by parsing financial data and SEC filings into a dynamic knowledge graph of similarity, ownership, and validation. ([GitHub][13])                                                                                 | [https://github.com/Jumade/sec-graph](https://github.com/Jumade/sec-graph?utm_source=chatgpt.com)                                                     |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |

There is also this smaller semiconductor chokepoint analysis project using NetworkX centrality:

[https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis](https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis?utm_source=chatgpt.com) ([GitHub][15])

### ProphetMap is the one to inspect first

Its conceptual model is remarkably close to ours:

**models → accelerators → EDA → semiconductor materials → equipment → packaging → substrates → HBM → servers → networking → power/cooling → optics → construction → power generation → nuclear fuel → grid → commodities → embodied AI.**

It then scores each ticker by physical constraint, whether the company actually captures the scarcity rent, AI revenue sensitivity, time-to-realization and whether the market has already priced it. Most importantly, it maintains **pre-declared falsifiers** and evaluates them daily. ([GitHub][1])

That last part is exactly what was missing from our discussion:

> HBM is the bottleneck — **until what observable event makes that statement false?**

ProphetMap already thinks this way.

Its live frontend is:

[https://prophetmap.vercel.app/](https://prophetmap.vercel.app/?utm_source=chatgpt.com)

Keystone's live industrial maps:

[https://skeeter-spec.github.io/keystone/](https://skeeter-spec.github.io/keystone/?utm_source=chatgpt.com) ([GitHub][2])

Memory Atlas:

[https://memory.upamanyuacharya.com/](https://memory.upamanyuacharya.com/?utm_source=chatgpt.com) ([The Memory Atlas][16])

## 2. Graph/math projects that give us the quantitative machinery

We shouldn't build our own graph science. These give us nearly everything.

| Tool           | What I'd use it for                                                                                                                          | Link                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **NetworkX**   | betweenness, PageRank, articulation nodes, centrality, shortest paths, min-cut/max-flow and simulated node removal                           | [https://github.com/networkx/networkx](https://github.com/networkx/networkx?utm_source=chatgpt.com)         |
| **Graphiti**   | **temporal knowledge graph** — crucial because dependencies become true/false through time rather than being permanent facts. ([GitHub][17]) | [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti?utm_source=chatgpt.com)             |
| **cuGraph**    | GPU-accelerated graph analysis once the graph gets enormous                                                                                  | [https://github.com/rapidsai/cugraph](https://github.com/rapidsai/cugraph?utm_source=chatgpt.com)           |
| **River**      | online ML + concept/drift detection: detect when a bottleneck regime changes                                                                 | [https://github.com/online-ml/river](https://github.com/online-ml/river?utm_source=chatgpt.com)             |
| **ruptures**   | historical change-point detection                                                                                                            | [https://github.com/deepcharles/ruptures](https://github.com/deepcharles/ruptures?utm_source=chatgpt.com)   |
| **Tigramite**  | causal discovery on time series rather than merely observing correlation                                                                     | [https://github.com/jakobrunge/tigramite](https://github.com/jakobrunge/tigramite?utm_source=chatgpt.com)   |
| **DoWhy**      | intervention/counterfactual analysis: “if HBM capacity rises 50%, what becomes binding?”                                                     | [https://github.com/py-why/dowhy](https://github.com/py-why/dowhy?utm_source=chatgpt.com)                   |
| **Qlib**       | convert bottleneck signals into an actual backtested dynamic portfolio                                                                       | [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib?utm_source=chatgpt.com)               |
| **OpenBB**     | market/fundamental data abstraction layer                                                                                                    | [https://github.com/OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB?utm_source=chatgpt.com) |
| **PyPSA**      | physically model the electricity/grid branch rather than relying on narratives                                                               | [https://github.com/PyPSA/PyPSA](https://github.com/PyPSA/PyPSA?utm_source=chatgpt.com)                     |
| **gridstatus** | live ISO electricity demand, generation and pricing                                                                                          | [https://github.com/gridstatus/gridstatus](https://github.com/gridstatus/gridstatus?utm_source=chatgpt.com) |
| **pymrio**     | global input-output dependency analysis                                                                                                      | [https://github.com/IndEcol/pymrio](https://github.com/IndEcol/pymrio?utm_source=chatgpt.com)               |
| **leontief**   | U.S. BEA input-output tables → direct + indirect dependency multipliers                                                                      | [https://github.com/andenick/leontief](https://github.com/andenick/leontief?utm_source=chatgpt.com)         |

Graphiti is particularly important for our thesis.

Instead of storing:

`AI → REQUIRES → HBM`

we should store something closer to:

`AI architecture X → REQUIRES → HBM bandwidth`

with:

`valid_from`
`valid_to`
`quantity_per_unit_compute`
`confidence`
`evidence`
`architecture`

Because your hypothetical ChatGPT-8 event shouldn't delete historical knowledge. It should turn:

**HBM requirement: high, valid Jan–Sep 2026**

into

**HBM requirement: dramatically lower, valid from Oct 2026**

and immediately propagate that change through the graph.

That's precisely why a temporal KG is superior to a conventional static supply-chain diagram. Graphiti is specifically designed around time-valid facts and incremental graph updates. ([GitHub][17])

## 3. Free raw data we can continuously feed it

This is where it becomes much more powerful than any of those individual projects.

| Dataset                 | What it tells us                                                                      | Full resource                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SEC EDGAR**           | supplier concentration, customers, capex, capacity, risks, contracts, backlog         | [https://www.sec.gov/about/developer-resources](https://www.sec.gov/about/developer-resources?utm_source=chatgpt.com)                                                               |
| **UN Comtrade**         | who actually exports/imports a material/component and geographic concentration        | [https://uncomtrade.org/docs/un-comtrade-api/](https://uncomtrade.org/docs/un-comtrade-api/?utm_source=chatgpt.com)                                                               |
| **BEA Input-Output**    | U.S. industry → industry dependencies                                                 | [https://www.bea.gov/data/industries/input-output-accounts-data](https://www.bea.gov/data/industries/input-output-accounts-data?utm_source=chatgpt.com)                             |
| **BEA API**             | automate the above                                                                    | [https://apps.bea.gov/api/signup/](https://apps.bea.gov/api/signup/?utm_source=chatgpt.com)                                                                                         |
| **OECD ICIO**           | global inter-country input/output dependencies                                        | [https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html](https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html?utm_source=chatgpt.com) |
| **EXIOBASE**            | extremely detailed global multi-regional production network                           | [https://exiobase.eu/](https://exiobase.eu/?utm_source=chatgpt.com)                                                                                                                 |
| **USGS Minerals**       | production/concentration/reserves for gallium, uranium, copper, rare earths etc.      | [https://www.usgs.gov/centers/national-minerals-information-center/tools](https://www.usgs.gov/centers/national-minerals-information-center/tools?utm_source=chatgpt.com)           |
| **EIA API**             | power generation, capacity, demand and grid flows                                     | [https://www.eia.gov/opendata/](https://www.eia.gov/opendata/?utm_source=chatgpt.com)                                                                                               |
| **OpenAlex**            | research velocity — incredibly useful for detecting scientists attacking a bottleneck | [https://help.openalex.org/api/](https://help.openalex.org/api/?utm_source=chatgpt.com)                                                                                             |
| **PatentsView / USPTO** | patent acceleration around substitutes/new architectures                              | [https://www.uspto.gov/ip-policy/economic-research/patentsview](https://www.uspto.gov/ip-policy/economic-research/patentsview?utm_source=chatgpt.com)                               |
| **FRED**                | prices, industrial production, commodities and macro time series                      | [https://fred.stlouisfed.org/docs/api/fred/overview.html](https://fred.stlouisfed.org/docs/api/fred/overview.html?utm_source=chatgpt.com)                                         |
| **Wikidata SPARQL**     | entity resolution: companies, facilities, subsidiaries, countries, products           | [https://query.wikidata.org/](https://query.wikidata.org/?utm_source=chatgpt.com)                                                                                                   |
| **GDELT**               | machine-readable live world news/event stream                                         | [https://www.gdeltproject.org/](https://www.gdeltproject.org/?utm_source=chatgpt.com)                                                                                               |

The **OpenAlex + USPTO** combination is especially interesting because it gives us something normal supply-chain maps completely miss:

### probability that the bottleneck is about to be destroyed.

For every bottleneck node, track:

**papers about reducing requirement for X**
**papers about substitutes for X**
**patent acceleration**
**new architecture announcements**
**startup funding targeting X**
**benchmark improvements reducing X/unit of intelligence**

So while HBM's *current scarcity score* might increase, its *expected persistence* could simultaneously fall.

That is exactly your ChatGPT-8 scenario.

## 4. I think our graph should go deeper than ProphetMap

ProphetMap is primarily:

**sector/layer → ticker**

We want:

**AGI capability**
→ **technical requirement**
→ **system**
→ **process**
→ **component**
→ **material**
→ **equipment**
→ **factory**
→ **company**
→ **geography**
→ **stock**

For example:

**frontier inference**
→ memory bandwidth
→ HBM3E/HBM4
→ stacked DRAM
→ TSV
→ wafer thinning
→ TC/hybrid bonding
→ CoWoS
→ ABF substrate
→ ABF film
→ Ajinomoto
→ chemical/feedstock/equipment dependency...

And every node can itself recursively answer:

> **What constrains increasing the output of this node?**

That creates the graph automatically.

This is actually the simplest definition of our system:

$$
\boxed{
B(x)=\text{What prevents production of }x\text{ increasing?}
}
$$

Apply `B()` recursively.

For HBM:

**HBM**
→ DRAM wafer capacity
→ yields
→ TSV
→ bonding machines
→ packaging capacity
→ substrates
→ electricity
→ ultrapure water
→ specialized labor
→ fab equipment.

Then recursively:

**bonding machines**
→ precision stages
→ optics
→ encoders
→ motors
→ bearings
→ specialty materials...

And suddenly you hit exactly the obscure companies we've been finding.

## 5. The CHOKEPOINT idea gives us the quantitative breakthrough

The most interesting methodology I found outside ProphetMap may actually be this tiny **zero-star/low-star personal repo**:

[https://github.com/atharvahirulkar/chokepoint](https://github.com/atharvahirulkar/chokepoint?utm_source=chatgpt.com)

Instead of asking:

> "Which node looks important?"

it removes each vendor from the graph and calculates **coverage collapse**. It trains against those simulated failures and validates against historical disruptions. It reports a ~49,842-vendor universe in its defense dataset. ([GitHub][18])

We can generalize this beautifully.

For every node \(v\):

$$
Criticality(v)
=
AGIThroughput(G)-AGIThroughput(G-v)
$$

Then instead of simply saying **"HBM is important"**, we could estimate:

> Removing HBM capacity decreases available AI-compute throughput 63%.

And then:

> Increasing HBM capacity 50% only increases total throughput 17%, because CoWoS subsequently becomes binding.

**Boom. That's the next bottleneck.**

Then simulate:

+50% CoWoS.

Maybe substrates bind.

+50% substrates.

Power binds.

You're computationally walking the bottleneck frontier.

That is much better than a static research report.

---

## What I'd actually build

I wouldn't create another massive schema-heavy research platform. I'd combine the clever parts that already exist:

**ProphetMap**
→ thesis/falsification/scoring discipline

**Keystone + Silicon Stack + Memory Atlas**
→ initial dependency graph

**eugenehp/supplychain**
→ recursive upstream tracing pattern

**alphasig + SEC EDGAR**
→ continual evidence extraction

**Graphiti**
→ temporal edges

**NetworkX**
→ centrality/min-cut/removal simulations

**CHOKEPOINT**
→ counterfactual failure scoring

**River**
→ regime-change detection

**OpenAlex + PatentsView**
→ bottleneck-obsolescence score

**Qlib**
→ historical portfolio simulation.

I would keep the underlying storage boring initially: **Parquet + DuckDB + NetworkX**, not Neo4j. Only introduce a graph DB when queries actually demand it.

And the fundamental object doesn't need 200 fields. Something like:

```text
NODE
id
type
name

EDGE
source
target
relation
amount
capacity
utilization
lead_time
substitutability
valid_from
valid_to
confidence
source_url
```

Then derive everything else.

The important calculated quantities become:

$$
Scarcity =
\frac{DemandGrowth}{CapacityGrowth}
$$

$$
Fragility =
Utilization
\times Concentration
\times LeadTime
\times (1-Substitutability)
$$

and roughly:

$$
BottleneckAlpha =
\frac{
Scarcity \times Persistence \times Criticality
\times PricingPower \times MarketSurprise
}{
Valuation \times ObsolescenceRisk
}
```

But the really powerful output isn't merely the highest score.

It's:

> **Current bottleneck:** HBM
> **Likely next bottleneck if HBM supply expands:** CoWoS
> **Likely next:** ABF / bonding / power
> **Companies with greatest revenue sensitivity:** ...
> **Market awareness:** ...
> **Research attacking this constraint:** accelerating/decelerating
> **Probability constraint remains binding in 3/6/12/24 months:** ...

### The gap

After searching all of this, I **didn't find a project that combines all four**:

**physical AGI dependency graph + recursive bottleneck discovery + temporal/obsolescence detection + systematic equity reallocation.**

ProphetMap comes closest on the investing side. Keystone comes closest on rigorous industrial dependency mapping. CHOKEPOINT has the best quantitative bottleneck-identification mechanism. Graphiti solves temporal facts.

So I don't think we need to invent the primitives. **The novel project is connecting these four things.**

And I would absolutely clone **ProphetMap, Keystone, CHOKEPOINT, Chip Sense, Silicon Stack and Memory Atlas first** and compare their graph representations before writing ours. One caution: the repositories have different licenses—ProphetMap is MIT and Keystone AGPL-3.0, while `eugenehp/supplychain` is free for non-commercial use but requires permission for commercial deployment, and TWSE-KG is publicly visible but marked proprietary. ([GitHub][1])

This is considerably more developed in the wild than I expected. The striking part is that these independent builders have already converged on **“physical constraints,” “chokepoints,” “dependency graphs,” “falsification,” and even “bottleneck relay”** almost simultaneously. Our extension is making the relay itself the object being predicted.

[1]: https://github.com/Beltran12138/prophetmap "GitHub - Beltran12138/prophetmap: AI industry chain transmission map for US equity alpha discovery — 19-layer propagation model with automated daily scoring · GitHub"
[2]: https://github.com/Skeeter-spec/keystone "GitHub - Skeeter-spec/keystone: A living atlas of the world's industrial value chains, mapped to find the chokepoints. Educational research, not investment advice. · GitHub"
[3]: https://github.com/eugenehp/supplychain?utm_source=chatgpt.com "GitHub - eugenehp/supplychain · GitHub"
[4]: https://github.com/atharvahirulkar/chokepoint "GitHub - atharvahirulkar/chokepoint: Graph ML pipeline that scores defense procurement vendors by mission coverage collapse risk - find structural single points of failure in public contract data before disruption does. · GitHub"
[5]: https://github.com/aminalav/chip-sense "GitHub - aminalav/chip-sense: Open-source research board for the semiconductor supply chain — companies, fabs, cited relationship arcs, trade flows and illustrative stress scenarios. Next.js + MapLibre. · GitHub"
[6]: https://github.com/sflans99/silicon-stack?utm_source=chatgpt.com "GitHub - sflans99/silicon-stack: Interactive semiconductor supply chain visualizer — 239 companies, 1,110 relationships, React + D3 · GitHub"
[7]: https://github.com/upamanyuacharya/memory-atlas "GitHub - upamanyuacharya/memory-atlas: An interactive 3D map of the AI memory supply chain — HBM, CXL, photonics: who makes what, the bottlenecks, and who matters. Single-file Three.js. · GitHub"
[8]: https://github.com/YichengYang-Ethan/ai-supply-chain-research?utm_source=chatgpt.com "GitHub - YichengYang-Ethan/ai-supply-chain-research: Verified ten-sector research on the AI compute build-out, distilled from 311 public SemiAnalysis articles — with an independent credibility audit of the source (664 events, 119 tickers). · GitHub"
[9]: https://github.com/sushaan-k/alphasig?utm_source=chatgpt.com "GitHub - sushaan-k/alphasig: Causal signal extraction from SEC filings using LLMs. · GitHub"
[10]: https://github.com/tunglich/TWSE-KG?utm_source=chatgpt.com "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[11]: https://github.com/Timeverse/My-TW-Coverage "GitHub - Timeverse/My-TW-Coverage: Equity research coverage of 1,735 Taiwan-listed companies (TWSE + OTC). Business overviews, supply chain mapping, and financial data with wikilink cross-referencing. · GitHub"
[12]: https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com "GitHub - supat-roong/stock-relation: Interactive dashboard that maps corporate relationships by parsing financial data and SEC filings into a dynamic knowledge graph of similarity, ownership, and validation. ([GitHub][13])                                                                                 | [https://github.com/Jumade/sec-graph](https://github.com/Jumade/sec-graph?utm_source=chatgpt.com)                                                     |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |

There is also this smaller semiconductor chokepoint analysis project using NetworkX centrality:

[https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis](https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis?utm_source=chatgpt.com) ([GitHub][15])

### ProphetMap is the one to inspect first

Its conceptual model is remarkably close to ours:

**models → accelerators → EDA → semiconductor materials → equipment → packaging → substrates → HBM → servers → networking → power/cooling → optics → construction → power generation → nuclear fuel → grid → commodities → embodied AI.**

It then scores each ticker by physical constraint, whether the company actually captures the scarcity rent, AI revenue sensitivity, time-to-realization and whether the market has already priced it. Most importantly, it maintains **pre-declared falsifiers** and evaluates them daily. ([GitHub][1])

That last part is exactly what was missing from our discussion:

> HBM is the bottleneck — **until what observable event makes that statement false?**

ProphetMap already thinks this way.

Its live frontend is:

[https://prophetmap.vercel.app/](https://prophetmap.vercel.app/?utm_source=chatgpt.com)

Keystone's live industrial maps:

[https://skeeter-spec.github.io/keystone/](https://skeeter-spec.github.io/keystone/?utm_source=chatgpt.com) ([GitHub][2])

Memory Atlas:

[https://memory.upamanyuacharya.com/](https://memory.upamanyuacharya.com/?utm_source=chatgpt.com) ([The Memory Atlas][16])

## 2. Graph/math projects that give us the quantitative machinery

We shouldn't build our own graph science. These give us nearly everything.

| Tool           | What I'd use it for                                                                                                                          | Link                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **NetworkX**   | betweenness, PageRank, articulation nodes, centrality, shortest paths, min-cut/max-flow and simulated node removal                           | [https://github.com/networkx/networkx](https://github.com/networkx/networkx?utm_source=chatgpt.com)         |
| **Graphiti**   | **temporal knowledge graph** — crucial because dependencies become true/false through time rather than being permanent facts. ([GitHub][17]) | [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti?utm_source=chatgpt.com)             |
| **cuGraph**    | GPU-accelerated graph analysis once the graph gets enormous                                                                                  | [https://github.com/rapidsai/cugraph](https://github.com/rapidsai/cugraph?utm_source=chatgpt.com)           |
| **River**      | online ML + concept/drift detection: detect when a bottleneck regime changes                                                                 | [https://github.com/online-ml/river](https://github.com/online-ml/river?utm_source=chatgpt.com)             |
| **ruptures**   | historical change-point detection                                                                                                            | [https://github.com/deepcharles/ruptures](https://github.com/deepcharles/ruptures?utm_source=chatgpt.com)   |
| **Tigramite**  | causal discovery on time series rather than merely observing correlation                                                                     | [https://github.com/jakobrunge/tigramite](https://github.com/jakobrunge/tigramite?utm_source=chatgpt.com)   |
| **DoWhy**      | intervention/counterfactual analysis: “if HBM capacity rises 50%, what becomes binding?”                                                     | [https://github.com/py-why/dowhy](https://github.com/py-why/dowhy?utm_source=chatgpt.com)                   |
| **Qlib**       | convert bottleneck signals into an actual backtested dynamic portfolio                                                                       | [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib?utm_source=chatgpt.com)               |
| **OpenBB**     | market/fundamental data abstraction layer                                                                                                    | [https://github.com/OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB?utm_source=chatgpt.com) |
| **PyPSA**      | physically model the electricity/grid branch rather than relying on narratives                                                               | [https://github.com/PyPSA/PyPSA](https://github.com/PyPSA/PyPSA?utm_source=chatgpt.com)                     |
| **gridstatus** | live ISO electricity demand, generation and pricing                                                                                          | [https://github.com/gridstatus/gridstatus](https://github.com/gridstatus/gridstatus?utm_source=chatgpt.com) |
| **pymrio**     | global input-output dependency analysis                                                                                                      | [https://github.com/IndEcol/pymrio](https://github.com/IndEcol/pymrio?utm_source=chatgpt.com)               |
| **leontief**   | U.S. BEA input-output tables → direct + indirect dependency multipliers                                                                      | [https://github.com/andenick/leontief](https://github.com/andenick/leontief?utm_source=chatgpt.com)         |

Graphiti is particularly important for our thesis.

Instead of storing:

`AI → REQUIRES → HBM`

we should store something closer to:

`AI architecture X → REQUIRES → HBM bandwidth`

with:

`valid_from`
`valid_to`
`quantity_per_unit_compute`
`confidence`
`evidence`
`architecture`

Because your hypothetical ChatGPT-8 event shouldn't delete historical knowledge. It should turn:

**HBM requirement: high, valid Jan–Sep 2026**

into

**HBM requirement: dramatically lower, valid from Oct 2026**

and immediately propagate that change through the graph.

That's precisely why a temporal KG is superior to a conventional static supply-chain diagram. Graphiti is specifically designed around time-valid facts and incremental graph updates. ([GitHub][17])

## 3. Free raw data we can continuously feed it

This is where it becomes much more powerful than any of those individual projects.

| Dataset                 | What it tells us                                                                      | Full resource                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SEC EDGAR**           | supplier concentration, customers, capex, capacity, risks, contracts, backlog         | [https://www.sec.gov/about/developer-resources](https://www.sec.gov/about/developer-resources?utm_source=chatgpt.com)                                                               |
| **UN Comtrade**         | who actually exports/imports a material/component and geographic concentration        | [https://uncomtrade.org/docs/un-comtrade-api/](https://uncomtrade.org/docs/un-comtrade-api/?utm_source=chatgpt.com)                                                               |
| **BEA Input-Output**    | U.S. industry → industry dependencies                                                 | [https://www.bea.gov/data/industries/input-output-accounts-data](https://www.bea.gov/data/industries/input-output-accounts-data?utm_source=chatgpt.com)                             |
| **BEA API**             | automate the above                                                                    | [https://apps.bea.gov/api/signup/](https://apps.bea.gov/api/signup/?utm_source=chatgpt.com)                                                                                         |
| **OECD ICIO**           | global inter-country input/output dependencies                                        | [https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html](https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html?utm_source=chatgpt.com) |
| **EXIOBASE**            | extremely detailed global multi-regional production network                           | [https://exiobase.eu/](https://exiobase.eu/?utm_source=chatgpt.com)                                                                                                                 |
| **USGS Minerals**       | production/concentration/reserves for gallium, uranium, copper, rare earths etc.      | [https://www.usgs.gov/centers/national-minerals-information-center/tools](https://www.usgs.gov/centers/national-minerals-information-center/tools?utm_source=chatgpt.com)           |
| **EIA API**             | power generation, capacity, demand and grid flows                                     | [https://www.eia.gov/opendata/](https://www.eia.gov/opendata/?utm_source=chatgpt.com)                                                                                               |
| **OpenAlex**            | research velocity — incredibly useful for detecting scientists attacking a bottleneck | [https://help.openalex.org/api/](https://help.openalex.org/api/?utm_source=chatgpt.com)                                                                                             |
| **PatentsView / USPTO** | patent acceleration around substitutes/new architectures                              | [https://www.uspto.gov/ip-policy/economic-research/patentsview](https://www.uspto.gov/ip-policy/economic-research/patentsview?utm_source=chatgpt.com)                               |
| **FRED**                | prices, industrial production, commodities and macro time series                      | [https://fred.stlouisfed.org/docs/api/fred/overview.html](https://fred.stlouisfed.org/docs/api/fred/overview.html?utm_source=chatgpt.com)                                         |
| **Wikidata SPARQL**     | entity resolution: companies, facilities, subsidiaries, countries, products           | [https://query.wikidata.org/](https://query.wikidata.org/?utm_source=chatgpt.com)                                                                                                   |
| **GDELT**               | machine-readable live world news/event stream                                         | [https://www.gdeltproject.org/](https://www.gdeltproject.org/?utm_source=chatgpt.com)                                                                                               |

The **OpenAlex + USPTO** combination is especially interesting because it gives us something normal supply-chain maps completely miss:

### probability that the bottleneck is about to be destroyed.

For every bottleneck node, track:

**papers about reducing requirement for X**
**papers about substitutes for X**
**patent acceleration**
**new architecture announcements**
**startup funding targeting X**
**benchmark improvements reducing X/unit of intelligence**

So while HBM's *current scarcity score* might increase, its *expected persistence* could simultaneously fall.

That is exactly your ChatGPT-8 scenario.

## 4. I think our graph should go deeper than ProphetMap

ProphetMap is primarily:

**sector/layer → ticker**

We want:

**AGI capability**
→ **technical requirement**
→ **system**
→ **process**
→ **component**
→ **material**
→ **equipment**
→ **factory**
→ **company**
→ **geography**
→ **stock**

For example:

**frontier inference**
→ memory bandwidth
→ HBM3E/HBM4
→ stacked DRAM
→ TSV
→ wafer thinning
→ TC/hybrid bonding
→ CoWoS
→ ABF substrate
→ ABF film
→ Ajinomoto
→ chemical/feedstock/equipment dependency...

And every node can itself recursively answer:

> **What constrains increasing the output of this node?**

That creates the graph automatically.

This is actually the simplest definition of our system:

$$
\boxed{
B(x)=\text{What prevents production of }x\text{ increasing?}
}
$$

Apply `B()` recursively.

For HBM:

**HBM**
→ DRAM wafer capacity
→ yields
→ TSV
→ bonding machines
→ packaging capacity
→ substrates
→ electricity
→ ultrapure water
→ specialized labor
→ fab equipment.

Then recursively:

**bonding machines**
→ precision stages
→ optics
→ encoders
→ motors
→ bearings
→ specialty materials...

And suddenly you hit exactly the obscure companies we've been finding.

## 5. The CHOKEPOINT idea gives us the quantitative breakthrough

The most interesting methodology I found outside ProphetMap may actually be this tiny **zero-star/low-star personal repo**:

[https://github.com/atharvahirulkar/chokepoint](https://github.com/atharvahirulkar/chokepoint?utm_source=chatgpt.com)

Instead of asking:

> "Which node looks important?"

it removes each vendor from the graph and calculates **coverage collapse**. It trains against those simulated failures and validates against historical disruptions. It reports a ~49,842-vendor universe in its defense dataset. ([GitHub][18])

We can generalize this beautifully.

For every node \(v\):

$$
Criticality(v)
=
AGIThroughput(G)-AGIThroughput(G-v)
$$

Then instead of simply saying **"HBM is important"**, we could estimate:

> Removing HBM capacity decreases available AI-compute throughput 63%.

And then:

> Increasing HBM capacity 50% only increases total throughput 17%, because CoWoS subsequently becomes binding.

**Boom. That's the next bottleneck.**

Then simulate:

+50% CoWoS.

Maybe substrates bind.

+50% substrates.

Power binds.

You're computationally walking the bottleneck frontier.

That is much better than a static research report.

---

## What I'd actually build

I wouldn't create another massive schema-heavy research platform. I'd combine the clever parts that already exist:

**ProphetMap**
→ thesis/falsification/scoring discipline

**Keystone + Silicon Stack + Memory Atlas**
→ initial dependency graph

**eugenehp/supplychain**
→ recursive upstream tracing pattern

**alphasig + SEC EDGAR**
→ continual evidence extraction

**Graphiti**
→ temporal edges

**NetworkX**
→ centrality/min-cut/removal simulations

**CHOKEPOINT**
→ counterfactual failure scoring

**River**
→ regime-change detection

**OpenAlex + PatentsView**
→ bottleneck-obsolescence score

**Qlib**
→ historical portfolio simulation.

I would keep the underlying storage boring initially: **Parquet + DuckDB + NetworkX**, not Neo4j. Only introduce a graph DB when queries actually demand it.

And the fundamental object doesn't need 200 fields. Something like:

```text
NODE
id
type
name

EDGE
source
target
relation
amount
capacity
utilization
lead_time
substitutability
valid_from
valid_to
confidence
source_url
```

Then derive everything else.

The important calculated quantities become:

$$
Scarcity =
\frac{DemandGrowth}{CapacityGrowth}
$$

$$
Fragility =
Utilization
\times Concentration
\times LeadTime
\times (1-Substitutability)
$$

and roughly:

$$
BottleneckAlpha =
\frac{
Scarcity \times Persistence \times Criticality
\times PricingPower \times MarketSurprise
}{
Valuation \times ObsolescenceRisk
}
```

But the really powerful output isn't merely the highest score.

It's:

> **Current bottleneck:** HBM
> **Likely next bottleneck if HBM supply expands:** CoWoS
> **Likely next:** ABF / bonding / power
> **Companies with greatest revenue sensitivity:** ...
> **Market awareness:** ...
> **Research attacking this constraint:** accelerating/decelerating
> **Probability constraint remains binding in 3/6/12/24 months:** ...

### The gap

After searching all of this, I **didn't find a project that combines all four**:

**physical AGI dependency graph + recursive bottleneck discovery + temporal/obsolescence detection + systematic equity reallocation.**

ProphetMap comes closest on the investing side. Keystone comes closest on rigorous industrial dependency mapping. CHOKEPOINT has the best quantitative bottleneck-identification mechanism. Graphiti solves temporal facts.

So I don't think we need to invent the primitives. **The novel project is connecting these four things.**

And I would absolutely clone **ProphetMap, Keystone, CHOKEPOINT, Chip Sense, Silicon Stack and Memory Atlas first** and compare their graph representations before writing ours. One caution: the repositories have different licenses—ProphetMap is MIT and Keystone AGPL-3.0, while `eugenehp/supplychain` is free for non-commercial use but requires permission for commercial deployment, and TWSE-KG is publicly visible but marked proprietary. ([GitHub][1])

This is considerably more developed in the wild than I expected. The striking part is that these independent builders have already converged on **“physical constraints,” “chokepoints,” “dependency graphs,” “falsification,” and even “bottleneck relay”** almost simultaneously. Our extension is making the relay itself the object being predicted.

[1]: https://github.com/Beltran12138/prophetmap "GitHub - Beltran12138/prophetmap: AI industry chain transmission map for US equity alpha discovery — 19-layer propagation model with automated daily scoring · GitHub"
[2]: https://github.com/Skeeter-spec/keystone "GitHub - Skeeter-spec/keystone: A living atlas of the world's industrial value chains, mapped to find the chokepoints. Educational research, not investment advice. · GitHub"
[3]: https://github.com/eugenehp/supplychain?utm_source=chatgpt.com "GitHub - eugenehp/supplychain · GitHub"
[4]: https://github.com/atharvahirulkar/chokepoint "GitHub - atharvahirulkar/chokepoint: Graph ML pipeline that scores defense procurement vendors by mission coverage collapse risk - find structural single points of failure in public contract data before disruption does. · GitHub"
[5]: https://github.com/aminalav/chip-sense "GitHub - aminalav/chip-sense: Open-source research board for the semiconductor supply chain — companies, fabs, cited relationship arcs, trade flows and illustrative stress scenarios. Next.js + MapLibre. · GitHub"
[6]: https://github.com/sflans99/silicon-stack?utm_source=chatgpt.com "GitHub - sflans99/silicon-stack: Interactive semiconductor supply chain visualizer — 239 companies, 1,110 relationships, React + D3 · GitHub"
[7]: https://github.com/upamanyuacharya/memory-atlas "GitHub - upamanyuacharya/memory-atlas: An interactive 3D map of the AI memory supply chain — HBM, CXL, photonics: who makes what, the bottlenecks, and who matters. Single-file Three.js. · GitHub"
[8]: https://github.com/YichengYang-Ethan/ai-supply-chain-research?utm_source=chatgpt.com "GitHub - YichengYang-Ethan/ai-supply-chain-research: Verified ten-sector research on the AI compute build-out, distilled from 311 public SemiAnalysis articles — with an independent credibility audit of the source (664 events, 119 tickers). · GitHub"
[9]: https://github.com/sushaan-k/alphasig?utm_source=chatgpt.com "GitHub - sushaan-k/alphasig: Causal signal extraction from SEC filings using LLMs. · GitHub"
[10]: https://github.com/tunglich/TWSE-KG?utm_source=chatgpt.com "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[11]: https://github.com/Timeverse/My-TW-Coverage "GitHub - Timeverse/My-TW-Coverage: Equity research coverage of 1,735 Taiwan-listed companies (TWSE + OTC). Business overviews, supply chain mapping, and financial data with wikilink cross-referencing. · GitHub"
[12]: https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com "GitHub - supat-roong/stock-relation: Interactive dashboard that maps corporate relationships by parsing financial data and SEC filings into a dynamic knowledge graph of similarity, ownership, and validation. ([GitHub][13])                                                                                 | [https://github.com/Jumade/sec-graph](https://github.com/Jumade/sec-graph?utm_source=chatgpt.com)                                                     |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |

There is also this smaller semiconductor chokepoint analysis project using NetworkX centrality:

[https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis](https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis?utm_source=chatgpt.com) ([GitHub][15])

### ProphetMap is the one to inspect first

Its conceptual model is remarkably close to ours:

**models → accelerators → EDA → semiconductor materials → equipment → packaging → substrates → HBM → servers → networking → power/cooling → optics → construction → power generation → nuclear fuel → grid → commodities → embodied AI.**

It then scores each ticker by physical constraint, whether the company actually captures the scarcity rent, AI revenue sensitivity, time-to-realization and whether the market has already priced it. Most importantly, it maintains **pre-declared falsifiers** and evaluates them daily. ([GitHub][1])

That last part is exactly what was missing from our discussion:

> HBM is the bottleneck — **until what observable event makes that statement false?**

ProphetMap already thinks this way.

Its live frontend is:

[https://prophetmap.vercel.app/](https://prophetmap.vercel.app/?utm_source=chatgpt.com)

Keystone's live industrial maps:

[https://skeeter-spec.github.io/keystone/](https://skeeter-spec.github.io/keystone/?utm_source=chatgpt.com) ([GitHub][2])

Memory Atlas:

[https://memory.upamanyuacharya.com/](https://memory.upamanyuacharya.com/?utm_source=chatgpt.com) ([The Memory Atlas][16])

## 2. Graph/math projects that give us the quantitative machinery

We shouldn't build our own graph science. These give us nearly everything.

| Tool           | What I'd use it for                                                                                                                          | Link                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **NetworkX**   | betweenness, PageRank, articulation nodes, centrality, shortest paths, min-cut/max-flow and simulated node removal                           | [https://github.com/networkx/networkx](https://github.com/networkx/networkx?utm_source=chatgpt.com)         |
| **Graphiti**   | **temporal knowledge graph** — crucial because dependencies become true/false through time rather than being permanent facts. ([GitHub][17]) | [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti?utm_source=chatgpt.com)             |
| **cuGraph**    | GPU-accelerated graph analysis once the graph gets enormous                                                                                  | [https://github.com/rapidsai/cugraph](https://github.com/rapidsai/cugraph?utm_source=chatgpt.com)           |
| **River**      | online ML + concept/drift detection: detect when a bottleneck regime changes                                                                 | [https://github.com/online-ml/river](https://github.com/online-ml/river?utm_source=chatgpt.com)             |
| **ruptures**   | historical change-point detection                                                                                                            | [https://github.com/deepcharles/ruptures](https://github.com/deepcharles/ruptures?utm_source=chatgpt.com)   |
| **Tigramite**  | causal discovery on time series rather than merely observing correlation                                                                     | [https://github.com/jakobrunge/tigramite](https://github.com/jakobrunge/tigramite?utm_source=chatgpt.com)   |
| **DoWhy**      | intervention/counterfactual analysis: “if HBM capacity rises 50%, what becomes binding?”                                                     | [https://github.com/py-why/dowhy](https://github.com/py-why/dowhy?utm_source=chatgpt.com)                   |
| **Qlib**       | convert bottleneck signals into an actual backtested dynamic portfolio                                                                       | [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib?utm_source=chatgpt.com)               |
| **OpenBB**     | market/fundamental data abstraction layer                                                                                                    | [https://github.com/OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB?utm_source=chatgpt.com) |
| **PyPSA**      | physically model the electricity/grid branch rather than relying on narratives                                                               | [https://github.com/PyPSA/PyPSA](https://github.com/PyPSA/PyPSA?utm_source=chatgpt.com)                     |
| **gridstatus** | live ISO electricity demand, generation and pricing                                                                                          | [https://github.com/gridstatus/gridstatus](https://github.com/gridstatus/gridstatus?utm_source=chatgpt.com) |
| **pymrio**     | global input-output dependency analysis                                                                                                      | [https://github.com/IndEcol/pymrio](https://github.com/IndEcol/pymrio?utm_source=chatgpt.com)               |
| **leontief**   | U.S. BEA input-output tables → direct + indirect dependency multipliers                                                                      | [https://github.com/andenick/leontief](https://github.com/andenick/leontief?utm_source=chatgpt.com)         |

Graphiti is particularly important for our thesis.

Instead of storing:

`AI → REQUIRES → HBM`

we should store something closer to:

`AI architecture X → REQUIRES → HBM bandwidth`

with:

`valid_from`
`valid_to`
`quantity_per_unit_compute`
`confidence`
`evidence`
`architecture`

Because your hypothetical ChatGPT-8 event shouldn't delete historical knowledge. It should turn:

**HBM requirement: high, valid Jan–Sep 2026**

into

**HBM requirement: dramatically lower, valid from Oct 2026**

and immediately propagate that change through the graph.

That's precisely why a temporal KG is superior to a conventional static supply-chain diagram. Graphiti is specifically designed around time-valid facts and incremental graph updates. ([GitHub][17])

## 3. Free raw data we can continuously feed it

This is where it becomes much more powerful than any of those individual projects.

| Dataset                 | What it tells us                                                                      | Full resource                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SEC EDGAR**           | supplier concentration, customers, capex, capacity, risks, contracts, backlog         | [https://www.sec.gov/about/developer-resources](https://www.sec.gov/about/developer-resources?utm_source=chatgpt.com)                                                               |
| **UN Comtrade**         | who actually exports/imports a material/component and geographic concentration        | [https://uncomtrade.org/docs/un-comtrade-api/](https://uncomtrade.org/docs/un-comtrade-api/?utm_source=chatgpt.com)                                                               |
| **BEA Input-Output**    | U.S. industry → industry dependencies                                                 | [https://www.bea.gov/data/industries/input-output-accounts-data](https://www.bea.gov/data/industries/input-output-accounts-data?utm_source=chatgpt.com)                             |
| **BEA API**             | automate the above                                                                    | [https://apps.bea.gov/api/signup/](https://apps.bea.gov/api/signup/?utm_source=chatgpt.com)                                                                                         |
| **OECD ICIO**           | global inter-country input/output dependencies                                        | [https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html](https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html?utm_source=chatgpt.com) |
| **EXIOBASE**            | extremely detailed global multi-regional production network                           | [https://exiobase.eu/](https://exiobase.eu/?utm_source=chatgpt.com)                                                                                                                 |
| **USGS Minerals**       | production/concentration/reserves for gallium, uranium, copper, rare earths etc.      | [https://www.usgs.gov/centers/national-minerals-information-center/tools](https://www.usgs.gov/centers/national-minerals-information-center/tools?utm_source=chatgpt.com)           |
| **EIA API**             | power generation, capacity, demand and grid flows                                     | [https://www.eia.gov/opendata/](https://www.eia.gov/opendata/?utm_source=chatgpt.com)                                                                                               |
| **OpenAlex**            | research velocity — incredibly useful for detecting scientists attacking a bottleneck | [https://help.openalex.org/api/](https://help.openalex.org/api/?utm_source=chatgpt.com)                                                                                             |
| **PatentsView / USPTO** | patent acceleration around substitutes/new architectures                              | [https://www.uspto.gov/ip-policy/economic-research/patentsview](https://www.uspto.gov/ip-policy/economic-research/patentsview?utm_source=chatgpt.com)                               |
| **FRED**                | prices, industrial production, commodities and macro time series                      | [https://fred.stlouisfed.org/docs/api/fred/overview.html](https://fred.stlouisfed.org/docs/api/fred/overview.html?utm_source=chatgpt.com)                                         |
| **Wikidata SPARQL**     | entity resolution: companies, facilities, subsidiaries, countries, products           | [https://query.wikidata.org/](https://query.wikidata.org/?utm_source=chatgpt.com)                                                                                                   |
| **GDELT**               | machine-readable live world news/event stream                                         | [https://www.gdeltproject.org/](https://www.gdeltproject.org/?utm_source=chatgpt.com)                                                                                               |

The **OpenAlex + USPTO** combination is especially interesting because it gives us something normal supply-chain maps completely miss:

### probability that the bottleneck is about to be destroyed.

For every bottleneck node, track:

**papers about reducing requirement for X**
**papers about substitutes for X**
**patent acceleration**
**new architecture announcements**
**startup funding targeting X**
**benchmark improvements reducing X/unit of intelligence**

So while HBM's *current scarcity score* might increase, its *expected persistence* could simultaneously fall.

That is exactly your ChatGPT-8 scenario.

## 4. I think our graph should go deeper than ProphetMap

ProphetMap is primarily:

**sector/layer → ticker**

We want:

**AGI capability**
→ **technical requirement**
→ **system**
→ **process**
→ **component**
→ **material**
→ **equipment**
→ **factory**
→ **company**
→ **geography**
→ **stock**

For example:

**frontier inference**
→ memory bandwidth
→ HBM3E/HBM4
→ stacked DRAM
→ TSV
→ wafer thinning
→ TC/hybrid bonding
→ CoWoS
→ ABF substrate
→ ABF film
→ Ajinomoto
→ chemical/feedstock/equipment dependency...

And every node can itself recursively answer:

> **What constrains increasing the output of this node?**

That creates the graph automatically.

This is actually the simplest definition of our system:

$$
\boxed{
B(x)=\text{What prevents production of }x\text{ increasing?}
}
$$

Apply `B()` recursively.

For HBM:

**HBM**
→ DRAM wafer capacity
→ yields
→ TSV
→ bonding machines
→ packaging capacity
→ substrates
→ electricity
→ ultrapure water
→ specialized labor
→ fab equipment.

Then recursively:

**bonding machines**
→ precision stages
→ optics
→ encoders
→ motors
→ bearings
→ specialty materials...

And suddenly you hit exactly the obscure companies we've been finding.

## 5. The CHOKEPOINT idea gives us the quantitative breakthrough

The most interesting methodology I found outside ProphetMap may actually be this tiny **zero-star/low-star personal repo**:

[https://github.com/atharvahirulkar/chokepoint](https://github.com/atharvahirulkar/chokepoint?utm_source=chatgpt.com)

Instead of asking:

> "Which node looks important?"

it removes each vendor from the graph and calculates **coverage collapse**. It trains against those simulated failures and validates against historical disruptions. It reports a ~49,842-vendor universe in its defense dataset. ([GitHub][18])

We can generalize this beautifully.

For every node \(v\):

$$
Criticality(v)
=
AGIThroughput(G)-AGIThroughput(G-v)
$$

Then instead of simply saying **"HBM is important"**, we could estimate:

> Removing HBM capacity decreases available AI-compute throughput 63%.

And then:

> Increasing HBM capacity 50% only increases total throughput 17%, because CoWoS subsequently becomes binding.

**Boom. That's the next bottleneck.**

Then simulate:

+50% CoWoS.

Maybe substrates bind.

+50% substrates.

Power binds.

You're computationally walking the bottleneck frontier.

That is much better than a static research report.

---

## What I'd actually build

I wouldn't create another massive schema-heavy research platform. I'd combine the clever parts that already exist:

**ProphetMap**
→ thesis/falsification/scoring discipline

**Keystone + Silicon Stack + Memory Atlas**
→ initial dependency graph

**eugenehp/supplychain**
→ recursive upstream tracing pattern

**alphasig + SEC EDGAR**
→ continual evidence extraction

**Graphiti**
→ temporal edges

**NetworkX**
→ centrality/min-cut/removal simulations

**CHOKEPOINT**
→ counterfactual failure scoring

**River**
→ regime-change detection

**OpenAlex + PatentsView**
→ bottleneck-obsolescence score

**Qlib**
→ historical portfolio simulation.

I would keep the underlying storage boring initially: **Parquet + DuckDB + NetworkX**, not Neo4j. Only introduce a graph DB when queries actually demand it.

And the fundamental object doesn't need 200 fields. Something like:

```text
NODE
id
type
name

EDGE
source
target
relation
amount
capacity
utilization
lead_time
substitutability
valid_from
valid_to
confidence
source_url
```

Then derive everything else.

The important calculated quantities become:

$$
Scarcity =
\frac{DemandGrowth}{CapacityGrowth}
$$

$$
Fragility =
Utilization
\times Concentration
\times LeadTime
\times (1-Substitutability)
$$

and roughly:

$$
BottleneckAlpha =
\frac{
Scarcity \times Persistence \times Criticality
\times PricingPower \times MarketSurprise
}{
Valuation \times ObsolescenceRisk
}
```

But the really powerful output isn't merely the highest score.

It's:

> **Current bottleneck:** HBM
> **Likely next bottleneck if HBM supply expands:** CoWoS
> **Likely next:** ABF / bonding / power
> **Companies with greatest revenue sensitivity:** ...
> **Market awareness:** ...
> **Research attacking this constraint:** accelerating/decelerating
> **Probability constraint remains binding in 3/6/12/24 months:** ...

### The gap

After searching all of this, I **didn't find a project that combines all four**:

**physical AGI dependency graph + recursive bottleneck discovery + temporal/obsolescence detection + systematic equity reallocation.**

ProphetMap comes closest on the investing side. Keystone comes closest on rigorous industrial dependency mapping. CHOKEPOINT has the best quantitative bottleneck-identification mechanism. Graphiti solves temporal facts.

So I don't think we need to invent the primitives. **The novel project is connecting these four things.**

And I would absolutely clone **ProphetMap, Keystone, CHOKEPOINT, Chip Sense, Silicon Stack and Memory Atlas first** and compare their graph representations before writing ours. One caution: the repositories have different licenses—ProphetMap is MIT and Keystone AGPL-3.0, while `eugenehp/supplychain` is free for non-commercial use but requires permission for commercial deployment, and TWSE-KG is publicly visible but marked proprietary. ([GitHub][1])

This is considerably more developed in the wild than I expected. The striking part is that these independent builders have already converged on **“physical constraints,” “chokepoints,” “dependency graphs,” “falsification,” and even “bottleneck relay”** almost simultaneously. Our extension is making the relay itself the object being predicted.

[1]: https://github.com/Beltran12138/prophetmap "GitHub - Beltran12138/prophetmap: AI industry chain transmission map for US equity alpha discovery — 19-layer propagation model with automated daily scoring · GitHub"
[2]: https://github.com/Skeeter-spec/keystone "GitHub - Skeeter-spec/keystone: A living atlas of the world's industrial value chains, mapped to find the chokepoints. Educational research, not investment advice. · GitHub"
[3]: https://github.com/eugenehp/supplychain?utm_source=chatgpt.com "GitHub - eugenehp/supplychain · GitHub"
[4]: https://github.com/atharvahirulkar/chokepoint "GitHub - atharvahirulkar/chokepoint: Graph ML pipeline that scores defense procurement vendors by mission coverage collapse risk - find structural single points of failure in public contract data before disruption does. · GitHub"
[5]: https://github.com/aminalav/chip-sense "GitHub - aminalav/chip-sense: Open-source research board for the semiconductor supply chain — companies, fabs, cited relationship arcs, trade flows and illustrative stress scenarios. Next.js + MapLibre. · GitHub"
[6]: https://github.com/sflans99/silicon-stack?utm_source=chatgpt.com "GitHub - sflans99/silicon-stack: Interactive semiconductor supply chain visualizer — 239 companies, 1,110 relationships, React + D3 · GitHub"
[7]: https://github.com/upamanyuacharya/memory-atlas "GitHub - upamanyuacharya/memory-atlas: An interactive 3D map of the AI memory supply chain — HBM, CXL, photonics: who makes what, the bottlenecks, and who matters. Single-file Three.js. · GitHub"
[8]: https://github.com/YichengYang-Ethan/ai-supply-chain-research?utm_source=chatgpt.com "GitHub - YichengYang-Ethan/ai-supply-chain-research: Verified ten-sector research on the AI compute build-out, distilled from 311 public SemiAnalysis articles — with an independent credibility audit of the source (664 events, 119 tickers). · GitHub"
[9]: https://github.com/sushaan-k/alphasig?utm_source=chatgpt.com "GitHub - sushaan-k/alphasig: Causal signal extraction from SEC filings using LLMs. · GitHub"
[10]: https://github.com/tunglich/TWSE-KG?utm_source=chatgpt.com "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[11]: https://github.com/Timeverse/My-TW-Coverage "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[12]: https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com "GitHub - supat-roong/stock-relation: Interactive dashboard that maps corporate relationships by parsing financial data and SEC filings into a dynamic knowledge graph of similarity, ownership, and validation. ([GitHub][13])                                                                                 | [https://github.com/Jumade/sec-graph](https://github.com/Jumade/sec-graph?utm_source=chatgpt.com)                                                     |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |

There is also this smaller semiconductor chokepoint analysis project using NetworkX centrality:

[https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis](https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis?utm_source=chatgpt.com) ([GitHub][15])

### ProphetMap is the one to inspect first

Its conceptual model is remarkably close to ours:

**models → accelerators → EDA → semiconductor materials → equipment → packaging → substrates → HBM → servers → networking → power/cooling → optics → construction → power generation → nuclear fuel → grid → commodities → embodied AI.**

It then scores each ticker by physical constraint, whether the company actually captures the scarcity rent, AI revenue sensitivity, time-to-realization and whether the market has already priced it. Most importantly, it maintains **pre-declared falsifiers** and evaluates them daily. ([GitHub][1])

That last part is exactly what was missing from our discussion:

> HBM is the bottleneck — **until what observable event makes that statement false?**

ProphetMap already thinks this way.

Its live frontend is:

[https://prophetmap.vercel.app/](https://prophetmap.vercel.app/?utm_source=chatgpt.com)

Keystone's live industrial maps:

[https://skeeter-spec.github.io/keystone/](https://skeeter-spec.github.io/keystone/?utm_source=chatgpt.com) ([GitHub][2])

Memory Atlas:

[https://memory.upamanyuacharya.com/](https://memory.upamanyuacharya.com/?utm_source=chatgpt.com) ([The Memory Atlas][16])

## 2. Graph/math projects that give us the quantitative machinery

We shouldn't build our own graph science. These give us nearly everything.

| Tool           | What I'd use it for                                                                                                                          | Link                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **NetworkX**   | betweenness, PageRank, articulation nodes, centrality, shortest paths, min-cut/max-flow and simulated node removal                           | [https://github.com/networkx/networkx](https://github.com/networkx/networkx?utm_source=chatgpt.com)         |
| **Graphiti**   | **temporal knowledge graph** — crucial because dependencies become true/false through time rather than being permanent facts. ([GitHub][17]) | [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti?utm_source=chatgpt.com)             |
| **cuGraph**    | GPU-accelerated graph analysis once the graph gets enormous                                                                                  | [https://github.com/rapidsai/cugraph](https://github.com/rapidsai/cugraph?utm_source=chatgpt.com)           |
| **River**      | online ML + concept/drift detection: detect when a bottleneck regime changes                                                                 | [https://github.com/online-ml/river](https://github.com/online-ml/river?utm_source=chatgpt.com)             |
| **ruptures**   | historical change-point detection                                                                                                            | [https://github.com/deepcharles/ruptures](https://github.com/deepcharles/ruptures?utm_source=chatgpt.com)   |
| **Tigramite**  | causal discovery on time series rather than merely observing correlation                                                                     | [https://github.com/jakobrunge/tigramite](https://github.com/jakobrunge/tigramite?utm_source=chatgpt.com)   |
| **DoWhy**      | intervention/counterfactual analysis: “if HBM capacity rises 50%, what becomes binding?”                                                     | [https://github.com/py-why/dowhy](https://github.com/py-why/dowhy?utm_source=chatgpt.com)                   |
| **Qlib**       | convert bottleneck signals into an actual backtested dynamic portfolio                                                                       | [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib?utm_source=chatgpt.com)               |
| **OpenBB**     | market/fundamental data abstraction layer                                                                                                    | [https://github.com/OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB?utm_source=chatgpt.com) |
| **PyPSA**      | physically model the electricity/grid branch rather than relying on narratives                                                               | [https://github.com/PyPSA/PyPSA](https://github.com/PyPSA/PyPSA?utm_source=chatgpt.com)                     |
| **gridstatus** | live ISO electricity demand, generation and pricing                                                                                          | [https://github.com/gridstatus/gridstatus](https://github.com/gridstatus/gridstatus?utm_source=chatgpt.com) |
| **pymrio**     | global input-output dependency analysis                                                                                                      | [https://github.com/IndEcol/pymrio](https://github.com/IndEcol/pymrio?utm_source=chatgpt.com)               |
| **leontief**   | U.S. BEA input-output tables → direct + indirect dependency multipliers                                                                      | [https://github.com/andenick/leontief](https://github.com/andenick/leontief?utm_source=chatgpt.com)         |
[11]: https://github.com/Timeverse/My-TW-Coverage "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[12]: https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com "GitHub - supat-roong/stock-relation: Interactive dashboard that maps corporate relationships by parsing financial data and SEC filings into a dynamic knowledge graph of similarity, ownership, and validation. ([GitHub][13])                                                                                 | [https://github.com/Jumade/sec-graph](https://github.com/Jumade/sec-graph?utm_source=chatgpt.com)                                                     |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |

There is also this smaller semiconductor chokepoint analysis project using NetworkX centrality:

[https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis](https://github.com/navyawalia23-bit/Semiconductor-AI-Analysis?utm_source=chatgpt.com) ([GitHub][15])

### ProphetMap is the one to inspect first

Its conceptual model is remarkably close to ours:

**models → accelerators → EDA → semiconductor materials → equipment → packaging → substrates → HBM → servers → networking → power/cooling → optics → construction → power generation → nuclear fuel → grid → commodities → embodied AI.**

It then scores each ticker by physical constraint, whether the company actually captures the scarcity rent, AI revenue sensitivity, time-to-realization and whether the market has already priced it. Most importantly, it maintains **pre-declared falsifiers** and evaluates them daily. ([GitHub][1])

That last part is exactly what was missing from our discussion:

> HBM is the bottleneck — **until what observable event makes that statement false?**

ProphetMap already thinks this way.

Its live frontend is:

[https://prophetmap.vercel.app/](https://prophetmap.vercel.app/?utm_source=chatgpt.com)

Keystone's live industrial maps:

[https://skeeter-spec.github.io/keystone/](https://skeeter-spec.github.io/keystone/?utm_source=chatgpt.com) ([GitHub][2])

Memory Atlas:

[https://memory.upamanyuacharya.com/](https://memory.upamanyuacharya.com/?utm_source=chatgpt.com) ([The Memory Atlas][16])

## 2. Graph/math projects that give us the quantitative machinery

We shouldn't build our own graph science. These give us nearly everything.

| Tool           | What I'd use it for                                                                                                                          | Link                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **NetworkX**   | betweenness, PageRank, articulation nodes, centrality, shortest paths, min-cut/max-flow and simulated node removal                           | [https://github.com/networkx/networkx](https://github.com/networkx/networkx?utm_source=chatgpt.com)         |
| **Graphiti**   | **temporal knowledge graph** — crucial because dependencies become true/false through time rather than being permanent facts. ([GitHub][17]) | [https://github.com/getzep/graphiti](https://github.com/getzep/graphiti?utm_source=chatgpt.com)             |
| **cuGraph**    | GPU-accelerated graph analysis once the graph gets enormous                                                                                  | [https://github.com/rapidsai/cugraph](https://github.com/rapidsai/cugraph?utm_source=chatgpt.com)           |
| **River**      | online ML + concept/drift detection: detect when a bottleneck regime changes                                                                 | [https://github.com/online-ml/river](https://github.com/online-ml/river?utm_source=chatgpt.com)             |
| **ruptures**   | historical change-point detection                                                                                                            | [https://github.com/deepcharles/ruptures](https://github.com/deepcharles/ruptures?utm_source=chatgpt.com)   |
| **Tigramite**  | causal discovery on time series rather than merely observing correlation                                                                     | [https://github.com/jakobrunge/tigramite](https://github.com/jakobrunge/tigramite?utm_source=chatgpt.com)   |
| **DoWhy**      | intervention/counterfactual analysis: “if HBM capacity rises 50%, what becomes binding?”                                                     | [https://github.com/py-why/dowhy](https://github.com/py-why/dowhy?utm_source=chatgpt.com)                   |
| **Qlib**       | convert bottleneck signals into an actual backtested dynamic portfolio                                                                       | [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib?utm_source=chatgpt.com)               |
| **OpenBB**     | market/fundamental data abstraction layer                                                                                                    | [https://github.com/OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB?utm_source=chatgpt.com) |
| **PyPSA**      | physically model the electricity/grid branch rather than relying on narratives                                                               | [https://github.com/PyPSA/PyPSA](https://github.com/PyPSA/PyPSA?utm_source=chatgpt.com)                     |
| **gridstatus** | live ISO electricity demand, generation and pricing                                                                                          | [https://github.com/gridstatus/gridstatus](https://github.com/gridstatus/gridstatus?utm_source=chatgpt.com) |
| **pymrio**     | global input-output dependency analysis                                                                                                      | [https://github.com/IndEcol/pymrio](https://github.com/IndEcol/pymrio?utm_source=chatgpt.com)               |
| **leontief**   | U.S. BEA input-output tables → direct + indirect dependency multipliers                                                                      | [https://github.com/andenick/leontief](https://github.com/andenick/leontief?utm_source=chatgpt.com)         |
[11]: https://github.com/Timeverse/My-TW-Coverage "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[12]: https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com "GitHub - supat-roong/stock-relation: Interactive dashboard that maps corporate relationships by parsing financial data and SEC filings into a dynamic knowledge graph of similarity, ownership, and validation. ([GitHub][13])                                                                                 | [https://github.com/Jumade/sec-graph](https://github.com/Jumade/sec-graph?utm_source=chatgpt.com)                                                     |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |
[11]: https://github.com/Timeverse/My-TW-Coverage "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[12]: https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com "GitHub - supat-roong/stock-relation: Interactive dashboard that maps corporate relationships by parsing financial data and SEC filings into a dynamic knowledge graph of similarity, ownership, and validation. ([GitHub][13])                                                                                 | [https://github.com/Jumade/sec-graph](https://github.com/Jumade/sec-graph?utm_source=chatgpt.com)                                                     |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |
[11]: https://github.com/Timeverse/My-TW-Coverage "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[12]: https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com "GitHub - supat-roong/stock-relation: Interactive dashboard that maps corporate relationships by parsing financial data and SEC filings into a dynamic knowledge graph of similarity, ownership, and validation. ([GitHub][13])                                                                                 | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |
| **A**    | **DisruptIQ**                 | Live news → disruption classifier → Kafka → Neo4j → graph risk propagation. Small project, but the architecture is exactly what our live event layer needs. ([GitHub][14])                                              | [https://github.com/Sakshi3027/disruptiq](https://github.com/Sakshi3027/disruptiq?utm_source=chatgpt.com)                                             |
[11]: https://github.com/Timeverse/My-TW-Coverage "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Consent. ([GitHub][17]) |

## 3. Free raw data we can continuously feed it

This is where it becomes much more powerful than any of those individual projects.

| Dataset                 | What it tells us                                                                      | Full resource                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SEC EDGAR**           | supplier concentration, customers, capex, capacity, risks, contracts, backlog         | [https://www.sec.gov/about/developer-resources](https://www.sec.gov/about/developer-resources?utm_source=chatgpt.com)                                                               |
| **UN Comtrade**         | who actually exports/imports a material/component and geographic concentration        | [https://uncomtrade.org/docs/un-comtrade-api/](https://uncomtrade.org/docs/un-comtrade-api/?utm_source=chatgpt.com)                                                               |
| **BEA Input-Output**    | U.S. industry → industry dependencies                                                 | [https://www.bea.gov/data/industries/input-output-accounts-data](https://www.bea.gov/data/industries/input-output-accounts-data?utm_source=chatgpt.com)                             |
| **BEA API**             | automate the above                                                                    | [https://apps.bea.gov/api/signup/](https://apps.bea.gov/api/signup/?utm_source=chatgpt.com)                                                                                         |
| **OECD ICIO**           | global inter-country input/output dependencies                                        | [https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html](https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html?utm_source=chatgpt.com) |
| **EXIOBASE**            | extremely detailed global multi-regional production network                           | [https://exiobase.eu/](https://exiobase.eu/?utm_source=chatgpt.com)                                                                                                                 |
| **USGS Minerals**       | production/concentration/reserves for gallium, uranium, copper, rare earths etc.      | [https://www.usgs.gov/centers/national-minerals-information-center/tools](https://www.usgs.gov/centers/national-minerals-information-center/tools?utm_source=chatgpt.com)           |
| **EIA API**             | power generation, capacity, demand and grid flows                                     | [https://www.eia.gov/opendata/](https://www.eia.gov/opendata/?utm_source=chatgpt.com)                                                                                               |
| **OpenAlex**            | research velocity — incredibly useful for detecting scientists attacking a bottleneck | [https://help.openalex.org/api/](https://help.openalex.org/api/?utm_source=chatgpt.com)                                                                                             |
| **PatentsView / USPTO** | patent acceleration around substitutes/new architectures                              | [https://www.uspto.gov/ip-policy/economic-research/patentsview](https://www.uspto.gov/ip-policy/economic-research/patentsview?utm_source=chatgpt.com)                               |
| **FRED**                | prices, industrial production, commodities and macro time series                      | [https://fred.stlouisfed.org/docs/api/fred/overview.html](https://fred.stlouisfed.org/docs/api/fred/overview.html?utm_source=chatgpt.com)                                         |
| **Wikidata SPARQL**     | entity resolution: companies, facilities, subsidiaries, countries, products           | [https://query.wikidata.org/](https://query.wikidata.org/?utm_source=chatgpt.com)                                                                                                   |
| **GDELT**               | machine-readable live world news/event stream                                         | [https://www.gdeltproject.org/](https://www.gdeltproject.org/?utm_source=chatgpt.com)                                                                                               |

The **OpenAlex + USPTO** combination is especially interesting because it gives us something normal supply-chain maps completely miss:

### probability that the bottleneck is about to be destroyed.

For every bottleneck node, track:

**papers about reducing requirement for X**
**papers about substitutes for X**
**patent acceleration**
**new architecture announcements**
**startup funding targeting X**
**benchmark improvements reducing X/unit of intelligence**

So while HBM's *current scarcity score* might increase, its *expected persistence* could simultaneously fall.

That is exactly your ChatGPT-8 scenario.

## 4. I think our graph should go deeper than ProphetMap

ProphetMap is primarily:

**sector/layer → ticker**

We want:

**AGI capability**
→ **technical requirement**
→ **system**
→ **process**
→ **component**
→ **material**
→ **equipment**
→ **factory**
→ **company**
→ **geography**
→ **stock**

For example:

**frontier inference**
→ memory bandwidth
→ HBM3E/HBM4
→ stacked DRAM
→ TSV
→ wafer thinning
→ TC/hybrid bonding
→ CoWoS
→ ABF substrate
→ ABF film
→ Ajinomoto
→ chemical/feedstock/equipment dependency...

And every node can itself recursively answer:

> **What constrains increasing the output of this node?**

That creates the graph automatically.

This is actually the simplest definition of our system:

$$
\boxed{
B(x)=\text{What prevents production of }x\text{ increasing?}
}
$$

Apply `B()` recursively.

For HBM:

**HBM**
→ DRAM wafer capacity
→ yields
→ TSV
→ bonding machines
→ packaging capacity
→ substrates
→ electricity
→ ultrapure water
→ specialized labor
→ fab equipment.

Then recursively:

**bonding machines**
→ precision stages
→ optics
→ encoders
→ motors
→ bearings
→ specialty materials...

And suddenly you hit exactly the obscure companies we've been finding.

## 5. The CHOKEPOINT idea gives us the quantitative breakthrough

The most interesting methodology I found outside ProphetMap may actually be this tiny **zero-star/low-star personal repo**:

[https://github.com/atharvahirulkar/chokepoint](https://github.com/atharvahirulkar/chokepoint?utm_source=chatgpt.com)

Instead of asking:

> "Which node looks important?"

it removes each vendor from the graph and calculates **coverage collapse**. It trains against those simulated failures and validates against historical disruptions. It reports a ~49,842-vendor universe in its defense dataset. ([GitHub][18])

We can generalize this beautifully.

For every node \(v\):

$$
Criticality(v)
=
AGIThroughput(G)-AGIThroughput(G-v)
$$

Then instead of simply saying **"HBM is important"**, we could estimate:

> Removing HBM capacity decreases available AI-compute throughput 63%.

And then:

> Increasing HBM capacity 50% only increases total throughput 17%, because CoWoS subsequently becomes binding.

**Boom. That's the next bottleneck.**

Then simulate:

+50% CoWoS.

Maybe substrates bind.

+50% substrates.

Power binds.

You're computationally walking the bottleneck frontier.

That is much better than a static research report.

---

## What I'd actually build

I wouldn't create another massive schema-heavy research platform. I'd combine the clever parts that already exist:

**ProphetMap**
→ thesis/falsification/scoring discipline

**Keystone + Silicon Stack + Memory Atlas**
→ initial dependency graph

**eugenehp/supplychain**
→ recursive upstream tracing pattern

**alphasig + SEC EDGAR**
→ continual evidence extraction

**Graphiti**
→ temporal edges

**NetworkX**
→ centrality/min-cut/removal simulations

**CHOKEPOINT**
→ counterfactual failure scoring

**River**
→ regime-change detection

**OpenAlex + PatentsView**
→ bottleneck-obsolescence score

**Qlib**
→ historical portfolio simulation.

I would keep the underlying storage boring initially: **Parquet + DuckDB + NetworkX**, not Neo4j. Only introduce a graph DB when queries actually demand it.

And the fundamental object doesn't need 200 fields. Something like:

```text
NODE
id
type
name

EDGE
source
target
relation
amount
capacity
utilization
lead_time
substitutability
valid_from
valid_to
confidence
source_url
```

Then derive everything else.

The important calculated quantities become:

$$
Scarcity =
\frac{DemandGrowth}{CapacityGrowth}
$$

$$
Fragility =
Utilization
\times Concentration
\times LeadTime
\times (1-Substitutability)
$$

and roughly:

$$
BottleneckAlpha =
\frac{
Scarcity \times Persistence \times Criticality
\times PricingPower \times MarketSurprise
}{
Valuation \times ObsolescenceRisk
}
```

But the really powerful output isn't merely the highest score.

It's:

> **Current bottleneck:** HBM
> **Likely next bottleneck if HBM supply expands:** CoWoS
> **Likely next:** ABF / bonding / power
> **Companies with greatest revenue sensitivity:** ...
> **Market awareness:** ...
> **Research attacking this constraint:** accelerating/decelerating
> **Probability constraint remains binding in 3/6/12/24 months:** ...

### The gap

After searching all of this, I **didn't find a project that combines all four**:

**physical AGI dependency graph + recursive bottleneck discovery + temporal/obsolescence detection + systematic equity reallocation.**

ProphetMap comes closest on the investing side. Keystone comes closest on rigorous industrial dependency mapping. CHOKEPOINT has the best quantitative bottleneck-identification mechanism. Graphiti solves temporal facts.

So I don't think we need to invent the primitives. **The novel project is connecting these four things.**

And I would absolutely clone **ProphetMap, Keystone, CHOKEPOINT, Chip Sense, Silicon Stack and Memory Atlas first** and compare their graph representations before writing ours. One caution: the repositories have different licenses—ProphetMap is MIT and Keystone AGPL-3.0, while `eugenehp/supplychain` is free for non-commercial use but requires permission for commercial deployment, and TWSE-KG is publicly visible but marked proprietary. ([GitHub][1])

This is considerably more developed in the wild than I expected. The striking part is that these independent builders have already converged on **“physical constraints,” “chokepoints,” “dependency graphs,” “falsification,” and even “bottleneck relay”** almost simultaneously. Our extension is making the relay itself the object being predicted.

[1]: https://github.com/Beltran12138/prophetmap "GitHub - Beltran12138/prophetmap: AI industry chain transmission map for US equity alpha discovery — 19-layer propagation model with automated daily scoring · GitHub"
[2]: https://github.com/Skeeter-spec/keystone "GitHub - Skeeter-spec/keystone: A living atlas of the world's industrial value chains, mapped to find the chokepoints. Educational research, not investment advice. · GitHub"
[3]: https://github.com/eugenehp/supplychain?utm_source=chatgpt.com "GitHub - eugenehp/supplychain · GitHub"
[4]: https://github.com/atharvahirulkar/chokepoint "GitHub - atharvahirulkar/chokepoint: Graph ML pipeline that scores defense procurement vendors by mission coverage collapse risk - find structural single points of failure in public contract data before disruption does. · GitHub"
[5]: https://github.com/aminalav/chip-sense "GitHub - aminalav/chip-sense: Open-source research board for the semiconductor supply chain — companies, fabs, cited relationship arcs, trade flows and illustrative stress scenarios. Next.js + MapLibre. · GitHub"
[6]: https://github.com/sflans99/silicon-stack?utm_source=chatgpt.com "GitHub - sflans99/silicon-stack: Interactive semiconductor supply chain visualizer — 239 companies, 1,110 relationships, React + D3 · GitHub"
[7]: https://github.com/upamanyuacharya/memory-atlas "GitHub - upamanyuacharya/memory-atlas: An interactive 3D map of the AI memory supply chain — HBM, CXL, photonics: who makes what, the bottlenecks, and who matters. Single-file Three.js. · GitHub"
[12]: https://github.com/supat-roong/stock-relation?utm_source=chatgpt.com "GitHub - supat-roong/stock-relation: Interactive dashboard that maps corporate relationships by parsing financial data and SEC filings into a dynamic knowledge graph of similarity, ownership, and validation. ([GitHub][13])                                                                                 | [https://github.com/Jumade/sec-graph](https://github.com/Jumade/sec-graph?utm_source=chatgpt.com)                                                     |
[13]: https://github.com/Jumade/sec-graph "GitHub - Jumade/sec-graph: GraphRAG platform for SEC financial filings — ingests 10-K/10-Q/8-K, extracts entities and relationships with LLMs, and answers complex financial intelligence questions by combining Neo4j graph traversal with Qdrant vector search. · GitHub"
[14]: https://github.com/Sakshi3027/disruptiq "GitHub - Sakshi3027/disruptiq: GraphRAG platform for SEC financial filings — ingests 10-K/10-Q/8-K, extracts entities and relationships with LLMs, and answers complex financial intelligence questions by combining Neo4j graph traversal with Qdrant vector search. · GitHub"
[9]: https://github.com/sushaan-k/alphasig?utm_source=chatgpt.com "GitHub - sushaan-k/alphasig: Causal signal extraction from SEC filings using LLMs. · GitHub"
[10]: https://github.com/tunglich/TWSE-KG?utm_source=chatgpt.com "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[8]: https://github.com/YichengYang-Ethan/ai-supply-chain-research?utm_source=chatgpt.com "GitHub - YichengYang-Ethan/ai-supply-chain-research: Verified ten-sector research on the AI compute build-out, distilled from 311 public SemiAnalysis articles — with an independent credibility audit of the source (664 events, 119 tickers). · GitHub"
[9]: https://github.com/sushaan-k/alphasig?utm_source=chatgpt.com "GitHub - sushaan-k/alphasig: Causal signal extraction from SEC filings using LLMs. · GitHub"
[10]: https://github.com/tunglich/TWSE-KG?utm_source=chatgpt.com "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[8]: https://github.com/YichengYang-Ethan/ai-supply-chain-research?utm_source=chatgpt.com "GitHub - YichengYang-Ethan/ai-supply-chain-research: Verified ten-sector research on the AI compute build-out, distilled from 311 public SemiAnalysis articles — with an independent credibility audit of the source (664 events, 119 tickers). · GitHub"
[9]: https://github.com/sushaan-k/alphasig?utm_source=chatgpt.com "GitHub - sushaan-k/alphasig: Causal signal extraction from SEC filings using LLMs. · GitHub"
[10]: https://github.com/tunglich/TWSE-KG?utm_source=chatgpt.com "GitHub - TWSE-KG: Empirical Knowledge Graph Propagation Experiments for Taiwan Stock Supply Chain Sentiment Scoring · GitHub"
[8]: https://github.com/YichengYang-Ethan/ai-supply-chain-research?utm_source=chatgpt.com "GitHub - YichengYang-Ethan/ai-supply-chain-research: Verified ten-sector research on the AI compute build-out, distilled from 311 public SemiAnalysis articles — with an independent credibility audit of the source (664 events, 119 tickers). · GitHub"
