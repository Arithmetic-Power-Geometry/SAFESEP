# Legitimacy Obstruction Certificate — Tests 139–146

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Exact identity
For a decision-critical branch C and candidate resolving actions E, let R(w) be the actions legitimate in world w and A_w=E\R(w). A common legitimate resolver exists iff intersection_{w in C} R(w) is nonempty. Therefore no common resolver exists iff union_{w in C} A_w=E. The minimum number of worlds certifying one-step obstruction is exactly the minimum set-cover size of E by the absence sets A_w.

This gives an authorization-incidence certificate: a small witness can prove that every candidate resolver is blocked somewhere in the current possible-world branch without enumerating a full adaptive policy tree.

## Tests
139 positive common-resolver boundary; 140 one-world obstruction; 141 exact cover identity; 142 local-per-world permissiveness versus global obstruction; 143 exact obstruction-number sweep n=2..12; 144 scalable greedy certificate with verification at 128 resolvers; 145 renaming invariance; 146 controlled 10,000-world structural certificate with 5,000 resolvers.

## Large controlled result
At 10,000 possible worlds and 5,000 candidate resolvers, every sampled world is legitimate for 4,999 of 5,000 resolvers, yet the full branch has no common legitimate resolver. An explicit verified obstruction witness uses 5,000 blocker worlds. This is deliberately adversarial controlled theorem data, not production authorization telemetry.

## Prior-art attack
The set-cover identity itself is not breakthrough novelty: Set Cover/Hitting Set and minimal conflict/unsatisfiable-core ideas are classical, while automated trust negotiation already supports protected, selective and incremental credential disclosure and searches disclosure sequences. Belief-state/contingent planning also represents universal action applicability. Therefore Tests 139–146 establish a useful exact SAFESEP certificate and a clean complexity bridge, but not yet the stop-and-write theorem.

## Cheapest unresolved experiment
This certificate concerns resolver legitimacy rather than the separate cheapest-unresolved information diagnostic. In the current pair-flow balanced family, CI-corrected Tests 123–138 show that the cheapest cost-1 unresolved action is selected lexicographically among tied cost-1 actions and `bit0` leaves fewer incompatible pairs than q. We do not transfer q's earlier-family diagnostic into this new family.

## Real-data boundary
The 10,000-world row is controlled. Existing public authorization benchmarks audited by SAFESEP provide real permission/task structure but not the counterfactual possible-world × experiment legitimacy relation required to call these obstruction witnesses empirical ground truth. We therefore refuse to fabricate those labels.

## Decision
Retain the certificate and tests permanently. Do not write the paper yet. Next target: combine decision-incompatible pair separation with legitimacy-obstruction witnesses in a recursive state-dependent certificate, and test whether it yields a sound lower bound against exact joint-state search even when token-only transitions unlock later probes.
