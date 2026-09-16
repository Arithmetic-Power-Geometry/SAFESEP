"""Branchwise universal-admissibility gap attack.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

This module isolates the difference between per-world availability of a resolving
probe and uniform branchwise executability while uncertainty remains.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class GapCase:
    n: int = 100
    uniform: bool = True

    @property
    def worlds(self):
        return tuple(f"r{i}" for i in range(self.n)) + tuple(f"w{i}" for i in range(self.n))

    def decision(self, w):
        return "R" if w.startswith("r") else "W"

    def q_outcome(self, w):
        return "special" if w == "r0" else "rest"


def incompatible_pairs(case, worlds=None):
    W = case.worlds if worlds is None else tuple(worlds)
    nr = sum(case.decision(w) == "R" for w in W)
    nw = sum(case.decision(w) == "W" for w in W)
    return nr * nw


def cheapest_unresolved(case):
    rest = tuple(w for w in case.worlds if case.q_outcome(w) == "rest")
    return {"name": "q", "cost": 1.0,
            "worst_incompatible_pairs": incompatible_pairs(case, rest)}


def per_world_resolver_available(case, w):
    # Every world individually has a resolver witness.
    return True


def resolver_name(case, w):
    if case.uniform:
        return "r"
    # In the nonuniform system, the witness is world-specific; while worlds remain
    # compatible there is no single resolver executable throughout the branch.
    return f"r_{w}"


def per_world_summary(case):
    return {"worlds": len(case.worlds),
            "R": case.n, "W": case.n,
            "each_world_has_resolver": all(per_world_resolver_available(case,w) for w in case.worlds),
            "resolver_cost_multiset": (1.0,) * len(case.worlds)}


def branchwise_uniform_resolver(case, worlds=None):
    W = case.worlds if worlds is None else tuple(worlds)
    if not W:
        return True
    return len({resolver_name(case,w) for w in W}) == 1


def safely_resolvable_after_q_rest(case):
    rest = tuple(w for w in case.worlds if case.q_outcome(w) == "rest")
    if incompatible_pairs(case, rest) == 0:
        return True
    return branchwise_uniform_resolver(case, rest)
