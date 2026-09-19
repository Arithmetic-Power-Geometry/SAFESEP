# SAFESEP-II revocation frontier — autonomous pass V1

## Research question
What non-monotone authority effects can be admitted without losing a sound branch-relative normalization?

## Prior-art attack (19 Sep 2026)
Revocation itself is not a novelty claim. Current neighboring work already treats explicit/cascade agent revocation, revocation closure, edge-revocation targets, and residual authorization state. SAFESEP-II must therefore remain about **decision-critical evidence acquisition whose probes are themselves authorization-sensitive**.

## First surviving lemma: requirement-disjoint revocation commutation
At a joint state (C,A), let e be branch-constant and branchwise legitimate. Suppose:
1. e has world-independent grants and revocations;
2. e leaves C unchanged;
3. every token revoked by e is absent from the requirement set of every probe that may still be used before resolution on C or any descendant branch.

Then moving e earlier cannot disable any later probe solely through its revocation effect. If grants are otherwise treated by the existing world-independent semantics, the revocation component is commutation-safe with respect to future probe applicability.

This is a **sufficient local commutation lemma**, not a completeness theorem. It deliberately does not claim that all safe revocations satisfy the condition.

### Proof
By (3), no future probe in the considered continuation requires a token in revoke(e). Therefore removing revoke(e) from A cannot falsify a future probe requirement. By (1), all compatible worlds receive the same authority update, and by (2) the branch is not changed. Hence the revocation component cannot alter the applicability of any probe in that continuation. The grant component can only be handled under the existing SAFESEP world-independent grant semantics. QED.

## Why this is not yet the paper result
The condition can be conservative: a revoked token may syntactically occur in a probe requirement even though that probe is never needed by any resolving policy. Determining the maximal safe set is therefore policy-dependent and may recover the difficulty of joint planning.

## Breakthrough gate
Do not write SAFESEP-II yet. Continue until at least one survives:
- an iff characterization for a nontrivial revocation class;
- a sharp complexity/parameterized-complexity boundary caused by revocation;
- a minimal-state theorem showing exactly what authority history must be retained for safe resolution, distinct from existing residual-authorization results.

## Next attack
Replace syntactic requirement-disjointness by **resolution-relevant revocation**: a revoked token matters only if every safe continuation for some unresolved decision-incompatible pair needs a probe requiring that token. Search for a cut/duality characterization over incompatible world pairs and authority dependencies.

## Paper gate
Write SAFESEP-II only after theorem + adversarial counterexamples + exact-oracle agreement + prior-art survival. Until then, preserve SAFESEP-I as the paper-ready result and label this branch exploratory.
