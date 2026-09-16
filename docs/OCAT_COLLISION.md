# Observation-Conditioned Authority Topology (OCAT) — collision result

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Question
Can two authorization systems have the same initial worlds, decision counts, cheapest unresolved probe, cost, and initial authority graph, yet differ after an observation because that observation changes which authority edge is active?

## Matched witness
Both systems have 2n worlds, n requiring R and n requiring W. Probe `q` costs 1, isolates `r0`, and leaves the other branch decision-critical. Both initially expose the same authority edge `alpha -> r`. In A, observing `q=rest` activates `q:rest -> alpha`; in B it does not. Thus the initial graph matches, but the post-observation authority topology differs. A can then use resolver `r`; B cannot.

The cheapest experiment that leaves mutually incompatible possible worlds remains `q`, cost 1. The residual incompatible-pair count is 9,900 at 200 worlds and 24,995,000 at 10,000 worlds.

## Full-state planning attack
This does NOT establish representational irreducibility. A full-state contingent planner can include the active authority edges/tokens in state, make the observation update that state, and condition resolver applicability on the resulting state. The planner therefore reproduces A=RESOLVABLE and B=BLOCKED exactly.

## Prior-art attack
Dynamic authorization already permits access decisions to depend on changing context. More strongly, Becker (CSF 2009), *Specification and Analysis of Dynamic Authorisation Policies*, studies authorization rules whose actions may depend on and update authorization state, and analyzes finite-domain reachability using AI planning. Therefore observation-conditioned authorization-state change, by itself, is not a breakthrough claim.

## Scientific result
KEEP the matched construction as a permanent negative/collision result: identical initial authority topology does not determine future safe resolvability when observations can update authority state. But DO NOT claim OCAT as a new planning primitive or breakthrough theory.

## Next novelty frontier
The next candidate must survive full-state compilation. A stronger target is a theorem about the *minimum legitimate information needed to determine which authority transition rule applies*, where obtaining that information may itself require authority whose validity differs across still-compatible worlds. This creates a second-order authorization question rather than merely a dynamic state update. It must be attacked against epistemic planning, dynamic authorization, trust negotiation, and policy-information acquisition before promotion.

## Empirical boundary
The 10,000-world benchmark is controlled theorem data. Existing real authorization datasets do not provide counterfactual observation-conditioned authority-transition ground truth, so no real rows are relabeled to fabricate it.
