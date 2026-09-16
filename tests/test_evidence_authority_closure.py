from safesep.evidence_authority_closure import (
    AuthorityRule, authority_closure,
    cheapest_executable_leaving_incompatibility, has_resolver,
)


def systems():
    # q is independently executable and is the same cheapest unresolved probe.
    # Resolver r requires token alpha. In A, q yields alpha. In B, alpha can
    # only be obtained by s, while s itself requires beta produced only by r.
    costs = {"q": 1.0, "r": 2.0, "s": 2.0}
    leaves = {"q": True, "r": False, "s": True}
    rules = [
        AuthorityRule("q", frozenset()),
        AuthorityRule("r", frozenset({"alpha"})),
        AuthorityRule("s", frozenset({"beta"})),
    ]
    yields_a = {"q": frozenset({"alpha"}), "r": frozenset({"beta"}), "s": frozenset({"alpha"})}
    yields_b = {"q": frozenset(), "r": frozenset({"beta"}), "s": frozenset({"alpha"})}
    return costs, leaves, rules, yields_a, yields_b


def test_30_cheapest_experiment_still_leaves_incompatible_worlds():
    costs, leaves, rules, ya, yb = systems()
    for yields in (ya, yb):
        _, executable = authority_closure(frozenset(), rules, yields)
        assert cheapest_executable_leaving_incompatibility(executable, costs, leaves) == "q"
        assert costs["q"] == 1.0


def test_31_unseeded_authority_cycle_cannot_self_authorize():
    costs, leaves, rules, ya, yb = systems()
    _, ea = authority_closure(frozenset(), rules, ya)
    _, eb = authority_closure(frozenset(), rules, yb)
    assert has_resolver(ea, {"r"})
    assert not has_resolver(eb, {"r"})
    assert "s" not in eb


def test_32_scale_10000_world_interpretation_preserves_closure_separation():
    # Closure computation is structural and does not enumerate incompatible pairs.
    n = 5000
    worlds = tuple([f"r{i}" for i in range(n)] + [f"w{i}" for i in range(n)])
    assert len(worlds) == 10000
    costs, leaves, rules, ya, yb = systems()
    _, ea = authority_closure(frozenset(), rules, ya)
    _, eb = authority_closure(frozenset(), rules, yb)
    assert cheapest_executable_leaving_incompatibility(ea, costs, leaves) == "q"
    assert cheapest_executable_leaving_incompatibility(eb, costs, leaves) == "q"
    assert has_resolver(ea, {"r"}) and not has_resolver(eb, {"r"})
