from math import inf

from safesep.authority_premium import (
    make_case, cheapest_experiment_leaving_incompatibility,
    unconstrained_resolution_cost, authorization_safe_resolution_cost,
    authority_premium,
)


def test_41_cheapest_experiment_still_leaves_incompatible_worlds():
    c = make_case(100, True)
    d = cheapest_experiment_leaving_incompatibility(c)
    assert d == {"name": "q", "cost": 1.0, "unresolved_branches": 1,
                 "worst_incompatible_pairs": 9900}


def test_42_finite_authority_premium_when_safe_path_exists():
    c = make_case(100, True)
    assert unconstrained_resolution_cost(c) == 1.0
    assert authorization_safe_resolution_cost(c) == 2.0
    assert authority_premium(c) == 1.0


def test_43_infinite_authority_premium_under_authority_obstruction():
    c = make_case(100, False)
    assert unconstrained_resolution_cost(c) == 1.0
    assert authorization_safe_resolution_cost(c) == inf
    assert authority_premium(c) == inf


def test_44_10000_world_authority_premium_stress():
    good = make_case(5000, True)
    blocked = make_case(5000, False)
    dg = cheapest_experiment_leaving_incompatibility(good)
    db = cheapest_experiment_leaving_incompatibility(blocked)
    assert dg == db
    assert dg["worst_incompatible_pairs"] == 24_995_000
    assert authority_premium(good) == 1.0
    assert authority_premium(blocked) == inf
