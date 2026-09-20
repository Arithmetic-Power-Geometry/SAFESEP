# SAFESEP-II autonomous pass V9 — complexity gate

## Exact finite upper bound
From V8 the normalized state is
    Q* = (P, A_rel, U)
with at most k incompatible-pair obligations, r relevant authority tokens, and m probes.

A direct memoized exact search therefore has at most
    2^k * 2^r * 2^m = 2^(k+r+m)
normalized states, before polynomial transition-processing factors.

This is an exact finite upper bound, not a tractability claim.

## Important negative conclusion
V8 does NOT imply fixed-parameter tractability in k+r.

Reason: the unused-probe component U has up to 2^m possibilities. Unless U can be eliminated/compressed, the direct algorithm is exponential in m even when k+r is fixed. Therefore claiming
    f(k+r) poly(m)
would currently be unjustified.

This is an important paper-safety result: do not advertise FPT(k+r).

## Bounded-depth positive result
If the resolving policy is restricted to depth ell, only unused sets obtained after at most ell executed probes are reachable. Their number is at most
    sum_{i=0}^ell C(m,i).
Thus a memoized normalized search has state bound
    2^(k+r) * sum_{i=0}^ell C(m,i).

For fixed ell this is polynomial in m, but parameterized by ell the factor m^ell is XP-style, not an FPT bound f(k+r+ell) poly(m). Do not mislabel it FPT.

## Research consequence
The decisive question is now whether unused probes can be quotiented by behavioral type.

Two remaining probes are candidate-equivalent at a quotient state if they have the same:
- requirement set over relevant tokens;
- grant/revoke effect over relevant tokens;
- observation partition over endpoints of surviving obligations.

If multiplicity beyond a bounded number per behavioral type is irrelevant in the one-shot deterministic model, U may compress from an arbitrary subset of m named probes to a bounded vector/set of types controlled by k and r. THAT could yield an FPT result.

## Next theorem target
Prove or falsify:
    duplicate-type elimination:
    at any normalized state, retaining one representative of each identical behavioral probe type preserves safe resolvability.

If true, the number of distinct binary observation signatures over at most 2k obligation endpoints is finite as a function of k, and authority requirement/effect signatures are functions of r. This opens a genuine route to FPT in k+r (subject to outcome alphabet/partition encoding).

## Prior-art caution
Parameterized planning is a mature area; published classifications show both FPT and W-hard cases under different restrictions. Any SAFESEP-II parameterized result must therefore be stated for our exact revocable-evidence semantics and compared carefully with those planning results.

## Paper gate
DO NOT write yet. We have now ruled out one tempting overclaim and identified the precise missing lemma. Start the paper immediately if duplicate-type elimination survives proof + exhaustive attack and yields a valid f(k+r) poly(input) algorithm, or if its failure produces a hardness construction showing why named probe multiplicity matters.
