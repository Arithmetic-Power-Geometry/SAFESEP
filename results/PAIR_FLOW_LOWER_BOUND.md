# Authorization Pair-Flow Lower-Bound Attack — Tests 123–138

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Result
For a decision-critical branch C define incompatible-pair mass M(C). For a branchwise-legitimate informative action e define Delta_e(C)=M(C)-max_o M(C_{e,o}). The static local counting certificate gives a restricted-model lower-bound candidate when its capacity ceiling remains valid along the path. It is not claimed as a general dynamic SAFESEP theorem.

## CI-discovered correction to the cheapest-experiment diagnostic
The first version hard-coded q as the cheapest unresolved experiment. GitHub CI correctly falsified that claim. In this balanced-family battery, bit0 has the same unit cost as q but leaves fewer incompatible pairs, and the diagnostic tie-breaks by (cost,name,worst residual). At 200 worlds the actual selected experiment is bit0, cost 1, leaving 2,500 incompatible pairs; q still costs 1 but leaves 9,900. At 10,000 worlds bit0 leaves 6,250,000 incompatible pairs, while q leaves 24,995,000. This correction is permanent and demonstrates why the cheapest experiment must be recomputed rather than assumed from earlier witness families.

## Battery
Tests 123–138 cover zero mass, exact pair counting, actual cheapest unresolved experiment, exact q capacity, illegitimate-action filtering, no-op filtering, perfect resolver, infinite obstruction, partition monotonicity, parameter sweeps, representation/action-order invariance, cost scaling, and 10,000-world stress.

## Prior-art attack
This is not promoted to breakthrough novelty. Pair counting/cut/cover lower bounds have close relatives in test cover, diagnosis, decision-region determination and planning heuristics. Trust negotiation already studies selective/incremental protected disclosure, minimal credential disclosure, and minimum-cost credential exchange. Therefore the generic counting inequality is supporting machinery, not the novelty claim.

## Important limitation found
A root-only bound using max pair reduction is not automatically valid for arbitrary dynamic SAFESEP because an authority-changing action can unlock a later action with larger pair-separation capacity. A valid general theorem must be pathwise/state-dependent, e.g. a potential Phi(C,A) whose decrease per legitimate transition is globally bounded, or a cut over the reachable joint-state graph.

## Real-data boundary
No audited public benchmark supplies the counterfactual world×experiment legitimacy plus authority-transition semantics required for SAFESEP ground truth. The 10,000-world table is controlled theorem stress data, not production telemetry. Real authorization data remain an external-validity/coverage layer until a defensible adapter exists.

## Decision
Do not write the paper yet. Next attack: construct a state-dependent potential/cut certificate that remains sound when token-only authority transitions unlock future high-capacity experiments, compare it with exact joint-state search on exhaustive small instances, and retain every counterexample.
