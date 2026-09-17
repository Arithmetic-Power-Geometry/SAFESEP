# Closure Exactness Boundary Attack — Tests 203–226

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Question
Can the MCAS closure-first exactness class be safely enlarged by allowing informative probes to change authority, hidden world-dependent grants, or revocation?

## Result 1 — informative grants are not a free extension
A simple informative grant can agree with exact search, but unrestricted informative authority-changing probes break the current closure-first normal form. Test 206 gives a four-world witness: probe `s` reveals a branch and grants `x`; probe `t` requires `x`, becomes observation-constant inside that branch, and grants `y`; resolver `k` requires `y`. Exact joint-state search executes `t` for authority progress even though it is no longer informative. The naive closure-first solver discards it as branch-constant. Result: `(closure-first, exact)=(False, True)`.

This narrows rather than expands the theorem class. The restriction separating authority-only progress from sensing is doing real work for the current normal form.

## Result 2 — hidden world-dependent grants have a minimal two-world counterexample
Worlds `r,w` require incompatible decisions. A one-outcome `fetch` grants token `x` only in `r`; perfect separator `k` requires `x`. An unsafe union-of-possible-grants abstraction concludes that `x` is available and returns resolvable. Exact belief search over `(world,authority)` states returns obstructed because `k` is not legitimate throughout the branch. Two worlds are minimal because a one-world state cannot be decision-critical.

## Result 3 — revocation has a minimal two-world counterexample
Start with token `x`. A one-outcome action revokes `x`; resolver `k` requires `x`. Exact search simply skips the revoker and resolves with `k`. A closure procedure that blindly saturates state-changing authority actions first destroys the needed authority and returns false. Again two worlds are minimal for decision incompatibility.

## Cheapest unresolved experiment
For the retained dynamic OPEN family the diagnostic is recomputed, not inherited: `q`, cost 1, leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000 worlds. Tests 223–224 pin these values.

## Scale and real-data boundary
Controlled structural stress remains 200→10,000 worlds because these instances have the counterfactual world×probe authority semantics required by the theorem. AuthBench is retained as the real external-validity source: it has 120 realistic terminal tasks with human-reviewed file-level read/write/execute permission labels and executable utility/attack validators. It does not natively provide hidden counterfactual world-dependent authority grants or revocation semantics, so those labels are not fabricated.

## Prior-art attack
This boundary is not automatically a novelty claim. Contingent-planning literature explicitly separates sensing from actuation and notes transformations between representations; belief-state AND/OR search is established. Automated trust negotiation already studies protected credential disclosure and cyclic disclosure dependencies. Access-control systems such as Cassandra use fixed-point policy semantics and state-changing authorization operations. Therefore the current contribution is a sharply tested SAFESEP boundary/counterexample result, not yet a breakthrough theorem.

## Decision
Do not write the paper yet. The strongest next target is to formulate the exact authorization-specific conditions under which authority-progress actions can be commuted/saturated without loss, prove necessity/sufficiency for that class, and compare that theorem against sensing/actuation normal forms and trust-negotiation semantics. Tests 203–226 permanently preserve the failed extension so it cannot be accidentally reintroduced.
