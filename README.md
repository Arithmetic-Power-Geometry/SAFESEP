# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent/epistemic planning, world-dependent applicability, history/provenance authorization, proof-carrying authorization, trust negotiation, runtime access-policy discovery, cyclic credentials, cyclic policy interdependency, recursive authorization/fixed-point closure, dynamic evidence gathering, joint information-authority state representation, minimal credential disclosure, generic cost-sensitive trust negotiation, pair separation, minimum test cover, decision-region edge cutting, generic planning landmarks, generic unavoidable-deadend reasoning, dynamic authorization-state updates, observation-conditioned authority-state transitions, latent policy identity, or generic context-dependent/nonmonotonic rule validity.

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
Tests 69–72 ask whether matched coarse rule-validity marginals plus different world/rule alignment can separate safe resolvability. They cannot under branchwise universal legitimacy: after q=rest, both constructions retain at least one world in which the resolver's rule is invalid. This is a useful negative result because it prevents us from promoting mere correlation between worlds and policy validity as a breakthrough. Context-dependent, incomplete, conflicting and nonmonotonic authorization policies are already established.

## Certificate vs full planner
`certificate_pruning.py` independently instruments full joint-state search. The corrected authorization-cut certificate agrees with full search on parameterized OPEN/BLOCKED witnesses, but its exact check itself performs restricted AND/OR reasoning; no asymptotic advantage is claimed.

## Datasets and empirical boundary
Controlled theorem datasets include `large_authorization_benchmark.csv`, `dynamic_proof_coupling.csv`, `evidence_authority_closure.csv`, `joint_coupling_matched_marginals.csv`, `joint_planning_collision.csv`, `authority_premium.csv`, `legitimate_pair_cut.csv`, `dynamic_authority_cut.csv`, `certificate_planner_comparison.csv`, `ocat_collision.csv`, `policy_uncertainty.csv`, `self_referential_legitimacy.csv`, and `rule_validity_coupling.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks do not natively provide counterfactual world-indexed rule-validity or justification labels; we do not fabricate them.

## Test registry
1–40. Previous SAFESEP regression and collision tests retained unchanged.
41–48. Authority-premium and legitimate-pair-cut tests retained.
49–56. Corrected dynamic-cut and full-planner comparison tests retained.
57. OCAT cheapest unresolved probe — q, cost 1; 9,900 residual pairs.
58. Matched initial authority topology.
59. Observation-conditioned topology separation/full-state collision.
60. 10,000-world OCAT structural stress — 24,995,000 residual pairs.
61. Second-order cheapest unresolved probe — q, cost 1; 9,900 residual pairs with two policy hypotheses.
62. Policy-as-latent-state regression.
63. Joint decision/policy uncertainty after q.
64. 10,000-world second-order stress — 24,995,000 residual pairs.
65. Self-referential cheapest unresolved probe — q, cost 1; 9,900 residual incompatible pairs.
66. Unseeded policy/evidence cycle — least-fixed-point closure does not bootstrap P or E.
67. External legitimacy seed — breaks the cycle and restores resolution.
68. 10,000-world self-reference stress — q cost 1; 24,995,000 residual incompatible pairs.
69. **Rule-validity cheapest unresolved probe** — q, cost 1; 9,900 residual incompatible pairs.
70. **Matched coarse rule-validity summaries** — same worlds, decisions, q partition, costs, and validity counts.
71. **Naive world/rule alignment negative result** — neither matched construction satisfies branchwise universal legitimacy.
72. **10,000-world rule-validity stress** — q cost 1; 24,995,000 residual incompatible pairs with matched validity marginals.

## Current novelty status
**Do not write the paper yet.** Simple world-dependent rule validity is both already represented in context-dependent/nonmonotonic authorization and insufficient to create our desired matched-system separation under SAFESEP's universal branch legitimacy. The next candidate is justification non-equivalence: systems that agree extensionally on authorization decisions, policy validity marginals, dependency graphs and information partitions but differ in whether the same authorization conclusion has a non-circular admissible justification. This must survive argumentation/nonmonotonic proof semantics, proof-carrying authorization, provenance, trust management and epistemic planning.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.