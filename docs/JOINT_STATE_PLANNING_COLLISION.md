# Full joint-state contingent-planning collision

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Question
Does the matched information/authority marginal separation survive once an ordinary contingent planner is allowed to represent the full joint state?

## Permanent cheapest-experiment diagnostic
For both matched systems A_n and B_n, the cheapest executable informative experiment that still leaves a decision-incompatible branch is q with cost 1. The residual branch contains (n-1)n incompatible R/W pairs. At 10,000 worlds (n=5000), this is 24,995,000 pairs.

## Independent baseline
`src/safesep/joint_planning_baseline.py` represents a state as `(compatible worlds, acquired authority tokens)`. After q, each observation updates both components. A branch is winning if it is already decision homogeneous or the acquired token enables the branch resolver. All observation branches must win.

## Result
The baseline exactly reproduces the earlier separation:

- A_n: resolvable.
- B_n: not resolvable.
- separate information/authority marginals: identical.
- full branch-sensitive joint-state signatures: different.

Thus the matched-marginals result is valid as a summary-insufficiency theorem, but it is **not** an irreducibility result against contingent planning. Once authority tokens are ordinary state variables, the full coupling is representable by standard belief-state contingent planning.

## Prior-art comparison
Contingent planning already reasons over belief states, action preconditions/effects and observation-conditioned branches. A planner may add authority tokens as state propositions and encode their acquisition as conditional effects. Therefore joint information-authority evolution, by itself, is not a new planning primitive.

## Novelty consequence
Do not claim that SAFESEP cannot be represented by contingent planning. The surviving research target must be a theorem not erased by full-state compilation—for example a restricted complexity separation, a new invariant/lower bound for authorization-safe resolution, or an empirical phenomenon tied to authorization semantics rather than generic state representation.

## Tests
37. Cheapest q/cost-1 diagnostic preserved at 200 worlds.
38. Combined-state planner exactly reproduces A/B resolvability.
39. Separate marginals match while full joint-state signatures differ.
40. 10,000-world collision: q cost 1, 24,995,000 residual incompatible pairs, planner resolves A but not B.
