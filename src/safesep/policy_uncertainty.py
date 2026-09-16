"""Second-order policy uncertainty stress test for SAFESEP.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

This module deliberately tests a stronger-looking idea: the applicable
authorization rule is itself uncertain. The result is used as a novelty
attack, not as a novelty claim.
"""
from dataclasses import dataclass
from typing import Mapping, Tuple

World = str

@dataclass(frozen=True)
class PolicyCase:
    worlds: Tuple[World, ...]
    decisions: Mapping[World, str]
    policy: Mapping[World, str]
    q_outcome: Mapping[World, str]
    q_cost: float = 1.0


def make_case(n: int = 100) -> PolicyCase:
    if n < 2:
        raise ValueError("n must be >= 2")
    rs=tuple(f"r{i}" for i in range(n)); ws=tuple(f"w{i}" for i in range(n))
    worlds=rs+ws
    decisions={w:("R" if w.startswith("r") else "W") for w in worlds}
    # Two still-compatible policy hypotheses. Policy identity is not needed
    # for q; it remains unresolved on q=rest.
    policy={w:("P0" if w.endswith("0") else "P1") for w in worlds}
    q={w:("special" if w=="r0" else "rest") for w in worlds}
    return PolicyCase(worlds, decisions, policy, q)


def incompatible_pairs(case: PolicyCase, worlds=None) -> int:
    C=case.worlds if worlds is None else tuple(worlds)
    r=sum(case.decisions[w]=="R" for w in C)
    w=sum(case.decisions[x]=="W" for x in C)
    return r*w


def cheapest_unresolved(case: PolicyCase):
    rest=tuple(w for w in case.worlds if case.q_outcome[w]=="rest")
    return {"name":"q", "cost":case.q_cost,
            "worst_incompatible_pairs":incompatible_pairs(case,rest),
            "policies_remaining":len({case.policy[w] for w in rest})}


def second_order_state_size(case: PolicyCase) -> int:
    """Number of explicit (world, policy) labels in this construction."""
    return len({(w,case.policy[w]) for w in case.worlds})
