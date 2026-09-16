# Decision-Neutral Authority Closure (DNAC) — novelty attack

## Result

The previous Justification-Relative Safe Separability (JRSS) direction collides substantially with established authorization work. History-based access control already makes authorization depend on past security-sensitive events; purpose/consent models make permission depend on purpose and conditions; proof-carrying authorization supports distributed proofs, sessions and iterative challenges; automated trust negotiation protects sensitive credentials with access-control policies and explicitly studies cyclic disclosure dependencies. Provenance-aware access control and 2026 agent authorization evidence-chain work further weaken any claim that provenance itself is new.

Therefore SAFESEP does **not** claim novelty for history-, provenance-, purpose-, consent-, delegation-, proof-, or credential-dependent authorization.

## Surviving narrower candidate

Let C be a decision-critical set of worlds: at least two worlds in C require incompatible authorization decisions. A probe e is **decision-neutral admissible on C** when the authorization basis for executing e is valid without presupposing which of those unresolved decisions is correct.

This is stronger than extensional state-wise applicability. A probe may happen to be permitted in every actual world while still fail decision-neutral admissibility if the only justification for permission depends on assuming the very decision that the probe is supposed to resolve.

Define DN-SafeSep(C) as the minimum worst-case cost of an adaptive tree whose probes are decision-neutral admissible on every current branch and whose leaves are decision-homogeneous. If no such tree exists, DN-SafeSep(C)=infinity.

## Matched construction

Use n READ worlds and n WRITE worlds. Probe q costs 1, is decision-neutral, isolates r0, and leaves a decision-critical residual branch. Probe resolve costs 1 and perfectly reveals READ versus WRITE.

Construct two systems with identical worlds, decisions, outcomes, costs and ordinary information structure. In N, `resolve` has a decision-independent authorization basis. In P, `resolve` has only a decision-presupposing basis. Then N is decision-neutrally separable while P is not.

The computational regression suite checks this construction through 10,000 explicit worlds.

## Cheapest experiment question

For the blocked construction the cheapest decision-neutral informative probe that still leaves mutually incompatible worlds is q at cost 1. This explicitly answers the recurring diagnostic without confusing it with the full safe-separability objective.

## Why this may be different

The candidate contribution is not that a planner cannot encode an extra Boolean predicate. A sufficiently expressive planner can encode almost any finite policy state. The candidate is a normative and structural authorization distinction: **extensional permission is not sufficient when the proof of permission presupposes the unresolved authorization conclusion.** This resembles non-circular justification/proof obligations more than ordinary action applicability.

## Prior-art boundary

Closest established neighbors found in the current attack:
- automated trust negotiation: protected credentials, iterative disclosure, and cyclic credential-policy dependencies;
- proof-carrying authorization: distributed policy proof search and iterative authorization;
- history-based access control: policies over past security-sensitive behavior;
- purpose/consent/provenance access control: permission depends on purpose, consent, provenance and conditions;
- evidential transaction logics: distributed construction of authorization evidence;
- recent agent authorization evidence chains and evidence-qualification receipts.

These ancestors mean that circular evidence disclosure and provenance-aware authorization cannot be claimed as new.

## Current novelty status

DNAC / decision-neutral safe separability is a **surviving theorem candidate**, not yet a breakthrough claim. The decisive next attack is against non-circular proof theory, authorization logics with recursive credentials, well-founded semantics, trust-management policy cycles, and justification logic. If an existing formalism already imposes the same no-presupposition criterion, the claim must narrow again. If not, the matched construction plus a formal non-circularity theorem may be sufficient to stop novelty hunting and write the paper.
