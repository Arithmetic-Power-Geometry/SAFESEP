# SAFESEP-II autonomous pass V11 — dynamic type quotient and FPT route

## Dynamic duplicate-type theorem candidate
At every normalized state, recompute behavioral probe types using:
- the worlds that remain endpoints of unresolved decision obligations;
- authority tokens appearing in requirements of remaining probes;
- requirement/grant/revoke signatures on those tokens;
- the induced observation partition on relevant worlds.

Then retain one representative of each type.

### Candidate theorem
For deterministic one-shot probes with idempotent set-valued world-independent authority effects, dynamic retyping and duplicate elimination preserve exact safe resolvability.

## Proof skeleton
Induct on the number of distinct remaining behavioral types.

If probes e and f have identical type at state Q, they have identical executability, authority transition on all currently relevant tokens, and observation partition on all worlds participating in unresolved obligations. Any policy beginning with f can begin with e and reach quotient-equivalent children.

After executing e, f cannot provide new information on a descendant branch: restricting identical parent partitions to a subset keeps them identical. Relevance pruning may erase tokens or merge additional probe types, but cannot distinguish e from f. Since the authority update is idempotent set union/minus, repeating f after e cannot produce an authority state unavailable after e solely because f is a duplicate. Hence one representative suffices recursively.

## FPT consequence if theorem is finalized
Let k be the number of unresolved incompatible pairs and r the number of relevant authority tokens.

There are at most 2k relevant world endpoints. A deterministic probe's observation behavior is a partition of those endpoints, so there are at most Bell(2k) observation types. Requirement, grant, and revoke components each have at most 2^r signatures.

Therefore the number of behavioral probe types is bounded by
    T(k,r) <= Bell(2k) * 2^(3r).

After dynamic deduplication, at most T(k,r) probes need be represented. The normalized state space is then bounded by a computable function of k+r alone (very large but parameter-only), while initial type construction scans the input probes polynomially.

This gives a credible FPT algorithm parameterized by k+r:
    f(k+r) * poly(|I|)
for the restricted deterministic explicit SAFESEP-II model.

## Why wording must remain careful
The bound is theoretical, not practical. It depends on explicit finite worlds/probes, deterministic outcomes, one-shot probes, idempotent set-valued grants/revocations, and world-independent authority effects. General planning parameterized-complexity results remain neighboring prior art; novelty must be the authorization/evidence semantics and the specific obligation-authority-type kernel, not 'FPT planning' in general.

## Computational falsification
Added a dynamic type-quotient solver that retypes/deduplicates after every observation branch and compares against the independent exact AND/OR solver on:
- the harmless global-cycle V6 instance;
- an exhaustive 1,728-instance three-world slice with duplicate probes, arbitrary binary observations, requirements, revocations, and repeated decision labels.

## Paper gate
CONDITIONAL OPEN.
If CI passes and a focused prior-art attack finds no equivalent obligation-authority behavioral kernel theorem for revocable authorization-sensitive evidence, begin drafting SAFESEP-II now. Do not wait for more theorem invention before drafting; remaining work should be proof hardening, larger exhaustive validation, and a controlled Android/MCP realization.
