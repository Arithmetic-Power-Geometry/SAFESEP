# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent/epistemic planning, world-dependent applicability, history/provenance authorization, proof-carrying authorization, trust negotiation, runtime access-policy discovery, cyclic credentials, cyclic policy interdependency, recursive authorization/fixed-point closure, dynamic evidence gathering, joint information-authority state representation, minimal credential disclosure, generic cost-sensitive trust negotiation, pair separation, minimum test cover, decision-region edge cutting, generic planning landmarks, generic unavoidable-deadend reasoning, dynamic authorization-state updates, observation-conditioned authority-state transitions, latent policy identity, generic context-dependent/nonmonotonic rule validity, or the generic distinction between grounded and unsupported circular authorization proofs.

## Structural results retained
Matched information/authority marginals do not determine joint resolvability, but full joint-state planning can encode the missing alignment. The authorization-safe evidence premium quantifies extra legitimate cost, but disclosure-cost optimization is established. Static pair cuts reduce to test-cover/DRD structure after filtering unavailable tests.

## Dynamic branch-relative authorization cut — corrected
Let joint state be `S=(C,A)` and let `K` be a candidate mandatory probe set. The corrected sufficient certificate is: (1) after removing K, no complete resolving policy exists; and (2) in every decision-critical joint state reachable without K, every probe in K is unauthorized. Then no legitimate resolving policy exists.

### CI-discovered scientific correction
The first implementation incorrectly required every incompatible root pair to be separable only by K. GitHub CI rejected Tests 49–52. The code and theorem were corrected to exact restricted AND/OR semantics; the failure remains documented rather than hidden.

## Observation-Conditioned Authority Topology attack
Tests 57–60 match initial worlds, decisions, cheapest probe, cost, and initial authority graph, then let an observation activate an authority edge only in A. A resolves and B blocks, but full-state contingent planning captures this difference. OCAT is therefore a collision result, not a breakthrough.

## Second-order policy uncertainty attack
Tests 61–64 make the applicable authorization policy latent. q remains cost 1 and leaves incompatible decisions plus multiple policy hypotheses. Runtime policy discovery and state augmentation already cover the generic mechanism, so unknown-policy state alone is not novel.

## Self-referential evidence-legitimacy attack
Tests 65–68 examine a stronger circle: evidence E is needed to justify policy P, while release/acquisition of E is governed by P. Without an independently grounded seed, least-fixed-point closure contains neither P nor E; with a seed, the cycle resolves. This collides with established automated-trust-negotiation work on cyclic policy/credential dependencies.

## Rule-validity coupling attack
Tests 69–72 ask whether matched coarse rule-validity marginals plus different world/rule alignment can separate safe resolvability. They cannot under branchwise universal legitimacy: after q=rest, both constructions retain at least one world in which the resolver's rule is invalid. This prevents us from promoting mere correlation between worlds and policy validity as a breakthrough.

## Justification non-equivalence attack
Tests 73–76 match the extensional authorization relation itself: A and B have the same worlds, decisions, q partition, q cost, and `authorized=True` bit. A has a grounded finite proof (`credential -> authorize` with credential as axiom); B has only a self-supporting cycle (`authorize -> support -> authorize`) with no axiom. Least-grounded closure derives authorization only in A. This proves extensional authorization alone is insufficient to certify provenance, but it is not a breakthrough: proof-carrying authorization and formally founded trust-management systems already make proof validity explicit, and general cyclic-proof theory warns that cyclicity alone is not synonymous with invalidity.

## Certificate vs full planner
`certificate_pruning.py` independently instruments full joint-state search. The corrected authorization-cut certificate agrees with full search on parameterized OPEN/BLOCKED witnesses, but its exact check itself performs restricted AND/OR reasoning; no asymptotic advantage is claimed.

## Datasets and empirical boundary
Controlled theorem datasets include `large_authorization_benchmark.csv`, `dynamic_proof_coupling.csv`, `evidence_authority_closure.csv`, `joint_coupling_matched_marginals.csv`, `joint_planning_collision.csv`, `authority_premium.csv`, `legitimate_pair_cut.csv`, `dynamic_authority_cut.csv`, `certificate_planner_comparison.csv`, `ocat_collision.csv`, `policy_uncertainty.csv`, `self_referential_legitimacy.csv`, `rule_validity_coupling.csv`, and `justification_non_equivalence.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks do not natively provide counterfactual proof-acquisition legitimacy labels; we do not fabricate them.

## Test registry
1–40. Previous SAFESEP regression and collision tests retained unchanged.
41–48. Authority-premium and legitimate-pair-cut tests retained.
49–56. Corrected dynamic-cut and full-planner comparison tests retained.
57–60. OCAT collision and 10,000-world stress retained.
61–64. Second-order policy-uncertainty tests retained.
65–68. Self-referential evidence-legitimacy tests retained.
69. Rule-validity cheapest unresolved probe — q, cost 1; 9,900 residual incompatible pairs.
70. Matched coarse rule-validity summaries.
71. Naive world/rule alignment negative result.
72. 10,000-world rule-validity stress — q cost 1; 24,995,000 residual incompatible pairs.
73. **Justification-non-equivalence cheapest unresolved probe** — q, cost 1; 9,900 residual incompatible pairs.
74. **Extensional authorization equality** — same worlds, decisions, q partition, costs, and authorization bit.
75. **Grounded-vs-self-supporting proof separation** — A has grounded authorization; B's unseeded cycle does not derive authorization under least-grounded semantics.
76. **10,000-world justification stress** — q cost 1; 24,995,000 residual incompatible pairs while extensional authorization remains matched.

## Current novelty status
**Do not write the paper yet.** Justification non-equivalence is scientifically relevant but collides with proof-carrying authorization, authorization proof theory, and formally founded trust-management semantics. The next candidate must go beyond proof existence: match ordinary proof existence/proof-graph summaries while differing in whether the proof components can themselves be acquired through a branchwise legitimate evidence policy. That candidate must survive iterative PCA, hidden policy modules, privacy-aware PCA, automated trust negotiation, and full-state epistemic/contingent planning.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.