"""Branch-relative authorization-proof eligibility baseline.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

This module tests the DRAC branch-evolution idea without overclaiming novelty.
A proof may be usable only on specified belief/knowledge states.  This is an
explicit finite baseline for comparison with stateful authorization logic and
contingent planning.
"""
from dataclasses import dataclass
from typing import FrozenSet, Hashable, Iterable, Mapping, Sequence

World = Hashable
Decision = Hashable
Outcome = Hashable


@dataclass(frozen=True)
class DynamicProof:
    name: str
    forbidden_decisions: FrozenSet[Decision]
    max_worlds: int | None = None

    def eligible(self, C: FrozenSet[World], decisions: Mapping[World, Decision]) -> bool:
        unresolved = frozenset(decisions[w] for w in C)
        if not self.forbidden_decisions.isdisjoint(unresolved):
            return False
        return self.max_worlds is None or len(C) <= self.max_worlds


@dataclass(frozen=True)
class DynamicProbe:
    name: str
    cost: float
    outcomes: Mapping[World, Outcome]
    proofs: Sequence[DynamicProof]

    def eligible(self, C: FrozenSet[World], decisions: Mapping[World, Decision]) -> bool:
        return any(p.eligible(C, decisions) for p in self.proofs)


def critical(C: Iterable[World], decisions: Mapping[World, Decision]) -> bool:
    return len({decisions[w] for w in C}) > 1


def branches(probe: DynamicProbe, C: Iterable[World]):
    out = {}
    for w in C:
        out.setdefault(probe.outcomes[w], set()).add(w)
    return tuple(frozenset(v) for v in out.values())


def cheapest_eligible_leaving_incompatibility(C, decisions, probes):
    C = frozenset(C)
    candidates = []
    for p in probes:
        if not p.eligible(C, decisions):
            continue
        bs = branches(p, C)
        if len(bs) > 1 and any(critical(b, decisions) for b in bs):
            candidates.append(p)
    return min(candidates, key=lambda p: (p.cost, p.name), default=None)


def drac_exists(C, decisions, probes):
    C = frozenset(C)
    probes = tuple(probes)
    memo, visiting = {}, set()

    def win(S):
        if not critical(S, decisions):
            return True
        if S in memo:
            return memo[S]
        if S in visiting:
            return False
        visiting.add(S)
        for p in probes:
            if not p.eligible(S, decisions):
                continue
            bs = branches(p, S)
            if len(bs) <= 1:
                continue
            if all(win(b) for b in bs):
                visiting.remove(S)
                memo[S] = True
                return True
        visiting.remove(S)
        memo[S] = False
        return False

    return win(C)
