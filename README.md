# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, conformant/contingent/epistemic planning, possible-world/belief-state authorization semantics, universal belief-state action applicability, world-dependent applicability, history/provenance authorization, proof-carrying authorization, iterative proof-component fetching, trust negotiation, cost-sensitive credential/policy disclosure, credential-disclosure sequences, runtime access-policy discovery, cyclic credentials, recursive authorization/fixed-point closure, joint information-authority state representation, minimal credential disclosure, pair separation, decision-region edge cutting, dynamic authorization-state updates, latent policy identity, generic context-dependent rule validity, grounded-vs-unsupported circular proofs, ordinary protected proof-component acquisition, planning abstraction loss, generic k-wise indistinguishability, generic local-vs-global consistency gaps, or generic set-cover/minimal-cover reductions in access control.

## Structural results retained
Matched information/authority marginals do not determine joint resolvability, but full joint-state planning can encode the missing alignment. The authorization-safe evidence premium quantifies extra legitimate cost. Static pair cuts reduce to test-cover/DRD structure after filtering unavailable tests.

## Dynamic branch-relative authorization cut — corrected twice
Let joint state be `S=(C,A)` and let `K` be a candidate mandatory probe set. A sufficient certificate is: (1) after removing K, no complete resolving policy exists; and (2) in every decision-critical joint state reachable without K, every probe in K is unauthorized. Then no legitimate resolving policy exists. An earlier stronger root-pair condition failed CI and was corrected rather than hidden. Tests 85–86 add a second soundness correction: one-outcome probes must still be explored when they change authority state. A credential-fetch action can leave C unchanged while granting a token that unlocks K; only true no-ops may be skipped.

## Branchwise universal-admissibility, CLE, and premium
Tests 87–98 isolate and quantify common legitimacy. They establish finite/infinite CLE and an exact unbounded authorization-legitimacy premium, but these are not alone novelty claims because belief-state planning and cost-sensitive trust negotiation cover universal applicability and weighted disclosure.

## Matched-cost branchwise coupling attack
Tests 99–102 remove trivial cost padding: matched systems have the same worlds, decisions, raw experiment partitions, costs, action counts, unconstrained optimum, and local legitimate witnesses, yet differ in existence of a branchwise-common resolver. Full joint-state planning can still encode the incidence relation, so this remains a structural witness rather than the final breakthrough.

## Legitimate incompatible-pair cover certificate
Tests 103–106 define a semantic certificate over incompatible decision pairs. At branch C, only experiments legitimate in every compatible world may cover/separate pairs. If none separates any incompatible pair, C is immediately obstructed. A coarse lower bound is `ceil(|P|/max_cover)*min_cost`. The matched A/B witness has identical worlds, decisions, experiment costs and raw outcome partitions; after q=rest, A has a legitimate pair-separating resolver while B has none. This certificate is representation-independent with respect to planner encoding, but generic set/minimal-cover reductions are already established in RBAC and access-control testing. The next target must make the certificate dynamic under authority-changing transitions rather than claim generic covering novelty. See `results/LEGITIMATE_PAIR_COVER_BOUND.md`.

## Datasets and empirical boundary
Controlled theorem datasets include the prior SAFESEP stress suites plus `matched_coupling_premium.csv` and `legitimate_pair_cover_bound.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks do not natively provide counterfactual world×experiment legitimacy or authority-transition semantics; we do not fabricate such labels.

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
95–98. Unbounded authorization-legitimacy premium retained.
99–102. Matched-cost branchwise coupling attack retained.
103. **Pair-cover cheapest unresolved probe** — q, cost 1; 9,900 residual incompatible pairs at 200 worlds.
104. **Semantic pair-cover obstruction** — after q=rest, A has finite pair-separating cover while B has no branchwise-legitimate pair separator.
105. **Encoding-independence regression** — A/B match raw outcome partitions and costs; legitimacy-filtered pair cover alone separates them.
106. **10,000-world analytic stress** — q cost 1; 24,995,000 residual incompatible pairs without quadratic pair materialization.

## Current novelty status
**Do not write the paper yet.** Tests 103–106 produce the requested representation-independent semantic obstruction, but the static covering core collides with established set-cover/minimal-cover work in authorization and policy testing. The strongest next stop-and-write candidate is a **dynamic legitimate-pair-flow theorem**: pair-separation capacity can be created only by authority-changing transitions, and every safe resolving policy must transport all incompatible-pair mass through legitimate authority states. A nontrivial lower bound or conservation/cut theorem here could survive the generic static-cover collision.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.