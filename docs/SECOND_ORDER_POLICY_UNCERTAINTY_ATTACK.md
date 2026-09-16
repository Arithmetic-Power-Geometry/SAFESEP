# Second-order policy uncertainty — prior-art attack

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Question
What changes if the still-compatible worlds disagree not only on the required authorization decision, but also on which authorization policy/rule is applicable?

## Diagnostic
The controlled witness retains the permanent cheapest-unresolved diagnostic: q has cost 1. At 200 worlds its rest branch leaves 9,900 decision-incompatible pairs and two policy hypotheses; at 10,000 worlds it leaves 24,995,000 incompatible pairs and two policy hypotheses.

## Result
Policy identity can be included in the latent possible-world state. This is a useful stress test because an observation can leave both decision uncertainty and policy uncertainty.

## Prior-art collision
This does NOT yet establish a breakthrough. Automated trust negotiation already supports runtime access-policy discovery: a client need not know the protecting policy a priori and can discover relevant policy during authorization. Dynamic authorization work also permits actions to depend on and update authorization state and analyzes reachability using AI planning. Epistemic/contingent planning can represent uncertainty over latent state, including a policy identifier, by enlarging the state space.

Therefore merely making the authorization rule unknown is not a new representational primitive. The second-order formulation is retained as a regression boundary, not promoted as novelty.

## Real-data boundary
The 10,000-world rows are controlled theorem stress data. Existing real authorization sources audited by SAFESEP do not supply ground-truth counterfactual policy-hypothesis × evidence-action outcomes and legitimacy labels. We do not fabricate them.

## Next surviving target
A stronger result would have to show an authorization-specific obstruction/invariant that cannot be removed by simply augmenting the planner state with a policy identifier. Candidate direction: self-referential evidence legitimacy, where the evidence needed to establish which policy governs an experiment is itself governed by one of the unresolved policies. This must be attacked against trust negotiation, recursive authorization logics, fixed-point semantics, dynamic epistemic logic, and planning before any novelty claim.

## Verdict
KEEP Tests 61–64 because they permanently delimit the second-order-policy idea. DO NOT call this a breakthrough and DO NOT start the paper yet.
