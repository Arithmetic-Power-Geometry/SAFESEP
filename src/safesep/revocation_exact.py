"""Exact finite revocation semantics for SAFESEP-II falsification."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Hashable, Mapping

World = Hashable
Decision = Hashable


@dataclass(frozen=True)
class RevProbe:
    name: str
    outcomes: tuple[tuple[World, Hashable], ...]
    requires: frozenset[str] = frozenset()
    grants: frozenset[str] = frozenset()
    revokes: frozenset[str] = frozenset()

    def outcome_map(self) -> dict[World, Hashable]:
        return dict(self.outcomes)


def exact_revocation_resolves(
    worlds: frozenset[World],
    decisions: Mapping[World, Decision],
    probes: tuple[RevProbe, ...],
    authority: frozenset[str],
) -> bool:
    """Exact AND/OR resolver with world-independent grants and revocations."""

    @lru_cache(maxsize=None)
    def solve(C: frozenset[World], A: frozenset[str], unused: tuple[int, ...]) -> bool:
        if len({decisions[w] for w in C}) <= 1:
            return True
        for i in unused:
            p = probes[i]
            if not p.requires <= A:
                continue
            om = p.outcome_map()
            groups: dict[Hashable, set[World]] = {}
            for w in C:
                groups.setdefault(om[w], set()).add(w)
            A2 = (A | p.grants) - p.revokes
            remaining = tuple(j for j in unused if j != i)
            # Require joint-state progress: observation refinement or authority change.
            if len(groups) == 1 and A2 == A:
                continue
            if all(solve(frozenset(g), A2, remaining) for g in groups.values()):
                return True
        return False

    return solve(worlds, authority, tuple(range(len(probes))))


def every_incompatible_pair_has_initial_separator(
    worlds: frozenset[World],
    decisions: Mapping[World, Decision],
    probes: tuple[RevProbe, ...],
    authority: frozenset[str],
) -> bool:
    """Naive pairwise criterion intentionally used as a falsification target."""
    for u in worlds:
        for v in worlds:
            if repr(u) >= repr(v) or decisions[u] == decisions[v]:
                continue
            if not any(
                p.requires <= authority
                and p.outcome_map()[u] != p.outcome_map()[v]
                for p in probes
            ):
                return False
    return True
