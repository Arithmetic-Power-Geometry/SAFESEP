from itertools import product

from safesep.revocation_dynamic_types import dynamic_type_quotient_resolves
from safesep.revocation_exact import RevProbe, exact_revocation_resolves


def test_dynamic_retyping_branch_cycle():
    W = frozenset({0, 1, 2, 3})
    D = {0: "A", 1: "B", 2: "C", 3: "D"}
    A = frozenset({"x", "y"})
    probes = (
        RevProbe("r", ((0, 0), (1, 0), (2, 1), (3, 1))),
        RevProbe("p", ((0, 0), (1, 1), (2, 0), (3, 0)), frozenset({"x"}), revokes=frozenset({"y"})),
        RevProbe("q", ((0, 0), (1, 0), (2, 0), (3, 1)), frozenset({"y"}), revokes=frozenset({"x"})),
    )
    assert dynamic_type_quotient_resolves(W, D, probes, A) == exact_revocation_resolves(W, D, probes, A)


def test_exhaustive_dynamic_duplicate_quotient():
    W = frozenset({0, 1, 2})
    A = frozenset({"x", "y"})
    decisions = (
        {0: "A", 1: "B", 2: "C"},
        {0: "A", 1: "A", 2: "B"},
        {0: "A", 1: "B", 2: "A"},
    )
    outcomes = list(product((0, 1), repeat=3))
    reqs = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    revs = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    checked = 0
    # p and p2 are behaviorally identical initially; q is arbitrary. Dynamic
    # retyping after each branch may merge further probes.
    for D in decisions:
        for op in outcomes:
            for oq in outcomes:
                for req in reqs:
                    for rev in revs:
                        p = RevProbe("p", tuple(enumerate(op)), req, revokes=rev)
                        p2 = RevProbe("p2", tuple((w, ("L" if o == 0 else "R")) for w, o in enumerate(op)), req, revokes=rev)
                        q = RevProbe("q", tuple(enumerate(oq)))
                        probes = (p, p2, q)
                        assert dynamic_type_quotient_resolves(W, D, probes, A) == exact_revocation_resolves(W, D, probes, A)
                        checked += 1
    assert checked == 3 * 8 * 8 * 3 * 3
