# Rule-Validity Coupling Attack

## Question
Can two authorization systems have the same coarse rule-validity marginals yet differ in safe separability solely because rule validity is coupled differently to possible worlds?

## Controlled witness
For 2n worlds, q isolates r0 and leaves a residual branch containing n-1 R worlds and n W worlds. A and B have the same worlds, decision counts, q partition, experiment costs, number of rule-valid worlds, and number of rule-invalid worlds. They differ only in which worlds validate the candidate resolver rule.

The cheapest informative experiment that still leaves incompatible worlds is q with cost 1. The residual branch contains n(n-1) incompatible pairs: 9,900 at 200 worlds and 24,995,000 at 10,000 worlds.

## Negative result
Under SAFESEP's branchwise universal legitimacy requirement, the simple aligned-vs-rotated validity construction does **not** separate A from B: the unresolved q=rest branch contains at least one world in which the resolver rule is invalid in both systems. Thus matched validity marginals plus simple world-rule correlation are not enough.

This is scientifically useful because it kills an attractive but invalid shortcut before it becomes a novelty claim.

## Prior-art attack
Context-dependent, exception-based, incomplete and conflicting authorization policies are established topics. Nonmonotonic access-control formalisms already permit policies to change validity/priority with context and to retract earlier conclusions. Trust negotiation also protects credentials with disclosure policies and reasons about policy satisfaction during negotiation. Therefore world-dependent rule validity by itself is not a breakthrough target.

## Consequence
The next candidate must operate above simple rule validity. A stronger target is **justification non-equivalence**: two systems agree on all extensional policy decisions, rule-validity marginals, dependency graphs and ordinary information partitions, but differ in whether the *same authorization conclusion has a justification that is admissible without circularly presupposing the conclusion*. This should be attacked against argumentation/nonmonotonic proof semantics, proof-carrying authorization, provenance, and epistemic planning before any novelty claim.

## Data status
`data/rule_validity_coupling.csv` is controlled theorem stress data, not production telemetry. Real authorization datasets do not provide counterfactual world-indexed rule-validity/justification labels; such labels must not be fabricated.
