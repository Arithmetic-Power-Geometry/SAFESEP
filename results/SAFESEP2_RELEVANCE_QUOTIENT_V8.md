# SAFESEP-II autonomous pass V8 — relevance-pruned authority quotient

## Candidate theorem: irrelevant-authority erasure
In the explicit deterministic one-shot model with world-independent authority transitions, authority tokens that do not occur in the requirement set of any remaining probe can be erased from the state without changing safe resolvability.

Let U be the unused probes and
    R(U) = union_{e in U} Req(e).
Define the pruned authority
    A|U = A intersect R(U).

Then the candidate invariant is
    Resolve(P,A,U) = Resolve(P,A|U,U).

## Proof
Future executability of a remaining probe e depends only on whether Req(e) is contained in A. Tokens outside R(U) occur in no remaining requirement and therefore cannot affect this predicate for any future action. Grants or revocations of such tokens likewise cannot affect future executability. Observation partitions are authority-independent in the restricted model. After executing a probe, repeat the same projection against the new unused set. Induction on |U| yields equality of the exact and relevance-pruned recursions.

## Combined quotient
The exact state may therefore be normalized to
    Q* = (P(C), A intersect R(U), U)
where P(C) is the surviving set of decision-incompatible pairs.

This removes:
- observation history beyond surviving decision obligations;
- worlds irrelevant to any unresolved decision conflict;
- authority tokens irrelevant to all future probe requirements.

## What this does NOT prove
It does not yet remove U, and it does not make the general adaptive search polynomial. It is an exact state normalization, not yet a complexity breakthrough.

## BCEP consequence
Precedence edges caused by revoking token t are irrelevant once t is absent from R(U) on that branch. Thus evidence can erase authority conflicts in two independent ways:
1. observations discharge incompatible-pair obligations;
2. execution removes probes, shrinking R(U), so authority dimensions themselves become irrelevant.

## Falsification
Added an independent relevance-pruned solver and exhaustive three-world/two-probe comparison slice with all binary observation maps and all requirement/grant/revoke choices for one probe, including a deliberately irrelevant token "dead".

## Paper gate
DO NOT write the full paper yet. We now have a strong normalization chain, but standard planning/state-abstraction literature may subsume parts of it. The next decisive target is complexity:
- derive an explicit upper bound in terms of number of incompatible pairs k, relevant authority tokens r, and probes m;
- test whether the problem is fixed-parameter tractable in k+r, or whether U/history of unused probes prevents FPT;
- seek a lower-bound reduction if FPT fails.

If a sharp parameterized boundary survives prior-art review, begin writing immediately.
