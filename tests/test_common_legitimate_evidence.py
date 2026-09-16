from math import isinf
from safesep.common_legitimate_evidence import matched_pair, cheapest_unresolved, common_legitimate_evidence, incompatible_pairs

# 91 cheapest experiment preserving incompatible worlds
def test_91_cheapest_unresolved_200():
    A,_=matched_pair(100)
    assert cheapest_unresolved(A)=={"name":"q","cost":1.0,"worst_incompatible_pairs":9900}

# 92 finite-vs-infinite common legitimate evidence after q=rest
def test_92_cle_separation():
    A,B=matched_pair(100); rest=tuple(w for w in A.worlds if w!="r0")
    assert common_legitimate_evidence(A,rest)==2.0
    assert isinf(common_legitimate_evidence(B,rest))

# 93 every residual world individually has a cost-2 legitimate resolver in B, yet no common one
def test_93_local_does_not_imply_common():
    _,B=matched_pair(20); rest=tuple(w for w in B.worlds if w!="r0")
    for w in rest:
        assert any(e.cost==2.0 and w in e.legitimate for e in B.experiments if e.name.startswith("r_"))
    assert isinf(common_legitimate_evidence(B,rest))

# 94 analytic 10k stress without materializing pair list
def test_94_10k_stress():
    A,B=matched_pair(5000); rest=tuple(w for w in A.worlds if w!="r0")
    assert incompatible_pairs(A,rest)==24995000
    assert common_legitimate_evidence(A,rest)==2.0
    assert isinf(common_legitimate_evidence(B,rest))
