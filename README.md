# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions whose authorization is itself legitimately justified.

> **Know enough to grant — but never grant to know.**

## Core question
Given compatible worlds `C` requiring potentially different authorization decisions, can adaptive evidence reach a decision-homogeneous branch while every evidence probe is authorized without improperly presupposing the unresolved decision?

## Cheapest-experiment diagnostic
We permanently recompute: **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?** In the dynamic/MCAS family, `q`, cost 1, leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000. In the stronger-bit family of Tests 123–138, `bit0`, also cost 1, is cheaper under the tie-breaking diagnostic because it leaves fewer incompatible pairs. We never inherit the answer across families.

## Prior-art boundary
SAFESEP does not claim novelty for adaptive diagnosis/testing, contingent/conformant/epistemic planning, belief-state applicability, trust negotiation, proof-carrying authorization, fixed-point authorization/trust semantics, monotone closure, credential disclosure, set cover, pair separation, planning cuts/deadends, or generic AND/OR recursion.

## Results retained
Tests 1–162 establish and attack matched-summary irreducibility, dynamic authority flow, legitimacy obstruction, pair-flow limits, and exact joint-state recursion. Tests 163–178 add least authority closure under zero-information token actions.

## MCAS closure exactness candidate
Tests 179–202 define the restricted **Monotone Closure-then-Authorized Sensing (MCAS)** class: authority-only actions have one observation, preserve the compatible-world set, monotonically add world-independent authority; informative sensing actions do not alter authority; sensing legitimacy depends only on current authority. In finite MCAS systems, authority-only actions commute before sensing, so least authority closure can be saturated without loss of resolvability. The repository compares a closure-first solver against exact joint-state search. See `results/CLOSURE_EXACTNESS_CLASS.md`.

This is stronger than the earlier sufficient certificate because it proposes an exactness/normal-form boundary, but it is **not yet claimed as novel**: fixed-point authorization semantics are established and the remaining task is to rule out equivalent commutation/normal-form results in authorization/trust-negotiation and contingent-planning literature.

## Datasets and empirical boundary
Controlled theorem datasets scale through 10,000 worlds. `closure_exactness_scaling.csv` records 200/1k/2k/5k/10k stress. `real_authorization_source_audit.csv` records real-source coverage. Current real authorization benchmarks do not provide the counterfactual world×experiment legitimacy and authority-transition ground truth required for a direct MCAS test; we do not fabricate it.

## Test registry
1–178. Prior SAFESEP regression, collision, pair-flow, obstruction, recursive and authority-closure batteries retained.
179. OPEN closure-first/exact agreement.
180. BLOCKED closure-first/exact agreement.
181. OPEN satisfies MCAS syntactic class.
182. BLOCKED satisfies MCAS syntactic class.
183. Authority closure unlocks alpha.
184. Matched no-op closure remains empty.
185. Exact agreement sweep n=2..64 for OPEN/BLOCKED.
186. Action-order invariance.
187. World-order invariance.
188. Initial-token boundary restores resolution.
189. Multi-step authority-chain exactness.
190. Unseeded authority cycle obstruction.
191. Seeded authority cycle resolution.
192. Informative authority grant is outside MCAS.
193. Exhaustive small MCAS configuration agreement.
194. 500 deterministic randomized MCAS instances agree with exact solver.
195. 200-world cheapest unresolved: q, cost 1, 9,900 residual incompatible pairs.
196. 1,000-world stress: 249,500 residual pairs.
197. 2,000-world stress: 999,000 residual pairs.
198. 5,000-world stress: 6,247,500 residual pairs.
199. 10,000-world stress: q, cost 1, 24,995,000 residual pairs.
200. Authority closure idempotence.
201. Authority closure monotonicity.
202. Exactness-class boundary regression: informative grants excluded.

## Current novelty status
**Do not write the paper yet.** MCAS closure exactness is the strongest current theorem candidate because it replaces full interleaving search by a closure-first normal form for a precisely stated authorization class. But least-fixed-point authorization semantics are established prior art, and we have not yet excluded an equivalent commutation theorem. Next: aggressive prior-art search plus smallest-counterexample tests for each removed MCAS assumption (world-dependent grants, revocation, informative authority grants, evidence-conditioned legitimacy). If the exactness theorem survives that attack with an authorization-specific boundary not already known, stop testing and write the paper.

## Research protocol
For every significant result: attack prior art; construct witness/counterexample; compare baselines; use real data only when its fields genuinely support the claim; save code/data/results; add permanent regression tests; append this registry; run CI; and preserve scientifically meaningful failures/corrections.

## License
Apache License 2.0. See `LICENSE`.