from itertools import product

from safesep.revocation_certificate import has_static_noninterfering_cover
from safesep.revocation_exact import RevProbe, exact_revocation_resolves


def test_v3_destructive_example_has_no_noninterfering_cover():
    W = frozenset({0, 1, 2})
    D = {0: "A", 1: "B", 2: "C"}
    probes = (
        RevProbe("p", ((0, 0), (1, 1), (2, 1)), frozenset({"x"}), revokes=frozenset({"y"})),
        RevProbe("q", ((0, 0), (1, 0), (2, 1)), frozenset({"y"}), revokes=frozenset({"x"})),
    )
    assert not has_static_noninterfering_cover(W, D, probes, frozenset({"x", "y"}))


def test_exhaustive_three_world_two_probe_certificate_is_sound():
    # Complete deterministic binary observations; requirements x/y/none;
    # revocations none/x/y. We test the implication certificate => exact.
    W = frozenset({0, 1, 2})
    D = {0: "A", 1: "B", 2: "C"}
    A = frozenset({"x", "y"})
    outcome_maps = list(product((0, 1), repeat=3))
    requirements = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    revocations = (frozenset(), frozenset({"x"}), frozenset({"y"}))
    types = [
        (o, req, rev)
        for o in outcome_maps for req in requirements for rev in revocations
    ]
    checked = certified = 0
    for a in types:
        for b in types:
            probes = (
                RevProbe("p", tuple(enumerate(a[0])), a[1], revokes=a[2]),
                RevProbe("q", tuple(enumerate(b[0])), b[1], revokes=b[2]),
            )
            checked += 1
            if has_static_noninterfering_cover(W, D, probes, A):
                certified += 1
                assert exact_revocation_resolves(W, D, probes, A)
    assert checked == len(types) ** 2
    assert certified > 0
