# Closure Exactness Class Attack — Tests 179–202

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Candidate restricted theorem
Define MCAS (Monotone Closure-then-Authorized Sensing): authority-only actions have a single observation, never change the compatible-world set, add authority monotonically, and have world-independent requirements/grants; informative sensing actions do not change authority; sensing legitimacy depends only on acquired authority.

For finite MCAS systems, saturating the least authority closure before selecting an informative sensing action is without loss of *resolvability*. Therefore closure-first search and exact joint-state search agree on existence of a resolving policy.

### Proof sketch
Any finite exact resolving policy contains some interleaving of authority-only and informative actions. Authority-only actions do not alter C and only monotonically add tokens. Because requirements and grants are world-independent and informative actions do not alter authority, every authority-only action executable before a sensing step remains executable if moved earlier. Repeatedly commute all executable authority-only actions to the front. Their least fixed-point closure therefore contains every authority token obtainable before the first informative action. The first sensing action remains legitimate. Apply the same argument recursively to every observation branch. The reverse direction is immediate because closure actions are legitimate exact transitions. Hence closure-first and exact resolvability coincide.

## Falsification battery
Tests 179–202 cover OPEN/BLOCKED agreement, n=2..64 sweeps, action/world permutation, initial authority, multi-step authority chains, unseeded/seeded cycles, exhaustive small configurations, 500 deterministic randomized MCAS instances, closure idempotence/monotonicity, and controlled 200/1k/2k/5k/10k cheapest-unresolved stress.

## Permanent diagnostic
For the dynamic family the cheapest informative experiment that still leaves a decision-incompatible branch is q at cost 1. Worst remaining incompatible-pair counts are 9,900 (200 worlds), 249,500 (1,000), 999,000 (2,000), 6,247,500 (5,000), and 24,995,000 (10,000).

## Prior-art attack
This is not yet claimed as a breakthrough. Least-fixed-point authorization/trust semantics are established, including Weeks-style authorization maps and trust-structure fixed points; operational access-control systems also use fixed-point evaluation. The potentially useful contribution is the *specific exactness boundary* connecting monotone authorization closure to SAFESEP decision-separating sensing. A paper-level novelty claim requires a broader search for an equivalent commutation/normal-form theorem in trust negotiation, authorization logics, and contingent/epistemic planning.

## Empirical boundary
The 10,000-world runs are controlled theorem stress tests, not production authorization telemetry. Real authorization benchmarks currently audited do not provide the counterfactual world×experiment legitimacy and authority-transition labels needed to test this theorem directly. Do not fabricate them.

## Status
Promising theorem-class result, but STOP-AND-WRITE criterion is not yet met. Next attack: search for prior commutation/normal-form results and deliberately construct the smallest counterexample when each MCAS assumption is removed (world-dependent authority, revocation, informative grants, evidence-conditioned legitimacy).