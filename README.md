# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Across current constructions the diagnostic remains `q`, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, conformant/contingent/epistemic planning, possible-world/belief-state authorization semantics, universal belief-state action applicability, world-dependent applicability, history/provenance authorization, proof-carrying authorization, iterative proof-component fetching, trust negotiation, cost-sensitive credential/policy disclosure, credential-disclosure sequences, runtime access-policy discovery, cyclic credentials, recursive authorization/fixed-point closure, joint information-authority state representation, minimal credential disclosure, pair separation, decision-region edge cutting, dynamic authorization-state updates, latent policy identity, generic context-dependent rule validity, grounded-vs-unsupported circular proofs, ordinary protected proof-component acquisition, planning abstraction loss, generic k-wise indistinguishability, generic local-vs-global consistency gaps, generic set-cover/minimal-cover reductions, generic planning cuts/dead-end reasoning, or generic pair-counting/cover lower bounds.

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

## Authorization pair-flow lower-bound attack
Tests 123–138 define incompatible-pair mass `M(C)` and worst-branch legitimate pair reduction `Delta_e(C)=M(C)-max_o M(C_e,o)`. They test a local counting lower bound, exact pair formulas, illegitimate/no-op filtering, perfect resolution, invariances, cost scaling, parameter sweeps, and 10,000-world stress. A scientifically important limitation is retained: a root-only capacity ceiling is not a general dynamic SAFESEP theorem because authority-changing transitions may unlock later high-capacity actions. The next theorem must therefore use a state-dependent potential or a cut over reachable joint states. See `results/PAIR_FLOW_LOWER_BOUND.md`.

## Datasets and empirical boundary
Controlled theorem datasets include the prior SAFESEP stress suites plus `matched_coupling_premium.csv`, `legitimate_pair_cover_bound.csv`, `dynamic_pair_flow.csv`, and `pair_flow_bound.csv`, scaling through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks do not natively provide counterfactual world×experiment legitimacy and authority-transition semantics; we do not fabricate such labels.

## Test registry
1–40. Previous SAFESEP regression and collision tests retained unchanged.
41–84. Prior premium, pair-cut, dynamic-cut, OCAT, policy uncertainty, self-reference, rule-validity, proof/acquisition and bounded-summary tests retained.
85–86. Token-only transition soundness corrections retained.
87–90. Branchwise universal-admissibility gap retained.
91–94. Common Legitimate Evidence obstruction retained.
95–98. Unbounded authorization-legitimacy premium retained.
99–102. Matched-cost branchwise coupling attack retained.
103–106. Legitimate incompatible-pair cover certificate retained.
107–122. Dynamic legitimate-pair-flow battery retained.
123. **Zero pair-mass boundary** — decision-homogeneous branch has zero lower bound.
124. **Exact binary pair mass** — 200 worlds give 10,000 incompatible root pairs.
125. **Cheapest unresolved diagnostic** — q cost 1 leaves 9,900 incompatible pairs at 200 worlds.
126. **Exact q pair reduction** — q removes exactly 100 pairs in its worst branch at n=100.
127. **Illegitimate-probe capacity** — non-universal probe contributes zero safe pair-flow capacity.
128. **True no-op capacity** — information-free no-op contributes zero pair reduction.
129. **Perfect resolver capacity** — universally legitimate perfect resolver removes all incompatible pairs.
130. **Perfect-resolver lower bound** — one step, exact action cost.
131. **No-progress obstruction** — no legitimate progress implies infinite local bound.
132. **Partition monotonicity sweep** — incompatible-pair mass never increases under observation partition, n=2..64.
133. **q formula sweep** — n=2..128 verifies reduction n and residual n(n-1).
134. **World-renaming/order invariance** — certificate independent of representation ordering.
135. **Action-order invariance** — lower bound independent of action enumeration.
136. **Uniform cost scaling** — step bound invariant; cost bound scales exactly.
137. **10,000-world cheapest unresolved stress** — q cost 1 leaves 24,995,000 incompatible pairs.
138. **10,000-world pair-flow invariant** — root mass 25,000,000; q worst-branch reduction 5,000.

## Current novelty status
**Do not write the paper yet.** Tests 123–138 strengthen the quantitative machinery but also expose the key limitation: a root-only pair-flow capacity bound can be invalidated when legitimate authority-changing transitions unlock stronger future probes. This is a useful negative result, not a breakthrough claim. The next stop-and-write candidate is a sound state-dependent potential/cut theorem over reachable joint states `(C,A)`, tested against exact joint-state search on exhaustive small systems and randomized adversarial instances. If such a theorem survives prior-art attack and yields a nontrivial authorization-specific bound, we will have a much stronger basis to stop novelty hunting and write.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.