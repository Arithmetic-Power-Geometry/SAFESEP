# Dynamic Legitimate-Pair-Flow Attack — Tests 107–122

## Permanent diagnostic
The cheapest informative experiment that still leaves mutually decision-incompatible possible worlds remains `q`, cost 1. At 200 worlds it leaves 9,900 incompatible pairs; at 10,000 controlled worlds the analytic count is 24,995,000.

## Construction
Joint state is `(C,A)` where `C` is the compatible-world branch and `A` the acquired authority-token set. Probe `k` perfectly separates R/W but requires token `alpha`. Both OPEN and BLOCKED have the same worlds, decisions, raw outcome maps, probe names, probe costs, and initial illegitimacy of `k`. A one-outcome `fetch` action is also information-identical in the two cases. OPEN's fetch grants `alpha`; BLOCKED's fetch is a true no-op.

## Dynamic cut certificate
For a candidate mandatory probe set K, enumerate joint states reachable without K. If every reachable decision-critical state keeps every K probe illegitimate, then K is dynamically blocked. In this family K={k}. BLOCKED satisfies the certificate; OPEN does not because a token-only transition reaches `(C,{alpha})` without changing C.

This is a useful representation-independent *semantic certificate* in the sense that it is stated on reachable authorization states, not a particular planner encoding. It also directly regression-tests the token-only transition bug fixed in Tests 85–86.

## Prior-art attack
Do **not** call the general mechanism a breakthrough yet. Automated trust negotiation already models incremental protected credential/policy disclosure, cyclic dependencies, and minimum-cost disclosure sequences. Conformant/contingent planning can represent joint belief/authority state transitions. Static pair-cover/set-cover and planning cut/dead-end reasoning are also established neighboring ideas. Therefore the current contribution is best treated as a SAFESEP-specific certificate and implementation invariant, not a new general planning principle.

## What survived
The most promising remaining theorem target is not merely existence of a dynamic cut. It is a quantitative **authorization pair-flow lower bound** that relates the amount of decision-incompatibility eliminated to authority that must be legitimately acquired along every branch, ideally under a restricted authorization language and with a bound not reducible to ordinary disclosure cost or generic planning depth.

## Empirical boundary
`data/dynamic_pair_flow.csv` scales the controlled theorem family from 200 to 10,000 worlds. These are synthetic structural stress tests. Public authorization datasets do not provide the counterfactual world×probe legitimacy and token-yield labels needed to assert this dynamic certificate empirically; no such labels are fabricated.
