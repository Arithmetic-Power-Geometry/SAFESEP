from safesep.dynamic_proof import DynamicProof, DynamicProbe, cheapest_eligible_leaving_incompatibility, drac_exists


def pair(n=20):
    worlds = frozenset([f"r{i}" for i in range(n)] + [f"w{i}" for i in range(n)])
    decisions = {w: ("R" if w.startswith("r") else "W") for w in worlds}
    q_out = {w: ("special" if w == "r0" else "rest") for w in worlds}
    resolve_out = {w: decisions[w] for w in worlds}
    q = DynamicProbe("q", 1.0, q_out, [DynamicProof("q_public", frozenset())])
    # Both resolvers are initially ineligible and informationally identical.
    # In A, q's residual contraction is enough to activate a legitimate proof.
    # In B, the matched contraction is still insufficient.
    ra = DynamicProbe("resolve", 1.0, resolve_out,
                      [DynamicProof("resolver", frozenset(), max_worlds=2*n-1)])
    rb = DynamicProbe("resolve", 1.0, resolve_out,
                      [DynamicProof("resolver", frozenset(), max_worlds=2*n-2)])
    return worlds, decisions, q, ra, rb


def test_27_cheapest_probe_is_matched_and_leaves_incompatibility():
    worlds, decisions, q, ra, rb = pair(100)
    a = cheapest_eligible_leaving_incompatibility(worlds, decisions, [q, ra])
    b = cheapest_eligible_leaving_incompatibility(worlds, decisions, [q, rb])
    assert a is not None and b is not None
    assert (a.name, a.cost) == (b.name, b.cost) == ("q", 1.0)


def test_28_branch_evolution_changes_resolvability_after_matched_root():
    worlds, decisions, q, ra, rb = pair(50)
    assert not ra.eligible(worlds, decisions)
    assert not rb.eligible(worlds, decisions)
    residual = frozenset(w for w in worlds if w != "r0")
    assert ra.eligible(residual, decisions)
    assert not rb.eligible(residual, decisions)
    assert drac_exists(worlds, decisions, [q, ra])
    assert not drac_exists(worlds, decisions, [q, rb])


def test_29_branch_evolution_scale_10000_worlds():
    worlds, decisions, q, ra, rb = pair(5000)
    assert len(worlds) == 10000
    a = cheapest_eligible_leaving_incompatibility(worlds, decisions, [q, ra])
    b = cheapest_eligible_leaving_incompatibility(worlds, decisions, [q, rb])
    assert (a.name, a.cost) == (b.name, b.cost) == ("q", 1.0)
    residual = frozenset(w for w in worlds if w != "r0")
    assert len(residual) == 9999
    assert ra.eligible(residual, decisions)
    assert not rb.eligible(residual, decisions)
