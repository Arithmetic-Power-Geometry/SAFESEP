# Authorization Commutation Condition Attack — Tests 227–250

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Goal
Make the MCAS closure-first assumptions explicit as local authorization commutation obligations and attack the resulting sufficient certificate against exact joint-state search.

## Certificate
The current `Probe` model is certified only when authority is monotone/world-independent and every authority-changing action is observation-constant; informative sensing must not change authority. This is a conservative sufficient class, not a necessary characterization of every resolvable instance.

## Battery
Tests 227–250 cover empty/pure-sensing boundaries, authority chains, missing/initial tokens, redundant grants, seeded/unseeded cycles, action-order invariance, 1,250 deterministic randomized certified instances, explicit rejection of informative authority grants, and controlled scaling through 10,000 worlds.

## Cheapest unresolved experiment
The diagnostic is recomputed for this family. `q`, cost 1, leaves 9,900 incompatible pairs at 200 worlds; 249,500 at 1,000; 999,000 at 2,000; 6,247,500 at 5,000; and 24,995,000 at 10,000 worlds. These are family-specific results, not a universal claim.

## Prior-art boundary
The certificate must not be advertised as a generic planning breakthrough. Belief-state contingent planning, sensing/actuation separation, trust negotiation, monotone credential acquisition, fixed-point authorization, and stateful authorization are established neighboring mechanisms. The research question is narrower: whether an authorization-specific decision-neutral commutation theorem can be made both necessary and sufficient under semantics that exclude presupposing the unresolved authorization decision.

## 2026 collision check
Fresh search also found current agent-authorization work emphasizing dynamic authorization, delegation/provenance binding, negotiated scopes, and runtime activation of acquired authority. These reinforce the need to avoid novelty claims based merely on dynamic authority acquisition or provenance.

## Decision
Tests 227–250 strengthen the verified sufficient boundary but do not yet establish the desired necessary-and-sufficient authorization-specific theorem. Do not write the paper yet solely on this result. Preserve any CI falsification and narrow again if required.
