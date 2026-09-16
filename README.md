# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** The answer is recomputed per experiment family. Earlier matched and dynamic OPEN/BLOCKED families select `q`, cost 1, leaving 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000 worlds. Tests 123–138 deliberately add stronger bit probes; there `bit0`, also cost 1, leaves only 2,500 at 200 and 6,250,000 at 10,000. We never inherit a cheapest-probe answer from another family.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, conformant/contingent/epistemic planning, possible-world/belief-state authorization semantics, universal belief-state action applicability, world-dependent applicability, history/provenance authorization, proof-carrying authorization, iterative proof-component fetching, trust negotiation, cost-sensitive credential/policy disclosure, credential-disclosure sequences, runtime access-policy discovery, cyclic credentials, recursive authorization/fixed-point closure, joint information-authority state representation, minimal credential disclosure, pair separation, decision-region edge cutting, dynamic authorization-state updates, latent policy identity, generic context-dependent rule validity, grounded-vs-unsupported circular proofs, ordinary protected proof-component acquisition, planning abstraction loss, generic k-wise indistinguishability, generic local-vs-global consistency gaps, generic set-cover/minimal-cover reductions, generic planning cuts/dead-end reasoning, generic pair-counting/cover lower bounds, generic AND/OR belief-state recursion, or generic monotone closure.

## Structural results retained
Matched information/authority marginals do not determine joint resolvability, but full joint-state planning can encode the missing alignment. The authorization-safe evidence premium quantifies extra legitimate cost. Static pair cuts reduce to test-cover/DRD structure after filtering unavailable tests.

## Dynamic branch-relative authorization cut
Let joint state be `S=(C,A)`. Tests 85–86 repaired token-only transition soundness: authority progress does not require information gain. Tests 107–122 then stress the dynamic cut through 10,000 worlds.

## Pair-flow and legitimacy obstruction
Tests 123–138 define incompatible-pair mass and expose the limitation of a root-only capacity ceiling. Tests 139–146 convert branchwise resolver legitimacy into an exact absence-set/set-cover obstruction identity. Both are retained as machinery, not breakthrough claims.

## Recursive authorization-obstruction attack
Tests 147–162 add an exact finite recursion over joint states `(C,A)`. A transition counts as progress if it changes the compatible-world branch or acquired authority. Thus one-outcome token acquisition is retained while a true no-op is discarded. OPEN resolves because `fetch` grants `alpha` and unlocks `k`; BLOCKED remains obstructed because its matched-cost fetch is a true no-op. The recursion is a sound SAFESEP baseline but its generic AND/OR structure collides with established contingent planning.

## Authority-closure obstruction certificate
Tests 163–178 compute the least monotone authority closure under legitimate zero-information token actions before testing separator availability. This repairs the static certificate failure mode without requiring the certificate itself to discard token-only progress. In OPEN, closure obtains `alpha` and unlocks `k`; in BLOCKED, the matched no-op cannot. After `q=rest`, BLOCKED has no separator even after closure and is certified obstructed, while OPEN is not. This is a compact sufficient certificate for the monotone token-only closure model, not a claim that closure/dead-end detection is new. See `results/AUTHORITY_CLOSURE_CERTIFICATE.md`.

## Datasets and empirical boundary
Controlled theorem datasets scale through 10,000 worlds, including `legitimacy_obstruction_scaling.csv`, `recursive_obstruction.csv`, and `authority_closure_certificate.csv`. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks audited so far do not natively provide counterfactual world×experiment legitimacy and authority-transition semantics; we do not fabricate such labels.

## Test registry
1–122. Prior SAFESEP regression, collision, closure, coupling, dynamic-flow and large-scale tests retained.
123–138. Pair-flow lower-bound battery retained, including the CI-corrected `bit0` cheapest-probe result.
139–146. Legitimacy-obstruction/set-cover certificate battery retained.
147–162. Recursive joint-state obstruction battery retained.
163. **Homogeneous closure boundary** — homogeneous branch is not obstructed.
164. **Root separator boundary** — BLOCKED root is not prematurely called dead because q is available.
165. **OPEN authority closure** — zero-information fetch derives alpha.
166. **BLOCKED authority closure** — matched no-op does not derive alpha.
167. **OPEN separator unlock** — closure makes k legitimate.
168. **BLOCKED separator lock** — k remains unavailable after closure.
169. **Residual BLOCKED certificate** — after q=rest, no separator exists even after authority closure.
170. **Residual OPEN certificate** — after q=rest, closure unlocks k and rejects false obstruction.
171. **Cheapest unresolved diagnostic at 200 worlds** — q cost 1 leaves 9,900 incompatible pairs.
172. **Multi-step authority chain** — x then alpha is reached through zero-information closure.
173. **Unseeded authority cycle** — x/y cycle creates no authority from nothing.
174. **Seeded authority cycle** — one seed closes the x/y cycle.
175. **Action-order invariance** — closure independent of enumeration order.
176. **World-order invariance** — separator certificate independent of representation order.
177. **Scale sweep** — residual BLOCKED obstruction verified for n=2,4,...,128.
178. **10,000-world cheapest unresolved stress** — q cost 1 leaves 24,995,000 incompatible pairs.

## Current novelty status
**Do not write the paper yet.** Tests 163–178 produce a more compact sound certificate for a monotone authority-closure subclass, but generic closure, belief-state applicability, dead-end reasoning and credential negotiation are established. The next decisive step is exhaustive/random comparison against exact joint-state search to characterize precisely when the closure certificate is sound and complete, and to construct the smallest counterexample outside that class. A genuinely authorization-specific theorem at that boundary could satisfy the stop-and-write criterion.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.