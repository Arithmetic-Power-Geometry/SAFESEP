# SAFESEP reduction boundary: ECD / DRD / active diagnosis

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Result

SAFESEP contains an established information-acquisition core, but adds a state-dependent feasibility constraint on tests.

### Unconstrained reduction

If every experiment is admissible in every possible world, a SAFESEP instance with decision map D reduces to Equivalence Class Determination (ECD): hypotheses are worlds and equivalence classes are the fibres D^{-1}(d). A terminal SAFESEP state is decision-homogeneous exactly when the surviving hypotheses lie in one ECD class. Therefore decision-relative stopping itself is not a novelty claim.

Decision Region Determination (DRD) is even more general on the decision side because it permits overlapping decision regions. SAFESEP should not claim invention of decision-directed information acquisition, equivalence-class stopping, adaptive testing, or cost-sensitive test selection.

### Active-diagnosis overlap

Active diagnosis already uses conditional plans, admissible actions, partial observations, AND-OR planning, and safety considerations to refine ambiguous diagnoses. Therefore SAFESEP should not claim invention of safe conditional sensing or adaptive diagnosability.

### Surviving structural distinction

In SAFESEP, test feasibility is endogenous to the unresolved authorization worlds: e may be used at belief state C only when Adm(e,w)=1 for every w in C. After an observation shrinks C, a previously forbidden experiment can become legal. The authorization decision being inferred and the authority to gather its evidence are therefore coupled through the same unresolved worlds.

The matched A_n/B_n family isolates this incidence dependence. A_n and B_n have identical hypotheses/worlds, decision classes, test costs, complete outcome maps, admissibility cardinalities, unconstrained resolution cost, one-step closed cost, and cheapest-root-probe diagnostics. They differ only in which individual world admits e2. Nevertheless A_n has a constructive safe tree of cost 2 and B_n is obstructed.

## Novelty boundary

This does NOT prove that no active-diagnosis, constrained contingent-planning, epistemic-planning, or test-selection formalism can encode SAFESEP. In fact sufficiently general planning formalisms can encode world-dependent action preconditions. The defensible contribution is therefore not representational impossibility.

The current candidate contribution is a domain-specific authorization property and its structural consequences: decision-relative safe separability under authorization-dependent evidence admissibility, together with matched-summary irreducibility constructions and exact/constructive solvers.

## Next falsification target

Search specifically for prior work whose action/sensing precondition is evaluated universally over the current belief state AND whose goal is equivalence-class/decision resolution rather than exact diagnosis. If such work already states the same property and incidence result, narrow the novelty further. Otherwise, proceed to complexity and approximation results for the explicit finite SAFESEP model.
