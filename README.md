# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** This is a diagnostic, not the SafeSep objective.

In the original matched family, both systems have the same cheapest safe informative root probe `e1`, cost 1, one incompatible branch and `n(n-1)` worst-case incompatible pairs, yet `SafeSep(A_n)=2` and `SafeSep(B_n)=∞`.

Under the proof-qualified branch-evolution construction, both matched systems again have the same cheapest eligible unresolved probe `q`, cost 1. It is informative but deliberately leaves a decision-critical residual branch.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent planning, epistemic planning, world-dependent action applicability, history/provenance/purpose/consent authorization, proof-carrying authorization, trust negotiation, cyclic credential dependencies, non-circular authorization proofs, well-founded authorization semantics, stateful authorization, or branch-dependent proof eligibility by itself.

The local Decision-Neutral Authority Closure check can be compiled into ordinary authorization-proof dependency analysis when proof premises are explicit. `src/safesep/proof_neutral.py` implements this collision. The new `src/safesep/dynamic_proof.py` additionally tests branch-relative proof eligibility. See `docs/PROOF_NEUTRALITY_COLLISION.md` and `docs/BRANCH_EVOLUTION_COLLISION.md`.

## DRAC branch-evolution result
For matched systems A_n and B_n, `q` has the same cost and outcomes and is the same cheapest eligible unresolved root probe. The resolver has the same cost, outcomes, proof count, and is initially ineligible in both systems. After q contracts the belief from 2n to 2n-1 worlds, the resolver becomes proof-eligible in A_n but remains ineligible in B_n. Hence A_n is adaptively resolvable while B_n is not. The construction is stress-tested through 10,000 explicit worlds.

This is a useful coupling result but **not yet the breakthrough stop point**. Stateful Authorization Logic already permits policies to depend on system state, proof-carrying authorization supports iterative proof acquisition/challenges, and a general contingent planner can enlarge its state to include proof/policy state. Therefore dynamic proof eligibility alone is not claimed as a new planning primitive.

## Surviving frontier
The remaining target is stricter: characterize cases where the *justification for evidence acquisition itself* depends on evidence whose legitimate acquisition is governed by the unresolved authorization relation, and derive an invariant/impossibility/complexity result that is not erased by simply compiling proof state into an enlarged planning state.

## Datasets and empirical boundary
- `data/cheapest_experiment_cases.csv` — cheapest-probe cases.
- `data/parameterized_irreducibility.csv` — matched family through 100 worlds.
- `data/large_authorization_benchmark.csv` — controlled theorem benchmark from 200 through 10,000 explicit worlds.
- `data/dynamic_proof_coupling.csv` — branch-evolving proof-eligibility separation through 10,000 worlds.
- `data/real_authorization_source_audit.csv` — real-vs-controlled coverage audit.

AuthBench is verified from its public repository: 120 tasks, 80 standard + 40 sensitive, 10 categories, gold read/write/execute permissions, and constrained execution. It does not provide counterfactual proof-dependency/decision-dependency labels, so those fields are not fabricated. Controlled 10,000-world constructions remain theorem stress tests.

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
24. All resolver proofs decision-tainted — proof-dependency compilation reproduces the DNAC obstruction.
25. Independent alternative-proof restoration — one decision-independent proof restores eligible resolution.
26. 10,000-world proof-neutrality compilation.
27. **Matched cheapest branch-evolving probe** — both systems select `q`, cost 1, while q leaves incompatible worlds.
28. **Branch-evolution resolvability separation** — identical root eligibility and information structure, but resolver eligibility diverges after the same belief contraction, yielding finite vs impossible adaptive resolution.
29. **10,000-world branch-evolution stress test** — preserves the divergence at 5,000 READ + 5,000 WRITE worlds.

## Current novelty status
**Do not stop yet.** Tests 27-29 establish the requested branch-evolution separation, but the prior-art attack shows that state-dependent authorization and iterative proof acquisition are established. The result is preserved because it identifies exactly what still fails to establish novelty.

The next stop-and-write threshold remains one coupling-specific invariant, impossibility, or complexity theorem that survives reduction to stateful/proof-carrying authorization and contingent/epistemic planning. The strongest next direction is a self-governing evidence-authority closure in which evidence needed to justify a probe is itself obtainable only through probes governed by the unresolved authority relation.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and narrow claims after every collision.

## License
Apache License 2.0. See `LICENSE`.
