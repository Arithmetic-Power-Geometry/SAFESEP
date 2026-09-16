# Proof-Component Acquisition-Path Coupling — Tests 77–80

## Result
The matched A/B family has identical worlds, authorization decisions, q partitions, q cost, ordinary proof existence, proof-component count, and coarse proof graph. The cheapest informative experiment that still leaves incompatible worlds is q at cost 1. At 200 worlds its residual branch contains 9,900 incompatible R/W pairs; at 10,000 worlds it contains 24,995,000.

The systems differ only in whether the proof component c can be obtained by a branchwise legitimate route after q=rest. A has an independent acquisition route and resolves; B's route presupposes the resolver authorization it is intended to justify and remains blocked.

## Prior-art attack
This is stronger than merely comparing proof existence, but it is not yet a breakthrough. Classical proof-carrying authorization already supports iterative fetching of distributed proof components and iterative challenges. Automated trust negotiation already searches disclosure sequences for policy-protected credentials, including hidden credentials/policies and cycles. Therefore 'same proof exists, different obtainable proof-component path' overlaps established distributed proof acquisition / trust-sequence machinery.

The surviving SAFESEP-specific question is narrower: can we prove an irreducibility result for branchwise universal legitimacy under uncertainty that remains after representing the complete acquisition state and all protected-component policies? A mere acquisition-path witness is representable by an augmented planner/negotiation state.

## Empirical boundary
The CSV is a controlled theorem stress dataset, not production telemetry. Public authorization datasets do not provide counterfactual proof-component acquisition legitimacy for every compatible world. No such labels are fabricated.

## Decision
Retain Tests 77–80 as a negative/collision boundary. Do not write the paper yet solely on this result.
