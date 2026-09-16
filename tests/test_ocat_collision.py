# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under Apache-2.0.

from safesep.ocat import (
    matched_pair, cheapest_unresolved, initial_signature,
    full_state_resolvable,
)


def test_57_ocat_cheapest_unresolved_probe():
    A, B = matched_pair(100)
    for case in (A, B):
        d = cheapest_unresolved(case)
        assert d["name"] == "q"
        assert d["cost"] == 1.0
        assert d["worst_incompatible_pairs"] == 9900


def test_58_ocat_initial_state_is_matched():
    A, B = matched_pair(100)
    assert initial_signature(A) == initial_signature(B)
    assert A.initial_authority_edges == B.initial_authority_edges


def test_59_observation_conditioned_topology_separates_but_full_state_represents_it():
    A, B = matched_pair(100)
    assert A.post_q_edges("rest") != B.post_q_edges("rest")
    assert full_state_resolvable(A) is True
    assert full_state_resolvable(B) is False


def test_60_ocat_10000_world_structural_stress():
    A, B = matched_pair(5000)
    da = cheapest_unresolved(A)
    db = cheapest_unresolved(B)
    assert da == db
    assert da["worst_incompatible_pairs"] == 24_995_000
    assert initial_signature(A) == initial_signature(B)
    assert full_state_resolvable(A) is True
    assert full_state_resolvable(B) is False
