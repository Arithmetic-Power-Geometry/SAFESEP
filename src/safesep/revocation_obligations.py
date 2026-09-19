"""Decision-obligation quotient for SAFESEP-II exact revocation semantics."""
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


def obligation_quotient_resolves(
    worlds: frozenset[World],
    decisions: Mapping[World, Decision],
    probes: tuple[RevProbe, ...],
    authority: frozenset[str],
) -> bool:
    """Exact recursion on decision-incompatible pair obligations."""

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
            outcome_values = {om[w] for w in C}
            A2 = (A | p.grants) - p.revokes
            remaining = tuple(j for j in unused if j != i)
            children: list[frozenset[Pair]] = []
            for o in outcome_values:
                child_pairs = frozenset(
                    pair for pair in P
                    if all(om[w] == o for w in pair)
                )
                if child_pairs:
                    children.append(child_pairs)

            # Progress occurs if the observation removes at least one unresolved
            # obligation OR authority changes.  In particular, children == []
            # means the probe resolved every obligation and must be accepted.
            surviving = frozenset(pair for child in children for pair in child)
            if surviving == P and A2 == A:
                continue
            if all(solve(child, A2, remaining) for child in children):
                return True
        return False

    return solve(obligations(worlds, decisions), authority, tuple(range(len(probes))))
