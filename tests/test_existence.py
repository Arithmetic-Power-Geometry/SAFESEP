# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
from math import inf

from safesep.existence import safesep_exists
from safesep.examples import minimal_deadlock_problem, adaptive_safe_problem, already_homogeneous_problem
from safesep.families import finite_family, infinite_family
from safesep.solver import solve_safesep


def test_existence_matches_optimization_on_core_cases():
    for p in (minimal_deadlock_problem(), adaptive_safe_problem(), already_homogeneous_problem()):
        cost, _ = solve_safesep(p)
        assert safesep_exists(p) == (cost < inf)


def test_existence_separates_parameterized_family():
    for n in range(2, 31):
        assert safesep_exists(finite_family(n))
        assert not safesep_exists(infinite_family(n))
