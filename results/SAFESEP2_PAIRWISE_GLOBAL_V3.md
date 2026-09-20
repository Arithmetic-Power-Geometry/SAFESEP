# SAFESEP-II V3 — pairwise/global separation failure

## Proposition

There is a three-world, two-probe instance in which every pair of worlds requiring different decisions is separated by an initially legitimate probe, yet no safely resolving policy exists.

Let `W={0,1,2}`, with three distinct required decisions and initial authority `{x,y}`.

- `p` requires `x`, partitions `{0}|{1,2}`, and revokes `y`.
- `q` requires `y`, partitions `{0,1}|{2}`, and revokes `x`.

Every incompatible pair is initially separable. If `p` is executed first, the unresolved branch `{1,2}` remains but `q` is no longer executable. If `q` is executed first, the unresolved branch `{0,1}` remains but `p` is no longer executable. Hence no first probe succeeds on all branches.

This is the destructive evidence-coupling obstruction reported as Proposition 1 in SAFESEP-II V1.

## Citation

Akhtar, M. A. K. (2026). *Safe Separability under Revocable Authority: Destructive Evidence Coupling, Branch-Conditioned Adaptivity, and a Fixed-Parameter Behavioral Kernel* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22852609
