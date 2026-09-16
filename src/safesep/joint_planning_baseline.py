"""Independent combined-state contingent-planning baseline for joint coupling.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

This module deliberately attacks the matched-marginal witness by exposing the
joint information/authority state to an ordinary contingent planner. It is a
collision baseline, not a novelty claim.
"""
from dataclasses import dataclass
from typing import FrozenSet

from .joint_coupling import JointCase


@dataclass(frozen=True)
class CombinedState:
    worlds: FrozenSet[str]
    tokens: FrozenSet[str]


def decision_homogeneous(case: JointCase, worlds: FrozenSet[str]) -> bool:
    return len({case.decisions[w] for w in worlds}) <= 1


def after_q(case: JointCase, outcome: str) -> CombinedState:
    worlds = frozenset(w for w in case.worlds if case.q_outcome[w] == outcome)
    token = case.outcome_token[outcome]
    return CombinedState(worlds, frozenset({token}))


def resolver_applicable(case: JointCase, state: CombinedState, resolver: str) -> bool:
    return any(case.token_resolver.get(t) == resolver for t in state.tokens)


def combined_state_contingent_resolvable(case: JointCase) -> bool:
    """Exact result for the deliberately minimal q -> resolver witness.

    q is root-executable. Every q outcome must either be decision homogeneous
    or have the resolver appropriate to that branch enabled by the acquired
    authority token. This is exactly a contingent-plan AND over observations.
    """
    outcomes = set(case.q_outcome.values())
    for outcome in outcomes:
        state = after_q(case, outcome)
        if decision_homogeneous(case, state.worlds):
            continue
        required = f"resolve_{outcome}"
        if not resolver_applicable(case, state, required):
            return False
    return True


def joint_state_signature(case: JointCase):
    """Full branch-sensitive state signature retained by a planner."""
    rows = []
    for outcome in sorted(set(case.q_outcome.values())):
        s = after_q(case, outcome)
        rows.append((outcome, len(s.worlds), tuple(sorted(s.tokens)),
                     tuple(sorted(case.token_resolver[t] for t in s.tokens))))
    return tuple(rows)
