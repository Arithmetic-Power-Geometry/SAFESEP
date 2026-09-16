from math import isinf
from safesep.matched_coupling_premium import (
    matched_pair, cheapest_unresolved, every_residual_world_has_unit_witness,
    common_unit_resolver, safe_cost_after_q,
)


def test_99_cheapest_unresolved_matched_cost_family():
    A, B = matched_pair(100)
    assert cheapest_unresolved(A) == {"experiment": "q", "cost": 1, "worst_incompatible_pairs": 9900}
    assert cheapest_unresolved(B) == cheapest_unresolved(A)


def test_100_matched_cost_and_local_witness_summaries():
    A, B = matched_pair(100)
    assert A.structural_signature() == B.structural_signature()
    assert every_residual_world_has_unit_witness(A)
    assert every_residual_world_has_unit_witness(B)


def test_101_branchwise_coupling_separates_safe_completion():
    A, B = matched_pair(100)
    assert common_unit_resolver(A)
    assert not common_unit_resolver(B)
    assert safe_cost_after_q(A) == 1.0
    assert isinf(safe_cost_after_q(B))


def test_102_10000_world_matched_cost_stress():
    A, B = matched_pair(5000)
    assert A.structural_signature() == B.structural_signature()
    assert cheapest_unresolved(A)["cost"] == 1
    assert cheapest_unresolved(A)["worst_incompatible_pairs"] == 24_995_000
    assert every_residual_world_has_unit_witness(B)
    assert common_unit_resolver(A)
    assert not common_unit_resolver(B)
