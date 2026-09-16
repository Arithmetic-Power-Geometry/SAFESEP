# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent/epistemic planning, world-dependent applicability, history/provenance authorization, proof-carrying authorization, trust negotiation, cyclic credentials, recursive authorization, dynamic evidence gathering, joint information-authority state representation, minimal credential disclosure, generic cost-sensitive trust negotiation, pair separation, minimum test cover, or decision-region/equivalence-class edge cutting.

## Structural results retained
Matched information/authority marginals do not determine joint resolvability, but full joint-state planning can encode the missing alignment. The authorization-safe evidence premium quantifies extra legitimate cost, but disclosure-cost optimization is established. The static legitimate-pair cut is a useful impossibility certificate but reduces to test-cover/DRD structure after filtering unavailable tests.

## Dynamic branch-relative authorization cut
Let a joint state be `S=(C,A)`, compatible worlds plus currently held authority facts, and let `K` be a set of decision-separating probes. A sufficient deadlock certificate is:

1. every decision-incompatible root pair can be separated only by a probe in `K`; and
2. in every decision-critical joint state reachable without using `K`, every probe in `K` is unauthorized.

Then no legitimate resolving policy exists: any resolving policy must have a first use of `K`, but its predecessor is a decision-critical state reachable without `K`, where condition 2 says no member of `K` is executable.

In the controlled OPEN/BLOCKED witness, `q` is the cheapest unresolved probe at cost 1. Resolver `r` is the mandatory cut and requires token `alpha`. OPEN grants alpha after q's residual outcome, so the certificate correctly rejects deadlock. BLOCKED never grants alpha, so the certificate proves deadlock. This is a compact sufficient authorization-deadlock certificate, **not yet a claimed breakthrough**: full-state contingent planning can represent the same state transition, and planning dead-end/landmark/cut literature remains the next collision target.

## Datasets and empirical boundary
Controlled theorem datasets include `large_authorization_benchmark.csv`, `dynamic_proof_coupling.csv`, `evidence_authority_closure.csv`, `joint_coupling_matched_marginals.csv`, `joint_planning_collision.csv`, `authority_premium.csv`, `legitimate_pair_cut.csv`, and `dynamic_authority_cut.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. AuthBench is retained as real external-validity evidence, but it does not natively provide counterfactual world×experiment outcomes plus legitimate-executability/proof labels; we do not fabricate them.

## Test registry
1–40. Previous SAFESEP regression and collision tests retained unchanged.
41. **Authority-premium cheapest experiment** — `q`, cost 1; 9,900 residual incompatible pairs at 200 worlds.
42. **Finite authorization premium** — unconstrained cost 1 versus legitimate cost 2, `AP=1`.
43. **Infinite authorization premium** — unconstrained cost 1 versus legitimate impossibility, `AP=infinity`.
44. **10,000-world authority-premium stress** — 24,995,000 residual incompatible pairs.
45. **Legitimate pair-cut cheapest probe** — `q`, cost 1, still leaves 9,900 incompatible pairs at 200 worlds.
46. **Uncovered-pair impossibility certificate** — static legitimate cover detects obstruction.
47. **Raw-information equality / usable-cover separation** — identical information, different legitimate pair cover.
48. **10,000-world pair-cut structural stress** — 24,995,000 residual incompatible pairs.
49. **Dynamic-cut cheapest probe** — `q`, cost 1, leaves 9,900 incompatible pairs at 200 worlds.
50. **Dynamic mandatory-cut deadlock certificate** — BLOCKED satisfies mandatory-cut plus pre-cut authorization obstruction.
51. **Certificate rejection on resolvable system** — OPEN grants the cut authority after `q`, so the deadlock certificate correctly fails.
52. **10,000-world dynamic-cut structural stress** — same `q` diagnostic and 24,995,000 residual incompatible pairs; scale-invariant certificate structure checked without materializing O(N^2) pairs in CI.

## Current novelty status
**Do not write the paper yet.** The dynamic authorization cut is stronger than the static pair-cover certificate because legitimacy changes along branches, but it is still representable in the full joint state. The next decisive attack is against planning dead-end certificates, landmarks/action cuts, strong cyclic/contingent planning, and AND/OR reachability. We stop novelty hunting only if a theorem, invariant, lower bound, or algorithmic advantage remains after that reduction.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and narrow claims after every collision.

## License
Apache License 2.0. See `LICENSE`.
