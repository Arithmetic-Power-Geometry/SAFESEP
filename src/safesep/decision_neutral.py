"""Decision-relative authority closure diagnostics.

A resolving probe is decision-neutral on an unresolved class C only when its
admissibility does not presuppose which mutually incompatible authorization
decision is correct.  This module intentionally keeps the criterion separate
from ordinary state-wise action applicability.
"""
from dataclasses import dataclass
from typing import Callable, FrozenSet, Hashable, Iterable, Mapping, Optional

World = Hashable
Decision = Hashable
Outcome = Hashable

@dataclass(frozen=True)
class NeutralProbe:
    name: str
    cost: float
    outcome: Mapping[World, Outcome]
    # admissible_without_decision[w] means the probe is justified in w by a
    # basis independent of the disputed decision itself.
    admissible_without_decision: Mapping[World, bool]


def decision_critical(worlds: Iterable[World], decisions: Mapping[World, Decision]) -> bool:
    return len({decisions[w] for w in worlds}) > 1


def decision_neutral_admissible(probe: NeutralProbe, worlds: Iterable[World]) -> bool:
    ws = tuple(worlds)
    return bool(ws) and all(probe.admissible_without_decision.get(w, False) for w in ws)


def incompatible_pair_count(worlds: Iterable[World], decisions: Mapping[World, Decision]) -> int:
    ws = tuple(worlds)
    return sum(1 for i, a in enumerate(ws) for b in ws[i+1:] if decisions[a] != decisions[b])


def partitions(probe: NeutralProbe, worlds: Iterable[World]):
    out = {}
    for w in worlds:
        out.setdefault(probe.outcome[w], set()).add(w)
    return list(out.values())


def cheapest_neutral_probe_leaving_incompatibility(
    worlds: Iterable[World],
    decisions: Mapping[World, Decision],
    probes: Iterable[NeutralProbe],
) -> Optional[NeutralProbe]:
    """Cheapest decision-neutral informative probe leaving an incompatible branch."""
    ws = frozenset(worlds)
    candidates = []
    for p in probes:
        if not decision_neutral_admissible(p, ws):
            continue
        parts = partitions(p, ws)
        if len(parts) <= 1:
            continue
        if any(decision_critical(branch, decisions) for branch in parts):
            candidates.append(p)
    return min(candidates, key=lambda p: (p.cost, p.name), default=None)


def neutral_safe_separable(
    worlds: FrozenSet[World],
    decisions: Mapping[World, Decision],
    probes: Iterable[NeutralProbe],
) -> bool:
    """Exact finite AND/OR test under decision-neutral probe admissibility."""
    probes = tuple(probes)
    memo = {}
    visiting = set()

    def win(C: FrozenSet[World]) -> bool:
        if not decision_critical(C, decisions):
            return True
        if C in memo:
            return memo[C]
        if C in visiting:
            return False
        visiting.add(C)
        for p in probes:
            if not decision_neutral_admissible(p, C):
                continue
            children = [frozenset(x) for x in partitions(p, C)]
            if len(children) <= 1:
                continue
            if all(win(child) for child in children):
                visiting.remove(C)
                memo[C] = True
                return True
        visiting.remove(C)
        memo[C] = False
        return False

    return win(worlds)
