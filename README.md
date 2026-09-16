# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** Earlier matched witness families select `q`, cost 1, leaving 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000 worlds. Tests 123–138 deliberately add stronger bit probes and CI exposed that `q` must not be assumed globally: in this family the actual selected cheapest unresolved experiment is `bit0`, cost 1, leaving 2,500 incompatible pairs at 200 worlds and 6,250,000 at 10,000 worlds. The repository now recomputes this diagnostic per experiment family.

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
Tests 107–122 make the certificate dynamic over joint states `(C,A)`, including information-free authority transitions. The dynamic cut is a SAFESEP-specific semantic certificate, not yet a claim that dynamic cuts or joint-state planning are new. See `results/DYNAMIC_PAIR_FLOW_ATTACK.md`.

## Authorization pair-flow lower-bound attack
Tests 123–138 define incompatible-pair mass `M(C)` and worst-branch legitimate pair reduction. They test local counting, filtering, invariances, cost scaling, parameter sweeps and 10,000-world stress. CI also produced a scientifically important correction: bit probes beat q at equal cost in this family. A root-only capacity ceiling is not a general dynamic SAFESEP theorem because authority-changing transitions may unlock later high-capacity actions. See `results/PAIR_FLOW_LOWER_BOUND.md`.

## Datasets and empirical boundary
Controlled theorem datasets scale through 10,000 worlds. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks audited so far do not natively provide counterfactual world×experiment legitimacy and authority-transition semantics; we do not fabricate such labels.

## Test registry
1–122. Prior SAFESEP regression, collision, closure, coupling, dynamic-flow and large-scale tests retained.
123. **Zero pair-mass boundary** — homogeneous branch has zero lower bound.
124. **Exact binary pair mass** — 200 worlds give 10,000 incompatible root pairs.
125. **CI-corrected cheapest unresolved diagnostic** — `bit0`, cost 1, leaves 2,500 incompatible pairs at 200 worlds; earlier hard-coded q assertion was falsified and corrected.
126. **Exact q pair reduction** — q removes exactly 100 pairs in its worst branch at n=100.
127. **Illegitimate-probe capacity** — non-universal probe contributes zero safe pair-flow capacity.
128. **True no-op capacity** — information-free no-op contributes zero pair reduction.
129. **Perfect resolver capacity** — universally legitimate perfect resolver removes all incompatible pairs.
130. **Perfect-resolver lower bound** — one step, exact action cost.
131. **No-progress obstruction** — no legitimate progress implies infinite local bound.
132. **Partition monotonicity sweep** — pair mass never increases under observation partition, n=2..64.
133. **q formula sweep** — n=2..128 verifies q reduction n and residual n(n-1).
134. **World-order invariance** — certificate independent of representation ordering.
135. **Action-order invariance** — lower bound independent of action enumeration.
136. **Uniform cost scaling** — step bound invariant; cost bound scales exactly.
137. **10,000-world CI-corrected cheapest unresolved stress** — `bit0`, cost 1, leaves 6,250,000 incompatible pairs.
138. **10,000-world q invariant** — root mass 25,000,000; q reduction 5,000 and residual 24,995,000.

## Current novelty status
**Do not write the paper yet.** The CI failure is retained as evidence that the diagnostic must be computed rather than inherited from a previous construction. The next stop-and-write candidate remains a sound state-dependent potential/cut theorem over reachable joint states `(C,A)`, tested against exact joint-state search on exhaustive small systems and randomized adversarial instances.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.