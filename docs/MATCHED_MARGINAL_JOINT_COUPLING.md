# Matched-Marginal Joint Information-Authority Coupling

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Result
For every n>=2 construct A_n and B_n on 2n worlds with the same decisions, experiment q, q cost, q outcome partition, branch-size multiset, token multiset, resolver multiset, authority-edge count, and cheapest-unresolved-experiment statistics.

q isolates r0 and leaves the residual branch {r1,...,r(n-1),w0,...,w(n-1)} decision-critical. Therefore in both systems the cheapest informative experiment that still leaves mutually incompatible possible worlds is q with cost 1. The residual branch contains n(n-1) incompatible R/W pairs.

The systems differ only in alignment. In A, q(rest) yields alpha and alpha authorizes resolve_rest. In B, q(rest) yields beta while beta authorizes resolve_special. The separate information and authority marginals are unchanged, but A resolves the residual branch and B does not under the available resolver mapping.

Thus the tested summaries satisfy

    M_info(A_n)=M_info(B_n)
    M_auth(A_n)=M_auth(B_n)

while the joint outcome-authority alignment changes resolvability.

## What this proves
It proves only that the explicitly tested separate marginals do not determine resolvability. It does NOT prove that existing planning or authorization formalisms cannot encode the joint relation.

## Prior-art attack
Authorization/trust systems already gather evidence dynamically and can follow authorization-register or credential chains. Contingent planners can encode a combined state containing both belief and authority variables. Therefore the representation of joint coupling is not by itself a novelty claim.

The remaining research question is whether the coupling yields a nontrivial structural invariant, irreducibility theorem, or complexity consequence that is not inherited from generic combined-state contingent planning or recursive trust management.

## Empirical boundary
The 200- and 10,000-world instances are controlled structural benchmarks. Real benchmarks such as AuthBench provide permission/execution observations but not the counterfactual outcome-to-authority alignment required for this theorem. Missing labels are not fabricated.

## Permanent tests
33. Same cheapest unresolved experiment q, cost 1, same residual ambiguity.
34. Separate information and authority marginals match exactly under the implemented summaries.
35. Joint alignment alone changes residual resolvability.
36. Same result at 10,000 explicit worlds; residual incompatible-pair count 24,995,000.
