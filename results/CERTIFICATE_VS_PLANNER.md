# Dynamic Authorization Cut vs Full Joint-State Planning

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Permanent diagnostic
For the matched witness the cheapest currently executable informative experiment that still leaves mutually incompatible authorization worlds is q, cost 1. It leaves n(n-1) incompatible pairs: 9,900 at 200 worlds and 24,995,000 at 10,000 worlds.

## CI-discovered correction
The first implementation of the dynamic-cut `mandatory_cut` predicate was too strong: it required every incompatible root pair to be separable only by a cut probe. That is not necessary for a mandatory action cut, because non-cut probes may resolve some branches while every complete policy still requires the cut on another branch. CI correctly rejected Tests 49-52. The implementation was corrected to an exact restricted AND/OR check: removing the cut must destroy every complete resolving policy.

This failure is preserved as a scientific correction rather than hidden.

## Certificate
For cut K, the implemented sufficient certificate checks:
1. no complete resolving policy exists after removing K; and
2. no action in K is executable in any decision-critical joint state reachable without K.

Then a resolving policy would require a first use of K, but no such first use is authorized.

## Planner comparison
An independent full joint-state search is instrumented in `certificate_pruning.py`. Tests compare the certificate with full search across the parameterized family. The certificate is a sound precheck on these witnesses, but the current mandatory-cut check itself invokes restricted AND/OR reasoning. Therefore we do **not** claim an asymptotic complexity advantage.

## Prior-art attack
Strong planning under partial observability already uses AND/OR belief-space search. Contingent-planning work also studies unavoidable deadends, and landmark heuristics identify actions/facts that must occur in successful plans. Hence mandatory-cut/deadend reasoning is established at the generic planning level. The present authorization interpretation is useful, but without a cheaper authorization-specific certificate or a new complexity separation it is not yet breakthrough novelty.

## Empirical boundary
`data/certificate_planner_comparison.csv` scales the controlled structural benchmark through 10,000 worlds. It is synthetic theorem data, not production authorization telemetry. Real authorization corpora do not currently provide the counterfactual world-by-probe outcome and legitimate-executability labels required for this theorem; these labels are not fabricated.

## Decision
Do not stop for paper yet. Next target: seek a certificate computable from an authorization dependency graph (without belief-space AND/OR search), prove soundness, then determine whether it gives a polynomial-time obstruction test for a nontrivial restricted SAFESEP class. That would be materially stronger than merely renaming a planning deadend.
