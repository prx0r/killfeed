# Architecture

```text
SOURCE STREAMS
  equity/options | Polymarket/Kalshi | calibrated experts
  GitHub/HF | benchmarks | papers | patents | filings
  government | trade | power | minerals | jobs
        |
        v
NORMALIZE EVENTS
        v
ENTITY RESOLUTION + CLAIM EXTRACTION
        v
INFORMATION-LINEAGE DEDUP
        v
EVIDENCE / SOURCE CALIBRATION
        v
TEMPORAL BELIEF GRAPH
        | updates edge probabilities
        v
PHYSICAL + LEGAL DEPENDENCY GRAPH
        v
COUNTERFACTUAL PROPAGATION
    /                         \
EMERGING BOTTLENECK        DISSOLUTION
    \                         /
      SECURITY EXPOSURE GRAPH
               v
        ACTION GATES / SIZING
```

## Recursive operators
`CONSTRAIN(x)`: if upstream intelligence became free, what still prevents arbitrary production of x?

`DESTROY(x)`: what demonstrated/plausible AI-enabled development would make x unnecessary, substitutable, abundant or nearly free?

## Non-technical constraints are first class
Track physical resources/processes, minimum elapsed time, patents/FTO, licensing, regulation, certification, sites/land, grid interconnection, export controls, trust/provenance. AGI can eliminate a technical edge and reveal one of these as the next binding edge.
