# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization does not improperly presuppose the unresolved decision.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, SAFESEP asks whether adaptive evidence can reach a decision-homogeneous branch while every probe is itself legitimately authorized.

## Cheapest-experiment diagnostic
We explicitly test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** This is a diagnostic, not the SafeSep objective. The original matched family has the same cheapest safe informative root probe `e1`, cost 1, one incompatible branch and `n(n-1)` worst-case incompatible pairs, yet `SafeSep(A_n)=2` and `SafeSep(B_n)=∞`.

The new decision-neutral construction asks the same question under a stronger criterion: a probe must be authorized without presupposing which unresolved authorization decision is correct. Its cheapest such probe is `q`, cost 1; `q` is informative but deliberately leaves a decision-critical residual branch.

## Prior-art collisions already established
When experiments are universally admissible the target reduces to Equivalence Class Determination. Strong contingent planning can encode the original finite SAFESEP model. Belief-relative admissibility can be encoded as epistemic action preconditions. Therefore adaptive sensing, decision-class stopping, fixed state-dependent admissibility, AND/OR belief search, cheapest-probe selection and knowledge-relative preconditions are not claimed as foundational novelties.

The JRSS provenance/history direction also substantially collides with established work: history-based access control makes authorization depend on prior security-sensitive events; purpose/consent models use purpose and conditions; proof-carrying authorization supports distributed proof search, sessions and iterative challenges; automated trust negotiation protects credentials by policies and explicitly studies cyclic credential-disclosure dependencies; provenance-aware authorization and evidential transaction logics likewise make provenance/evidence part of authorization. Consequently SAFESEP does **not** claim that history, provenance, purpose, consent, delegation, proof-carrying authorization or circular credential disclosure is new. See `docs/DECISION_NEUTRAL_AUTHORITY_CLOSURE.md`.

## Surviving candidate: Decision-Neutral Authority Closure
Let `C` be decision-critical. A probe `e` is **decision-neutral admissible on C** when its authorization basis is valid without presupposing which of the mutually incompatible decisions represented in `C` is correct.

This is stronger than extensional applicability. A probe can happen to be permitted in every actual world while still be unusable as a legitimate resolver when the only argument authorizing it assumes the very conclusion it is intended to establish.

Define `DN-SafeSep(C)` as the minimum worst-case cost of an adaptive decision-neutral probe tree ending at decision-homogeneous leaves; infinity means no such tree exists. The executable prototype is `src/safesep/decision_neutral.py`.

### Matched no-presupposition separation
The new construction fixes worlds, decisions, probe outcomes, costs and ordinary information structure. The resolver is informationally identical in both systems. In one system it has a decision-independent authorization basis; in the other its authorization basis presupposes the disputed decision. The first is decision-neutrally separable and the second is not.

This is a **surviving theorem candidate**, not yet a breakthrough claim. A general planner can encode an extra predicate; the candidate contribution is the authorization principle and its structural consequences, not raw representational impossibility.

## Datasets and empirical boundary
- `data/cheapest_experiment_cases.csv` — cheapest-probe cases.
- `data/parameterized_irreducibility.csv` — matched family through 100 worlds.
- `data/large_authorization_benchmark.csv` — controlled benchmark from 200 through 10,000 explicit worlds.
- `data/real_authorization_source_audit.csv` — explicit coverage audit separating real authorization data from the counterfactual fields required by SAFESEP.

AuthBench is a real public agent-authorization benchmark with permission-generation/replay infrastructure; the Amazon employee-access dataset is a large real access dataset. Neither natively supplies the counterfactual world × evidence-probe admissibility plus decision-independent-justification labels required to estimate DN-SafeSep. We therefore use them as external-validity/coverage sources and do not fabricate missing ground truth. The 10,000-world controlled benchmark remains the theorem stress test.

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
21. **Cheapest decision-neutral probe leaves incompatible worlds** — verifies `q` is the cheapest legitimate informative probe at cost 1 on a 200-world instance.
22. **Decision-neutral authority-closure separation** — identical information structure but finite/infinite neutral resolvability depending only on whether resolver authorization presupposes the disputed decision.
23. **10,000-world decision-neutral scale test** — repeats the separation on 5,000 READ + 5,000 WRITE worlds without enumerating all incompatible pairs.

## Current novelty status
We are closer, but have not yet reached the stop point. The strongest survivor is no longer provenance itself; it is **decision-neutral authorization of evidence acquisition**: extensional permission should not count as a resolving authority when its justification presupposes the unresolved authorization conclusion. Exact phrase searches did not reveal a direct SAFESEP/DNAC formulation, but adjacent trust-management and proof systems are expressive enough that a deeper comparison is mandatory.

The next decisive attack is against non-circular proof theory, recursive authorization/trust-management logics, well-founded semantics and justification logic. If those already impose an equivalent no-presupposition condition, we narrow again. If they do not, the next target is a formal non-circularity theorem plus a reduction/separation result; that is the intended stop-and-write threshold.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and narrow claims after every collision.

## License
Apache License 2.0. See `LICENSE`.
