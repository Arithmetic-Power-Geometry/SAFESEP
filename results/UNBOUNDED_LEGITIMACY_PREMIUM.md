# Unbounded Authorization-Legitimacy Premium — Tests 95–98

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Result
For each n>=2 construct 2n compatible worlds, n requiring R and n requiring W. The permanent diagnostic q has cost 1, isolates r0, and leaves (n-1)n decision-incompatible pairs on its residual branch.

Let U_n be the minimum decision-resolution cost if authorization legitimacy is ignored. A perfect resolver gives U_n=1.

In the controlled legitimate construction, the safe resolver requires n independent authority tokens alpha_0,...,alpha_{n-1}. Each token has a legitimate acquisition action of cost 1 and the final resolver costs 1. Therefore

S_n = n+1,
Lambda_n = S_n-U_n = n.

Thus the authorization-legitimacy premium is unbounded in this family while unconstrained information-resolution cost stays constant.

At n=5000 (10,000 worlds), q still costs 1 and leaves 24,995,000 incompatible pairs; U=1, S=5001, Lambda=5000.

## Prior-art attack
This exact construction is **not promoted as breakthrough novelty**. Conformant planning already searches belief space and requires actions/plans to be applicable across all possible states. Cost-sensitive automated trust negotiation already assigns costs to credentials/policies and optimizes successful disclosure sequences; published Minimum Sensitivity Cost formulations can be NP-complete. Therefore the broad statement that authorization/disclosure constraints can make a successful plan arbitrarily more expensive is not, by itself, a new foundational result.

What survives is a target for a stronger theorem: prove an unbounded gap under matched ordinary planning/disclosure cost structure where the growth is caused specifically by SAFESEP's decision-critical branchwise authorization condition rather than by simply inserting n mandatory token-acquisition actions.

## Empirical boundary
`data/unbounded_legitimacy_premium.csv` is controlled theorem stress data, not production authorization telemetry. Existing real authorization datasets audited in this repository do not provide counterfactual world-by-action legitimacy and token-acquisition semantics needed to instantiate Lambda without assumptions. We do not fabricate those labels.

## Decision
Do not stop for paper yet. Tests 95–98 establish the quantitative shape and a reproducible 10,000-world stress test, but the current linear lower bound is construction-driven and collides with generic cost-sensitive planning/trust-negotiation intuition. Next: matched-cost irreducibility—same action costs, same per-world acquisition lengths, same token counts, same ordinary planner optimum, but branchwise legitimacy alone forces growing SAFESEP cost or infinity.
