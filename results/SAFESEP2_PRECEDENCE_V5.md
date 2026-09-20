# SAFESEP-II V5 — evidence precedence

For a selected separator family `S`, add a precedence edge `q -> p` whenever `p` revokes a token required by `q`. The edge means that `q` must execute before `p` when both probes are needed on the same execution path.

## Acyclic separator-cover soundness

Under world-independent authority effects, if every selected probe is initially executable, the selected family separates every decision-incompatible pair, and its evidence-precedence graph is acyclic, then the instance is safely resolvable by a topological ordering.

This result appears as Theorem 1 in SAFESEP-II V1. Global acyclicity is sufficient but not necessary because adaptive branching can discharge obligations before conflicting probes become jointly necessary.

The exhaustive validation slice contains 5,184 three-world/two-probe cases.

## Citation

Akhtar, M. A. K. (2026). *Safe Separability under Revocable Authority: Destructive Evidence Coupling, Branch-Conditioned Adaptivity, and a Fixed-Parameter Behavioral Kernel* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22852609
