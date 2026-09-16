# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from dataclasses import dataclass
from functools import lru_cache
from math import inf
from typing import FrozenSet, Optional

from .model import Problem, Experiment, World

@dataclass(frozen=True)
class Tree:
    worlds: FrozenSet[World]
    experiment: Optional[str] = None
    cost: float = 0.0
    children: tuple[tuple[object, "Tree"], ...] = ()


def _partition(worlds: FrozenSet[World], e: Experiment):
    buckets = {}
    for w in worlds:
        buckets.setdefault(e.outcome(w), set()).add(w)
    return tuple((o, frozenset(ws)) for o, ws in buckets.items())


def solve_safesep(problem: Problem, worlds: FrozenSet[World] | None = None):
    """Minimax SafeSep cost and a witness tree.

    Cost model: experiment cost plus worst-case continuation cost.
    Only experiments admissible in every currently possible world may be used.
    """
    start = problem.worlds if worlds is None else worlds

    @lru_cache(maxsize=None)
    def rec(state: FrozenSet[World]):
        if problem.decision_homogeneous(state):
            return 0.0, Tree(state)
        best_cost, best_tree = inf, None
        for e in problem.experiments:
            if not e.is_admissible_on(state):
                continue
            parts = _partition(state, e)
            if len(parts) <= 1:
                continue
            child_rows = []
            worst = 0.0
            feasible = True
            for outcome, child in parts:
                c, t = rec(child)
                if c == inf:
                    feasible = False
                    break
                worst = max(worst, c)
                child_rows.append((outcome, t))
            if feasible:
                total = e.cost + worst
                if total < best_cost:
                    best_cost = total
                    best_tree = Tree(state, e.name, total, tuple(child_rows))
        return best_cost, best_tree

    return rec(start)


def solve_unconstrained(problem: Problem, worlds: FrozenSet[World] | None = None):
    """ARC-like minimax resolver ignoring experiment admissibility."""
    start = problem.worlds if worlds is None else worlds

    @lru_cache(maxsize=None)
    def rec(state: FrozenSet[World]):
        if problem.decision_homogeneous(state):
            return 0.0
        best = inf
        for e in problem.experiments:
            parts = _partition(state, e)
            if len(parts) <= 1:
                continue
            vals = [rec(child) for _, child in parts]
            if all(v < inf for v in vals):
                best = min(best, e.cost + max(vals))
        return best

    return rec(start)


def solve_one_step_closed(problem: Problem, worlds: FrozenSet[World] | None = None):
    """CARC-like one-step baseline: one globally admissible probe must immediately
    make every outcome branch decision-homogeneous.
    """
    state = problem.worlds if worlds is None else worlds
    if problem.decision_homogeneous(state):
        return 0.0
    best = inf
    for e in problem.experiments:
        if not e.is_admissible_on(state):
            continue
        parts = _partition(state, e)
        if len(parts) > 1 and all(problem.decision_homogeneous(child) for _, child in parts):
            best = min(best, e.cost)
    return best
