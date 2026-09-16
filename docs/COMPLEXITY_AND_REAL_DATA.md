# SAFESEP-EXISTS: exact algorithm, complexity boundary, and real-data plan

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Decision problem

`SAFESEP-EXISTS(P)` asks whether a finite explicit instance admits any branchwise safely admissible adaptive experiment tree whose leaves are authorization-decision homogeneous.

## Exact upper bound

For `N=|W|` explicit worlds there are at most `2^N` knowledge subsets. For each subset the exact fixed-point/AND-OR solver examines each experiment, checks universal admissibility, partitions the subset by outcomes, and requires every resulting child to be winning. Thus a direct memoized implementation gives an exponential-time upper bound in the number of explicit worlds (polynomial work per visited subset).

This is an algorithmic upper bound, not a hardness theorem. We do not infer EXPTIME-hardness, PSPACE-hardness, or NP-hardness from the exponential algorithm.

The existence question is distinct from minimum-cost SafeSep optimization. Existing adaptive-testing literature already contains NP/PSPACE hardness results for related extensional adaptive-testing variants, so any SAFESEP hardness claim requires a reduction for the exact SAFESEP model rather than inheritance by analogy.

## Prior-art comparison

When all experiments are universally admissible, the authorization-specific constraint disappears and the target reduces to decision/equivalence-class determination. Related adaptive-testing work also studies minimum strategies that decide correct-versus-incorrect without identifying the exact underlying implementation. Therefore neither decision-relative stopping nor generic adaptive-test hardness is claimed as novel.

SAFESEP's candidate contribution remains the coupling in which the still-compatible worlds determine whether the next evidence action is itself authorized.

## Real large authorization data

A focused search identified public empirical/real-world authorization resources, but they do not directly contain SAFESEP latent-world counterfactuals (`O_e(w)` and `Adm(e,w)` for every possible world). Examples include:

- the Amazon employee access challenge used in published access-control research: 32,769 authorization records, 9,560 users, 7,517 resources in a recent published characterization;
- AuthBench, which supplies agent tasks with gold read/write/execute permission annotations and replay under policy constraints;
- recent real-world serverless studies that analyze IAM policies from hundreds of AWS Lambda applications.

These are valuable external-validity sources, but converting an ordinary allow/deny row into a SAFESEP possible-world experiment system without a declared mapping would fabricate missing counterfactual semantics. The repository therefore keeps two layers separate:

1. **controlled SAFESEP theorem benchmarks**, where latent worlds and probe admissibility are fully known; and
2. **empirical authorization datasets**, used only for quantities actually present in the source (decisions, permissions, actions, policy structure) until a defensible SAFESEP adapter is specified.

This boundary is intentional research hygiene, not a limitation to hide.

## Current result

The exact existence solver is now independently tested against the minimum-cost solver on the core examples and on the parameterized matched family. It verifies that the finite/infinite distinction is a property of existence itself, not an artifact of cost arithmetic.
