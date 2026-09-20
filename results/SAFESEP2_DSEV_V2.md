# SAFESEP-II autonomous pass V2 — decision-separating evidence viability

## Prior-art correction
Do not use "revocation cut", "revocation closure", cascade revocation, revocable capabilities, or authority-transition receipts as novelty labels. September 2026 adjacent work already uses these concepts for agentic authorization.

SAFESEP-II instead asks an epistemic-authority question: **after authority can disappear, is there still a branchwise legitimate evidence strategy that separates every pair of worlds requiring different authorization decisions?**

## Candidate object: Decision-Separating Evidence Viability (DSEV)
For a joint state (C,A), define an incompatible pair as u,v in C with D(u) != D(v).

A continuation is viable for pair {u,v} when there exists a branchwise legitimate adaptive continuation that, before either world reaches an unresolved terminal state, executes an observation whose outcomes differ on u and v.

DSEV(C,A) holds when every incompatible pair is covered by a single safe adaptive policy, not merely by pairwise policies chosen independently.

The final clause is essential. Independent pairwise witnesses can be mutually incompatible because acquiring or preserving authority for one witness may revoke authority required by another.

## Candidate conjecture V2
A naive conjecture,
    "every incompatible pair has some individually viable separating continuation"
is sufficient for global safe resolvability,
is likely false under revocation.

### Minimal counterexample template to search
Use three decision-relevant worlds and two authority tokens x,y. From initial authority {x,y}, resolving pair P requires consuming/revoking y, while resolving pair Q requires consuming/revoking x. Each pair has an individual witness, but no single adaptive policy may preserve both obligations. Exhaustively search the smallest deterministic instances for this pairwise-to-global failure.

## Stronger target
Represent unresolved obligations as a set P(C) of decision-incompatible world pairs. A state is safely resolvable exactly when there exists a branchwise legitimate action whose authority transition and observation partition send every surviving obligation to successor states that are themselves resolvable.

This recursion is exact but not novel by itself: it is joint-state contingent planning. The research target is to find a nontrivial structural restriction on revocation under which the recursion collapses to a smaller certificate.

Candidate restrictions to falsify in order:
1. one-shot revocation;
2. acyclic token-dependency/revocation graph;
3. laminar authority requirements;
4. bounded number r of revocable tokens;
5. pairwise noninterference among decision-separating witnesses.

## Parameterized-complexity target
If no polynomial characterization survives, test whether explicit finite safe resolvability is fixed-parameter tractable in r = number of revocable tokens, using state (C,A) but enumerating at most 2^r revocation configurations around the monotone closure core. Do not claim FPT until a formal algorithm and bound are proved.

## Paper gate
NO PAPER YET.

Trigger writing only after one of:
A. an iff characterization strictly beyond SAFESEP-I that survives exhaustive counterexample search and prior-art attack;
B. a proved parameterized/complexity frontier with a matching exact algorithm and lower-bound evidence/theorem;
C. a minimal impossibility theorem showing pairwise evidence viability is insufficient, plus a new global certificate that is provably exact for a meaningful restricted class.

Before writing, require:
- exact solver and independent checker agree exhaustively on the smallest complete instance class;
- at least one real controlled MCP/Android sequence instantiates evidence -> authority change -> observation -> authorization decision;
- final prior-art attack finds no equivalent theorem in contingent planning, trust negotiation, revocable capability, or agent authorization literature.
