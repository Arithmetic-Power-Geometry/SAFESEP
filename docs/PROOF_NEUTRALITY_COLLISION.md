# Proof-neutrality collision — DNAC prior-art attack

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Question
Is the current Decision-Neutral Authority Closure (DNAC) criterion itself a new authorization-proof principle?

## Prior-art attack
No broad claim is defensible. Delegation Logic and related trust-management systems already treat authorization as proof-of-compliance and use logic-programming semantics; well-founded semantics and restrictions on cyclic dependencies are established. Proof-carrying authorization explicitly constructs and checks authorization proofs, and implementations guard against cyclic proof/module structures. Automated trust negotiation explicitly studies circular credential-policy dependencies and deadlock.

Therefore SAFESEP must not claim novelty for non-circular authorization proofs, proof provenance, cyclic-dependency detection, or well-founded authorization semantics by themselves.

## Executable collision
`src/safesep/proof_neutral.py` compiles a simple proof-dependency model into the current DNAC Boolean admissibility map. A proof is decision-neutral when its premise set avoids the unresolved decision literals. A probe is neutral when at least one valid authorization proof is neutral.

Tests 24–26 establish:
1. if every proof of the resolving probe depends on a disputed decision literal, the DNAC obstruction is reproduced;
2. if even one alternative proof is independent of the disputed decision, resolution is restored;
3. the compilation reproduces the obstruction on 10,000 explicit worlds.

This is a negative novelty result: the *local no-presupposition check* can be represented as authorization-proof dependency analysis.

## Surviving target
The remaining candidate is not local proof acyclicity. It is the **adaptive decision-resolution problem under proof-qualified evidence acquisition**:

- current knowledge induces a decision-critical class C;
- each candidate evidence probe may have multiple authorization proofs;
- only proofs independent of the unresolved decision are eligible;
- observations change C and may change which proofs are available/relevant;
- the objective is a minimum-cost adaptive tree ending when the authorization decision, not necessarily the exact world, is resolved.

Call this **Decision-Relative Authority Closure (DRAC)** / **Authorization Safe Separability with proof-qualified probes** until a final name is selected.

The novelty question is now narrower: does prior work jointly optimize adaptive evidence acquisition for a disputed authorization decision while requiring every evidence-acquisition step to possess a proof whose justification is independent of that same unresolved decision? The components separately are established. A publishable contribution must come from a theorem/complexity/separation about their coupling, not from claiming the components are new.

## Real-data boundary
AuthBench is a real public agent-permission benchmark with 120 tasks, gold read/write/execute permissions, and constrained execution. It is useful for external validity, but it does not label alternative authorization proofs or whether a proof depends on the disputed authorization conclusion. Those labels must not be fabricated. Controlled 10,000-world constructions remain appropriate for theorem stress tests until a real source with proof-dependency ground truth is identified.

## Stop criterion
Do not stop novelty search yet. Stop and write when at least one coupling-specific theorem survives comparison with trust negotiation, proof-carrying authorization, authorization logic, contingent/epistemic planning, and adaptive diagnosis—preferably accompanied by a complexity or irreducibility result that is not merely inherited from those ancestors.
