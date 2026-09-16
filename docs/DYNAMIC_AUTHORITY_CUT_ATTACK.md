# Dynamic Branch-Relative Authorization Cut — theorem candidate and attack

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

## Certificate
Let a joint state be S=(C,A), compatible worlds plus currently held authority facts. Let K be a set of probes. If (i) every decision-incompatible pair at the root can be separated only by a probe in K, and (ii) in every decision-critical joint state reachable without using K, every probe in K is unauthorized, then no legitimate autonomous resolution policy exists.

Proof: any resolving policy must have a first use of K by (i). Its predecessor state is reachable without K and remains decision-critical. By (ii), no K probe is executable there, contradiction.

This is a sufficient impossibility certificate, not a new planning formalism.

## Cheapest unresolved experiment
In the witness, q has cost 1 and is the cheapest executable informative experiment that leaves mutually incompatible worlds. At 200 worlds its residual branch has 9,900 incompatible R/W pairs; at 10,000 worlds the structural count is 24,995,000.

## Matched open/blocked witness
Both systems use the same worlds, decisions, q and resolver r. q isolates r0 and leaves the residual branch decision-critical. r is the only R/W separator and requires token alpha. In OPEN, q/rest grants alpha. In BLOCKED, q/rest grants nothing. Thus K={r} fails condition (ii) in OPEN but satisfies both certificate conditions in BLOCKED.

## Prior-art attack
Decision Region Determination already chooses adaptive tests until remaining hypotheses fit a decision region, and edge/hyperedge-cutting formulations explicitly cut relationships between hypotheses belonging to different decision regions. Therefore pair cutting and decision-directed information acquisition are not novel.

Full-state contingent planning can also encode the state (C,A), token effects, and r's precondition. Therefore the certificate does not establish a new representational primitive or greater expressivity.

The retained contribution is narrower: a compact authorization-specific *sufficient deadlock certificate* phrased as a mandatory decision-separating cut whose members cannot become executable before the first cut action. This may be useful for explanation/pruning, but novelty is not yet established because it resembles dead-end/cut certificates in planning and mandatory-action cuts.

## Verdict
KEEP as a significant theorem candidate and regression test; DO NOT yet call it breakthrough. Next attack: determine whether this certificate is merely a planning dead-end landmark/cut in disguise. If so, seek an authorization-specific quantitative invariant or complexity separation. If not, prove a nontrivial certificate/algorithmic advantage over full joint-state search.
