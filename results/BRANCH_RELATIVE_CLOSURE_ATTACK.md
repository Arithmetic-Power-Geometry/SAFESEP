# BRAC final-boundary attack — Tests 251–266

## Question
Can closure-first normalization be repaired by making authority closure relative to the current belief branch?

## Candidate
Branch-Relative Authority Closure (BRAC) repeatedly executes legitimate, monotone authority-progress actions whose observations are constant on the current branch. An action may be globally informative and become closure-eligible only after an earlier observation.

## Scientific target
This directly attacks the Test-206 failure mode of the naive global MCAS extension. Exact joint-state search remains the oracle.

## Permanent checks
- locally constant vs globally informative distinction;
- branch-relative authority fixed point and chains;
- seeded/unseeded cycles;
- initial/missing authority;
- action-order invariance;
- exhaustive 4-world binary-outcome enumeration (256 systems);
- branch-specific authority after observation;
- redundant grants;
- cheapest-unresolved regression through 10,000 worlds.

## Cheapest unresolved diagnostic
Dynamic/MCAS witness family:
- 200 worlds: q, cost 1, residual incompatible pairs 9,900
- 1,000 worlds: q, cost 1, residual incompatible pairs 249,500
- 5,000 worlds: q, cost 1, residual incompatible pairs 6,247,500
- 10,000 worlds: q, cost 1, residual incompatible pairs 24,995,000

## Interpretation
Agreement in this battery is evidence for a sharper authorization-specific normal form, not yet proof of novelty or necessity. World-dependent grants and revocation remain outside the Probe semantics and are retained as known boundary counterexamples from Tests 203–226. Generic belief-state planning, trust negotiation, monotone closure, and sensing/action sequencing remain prior art.

## Real-data boundary
No real benchmark currently used here supplies truthful counterfactual world-by-action authority-transition labels. AuthBench remains external-validity context only; BRAC labels are not fabricated from it.
