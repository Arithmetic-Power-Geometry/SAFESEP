# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP studies whether an autonomous agent can resolve an authorization decision using evidence-gathering actions that are themselves justified by the information currently available.

> **Know enough to grant — but never grant to know.**

## Core model
A finite instance has worlds `W`, current set `C`, decision `D(w)`, experiments `e`, outcomes `O_e(w)`, costs `c(e)`, and world-dependent admissibility `Adm(e,w)`. Resolution occurs when `|{D(w):w∈C}|=1`. A probe is branchwise safe iff it is admissible in every world still possible on that branch. `SafeSep(C)` is the minimum worst-case cost of a resolving adaptive tree; it is infinite if no such tree exists.

## Cheapest-experiment diagnostic
We test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** This is only a diagnostic, not the optimization objective. The matched family has the same cheapest safe root probe, same cost, same number of incompatible branches and same incompatible-pair count, yet finite versus infinite SafeSep.

## Important prior-art collision
A targeted comparison with classical strong/conditional planning under partial observability found a major overlap: prior planning work already performs AND/OR search over belief states, uses conditional observation trees, and defines an action as applicable to an uncertain belief only when it is applicable in every state represented by that belief. Consequently **belief-universal action admissibility, branchwise sensing, conditional resolution trees, and SAFESEP-EXISTS as a bare planning structure are not claimed as novel.** See `docs/CONTINGENT_PLANNING_COLLISION.md`.

The surviving research frontier is narrower: **endogenous authorization of epistemic actions**—the unresolved authorization state is simultaneously what the agent must learn and what determines whether the learning action is legally/organizationally permitted. Mere encoding of this coupling as ordinary planning preconditions is not enough for novelty; we now require an authorization-specific theorem or separation that uses the coupling essentially.

## Parameterized matched-summary separation
For every `n>=2`, `A_n` and `B_n` have `2n` worlds and identical decisions, probe costs, complete outcome maps, aggregate admissibility counts, unconstrained resolution cost, one-step closed resolution, and cheapest-root-probe statistics. They differ only in world × probe admissibility incidence. Nevertheless `SafeSep(A_n)=2` while `SafeSep(B_n)=∞`. This remains a useful structural result, but after the contingent-planning collision it is treated as an authorization-interpretation result rather than proof of a new planning primitive.

## SAFESEP-EXISTS
`SAFESEP-EXISTS(P)` asks whether `SafeSep(P)<∞`. The exact repository solver explores at most `2^N` explicit knowledge subsets. This is an algorithmic upper bound, not a hardness result. Because strong contingent planning already studies closely related belief-space existence problems, no complexity novelty is claimed without a reduction that isolates genuinely authorization-specific structure.

## Datasets
- `data/cheapest_experiment_cases.csv` — cheapest-probe cases.
- `data/parameterized_irreducibility.csv` — matched family through 100 worlds.
- `data/large_authorization_benchmark.csv` — controlled structural benchmark through 10,000 explicit worlds.

Real/public authorization sources are tracked separately. Existing employee-access and agent-permission datasets do not directly contain SAFESEP's counterfactual world × probe-admissibility relation, so the project will not fabricate that relation and call it real data.

## Test registry
Scientifically meaningful tests are permanent repository tests and their results are preserved.

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
15. SAFESEP-EXISTS parameterized separation, n=2..30.
16. **Contingent-planning collision audit** — literature-level falsification test showing that universal belief-state applicability and AND/OR conditional planning are established ancestors; preserved in `docs/CONTINGENT_PLANNING_COLLISION.md` and used to prohibit overclaiming.

## Current novelty status
**Do not write the paper yet.** The latest prior-art attack materially narrows the novelty claim. The matched incidence family is valid, but its general computational mechanism is representable inside established contingent planning. The next breakthrough criterion is therefore stronger: prove an invariant, impossibility, separation, or quantitative law that follows specifically from authorization being endogenous to evidence acquisition and is not merely a restatement of ordinary action preconditions.

## Research protocol
For every significant result: formulate; attack with prior art; build a witness/counterexample; compare baselines; use real data only where semantics are genuine; save code/data/results; preserve significant tests; run CI; and narrow claims whenever an ancestor already contains the general idea.

## License
Apache License 2.0. See `LICENSE`.
