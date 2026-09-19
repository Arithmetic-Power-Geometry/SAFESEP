# Final prior-art attack for SAFESEP / BRAC

## Result

The completeness and complexity pass strengthens the mathematics but narrows the
novelty claim.

### Established neighboring results that must not be claimed

1. **Conditional / contingent planning with sensing.** Belief-state branching,
   sensing actions, AND/OR policy trees, soundness/completeness of planners, and
   high complexity for general partial-observability planning are established.
2. **Automated trust negotiation.** Protected credential disclosure,
   authorization-sensitive evidence release, cyclic policy dependencies, and
   complete strategies for monotonic policy languages are established.
3. **Authorization credential gathering.** Computing and acquiring credentials
   needed to satisfy an authorization policy is established.
4. **Optimal decision trees / test cover.** Cost-optimal diagnostic or
   identification trees have classical hardness results.

### What survives as the paper-specific contribution

The defensible contribution is the combination of:

- decision-critical authorization equivalence classes rather than exact world
  identification;
- universal branchwise legitimacy of evidence probes over all worlds still
  compatible with the current branch;
- exact joint knowledge-authority semantics used as a falsification oracle;
- the MCAS-to-BRAC counterexample progression;
- BRAC as an authorization-specific branch-relative normalization;
- explicit semantic boundaries: hidden world-dependent grants and revocation
  invalidate the monotone normalization;
- reproducible theorem attacks and controlled counterexamples.

### New theorem framing

Do **not** claim that monotone authorization closure, credential sequencing, or
planner completeness is new.

Claim instead:

> In the explicit finite SAFESEP Probe model, monotone world-independent
> authority acquisition yields a pair-separation characterization of safe
> authorization resolvability. BRAC is complete for this restricted model.
> The result identifies precisely why the normalization fails once authority
> effects become world-dependent or non-monotone.

### Novelty verdict

The theorem is a useful paper-strengthening result, not by itself evidence of a
field-level breakthrough. Its value is a sharp characterization and boundary
inside the SAFESEP semantics.

### Sources checked

- Rintanen, *Complexity of Planning with Partial Observability* (ICAPS 2004).
- Oglietti, *Understanding planning with incomplete information and sensing*
  (Artificial Intelligence, 2005).
- Li, Li & Winsborough, *Automated trust negotiation using cryptographic
  credentials* (CCS 2005).
- Becker, Mackay & Dillaway, *Abductive Authorization Credential Gathering*
  (IEEE POLICY 2009).
- Hyafil & Rivest, *Constructing optimal binary decision trees is NP-complete*
  (Information Processing Letters, 1976).

Searches for the exact phrases "safe separability" in autonomous authorization
and "Branch-Relative Authority Closure" did not surface an obvious exact prior
use in the reviewed results. This is not a guarantee of novelty; it is only a
negative search observation.
