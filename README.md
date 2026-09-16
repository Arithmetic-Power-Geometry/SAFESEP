# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions that are themselves justified by the information currently available.

> Know enough to grant — but never grant to know.

## Core question

Given a current set of possible worlds `C`, a required authorization decision `D(w)` in each world, experiments `e` with outcomes `O_e(w)`, costs `c(e)`, and world-dependent admissibility `Adm(e,w)`, does there exist a finite adaptive experiment tree such that:

1. every experiment is admissible in every world still possible on its branch; and
2. every leaf contains worlds requiring the same authorization decision?

If yes, `SafeSep(C) < infinity`. If no, `SafeSep(C) = infinity`.

## Main research objects

- decision-critical equivalence classes
- Authority Resolution Cost (ARC)
- Closed Authority Resolution Cost (CARC)
- Authority-Resolution Deadlock (ARD)
- branchwise authorization closure
- SafeSep: minimum-cost safely admissible decision-resolving experiment tree
- Safe-Separability solvability criterion

## What SAFESEP is not

SAFESEP does **not** claim novelty for least privilege, JIT authorization, task-scoped permissions, dynamic capability scoping, missing-attribute retrieval, generic active sensing, POMDP information gathering, value of information, or trust negotiation. These are treated as prior art / baselines.

## Reproducible software

The package contains:

- exact finite-world solver for SafeSep
- ordinary unconstrained decision-resolution solver (ARC-like baseline)
- one-step closed resolver (CARC-like baseline)
- constructive counterexamples
- benchmark generators
- unit tests for theorem conditions and separation cases
- scripts that emit machine-readable benchmark results

## Quick start

```bash
python -m pip install -e .
python -m pytest -q
python scripts/run_benchmarks.py
```

## License

Apache License 2.0. See `LICENSE`.
