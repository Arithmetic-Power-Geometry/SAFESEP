# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from math import inf

from safesep.examples import minimal_deadlock_problem, adaptive_safe_problem, already_homogeneous_problem
from safesep.solver import solve_safesep, solve_unconstrained, solve_one_step_closed


def test_minimal_deadlock_separates_information_from_safe_resolution():
    p = minimal_deadlock_problem()
    assert solve_unconstrained(p) == 1.0
    safe_cost, tree = solve_safesep(p)
    assert safe_cost == inf
    assert tree is None


def test_adaptive_branchwise_resolution_beats_one_step_closed():
    p = adaptive_safe_problem()
    assert solve_one_step_closed(p) == inf
    safe_cost, tree = solve_safesep(p)
    assert safe_cost == 2.0
    assert tree is not None
    assert tree.experiment == "safe_metadata_probe"


def test_homogeneous_class_needs_no_identification():
    p = already_homogeneous_problem()
    assert solve_unconstrained(p) == 0.0
    safe_cost, tree = solve_safesep(p)
    assert safe_cost == 0.0
    assert tree is not None
    assert tree.experiment is None
