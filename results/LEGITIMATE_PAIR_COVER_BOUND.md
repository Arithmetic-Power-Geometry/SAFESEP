# Legitimate Incompatible-Pair Cover Bound — Tests 103–106

## Result
For a decision-critical branch C, let P(C) be its incompatible decision pairs. For each experiment e that is legitimate in every world of C, let Sep(e,C) be the incompatible pairs separated by e's outcome partition.

If no branchwise-legitimate experiment has nonempty Sep(e,C), then C is an immediate SAFESEP obstruction. This certificate is representation-independent in the limited but useful sense that it depends only on the semantic world/decision/outcome/legitimacy incidence relation, not on a particular belief-state data structure.

A coarse cost lower bound is

    LB(C) = ceil(|P(C)| / max_e |Sep(e,C)|) * min_e c(e),

where e ranges over currently branchwise-legitimate pair-separating experiments. This is only a lower bound; it is not claimed to equal optimal SAFESEP cost because adaptive overlap and future authority changes matter.

## Matched witness
A and B have identical worlds, decisions, experiment names/costs, and raw outcome partitions. q costs 1 and isolates r0. The resolver has the same perfect R/W partition and cost 1 in both systems. Only legitimacy differs. On q=rest, A retains a branchwise-legitimate resolver; B does not. Thus the semantic pair-cover certificate is finite/non-obstructed in A and infinite/obstructed in B.

The cheapest informative experiment that still leaves mutually incompatible worlds is q, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000 controlled worlds.

## Prior-art attack
This direction is not yet a breakthrough theorem. Set-cover/minimal-cover reductions are established in RBAC and access-control policy optimization, and access-control test selection has also been reduced to set cover. Therefore generic pair/set covering, NP-hardness from cover, or a cover lower bound cannot be claimed as new. The surviving SAFESEP-specific content is the legitimacy-filtered, branch-relative semantic obstruction and its interaction with future authority transitions.

The next theorem must exploit that dynamic interaction: a lower bound/certificate that remains sound when token-only authority transitions and adaptive observations can change which experiments become legitimate. A static cover at the current branch is insufficient for that claim.

## Data boundary
`data/legitimate_pair_cover_bound.csv` is controlled theorem stress data, not production authorization telemetry. Existing real authorization datasets do not provide the required counterfactual world×experiment legitimacy relation, so no such labels are fabricated.

## Decision
Retain as a useful certificate and negative prior-art boundary. Do not stop novelty search yet.
