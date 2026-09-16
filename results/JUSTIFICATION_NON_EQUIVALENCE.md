# Justification Non-Equivalence Attack — Tests 73–76

## Question
Can two authorization systems expose the same extensional authorization relation yet differ because one authorization conclusion has a grounded finite justification while the other is supported only by a cycle?

## Matched construction
A and B have the same worlds, R/W decisions, q outcome partition, q cost, and extensional `authorized=True` bit. A has an axiom `credential` and edge `credential -> authorize`. B has only `authorize -> support -> authorize`, with no grounded axiom.

Under least-grounded proof closure, A derives `authorize`; B does not. Thus extensional authorization alone is insufficient to certify legitimate authorization provenance.

## Cheapest experiment diagnostic
The cheapest informative experiment that still leaves a decision-incompatible branch remains q at cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at the controlled 10,000-world scale.

## Prior-art attack
This result is NOT claimed as a breakthrough. Proof-carrying authorization already makes formal proofs first-class authorization evidence, and classic PCA systems mechanically fetch proof components until a valid proof is constructed. Formally founded trust-management systems likewise define authorization through rigorous logical semantics. Therefore distinguishing a grounded proof from unsupported circular justification belongs to established proof/authorization semantics unless SAFESEP can prove a stronger result about safe evidence acquisition that is not reducible to proof validity or augmented planner state.

Relevant boundary literature includes Bauer/Schneider/Felten/Appel on proof-carrying authorization, proof-theoretic authorization logic, and formally founded trust-management authorization. General cyclic-proof theory also shows that cycles are not automatically invalid: cyclic proofs may be sound under global progress conditions. Therefore SAFESEP must not equate graph cyclicity with illegitimacy in general.

## Decision
Retain Tests 73–76 as a permanent negative-boundary regression. Do not stop for the paper. Next candidate must concern acquisition of proof components under authorization constraints while matching ordinary proof existence/proof graph summaries, and it must survive iterative PCA, hidden-policy modules, privacy-aware PCA, trust negotiation, and full-state planning.

## Data status
`data/justification_non_equivalence.csv` is a controlled theorem benchmark, not production authorization telemetry. Public benchmarks do not provide ground-truth counterfactual proof-acquisition legitimacy labels; none are fabricated.
