# SAFESEP — Safe Separability for Autonomous Authorization

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

SAFESEP is a formal and reproducible research framework for deciding whether an autonomous AI agent can resolve an authorization decision using only evidence-gathering actions that are themselves justified by the information currently available.

> **Know enough to grant — but never grant to know.**

## Motivation

Autonomous agents increasingly need to decide whether to read, write, send, delete, execute, disclose, or escalate. Under uncertainty, several possible worlds may remain compatible with current knowledge, while requiring different authorization decisions. The evidence needed to distinguish those worlds can itself require authority. SAFESEP studies this coupled epistemic-control problem.

The central distinction is between **information that exists** and **information that can be obtained safely under currently justified authority**.

## Formal model

A finite SAFESEP instance contains possible worlds `W`, current compatible set `C ⊆ W`, required decision `D(w)`, experiments `e`, outcome maps `O_e(w)`, costs `c(e)`, and world-dependent admissibility `Adm(e,w)`.

`C` is **decision-critical** when `|{D(w): w ∈ C}| > 1`. An experiment is branchwise safely admissible at `C` only when it is admissible in every world still compatible with that branch. After outcome `o`, knowledge contracts to `C_(e,o)={w∈C:O_e(w)=o}`.

The exact world need not be identified. Resolution is achieved when every remaining world requires the same authorization decision.

## SafeSep

A valid adaptive experiment tree satisfies: (1) every probe is admissible in every world remaining on its branch; and (2) every terminal leaf is decision-homogeneous.

`SafeSep(C)` is the minimum worst-case accumulated experiment cost among all valid trees. If no valid finite tree exists, `SafeSep(C)=∞`.

Candidate criterion:

**Autonomous safe authorization resolution exists exactly when every reachable decision-critical class admits a finite branchwise safely admissible decision-resolving tree.**

This is a research theorem candidate under continuing prior-art and mathematical stress testing, not a claim of established worldwide novelty.

## Related quantities

**ARC-like baseline:** minimum decision-resolution cost when experiment admissibility is ignored.

**CARC-like one-step baseline:** cheapest currently admissible single probe that immediately makes every outcome branch decision-homogeneous.

**Authority-Resolution Deadlock (ARD):** a decision-critical state in which distinguishing information may exist but no permitted safe strategy can acquire enough information to resolve the authorization decision.

## Cheapest-experiment diagnostic

The repository tests:

> **What is the cheapest informative experiment, given current knowledge, that still leaves at least one branch containing mutually authorization-incompatible possible worlds?**

This is not the SafeSep objective. It detects cheap probes that appear informative but remain insufficient for authorization resolution. `cheapest_experiment_leaving_incompatibility(...)` records cost, current admissibility, incompatible branches, and worst remaining incompatible-pair count. `cheapest_one_step_resolver(...)` finds a cheapest single complete resolver.

## Current reproducible results

| Case | ARC-like | CARC-like one-step | SafeSep | Meaning |
|---|---:|---:|---:|---|
| minimal deadlock | 1 | ∞ | ∞ | information exists, but no safe autonomous resolution |
| adaptive safe | 1 | ∞ | 2 | one-step resolution fails, adaptive branchwise resolution succeeds |
| already homogeneous | 0 | 0 | 0 | no experiment required |
| matched family A_n | 1 | ∞ | 2 | safely resolvable for every tested n |
| matched family B_n | 1 | ∞ | ∞ | same coarse summaries, but safely unresolvable |

### Parameterized matched-summary separation

For every constructed `n >= 2`, systems `A_n` and `B_n` contain `2n` worlds and have identical decisions, experiment costs, experiment outcome maps, per-experiment admissibility counts, ARC-like cost, and CARC-like one-step cost. They differ only in **which worlds** admit the second experiment.

The construction yields

`ARC(A_n)=ARC(B_n)=1`,

`CARC(A_n)=CARC(B_n)=∞`,

