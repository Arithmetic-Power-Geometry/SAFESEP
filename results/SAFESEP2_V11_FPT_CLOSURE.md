# SAFESEP-II V11 final parameter-monotonicity closure

## Purpose
Close the final formal gap in the dynamic behavioral-kernel FPT argument: prove that the parameters controlling the behavioral universe cannot grow along a descendant branch.

Let an initial normalized state be Q0=(P0,A0,U0). For any state Q=(P,A,U) reachable from Q0 under the restricted SAFESEP-II semantics, define:
- W(P): worlds appearing as endpoints of obligations in P;
- R(U)=union_{e in U} Req(e).

## Lemma 5 — obligation monotonicity
For every reachable descendant, P subseteq P0. Consequently W(P) subseteq W(P0).

### Proof
An observation update never creates an incompatible pair. For outcome o it retains exactly those existing pairs whose two endpoints both yield o:
    P_o = { {u,v} in P : O_e(u)=O_e(v)=o }.
Therefore P_o subseteq P. Induction along the execution path yields P subseteq P0. Endpoint monotonicity follows immediately. QED.

## Lemma 6 — relevant-token monotonicity
For every reachable descendant, R(U) subseteq R(U0).

### Proof
One-shot execution only removes probes: U' = U \ {e}. Probe requirements are fixed by the model and execution creates no new probes. Hence
    R(U') = union_{f in U'} Req(f)
           subseteq union_{f in U} Req(f)
           = R(U).
Induction gives R(U) subseteq R(U0). Grants may add a token to authority A, but they do not add that token to R(U); relevance is defined by requirements of remaining probes. QED.

## Lemma 7 — parameter monotonicity
Let k0=|P0| and r0=|R(U0)|. Every reachable normalized state has at most k0 obligations, at most 2k0 obligation endpoints, and at most r0 relevant authority tokens.

This follows from Lemmas 5 and 6.

## Theorem — bounded dynamic behavioral universe
At every reachable state, the number of behavioral probe types is at most
    T(k0,r0) = Bell(2k0) * 2^(3r0).

### Proof
By Lemma 7, a probe observation induces a partition on at most 2k0 relevant worlds, giving at most Bell(2k0) partition signatures. Requirement, grant, and revoke components restricted to the relevant-token universe each have at most 2^r0 signatures. Multiplication gives the bound. QED.

## Corollary — restricted SAFESEP-II is FPT in k+r
Under assumptions 1–7 of SAFESEP2_V11_FORMAL_PROOF_FREEZE.md, explicit finite safe resolvability is fixed-parameter tractable for parameter
    p = k0 + r0.

### Algorithm
1. Construct P0 and R(U0) in polynomial time from the explicit instance.
2. At every search state, project to surviving obligations and relevant authority.
3. Canonicalize remaining probes by dynamic behavioral type and retain one representative per type.
4. Memoize normalized states and perform exact AND/OR recursion.

After Step 3, at most T(k0,r0) probe representatives remain. A normalized state is described using:
- a subset of at most k0 obligations;
- a subset of at most r0 authority tokens;
- a subset of at most T(k0,r0) behavioral representatives/types.

A deliberately coarse state bound is therefore
    2^k0 * 2^r0 * 2^T(k0,r0),
which is a computable function solely of p because k0<=p and r0<=p. Transition generation and initial canonicalization are polynomial in the explicit input size. Hence running time has form
    f(p) * poly(|I|).
Therefore the restricted problem is FPT parameterized by k0+r0. QED.

## Scope
This theorem is ONLY for:
- explicit finite worlds;
- deterministic observations;
- one-shot probes;
- world-independent requirements/grants/revocations;
- idempotent set-valued authority update;
- no hidden side effects beyond observation, authority update, and probe consumption.

The theorem does not cover stochastic/reusable probes, quantitative resources, world-dependent authority effects, dynamically created probes, or arbitrary state-changing actions.

## Status
The mathematical parameter-growth gap identified in V11 is closed. Remaining gates are empirical/software verification and prior-art positioning, not an unresolved step in this proof chain.
