from safesep.self_referential_legitimacy import (
    SRLCase, cheapest_unresolved, dependency_edges, grounded, safely_resolvable
)


def test_65_cheapest_experiment_leaves_incompatible_worlds():
    x = cheapest_unresolved(SRLCase(100, False))
    assert x == {"name":"q", "cost":1.0, "worst_incompatible_pairs":9900}


def test_66_unseeded_self_reference_is_ungrounded():
    c = SRLCase(100, False)
    assert dependency_edges(c) == frozenset({("policy_alpha","evidence_E"),("evidence_E","policy_alpha")})
    assert grounded(c) == frozenset({"q"})
    assert not safely_resolvable(c)


def test_67_external_legitimacy_seed_breaks_cycle():
    c = SRLCase(100, True)
    assert {"policy_alpha","evidence_E"}.issubset(grounded(c))
    assert safely_resolvable(c)


def test_68_10000_world_structural_stress():
    c = SRLCase(5000, False)
    x = cheapest_unresolved(c)
    assert x["name"] == "q" and x["cost"] == 1.0
    assert x["worst_incompatible_pairs"] == 24_995_000
    assert not safely_resolvable(c)
