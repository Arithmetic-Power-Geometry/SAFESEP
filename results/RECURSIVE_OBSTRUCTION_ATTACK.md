# Recursive Authorization-Obstruction Attack — Tests 147–162

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Question
Can a recursive obstruction certificate remain sound when an information-free authority transition changes which future experiments are legitimate?

## Construction
The joint state is S=(C,A), with compatible worlds C and acquired authority tokens A. A transition is progress if it either changes C through observations or changes A through authority acquisition. A one-outcome action that changes neither is a true no-op and is discarded.

The exact finite recursion is:
- terminal success when C is decision-homogeneous;
- otherwise success iff there exists a currently legitimate progress action for which every observation successor recursively succeeds;
- obstruction is the Boolean dual.

This is exact for the finite monotone belief/token model implemented here.

## Permanent cheapest-experiment diagnostic
In the dynamic OPEN/BLOCKED family the currently legitimate informative experiments are recomputed. The cheapest experiment that still leaves a decision-critical branch is q at cost 1. It leaves 9,900 incompatible pairs at 200 worlds and 24,995,000 at 10,000 controlled worlds. The information-free fetch action is not counted as an informative experiment.

## Significant result
OPEN and BLOCKED have the same q diagnostic and the same raw resolving probe k. OPEN's one-outcome fetch grants alpha and the recursion reaches k; BLOCKED's same-cost fetch is a true no-op and cannot reach k. Tests explicitly protect the token-only transition from being discarded.

## Prior-art attack
This result is NOT promoted to breakthrough novelty. Exact AND/OR recursion over belief states is standard contingent-planning/game machinery, and automated trust negotiation already supports incremental policy/credential disclosure and protected evidence. The contribution here is a sound SAFESEP regression/certificate layer that unifies information and authority progress; the generic recursion itself is not new.

## Real-data boundary
The 10,000-world rows are controlled theorem stress data. Existing public authorization benchmarks audited by SAFESEP do not provide counterfactual world-by-experiment legitimacy plus token-transition ground truth. We therefore do not fabricate empirical authority transitions. Real data remain useful for permission/policy-shape external validation, not as ground truth for this theorem.

## Decision
Do not write the paper yet. The recursion closes the soundness gap but collides with established contingent planning. The next novelty target must be a genuinely authorization-specific theorem derived from the legitimacy structure—for example a nontrivial compact obstruction/lower bound that is strictly cheaper to certify than full joint-state search for a defensible policy class, while remaining sound under token-only transitions.
