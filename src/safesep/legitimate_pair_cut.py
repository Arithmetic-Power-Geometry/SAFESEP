"""Legitimate incompatible-pair cut certificates for SAFESEP.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

This module deliberately separates an established pair-cover idea from the
authorization-specific obstruction: every decision-incompatible pair must be
separated on a resolving path, but only legitimately executable experiments
may perform that separation.
"""
from dataclasses import dataclass
from typing import FrozenSet, Mapping, Sequence, Tuple

World = str
Pair = Tuple[World, World]

@dataclass(frozen=True)
class CutExperiment:
    name: str
    cost: float
    outcomes: Mapping[World, str]
    legitimate: bool

@dataclass(frozen=True)
class PairCutCase:
    worlds: Tuple[World, ...]
    decisions: Mapping[World, str]
    experiments: Tuple[CutExperiment, ...]


def incompatible_pairs(case: PairCutCase) -> FrozenSet[Pair]:
    out = set()
    for i, a in enumerate(case.worlds):
        for b in case.worlds[i + 1:]:
            if case.decisions[a] != case.decisions[b]:
                out.add((a, b))
    return frozenset(out)


def separated_pairs(case: PairCutCase, e: CutExperiment) -> FrozenSet[Pair]:
    return frozenset((a, b) for a, b in incompatible_pairs(case)
                     if e.outcomes[a] != e.outcomes[b])


def legitimate_pair_cover(case: PairCutCase) -> FrozenSet[Pair]:
    covered = set()
    for e in case.experiments:
        if e.legitimate:
            covered.update(separated_pairs(case, e))
    return frozenset(covered)


def uncovered_legitimate_pairs(case: PairCutCase) -> FrozenSet[Pair]:
    return incompatible_pairs(case) - legitimate_pair_cover(case)


def pair_cut_obstruction(case: PairCutCase) -> bool:
    """Sufficient impossibility certificate for this static-legitimacy model."""
    return bool(uncovered_legitimate_pairs(case))


def cheapest_legitimate_unresolved(case: PairCutCase):
    """Cheapest legitimate informative experiment leaving an incompatible branch."""
    best = None
    for e in case.experiments:
        if not e.legitimate:
            continue
        branches = {}
        for w in case.worlds:
            branches.setdefault(e.outcomes[w], []).append(w)
        if len(branches) < 2:
            continue
        unresolved = []
        for branch in branches.values():
            r = sum(case.decisions[w] == "R" for w in branch)
            x = len(branch) - r
            if r and x:
                unresolved.append(r * x)
        if not unresolved:
            continue
        cand = (e.cost, e.name, len(unresolved), max(unresolved))
        if best is None or cand < best:
            best = cand
    if best is None:
        return None
    return {"cost": best[0], "name": best[1],
            "unresolved_branches": best[2],
            "worst_incompatible_pairs": best[3]}


def matched_pair_cut_family(n: int = 50):
    """A has legitimate pair coverage; B has the same tests but resolver blocked."""
    if n < 2:
        raise ValueError("n must be >=2")
    rs = tuple(f"r{i}" for i in range(n))
    ws = tuple(f"w{i}" for i in range(n))
    worlds = rs + ws
    decisions = {w: ("R" if w.startswith("r") else "W") for w in worlds}
    q = {w: ("special" if w == "r0" else "rest") for w in worlds}
    resolver = {w: decisions[w] for w in worlds}
    qA = CutExperiment("q", 1.0, q, True)
    qB = CutExperiment("q", 1.0, q, True)
    rA = CutExperiment("resolver", 1.0, resolver, True)
    rB = CutExperiment("resolver", 1.0, resolver, False)
    return (PairCutCase(worlds, decisions, (qA, rA)),
            PairCutCase(worlds, decisions, (qB, rB)))
