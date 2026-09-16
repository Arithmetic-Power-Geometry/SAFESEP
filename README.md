# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent/epistemic planning, world-dependent applicability, history/provenance authorization, proof-carrying authorization, iterative proof-component fetching, trust negotiation, credential-disclosure sequences, runtime access-policy discovery, cyclic credentials, recursive authorization/fixed-point closure, joint information-authority state representation, minimal credential disclosure, pair separation, decision-region edge cutting, dynamic authorization-state updates, latent policy identity, generic context-dependent rule validity, grounded-vs-unsupported circular proofs, or ordinary protected proof-component acquisition.

## Structural results retained
Matched information/authority marginals do not determine joint resolvability, but full joint-state planning can encode the missing alignment. The authorization-safe evidence premium quantifies extra legitimate cost. Static pair cuts reduce to test-cover/DRD structure after filtering unavailable tests.

## Dynamic branch-relative authorization cut — corrected
Let joint state be `S=(C,A)` and let `K` be a candidate mandatory probe set. A sufficient certificate is: (1) after removing K, no complete resolving policy exists; and (2) in every decision-critical joint state reachable without K, every probe in K is unauthorized. Then no legitimate resolving policy exists. An earlier stronger root-pair condition failed CI and was corrected rather than hidden.

## Collision sequence
Tests 57–60: observation-conditioned authority topology is representable by full-state planning. Tests 61–64: latent policy identity collides with runtime policy discovery/state augmentation. Tests 65–68: simple self-referential evidence legitimacy collides with cyclic trust negotiation. Tests 69–72: coarse world/rule-validity alignment is insufficient under universal branch legitimacy. Tests 73–76: grounded-vs-self-supporting proof differences collide with proof-carrying authorization/proof theory.

## Proof-component acquisition-path coupling
Tests 77–80 go beyond ordinary proof existence. A and B have the same worlds, decisions, q partition, q cost, ordinary proof existence, proof-component count, and coarse proof graph. After q=rest, A can obtain the required proof component through an independently legitimate route; B's only acquisition route presupposes the resolver authorization that component is meant to justify. Hence A resolves and B blocks. Nevertheless this is retained as a collision boundary, not a breakthrough: PCA already iteratively fetches distributed proof components and automated trust negotiation already searches policy-protected credential disclosure sequences. A complete acquisition state can also be represented in an augmented planner.

## Datasets and empirical boundary
Controlled theorem datasets include `large_authorization_benchmark.csv`, `dynamic_proof_coupling.csv`, `evidence_authority_closure.csv`, `joint_coupling_matched_marginals.csv`, `joint_planning_collision.csv`, `authority_premium.csv`, `legitimate_pair_cut.csv`, `dynamic_authority_cut.csv`, `certificate_planner_comparison.csv`, `ocat_collision.csv`, `policy_uncertainty.csv`, `self_referential_legitimacy.csv`, `rule_validity_coupling.csv`, `justification_non_equivalence.csv`, and `acquisition_path_coupling.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks do not natively provide counterfactual proof-component acquisition legitimacy for every compatible world; we do not fabricate it.

## Test registry
1–40. Previous SAFESEP regression and collision tests retained unchanged.
41–48. Authority-premium and legitimate-pair-cut tests retained.
49–56. Corrected dynamic-cut and full-planner comparison tests retained.
57–60. OCAT collision and 10,000-world stress retained.
61–64. Second-order policy-uncertainty tests retained.
65–68. Self-referential evidence-legitimacy tests retained.
69–72. Rule-validity coupling tests retained.
73. Justification-non-equivalence cheapest unresolved probe — q, cost 1; 9,900 residual pairs.
74. Extensional authorization equality.
75. Grounded-vs-self-supporting proof separation.
76. 10,000-world justification stress — 24,995,000 residual pairs.
77. **Acquisition-path cheapest unresolved probe** — q, cost 1; 9,900 residual incompatible pairs.
78. **Matched ordinary proof structure** — same proof existence, proof component count, and coarse proof graph.
79. **Legitimate acquisition-path separation** — A obtains the component independently and resolves; B's acquisition presupposes resolver authority and blocks.
80. **10,000-world acquisition-path stress** — q cost 1; 24,995,000 residual incompatible pairs with matched ordinary proof structure.

## Current novelty status
**Do not write the paper yet.** Tests 77–80 strengthen the witness, but iterative PCA and automated trust negotiation already model fetching protected proof/credential components, and augmented planning can represent acquisition state. The next stop-and-write candidate must establish an authorization-specific irreducibility or lower-bound result that survives a full representation of acquisition state and policies—for example, a hierarchy showing that bounded-order/local authorization summaries cannot determine safe separability even when ordinary proof and acquisition graphs are matched.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.