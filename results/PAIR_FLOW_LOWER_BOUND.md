# Authorization Pair-Flow Lower-Bound Attack — Tests 123–138

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Result
For a decision-critical branch C define incompatible-pair mass M(C). For a branchwise-legitimate informative action e define its worst-branch pair reduction

Delta_e(C) = M(C) - max_o M(C_{e,o}).

If every legitimate progress action available at C has worst-branch reduction at most delta>0, the static local counting certificate gives ceil(M(C)/delta) unit-cost progress steps as a lower bound under the restricted model in which the same capacity ceiling remains applicable along the relevant path. If no legitimate progress action exists, the branch is immediately obstructed. The implementation intentionally labels this a lower-bound attack rather than a final theorem for arbitrary dynamic SAFESEP systems; future authority-changing transitions can invalidate a root-only capacity ceiling.

## Permanent diagnostic
The cheapest informative experiment that still leaves incompatible worlds remains q, cost 1. At 200 worlds q leaves 9,900 incompatible pairs. At 10,000 controlled worlds it leaves 24,995,000. Root pair mass at 10,000 is 25,000,000 and q removes 5,000 pairs in its worst branch.

## Battery
Tests 123–138 cover zero mass, exact pair counting, cheapest unresolved q, exact q capacity, illegitimate-action filtering, no-op filtering, perfect resolver, infinite obstruction, partition monotonicity, parameter sweeps, representation/action-order invariance, cost scaling, and 10,000-world stress.

## Prior-art attack
This is not promoted to breakthrough novelty. Pair counting/cut/cover lower bounds have close relatives in test cover, diagnosis, decision-region determination and planning heuristics. Contingent planning already defines action applicability over every state in a belief state, and trust negotiation already studies incremental protected credential disclosure and minimum disclosure/cost. Therefore the generic counting inequality is supporting machinery, not the novelty claim.

## Important limitation found
A root-only bound using max pair reduction is not automatically valid for arbitrary dynamic SAFESEP because an authority-changing action can unlock a later action with larger pair-separation capacity. A valid general theorem must be pathwise/state-dependent, e.g. a potential Phi(C,A) whose decrease per legitimate transition is globally bounded, or a cut over the reachable joint state graph. This limitation is scientifically significant and is retained rather than hidden.

## Real-data boundary
No public benchmark currently audited in SAFESEP supplies counterfactual world×experiment legitimacy plus authority-transition semantics needed to interpret this pair-flow quantity as empirical ground truth. The 10,000-world table is therefore controlled theorem stress data, not production telemetry. Real authorization data remain an external-validity/coverage layer until a defensible adapter exists.

## Decision
Do not write the paper yet. Next attack: construct a state-dependent potential/cut certificate that remains sound when token-only authority transitions unlock future high-capacity experiments, then compare it directly with exact joint-state search on exhaustive small instances and randomized adversarial systems.
