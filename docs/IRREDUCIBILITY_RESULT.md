# Matched-Summary Irreducibility Result

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Construction

Systems A and B each contain four possible worlds, the same required authorization decisions `(R,R,W,W)`, two experiments with the same costs `(1,1)`, and exactly the same outcome maps. Experiment `e1` is universally admissible in both systems and partitions the worlds as `{w1} | {w2,w3,w4}`. Experiment `e2` partitions authorization decisions as `{w1,w2} | {w3,w4}` and is admissible in exactly three worlds in each system.

The only difference is the incidence pattern of admissibility:

- **A (finite):** `Adm(e2)={w2,w3,w4}`. After outcome `b` of `e1`, `e2` is safe on the entire residual branch and resolves R versus W. Thus `SafeSep(A)=2`.
- **B (infinite):** `Adm(e2)={w1,w3,w4}`. After outcome `b` of `e1`, world `w2` remains possible, so `e2` is not admissible on the residual branch. No informative safe probe remains. Thus `SafeSep(B)=infinity`.

## Matched quantities

A and B have identical:

1. number and identity of worlds;
2. required authorization decisions;
3. experiment names and costs;
4. complete experiment outcome maps;
5. root-level admissibility counts;
6. unconstrained optimal decision-resolution cost (=1);
7. one-step closed resolution cost (=infinity).

Yet their SafeSep values differ: `2` versus `infinity`.

## Proposition (coarse-summary insufficiency)

No function of the matched quantities above can determine safe authorization resolvability on all finite instances.

### Proof

Assume a function `F` of only those quantities determines whether SafeSep is finite. Systems A and B have identical inputs to `F`, so `F(A)=F(B)`. But A is safely separable and B is not. Contradiction.

The missing information is the branchwise incidence relation between possible worlds and probe admissibility. Counting permissions, experiment costs, unconstrained information, or one-step closed resolvability is therefore insufficient.

## Important scope

This is an irreducibility result relative to the explicitly listed summaries. It is **not** a claim that SAFESEP cannot be represented by any existing formalism, nor a proof of worldwide novelty. Active diagnosis already optimizes adaptive diagnostic controllers, and authorization-workflow research already studies obstruction. SAFESEP's candidate distinction is that diagnostic/evidence actions have world-dependent authorization and the target is authorization-decision homogeneity rather than exact state identification.
