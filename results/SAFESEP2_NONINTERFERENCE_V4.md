# SAFESEP-II autonomous pass V4 — static noninterference certificate

## Candidate positive result
Define a static noninterfering separator cover S at the initial state:
1. every probe in S is initially legitimate;
2. S separates every decision-incompatible world pair;
3. for distinct e,f in S, revoke(e) is disjoint from require(f).

### Proposition (soundness)
If such a cover exists under world-independent authority effects and one-shot probes, the instance is safely resolvable.

### Proof sketch
Execute probes from S in any order until the current branch is decision-homogeneous. Condition 3 ensures executing a selected probe never destroys the authority required by another unexecuted selected probe. Thus every selected probe remains executable when reached. If two worlds with different required decisions survived all selected observations, S would fail to separate that pair, contradicting condition 2. Hence every terminal branch is decision-homogeneous.

This is a sufficient certificate, not an iff characterization. It deliberately trades completeness for a polynomially/checkably structured witness when S is supplied.

## Falsification programme
A complete 3-world/2-probe deterministic binary-observation battery is added. Probe types range over 8 outcome maps x 3 requirement choices (none/x/y) x 3 revocation choices (none/x/y) = 72 types; ordered pairs give 5,184 systems. Every system certified by the static noninterference condition must be accepted by the exact AND/OR oracle.

## Why this is not yet enough
The certificate can reject resolvable systems whose useful probes interfere syntactically but where observation branching makes the conflict irrelevant. Therefore the likely paper-level object is branch-relative noninterference, not this static certificate.

## Next attack
Search automatically for the smallest exact-resolvable system rejected by the static certificate. Classify why it resolves. Use that witness to define branch-relative noninterference, then test whether the strengthened certificate is exact on complete small universes.

## Paper gate
NO PAPER YET. The paper gate opens if branch-relative noninterference becomes an exact characterization for a meaningful revocation class, or if its failure yields a sharp complexity/parameterized-complexity boundary.
