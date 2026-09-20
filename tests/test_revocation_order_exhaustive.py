from itertools import product

from safesep.revocation_exact import RevProbe, exact_revocation_resolves
from safesep.revocation_order import has_acyclic_separator_cover


def test_ordered_cover_accepts_safe_one_way_interference():
    W = frozenset({0, 1, 2})
    D = {0: "A", 1: "B", 2: "C"}
    A = frozenset({"x", "y"})
    probes = (
        RevProbe("p", ((0, 0), (1, 1), (2, 1)), frozenset({"x"}), revokes=frozenset({"y"})),
        RevProbe("q", ((0, 0), (1, 0), (2, 1)), frozenset({"y"})),
    )
    assert has_acyclic_separator_cover(W, D, probes, A)
    assert exact_revocation_resolves(W, D, probes, A)


def test_ordered_cover_rejects_v3_cycle():
    W = frozenset({0, 1, 2})
    D = {0: "A", 1: "B", 2: "C"}
    A = frozenset({"x", "y"})
    probes = (
        RevProbe("p", ((0, 0), (1, 1), (2, 1)), frozenset({"x"}), revokes=frozenset({"y"})),
        RevProbe("q", ((0, 0), (1, 0), (2, 1)), frozenset({"y"}), revokes=frozenset({"x"})),
    )
    assert not has_acyclic_separator_cover(W, D, probes, A)


def test_exhaustive_three_world_two_probe_acyclic_certificate_is_sound():
    W = frozenset({0, 1, 2})
    D = {0: "A", 1: "B", 2: "C"}
    A = frozenset({"x", "y"})
    outcome_maps = list(product((0, 1), repeat=3))
    requirements = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    revocations = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    types = [(o, req, rev) for o in outcome_maps for req in requirements for rev in revocations]
    checked = certified = 0
    for a in types:
        for b in types:
            probes = (
                RevProbe("p", tuple(enumerate(a[0])), a[1], revokes=a[2]),
                RevProbe("q", tuple(enumerate(b[0])), b[1], revokes=b[2]),
            )
            checked += 1
            if has_acyclic_separator_cover(W, D, probes, A):
                certified += 1
                assert exact_revocation_resolves(W, D, probes, A)
    assert checked == 5184
    assert certified > 0
