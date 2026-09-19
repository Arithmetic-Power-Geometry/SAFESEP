# Manuscript freeze patch after BRAC completeness pass

Do not freeze the current PDF unchanged. Apply these corrections first.

## 1. Replace the current one-directional BRAC theorem

Current manuscript Theorem 2 proves closure soundness and then reports empirical
agreement. Replace/extend it with the restricted completeness result:

**Theorem (BRAC exactness in the monotone world-independent Probe model).**
Assume finite worlds and probes, world-independent token requirements and
grants, monotone token addition, no revocation, and observations that only
refine the compatible-world branch. Then BRAC resolves an initial joint state
if and only if exact joint-state search resolves it.

The proof may be given through the monotone pair-separation characterization in
`results/BRAC_COMPLETENESS_AND_COMPLEXITY.md`.

## 2. Add the polynomial resolvability corollary

For the explicit finite representation, compute the least authority-reachable
token closure T*. Let E* contain all probes enabled by T*. Safe boolean
resolvability holds iff every pair of compatible worlds with different required
decisions is separated by at least one probe in E*.

State clearly that this is polynomial-time checkable in the explicit input
representation.

## 3. Correct the complexity discussion

Do not transfer the 2-EXPTIME result for general partial-observability
conditional planning to this restricted SAFESEP decision problem.

Separate:
- **boolean resolvability in current monotone Probe model:** polynomial;
- **cost-optimal adaptive tree:** retains classical optimal decision-tree
  hardness as a special case;
- **richer semantics with revocation/world-dependent effects:** complexity left
  open unless separately proved.

## 4. Update experimental count

Add the new 6,144-system exhaustive battery comparing:
- polynomial pair criterion,
- exact joint-state search,
- BRAC.

Do not replace the earlier 256-system experiment; report the new battery as a
stronger independent falsification layer.

## 5. Tighten novelty language

Explicitly acknowledge:
- complete contingent/sensing planners;
- monotonic trust-negotiation completeness;
- protected credential disclosure and cyclic dependencies;
- authorization credential gathering;
- optimal decision-tree hardness.

Retain novelty only at the authorization-specific SAFESEP/BRAC formulation and
its proved restricted characterization/boundary.

## 6. Android empirical status

Do not claim Android empirical validation until the emulator workflow has
actually executed successfully. A permission-state grant/revoke experiment is a
platform-semantics sanity check, not evidence of an Android vulnerability and
not a proof of SAFESEP novelty.

## Freeze condition

Freeze the paper only after:
1. theorem CI is green;
2. the 6,144-system exhaustive comparison is green;
3. Android emulator sanity workflow is green or explicitly moved to future
   work;
4. manuscript theorem/complexity/novelty text is updated consistently.
