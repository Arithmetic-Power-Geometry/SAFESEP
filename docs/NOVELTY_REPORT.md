# SAFESEP Novelty and Prior-Art Report

**Date:** 16 September 2026  
**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

## Executive finding

SAFESEP should **not** claim novelty for least privilege, JIT authorization, task-scoped authorization, dynamic capability scoping, generic active sensing, optimal diagnostic testing, contingent planning, epistemic planning, safe exploration, value of information, or generic authorization deadlocks.

The current novelty candidate that survives this comparison is narrower:

> **Safe authorization resolution under world-dependent probe admissibility:** an adaptive experiment tree whose probes are admissible in every world still possible on the current branch, terminating when all remaining worlds require the same authorization decision.

The associated decision criterion is `SafeSep(C) < infinity`.

## Comparison table

| Area / system | Established contribution | Collision with SAFESEP | Residual distinction |
|---|---|---|---|
| Microsoft least-privilege guidance (2026) | task-scoped RBAC, tool allowlists, JIT elevation, downstream authorization checks | rules out novelty claims about dynamic least privilege itself | does not formulate a decision-homogenizing experiment tree under world-dependent probe admissibility |
| Microsoft PAuth (2026) | precise task-scoped implicit authorization, symbolic NL slices, provenance envelopes | rules out broad claims about precise task-derived permissions | SAFESEP asks whether evidence needed to determine the authorization can itself be safely acquired under unresolved worlds |
| IETF agent authorization drafts (2026) | intent-driven JIT authorization, fine-grained operation authorization, agent authorization envelopes | rules out broad protocol-level novelty | SAFESEP is a finite-world solvability / experiment-selection problem rather than a token or delegation protocol |
| Dynamic capability scoping (Noyan, 2026) | role ceilings + task classifier + policy constraints; minimum permission labels | rules out dynamic capability scoping as novelty | SAFESEP does not assume the minimum permission label is already identifiable |
| Active diagnosis / optimal testing | adaptive test trees; minimize expected/worst-case test cost; diagnosis leaves | strong mathematical ancestor for the experiment-tree optimization | SAFESEP's probe availability is constrained by authorization across every still-compatible world, and leaves need only be authorization-decision homogeneous rather than world-identifying |
| Contingent / epistemic planning | action trees branch on sensing results; action preconditions and belief updates | strong structural ancestor | SAFESEP couples the legality of information acquisition to the authorization decision being inferred |
| Safe exploration in MDPs | restrict exploration to guaranteed-safe actions / states | strong safety ancestor | SAFESEP safety is an authorization-legitimacy predicate across an unresolved possible-world class, not only a physical reward/safety constraint |
| Obstruction-free authorization enforcement | authorization constraints can obstruct workflow progress; obstruction/deadlock analysis | rules out generic 'authorization deadlock' novelty | SAFESEP's obstruction occurs at the epistemic layer: the resolving probe itself is not jointly admissible across worlds whose required authorization decisions disagree |

## Constructive separations implemented in the repository

### Separation A: ordinary information sufficiency does not imply safe resolution

`minimal_deadlock_problem()` has two possible worlds requiring different authorization decisions. A probe perfectly distinguishes them and costs 1, but that probe is unauthorized in one of the worlds.

Expected result:

```text
ARC-like = 1
SafeSep  = infinity
```

This establishes that unconstrained decision distinguishability does not imply safely authorized distinguishability.

### Separation B: one-step closed probing does not imply adaptive safe separability

`adaptive_safe_problem()` uses four worlds. No globally admissible **single** probe immediately makes all branches decision-homogeneous, so the one-step closed baseline is infinite. A globally safe first probe removes one world; on the remaining branch, a second probe becomes admissible and completes authorization resolution.

Expected result:

```text
CARC-like one-step = infinity
SafeSep            = 2
```

This establishes that branchwise adaptive authorization closure is strictly more expressive than one-shot closed resolution.

## Current strongest theorem candidate

For a finite problem with deterministic experiments and finite experiment costs:

> A decision-critical world set `C` admits safe autonomous authorization resolution iff there exists a finite adaptive experiment tree in which every probe is admissible in every world remaining on its branch and every leaf is homogeneous in the required authorization decision.

The current implementation provides an exact dynamic-programming solver for this finite deterministic case and returns `infinity` when no such tree exists.

## Novelty status

**Status: strong novelty candidate, not yet a worldwide novelty claim.**

The most important surviving distinction is the combination of:

1. decision-relative stopping (same authorization decision, not exact world identification),
2. world-dependent admissibility of evidence-gathering actions,
3. branchwise recomputation of admissible probes after observations, and
4. minimum-cost adaptive resolution under those constraints.

A patent search and deeper formal comparison with contingent planning / conformant planning / active diagnosis are still required before describing the result as a confirmed breakthrough.
