"""Tests 95-98: unbounded authorization-legitimacy premium."""
from safesep.unbounded_legitimacy_premium import (
    PremiumFamily, cheapest_unresolved, unconstrained_resolution_cost,
    authorization_safe_resolution_cost, legitimacy_premium, token_requirements,
    theorem_holds,
)


def test_95_cheapest_unresolved_200_worlds():
    c = PremiumFamily(100)
    assert cheapest_unresolved(c) == {
        "experiment": "q", "cost": 1.0, "worst_incompatible_pairs": 9900}


def test_96_exact_linear_premium_family():
    for n in range(2, 129):
        c = PremiumFamily(n)
        assert unconstrained_resolution_cost(c) == 1.0
        assert authorization_safe_resolution_cost(c) == n + 1
        assert legitimacy_premium(c) == n
        assert theorem_holds(c)


def test_97_premium_is_unbounded_over_family():
    vals = [legitimacy_premium(PremiumFamily(n)) for n in (2, 4, 8, 16, 32, 64, 128, 256)]
    assert vals == [2, 4, 8, 16, 32, 64, 128, 256]
    assert all(b > a for a, b in zip(vals, vals[1:]))


def test_98_10000_world_structural_stress():
    c = PremiumFamily(5000)
    d = cheapest_unresolved(c)
    assert d["experiment"] == "q" and d["cost"] == 1.0
    assert d["worst_incompatible_pairs"] == 24_995_000
    assert len(token_requirements(c)) == 5000
    assert unconstrained_resolution_cost(c) == 1.0
    assert authorization_safe_resolution_cost(c) == 5001.0
    assert legitimacy_premium(c) == 5000.0
