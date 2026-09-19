from safesep.revocation_exact import (
    RevProbe,
    every_incompatible_pair_has_initial_separator,
    exact_revocation_resolves,
)


def test_pairwise_separability_is_not_global_resolvability_under_revocation():
    worlds = frozenset({0, 1, 2})
    decisions = {0: "A", 1: "B", 2: "C"}
    probes = (
        RevProbe(
            "p",
            outcomes=((0, 0), (1, 1), (2, 1)),
            requires=frozenset({"x"}),
            revokes=frozenset({"y"}),
        ),
        RevProbe(
            "q",
            outcomes=((0, 0), (1, 0), (2, 1)),
            requires=frozenset({"y"}),
            revokes=frozenset({"x"}),
        ),
    )
    authority = frozenset({"x", "y"})

    assert every_incompatible_pair_has_initial_separator(
        worlds, decisions, probes, authority
    )
    assert not exact_revocation_resolves(worlds, decisions, probes, authority)


def test_same_observations_resolve_without_destructive_revocation():
    worlds = frozenset({0, 1, 2})
    decisions = {0: "A", 1: "B", 2: "C"}
    probes = (
        RevProbe("p", outcomes=((0, 0), (1, 1), (2, 1)), requires=frozenset({"x"})),
        RevProbe("q", outcomes=((0, 0), (1, 0), (2, 1)), requires=frozenset({"y"})),
    )
    authority = frozenset({"x", "y"})
    assert exact_revocation_resolves(worlds, decisions, probes, authority)
