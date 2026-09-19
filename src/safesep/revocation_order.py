"""Ordered evidence certificates for SAFESEP-II revocable authority."""
from __future__ import annotations

from collections.abc import Mapping
from itertools import combinations

from .revocation_exact import Decision, RevProbe, World


def incompatible_pairs(worlds: frozenset[World], decisions: Mapping[World, Decision]):
    return tuple(
        (u, v) for u, v in combinations(worlds, 2) if decisions[u] != decisions[v]
    )


def _acyclic_precedence(chosen: tuple[int, ...], probes: tuple[RevProbe, ...]) -> bool:
    """Edge j->i means j must run before i because i revokes a requirement of j."""
    succ = {i: set() for i in chosen}
    indeg = {i: 0 for i in chosen}
    for i in chosen:
        for j in chosen:
            if i == j:
                continue
            if probes[i].revokes & probes[j].requires:
                # j must precede i
                if i not in succ[j]:
                    succ[j].add(i)
                    indeg[i] += 1
    ready = [i for i in chosen if indeg[i] == 0]
    seen = 0
    while ready:
        u = ready.pop()
        seen += 1
        for v in succ[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                ready.append(v)
    return seen == len(chosen)


def has_acyclic_separator_cover(
    worlds: frozenset[World],
    decisions: Mapping[World, Decision],
    probes: tuple[RevProbe, ...],
    authority: frozenset[str],
) -> bool:
    """Sufficient certificate: initially executable pair cover with acyclic precedence."""
    obligations = incompatible_pairs(worlds, decisions)
    if not obligations:
        return True
    n = len(probes)
    for mask in range(1, 1 << n):
        chosen = tuple(i for i in range(n) if mask & (1 << i))
        if any(not probes[i].requires <= authority for i in chosen):
            continue
        if not _acyclic_precedence(chosen, probes):
            continue
        if all(
            any(
                probes[i].outcome_map()[u] != probes[i].outcome_map()[v]
                for i in chosen
            )
            for u, v in obligations
        ):
            return True
    return False
