# Common Legitimate Evidence (CLE) obstruction — Tests 91–94

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Definition
For a decision-critical compatible branch C, define

CLE(C) = min { c(e) : e is informative on C and e is legitimate in every w in C },

with CLE(C)=infinity when the set is empty.

CLE is a branchwise diagnostic/lower-bound object. It is not asserted to be a new planning primitive.

## Matched witness
A and B use the same 2n worlds, R/W decisions, and root probe q. q costs 1 and isolates r0. At n=100 its unresolved rest branch contains 9,900 incompatible pairs. At n=5,000 (10,000 worlds) it contains 24,995,000.

After q=rest, A has a common cost-2 resolver legitimate in every residual world, hence CLE_A=2. B gives every residual world an individually legitimate cost-2 resolver, but there is no single resolver legitimate throughout the branch, hence CLE_B=infinity.

This formalizes the quantifier gap: (for every world there exists a legitimate resolver) does not imply (there exists one resolver legitimate for every still-compatible world).

## Prior-art attack
This result is useful but not yet a breakthrough. Conformant/belief-state planning already requires an action to be applicable across all possible states in the current belief state, and conformant plans must succeed for every possible initial state. Thus the universal-applicability core of CLE is representable in established planning semantics. Test-cover/decision-region methods also optimize informative tests, while authorization/trust-negotiation systems constrain which evidence actions are available.

The potentially authorization-specific research target is therefore not CLE itself, but a theorem about the *extra cost or impossibility induced by legitimacy constraints* relative to an unconstrained decision tree, under a restricted authorization model where the bound cannot be dismissed as ordinary action applicability.

## Empirical boundary
`data/common_legitimate_evidence.csv` is controlled theorem stress data, not production authorization telemetry. Existing real authorization benchmarks do not provide the counterfactual world-by-experiment legitimacy matrix required to measure CLE without inventing labels. We therefore do not fabricate a real-data CLE score.

## Decision
Do not stop for the paper yet. Next attack: prove an authorization-specific legitimacy premium/lower bound family, ideally unbounded or infinite while ordinary information cost remains constant, and compare it directly with conformant planning and cost-sensitive trust negotiation.
