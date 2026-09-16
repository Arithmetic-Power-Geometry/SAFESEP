# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

"""Diagnostics for the cheapest experiment relative to decision incompatibility."""

from dataclasses import dataclass
from typing import FrozenSet, Optional

from .model import Problem, Experiment, World


@dataclass(frozen=True)
class ExperimentDiagnostic:
    name: str
    cost: float
    admissible: bool
    resolves_decision: bool
    incompatible_branches: int
    worst_incompatible_pairs: int


def _partition(worlds: FrozenSet[World], e: Experiment):
    buckets = {}
    for w in worlds:
        buckets.setdefault(e.outcome(w), set()).add(w)
    return tuple(frozenset(ws) for ws in buckets.values())


def incompatible_pairs(problem: Problem, worlds: FrozenSet[World]) -> int:
    ws = tuple(worlds)
    return sum(
        1
        for i in range(len(ws))
        for j in range(i + 1, len(ws))
        if problem.decisions[ws[i]] != problem.decisions[ws[j]]
    )


def diagnose_experiment(problem: Problem, e: Experiment, worlds: FrozenSet[World] | None = None):
    state = problem.worlds if worlds is None else worlds
    parts = _partition(state, e)
    bad = [child for child in parts if not problem.decision_homogeneous(child)]
    return ExperimentDiagnostic(
        name=e.name,
        cost=e.cost,
        admissible=e.is_admissible_on(state),
        resolves_decision=(len(parts) > 1 and not bad),
        incompatible_branches=len(bad),
        worst_incompatible_pairs=max((incompatible_pairs(problem, child) for child in bad), default=0),
    )


def cheapest_experiment_leaving_incompatibility(problem: Problem, worlds: FrozenSet[World] | None = None, *, require_admissible: bool = False) -> Optional[ExperimentDiagnostic]:
    """Cheapest informative experiment that still leaves a decision-incompatible branch.

    This directly operationalises the diagnostic question: which cheapest experiment,
    given current knowledge, fails to resolve all mutually incompatible possible worlds?
    It is deliberately a diagnostic baseline, not the SafeSep objective.
    """
    state = problem.worlds if worlds is None else worlds
    rows = []
    for e in problem.experiments:
        d = diagnose_experiment(problem, e, state)
        if require_admissible and not d.admissible:
            continue
        if d.incompatible_branches > 0 and len(_partition(state, e)) > 1:
            rows.append(d)
    return min(rows, key=lambda x: (x.cost, x.worst_incompatible_pairs, x.name), default=None)


def cheapest_one_step_resolver(problem: Problem, worlds: FrozenSet[World] | None = None, *, require_admissible: bool = True):
    """Cheapest single experiment whose every branch is decision-homogeneous."""
    state = problem.worlds if worlds is None else worlds
    rows = []
    for e in problem.experiments:
        d = diagnose_experiment(problem, e, state)
        if require_admissible and not d.admissible:
            continue
        if d.resolves_decision:
            rows.append(d)
    return min(rows, key=lambda x: (x.cost, x.name), default=None)
