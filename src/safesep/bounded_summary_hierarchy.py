"""Bounded-summary hierarchy attack for SAFESEP.

This module deliberately tests whether matching all local summaries through order k
can hide a global authorization obstruction.  It is a controlled theorem family,
not an empirical authorization claim.
"""
from dataclasses import dataclass
from itertools import combinations
from typing import Tuple


@dataclass(frozen=True)
class HierarchyCase:
    k: int
    blocked: bool

    @property
    def cycle_size(self) -> int:
        return self.k + 1


def incompatible_pair_count(n: int) -> int:
    """After q isolates one R world, residual R/W incompatible pairs."""
    return (n - 1) * n


def cheapest_unresolved(n: int):
    return {"name": "q", "cost": 1.0, "worst_incompatible_pairs": incompatible_pair_count(n)}


def local_summary(case: HierarchyCase, order: int) -> Tuple:
    """Summary visible to any view touching at most `order` acquisition dependencies.

    A and B are constructed to be identical for every order <= k.  The hidden bit is
    a global closure condition around a cycle of length k+1.
    """
    if order > case.k:
        return (case.k, order, case.blocked)
    return (case.k, order, case.cycle_size, "all_local_paths_open")


def all_summaries_match_through_k(a: HierarchyCase, b: HierarchyCase) -> bool:
    if a.k != b.k:
        return False
    return all(local_summary(a, j) == local_summary(b, j) for j in range(1, a.k + 1))


def globally_resolvable(case: HierarchyCase) -> bool:
    """A has an external grounding edge; B closes only through the full k+1 cycle."""
    return not case.blocked


def matched_pair(k: int):
    if k < 1:
        raise ValueError("k must be >= 1")
    return HierarchyCase(k, False), HierarchyCase(k, True)
