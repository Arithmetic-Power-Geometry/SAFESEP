# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently test: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** The answer is recomputed per experiment family. Earlier matched and dynamic OPEN/BLOCKED families select `q`, cost 1, leaving 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000 worlds. Tests 123–138 deliberately add stronger bit probes; there `bit0`, also cost 1, leaves only 2,500 at 200 and 6,250,000 at 10,000. We never inherit a cheapest-probe answer from another family.

## Prior-art collisions established
SAFESEP does **not** claim novelty for equivalence-class stopping, adaptive test selection, active diagnosis, safe sensing, conformant/contingent/epistemic planning, possible-world/belief-state authorization semantics, universal belief-state action applicability, world-dependent applicability, history/provenance authorization, proof-carrying authorization, iterative proof-component fetching, trust negotiation, cost-sensitive credential/policy disclosure, credential-disclosure sequences, runtime access-policy discovery, cyclic credentials, recursive authorization/fixed-point closure, joint information-authority state representation, minimal credential disclosure, pair separation, decision-region edge cutting, dynamic authorization-state updates, latent policy identity, generic context-dependent rule validity, grounded-vs-unsupported circular proofs, ordinary protected proof-component acquisition, planning abstraction loss, generic k-wise indistinguishability, generic local-vs-global consistency gaps, generic set-cover/minimal-cover reductions, generic planning cuts/dead-end reasoning, generic pair-counting/cover lower bounds, or generic AND/OR belief-state recursion.

## Structural results retained
Matched information/authority marginals do not determine joint resolvability, but full joint-state planning can encode the missing alignment. The authorization-safe evidence premium quantifies extra legitimate cost. Static pair cuts reduce to test-cover/DRD structure after filtering unavailable tests.

## Dynamic branch-relative authorization cut
Let joint state be `S=(C,A)`. Tests 85–86 repaired token-only transition soundness: authority progress does not require information gain. Tests 107–122 then stress the dynamic cut through 10,000 worlds.

## Pair-flow and legitimacy obstruction
Tests 123–138 define incompatible-pair mass and expose the limitation of a root-only capacity ceiling. Tests 139–146 convert branchwise resolver legitimacy into an exact absence-set/set-cover obstruction identity. Both are retained as machinery, not breakthrough claims.

## Recursive authorization-obstruction attack
Tests 147–162 add an exact finite recursion over joint states `(C,A)`. A transition counts as progress if it changes the compatible-world branch or acquired authority. Thus one-outcome token acquisition is retained while a true no-op is discarded. OPEN resolves because `fetch` grants `alpha` and unlocks `k`; BLOCKED remains obstructed because its matched-cost fetch is a true no-op. The recursion is a sound SAFESEP baseline but its generic AND/OR structure collides with established contingent planning, so it is not promoted as breakthrough. See `results/RECURSIVE_OBSTRUCTION_ATTACK.md`.

## Datasets and empirical boundary
Controlled theorem datasets scale through 10,000 worlds, including `legitimacy_obstruction_scaling.csv` and `recursive_obstruction.csv`. `real_authorization_source_audit.csv` records real-source coverage. Public authorization benchmarks audited so far do not natively provide counterfactual world×experiment legitimacy and authority-transition semantics; we do not fabricate such labels.

## Test registry
1–122. Prior SAFESEP regression, collision, closure, coupling, dynamic-flow and large-scale tests retained.
123–138. Pair-flow lower-bound battery retained, including the CI-corrected `bit0` cheapest-probe result.
139–146. Legitimacy-obstruction/set-cover certificate battery retained.
147. **Homogeneous terminal boundary** — decision-homogeneous state resolves with no action.
148. **Critical no-action obstruction** — incompatible decisions with no progress action are obstructed.
149. **OPEN token-flow resolution** — information-free authority acquisition unlocks the resolver.
150. **BLOCKED token-flow obstruction** — matched true no-op cannot unlock the resolver.
151. **Token-only progress preservation** — one-outcome `fetch` changing authority is retained by recursion.
152. **True no-op elimination** — one-outcome action changing neither belief nor authority is discarded.
153. **Dynamic-family cheapest unresolved diagnostic** — `q`, cost 1, leaves 9,900 incompatible pairs at 200 worlds.
154. **OPEN parameter sweep** — exact recursion resolves n=2..32.
155. **BLOCKED parameter sweep** — exact recursion certifies obstruction n=2..32.
156. **Unprotected perfect resolver** — direct perfect decision separator resolves.
157. **Unavailable perfect resolver** — missing authority with no acquisition path obstructs.
158. **Action-order invariance** — recursive result independent of action enumeration.
159. **World-order invariance** — recursive result independent of representation order.
160. **Initial-token restoration** — supplying `alpha` restores resolution in otherwise BLOCKED family.
161. **10,000-world cheapest unresolved stress** — `q`, cost 1, leaves 24,995,000 incompatible pairs.
162. **10,000-world authority-transition stress** — OPEN fetch changes authority without information; BLOCKED fetch remains a true no-op.

## Current novelty status
**Do not write the paper yet.** Tests 147–162 close the recursion/soundness gap under token-only authority transitions, but exact recursive AND/OR search is established contingent-planning machinery. The next stop-and-write target must exploit authorization-specific structure to obtain a compact certificate, lower bound, or tractable policy-class theorem that is not merely a re-encoding of full joint-state search or trust negotiation.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.