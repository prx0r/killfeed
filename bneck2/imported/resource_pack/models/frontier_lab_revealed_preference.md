# Frontier-lab revealed preference

Frontier model developers have private information about real model limits, serving bottlenecks, failure modes and expected future workloads. Their irreversible capital allocation is therefore a valuable signal.

## Do not interpret every purchase as a forecast
A lab can buy capacity because it expects demand, wants redundancy, wants negotiating leverage, hedges against architecture uncertainty, or simply needs near-term supply. The most informative signal is **specific + large + long-lived + hard to reverse + technically narrow**.

## Suggested event score

```text
LabCapitalSignal =
    log1p(commitment_usd)
  * irreversibility
  * technical_specificity
  * frontier_relevance
  * years_of_commitment
  * counterparty_purity
  * novelty_vs_previous_allocation
```

## Highest-value event types
1. custom chip / tape-out / architecture co-design
2. multi-generation capacity reservation
3. long-duration PPA, nuclear agreement, data-center site or grid commitment
4. strategic supplier investment/equity alignment
5. acquisition of narrow infrastructure/IP/tooling
6. hiring cluster in a previously small technical domain
7. supplier disclosure that reveals a large unnamed frontier customer

## Interpretation example
If OpenAI simultaneously commits to NVIDIA, AMD, Trainium, Cerebras and custom Broadcom silicon, do not conclude all five win. Conclude that **accelerator architecture is contested and OpenAI values optionality across latency, throughput, memory and power profiles**. The graph should lower confidence in any assumption that a single incumbent architecture is structurally unavoidable.

## Supplier-side triangulation
Private labs often disclose less than public suppliers. Monitor suppliers for:
- customer concentration
- purchase commitments
- capex specifically justified by AI customers
- book-to-bill/backlog
- lead times
- capacity reservations
- warrants/equity issued to customers
- long-term agreements
- risk-factor wording changes

Cross-reference supplier language against lab announcements before updating a graph edge.
