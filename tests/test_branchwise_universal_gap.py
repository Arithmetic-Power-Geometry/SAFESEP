from safesep.branchwise_universal_gap import (
    GapCase, cheapest_unresolved, per_world_summary,
    branchwise_uniform_resolver, safely_resolvable_after_q_rest,
)


def test_87_cheapest_unresolved_200_worlds():
    c=GapCase(100,True)
    assert cheapest_unresolved(c)=={"name":"q","cost":1.0,"worst_incompatible_pairs":9900}


def test_88_per_world_summaries_match():
    A=GapCase(100,True); B=GapCase(100,False)
    assert per_world_summary(A)==per_world_summary(B)
    assert per_world_summary(A)["each_world_has_resolver"] is True


def test_89_branchwise_uniformity_separates():
    A=GapCase(100,True); B=GapCase(100,False)
    restA=tuple(w for w in A.worlds if A.q_outcome(w)=="rest")
    restB=tuple(w for w in B.worlds if B.q_outcome(w)=="rest")
    assert branchwise_uniform_resolver(A,restA) is True
    assert branchwise_uniform_resolver(B,restB) is False
    assert safely_resolvable_after_q_rest(A) is True
    assert safely_resolvable_after_q_rest(B) is False


def test_90_large_10000_world_structural_stress():
    A=GapCase(5000,True); B=GapCase(5000,False)
    assert cheapest_unresolved(A)["worst_incompatible_pairs"]==24995000
    assert cheapest_unresolved(B)["worst_incompatible_pairs"]==24995000
    assert per_world_summary(A)==per_world_summary(B)
    assert safely_resolvable_after_q_rest(A) is True
    assert safely_resolvable_after_q_rest(B) is False
