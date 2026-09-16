"""Representation-independent legitimate incompatible-pair cover lower bound.

The certificate depends only on the current decision-critical branch C, experiment
outcome partitions, experiment costs, and branchwise legitimacy.  It does not depend
on how a planner encodes belief state.
"""
from dataclasses import dataclass
from math import ceil
from typing import Callable, Iterable, Mapping, Sequence


@dataclass(frozen=True)
class Experiment:
    name: str
    cost: float
    outcome: Callable[[str], str]
    legitimate: Callable[[str], bool]


def incompatible_pairs(worlds: Sequence[str], decision: Callable[[str], str]):
    return {(a,b) for i,a in enumerate(worlds) for b in worlds[i+1:]
            if decision(a) != decision(b)}


def separated_pairs(worlds: Sequence[str], decision, e: Experiment):
    return {(a,b) for (a,b) in incompatible_pairs(worlds, decision)
            if e.outcome(a) != e.outcome(b)}


def branchwise_legitimate(worlds: Sequence[str], e: Experiment) -> bool:
    return all(e.legitimate(w) for w in worlds)


def cheapest_unresolved_experiment(worlds, decision, experiments: Iterable[Experiment]):
    """Cheapest legitimate informative experiment that leaves an incompatible branch."""
    best = None
    for e in experiments:
        if not branchwise_legitimate(worlds, e):
            continue
        branches = {}
        for w in worlds:
            branches.setdefault(e.outcome(w), []).append(w)
        if len(branches) < 2:
            continue
        residual = max((len(incompatible_pairs(b, decision)) for b in branches.values()), default=0)
        if residual <= 0:
            continue
        cand = (e.cost, e.name, residual)
        if best is None or cand < best:
            best = cand
    return None if best is None else {"name":best[1], "cost":best[0], "worst_incompatible_pairs":best[2]}


def pair_cover_lower_bound(worlds, decision, experiments: Iterable[Experiment]):
    """A representation-independent cost lower bound.

    Any resolving policy must separate every initially incompatible pair along the
    realized branch.  At the current branch only experiments legitimate in every
    compatible world can be selected.  If m is the largest number of currently
    incompatible pairs separated by any such experiment and c_min its minimum cost,
    ceil(|P|/m)*c_min is a coarse cover lower bound.  If no legitimate experiment
    separates any incompatible pair, the branch is immediately obstructed.

    This is deliberately only a lower-bound/certificate, not an optimality claim.
    """
    P = incompatible_pairs(worlds, decision)
    if not P:
        return {"pairs":0, "max_cover":0, "min_cost":0.0, "lower_bound":0.0, "obstructed":False}
    usable = []
    for e in experiments:
        if branchwise_legitimate(worlds, e):
            k = len(separated_pairs(worlds, decision, e))
            if k:
                usable.append((e,k))
    if not usable:
        return {"pairs":len(P), "max_cover":0, "min_cost":None, "lower_bound":float("inf"), "obstructed":True}
    max_cover = max(k for _,k in usable)
    min_cost = min(e.cost for e,_ in usable)
    return {"pairs":len(P), "max_cover":max_cover, "min_cost":min_cost,
            "lower_bound":ceil(len(P)/max_cover)*min_cost, "obstructed":False}


def matched_case(n=100, variant="A"):
    worlds = tuple([f"r{i}" for i in range(n)] + [f"w{i}" for i in range(n)])
    decision = lambda w: "R" if w.startswith("r") else "W"
    q = Experiment("q",1.0,lambda w: "special" if w=="r0" else "rest",lambda w: True)
    # Same costs and same outcome partitions in A/B. Only branchwise legitimacy differs.
    resolver = Experiment("resolve",1.0,decision,
                          (lambda w: True) if variant=="A" else (lambda w: w=="r0"))
    return worlds, decision, (q,resolver)
