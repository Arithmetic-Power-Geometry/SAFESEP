# SAFESEP-II autonomous pass V10 — duplicate behavioral probe types

## Candidate lemma: duplicate-type elimination
At a normalized state, define the behavioral type of a remaining deterministic probe by:
1. requirements restricted to relevant authority tokens;
2. grants restricted to relevant authority tokens;
3. revocations restricted to relevant authority tokens;
4. its observation partition on worlds that are endpoints of surviving decision obligations.

Outcome labels themselves are irrelevant; only the induced partition matters.

Candidate lemma:
If two unused one-shot probes have the same behavioral type at a normalized state, deleting one preserves safe resolvability.

## Proof idea
Suppose a resolving policy uses both identical-type probes along one path. After the first execution:
- if its observation refines the branch, the second identical observation supplies no additional world separation;
- its authority effect is identical, so reapplying the same set-valued grant/revoke update cannot create a new authority state beyond the first application under the update A'=(A union G) minus R;
- if the first probe was not useful on a branch, the second cannot become observationally more informative because deterministic outcomes are fixed.

Therefore a policy can replace the first occurrence of either duplicate by the retained representative and remove later redundant occurrences.

## Critical caveat
This argument relies on idempotent set-valued authority effects and deterministic observations. It can fail with counters, consumable quantities, time-dependent observations, stochastic sensing, probe-specific side effects, or non-idempotent transitions.

## Why this matters for complexity
If the lemma is valid, named multiplicity of identical probes is irrelevant. The unused set U can be represented by distinct behavioral types rather than m arbitrary identities.

For at most 2k obligation endpoints and r relevant tokens:
- requirement signatures: <= 2^r;
- grant signatures: <= 2^r;
- revoke signatures: <= 2^r;
- observation partitions: Bell(2k) in the unrestricted finite-outcome case (or <=2^(2k) coarse bound for binary signatures up to complement).

Thus the number of behavior types is bounded solely by k and r. This is the first credible route to an FPT algorithm parameterized by k+r, although a full dynamic argument is still required because relevance and type signatures change after branching.

## Falsification
Added canonical type computation, duplicate elimination, a direct regression, and an exhaustive small slice comparing the exact solver before/after adding a behavioral duplicate.

## Paper gate
VERY CLOSE, BUT WAIT FOR ONE MORE PASS. If we prove that dynamic retyping after every normalized transition preserves duplicate elimination and derive an explicit FPT algorithm f(k+r)*poly(input), start writing Paper II. That would be a substantially stronger contribution than the normalization results alone.
