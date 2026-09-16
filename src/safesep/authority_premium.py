"""Authorization-safe evidence premium.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

This module isolates a quantitative diagnostic after the full joint-state
planning collision.  The premium is the extra decision-resolution cost caused
by authorization constraints relative to the same experiment system with
those constraints removed.
"""
from dataclasses import dataclass
from math import inf
from typing import Mapping, Tuple


@dataclass(frozen=True)
class PremiumCase:
    worlds: Tuple[str, ...]
    decisions: Mapping[str, str]
    q_outcome: Mapping[str, str]
    q_cost: float
    resolver_cost: float
    resolver_authorized_after_q: bool


def make_case(n: int = 50, authorized: bool = True) -> PremiumCase:
    if n < 2:
        raise ValueError("n must be >=2")
    rs = tuple(f"r{i}" for i in range(n))
    ws = tuple(f"w{i}" for i in range(n))
    worlds = rs + ws
    decisions = {w: ("R" if w.startswith("r") else "W") for w in worlds}
    q_outcome = {w: ("special" if w == "r0" else "rest") for w in worlds}
    return PremiumCase(worlds, decisions, q_outcome, 1.0, 1.0, authorized)


def cheapest_experiment_leaving_incompatibility(case: PremiumCase):
    rest = tuple(w for w in case.worlds if case.q_outcome[w] == "rest")
    r = sum(case.decisions[w] == "R" for w in rest)
    x = len(rest) - r
    return {"name": "q", "cost": case.q_cost,
            "unresolved_branches": 1,
            "worst_incompatible_pairs": r * x}


def unconstrained_resolution_cost(case: PremiumCase) -> float:
    """Perfect resolver is available immediately when authority is ignored."""
    return case.resolver_cost


def authorization_safe_resolution_cost(case: PremiumCase) -> float:
    """Construction cost: q then resolver, or infinity if resolver is blocked."""
    if not case.resolver_authorized_after_q:
        return inf
    return case.q_cost + case.resolver_cost


def authority_premium(case: PremiumCase) -> float:
    safe = authorization_safe_resolution_cost(case)
    base = unconstrained_resolution_cost(case)
    return inf if safe == inf else safe - base
