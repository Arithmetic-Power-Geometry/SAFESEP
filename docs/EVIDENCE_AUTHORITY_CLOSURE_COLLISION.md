# Evidence-Authority Closure: fixed-point attack

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Candidate tested
Evidence needed to authorize a resolving experiment may itself have to be acquired by authorized experiments. Define the executable/evidence set as the **least fixed point from exogenous evidence seeds**. Cycles with no grounded seed do not bootstrap authority.

## Matched construction
Both systems have the same probe names and costs. `q` costs 1 and is independently executable; it is the cheapest informative experiment that leaves mutually decision-incompatible worlds. Resolver `r` costs 2 and requires evidence token `alpha`. Probe `s` requires `beta`; `r` yields `beta`; `s` yields `alpha`.

System A: `q` additionally yields `alpha`, grounding the chain and making `r` executable.

System B: `q` yields no `alpha`. The remaining `r <-> s` support is circular and unseeded, so the least closure contains neither `r` nor `s`.

Thus the cheapest unresolved probe is identical (`q`, cost 1), but the resolver belongs to the grounded least closure only in A.

## Prior-art attack and collision
This is **not yet a foundational novelty**. Trust-management and authorization systems already use logical closure/fixed-point semantics, recursive predicates, proof search, credential dependency graphs, and mechanisms for cycles. KeyNote formalizes policy/credential compliance; trust-management literature explicitly discusses Datalog/recursive authorization and cyclic dependencies; SecPAL supports recursive predicates with terminating tabled evaluation; SAFE assembles linked credential proof contexts on demand. Therefore "authorization as least fixed point" and "unseeded cycles do not justify access" cannot be claimed as new.

## What survives
The remaining candidate is narrower: optimize adaptive evidence acquisition when the same actions simultaneously (i) change the decision-relevant information state and (ii) change the least authorization closure that determines which future evidence actions are legitimate. The novelty, if any, must be a theorem about this **joint information-authority closure optimization**, not fixed points or recursive authorization separately.

## Empirical boundary
The 10,000-world case is a controlled theorem stress test. Real authorization benchmarks do not natively provide counterfactual evidence-yield and recursive authority-dependency ground truth, so no such labels are fabricated.
