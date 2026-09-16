# Authority-Closure Obstruction Certificate — Tests 163–178

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Result
For a joint branch S=(C,A), first compute the least monotone closure A+ under all currently legitimate zero-information authority actions. Only after this closure do we ask whether a decision-separating experiment is legitimate. If C is decision-critical and no separator is legitimate under A+, the branch is certified obstructed for the monotone token-only closure model.

This directly repairs the weakness of a static/root-only pair-flow certificate: a zero-information credential action may unlock a future high-capacity separator and therefore cannot be discarded merely because it does not shrink C.

## Cheapest unresolved experiment
In this family, the computed cheapest informative experiment that still leaves incompatible possible worlds is q, cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000 controlled worlds.

## OPEN/BLOCKED separation
OPEN has a zero-information fetch that grants alpha. Authority closure therefore unlocks perfect separator k. BLOCKED has an information-identical true no-op fetch; alpha is absent from closure. After q=rest, BLOCKED is certified obstructed while OPEN is not.

## Battery
Tests 163–178 cover homogeneous boundary, root separator availability, token closure, OPEN/BLOCKED separation, residual obstruction, cheapest unresolved experiment, multi-step authority chains, unseeded and seeded cycles, action/world-order invariance, parameter sweep and 10,000-world stress.

## Prior-art attack
Do not claim generic closure, reachability, belief-state applicability, dead-end detection, credential negotiation, or planning landmarks as novel. Contingent planning already reasons over belief-state applicability and dead ends; automated/interactive authorization negotiation already gathers additional credentials and maintains authorization state. The surviving value is as SAFESEP-specific machinery tying decision incompatibility to legitimacy after authority closure. A stronger novelty claim would require a compact authorization-specific certificate or theorem that is provably sound yet strictly avoids full joint-state search on a meaningful class.

## Real-data boundary
The scaling table is controlled theorem data. AuthBench is useful for real required-permission structure, but it does not supply counterfactual world×experiment legitimacy or token-transition ground truth. Such semantics are not fabricated.

## Decision
Not enough to write the paper yet. Next attack should compare this closure certificate exhaustively with exact joint-state search on randomized small monotone systems, characterize its soundness/completeness class, and search for the first counterexample outside that class. That theorem boundary is more important than increasing the test count alone.
