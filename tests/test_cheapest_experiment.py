# Copyright (C) 2026 Mohammad Amir Khusru Akhtar

from safesep.cheapest import cheapest_experiment_leaving_incompatibility, cheapest_one_step_resolver
from safesep.examples import adaptive_safe_problem, minimal_deadlock_problem


def test_cheapest_admissible_experiment_can_leave_incompatible_worlds():
    p = adaptive_safe_problem()
    row = cheapest_experiment_leaving_incompatibility(p, require_admissible=True)
    assert row is not None
    assert row.name == "safe_metadata_probe"
    assert row.cost == 1.0
    assert row.admissible
    assert row.incompatible_branches == 1
    assert row.worst_incompatible_pairs > 0


def test_no_admissible_one_step_resolver_but_safesep_can_still_exist():
    p = adaptive_safe_problem()
    assert cheapest_one_step_resolver(p, require_admissible=True) is None


def test_deadlock_has_no_admissible_one_step_resolver():
    p = minimal_deadlock_problem()
    assert cheapest_one_step_resolver(p, require_admissible=True) is None
