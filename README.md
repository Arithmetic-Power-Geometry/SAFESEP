# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** This is a diagnostic, not the SafeSep objective.

In the original matched family, both systems have the same cheapest safe informative root probe `e1`, cost 1, one incompatible branch and `n(n-1)` worst-case incompatible pairs, yet `SafeSep(A_n)=2` and `SafeSep(B_n)=∞`.

Under the stronger decision-neutral criterion, the cheapest eligible unresolved probe is `q`, cost 1. It is informative but deliberately leaves a decision-critical residual branch.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent planning, epistemic planning, world-dependent action applicability, history/provenance/purpose/consent authorization, proof-carrying authorization, trust negotiation, cyclic credential dependencies, non-circular authorization proofs, or well-founded authorization semantics.

The latest attack is important: the local Decision-Neutral Authority Closure check can be compiled into ordinary authorization-proof dependency analysis when proof premises are explicit. `src/safesep/proof_neutral.py` implements this collision. A probe is locally neutral when at least one valid authorization proof avoids every disputed decision premise. Therefore **local no-presupposition checking itself is not our breakthrough**. See `docs/PROOF_NEUTRALITY_COLLISION.md`.

## Surviving target: Decision-Relative Authority Closure (DRAC)
The remaining candidate is the coupled adaptive problem. Let `C` be decision-critical. Each evidence probe may have multiple authorization proofs. A probe is eligible only if at least one proof is independent of the unresolved decision. Observations change `C`, which can change both the information problem and the relevant authorization-proof landscape. The objective is a minimum-cost adaptive tree ending at decision-homogeneous leaves.

The potentially novel object is therefore not proof acyclicity alone but **adaptive authorization resolution under proof-qualified evidence acquisition**. This remains a candidate until a coupling-specific theorem survives the remaining prior-art attack.

## Datasets and empirical boundary
- `data/cheapest_experiment_cases.csv` — cheapest-probe cases.
- `data/parameterized_irreducibility.csv` — matched family through 100 worlds.
- `data/large_authorization_benchmark.csv` — controlled theorem benchmark from 200 through 10,000 explicit worlds.
- `data/real_authorization_source_audit.csv` — real-vs-controlled coverage audit.

AuthBench is now verified directly from its public repository: **120 tasks, 80 standard + 40 sensitive, 10 categories**, gold read/write/execute permissions, and real constrained execution. This is useful external-validity evidence, but AuthBench does not provide alternative authorization-proof graphs or labels saying whether a proof depends on the disputed authorization conclusion. We do not fabricate those missing fields. The 10,000-world controlled benchmark remains the theorem stress test.

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
24. **All resolver proofs decision-tainted** — proof-dependency compilation reproduces the DNAC obstruction.
25. **Independent alternative-proof restoration** — one decision-independent proof restores eligible resolution even when another proof is circular/tainted.
26. **10,000-world proof-neutrality compilation** — the proof-dependency baseline reproduces the obstruction at scale.

## Current novelty status
**Do not stop yet.** The non-circular-proof attack narrows the claim again. Existing authorization logics and proof-carrying systems already provide proof-of-compliance, distributed proof construction, and mechanisms/restrictions for cyclic dependencies; trust negotiation explicitly studies circular credential dependencies. The surviving question is whether the *coupling* of minimum-cost adaptive evidence selection, decision-relative stopping, and proof-qualified authorization of the evidence itself yields a theorem or complexity separation not inherited from those ancestors.

The next stop-and-write threshold is: prove one coupling-specific result—ideally a reduction/separation or complexity theorem—and attack it against proof-carrying authorization, trust negotiation, authorization logic, contingent/epistemic planning and adaptive diagnosis. If it survives, we stop novelty hunting and write the paper.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and narrow claims after every collision.

## License
Apache License 2.0. See `LICENSE`.
