"""Observation-Conditioned Authority Topology (OCAT) collision experiment.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

This module tests a stronger candidate and deliberately treats it as a novelty
attack: an observation can activate an authority edge needed by a resolver.
The construction is representable by an ordinary full-state contingent planner,
so the mechanism alone is not claimed as novel.
"""
from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True)
class OCATCase:
    n: int
    activate_on_rest: bool

    @property
    def worlds(self):
        return tuple([f"r{i}" for i in range(self.n)] + [f"w{i}" for i in range(self.n)])

    def decision(self, w: str) -> str:
        return "R" if w.startswith("r") else "W"

    def q_outcome(self, w: str) -> str:
        return "special" if w == "r0" else "rest"

    @property
    def initial_authority_edges(self):
        # Both matched systems expose exactly the same initial authority graph.
        return frozenset({("alpha", "r")})

    def post_q_edges(self, outcome: str):
        edges = set(self.initial_authority_edges)
        if self.activate_on_rest and outcome == "rest":
            edges.add(("q:rest", "alpha"))
        return frozenset(edges)


def incompatible_pair_count(case: OCATCase, worlds: FrozenSet[str]) -> int:
    r = sum(case.decision(w) == "R" for w in worlds)
    w = len(worlds) - r
    return r * w


def cheapest_unresolved(case: OCATCase):
    branches = {}
    for w in case.worlds:
        branches.setdefault(case.q_outcome(w), set()).add(w)
    worst = max(incompatible_pair_count(case, frozenset(B)) for B in branches.values())
    return {"name": "q", "cost": 1.0, "worst_incompatible_pairs": worst}


def initial_signature(case: OCATCase):
    return (len(case.worlds), case.n, case.n, case.initial_authority_edges, 1.0)


def full_state_resolvable(case: OCATCase) -> bool:
    """Exact result for the minimal q->authority-edge->resolver witness."""
    rest = frozenset(w for w in case.worlds if case.q_outcome(w) == "rest")
    if incompatible_pair_count(case, rest) == 0:
        return True
    # r resolves R/W iff the observation-activated support edge exists.
    return ("q:rest", "alpha") in case.post_q_edges("rest") and ("alpha", "r") in case.post_q_edges("rest")


def matched_pair(n=100):
    return OCATCase(n, True), OCATCase(n, False)
