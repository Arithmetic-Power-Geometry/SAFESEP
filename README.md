# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** This is a diagnostic, not the SafeSep objective.

Across the current proof-qualified, evidence-authority, matched-marginal and full joint-state planning constructions, the cheapest unresolved probe is `q`, cost 1. In the matched family it is identical in both systems and leaves exactly one incompatible residual branch with `n(n-1)` incompatible pairs: 9,900 at 200 worlds and 24,995,000 at 10,000 worlds.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent planning, epistemic planning, world-dependent action applicability, history/provenance/purpose/consent authorization, proof-carrying authorization, trust negotiation, cyclic credential dependencies, non-circular authorization proofs, well-founded authorization semantics, recursive authorization, least-fixed-point credential closure, dynamic evidence gathering, or representing information and authority variables jointly in a planner.

## Current structural result: matched marginals do not determine joint resolvability
For every `n>=2`, `A_n` and `B_n` match the tested separate information and authority summaries: same `2n` worlds, decisions, q cost/outcome partition, branch-size multiset, token multiset, resolver multiset, authority-edge count and cheapest-unresolved-probe statistics. They differ only in the alignment between q outcomes and authority-enabling tokens.

`A_n`: residual outcome -> `alpha` -> `resolve_rest`.

`B_n`: residual outcome -> `beta` -> `resolve_special`.

Therefore the tested marginals satisfy `M_info(A_n)=M_info(B_n)` and `M_auth(A_n)=M_auth(B_n)`, while residual resolvability differs. This is a valid structural separation of the listed summaries.

## Full joint-state planning attack
`src/safesep/joint_planning_baseline.py` independently exposes `(compatible worlds, acquired authority tokens)` as the planner state. It exactly reproduces the A/B separation. Hence the matched-marginal theorem does **not** establish irreducibility to contingent planning: the full branch-sensitive joint signature distinguishes the systems and ordinary contingent planning can encode the authority tokens as state propositions/effects.

## Datasets and empirical boundary
- `data/cheapest_experiment_cases.csv` — cheapest-probe cases.
- `data/parameterized_irreducibility.csv` — matched family through 100 worlds.
- `data/large_authorization_benchmark.csv` — controlled theorem benchmark from 200 through 10,000 explicit worlds.
- `data/real_authorization_source_audit.csv` — real-vs-controlled coverage audit.
- `data/dynamic_proof_coupling.csv` — branch-evolving proof-eligibility construction.
- `data/evidence_authority_closure.csv` — recursive authority closure benchmark.
- `data/joint_coupling_matched_marginals.csv` — matched separate marginals at 200 and 10,000 worlds.
- `data/joint_planning_collision.csv` — full joint-state planning comparison through 10,000 worlds.

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
33. Matched-marginal cheapest experiment — both systems return `q`, cost 1, one unresolved branch; 9,900 incompatible pairs at 200 worlds.
34. Separate-marginal equality.
35. Joint-alignment separation.
36. 10,000-world matched-marginal stress test — 24,995,000 incompatible pairs.
37. **Full-planner cheapest-experiment preservation** — `q`, cost 1, still leaves incompatibility.
38. **Combined-state planning collision** — ordinary joint-state contingent planning exactly reproduces A resolvable/B blocked.
39. **Marginals-vs-joint-state test** — separate summaries match but full branch-sensitive state signatures differ.
40. **10,000-world full-planner stress test** — `q` cost 1, 24,995,000 residual incompatible pairs; combined-state planner reproduces the separation.

## Current novelty status
**Do not write the paper yet.** The full joint-state attack is a clean negative novelty result: the matched-marginal separation survives as a summary-insufficiency theorem, but disappears as a representational novelty claim once authority is included in the contingent-planning state.

The next stop-and-write candidate must survive full-state compilation. The strongest directions are now a restricted complexity theorem, an authorization-specific invariant/lower bound on legitimate evidence acquisition, or an empirical phenomenon with genuine authorization semantics. We will not claim a new planning primitive.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and narrow claims after every collision.

## License
Apache License 2.0. See `LICENSE`.
