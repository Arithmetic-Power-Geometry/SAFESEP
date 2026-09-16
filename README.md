# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions that are themselves justified by the information currently available.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, SAFESEP asks whether adaptive evidence can reach a decision-homogeneous branch while every probe is itself authorized.

## Cheapest-experiment diagnostic
We explicitly test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** This is a diagnostic, not the SafeSep objective. In the matched family both systems have the same cheapest safe informative root probe `e1`, cost 1, one incompatible branch, and `n(n-1)` worst-case incompatible pairs, yet `SafeSep(A_n)=2` and `SafeSep(B_n)=∞`.

## Prior-art boundary
When experiments are universally admissible the target reduces to Equivalence Class Determination. Strong contingent planning can encode the original finite SAFESEP model by mapping worlds to states, experiments to sensing actions, fixed `Adm(e,w)` to action applicability, observations to belief successors, and decision-homogeneous beliefs to goals. Therefore adaptive sensing, decision-class stopping, fixed state-dependent admissibility, AND/OR belief search, and cheapest-probe selection are not claimed as foundational novelties.

## New attack: endogenous authorization
We next tested knowledge-relative admissibility `J(e,C)`. This also collides with epistemic planning whenever `J` is a deterministic predicate of belief `C`: it can be compiled into an epistemic action precondition. Dynamic epistemic logic already supports formula-valued action preconditions, and prior work explicitly studies endogenizing epistemic actions. See `docs/ENDOGENOUS_AUTHORIZATION_ATTACK.md`.

The surviving candidate is narrower: **justification-relative safe separability (JRSS)**. Two histories can induce the same compatible-world set and the same information structure but carry different authority/consent/purpose/delegation provenance. Write `Q(h)` for that justification state and use admissibility `J(e,C,Q(h))`. The repository now contains a research prototype in `src/safesep/justification.py`.

Important limitation: JRSS is not yet claimed as non-reducible to planning, because a sufficiently general planner can augment its state with `Q`. The potential contribution is authorization-specific: whether epistemically identical histories can have different evidence-acquisition authority and therefore different safe resolvability.

## Matched-provenance separation
The new witness holds worlds, decisions, experiments, outcomes, costs and cheapest information structure fixed. Only the initial authority provenance differs. In the authorized instance, the protected decision-resolving probe is legal and `JR-SafeSep=1`; in the provenance-missing instance the same probe is illegal and `JR-SafeSep=∞`.

This proves only a matched-belief provenance separation for the prototype semantics. It does not yet establish literature-level novelty; the next attack is against history-based access control, provenance-aware authorization, trust/delegation logics, consent/purpose systems and proof-carrying authorization.

## Datasets
- `data/cheapest_experiment_cases.csv` — cheapest-probe cases.
- `data/parameterized_irreducibility.csv` — matched family through 100 worlds.
- `data/large_authorization_benchmark.csv` — controlled benchmark from 200 through 10,000 explicit worlds.

Real/public authorization datasets remain external-validity targets, but they do not natively provide counterfactual world × probe admissibility or justification-provenance ground truth. We will not fabricate such fields and call them real observations.

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
19. **Matched-belief justification-provenance separation** — identical epistemic state/information structure, finite versus infinite JR-SafeSep due solely to authority provenance.
20. **Cheapest-information invariance under provenance split** — both instances expose identical experiment names/costs and identical cheapest information cost despite different JR-SafeSep.

## Current novelty status
We have not reached the stop point. The original SAFESEP formalism collides with contingent planning; belief-relative preconditions collide with epistemic planning. JRSS is a stronger authorization-specific survivor, but must now survive provenance-aware authorization/history/delegation prior art. We will write the paper only when that attack leaves a theorem whose novelty can be stated narrowly and defensibly.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and narrow claims after every collision.

## License
Apache License 2.0. See `LICENSE`.
