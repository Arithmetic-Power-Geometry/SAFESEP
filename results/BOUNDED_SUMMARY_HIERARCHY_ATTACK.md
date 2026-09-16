# Bounded-Summary Hierarchy Attack

## Question
Can every fixed order-k local authorization/proof/acquisition summary be identical while global safe resolvability differs?

## Controlled construction
For each k>=1 construct A_k and B_k with a dependency cycle of length k+1. Every view containing at most k dependencies is intentionally identical. A_k has an external grounding route completing a legitimate acquisition chain; B_k has only the globally closed dependency. Therefore the implemented family has identical summaries through order k but A_k is marked resolvable and B_k blocked.

This is a deliberately controlled structural witness. It is not a real-world empirical authorization dataset and it is not yet a SAFESEP breakthrough theorem.

## Cheapest unresolved experiment
The permanent diagnostic remains q with cost 1. At 200 worlds q leaves 9,900 mutually decision-incompatible pairs. At 10,000 worlds it leaves 24,995,000.

## Prior-art attack
The broad phenomenon is not new. Planning abstractions intentionally merge concrete states into abstract equivalence classes, and an abstraction can lose distinctions needed by the concrete problem. k-wise indistinguishability and local-vs-global consistency phenomena are established across complexity/CSP-style reasoning. Thus the statement 'all bounded local summaries can miss a global property' is too generic to claim as a foundational authorization breakthrough.

The current code also encodes the order-k matching by construction rather than deriving it from the full SAFESEP proof/acquisition semantics. Consequently it is a hypothesis generator and regression witness, not a proof of an authorization-specific hierarchy.

## Novelty decision
DO NOT STOP FOR PAPER on this result. Retain Tests 81-84 as a negative-boundary test. The next required step is to derive an indistinguishability hierarchy from the actual SAFESEP transition/proof-acquisition semantics, then prove that a named natural class of summaries (not an invented summary function) cannot determine SafeSep. A surviving theorem must also be compared with planning abstraction lower bounds, CSP/local consistency, modal depth/bisimulation, and trust-management delegation depth.

## Empirical boundary
No public authorization corpus currently used by SAFESEP supplies counterfactual world-by-probe legitimacy plus multi-level proof-acquisition semantics. The 10,000-world row is controlled theorem stress data; no real rows are relabeled or fabricated.
