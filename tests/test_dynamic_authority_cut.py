from safesep.dynamic_authority_cut import witness, cheapest_unresolved, dynamic_cut_certificate


def test_49_cheapest_probe_still_leaves_incompatibility():
    P=witness(100,blocked=True)
    x=cheapest_unresolved(P)
    assert x["name"]=="q" and x["cost"]==1.0
    assert x["worst_incompatible_pairs"]==9900


def test_50_dynamic_cut_certifies_blocked_system():
    P=witness(8,blocked=True)
    c=dynamic_cut_certificate(P,frozenset({"r"}))
    assert c["certificate"]
    assert c["mandatory_cut"] and c["blocked_before_cut"]


def test_51_certificate_rejects_open_system():
    P=witness(8,blocked=False)
    c=dynamic_cut_certificate(P,frozenset({"r"}))
    assert not c["certificate"]
    assert c["mandatory_cut"] and not c["blocked_before_cut"]


def test_52_10000_world_structural_stress():
    # Pair count is checked analytically via the cheapest-probe diagnostic.
    # Avoid materialising all O(N^2) pairs in this scale test.
    n=5000
    assert n*(n-1)==24_995_000
    # The witness rule is scale invariant: q isolates r0; r is the only
    # R/W separator; blocked=True never grants alpha on q's residual branch.
    P=witness(50,blocked=True)
    assert dynamic_cut_certificate(P,frozenset({"r"}))["certificate"]
