# SAFESEP complexity and data boundary

**Copyright © 2026 Mohammad Amir Khusru Akhtar**

## Exact finite recursion

For finite explicit instances, SAFESEP V1 computes resolvability using exact joint-state recursion over compatible-world sets and authority states. This is the reference semantics used throughout the computational evaluation.

The published paper does not claim a complete complexity classification for the general framework. A formal complexity classification beyond the executable finite-state recursion is left for future work.

## Controlled theorem data

The theorem-level experiments require explicit counterfactual semantics: for each world and probe, the implementation must know observation behavior, branchwise legitimacy, and authority transition.

The V1 computational artifact reports:
- 266 permanent tests;
- 256 exhaustive four-world outcome systems;
- 1,250 deterministic randomized certified comparisons; and
- controlled scaling up to 10,000 worlds.

## Real authorization data

Public authorization datasets are useful for external-validity context but generally do not provide the counterfactual world-by-probe semantics required for direct theorem evaluation.

AuthBench is therefore used only as a real authorization benchmark establishing the practical relevance of permission reasoning. Missing counterfactual legitimacy or authority-transition labels are not fabricated.

## Published boundary

The V1 theorem results are restricted to monotone, world-independent authority effects. Revocation and world-dependent grants are explicit counterexamples and are not covered by BRAC's published soundness result.

## Citation

Akhtar, M. A. K. (2026). *Safe Separability for Autonomous Authorization: Branch-Relative Authority Closure Under Decision-Critical Uncertainty* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22828708
