# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent/epistemic planning, world-dependent applicability, history/provenance authorization, proof-carrying authorization, trust negotiation, runtime access-policy discovery, cyclic credentials, cyclic policy interdependency, recursive authorization/fixed-point closure, dynamic evidence gathering, joint information-authority state representation, minimal credential disclosure, generic cost-sensitive trust negotiation, pair separation, minimum test cover, decision-region edge cutting, generic planning landmarks, generic unavoidable-deadend reasoning, dynamic authorization-state updates, observation-conditioned authority-state transitions, or merely treating the applicable policy identifier as latent state.

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
Tests 65–68 examine a stronger circle: evidence E is needed to justify policy P, while release/acquisition of E is governed by P. Without an independently grounded seed, least-fixed-point closure contains neither P nor E; with a seed, the cycle resolves. The cheapest unresolved experiment is still q, cost 1, leaving 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000 worlds. This also collides with established automated-trust-negotiation work on protected credentials and cyclic policy/credential dependencies, so it is retained as a negative boundary result rather than a breakthrough claim.

## Certificate vs full planner
`certificate_pruning.py` independently instruments full joint-state search. The corrected authorization-cut certificate agrees with full search on parameterized OPEN/BLOCKED witnesses, but its exact check itself performs restricted AND/OR reasoning; no asymptotic advantage is claimed.

## Datasets and empirical boundary
Controlled theorem datasets include `large_authorization_benchmark.csv`, `dynamic_proof_coupling.csv`, `evidence_authority_closure.csv`, `joint_coupling_matched_marginals.csv`, `joint_planning_collision.csv`, `authority_premium.csv`, `legitimate_pair_cut.csv`, `dynamic_authority_cut.csv`, `certificate_planner_comparison.csv`, `ocat_collision.csv`, `policy_uncertainty.csv`, and `self_referential_legitimacy.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks do not natively provide the counterfactual rule-legitimacy/protected-evidence labels required here; we do not fabricate them.

## Test registry
1–40. Previous SAFESEP regression and collision tests retained unchanged.
41. Authority-premium cheapest experiment — q, cost 1; 9,900 residual incompatible pairs.
42. Finite authorization premium — unconstrained 1 versus legitimate 2.
43. Infinite authorization premium under obstruction.
44. 10,000-world authority-premium stress.
45. Legitimate pair-cut cheapest probe.
46. Static uncovered-pair obstruction.
47. Raw-information equality / usable-cover separation.
48. 10,000-world pair-cut stress.
49. Dynamic-cut cheapest probe — q, cost 1, 9,900 residual incompatible pairs.
50. Corrected dynamic mandatory-cut deadlock certificate.
51. Certificate rejection on OPEN system after q grants alpha.
52. 10,000-world dynamic-cut structural stress.
53. Cheapest-probe preservation after CI correction — q, cost 1, 9,900 pairs.
54. Corrected cut semantics regression — BLOCKED certifies; OPEN does not.
55. Certificate/full-planner agreement — parameterized comparison through n=30.
56. 10,000-world certificate/planner structural stress — 24,995,000 residual pairs.
57. OCAT cheapest unresolved probe — q, cost 1; 9,900 residual pairs.
58. Matched initial authority topology.
59. Observation-conditioned topology separation/full-state collision.
60. 10,000-world OCAT structural stress — 24,995,000 residual pairs.
61. Second-order cheapest unresolved probe — q, cost 1; 9,900 residual pairs with two policy hypotheses.
62. Policy-as-latent-state regression.
63. Joint decision/policy uncertainty after q.
64. 10,000-world second-order stress — 24,995,000 residual pairs.
65. **Self-referential cheapest unresolved probe** — q, cost 1; 9,900 residual incompatible pairs.
66. **Unseeded policy/evidence cycle** — least-fixed-point closure does not bootstrap P or E.
67. **External legitimacy seed** — breaks the cycle and restores resolution.
68. **10,000-world self-reference stress** — q cost 1; 24,995,000 residual incompatible pairs.

## Current novelty status
**Do not write the paper yet.** Self-referential evidence legitimacy in the simple P↔E form collides directly with established cyclic credential/policy dependencies in automated trust negotiation and recursive trust management. The next candidate must match dependency graph, SCCs, least-fixed-point closure, costs, and ordinary information partitions while differing in safe separability because the validity of the justification rule itself is world-dependent. That candidate must survive nonmonotonic authorization logics, policy-combining/conflict semantics, epistemic planning, and trust negotiation.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.