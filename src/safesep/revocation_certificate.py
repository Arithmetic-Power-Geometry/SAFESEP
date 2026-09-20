"""Structural certificates for SAFESEP-II revocable evidence."""
from __future__ import annotations

from collections.abc import Mapping
from itertools import combinations

from .revocation_exact import Decision, RevProbe, World


def incompatible_pairs(
    worlds: frozenset[World], decisions: Mapping[World, Decision]
) -> frozenset[frozenset[World]]:
    return frozenset(
        frozenset((u, v))
        for u, v in combinations(worlds, 2)
        if decisions[u] != decisions[v]
    )


def separators_for_pair(
    pair: frozenset[World], probes: tuple[RevProbe, ...]
) -> tuple[int, ...]:
    u, v = tuple(pair)
    return tuple(
        i for i, p in enumerate(probes)
        if p.outcome_map()[u] != p.outcome_map()[v]
    )


def has_static_noninterfering_cover(
    worlds: frozenset[World],
    decisions: Mapping[World, Decision],
    probes: tuple[RevProbe, ...],
    authority: frozenset[str],
) -> bool:
    """Sufficient-certificate candidate used for exhaustive falsification.

    Search subsets of initially executable probes that cover every incompatible
    pair and whose revocations never remove another selected probe's requirement.
    """
    obligations = incompatible_pairs(worlds, decisions)
    n = len(probes)
    for mask in range(1 << n):
        chosen = tuple(i for i in range(n) if mask & (1 << i))
        if any(not probes[i].requires <= authority for i in chosen):
            continue
        if any(
            probes[i].revokes & probes[j].requires
            for i in chosen for j in chosen if i != j
        ):
            continue
        covered = {
            pair
            for pair in obligations
            if any(i in separators_for_pair(pair, probes) for i in chosen)
        }
        if covered == set(obligations):
            return True
    return not obligations
