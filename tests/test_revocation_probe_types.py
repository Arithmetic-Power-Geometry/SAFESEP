from itertools import product

from safesep.revocation_exact import RevProbe, exact_revocation_resolves
from safesep.revocation_probe_types import deduplicate_probe_types


def test_duplicate_probe_type_elimination_simple():
    W = frozenset({0, 1, 2})
    D = {0: "A", 1: "B", 2: "C"}
    A = frozenset({"x"})
    p = RevProbe("p", ((0, 0), (1, 1), (2, 1)), frozenset({"x"}))
    p2 = RevProbe("p-copy", ((0, "L"), (1, "R"), (2, "R")), frozenset({"x"}))
    q = RevProbe("q", ((0, 0), (1, 0), (2, 1)), frozenset({"x"}))
    probes = (p, p2, q)
    dedup = deduplicate_probe_types(probes, W, frozenset({"x"}))
    assert len(dedup) == 2
    assert exact_revocation_resolves(W, D, probes, A) == exact_revocation_resolves(W, D, dedup, A)


def test_exhaustive_duplicate_elimination_small_slice():
    W = frozenset({0, 1, 2})
    decisions = (
        {0: "A", 1: "B", 2: "C"},
        {0: "A", 1: "A", 2: "B"},
    )
    A = frozenset({"x", "y"})
    outcomes = list(product((0, 1), repeat=3))
    reqs = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    revs = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    checked = 0
    # Build p and an exact behavioral duplicate p2, plus arbitrary q.
    for D in decisions:
        for op in outcomes:
            for oq in outcomes:
                for req in reqs:
                    for rev in revs:
                        p = RevProbe("p", tuple(enumerate(op)), req, revokes=rev)
                        p2 = RevProbe("p2", tuple((w, ("a" if o == 0 else "b")) for w, o in enumerate(op)), req, revokes=rev)
                        q = RevProbe("q", tuple(enumerate(oq)))
                        probes = (p, p2, q)
                        dedup = deduplicate_probe_types(probes, W, frozenset({"x", "y"}))
                        assert exact_revocation_resolves(W, D, probes, A) == exact_revocation_resolves(W, D, dedup, A)
                        checked += 1
    assert checked == 2 * 8 * 8 * 3 * 3
