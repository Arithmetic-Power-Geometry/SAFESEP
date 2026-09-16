# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from .model import Experiment, Problem


def minimal_deadlock_problem():
    """Two worlds, different authorization decisions.

    A probe perfectly distinguishes them but is not admissible in one world.
    Hence ordinary distinguishability is finite while SafeSep is infinite.
    """
    worlds = frozenset({"w_read", "w_write"})
    decisions = {"w_read": "READ", "w_write": "WRITE"}
    probe = Experiment(
        name="protected_probe",
        cost=1.0,
        outcomes={"w_read": "read-case", "w_write": "write-case"},
        admissible=frozenset({"w_write"}),
    )
    return Problem(worlds, decisions, (probe,))


def adaptive_safe_problem():
    """Branchwise safe resolution where no one-step resolver exists.

    e1 is globally admissible and separates w1 from {w2,w3,w4}; that remaining
    class is still decision-critical. e2 is not globally admissible because it
    is forbidden in w1, but after e1 rules w1 out, e2 becomes admissible and
    resolves the remaining decision ambiguity.
    """
    worlds = frozenset({"w1", "w2", "w3", "w4"})
    decisions = {"w1": "READ", "w2": "READ", "w3": "WRITE", "w4": "WRITE"}
    e1 = Experiment(
        name="safe_metadata_probe",
        cost=1.0,
        outcomes={"w1": "alone", "w2": "rest", "w3": "rest", "w4": "rest"},
        admissible=worlds,
    )
    e2 = Experiment(
        name="branch_probe",
        cost=1.0,
        outcomes={"w1": "x", "w2": "read", "w3": "write", "w4": "write"},
        admissible=frozenset({"w2", "w3", "w4"}),
    )
    return Problem(worlds, decisions, (e1, e2))


def already_homogeneous_problem():
    worlds = frozenset({"a", "b", "c"})
    decisions = {w: "READ" for w in worlds}
    return Problem(worlds, decisions, ())
