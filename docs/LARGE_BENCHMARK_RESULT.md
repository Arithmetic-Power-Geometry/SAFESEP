# Large-scale matched-family benchmark result

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Purpose

Stress-test the structural SAFESEP separation at substantially larger explicit world counts while avoiding the exponential exact dynamic-programming solver where the analytic construction already supplies a proof witness.

## Dataset

`data/large_authorization_benchmark.csv` records matched A/B systems at 200, 500, 1,000, 2,000, 5,000 and 10,000 worlds.

For each size the two systems match worlds, decisions, experiment costs, complete outcome maps, admissibility cardinalities, ARC-like cost, one-step closed cost, cheapest safe informative root probe, root probe cost, and worst incompatible-pair count.

At 10,000 worlds the cheapest root probe still costs 1 and leaves 24,995,000 mutually decision-incompatible pairs on its worst residual branch in both A and B.

## Structural result

For every benchmark size, A has a constructive branchwise-safe tree `e1 -> e2` of worst-case cost 2. B has the same root observation structure, but the residual READ world `r1` blocks `e2`; no alternative probe exists. Therefore the construction predicts `SafeSep(A)=2` and `SafeSep(B)=infinity` while all recorded coarse quantities remain matched.

## Validation method

`tests/test_large_authorization_benchmark.py` validates the construction directly at up to 10,000 explicit worlds. This is deliberately separate from exact minimax dynamic programming: it checks the theorem's structural proof obligations without presenting a large synthetic run as evidence that an exponential solver scales to 10,000 worlds.

## Scientific significance

The scale test does not create a new theorem beyond the parameterized family; its significance is robustness. It rules out the possibility that the observed separation was an artifact of the original four-world example or tiny finite test sizes.

## Data caveat

This is a large controlled synthetic authorization dataset, not production authorization telemetry. It is suitable for theorem validation because the latent possible-world and admissibility semantics are exactly known. Real policy data can be added later as an application benchmark, but should not be used to fabricate latent-world ground truth that the source does not contain.
