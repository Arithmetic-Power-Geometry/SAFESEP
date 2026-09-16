from safesep.rule_validity_coupling import matched_pair, cheapest_unresolved, branchwise_resolver_legitimate


def test_69_cheapest_unresolved_rule_validity_attack():
    A, B = matched_pair(100)
    for case in (A, B):
        d = cheapest_unresolved(case)
        assert d["experiment"] == "q"
        assert d["cost"] == 1
        assert d["worst_incompatible_pairs"] == 9900


def test_70_matched_coarse_rule_validity_summaries():
    A, B = matched_pair(100)
    assert A.structural_signature() == B.structural_signature()
    assert sum(A.rule_valid(w) for w in A.worlds) == 100
    assert sum(B.rule_valid(w) for w in B.worlds) == 100


def test_71_naive_world_rule_alignment_does_not_yield_safe_separation():
    A, B = matched_pair(20)
    # Critical negative result: under branchwise universal legitimacy, neither
    # coarse alignment is enough. This prevents a false breakthrough claim.
    assert not branchwise_resolver_legitimate(A)
    assert not branchwise_resolver_legitimate(B)


def test_72_10000_world_structural_stress():
    A, B = matched_pair(5000)
    assert A.structural_signature() == B.structural_signature()
    assert cheapest_unresolved(A)["worst_incompatible_pairs"] == 24_995_000
    assert cheapest_unresolved(B)["worst_incompatible_pairs"] == 24_995_000
