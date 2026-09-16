"""Independent belief-space contingent-planning baseline.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

This module intentionally does not call the SAFESEP solver.  It treats each
experiment as a sensing action, its world-wise admissibility set as the action
precondition, and decision-homogeneity as the goal predicate.  It is used to
test whether the current finite SAFESEP model is extensionally different from
standard strong contingent planning in belief space.
"""
from functools import lru_cache


def contingent_exists(problem) -> bool:
    """Return whether a strong sensing policy reaches a decision-homogeneous belief.

    An action is applicable at belief C iff its precondition/admissibility set
    contains every state in C. Every nonempty observation successor must win.
    Only strict belief contractions are used, matching informative SAFESEP probes.
    """
    root = frozenset(problem.worlds)

    @lru_cache(maxsize=None)
    def win(C: frozenset[str]) -> bool:
        if problem.decision_homogeneous(C):
            return True
        for e in problem.experiments:
            if not e.is_admissible_on(C):
                continue
            children = []
            for o in {e.outcome(w) for w in C}:
                child = frozenset(w for w in C if e.outcome(w) == o)
                if child and child != C:
                    children.append(child)
            # A useful sensing action must split the current belief, and all
            # possible observation branches must be winning.
            if len(children) >= 2 and all(win(child) for child in children):
                return True
        return False

    return win(root)
