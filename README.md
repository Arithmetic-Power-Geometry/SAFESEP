# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent/epistemic planning, world-dependent applicability, history/provenance authorization, proof-carrying authorization, trust negotiation, cyclic credentials, recursive authorization, dynamic evidence gathering, joint information-authority state representation, minimal credential disclosure, generic cost-sensitive trust negotiation, pair separation, minimum test cover, decision-region edge cutting, generic planning landmarks, generic unavoidable-deadend reasoning, dynamic authorization-state updates, or observation-conditioned authority-state transitions.

## Structural results retained
Matched information/authority marginals do not determine joint resolvability, but full joint-state planning can encode the missing alignment. The authorization-safe evidence premium quantifies extra legitimate cost, but disclosure-cost optimization is established. Static pair cuts reduce to test-cover/DRD structure after filtering unavailable tests.

## Dynamic branch-relative authorization cut — corrected
Let joint state be `S=(C,A)` and let `K` be a candidate mandatory probe set. The corrected sufficient certificate is:

1. after removing K, **no complete resolving policy exists** (non-cut probes may still resolve some branches); and
2. in every decision-critical joint state reachable without K, every probe in K is unauthorized.

Then no legitimate resolving policy exists: a successful policy would require a first use of K, but no such first use is executable.

### CI-discovered scientific correction
The first implementation incorrectly required every incompatible root pair to be separable only by K. GitHub CI rejected Tests 49–52. That condition was too strong because q can separate some incompatible pairs while every complete policy still requires r on the residual branch. The code and theorem statement were corrected to exact restricted AND/OR semantics. The failure is documented in `results/CERTIFICATE_VS_PLANNER.md` rather than hidden.

## Observation-Conditioned Authority Topology attack
Tests 57–60 strengthen the matched witness so that the two systems have the same initial worlds, decisions, cheapest unresolved probe, cost, and initial authority graph. Observation `q=rest` activates an authority edge in A but not B, yielding A=RESOLVABLE and B=BLOCKED. This establishes that initial authority topology alone is insufficient. However, a full-state contingent planner represents the active edge as state and reproduces the separation exactly. Dynamic authorization literature also permits authorization state to change with actions/context. Therefore OCAT is retained as a negative/collision result, not a breakthrough claim.

## Certificate vs full planner
`certificate_pruning.py` independently instruments full joint-state search. The corrected authorization-cut certificate agrees with full search on the parameterized OPEN/BLOCKED witnesses. However, the current mandatory-cut test itself performs restricted AND/OR reasoning. Therefore **no asymptotic complexity advantage is claimed**. This collision is consistent with established strong contingent planning, unavoidable-deadend analysis, and landmark-guided contingent planning.

## Datasets and empirical boundary
Controlled theorem datasets include `large_authorization_benchmark.csv`, `dynamic_proof_coupling.csv`, `evidence_authority_closure.csv`, `joint_coupling_matched_marginals.csv`, `joint_planning_collision.csv`, `authority_premium.csv`, `legitimate_pair_cut.csv`, `dynamic_authority_cut.csv`, `certificate_planner_comparison.csv`, and `ocat_collision.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. AuthBench remains real external-validity evidence, but it does not natively provide the counterfactual world×probe outcomes plus legitimate-executability/proof/authority-transition labels required by these theorems; we do not fabricate them.

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
53. **Cheapest-probe preservation after CI correction** — q, cost 1, 9,900 pairs.
54. **Corrected cut semantics regression** — BLOCKED certifies; OPEN does not.
55. **Certificate/full-planner agreement** — parameterized comparison through n=30.
56. **10,000-world certificate/planner structural stress** — 24,995,000 residual incompatible pairs with scale-invariant obstruction.
57. **OCAT cheapest unresolved probe** — q, cost 1; 9,900 residual incompatible pairs.
58. **Matched initial authority topology** — A/B initial graph and structural signature identical.
59. **Observation-conditioned topology separation/full-state collision** — A resolves, B blocks, while full-state representation captures the difference.
60. **10,000-world OCAT structural stress** — q remains cost 1 with 24,995,000 residual incompatible pairs.

## Current novelty status
**Do not write the paper yet.** OCAT proves that initial authority topology is insufficient, but the effect is representable by ordinary full-state planning and overlaps established dynamic authorization-state updates. The next stop-and-write target is second-order: the agent must determine which authority-transition rule is legitimate, while the evidence needed to determine that rule may itself require authority that differs across still-compatible worlds. Any theorem here must survive epistemic/contingent planning, dynamic authorization, trust negotiation, and policy-information-acquisition prior art.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.