but

`SafeSep(A_n)=2` and `SafeSep(B_n)=∞`.

Thus the tested coarse scalar summaries do not determine safe authorization resolvability. The world-by-experiment admissibility incidence structure matters. This is a stronger structural result than a single four-world counterexample, but it must still be compared carefully with active diagnosis, constrained epistemic planning, safe sensing, and related conditional-planning literature before making a worldwide novelty claim.

## Datasets

- `data/cheapest_experiment_cases.csv` — cheapest-probe diagnostic cases.
- `data/parameterized_irreducibility.csv` — matched-summary family benchmark points from 4 to 100 worlds.

Future benchmark families should retain machine-readable world/decision/outcome/admissibility/cost data so results can be regenerated rather than manually asserted.

## Test registry

Significant tests are preserved in GitHub rather than treated as disposable checks. Append every scientifically meaningful test here.

1. **Minimal authorization deadlock** — finite unconstrained distinguishability can coexist with `SafeSep=∞`.
2. **Adaptive safe resolution** — branchwise admissibility can make SafeSep finite even when no globally admissible one-step resolver exists.
3. **Already decision-homogeneous state** — zero resolution cost when all compatible worlds require the same decision.
4. **Irreducibility / matched-summary separation** — matching simpler authorization summaries can coexist with different SafeSep behavior.
5. **Cheapest admissible experiment leaves incompatibility** — the cheapest currently safe informative probe can leave a mutually decision-incompatible branch.
6. **No admissible one-step resolver in adaptive-safe case** — one-step failure does not imply SafeSep impossibility.
7. **Deadlock has no admissible one-step resolver** — a protected distinguishing probe cannot be treated as a legitimate current action.
8. **Parameterized SafeSep irreducibility family** — for `n=2..20`, verifies matched coarse signatures and identical ARC/CARC values while `SafeSep(A_n)=2` and `SafeSep(B_n)=∞`.
9. **Scale invariance of the separation** — verifies the same finite/infinite SafeSep separation at 4, 6, 10, 20, 40, and 100 worlds.

Current test files:

- `tests/test_safesep.py`
- `tests/test_irreducibility.py`
- `tests/test_cheapest_experiment.py`
- `tests/test_parameterized_irreducibility.py`

## Reproducible software

The package contains an exact finite-world SafeSep solver, unconstrained ARC-like baseline, one-step CARC-like baseline, constructive counterexamples, parameterized irreducibility families, cheapest-experiment diagnostics, benchmark datasets, unit tests, and CI.

## Quick start

```bash
python -m pip install -e .
python -m pytest -q
python scripts/run_benchmarks.py
```

## Research protocol

For each new result: state the mathematical claim precisely; construct the smallest counterexample or witness; encode it as machine-readable data when useful; implement the solver/diagnostic; add a permanent regression test when scientifically significant; compare against relevant baselines; run CI; preserve reproducible outputs; append the test to this README; and distinguish established prior art from SAFESEP novelty candidates.

## Prior-art boundary

SAFESEP does **not** claim novelty for least privilege, JIT authorization, task-scoped permissions, dynamic capability scoping, missing-attribute retrieval, generic active sensing, POMDP information gathering, value of information, trust negotiation, ordinary decision-tree optimization, active diagnosis, or conditional epistemic planning.

The current novelty candidate is narrower: **decision-relative safe separability for authorization**, where an adaptive evidence strategy must reach a decision-homogeneous knowledge state while every probe is itself justified on every world remaining on its branch.

## Next research targets

Immediate targets are: formal proof of the parameterized separation for all `n>=2`; comparison against active-diagnosis/epistemic-planning formalisms; complexity of the SAFESEP decision problem; randomized/generated authorization datasets; information-gain and risk baselines; and Microsoft-style read/write/send/delete/escalate authorization benchmarks.

## License

Apache License 2.0. See `LICENSE`.
