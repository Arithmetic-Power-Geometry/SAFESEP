# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
from math import inf

from safesep.existence import safesep_exists
from safesep.examples import minimal_deadlock_problem, adaptive_safe_problem, already_homogeneous_problem
from safesep.irreducibility import parameterized_pair
from safesep.solver import solve_safesep


def test_existence_matches_optimization_on_core_cases():
    for p in (minimal_deadlock_problem(), adaptive_safe_problem(), already_homogeneous_problem()):
        cost, _ = solve_safesep(p)
        assert safesep_exists(p) == (cost < inf)


def test_existence_separates_parameterized_family():
    for n in range(2, 31):
        a, b = parameterized_pair(n)
        assert safesep_exists(a)
        assert not safesep_exists(b)
