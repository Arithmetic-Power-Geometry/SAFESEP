# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. In the matched family it leaves one residual branch with `n(n-1)` incompatible pairs: 9,900 at 200 worlds and 24,995,000 at 10,000 worlds.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent/epistemic planning, world-dependent applicability, history/provenance authorization, proof-carrying authorization, trust negotiation, cyclic credentials, recursive authorization, dynamic evidence gathering, joint information-authority state representation, minimal credential disclosure, generic cost-sensitive trust negotiation, pair separation, minimum test cover, or decision-region/equivalence-class edge cutting.

## Structural results retained
The matched-marginal family proves that the implemented separate information and authority summaries do not determine joint resolvability. Full joint-state planning can encode the missing alignment, so this is summary insufficiency rather than a new planning primitive. The authorization-safe evidence premium measures the extra legitimate cost but is not claimed novel because disclosure-cost optimization is established.

## Legitimate incompatible-pair cut
For a decision-critical state let `I(C)` be all pairs of compatible worlds requiring different decisions. Each experiment separates a subset of `I(C)`. In the static-legitimacy restriction, let `L(C)` be the union of pairs separated by legitimately executable experiments. If `I(C) \\ L(C)` is nonempty, at least one incompatible pair cannot be separated by any legitimate experiment, giving a sufficient impossibility certificate.

The matched A/B construction keeps worlds, decisions, experiment names, costs and complete outcome maps identical. Thus raw pair-separation structure is identical. Authorization alone changes the usable pair cover: A's resolver is legitimate and covers all incompatible pairs; B's informationally identical resolver is blocked. This is useful, but the static certificate reduces to established pair/test-cover structure after filtering unavailable tests, so it is not the stop-and-write breakthrough.

## Datasets and empirical boundary
Controlled theorem datasets include `large_authorization_benchmark.csv`, `dynamic_proof_coupling.csv`, `evidence_authority_closure.csv`, `joint_coupling_matched_marginals.csv`, `joint_planning_collision.csv`, `authority_premium.csv`, and `legitimate_pair_cut.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. AuthBench is retained as real external-validity evidence, but it does not natively provide counterfactual world×experiment outcomes plus legitimate-executability/proof labels; we do not fabricate them.

## Test registry
1–40. Previous SAFESEP regression and collision tests retained unchanged.
41. **Authority-premium cheapest experiment** — `q`, cost 1; 9,900 residual incompatible pairs at 200 worlds.
42. **Finite authorization premium** — unconstrained cost 1 versus legitimate cost 2, `AP=1`.
43. **Infinite authorization premium** — unconstrained cost 1 versus legitimate impossibility, `AP=infinity`.
44. **10,000-world authority-premium stress** — 24,995,000 residual incompatible pairs.
45. **Legitimate pair-cut cheapest probe** — `q`, cost 1, still leaves 9,900 incompatible pairs at 200 worlds.
46. **Uncovered-pair impossibility certificate** — A has no uncovered incompatible pair; B has at least one and is pair-cut obstructed.
47. **Raw-information equality / usable-cover separation** — A/B have identical outcomes and separated-pair sets for every experiment, but different legitimate pair cover.
48. **10,000-world pair-cut structural stress** — `q` cost 1 and 24,995,000 residual incompatible pairs; the informationally identical resolver is legitimate only in A. Pair sets are counted analytically to avoid materializing 25,000,000 root pairs in CI.

## Current novelty status
**Do not write the paper yet.** The static legitimate-pair cut is scientifically clean but collides with classical test cover and Decision Region Determination once illegitimate experiments are simply removed. The next candidate must be **dynamic branch-relative authorization cut**: legitimacy must evolve with observations/evidence so no static deletion of tests reproduces the obstruction. It must then survive full-state contingent-planning comparison. A theorem or lower bound at that point would be a credible stop-and-write candidate.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and narrow claims after every collision.

## License
Apache License 2.0. See `LICENSE`.
