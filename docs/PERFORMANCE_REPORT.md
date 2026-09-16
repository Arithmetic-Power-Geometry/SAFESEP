# SAFESEP Performance / Correctness Report

**Date:** 16 September 2026  
**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

## Scope

This report evaluates the exact finite deterministic SAFESEP solver currently implemented in `src/safesep/solver.py`.

The present benchmark is a theorem/correctness benchmark, not a claim of production-scale throughput.

## Verified cases

| Case | Worlds | ARC-like | CARC-like one-step | SafeSep | Interpretation |
|---|---:|---:|---:|---:|---|
| `minimal_deadlock` | 2 | 1 | infinity | infinity | information exists, but no currently justified probe can obtain it |
| `adaptive_safe` | 4 | 1 | infinity | 2 | branchwise safe evidence acquisition succeeds where one-shot closure fails |
| `already_homogeneous` | 3 | 0 | 0 | 0 | exact world identification is unnecessary once all worlds require the same authorization decision |

## Correctness invariants tested

1. Decision-homogeneous classes terminate with zero additional cost.
2. An experiment is considered by SAFESEP only when it is admissible in every world remaining on the current branch.
3. Non-informative experiments that do not refine the current world set are ignored.
4. SAFESEP returns infinity when no finite safe resolving tree exists.
5. The adaptive solver can use a probe later on a branch even when that probe was not admissible at the root, provided it becomes admissible for all worlds still possible on that branch.

## Complexity note

The implementation is an exact dynamic-programming solver over reachable subsets of worlds. In the worst case, the number of belief/world subsets is exponential in `|W|`; each state may inspect all experiments and partition its worlds by outcomes. Thus the current exact solver is intended as a reference oracle for small/medium finite benchmarks and theorem validation, not yet as a large-enterprise optimizer.

## Performance claim boundary

The repository currently supports **correctness and separation claims**, not a claim that SAFESEP outperforms Microsoft PAuth, Entra, or other production authorization systems on latency or throughput. Such a claim would require a shared executable benchmark and equivalent authorization objectives.

The scientifically defensible current performance result is structural:

- an unconstrained resolver can have finite cost while SAFESEP is impossible;
- a one-step closed resolver can fail while a branchwise adaptive SAFESEP tree succeeds;
- SAFESEP can stop before world identification once authorization decisions become homogeneous.

These are capability separations, not runtime speedups.
