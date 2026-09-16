# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions that are themselves justified by the information currently available.

> **Know enough to grant — but never grant to know.**

## Motivation

Autonomous agents increasingly need to decide whether to read, write, send, delete, execute, disclose, or escalate. Under uncertainty, the agent may face several possible worlds compatible with everything it currently knows. Some worlds require different authorization decisions. The evidence needed to distinguish them can itself require authority. SAFESEP studies this coupled epistemic-control problem.

The central distinction is between **information that exists** and **information that can be obtained safely under currently justified authority**.

## Formal model

A finite SAFESEP instance contains:

- possible worlds `W`;
- current compatible set `C ⊆ W`;
- required authorization decision `D(w)` for every world;
- experiments `e ∈ E`;
- outcome map `O_e(w)`;
- experiment cost `c(e)`; and
- world-dependent admissibility `Adm(e,w)`.

A set `C` is **decision-critical** when it contains worlds requiring different authorization decisions:

`|{D(w): w ∈ C}| > 1`.

An experiment is branchwise safely admissible at `C` only when it is admissible in every world still compatible with that branch.

After observing outcome `o`, knowledge contracts to

`C_(e,o) = {w ∈ C : O_e(w)=o}`.

The exact world need not be identified. Resolution is achieved when every remaining world requires the same decision.

## SafeSep

A valid adaptive experiment tree satisfies:

1. every experiment is admissible in every world remaining on its branch; and
2. every terminal leaf is decision-homogeneous.

`SafeSep(C)` is the minimum worst-case accumulated experiment cost among all valid trees. If no valid finite tree exists, `SafeSep(C)=∞`.

This gives the candidate safe-separability criterion:

**Autonomous safe authorization resolution exists exactly when every reachable decision-critical class admits a finite branchwise safely admissible decision-resolving tree.**

This repository treats that statement as a research theorem candidate to be formally stress-tested, not as a claim of established worldwide novelty.

## Related quantities

**ARC-like baseline.** Minimum decision-resolution cost when experiment admissibility is ignored.

**CARC-like one-step baseline.** Cheapest currently admissible single probe that immediately makes every outcome branch decision-homogeneous.

**Authority-Resolution Deadlock (ARD).** A decision-critical state for which required distinguishing information may exist but no permitted safe strategy can acquire enough information to resolve the authorization decision.

A key separation already reproduced by the software is that finite unconstrained information cost does not imply finite SafeSep.

## Cheapest-experiment diagnostic

The repository also tests the diagnostic question:

> **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?**

This is intentionally **not** the SafeSep objective. It is useful because it detects cheap probes that appear informative but are insufficient for authorization resolution.

`cheapest_experiment_leaving_incompatibility(...)` returns the cheapest such probe and records its cost, current admissibility, number of incompatible branches, and worst remaining incompatible-pair count.

`cheapest_one_step_resolver(...)` separately finds the cheapest single probe that completely resolves the authorization decision, optionally requiring current admissibility.

## Current reproducible benchmark results

| Case | ARC-like | CARC-like one-step | SafeSep | Meaning |
|---|---:|---:|---:|---|
| minimal deadlock | 1 | ∞ | ∞ | information exists, but no safe autonomous resolution |
| adaptive safe | 1 | ∞ | 2 | one-step closed resolution fails, but adaptive branchwise resolution succeeds |
| already homogeneous | 0 | 0 | 0 | no experiment is required |

The `adaptive_safe` case is particularly important: `safe_metadata_probe` costs 1 and is globally admissible, yet leaves a decision-incompatible branch. On that reduced branch, `branch_probe` becomes admissible and completes resolution. Thus a one-step criterion can report failure while SafeSep remains finite.

## Dataset

`data/cheapest_experiment_cases.csv` records the current diagnostic cases and experiment roles. Future benchmark families should retain machine-readable world/decision/outcome/admissibility/cost data so results can be regenerated rather than manually asserted.

## Test registry

Significant tests are preserved in GitHub rather than treated as disposable checks. Append new scientifically meaningful tests to this registry.

1. **Minimal authorization deadlock** — verifies finite unconstrained distinguishability can coexist with `SafeSep=∞`.
2. **Adaptive safe resolution** — verifies branchwise admissibility can make `SafeSep` finite even when no globally admissible one-step resolver exists.
3. **Already decision-homogeneous state** — verifies zero resolution cost when all compatible worlds require the same decision.
4. **Irreducibility / matched-summary separation** — tests systems with matching simpler authorization summaries but different SafeSep behavior.
5. **Cheapest admissible experiment leaves incompatibility** — verifies the cheapest currently safe informative probe can leave a mutually decision-incompatible branch.
6. **No admissible one-step resolver in adaptive-safe case** — verifies failure of the one-step baseline does not imply SafeSep impossibility.
7. **Deadlock has no admissible one-step resolver** — verifies the protected distinguishing probe cannot be treated as a legitimate current action.

Current test files:

- `tests/test_safesep.py`
- `tests/test_irreducibility.py`
- `tests/test_cheapest_experiment.py`

## Reproducible software

The package contains an exact finite-world SafeSep solver, unconstrained ARC-like baseline, one-step CARC-like baseline, constructive counterexamples, irreducibility experiments, cheapest-experiment diagnostics, benchmark datasets, unit tests, and scripts emitting machine-readable results.

## Quick start

```bash
python -m pip install -e .
python -m pytest -q
python scripts/run_benchmarks.py
```

## Research protocol

For each new result:

1. state the mathematical claim precisely;
2. construct the smallest counterexample or witness;
3. encode it as machine-readable data when useful;
4. implement the corresponding solver/diagnostic;
5. add a permanent regression test when the result is scientifically significant;
6. compare against ARC/CARC and other relevant baselines;
7. run CI across supported Python versions;
8. preserve reproducible outputs and append the test to this README registry;
9. distinguish established prior art from SAFESEP novelty candidates.

## Prior-art boundary

SAFESEP does **not** claim novelty for least privilege, JIT authorization, task-scoped permissions, dynamic capability scoping, missing-attribute retrieval, generic active sensing, POMDP information gathering, value of information, trust negotiation, or ordinary decision-tree optimization. These are prior art / baselines.

The current novelty candidates concern decision-relative safe separability: authorization decisions must be resolved through an adaptive evidence strategy whose probes are themselves justified on every world remaining on the branch.

## Next research targets

The immediate targets are parameterized irreducibility families, large generated authorization datasets, comparisons with information-gain/risk/permission-count summaries, complexity of the SAFESEP decision problem, and Microsoft-style agent authorization benchmarks involving read/write/send/delete/escalate operations.

## License

Apache License 2.0. See `LICENSE`.
