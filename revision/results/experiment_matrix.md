# Computational experiments and source correspondence

| Evaluation | Exact definition | Public source | Evidence |
|---|---|---|---|
| Four-world observation-pattern enumeration | 16 binary outcome patterns for one grant-capable probe multiplied by 16 patterns for one pure sensor, yielding 256 model configurations | `tests/test_branch_relative_closure.py`, `test_260_exhaustive_small_outcome_patterns_against_exact` | Successful `pytest` job in CI run 382; comparison uses `brac_resolves` and `exact_resolves` |
| Certified randomized comparisons | 250 seeded instances plus 1,000 seeded instances; fixed seeds `227241` and `227242` | `tests/test_commutation_condition.py`, `test_241_random_certified_250`, `test_242_random_certified_1000` | Successful `pytest` job in CI run 382 |
| Three-world exhaustive authority-model enumeration | 32 probe types for each of two probes and six nonconstant binary decision patterns: 32 × 32 × 6 = 6,144 model configurations | `tests/test_brac_completeness.py`, `test_exhaustive_three_world_two_probe_semantics` | Successful BRAC completeness workflow run 157 |
| Controlled incompatible-pair scaling | For 2n worlds equally divided between two decisions, the probe `q` isolates one world, leaving n(n−1) incompatible pairs | `src/safesep/dynamic_pair_flow.py` and `tests/test_dynamic_pair_flow.py`; independent arithmetic in `checks/verify_diagnostic.py` | Five values checked independently; up to 10,000 worlds |
| Large-world structural checks | Explicit-world structural invariants, not exponential exact search | `tests/test_large_authorization_benchmark.py` | Successful `pytest` job in CI run 382 |
| Independent finite-model falsification | 4,800 seeded BRAC comparisons; 4,800 seeded MCAS comparisons | `revision/checks/independent_finite_check.py` | Executed independently using Python 3.13.5 on 12 November 2026 |
| Equal-cost diagnostic comparison | Eight worlds, parity decisions; `q` isolates world 0; `bit0` divides into two four-world halves | `revision/checks/verify_diagnostic.py` and `revision/checks/stronger_bit_example.json` | Worst residual incompatible pairs: q = 12, bit0 = 4 |

A model configuration inside a test loop is not a separate `pytest` test function. The present source includes a further 6,144-configuration exhaustive routine beyond the historical 256-configuration BRAC battery. GitHub Actions success establishes the outcome of the checked-in tests at the corresponding commit; it is not a formal proof of the general theorem.

