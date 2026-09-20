from itertools import product

from safesep.revocation_exact import RevProbe, exact_revocation_resolves
from safesep.revocation_obligations import obligation_quotient_resolves


def test_branch_cycle_example_agrees_under_obligation_quotient():
    W = frozenset({0, 1, 2, 3})
    D = {0: "A", 1: "B", 2: "C", 3: "D"}
    A = frozenset({"x", "y"})
    probes = (
        RevProbe("r", ((0, 0), (1, 0), (2, 1), (3, 1))),
        RevProbe("p", ((0, 0), (1, 1), (2, 0), (3, 0)), frozenset({"x"}), revokes=frozenset({"y"})),
        RevProbe("q", ((0, 0), (1, 0), (2, 0), (3, 1)), frozenset({"y"}), revokes=frozenset({"x"})),
    )
    assert exact_revocation_resolves(W, D, probes, A)
    assert obligation_quotient_resolves(W, D, probes, A)


def test_exhaustive_three_world_two_probe_quotient_exactness():
    W = frozenset({0, 1, 2})
    A = frozenset({"x", "y"})
    # Include repeated decision labels: quotient must preserve decision sufficiency,
    # not exact world identification.
    decision_maps = (
        {0: "A", 1: "B", 2: "C"},
        {0: "A", 1: "A", 2: "B"},
        {0: "A", 1: "B", 2: "A"},
        {0: "B", 1: "A", 2: "A"},
    )
    outcomes = list(product((0, 1), repeat=3))
    reqs = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    revs = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    # Reduced complete slice: all observation pairs and all single-token/empty
    # requirements/revocations for the first probe; second has empty requirement.
    checked = 0
    for D in decision_maps:
        for oa in outcomes:
            for ob in outcomes:
                for req in reqs:
                    for rev in revs:
                        probes = (
                            RevProbe("p", tuple(enumerate(oa)), req, revokes=rev),
                            RevProbe("q", tuple(enumerate(ob))),
                        )
                        assert obligation_quotient_resolves(W, D, probes, A) == exact_revocation_resolves(W, D, probes, A)
                        checked += 1
    assert checked == 4 * 8 * 8 * 3 * 3
