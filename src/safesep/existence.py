# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

"""Exact existence solver for finite explicit SAFESEP instances.

This separates the yes/no question SAFESEP-EXISTS from minimum-cost optimization.
The recursion is an AND-OR fixed point over reachable knowledge subsets.
"""
from functools import lru_cache
from typing import FrozenSet

from .model import Problem, World


def safesep_exists(problem: Problem, worlds: FrozenSet[World] | None = None) -> bool:
    start = problem.worlds if worlds is None else worlds
    visiting = set()

    @lru_cache(maxsize=None)
    def win(state: FrozenSet[World]) -> bool:
        if problem.decision_homogeneous(state):
            return True
        if state in visiting:
            return False
        visiting.add(state)
        try:
            for e in problem.experiments:
                if not e.is_admissible_on(state):
                    continue
                buckets = {}
                for w in state:
                    buckets.setdefault(e.outcome(w), set()).add(w)
                children = tuple(frozenset(v) for v in buckets.values())
                if len(children) <= 1:
                    continue
                if all(win(child) for child in children):
                    return True
            return False
        finally:
            visiting.discard(state)

    return win(start)
