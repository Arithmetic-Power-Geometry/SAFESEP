# Token-only transition soundness correction

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Why this correction matters
The dynamic authorization-cut search previously discarded every one-outcome probe as non-informative. That is unsound for joint information-authority state: a probe can leave the compatible-world set unchanged while granting a new authority token. Such a transition can unlock a mandatory resolver.

## Regression witness
Two worlds require incompatible decisions R and W. `credential_fetch` has one outcome in both worlds and therefore reveals no information, but legitimately grants token `alpha`. Resolver `r` requires `alpha` and then separates R/W.

Old behavior could incorrectly treat `r` as blocked forever. Correct behavior explores `(C, tokens) -> (C, tokens ∪ {alpha})`, so the cut certificate is rejected and the full joint-state planner resolves.

A second regression inserts a genuine no-op: one outcome, no world reduction, no new token. It is skipped, preventing self-loops and leaving the result unchanged.

## Correct progress condition
An executable action is explored iff it either (i) produces more than one observation branch, or (ii) changes the authority-token state on its single branch. A single-branch action that changes neither worlds nor tokens is a no-op.

## Scientific consequence
This is a soundness repair, not a novelty claim. It strengthens all later SAFESEP cut/planner comparisons because authority-only state transitions can no longer be silently omitted.

## Permanent diagnostic
The main matched-family cheapest informative unresolved experiment remains `q`, cost 1: 9,900 residual incompatible pairs at 200 worlds and 24,995,000 at 10,000 controlled worlds. This regression uses a separate minimal witness and does not redefine that diagnostic.

## Tests
- Test 85: token-only credential acquisition invalidates a false deadlock certificate and full joint-state search resolves.
- Test 86: a true one-outcome no-op neither loops nor changes resolvability/certificate semantics.
