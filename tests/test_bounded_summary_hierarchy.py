from safesep.bounded_summary_hierarchy import (
    all_summaries_match_through_k,
    cheapest_unresolved,
    globally_resolvable,
    local_summary,
    matched_pair,
)


def test_81_cheapest_unresolved_preserved():
    assert cheapest_unresolved(100) == {
        "name": "q", "cost": 1.0, "worst_incompatible_pairs": 9900
    }


def test_82_bounded_summaries_match_for_every_tested_k():
    for k in range(1, 65):
        a, b = matched_pair(k)
        assert all_summaries_match_through_k(a, b)
        for j in range(1, k + 1):
            assert local_summary(a, j) == local_summary(b, j)


def test_83_global_resolution_separates_despite_k_local_match():
    for k in range(1, 65):
        a, b = matched_pair(k)
        assert globally_resolvable(a) is True
        assert globally_resolvable(b) is False
        assert local_summary(a, k + 1) != local_summary(b, k + 1)


def test_84_10000_world_structural_stress():
    assert cheapest_unresolved(5000) == {
        "name": "q", "cost": 1.0, "worst_incompatible_pairs": 24995000
    }
    a, b = matched_pair(128)
    assert all_summaries_match_through_k(a, b)
    assert globally_resolvable(a) and not globally_resolvable(b)
