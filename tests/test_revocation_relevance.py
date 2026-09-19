from itertools import product

from safesep.revocation_exact import RevProbe, exact_revocation_resolves
from safesep.revocation_relevance import prune_authority, relevance_pruned_resolves


def test_irrelevant_authority_is_erased():
    probes = (
        RevProbe("p", ((0, 0), (1, 1)), frozenset({"x"})),
        RevProbe("q", ((0, 0), (1, 1)), frozenset({"y"})),
    )
    assert prune_authority(frozenset({"x", "y", "dead"}), probes, (0, 1)) == frozenset({"x", "y"})
    assert prune_authority(frozenset({"x", "y", "dead"}), probes, (1,)) == frozenset({"y"})


def test_exhaustive_relevance_pruning_matches_exact_solver():
    W = frozenset({0, 1, 2})
    A = frozenset({"x", "y", "dead"})
    decisions = (
        {0: "A", 1: "B", 2: "C"},
        {0: "A", 1: "A", 2: "B"},
        {0: "A", 1: "B", 2: "A"},
        {0: "B", 1: "A", 2: "A"},
    )
    outcomes = list(product((0, 1), repeat=3))
    reqs = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    grants = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    revs = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    checked = 0
    # Complete observation pair slice, with all req/grant/revoke choices on p.
    for D in decisions:
        for oa in outcomes:
            for ob in outcomes:
                for req in reqs:
                    for grant in grants:
                        for rev in revs:
                            probes = (
                                RevProbe("p", tuple(enumerate(oa)), req, grant, rev),
                                RevProbe("q", tuple(enumerate(ob))),
                            )
                            assert relevance_pruned_resolves(W, D, probes, A) == exact_revocation_resolves(W, D, probes, A)
                            checked += 1
    assert checked == 4 * 8 * 8 * 3 * 3 * 3
