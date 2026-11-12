# SAFESEP: supplementary verification for the revised manuscript

This directory contains finite-instance verification code, controlled diagnostic data, and traceable continuous-integration records for the SAFESEP authorization model. The implementation and its permanent regression tests are located in the repository's `src/safesep/` and `tests/` directories.

## Reproduction

The independent verification scripts use only the Python standard library. From the repository root, run:

```bash
python revision/checks/independent_finite_check.py
python revision/checks/verify_diagnostic.py
```

To exercise the implementation-level tests, install the repository and run:

```bash
python -m pip install -e . pytest
python -m pytest -q tests/test_branch_relative_closure.py tests/test_commutation_condition.py tests/test_brac_completeness.py
```

`independent_finite_check.py` compares exact state search with BRAC on 4,800 seeded systems and with MCAS on 4,800 seeded restricted systems; it also checks a concrete four-world informative-grant witness. `verify_diagnostic.py` checks an explicit eight-world example and five exact arithmetic values for the controlled incompatible-pair family. The independent checker does not import SAFESEP implementation modules.

## Experimental provenance

The historical three-version test workflow was successful as [run 210](https://github.com/Arithmetic-Power-Geometry/SAFESEP/actions/runs/35328293388), associated with commit [`2f63cb78ceb51f2cd801f9ef9ed055b6efd263c4`](https://github.com/Arithmetic-Power-Geometry/SAFESEP/commit/2f63cb78ceb51f2cd801f9ef9ed055b6efd263c4). A later baseline, [run 382](https://github.com/Arithmetic-Power-Geometry/SAFESEP/actions/runs/35492230097), and the [BRAC completeness workflow run 157](https://github.com/Arithmetic-Power-Geometry/SAFESEP/actions/runs/35492230090) also succeeded on commit [`a157123487f92c0657be11fd24dbe7322a04d622`](https://github.com/Arithmetic-Power-Geometry/SAFESEP/commit/a157123487f92c0657be11fd24dbe7322a04d622). These are archived GitHub Actions results, not newly executed CI runs.

The 256 four-world outcome combinations, 1,250 deterministic seeded comparisons, and 6,144 three-world model enumerations appear in the corresponding permanent tests. The 10,000-world results concern structural and analytic checks, not an exhaustive exact-search run at that size. Test identifiers numbered through 266 in the historical manuscript should not be read as the current `pytest` collected-test count. File-level source correspondence and execution boundaries are recorded under `results/`.

## Scope

The equivalence checks concern explicitly represented finite worlds, deterministic outcomes, positive authority requirements, and monotone world-independent token grants. Revocation, world-dependent effects, negative preconditions, and minimum-cost optimality are outside the Boolean closure equivalence checked here. The eight-world `bit0` example is a new fully specified illustration, not a reproduction of an earlier unnamed stronger-bit dataset.

This supplementary directory contains executable verification material and evidence provenance; the research manuscript and response to peer review are separate submission documents.
