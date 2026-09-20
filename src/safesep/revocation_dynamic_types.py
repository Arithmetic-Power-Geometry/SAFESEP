"""Dynamic behavioral-type quotient for SAFESEP-II."""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from typing import Hashable, Mapping

from .revocation_exact import Decision, RevProbe, World
from .revocation_probe_types import probe_type

Pair = frozenset[World]


def _obligations(C: frozenset[World], decisions: Mapping[World, Decision]) -> frozenset[Pair]:
    return frozenset(frozenset((u, v)) for u, v in combinations(C, 2) if decisions[u] != decisions[v])


def _worlds(P: frozenset[Pair]) -> frozenset[World]:
    return frozenset(w for pair in P for w in pair)


def _relevant_tokens(probes: tuple[RevProbe, ...]) -> frozenset[str]:
    return frozenset(t for p in probes for t in p.requires)


def _dedup_dynamic(probes: tuple[RevProbe, ...], P: frozenset[Pair]) -> tuple[RevProbe, ...]:
    W = _worlds(P)
    R = _relevant_tokens(probes)
    seen = set()
    out = []
    for p in probes:
        t = probe_type(p, W, R)
        if t not in seen:
            seen.add(t)
            out.append(p)
    return tuple(out)


def dynamic_type_quotient_resolves(
    worlds: frozenset[World],
    decisions: Mapping[World, Decision],
    probes: tuple[RevProbe, ...],
    authority: frozenset[str],
) -> bool:
    """Exact candidate solver that dynamically retypes and deduplicates probes."""

    @lru_cache(maxsize=None)
    def solve(P: frozenset[Pair], A: frozenset[str], ps: tuple[RevProbe, ...]) -> bool:
        if not P:
            return True
        ps = _dedup_dynamic(ps, P)
        R = _relevant_tokens(ps)
        A = A & R
        C = _worlds(P)
        for i, p in enumerate(ps):
            if not p.requires <= A:
                continue
            om = p.outcome_map()
            rest = ps[:i] + ps[i + 1:]
            raw_A2 = (A | p.grants) - p.revokes
            outcomes = {om[w] for w in C}
            ok = True
            for o in outcomes:
                child = frozenset(pair for pair in P if all(om[w] == o for w in pair))
                if not child:
                    continue
                child_ps = _dedup_dynamic(rest, child)
                child_R = _relevant_tokens(child_ps)
                if not solve(child, raw_A2 & child_R, child_ps):
                    ok = False
                    break
            if ok:
                return True
        return False

    P0 = _obligations(worlds, decisions)
    ps0 = _dedup_dynamic(probes, P0)
    return solve(P0, authority & _relevant_tokens(ps0), ps0)
