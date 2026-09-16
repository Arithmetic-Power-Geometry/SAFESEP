# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, conformant/contingent/epistemic planning, possible-world/belief-state authorization semantics, universal belief-state action applicability, world-dependent applicability, history/provenance authorization, proof-carrying authorization, iterative proof-component fetching, trust negotiation, cost-sensitive credential/policy disclosure, credential-disclosure sequences, runtime access-policy discovery, cyclic credentials, recursive authorization/fixed-point closure, joint information-authority state representation, minimal credential disclosure, pair separation, decision-region edge cutting, dynamic authorization-state updates, latent policy identity, generic context-dependent rule validity, grounded-vs-unsupported circular proofs, ordinary protected proof-component acquisition, planning abstraction loss, generic k-wise indistinguishability, or generic local-vs-global consistency gaps.

## Structural results retained
Matched information/authority marginals do not determine joint resolvability, but full joint-state planning can encode the missing alignment. The authorization-safe evidence premium quantifies extra legitimate cost. Static pair cuts reduce to test-cover/DRD structure after filtering unavailable tests.

## Dynamic branch-relative authorization cut — corrected twice
Let joint state be `S=(C,A)` and let `K` be a candidate mandatory probe set. A sufficient certificate is: (1) after removing K, no complete resolving policy exists; and (2) in every decision-critical joint state reachable without K, every probe in K is unauthorized. Then no legitimate resolving policy exists. An earlier stronger root-pair condition failed CI and was corrected rather than hidden. Tests 85–86 add a second soundness correction: one-outcome probes must still be explored when they change authority state. A credential-fetch action can leave C unchanged while granting a token that unlocks K; only true no-ops may be skipped.

## Collision sequence
Tests 57–60: observation-conditioned authority topology is representable by full-state planning. Tests 61–64: latent policy identity collides with runtime policy discovery/state augmentation. Tests 65–68: simple self-referential evidence legitimacy collides with cyclic trust negotiation. Tests 69–72: coarse world/rule-validity alignment is insufficient under universal branch legitimacy. Tests 73–76: grounded-vs-self-supporting proof differences collide with proof-carrying authorization/proof theory. Tests 77–80: protected proof-component acquisition collides with PCA/trust negotiation/augmented planning. Tests 81–84: an imposed bounded summary gives a hierarchy shape but not a natural authorization theorem.

## Token-only transition soundness
Tests 85–86 repair a general planner/certificate bug: authority progress does not require information gain. A one-outcome credential fetch that grants `alpha` is now explored, so a resolver requiring `alpha` is correctly recognized as reachable. A one-outcome action changing neither worlds nor tokens is skipped to avoid loops. See `results/TOKEN_ONLY_TRANSITION_SOUNDNESS.md`.

## Branchwise universal-admissibility gap and CLE
Tests 87–94 isolate and quantify the common-legitimacy requirement. A/B can match per-world resolver availability while only A has a resolver legitimate throughout the unresolved branch. `CLE(C)` is the minimum cost of an informative experiment legitimate in every world of a decision-critical branch; matched A has finite CLE while B can have CLE=infinity. This remains a diagnostic rather than a novelty claim because belief-state planning already requires universal applicability.

## Unbounded authorization-legitimacy premium
Tests 95–98 define U_n as unconstrained decision-resolution cost and S_n as authorization-safe cost. In the controlled family, U_n=1, S_n=n+1, so Lambda_n=S_n-U_n=n is unbounded. At 10,000 worlds (n=5000), q costs 1 and leaves 24,995,000 incompatible pairs; U=1, S=5001, Lambda=5000. This quantitative shape is reproducible but is **not yet promoted to breakthrough**: cost-sensitive trust negotiation already optimizes weighted credential/policy disclosure, and conformant planning already supports cost-bearing universally applicable action sequences. The next target is a matched-cost irreducibility theorem where the gap is caused by branchwise authorization coupling rather than by inserting n mandatory token acquisitions. See `results/UNBOUNDED_LEGITIMACY_PREMIUM.md`.

## Datasets and empirical boundary
Controlled theorem datasets include `large_authorization_benchmark.csv`, `dynamic_proof_coupling.csv`, `evidence_authority_closure.csv`, `joint_coupling_matched_marginals.csv`, `joint_planning_collision.csv`, `authority_premium.csv`, `legitimate_pair_cut.csv`, `dynamic_authority_cut.csv`, `certificate_planner_comparison.csv`, `ocat_collision.csv`, `policy_uncertainty.csv`, `self_referential_legitimacy.csv`, `rule_validity_coupling.csv`, `justification_non_equivalence.csv`, `acquisition_path_coupling.csv`, `bounded_summary_hierarchy.csv`, `branchwise_universal_gap.csv`, `common_legitimate_evidence.csv`, and `unbounded_legitimacy_premium.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks do not natively provide counterfactual legitimacy of every evidence/action-acquisition path in every compatible world; we do not fabricate such labels.

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
85–86. Token-only transition soundness corrections retained.
87–90. Branchwise universal-admissibility gap retained.
91–94. Common Legitimate Evidence obstruction retained.
95. **Unbounded-premium cheapest unresolved probe** — q, cost 1; 9,900 residual incompatible pairs at 200 worlds.
96. **Exact linear premium theorem regression** — for n=2..128, U_n=1, S_n=n+1, Lambda_n=n.
97. **Unboundedness regression** — Lambda_n strictly grows across n=2,4,...,256.
98. **10,000-world premium stress** — q leaves 24,995,000 incompatible pairs; U=1, S=5001, Lambda=5000.

## Current novelty status
**Do not write the paper yet.** Tests 95–98 establish an exact unbounded quantitative gap, but the present lower bound is construction-driven: n mandatory legitimate token acquisitions trivially create linear cost. Cost-sensitive trust negotiation already studies minimum disclosure cost, including NP-complete formulations, and conformant planning already handles universally applicable action sequences. The next stop-and-write candidate is matched-cost irreducibility: same action costs, same token counts, same per-world acquisition lengths and same unconstrained planner optimum, yet SAFESEP branchwise legitimacy alone yields a growing or infinite separation.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.