# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions that are themselves justified by the information currently available.

> **Know enough to grant — but never grant to know.**

## Core question

Given current knowledge, several possible worlds may remain compatible while demanding different authorization decisions. SAFESEP asks whether those decision-incompatible worlds can be separated by an adaptive sequence of probes such that every probe is authorized in every world still possible on its branch. The exact world need not be identified; resolution occurs when all remaining worlds require the same authorization decision.

## Formal model

A finite instance has worlds `W`, current set `C`, decision `D(w)`, experiments `e`, outcomes `O_e(w)`, costs `c(e)`, and world-dependent admissibility `Adm(e,w)`. `C` is decision-critical iff `|{D(w):w∈C}|>1`. Experiment `e` is safely admissible at `C` iff `Adm(e,w)=1` for every `w∈C`. Outcome `o` contracts knowledge to `C_(e,o)={w∈C:O_e(w)=o}`.

A valid adaptive tree uses only safely admissible probes and terminates only at decision-homogeneous leaves. `SafeSep(C)` is its minimum worst-case accumulated cost; if no finite valid tree exists, `SafeSep(C)=∞`.

## Cheapest-experiment diagnostic

We explicitly test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** This is a diagnostic, not the SafeSep objective. In the matched family, both systems have the same cheapest safe informative root probe `e1`, cost 1, one incompatible branch, and `n(n-1)` worst-case incompatible pairs, yet one has finite SafeSep and the other infinite SafeSep.

## Baselines and prior-art boundary

**ARC-like:** minimum decision-resolution cost ignoring admissibility. **CARC-like one-step:** cheapest currently admissible single experiment whose every outcome is decision-homogeneous.

When every experiment is universally admissible, SAFESEP's decision target reduces to Equivalence Class Determination with classes `D^{-1}(d)`. Decision Region Determination already covers decision-directed adaptive information acquisition more generally, and active diagnosis/adaptive testing already use conditional plans and safety constraints. SAFESEP therefore does not claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, least privilege, JIT/task-scoped authorization, POMDP information gathering, value of information, trust negotiation, or conditional/epistemic planning.

The surviving candidate is **authorization-dependent safe separability**: unresolved worlds jointly determine both the required authorization decision and whether the evidence-producing action is currently legal.

## Parameterized matched-summary separation

For every `n>=2`, `A_n` and `B_n` contain `2n` worlds: READ worlds `r0,...,r(n-1)` and WRITE worlds `w0,...,w(n-1)`. Probe `e1` is universally admissible, isolates `r0`, and otherwise yields a residual branch. Probe `e2` reveals R versus W. Both systems have identical worlds, decisions, costs, complete outcome maps and admissibility counts.

In `A_n`, `e2` is admissible exactly on the residual branch after `e1`, giving a safe tree of cost 2. In `B_n`, `r1` is removed from `e2`'s admissibility set and already-eliminated `r0` inserted instead. The count is unchanged, but `e2` is forbidden on the residual branch. Thus `ARC(A_n)=ARC(B_n)=1`, `CARC(A_n)=CARC(B_n)=∞`, but `SafeSep(A_n)=2` and `SafeSep(B_n)=∞`.

## SAFESEP-EXISTS

`SAFESEP-EXISTS(P)` asks only whether `SafeSep(P)<∞`. The repository now contains an independent exact AND-OR/fixed-point existence solver. With `N` explicit worlds, at most `2^N` knowledge subsets can be encountered, giving a direct exponential-time upper bound with polynomial work per subset. This is **not** a hardness result. We explicitly do not infer NP-, PSPACE-, or EXPTIME-hardness merely from the exponential algorithm. See `docs/COMPLEXITY_AND_REAL_DATA.md`.

## Reproducible results

| Case | ARC-like | CARC one-step | SafeSep | Meaning |
|---|---:|---:|---:|---|
| minimal deadlock | 1 | ∞ | ∞ | information exists but safe resolution fails |
| adaptive safe | 1 | ∞ | 2 | branchwise resolution succeeds after one-step failure |
| homogeneous | 0 | 0 | 0 | no probe needed |
| matched A_n | 1 | ∞ | 2 | safely resolvable |
| matched B_n | 1 | ∞ | ∞ | matched summaries but obstructed |

## Datasets

- `data/cheapest_experiment_cases.csv` — cheapest-probe cases.
- `data/parameterized_irreducibility.csv` — matched family through 100 worlds.
- `data/large_authorization_benchmark.csv` — controlled benchmark from 200 through 10,000 explicit worlds.

For empirical external validity, the project tracks real/public authorization sources separately. Published work characterizes the Amazon employee access dataset at 32,769 authorization records, 9,560 users and 7,517 resources. AuthBench provides agent tasks with gold read/write/execute permission annotations and policy-constrained replay. Real-world AWS serverless studies provide another route to empirical IAM policy structure. These sources do **not** directly provide SAFESEP's counterfactual world × probe-admissibility matrix, so we will not fabricate it. A real-data adapter must specify that mapping before any empirical SafeSep claim is made.

## Test registry

Scientifically meaningful tests are permanent repository tests and their results are preserved.

1. **Minimal authorization deadlock** — finite unconstrained distinguishability with `SafeSep=∞`.
2. **Adaptive safe resolution** — branchwise admissibility gives finite SafeSep despite no one-step resolver.
3. **Decision-homogeneous zero cost**.
4. **Matched-summary irreducibility**.
5. **Cheapest admissible experiment leaves incompatibility**.
6. **Adaptive-safe has no admissible one-step resolver**.
7. **Deadlock has no admissible one-step resolver**.
8. **Parameterized irreducibility, n=2..20**.
9. **Scale invariance through 100 worlds**.
10. **Parameterized analytic construction invariants, n=2..50**.
11. **Cheapest-probe irreducibility** — identical cheapest-probe statistics but finite/infinite SafeSep.
12. **Large matched-family structural invariants** — validates exact separation structure through 10,000 worlds.
13. **Large constructive safe-tree/obstruction test** — independently checks the two-step witness for A and residual authorization obstruction for B.
14. **SAFESEP-EXISTS/optimization equivalence on core cases** — independently verifies the yes/no fixed-point solver agrees with finite versus infinite minimum-cost SafeSep.
15. **SAFESEP-EXISTS parameterized separation** — verifies existence for `A_n` and nonexistence for `B_n`, `n=2..30`, without using cost values.

Current test files include `test_safesep.py`, `test_irreducibility.py`, `test_cheapest_experiment.py`, `test_parameterized_irreducibility.py`, `test_large_authorization_benchmark.py`, and `test_existence.py`.

## Current novelty status

The strongest surviving result is an infinite matched-summary family showing that authorization safe resolvability depends on branch-level world × probe-admissibility incidence even when worlds, decision classes, outcome maps, costs, admissibility counts, unconstrained resolution, one-step closed resolution and cheapest-root-probe statistics coincide. The new existence solver confirms the separation is about resolvability itself rather than cost arithmetic.

This is still not proof that general active-diagnosis or contingent-planning formalisms cannot encode SAFESEP. The next decisive mathematical target is a rigorous lower-bound reduction for the exact finite SAFESEP model, or a proof that its existence problem falls into a simpler class. We will stop novelty hunting and write the paper once the authorization-dependent incidence result plus its complexity boundary is strong enough to survive this comparison.

## Research protocol

For every significant result: formulate the claim; attack it with prior art; construct a witness/counterexample; compare baselines; use a dataset when meaningful; save code/data/results; add a permanent regression test; append this registry; run CI; and narrow claims whenever an ancestor already contains the general idea.

## License

Apache License 2.0. See `LICENSE`.
