# Authorization-Safe Evidence Premium

## Definition
For a fixed decision-resolution problem P, define

- U(P): minimum resolution cost when experiment authorization constraints are ignored;
- S(P): minimum resolution cost using only legitimately authorized experiments;
- AP(P)=S(P)-U(P), with AP(P)=infinity when U(P)<infinity but S(P)=infinity.

This quantity measures the additional decision-resolution burden induced by authority constraints. It is not claimed to be a new planning primitive.

## Controlled witness
The permanent cheapest-unresolved diagnostic remains q at cost 1. For n=100 the residual branch contains 9,900 incompatible R/W pairs; for n=5000 (10,000 worlds), 24,995,000.

The unconstrained perfect resolver costs 1 in both cases. In the safe case, authorization requires q before the resolver, so S=2 and AP=1. In the blocked case the resolver never becomes legitimately authorized, so S=infinity and AP=infinity despite U=1.

## Prior-art attack
Cost-sensitive trust negotiation already minimizes weighted credential/policy disclosure cost and has established complexity results. Minimal credential disclosure likewise explicitly seeks the least disclosure sufficient for authorization. Therefore the broad idea 'authorization has an extra evidence/disclosure cost' is not itself novel.

The surviving research question must be narrower: can we derive an authorization-specific invariant or lower bound tied to decision-incompatible possible worlds and legitimate evidence acquisition that is not merely a restatement of cost-sensitive trust negotiation or ordinary constrained planning?

## Empirical boundary
The 10,000-world rows are controlled structural stress tests. Real authorization datasets generally do not contain counterfactual world-by-probe authorization labels, so we do not fabricate an empirical authority premium from them.

## Status
Useful quantitative diagnostic, but not yet the stop-and-write breakthrough. Next attack: seek a lower bound based on decision-incompatible pairs that every legitimate evidence path must cut, then compare it directly with set-cover/test-cover, decision-region determination, trust-negotiation cost, and constrained planning lower bounds.
