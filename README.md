# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, conformant/contingent/epistemic planning, possible-world/belief-state authorization semantics, universal belief-state action applicability, world-dependent applicability, history/provenance authorization, proof-carrying authorization, iterative proof-component fetching, trust negotiation, cost-sensitive credential/policy disclosure, credential-disclosure sequences, runtime access-policy discovery, cyclic credentials, recursive authorization/fixed-point closure, joint information-authority state representation, minimal credential disclosure, pair separation, decision-region edge cutting, dynamic authorization-state updates, latent policy identity, generic context-dependent rule validity, grounded-vs-unsupported circular proofs, ordinary protected proof-component acquisition, planning abstraction loss, generic k-wise indistinguishability, generic local-vs-global consistency gaps, generic set-cover/minimal-cover reductions, or generic planning cuts/dead-end reasoning.

## Structural results retained
Matched information/authority marginals do not determine joint resolvability, but full joint-state planning can encode the missing alignment. The authorization-safe evidence premium quantifies extra legitimate cost. Static pair cuts reduce to test-cover/DRD structure after filtering unavailable tests.

## Dynamic branch-relative authorization cut — corrected twice
Let joint state be `S=(C,A)` and let `K` be a candidate mandatory probe set. A sufficient certificate is: (1) after removing K, no complete resolving policy exists; and (2) in every decision-critical joint state reachable without K, every probe in K is unauthorized. Then no legitimate resolving policy exists. Tests 85–86 repaired token-only transition soundness: authority progress does not require information gain.

## Branchwise universal-admissibility, CLE, premium, and matched coupling
Tests 87–102 isolate common legitimacy, quantify finite/infinite CLE and an unbounded authorization-legitimacy premium, then remove trivial cost padding with matched-cost A/B systems. These are strong structural witnesses but full joint-state planning/trust negotiation can encode their complete incidence relations.

## Legitimate incompatible-pair cover certificate
Tests 103–106 define a semantic incompatible-pair cover certificate. Static pair cover is useful but collides with established set/minimal-cover methods, so it is retained as a baseline rather than promoted to breakthrough.

## Dynamic legitimate-pair-flow attack
Tests 107–122 make the certificate dynamic over joint states `(C,A)`. Probe `k` perfectly resolves R/W but requires token `alpha`; OPEN and BLOCKED match worlds, decisions, raw information maps, action names/costs, and initial illegitimacy of `k`. Their one-outcome `fetch` actions are information-identical: OPEN grants `alpha`, BLOCKED is a true no-op. The cut K={k} is blocked exactly when every decision-critical joint state reachable without K keeps k illegitimate. This directly checks token-only authority transitions and scales through 10,000 controlled worlds. It is a SAFESEP-specific semantic certificate, not yet a claim that dynamic cuts or joint-state planning are new. See `results/DYNAMIC_PAIR_FLOW_ATTACK.md`.

## Datasets and empirical boundary
Controlled theorem datasets include the prior SAFESEP stress suites plus `matched_coupling_premium.csv`, `legitimate_pair_cover_bound.csv`, and `dynamic_pair_flow.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks do not natively provide counterfactual world×experiment legitimacy and token-yield semantics; we do not fabricate such labels.

## Test registry
1–40. Previous SAFESEP regression and collision tests retained unchanged.
41–84. Prior premium, pair-cut, dynamic-cut, OCAT, policy uncertainty, self-reference, rule-validity, proof/acquisition and bounded-summary tests retained.
85–86. Token-only transition soundness corrections retained.
87–90. Branchwise universal-admissibility gap retained.
91–94. Common Legitimate Evidence obstruction retained.
95–98. Unbounded authorization-legitimacy premium retained.
99–102. Matched-cost branchwise coupling attack retained.
103–106. Legitimate incompatible-pair cover certificate retained.
107. **Dynamic-flow cheapest unresolved OPEN** — q cost 1; 9,900 residual incompatible pairs at 200 worlds.
108. **Dynamic-flow cheapest unresolved BLOCKED** — same q/cost/pair count.
109. **Blocked dynamic-cut certificate** — K={k} remains illegitimate in all reachable critical states without K.
110. **Token-only escape regression** — OPEN fetch grants alpha without information gain, so K is not blocked.
111. **Cheapest-probe parameter sweep** — n=2..64 preserves q cost 1 and n(n-1) worst residual pairs.
112. **Dynamic-cut parameter sweep** — n=2..64 separates BLOCKED from OPEN.
113. **Authority-only reachability** — OPEN reaches token alpha with unchanged compatible-world set.
114. **True no-op regression** — BLOCKED fetch creates no spurious authority state.
115. **Raw-information matching** — OPEN/BLOCKED match probe names, costs, outcomes and requirements.
116. **Action-cost matching** — both have exactly three unit-cost actions.
117. **Authority-flow isolation** — only fetch token yield differs.
118. **Initial resolver illegitimacy** — k is initially unavailable in both cases.
119. **1,000-world stress** — q leaves 249,500 incompatible pairs.
120. **2,000-world stress** — q leaves 999,000 incompatible pairs.
121. **5,000-world stress** — q leaves 6,247,500 incompatible pairs.
122. **10,000-world analytic stress** — q cost 1; 24,995,000 residual incompatible pairs.

## Current novelty status
**Do not write the paper yet.** The dynamic certificate survives the static-cover weakness and correctly handles authority-only transitions, but automated trust negotiation already supports incremental protected credential/policy disclosure and cyclic dependencies, while contingent planning can encode joint state transitions. The next stop-and-write candidate is a quantitative **authorization pair-flow lower bound/conservation theorem** under a restricted authorization language: bound the decision-incompatibility that can be eliminated per legitimately acquired authority unit, and prove a family where the bound is tight or asymptotically separates safe authorization from ordinary information/planning cost without artificial cost padding.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.