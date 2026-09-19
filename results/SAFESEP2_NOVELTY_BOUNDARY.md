# SAFESEP-II novelty boundary — pre-manuscript freeze

## Established neighboring ideas that must NOT be claimed as inventions

1. Belief states as sufficient statistics for histories in partially observable decision making are classical.
2. Information-gathering / active-sensing planning over belief states is established.
3. Action equivalence, representative actions, symmetry/redundancy pruning are established planning techniques.
4. Parameterized complexity and kernelization for planning are established research areas.
5. Permission/authorization revocation is established in access-control systems.

## SAFESEP-II claim boundary

The paper should claim only results proved for its explicit restricted semantics:

- evidence probes are deterministic and one-shot;
- requirements, grants, and revocations are world-independent;
- authority is set-valued with update (A union G) minus R;
- the objective is decision sufficiency, not exact world identification;
- probe execution may destroy authority required by later evidence.

Within this model the paper contributes the following package:

1. Pairwise-global failure: every decision-incompatible pair can initially possess a legitimate separator while no globally safe adaptive resolving policy exists.
2. Static noninterference and evidence-precedence sufficient certificates.
3. Acyclic global precedence is not necessary: branch-conditioned adaptivity can resolve instances whose global selected family contains conflicting precedence.
4. Exact decision-obligation normalization plus irrelevant-authority projection.
5. Behavioral-probe equivalence specialized to the obligation/authority state.
6. Under the frozen assumptions, a bounded behavioral universe
       T(k,r) <= Bell(2k) * 2^(3r)
   and an FPT exact-resolvability algorithm parameterized by initial unresolved decision obligations k plus relevant authority tokens r.
7. Exact/exhaustive/randomized computational falsification and controlled capability-gate realization.

## Novelty wording

Preferred:
"We study a restricted evidence-acquisition problem in which observations refine uncertainty while their execution can revoke authority needed by later observations. Within this model, we derive ..."

Avoid:
- "We invent belief-state compression."
- "We introduce action equivalence."
- "We introduce parameterized planning/kernelization."
- "No previous work has considered revocation and information gathering."
- "First ever" unless a systematic review supports it.
- Any Android-permission claim from the current app-owned capability-gate experiment.

## Literature-audit status

Focused searches located established work on:
- POMDP belief-state sufficiency and information gathering;
- action equivalence / representative actions;
- parameterized complexity and kernel bounds for planning;
- authorization revocation.

No source located in this focused pass states the same combined SAFESEP-II theorem package. This is evidence for positioning, not a proof of novelty or priority.

## Manuscript gate

Open manuscript drafting only after the current controlled-experiment CI completes successfully. If CI fails, fix the implementation before drafting results around it.
