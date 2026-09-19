# World-Indexed Branch-Relative Authority Closure (WI-BRAC)

## Research question

The current BRAC paper deliberately excludes world-dependent grants because an
unsafe union abstraction can invent authority. WI-BRAC asks whether closure can
be recovered without that abstraction.

## Construction

At branch C, keep an authority vector (A_w) for every w in C rather than one
unioned token set. A probe is branchwise legitimate only when its requirements
hold in every corresponding A_w. If its observation is constant on C, execute
its monotone grant separately in every A_w and iterate to a fixed point. Never
union grants across worlds.

After closure, branch only on genuinely informative probes and recompute
world-indexed closure in every successor.

## Candidate theorem

For finite systems with monotone token-addition effects, no revocation, and
probe requirements evaluated branchwise against the per-world authority state,
saturating all legitimate branch-constant probes by WI-BRAC before each
informative probe is without loss of resolvability relative to exact
world-indexed joint-state search.

### Proof sketch

Take any finite exact resolving tree. On a fixed branch, any legitimate
branch-constant monotone action leaves the compatible-world set unchanged.
Executing additional such actions early only enlarges each world's authority
state and therefore cannot invalidate a token-requirement precondition.
World-dependent grants cause no cross-world leakage because states are retained
componentwise. Saturate these actions, preserve the first informative action,
then apply the argument recursively after each observation. The converse is
immediate because every WI-BRAC closure step is an exact branchwise-legitimate
transition.

## Why this is stronger than BRAC

BRAC's manuscript theorem assumes world-independent authority effects. WI-BRAC
allows the grant set to differ by world while retaining universal legitimacy.
The known false-positive construction from unioning grants remains rejected.

## Novelty gate

This is a **candidate extension**, not yet a breakthrough claim. Broad belief-
state planning, epistemic planning, bisimulation/simulation, trust negotiation,
and dynamic authorization are established prior art. Promotion requires:
(1) exhaustive/random agreement beyond the first finite census;
(2) a proof audit; (3) a systematic literature search for an equivalent
componentwise closure theorem; and (4) a useful authorization example where the
compression is nontrivial.
