# Dynamic Branch-Relative Authorization Cut — corrected theorem and attack

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Corrected certificate
Let a joint state be S=(C,A), compatible worlds plus currently held authority facts, and let K be a candidate mandatory probe set. A sufficient obstruction certificate is:

1. after removing K, **no complete resolving policy exists** under the restricted AND/OR semantics; and
2. in every decision-critical joint state reachable without using K, every probe in K is unauthorized.

Then no legitimate autonomous resolution policy exists.

### Proof
Assume a successful legitimate policy exists. Condition 1 implies that it must use some member of K. Consider its first use of K. The predecessor joint state is reachable without K and is decision-critical; otherwise the policy could already stop. By Condition 2 every member of K is unauthorized there, contradicting legitimacy. Therefore no successful legitimate policy exists.

## Why the earlier pairwise condition was wrong
The original draft required every incompatible root pair to be separable only by K. CI exposed this as unnecessarily strong: a non-K probe such as q may separate some incompatible root pairs while every *complete* resolving policy still requires a K probe on a residual branch. The implementation and permanent regression tests therefore use the corrected complete-policy condition above. The failed formulation is preserved in `results/CERTIFICATE_VS_PLANNER.md` as a scientific correction.

## Cheapest unresolved experiment
In the witness, q has cost 1 and is the cheapest executable informative experiment that leaves mutually incompatible worlds. At 200 worlds its residual branch has 9,900 incompatible R/W pairs; at 10,000 worlds the structural count is 24,995,000.

## Matched OPEN/BLOCKED witness
Both systems use the same worlds, decisions, q and resolver r. q isolates r0 and leaves the residual branch decision-critical. r requires token alpha. In OPEN, q/rest grants alpha; in BLOCKED it grants nothing. The corrected certificate rejects OPEN and certifies BLOCKED.

## Prior-art/full-planner attack
Decision Region Determination already studies adaptive tests until a decision region is determined, and contingent planning represents branch-dependent state and action applicability. The corrected mandatory-cut check itself performs restricted AND/OR reasoning, so no asymptotic advantage over full planning search is claimed. The result is retained as an authorization-specific explanation/pruning certificate, not as a new planning formalism.

## Verdict
KEEP the corrected theorem and Tests 49–56. DO NOT call it breakthrough. Any stronger claim must either obtain a genuinely cheaper certificate for a nontrivial class or establish an authorization-specific invariant/lower bound that survives full joint-state compilation.
