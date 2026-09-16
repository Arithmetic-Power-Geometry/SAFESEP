# Result — SAFESEP / strong contingent-planning collision

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Question
Does the present finite SAFESEP model define a resolvability notion that cannot already be represented as strong contingent planning under partial observability?

## Reduction
For a SAFESEP instance P map:

- possible world w -> planning state w;
- current possible-world set C -> belief state C;
- experiment e -> sensing action e;
- Adm(e,w) -> state-wise action applicability/precondition;
- observation O_e(w) -> sensing observation;
- authorization decision D(w) -> goal label;
- decision-homogeneous C -> goal belief.

An experiment is SAFESEP-admissible on C exactly when the corresponding action is applicable in every state in belief C. Observation successors are identical belief contractions. A SAFESEP terminal node is exactly a belief whose states share one decision label.

Therefore, for the current explicit finite model, SAFESEP-EXISTS is extensionally equivalent to existence of a strong contingent sensing policy for the translated instance.

## Executable cross-check
`src/safesep/contingent_baseline.py` is an independent belief-space AND/OR solver. `tests/test_contingent_collision.py` checks agreement on the core examples and the A_n/B_n family through n=30, with additional scale points through n=50.

## Scientific consequence
This is a negative novelty result and is preserved intentionally. The present combination of branchwise admissibility, adaptive sensing, decision-homogeneous stopping, and the A_n/B_n incidence separation is not by itself sufficient for a breakthrough claim, because the same structure can be encoded as contingent planning with state-dependent action applicability.

## Surviving research target
A stronger SAFESEP theory must add a genuinely authorization-specific semantic constraint not reducible to fixed world-state action preconditions. Candidate directions include justification-relative admissibility, non-presuppositional evidence acquisition, or policy/decision-dependent authorization semantics. Each candidate must itself be attacked against epistemic and knowledge-based planning before being claimed novel.
