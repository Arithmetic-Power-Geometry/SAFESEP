# SAFESEP-II validation status

The published SAFESEP-II V1 validation reports:
- 5,184 acyclic-precedence cases;
- 1,728 dynamic duplicate-quotient cases;
- 5,184 dynamic-type hardening cases;
- 2,500 randomized differential cases using seed `20260919`; and
- three controlled scenario families.

The independent world-state AND/OR solver is the reference oracle. Separate implementations cover the obligation quotient, relevance projection, precedence certificate, and dynamic behavioral reduction.

The validation supports the restricted deterministic one-shot model stated in the paper. It does not extend the theorem to stochastic observations, reusable probes, quantitative resources, world-dependent authority effects, dynamically created probes, time-varying observation maps, or hidden side effects.

## Citation

Akhtar, M. A. K. (2026). *Safe Separability under Revocable Authority: Destructive Evidence Coupling, Branch-Conditioned Adaptivity, and a Fixed-Parameter Behavioral Kernel* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22852609
