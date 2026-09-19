"""Relevance-pruned obligation/authority quotient for SAFESEP-II."""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from typing import Hashable, Mapping

from .revocation_exact import Decision, RevProbe, World

Pair = frozenset[World]


def obligations(C: frozenset[World], decisions: Mapping[World, Decision]) -> frozenset[Pair]:
    return frozenset(
        frozenset((u, v))
        for u, v in combinations(C, 2)
        if decisions[u] != decisions[v]
    )


def worlds_from_obligations(P: frozenset[Pair]) -> frozenset[World]:
    return frozenset(w for pair in P for w in pair)


def relevant_tokens(probes: tuple[RevProbe, ...], unused: tuple[int, ...]) -> frozenset[str]:
    """Tokens whose presence can affect future probe executability."""
    return frozenset(t for i in unused for t in probes[i].requires)


def prune_authority(
    A: frozenset[str], probes: tuple[RevProbe, ...], unused: tuple[int, ...]
) -> frozenset[str]:
    return A & relevant_tokens(probes, unused)


def relevance_pruned_resolves(
    worlds: frozenset[World],
    decisions: Mapping[World, Decision],
    probes: tuple[RevProbe, ...],
    authority: frozenset[str],
) -> bool:
    """Exact recursion after dropping authority irrelevant to remaining requirements."""

    @lru_cache(maxsize=None)
    def solve(P: frozenset[Pair], A: frozenset[str], unused: tuple[int, ...]) -> bool:
        if not P:
            return True
        C = worlds_from_obligations(P)
        for i in unused:
            p = probes[i]
            if not p.requires <= A:
                continue
            om = p.outcome_map()
            remaining = tuple(j for j in unused if j != i)
            raw_A2 = (A | p.grants) - p.revokes
            A2 = prune_authority(raw_A2, probes, remaining)
            outcomes = {om[w] for w in C}
            children = []
            for o in outcomes:
                child = frozenset(
                    pair for pair in P if all(om[w] == o for w in pair)
                )
                if child:
                    children.append(child)
            if all(solve(child, A2, remaining) for child in children):
                return True
        return False

    U = tuple(range(len(probes)))
    return solve(obligations(worlds, decisions), prune_authority(authority, probes, U), U)
