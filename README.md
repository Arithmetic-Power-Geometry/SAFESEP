# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, contingent/epistemic planning, possible-world/belief-state authorization semantics, world-dependent applicability, history/provenance authorization, proof-carrying authorization, iterative proof-component fetching, trust negotiation, credential-disclosure sequences, runtime access-policy discovery, cyclic credentials, recursive authorization/fixed-point closure, joint information-authority state representation, minimal credential disclosure, pair separation, decision-region edge cutting, dynamic authorization-state updates, latent policy identity, generic context-dependent rule validity, grounded-vs-unsupported circular proofs, ordinary protected proof-component acquisition, planning abstraction loss, generic k-wise indistinguishability, or generic local-vs-global consistency gaps.

## Structural results retained
Matched information/authority marginals do not determine joint resolvability, but full joint-state planning can encode the missing alignment. The authorization-safe evidence premium quantifies extra legitimate cost. Static pair cuts reduce to test-cover/DRD structure after filtering unavailable tests.

## Dynamic branch-relative authorization cut — corrected twice
Let joint state be `S=(C,A)` and let `K` be a candidate mandatory probe set. A sufficient certificate is: (1) after removing K, no complete resolving policy exists; and (2) in every decision-critical joint state reachable without K, every probe in K is unauthorized. Then no legitimate resolving policy exists. An earlier stronger root-pair condition failed CI and was corrected rather than hidden. Tests 85–86 add a second soundness correction: one-outcome probes must still be explored when they change authority state. A credential-fetch action can leave C unchanged while granting a token that unlocks K; only true no-ops may be skipped.

## Collision sequence
Tests 57–60: observation-conditioned authority topology is representable by full-state planning. Tests 61–64: latent policy identity collides with runtime policy discovery/state augmentation. Tests 65–68: simple self-referential evidence legitimacy collides with cyclic trust negotiation. Tests 69–72: coarse world/rule-validity alignment is insufficient under universal branch legitimacy. Tests 73–76: grounded-vs-self-supporting proof differences collide with proof-carrying authorization/proof theory. Tests 77–80: protected proof-component acquisition collides with PCA/trust negotiation/augmented planning. Tests 81–84: an imposed bounded summary gives a hierarchy shape but not a natural authorization theorem.

## Token-only transition soundness
Tests 85–86 repair a general planner/certificate bug: authority progress does not require information gain. A one-outcome credential fetch that grants `alpha` is now explored, so a resolver requiring `alpha` is correctly recognized as reachable. A one-outcome action changing neither worlds nor tokens is skipped to avoid loops. See `results/TOKEN_ONLY_TRANSITION_SOUNDNESS.md`.

## Branchwise universal-admissibility gap
Tests 87–90 match A/B on worlds, decisions, q partition/cost, and the per-world fact that every world individually has a cost-1 resolving witness. A uses one resolver uniformly across the unresolved branch; B has only world-specific resolver witnesses, so no single action is executable throughout the still-compatible branch. A resolves after q=rest and B does not. This precisely isolates the branchwise universal requirement, but is not yet promoted to breakthrough novelty: possible-world authorization semantics and full belief-state/contingent planning can represent the complete world-action relation.

## Datasets and empirical boundary
Controlled theorem datasets include `large_authorization_benchmark.csv`, `dynamic_proof_coupling.csv`, `evidence_authority_closure.csv`, `joint_coupling_matched_marginals.csv`, `joint_planning_collision.csv`, `authority_premium.csv`, `legitimate_pair_cut.csv`, `dynamic_authority_cut.csv`, `certificate_planner_comparison.csv`, `ocat_collision.csv`, `policy_uncertainty.csv`, `self_referential_legitimacy.csv`, `rule_validity_coupling.csv`, `justification_non_equivalence.csv`, `acquisition_path_coupling.csv`, `bounded_summary_hierarchy.csv`, and `branchwise_universal_gap.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks do not natively provide counterfactual legitimacy of every evidence action in every compatible possible world; we do not fabricate such labels.

## Test registry
1–40. Previous SAFESEP regression and collision tests retained unchanged.
41–48. Authority-premium and legitimate-pair-cut tests retained.
49–56. Corrected dynamic-cut and full-planner comparison tests retained.
57–60. OCAT collision and 10,000-world stress retained.
61–64. Second-order policy-uncertainty tests retained.
65–68. Self-referential evidence-legitimacy tests retained.
69–72. Rule-validity coupling tests retained.
73–76. Justification non-equivalence tests retained.
77–80. Acquisition-path coupling tests retained.
81–84. Bounded-summary hierarchy attack retained.
85. Token-only credential transition soundness — one-outcome credential fetch grants alpha; certificate rejects false obstruction and full search resolves.
86. True no-op loop regression — one-outcome action granting nothing is skipped safely.
87. **Branchwise-gap cheapest unresolved probe** — q, cost 1; 9,900 residual incompatible pairs at 200 worlds.
88. **Matched per-world resolver summaries** — every world in A/B individually has a cost-1 resolver witness.
89. **Uniform branchwise separation** — A has one common resolver and resolves; B has only world-specific witnesses and blocks while uncertainty remains.
90. **10,000-world branchwise stress** — q cost 1; 24,995,000 residual incompatible pairs with matched per-world summaries.

## Current novelty status
**Do not write the paper yet.** Tests 87–90 isolate a natural SAFESEP property rather than an artificial summary, but full possible-world/belief-state formalisms can encode it. The next stop-and-write candidate should quantify the minimum branchwise common legitimate evidence needed to separate decision classes and prove an authorization-specific lower bound, hierarchy, or compact obstruction that survives comparison with full-state planning, test cover/DRD, authorization logic, and trust negotiation.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.