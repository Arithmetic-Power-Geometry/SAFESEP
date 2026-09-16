# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
from safesep.contingent_baseline import contingent_exists
from safesep.existence import safesep_exists
from safesep.examples import minimal_deadlock_problem, adaptive_safe_problem, already_homogeneous_problem
from safesep.families import finite_family, infinite_family


def test_contingent_planning_collision_on_core_cases():
    """Significance test: current SAFESEP existence equals an independent belief planner."""
    for p in (minimal_deadlock_problem(), adaptive_safe_problem(), already_homogeneous_problem()):
        assert contingent_exists(p) == safesep_exists(p)


def test_contingent_planning_collision_on_parameterized_family():
    """The A_n/B_n separation is reproduced by ordinary belief-space applicability."""
    for n in range(2, 31):
        a, b = finite_family(n), infinite_family(n)
        assert contingent_exists(a) == safesep_exists(a) is True
        assert contingent_exists(b) == safesep_exists(b) is False


def test_cheapest_probe_does_not_break_planning_equivalence():
    """Even the matched cheapest-probe family remains representable by contingent planning."""
    for n in (2, 5, 10, 20, 50):
        assert contingent_exists(finite_family(n))
        assert not contingent_exists(infinite_family(n))
