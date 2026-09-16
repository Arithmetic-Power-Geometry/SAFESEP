from safesep.legitimate_pair_cut import (
    cheapest_legitimate_unresolved, incompatible_pairs,
    legitimate_pair_cover, matched_pair_cut_family,
    pair_cut_obstruction, separated_pairs, uncovered_legitimate_pairs,
)


def test_45_cheapest_legitimate_probe_still_q_cost_one_and_unresolved():
    A, B = matched_pair_cut_family(100)
    # In B q is the cheapest legitimate unresolved probe. In A the resolver
    # exists at equal cost, so q remains a cheapest unresolved probe by name tie.
    qb = cheapest_legitimate_unresolved(B)
    assert qb["name"] == "q" and qb["cost"] == 1.0
    assert qb["unresolved_branches"] == 1
    assert qb["worst_incompatible_pairs"] == 9900


def test_46_uncovered_incompatible_pair_is_impossibility_certificate():
    A, B = matched_pair_cut_family(20)
    assert not pair_cut_obstruction(A)
    assert pair_cut_obstruction(B)
    assert len(uncovered_legitimate_pairs(A)) == 0
    assert len(uncovered_legitimate_pairs(B)) > 0


def test_47_authorization_changes_usable_pair_cover_not_information_map():
    A, B = matched_pair_cut_family(30)
    assert incompatible_pairs(A) == incompatible_pairs(B)
    for ea, eb in zip(A.experiments, B.experiments):
        assert ea.name == eb.name
        assert ea.cost == eb.cost
        assert dict(ea.outcomes) == dict(eb.outcomes)
        assert separated_pairs(A, ea) == separated_pairs(B, eb)
    assert legitimate_pair_cover(A) != legitimate_pair_cover(B)


def test_48_10000_world_structural_pair_cut_without_materializing_all_pairs():
    # 25M pairs are counted analytically; avoid allocating them in CI.
    n = 5000
    A, B = matched_pair_cut_family(n)
    qb = cheapest_legitimate_unresolved(B)
    assert len(A.worlds) == len(B.worlds) == 10000
    assert qb["name"] == "q" and qb["cost"] == 1.0
    assert qb["worst_incompatible_pairs"] == n * (n - 1) == 24995000
    # Resolver is informationally identical but legitimate only in A.
    assert A.experiments[1].outcomes == B.experiments[1].outcomes
    assert A.experiments[1].legitimate is True
    assert B.experiments[1].legitimate is False
