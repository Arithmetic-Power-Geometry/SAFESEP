# SAFESEP-II autonomous pass V7 — decision-obligation quotient

## New candidate theorem
For deterministic explicit finite SAFESEP with one-shot probes and world-independent authority transitions, exact safe resolvability depends on the current compatible-world set only through the set of surviving decision-incompatible world pairs, together with current authority and unused probes.

Define
P(C) = {{u,v} subset C : D(u) != D(v)}.

Candidate quotient state:
    Q = (P(C), A, U)
where A is current authority and U the unused probes.

## Why this is smaller in principle
SAFESEP does not need exact world identification. Worlds matter only while they participate in an unresolved pair requiring different decisions. Once a world is in no surviving incompatible pair, retaining it cannot affect whether the authorization decision is determined.

For an observation outcome o, update obligations directly:
    P_o = {{u,v} in P : O_e(u)=O_e(v)=o}.
Pairs separated by the observation disappear. Authority updates exactly as before.

## Theorem candidate: obligation-quotient exactness
Under deterministic outcomes and world-independent authority transitions,
    Resolve(C,A,U) = ResolveQ(P(C),A,U).

### Induction proof skeleton
Base: P(C)=empty iff D is constant on C, exactly the terminal condition.

Step: executable probes depend on A and U, not on discarded same-decision worlds. For probe e and outcome o, an incompatible pair survives in the exact child C_o iff both endpoints have outcome o; this is exactly the quotient update P_o. Authority successor is world-independent, so it is identical in exact and quotient recursions. Thus the AND over outcome branches has the same unresolved obligations and authority states. Induct on |U|.

## Important caveat
The quotient still contains world identities inside pair endpoints. It is not yet a polynomial compression theorem: |P| is O(|C|^2), and adaptive search over subsets of obligations can remain exponential. Its value is conceptual and as a bridge to branch-conditioned precedence.

## Computational attack
Added an independent obligation-state solver and an exhaustive three-world/two-probe comparison slice including repeated decision labels. It must agree exactly with the existing world-state AND/OR solver.

## BCEP interpretation
Branch-conditioned precedence can now be defined over obligations rather than histories: conflicts matter only when the obligations requiring both probes coexist in the same reachable quotient state. This removes irrelevant global precedence cycles such as V6.

## Paper gate
ALMOST, BUT STILL WAIT. Obligation-quotient exactness alone is likely a normalization of belief-state planning. Start Paper II when we add one genuinely stronger result:
1. a non-circular BCEP certificate with an iff theorem for a meaningful revocation class; or
2. a sharp complexity/FPT theorem on the quotient; or
3. a provable asymptotic/state-space reduction that cannot be obtained by ordinary decision-homogeneous belief-state pruning.

At that point draft immediately; the V3/V5/V6 theorem-counterexample chain plus this quotient gives the paper a coherent spine.
