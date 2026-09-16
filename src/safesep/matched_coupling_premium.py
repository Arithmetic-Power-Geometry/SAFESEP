"""Matched-cost branchwise authorization-coupling stress family.

This module deliberately keeps the ordinary information experiment, action costs,
action counts, per-world legitimate action counts, and unconstrained optimum fixed.
The only changed object is the incidence relation between compatible worlds and
which unit-cost resolver is legitimate in that world.

It is a collision/novelty-attack construction, not by itself a novelty claim.
"""
from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class MatchedCouplingCase:
    n: int
    aligned: bool

    @property
    def worlds(self) -> Tuple[str, ...]:
        return tuple([f"r{i}" for i in range(self.n)] + [f"w{i}" for i in range(self.n)])

    def decision(self, w: str) -> str:
        return "R" if w.startswith("r") else "W"

    def q_outcome(self, w: str) -> str:
        return "special" if w == "r0" else "rest"

    @property
    def resolvers(self) -> Tuple[str, ...]:
        # Same number and same unit cost in both systems.
        return tuple(f"e{i}" for i in range(self.n))

    def legitimate(self, e: str, w: str) -> bool:
        i = int(e[1:])
        if self.aligned:
            # e0 is common on the unresolved rest branch; the remaining
            # incidences are padded so every world still has >=1 witness.
            if e == "e0" and w != "r0":
                return True
            return w == f"r{i}"
        # Dispersed incidence: each resolver is legitimate only for a matched
        # R/W index pair. Every world has one unit-cost witness, but no resolver
        # is legitimate throughout the unresolved branch.
        return w in {f"r{i}", f"w{i}"}

    def structural_signature(self) -> Dict[str, int]:
        # Deliberately coarse matched quantities used by the regression.
        return {
            "worlds": 2 * self.n,
            "R": self.n,
            "W": self.n,
            "q_cost": 1,
            "resolver_cost": 1,
            "resolver_count": self.n,
            "unconstrained_optimum": 1,
        }


def incompatible_pairs_after_q(case: MatchedCouplingCase) -> int:
    # q isolates r0; rest has n-1 R worlds and n W worlds.
    return (case.n - 1) * case.n


def cheapest_unresolved(case: MatchedCouplingCase) -> Dict[str, int]:
    return {"experiment": "q", "cost": 1,
            "worst_incompatible_pairs": incompatible_pairs_after_q(case)}


def every_residual_world_has_unit_witness(case: MatchedCouplingCase) -> bool:
    rest = [w for w in case.worlds if w != "r0"]
    return all(any(case.legitimate(e, w) for e in case.resolvers) for w in rest)


def common_unit_resolver(case: MatchedCouplingCase) -> bool:
    rest = [w for w in case.worlds if w != "r0"]
    return any(all(case.legitimate(e, w) for w in rest) for e in case.resolvers)


def safe_cost_after_q(case: MatchedCouplingCase) -> float:
    # In this restricted one-step resolver class, finite safe completion exists
    # exactly when one resolver is legitimate throughout the branch.
    return 1.0 if common_unit_resolver(case) else float("inf")


def matched_pair(n: int = 100):
    return MatchedCouplingCase(n, True), MatchedCouplingCase(n, False)
