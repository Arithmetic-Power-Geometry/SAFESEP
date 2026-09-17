# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently recompute: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** In the dynamic/MCAS family, `q`, cost 1, leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000. In the stronger-bit family of Tests 123–138, `bit0`, also cost 1, leaves fewer incompatible pairs. We never inherit the answer across families.

## Prior-art boundary
SAFESEP does not claim novelty for adaptive diagnosis/testing, contingent/conformant/epistemic planning, belief-state applicability, trust negotiation, proof-carrying authorization, fixed-point authorization/trust semantics, monotone closure, credential disclosure, set cover, pair separation, planning cuts/deadends, generic AND/OR recursion, dynamic authority acquisition, delegation chains, provenance binding, or negotiated capability scopes.

## Results retained
Tests 1–162 establish and attack matched-summary irreducibility, dynamic authority flow, legitimacy obstruction, pair-flow limits, and exact joint-state recursion. Tests 163–178 add least authority closure under zero-information token actions.

## MCAS closure exactness candidate
Tests 179–202 define the restricted **Monotone Closure-then-Authorized Sensing (MCAS)** class: authority-only actions have one observation, preserve the compatible-world set, monotonically add world-independent authority; informative sensing actions do not alter authority; sensing legitimacy depends only on current authority. In finite MCAS systems, authority-only actions can be saturated before sensing without loss of resolvability in the tested model. The repository compares a closure-first solver against exact joint-state search. See `results/CLOSURE_EXACTNESS_CLASS.md`.

## Boundary attack: Tests 203–226
The attempted extension beyond MCAS produced scientifically useful counterexamples rather than a broader theorem. A four-world informative-grant chain shows that an informative probe can become branch-constant after an earlier observation while still be needed solely for its authority grant; exact search retains that progress, whereas the naive closure-first extension discards it. Hidden world-dependent grants yield a minimal two-world false-positive for union-of-possible-authority closure. Revocation yields a minimal two-world false-negative for blind saturation because exact search can skip the revoker. These failures sharpen the MCAS assumptions instead of weakening them. See `results/CLOSURE_BOUNDARY_ATTACK.md`.

## Commutation-condition attack: Tests 227–250
The MCAS assumptions are now exposed as explicit local authorization commutation obligations. The checker certifies only monotone, world-independent authority progress separated from informative sensing. The battery attacks authority chains, missing and initial tokens, redundant grants, cycles, action order, 1,250 deterministic randomized certified instances, out-of-class informative grants, and 200→10,000-world scaling. This is retained as a **sufficient structural certificate**, not yet a necessary-and-sufficient breakthrough theorem. See `results/COMMUTATION_CONDITION_ATTACK.md`.

## Datasets and empirical boundary
Controlled theorem datasets scale through 10,000 worlds. `closure_exactness_scaling.csv`, `closure_boundary_stress.csv`, and `commutation_stress.csv` record stress results. AuthBench is retained as a real external-validity source with 120 realistic terminal tasks and human-reviewed file-level permission labels plus executable utility/attack validators. It does not natively provide counterfactual hidden authority grants/revocations, so such semantics are never fabricated.

## Test registry
1–178. Prior SAFESEP regression, collision, pair-flow, obstruction, recursive and authority-closure batteries retained.
179–202. MCAS closure exactness candidate, exhaustive/random exact-solver comparison, and 200→10,000 stress retained.
203–226. Informative-grant, hidden world-dependent grant, revocation, randomized boundary, and cheapest-experiment regression battery retained.
227. Empty probe-set commutation boundary.
228. Pure sensing certificate.
229. Authority-only monotone grant certificate.
230. Informative authority grant rejected by certificate.
231–233. Authority-chain exact agreement at depths 1, 2, and 8.
234. Missing authority blocks both solvers.
235. Initial authority repairs both solvers.
236. Redundant authority grant is harmless.
237. Unseeded authority cycle blocks.
238. Seeded authority cycle resolves.
239. Action-order invariance.
240. World-renaming/control invariance.
241. 250 deterministic randomized certified-system comparisons.
242. 1,000 additional deterministic randomized certified comparisons.
243. Out-of-class does not mean impossible.
244. Failed commutation obligation is exposed explicitly.
245. 200-world cheapest unresolved regression: q, cost 1, 9,900 pairs.
246. 1,000-world cheapest unresolved regression: q, cost 1, 249,500 pairs.
247. 2,000-world cheapest unresolved regression: 999,000 pairs.
248. 5,000-world cheapest unresolved regression: 6,247,500 pairs.
249. 10,000-world cheapest unresolved regression: q, cost 1, 24,995,000 pairs.
250. Certificate is sufficient, not necessary: rejected instance can still agree.

## Current novelty status
**Do not write the paper yet.** We now have a strongly tested sufficient commutation boundary plus minimal counterexamples outside it. Fresh 2026 work on runtime authorization of acquired resources, agent trust negotiation, authorization envelopes, and dynamic agent authorization further rules out broad claims based on authority acquisition, delegation, provenance, or negotiated scopes. The remaining stop-and-write target is narrower: a decision-neutral authorization commutation theorem with a necessary/sufficient boundary that is not merely established sensing/actuation normal form or trust-negotiation sequencing in different notation.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.