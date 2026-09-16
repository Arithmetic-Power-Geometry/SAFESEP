# Branchwise Universal-Admissibility Gap — Tests 87–90

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Diagnostic
The cheapest informative experiment that still leaves mutually decision-incompatible possible worlds remains `q`, cost 1. At 200 worlds the unresolved `rest` branch has 9,900 incompatible pairs; at 10,000 controlled worlds it has 24,995,000.

## Matched construction
A and B have the same number of R/W worlds, same q partition/cost, and the same per-world summary: every individual world possesses a cost-1 resolving witness. A differs only in that the same resolver is valid throughout the unresolved branch; B has world-specific resolver witnesses, so no single resolver is uniformly executable while those worlds remain compatible.

Thus per-world existence of legitimate resolving evidence does not imply branchwise safe resolvability.

## Prior-art attack
This is a useful authorization-specific formulation, but not yet a breakthrough theorem. Authorization logics already use possible-world/Kripke or belief semantics; PeerAccess reasons about possible worlds and legal message releases; uncertain-data access control also uses possible-world semantics. Full belief-state/contingent planning can encode the identity of world-specific actions and require action applicability across the current belief state. Therefore the present A/B witness is representable in established full-state semantics.

The surviving target is not the statement that uniform branch applicability matters. It is to prove a nontrivial lower bound, hierarchy, or compact authorization-specific obstruction that cannot be reduced to simply carrying the complete world-action relation in the state.

## Empirical boundary
The 10,000-world CSV is controlled theorem stress data, not production authorization telemetry. Public authorization corpora generally do not expose counterfactual legitimacy of every evidence action in every compatible possible world. We do not synthesize such labels and call them real.

## Decision
Do not stop for paper yet. Tests 87–90 sharpen the exact branchwise property, but full possible-world/belief-state formalisms can represent it. Next target: quantify the minimum branchwise common legitimate evidence needed to separate decision classes and attack whether its obstruction/complexity has an authorization-specific theorem beyond generic planning/test cover.
