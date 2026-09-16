# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** This is a diagnostic, not the SafeSep objective.

Across the current constructions, the cheapest unresolved probe remains `q`, cost 1. It leaves exactly one incompatible residual branch with `n(n-1)` incompatible pairs: 9,900 at 200 worlds and 24,995,000 at 10,000 worlds.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent/epistemic planning, world-dependent action applicability, history/provenance/purpose/consent authorization, proof-carrying authorization, trust negotiation, cyclic credential dependencies, recursive authorization, dynamic evidence gathering, joint information-authority state representation, minimal credential disclosure, or generic cost-sensitive trust negotiation.

## Structural results retained
The matched-marginal family proves that the implemented separate information and authority summaries do not determine joint resolvability. The full joint-state planning attack then shows that ordinary contingent planning can encode the missing alignment once authority is exposed as state. Thus this is a summary-insufficiency result, not a new planning primitive.

## Authorization-safe evidence premium
For a fixed problem P define `U(P)` as minimum decision-resolution cost when authority constraints are ignored and `S(P)` as minimum cost using only legitimately authorized experiments. Define `AP(P)=S(P)-U(P)`, with infinity when `U(P)` is finite but `S(P)` is infinite.

In the controlled witness, unconstrained resolution costs 1. The safely resolvable case requires `q` followed by the resolver, so `S=2` and `AP=1`; the authority-obstructed case has `S=infinity` and `AP=infinity`. This is a useful quantitative diagnostic, but broad authorization/disclosure-cost optimization already exists in cost-sensitive trust negotiation, so the premium alone is not claimed as breakthrough novelty.

## Datasets and empirical boundary
- `data/cheapest_experiment_cases.csv` — cheapest-probe cases.
- `data/parameterized_irreducibility.csv` — matched family through 100 worlds.
- `data/large_authorization_benchmark.csv` — controlled theorem benchmark from 200 through 10,000 explicit worlds.
- `data/real_authorization_source_audit.csv` — real-vs-controlled coverage audit.
- `data/dynamic_proof_coupling.csv` — branch-evolving proof-eligibility construction.
- `data/evidence_authority_closure.csv` — recursive authority closure benchmark.
- `data/joint_coupling_matched_marginals.csv` — matched separate marginals at 200 and 10,000 worlds.
- `data/joint_planning_collision.csv` — full joint-state planning comparison through 10,000 worlds.
- `data/authority_premium.csv` — authorization-safe evidence premium at 200 and 10,000 worlds.

AuthBench remains real external-validity evidence, but it does not natively provide counterfactual authorization-proof/evidence-yield graphs. We do not fabricate those labels. Controlled 10,000-world benchmarks remain theorem stress tests.

## Test registry
1. Minimal authorization deadlock.
2. Adaptive safe resolution.
3. Decision-homogeneous zero cost.
4. Matched-summary irreducibility.
5. Cheapest admissible experiment leaves incompatibility.
6. Adaptive-safe has no admissible one-step resolver.
7. Deadlock has no admissible one-step resolver.
8. Parameterized irreducibility, n=2..20.
9. Scale invariance through 100 worlds.
10. Parameterized analytic construction invariants, n=2..50.
11. Cheapest-probe irreducibility.
12. Large matched-family structural invariants through 10,000 worlds.
13. Large constructive safe-tree/obstruction test.
14. SAFESEP-EXISTS/optimization equivalence on core cases.
15. SAFESEP-EXISTS parameterized separation.
16. Contingent-planning collision on core cases.
17. Contingent-planning collision on A_n/B_n through n=30.
18. Cheapest-probe collision survives planning reduction through n=50.
19. Matched-belief justification-provenance separation.
20. Cheapest-information invariance under provenance split.
21. Cheapest decision-neutral probe leaves incompatible worlds — `q`, cost 1, on 200 worlds.
22. Decision-neutral authority-closure separation.
23. 10,000-world decision-neutral scale test.
24. All resolver proofs decision-tainted — proof-dependency compilation reproduces obstruction.
25. Independent alternative-proof restoration.
26. 10,000-world proof-neutrality compilation.
27. Branch-evolving matched cheapest-probe test.
28. Branch-evolving proof-eligibility resolvability separation.
29. 10,000-world branch-evolution stress test.
30. Cheapest experiment under recursive authority closure — `q`, cost 1.
31. Unseeded evidence-authority cycle cannot self-authorize.
32. 10,000-world evidence-authority closure stress test.
33. Matched-marginal cheapest experiment — `q`, cost 1; 9,900 incompatible pairs at 200 worlds.
34. Separate-marginal equality.
35. Joint-alignment separation.
36. 10,000-world matched-marginal stress test — 24,995,000 incompatible pairs.
37. Full-planner cheapest-experiment preservation.
38. Combined-state planning collision.
39. Marginals-vs-joint-state test.
40. 10,000-world full-planner stress test.
41. **Authority-premium cheapest experiment** — `q`, cost 1, still leaves 9,900 incompatible pairs at 200 worlds.
42. **Finite authorization premium** — unconstrained cost 1 versus legitimate cost 2, hence `AP=1`.
43. **Infinite authorization premium under obstruction** — unconstrained cost remains 1 while legitimate resolution is impossible, hence `AP=infinity`.
44. **10,000-world authority-premium stress test** — identical `q` diagnostic with 24,995,000 incompatible pairs; premium 1 versus infinity.

## Current novelty status
**Do not write the paper yet.** The authorization-safe evidence premium is quantitatively useful, but cost-sensitive trust negotiation already optimizes credential/policy disclosure costs and minimal credential disclosure is established. The next candidate must be a genuinely authorization-specific lower bound/invariant tied to decision-incompatible possible-world pairs and legitimate evidence paths, and must be attacked against test cover, decision-region determination, trust-negotiation cost optimization, and constrained planning.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and narrow claims after every collision.

## License
Apache License 2.0. See `LICENSE`.
