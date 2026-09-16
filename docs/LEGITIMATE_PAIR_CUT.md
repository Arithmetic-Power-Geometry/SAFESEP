# Legitimate Incompatible-Pair Cut

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Result
Let I(C) be the set of pairs of compatible worlds requiring different authorization decisions. An experiment separates pair {u,v} when its outcomes differ on u and v. Let L(C) be the union of pairs separated by experiments that are legitimately executable under the modeled authorization constraint.

In the static-legitimacy restriction implemented here, if I(C)\\L(C) is nonempty, at least one decision-incompatible pair cannot be distinguished by any legitimate experiment. Therefore no legitimate experiment family can make every remaining branch decision-homogeneous. This gives a simple sufficient impossibility certificate.

## Cheapest-experiment invariant
In the obstructed matched family, q remains the cheapest legitimate informative experiment that leaves incompatible worlds, at cost 1. With 2n worlds, q leaves one residual branch containing n(n-1) incompatible pairs: 9,900 at 200 worlds and 24,995,000 at 10,000 worlds.

## Matched information / different usable cover
A_n and B_n have the same worlds, decisions, experiment names, costs and outcome maps. Thus every experiment separates exactly the same incompatible pairs informationally. The resolver is legitimate in A_n and blocked in B_n. Hence authorization changes the *usable* pair cover without changing the raw information system.

## Prior-art attack
This is NOT yet a breakthrough novelty claim. Pair separation and minimum test cover are established: classical test-cover formulations seek tests that distinguish pairs/entities, and Decision Region Determination/Equivalence Class Determination use edges or regions so information gathering stops once the decision is determined. The new code is therefore an authorization-filtered certificate built on established pair-cover structure, not a claim that pair covering is new.

The remaining research question is whether a dynamic, branch-relative authorization cut admits a nontrivial theorem or lower bound that is not merely ordinary test cover after deleting unavailable tests, and not merely full-state contingent planning. A credible next result must use authorization evolution itself, not a static legitimate flag.

## Empirical boundary
The 10,000-world benchmark is controlled synthetic theorem stress, not production IAM telemetry. Public authorization datasets generally do not provide counterfactual world-by-experiment outcome maps plus legitimate-executability labels. We will not manufacture those labels and call them real.
