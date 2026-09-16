# Matched-Cost Branchwise Coupling Attack — Tests 99–102

## Question
Can we remove the trivial explanation behind the earlier unbounded premium construction—namely that the safe system simply had to acquire more costly credentials—while preserving a SAFESEP separation?

## Construction
For each n, systems A_n and B_n have exactly the same:

- 2n worlds and n/n authorization decisions;
- diagnostic experiment q and q cost 1;
- q outcome partition (r0 vs all remaining worlds);
- n resolver actions;
- unit resolver costs;
- unconstrained information optimum 1;
- per-world existence of a unit-cost legitimate resolver witness.

Only the world×resolver legitimacy incidence relation changes.

In A_n, one unit-cost resolver is legitimate throughout the unresolved q=rest branch. In B_n, legitimacy is dispersed: each world has a unit-cost witness, but no single resolver is legitimate throughout the still-compatible branch.

## Result
The cheapest informative experiment that still leaves incompatible worlds remains

    q, cost 1.

It leaves (n-1)n incompatible R/W pairs: 9,900 at 200 worlds and 24,995,000 at 10,000 worlds.

After q=rest, A_n has a common unit-cost resolver; B_n does not. In the restricted one-step resolver class used here:

    safe_after_q(A_n) = 1
    safe_after_q(B_n) = infinity.

Thus equal action counts, equal action costs, equal local witness existence, equal ordinary information structure, and equal unconstrained optimum do not determine safe completion. The coupling relation matters.

## Prior-art attack
This is stronger than the earlier cost-padding family, but it is not yet promoted to breakthrough novelty.

Automated trust negotiation already studies protected credentials, disclosure policies, negotiation sequences, cycles, and cost-sensitive/minimal disclosure. Conformant and contingent planning already reason over belief states with action applicability constraints. A full joint-state representation can encode the world×resolver legitimacy incidence relation used here.

Therefore the present result is best treated as a matched-cost irreducibility witness against coarse summaries, not as a claim that branchwise applicability or protected evidence negotiation is new.

## What would survive better
The next candidate should prove a representation-independent or restricted-class theorem: e.g. a lower bound on the amount of *common legitimate information* required that is derived from decision-critical pair coverage plus authorization incidence, with a compact certificate or hierarchy not obtained merely by restating full belief-state search.

## Empirical boundary
The 10,000-world rows are controlled theorem stress tests. Public authorization datasets provide real permissions/decisions but generally do not provide counterfactual world×evidence-action legitimacy for all alternative possible worlds. We do not synthesize those labels and call them empirical observations.

## Decision
Do not stop for the paper yet. Tests 99–102 eliminate a trivial cost-padding explanation, but the full relation is still encodable by established planning/trust-negotiation machinery.
