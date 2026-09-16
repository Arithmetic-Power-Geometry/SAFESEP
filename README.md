# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** This is a diagnostic, not the SafeSep objective.

The original matched family has the same cheapest root probe `e1`, cost 1. Under decision-neutral and proof-qualified constructions the cheapest unresolved probe is `q`, cost 1. The evidence-authority closure construction preserves this invariant: `q` is independently executable in both systems and remains the cheapest probe that leaves an incompatible branch.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent planning, epistemic planning, world-dependent action applicability, history/provenance/purpose/consent authorization, proof-carrying authorization, trust negotiation, cyclic credential dependencies, non-circular authorization proofs, well-founded authorization semantics, recursive authorization, or least-fixed-point credential closure.

The proof-neutrality and branch-evolution attacks showed that local no-presupposition checks and dynamic proof eligibility can be encoded in established authorization/planning machinery. The latest evidence-authority closure attack shows that recursive evidence/authority cycles alone are also insufficient: trust-management systems already use recursive logical closure and handle cyclic dependencies.

## Surviving target: joint information-authority closure
The remaining candidate couples two evolving objects:
1. the decision-relevant information state induced by experiment outcomes; and
2. the least grounded authorization closure determining which future evidence experiments may legitimately execute.

An experiment may therefore change both what the agent knows and what the agent is authorized to learn next. The research target is minimum-cost adaptive resolution under this joint evolution. Novelty must come from a coupling-specific theorem/separation/complexity result, not from fixed points, recursive credentials, proof search, or contingent sensing individually.

## Datasets and empirical boundary
- `data/cheapest_experiment_cases.csv` — cheapest-probe cases.
- `data/parameterized_irreducibility.csv` — matched family through 100 worlds.
- `data/large_authorization_benchmark.csv` — controlled theorem benchmark from 200 through 10,000 explicit worlds.
- `data/real_authorization_source_audit.csv` — real-vs-controlled coverage audit.
- `data/dynamic_proof_coupling.csv` — branch-evolving proof-eligibility construction.
- `data/evidence_authority_closure.csv` — grounded-vs-unseeded recursive authority closure at 200 and 10,000 worlds.

AuthBench remains real external-validity evidence, but it does not natively provide counterfactual authorization-proof/evidence-yield graphs. We do not fabricate those labels. The 10,000-world controlled benchmarks remain theorem stress tests.

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
30. **Cheapest experiment under recursive authority closure** — `q`, cost 1, remains the cheapest executable experiment leaving mutually incompatible worlds in both matched systems.
31. **Unseeded evidence-authority cycle cannot self-authorize** — grounded chain admits resolver `r`; pure `r↔s` authority/evidence cycle does not enter the least closure.
32. **10,000-world evidence-authority closure stress test** — preserves identical cheapest probe but different resolver closure without incompatible-pair enumeration.

## Current novelty status
**Do not write the paper yet.** The latest fixed-point attack collides with established trust-management/authorization semantics. The strongest remaining target is now a theorem about **joint information-authority closure optimization**: two systems should match ordinary information summaries and ordinary authorization-closure summaries yet differ because the adaptive coupling between observations and grounded authority changes future feasible evidence paths.

The stop-and-write threshold remains one coupling-specific result that survives direct comparison with recursive trust management, proof-carrying authorization, stateful authorization logic, contingent/epistemic planning and adaptive diagnosis.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and narrow claims after every collision.

## License
Apache License 2.0. See `LICENSE`.
