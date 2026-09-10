# Scoring model

## Physical bottleneck
`ScarcityPressure = demand_growth / max(capacity_growth, epsilon)`

`Fragility = utilization * concentration * normalized_lead_time * (1 - substitutability)`

`BottleneckScore = ScarcityPressure * Fragility`

Do not fabricate missing inputs. Missing observations carry a prior with explicit uncertainty.

## Frontier-lab revealed preference
`LabCapitalSignal = log1p(commitment_usd) * irreversibility * specificity * frontier_relevance * lead_time`

High-irreversibility signals: custom chip tape-out, multi-generation silicon partnership, GW-scale power/data-center commitment, multi-year capacity reservation, strategic supplier equity alignment, narrow capability acquisition.

## Dissolution / kill
Keep self-dug and architectural kills separate.

`SelfDugKill = capacity_overshoot + spot_price_break + inventory_build + order_cancellations + demand_miss`

`ArchitecturalKill = substitution_proof * workload_relevance * deployability * cost_advantage * dependency_reduction`

Use historical base rates: self-dug supply/demand collapses should carry a higher prior than exotic architecture kills until evidence changes it.

## Jevons correction
`NetDependencyChange = requirement_per_unit_change * total_output_change`

Efficiency can increase total resource demand if output grows faster.

## Consensus gap
Maintain `P_hard`, `P_expert`, `P_PM`, `P_equity`. The high-value state is often `P_hard >> P_equity`, especially for a crowded bottleneck whose terminal value assumes persistence.
