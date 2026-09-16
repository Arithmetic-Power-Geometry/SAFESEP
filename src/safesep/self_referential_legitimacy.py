"""Self-referential evidence-legitimacy attack.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

This module deliberately tests whether a policy/evidence circularity is new.
It is retained as a collision result: protected credentials and cyclic policy
interdependencies are established in automated trust negotiation (ATN).
"""
from dataclasses import dataclass
from typing import FrozenSet, Mapping, Tuple


@dataclass(frozen=True)
class SRLCase:
    n: int
    break_cycle: bool

    @property
    def worlds(self) -> Tuple[str, ...]:
        return tuple(f"r{i}" for i in range(self.n)) + tuple(f"w{i}" for i in range(self.n))

    def decision(self, w: str) -> str:
        return "R" if w.startswith("r") else "W"

    def q_outcome(self, w: str) -> str:
        return "special" if w == "r0" else "rest"


def incompatible_pairs(case: SRLCase, worlds=None) -> int:
    worlds = case.worlds if worlds is None else tuple(worlds)
    nr = sum(case.decision(w) == "R" for w in worlds)
    nw = len(worlds) - nr
    return nr * nw


def cheapest_unresolved(case: SRLCase):
    rest = tuple(w for w in case.worlds if case.q_outcome(w) == "rest")
    return {"name": "q", "cost": 1.0,
            "worst_incompatible_pairs": incompatible_pairs(case, rest)}


def dependency_edges(case: SRLCase) -> FrozenSet[tuple[str, str]]:
    """policy -> evidence and evidence -> policy legitimacy dependencies."""
    return frozenset({("policy_alpha", "evidence_E"),
                      ("evidence_E", "policy_alpha")})


def grounded(case: SRLCase) -> FrozenSet[str]:
    """Least fixed-point closure; breaker is an externally justified seed."""
    known = {"q"}
    if case.break_cycle:
        known.add("policy_alpha")
    changed = True
    while changed:
        changed = False
        if "policy_alpha" in known and "evidence_E" not in known:
            known.add("evidence_E"); changed = True
        if "evidence_E" in known and "policy_alpha" not in known:
            known.add("policy_alpha"); changed = True
    return frozenset(known)


def resolver_legitimate(case: SRLCase) -> bool:
    return "policy_alpha" in grounded(case) and "evidence_E" in grounded(case)


def safely_resolvable(case: SRLCase) -> bool:
    # q resolves r0; the residual R/W branch requires the protected resolver.
    return resolver_legitimate(case)
