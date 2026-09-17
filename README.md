# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently recompute: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** In the dynamic/MCAS family, `q`, cost 1, leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000. In the stronger-bit family of Tests 123–138, `bit0`, also cost 1, leaves fewer incompatible pairs. We never inherit the answer across families.

## Prior-art boundary
SAFESEP does not claim novelty for adaptive diagnosis/testing, contingent/conformant/epistemic planning, belief-state applicability, trust negotiation, proof-carrying authorization, fixed-point authorization/trust semantics, monotone closure, credential disclosure, set cover, pair separation, planning cuts/deadends, or generic AND/OR recursion.

## Results retained
Tests 1–162 establish and attack matched-summary irreducibility, dynamic authority flow, legitimacy obstruction, pair-flow limits, and exact joint-state recursion. Tests 163–178 add least authority closure under zero-information token actions.

## MCAS closure exactness candidate
Tests 179–202 define the restricted **Monotone Closure-then-Authorized Sensing (MCAS)** class: authority-only actions have one observation, preserve the compatible-world set, monotonically add world-independent authority; informative sensing actions do not alter authority; sensing legitimacy depends only on current authority. In finite MCAS systems, authority-only actions can be saturated before sensing without loss of resolvability in the tested model. The repository compares a closure-first solver against exact joint-state search. See `results/CLOSURE_EXACTNESS_CLASS.md`.

## Boundary attack: Tests 203–226
The attempted extension beyond MCAS produced scientifically useful counterexamples rather than a broader theorem. A four-world informative-grant chain shows that an informative probe can become branch-constant after an earlier observation while still being needed solely for its authority grant; exact search retains that progress, whereas the naive closure-first extension discards it. Hidden world-dependent grants yield a minimal two-world false-positive for union-of-possible-authority closure. Revocation yields a minimal two-world false-negative for blind saturation because exact search can skip the revoker. These failures sharpen the MCAS assumptions instead of weakening them. See `results/CLOSURE_BOUNDARY_ATTACK.md`.

## Datasets and empirical boundary
Controlled theorem datasets scale through 10,000 worlds. `closure_exactness_scaling.csv` and `closure_boundary_stress.csv` record stress results. AuthBench is retained as a real external-validity source with 120 realistic terminal tasks and human-reviewed file-level permission labels plus executable utility/attack validators. It does not natively provide counterfactual hidden authority grants/revocations, so such semantics are never fabricated.

## Test registry
1–178. Prior SAFESEP regression, collision, pair-flow, obstruction, recursive and authority-closure batteries retained.
179–202. MCAS closure exactness candidate, exhaustive/random exact-solver comparison, and 200→10,000 stress retained.
203. Informative authority grants admitted only as an attacked candidate extension.
204. Single informative grant agreeing case.
205. Informative grant needed after observation, agreeing case.
206. **Four-world informative-grant-chain counterexample** — closure-first false, exact true.
207. 500 deterministic randomized out-of-class boundary instances execute against both solvers.
208. Action-order invariance on agreeing candidate case.
209. World-order invariance on agreeing candidate case.
210. Hidden world-dependent grant: exact belief search blocks.
211. Unsafe union closure produces false positive.
212. Hidden-grant abstraction/exact gap pinned.
213. Two-world minimality of hidden-grant decision-critical witness.
214. Grant in every world repairs hidden-grant obstruction.
215. Initial common token repairs hidden-grant obstruction.
216. Revocation witness: exact solver skips revoker and resolves.
217. Blind closure saturation loses needed token and fails.
218. Two-world minimality of revocation witness.
219. Removing revoker restores normal-form result.
220. Revocation witness without initial token is obstructed.
221. World-dependent hidden-grant stress at 200 worlds.
222. World-dependent hidden-grant stress at 1,000 worlds.
223. 200-world cheapest unresolved regression: q, cost 1, 9,900 pairs.
224. 10,000-world cheapest unresolved regression: q, cost 1, 24,995,000 pairs.
225. Positive boundary narrowed: single informative grants do not justify unrestricted extension.
226. Negative boundary summary: hidden grants and revocation each admit two-world witnesses.

## Current novelty status
**Do not write the paper yet.** The boundary attack strengthened the scientific story by falsifying an over-broad extension and identifying minimal counterexamples. However, contingent-planning literature already separates sensing and actuation and studies conformant action segments between sensing steps; trust negotiation already studies credential-disclosure sequences; access-control systems already have fixed-point and state-changing semantics. The next stop-and-write target is therefore narrower: prove the exact authorization-specific commutation condition under which authority progress may be saturated before decision-separating sensing, and show that condition is not merely the established sensing/actuation normal form in different notation.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.