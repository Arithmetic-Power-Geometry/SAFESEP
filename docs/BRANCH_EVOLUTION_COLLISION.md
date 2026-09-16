# DRAC branch-evolution separation — result and collision audit

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Construction
For n READ worlds and n WRITE worlds, q costs 1 and isolates r0 while leaving a decision-critical residual set of size 2n-1. The resolver also costs 1 and perfectly separates READ from WRITE.

Systems A_n and B_n have the same worlds, decisions, root cheapest eligible experiment q, q cost, q outcome partition, resolver outcome map, resolver cost, proof count, and root resolver eligibility (false in both).

The only difference is the branch-relative proof activation condition. In A_n the resolver becomes eligible once the belief contracts to 2n-1 worlds. In B_n it requires contraction to at most 2n-2 worlds. Therefore after q's residual outcome:

- A_n: resolver eligible, hence DRAC resolution exists;
- B_n: resolver remains ineligible and no other informative probe exists, hence DRAC resolution fails.

This holds through the explicit 10,000-world stress test.

## Cheapest experiment
At the root of both systems, the cheapest eligible informative experiment that still leaves mutually incompatible possible worlds is q with cost 1.

## Novelty attack
This result is structurally useful but is **not yet a breakthrough theorem**. Stateful Authorization Logic already permits authorization policies to depend on interpreted predicates over system state, and proof-carrying authorization already supports iterative proof-component acquisition/challenges. A sufficiently expressive contingent planner can augment its belief state with proof-eligibility/policy state. Consequently branch-dependent proof eligibility by itself is representable by established machinery.

The result therefore falsifies a broader novelty claim: dynamic proof eligibility alone is not enough.

## Surviving frontier
A stronger contribution must constrain *why* proof eligibility changes, rather than merely allow it to change. The next candidate should make the authorization certificate depend on evidence whose legitimate acquisition is itself governed by the unresolved authorization relation, and should seek a structural invariant not eliminated by compiling policy/proof state into an enlarged planning state.

Tests 27-29 preserve this result as a permanent regression and collision witness.
