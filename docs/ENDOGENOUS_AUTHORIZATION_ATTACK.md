# Endogenous Authorization Attack

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Purpose

This audit asks whether making an evidence-gathering action legal only when the current knowledge justifies that action relative to the unresolved authorization decision escapes the contingent-planning collision.

## Candidate extension

Let C be the current compatible-world set and D(w) the required authorization decision. Replace fixed world-wise admissibility Adm(e,w) by a knowledge-relative predicate J(e,C). A probe is executable only if J(e,C)=1.

Example justification rule:

J(e,C)=1 iff every world in C whose decision would be prejudiced by executing e supplies an independent policy justification for e.

This looks endogenous because admissibility is evaluated on the current epistemic state rather than separately in each world.

## Reduction attack

For finite explicit models, if J(e,C) is a deterministic computable predicate of the current belief C and action e, an ordinary belief-space/epistemic planner can compile it into an epistemic action precondition. The planner state is C; action e is applicable exactly when J(e,C)=1; observations generate successor beliefs. Therefore knowledge-relative admissibility alone does not establish a new formalism.

Dynamic epistemic logic already gives epistemic actions formula-valued preconditions, and the literature also contains work explicitly titled “Endogenizing Epistemic Actions.” Thus the words endogenous or epistemic-action precondition are not novelty claims by themselves.

## Surviving boundary

A stronger survivor must make legality non-extensional with respect to the current belief set alone. Two histories h and h' may induce the same compatible worlds C but differ in whether a probe is authorized because the *provenance/justification path* differs.

Define a justification state Q(h), recording which authority, consent, delegation, purpose, or evidence provenance licensed prior observations. Candidate admissibility becomes

    J(e, C, Q(h)).

The key separation target is:

There exist histories h,h' with identical compatible-world set C, identical authorization decision alternatives, identical available experiment outcome maps and costs, but J(e,C,Q(h)) != J(e,C,Q(h')).

A planner whose state is only C cannot represent this distinction. However, a sufficiently general planner can augment its state with Q, so this still does not prove non-reducibility to planning. The potential novelty is therefore not “cannot be planned”; it is an authorization-specific state variable and theorem about *justification provenance closure*.

## Candidate theorem target: Justification-Relative Safe Separability (JRSS)

A resolution tree is JRSS-valid when each probe is authorized by the justification state accumulated on that branch and each leaf is decision-homogeneous. JR-SafeSep is minimum worst-case cost over such trees.

Desired matched-belief separation:

Construct two histories with the same C, D, probes, outcomes, costs, and cheapest informative probe statistics, but different justification provenance Q, such that one has finite JR-SafeSep and the other infinite JR-SafeSep.

This would show that belief/world uncertainty alone is insufficient for authorization-safe evidence acquisition; provenance of authority matters even when epistemic uncertainty is identical.

## Novelty status

NOT YET A BREAKTHROUGH. The reduction attack eliminates any claim based only on J(e,C). The next computational theorem must use matched belief states with different justification provenance and then be compared against provenance-aware access control, delegation logics, trust-management systems, purpose/consent systems, and history-based access control.
