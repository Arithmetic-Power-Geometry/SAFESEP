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
- a **one-directional BRAC soundness result** under the stated monotone, world-independent model; and
- a reproducibility package with 266 permanent tests.

Important: the paper intentionally does **not** claim a proved BRAC iff-completeness theorem. In the published manuscript, Theorem 2 proves only that each BRAC transition is a legitimate exact transition and that BRAC cannot create unsupported authority on the same branch. Agreement of BRAC with exact joint-state search is reported as computational evidence within the implemented model.

## Validation reported in the paper

The final computational artifact includes:

- 266 permanent regression tests;
- exhaustive comparison over 256 four-world outcome systems;
- 1,250 deterministic randomized certified comparisons;
- controlled stress tests up to 10,000 explicit worlds;
- exact-solver comparisons whenever tractable; and
- CI validation on Python 3.10, 3.11, and 3.12.

The controlled cheapest-unresolved diagnostic reports residual incompatible-pair counts of 9,900; 249,500; 999,000; 6,247,500; and 24,995,000 for 200, 1,000, 2,000, 5,000, and 10,000 worlds, respectively, in the stated witness family.

These values are family-specific. In a separate stronger-bit family, an equal-cost probe can leave fewer incompatible pairs, so probe q is not claimed to be universally optimal.

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

Some historical files preserve the chronological falsification process and retain names such as “attack,” “collision,” or “freeze.” They are archival research records rather than current manuscript instructions.

In particular, `results/BRAC_COMPLETENESS_AND_COMPLEXITY.md` is a post-paper research note exploring a stronger iff/completeness claim for the repository's restricted monotone model. That stronger result is **not part of the published V1 paper** and should not be cited as a claim of the manuscript unless separately proved, audited, and incorporated in a future version.

The authoritative claims, assumptions, counts, limitations, and reproducibility statements for V1 are those in the published paper and this README.

## Data and code availability

The source code, tests, controlled datasets, benchmark scripts, and result artifacts supporting the paper are contained in this repository.

The paper distinguishes controlled theorem-level data from real authorization benchmarks. AuthBench is used only as external-validity context because it does not provide the counterfactual world-by-probe legitimacy and authority-transition labels required for direct SAFESEP theorem evaluation. Missing semantics are not fabricated.

## Reproducibility correspondence

The repository corresponds to the paper's reported workflow:

- exact joint-state search is the reference oracle;
- MCAS closure exactness is tested inside its declared restricted class;
- the naive global extension is falsified by a four-world informative-grant counterexample;
- BRAC repairs that failure by recomputing branch-constant authority closure after each observation;
- the final BRAC battery preserves the 266-test registry;
- the paper reports exhaustive 256-system comparison, 1,250 deterministic randomized certified comparisons, and controlled scaling up to 10,000 worlds.

## Citation

Akhtar, M. A. K. (2026). *Safe Separability for Autonomous Authorization: Branch-Relative Authority Closure Under Decision-Critical Uncertainty* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22828708

## License

See `LICENSE`.
