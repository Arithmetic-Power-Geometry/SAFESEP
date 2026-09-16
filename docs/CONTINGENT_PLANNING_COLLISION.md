# Contingent-planning collision test

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Result
A targeted prior-art attack found that the bare SAFESEP-EXISTS structure is substantially covered by classical strong/conditional planning under partial observability.

Bertoli, Cimatti, Roveri and Traverso (Artificial Intelligence 170, 2006) define strong planning under partial observability as conditional planning that succeeds from all possible initial states and nondeterministic outcomes, using AND/OR belief-space search. Earlier conditional-planning formulations explicitly state that an action is applicable to a belief state iff it is applicable in every state in that belief state. This is structurally the same universal branch-admissibility condition used by SAFESEP.

Therefore we must NOT claim as novel by itself:
- belief-state AND/OR search;
- branchwise action/probe applicability in every still-possible world;
- conditional observation trees;
- existence of a finite safe conditional plan;
- the exponential belief-subset search upper bound.

## Mapping
SAFESEP knowledge set C -> planning belief state B.
SAFESEP probe e -> sensing/observation action.
Adm(e,w) -> state-dependent action applicability/precondition.
Universal branch admissibility forall w in C Adm(e,w) -> action applicable throughout belief B.
Outcome child C_(e,o) -> observation-conditioned successor belief.
SAFESEP terminal condition |{D(w):w in C}|=1 -> epistemic/knowledge goal that the required authorization decision is determined.

This mapping means SAFESEP-EXISTS is at least very close to a restricted strong contingent-planning problem. A formal equivalence/reduction should be treated as a novelty-falsification result, not a breakthrough claim.

## Surviving frontier
The authorization-specific contribution must require structure absent from ordinary contingent planning. The strongest frontier is now **endogenous authorization of epistemic actions**: the same unknown authorization decision that the agent is trying to determine also defines whether the information-gathering action is legally/organizationally permitted. A generic planner can encode this as preconditions if the authorization law is supplied exogenously; therefore mere encodability is not novelty.

A stronger result must exploit the coupling itself, for example by proving an authorization-specific invariant, impossibility, monotonicity failure, or separation that disappears when admissibility is exogenous.

## Status
This collision narrows the claim. SAFESEP is not yet at the requested stop point for a breakthrough paper.