# Finite-model scope of verification

A verification instance consists of a nonempty finite set of worlds, a finite set of probes and authority tokens, a fixed required decision for each world, deterministic observations, world-independent positive-token requirements, and world-independent grants that only add tokens. A compatible branch contains worlds consistent with the observed probe outcomes. A probe may run only if all its token requirements are held. A resolving tree reaches a decision-homogeneous leaf after finitely many legitimate probes on every observation path.

The exact solver searches joint compatible-world and authority states. MCAS closes globally observation-constant grant-capable actions in its restricted class. BRAC closes grant-capable actions whose observations are constant on the current branch and then branches on informative actions. The verification checks Boolean existence of a finite safe resolving tree, not preservation of minimum worst-case cost.

The archived BRAC completeness analysis can be inspected at `results/BRAC_COMPLETENESS_AND_COMPLEXITY.md` in the repository root. It identifies the positive-token and monotonicity assumptions under which the finite Boolean resolution criterion holds. Outside those assumptions, world-dependent grants and revocation can invalidate early closure. The independent scripts are additional finite falsification checks and do not constitute a mechanized proof.

