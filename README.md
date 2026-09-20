# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright © 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for authorization-sensitive evidence acquisition under decision-critical uncertainty.

## Published paper

Akhtar, M. A. K. (2026). *Safe Separability for Autonomous Authorization: Branch-Relative Authority Closure Under Decision-Critical Uncertainty* (Version V1). Zenodo.

DOI: https://doi.org/10.5281/zenodo.22828708

## Core problem

SAFESEP asks whether an autonomous agent can resolve an authorization decision when the evidence required to distinguish still-possible worlds is itself authorization-sensitive.

A policy is safe only when every probe used on a branch is legitimate in every world still compatible with that branch. The target is decision resolution, not necessarily exact world identification.

## Main results in the paper

The published SAFESEP paper develops:

- exact joint knowledge-authority recursion as the reference semantics;
- a cheapest-unresolved-experiment diagnostic for controlled witness families;
- the restricted Monotone Closure-then-Authorized Sensing (MCAS) class;
- an exact closure result for finite MCAS instances;
- counterexamples showing why naive closure fails with informative authority progress, world-dependent grants, and revocation;
- Branch-Relative Authority Closure (BRAC), which recomputes authority closure after each observation relative to the surviving compatible-world branch;
- a sound BRAC normalization result under the stated monotone, world-independent model; and
- a reproducibility package with 266 permanent tests.

## Validation reported in the paper

The final computational artifact includes:

- 266 permanent regression tests;
- exhaustive comparison over 256 four-world outcome systems;
- 1,250 deterministic randomized certified comparisons;
- controlled stress tests up to 10,000 explicit worlds;
- exact-solver comparisons whenever tractable; and
- CI validation on Python 3.10, 3.11, and 3.12.

The controlled cheapest-unresolved diagnostic reports residual incompatible-pair counts of 9,900; 249,500; 999,000; 6,247,500; and 24,995,000 for 200, 1,000, 2,000, 5,000, and 10,000 worlds, respectively, in the stated witness family.

## Model boundary

The paper's BRAC analysis assumes monotone, world-independent authority effects. Explicit counterexamples show that world-dependent grants and revocation require richer semantics.

The paper does not claim that BRAC is a complete solution for:

- revocable authority;
- world-dependent grants;
- stochastic observations;
- reusable probes;
- quantitative or consumable authority resources;
- dynamically created probes; or
- arbitrary hidden side effects.

A formal complexity classification beyond the executable finite-state recursion is left outside this paper.

## Repository organization

- `src/` — exact SAFESEP, MCAS, BRAC, diagnostics, and supporting code.
- `tests/` — permanent regression, exhaustive, randomized, and boundary tests.
- `data/` — controlled datasets and benchmark outputs.
- `results/` — retained result records, theorem checks, counterexamples, and historical development logs.
- `docs/` — supporting technical notes and prior-art positioning.
- `android-probe/` — limited controlled Android sanity material; Android/Pixel temporal-authority research is maintained separately in the Android Temporal Authority Lab.

Some historical files preserve the chronological falsification process and retain names such as “attack,” “collision,” or “freeze.” These are archival research records rather than current manuscript instructions. The authoritative claims, assumptions, counts, and limitations are those in the published V1 paper and this README.

## Data and code availability

The source code, tests, controlled datasets, benchmark scripts, and result artifacts supporting the paper are contained in this repository. Real authorization benchmarks are used only where their published fields directly support the reported analyses; missing counterfactual legitimacy or authority-transition semantics are not fabricated.

## Citation

Akhtar, M. A. K. (2026). *Safe Separability for Autonomous Authorization: Branch-Relative Authority Closure Under Decision-Critical Uncertainty* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22828708

## License

See `LICENSE`.
