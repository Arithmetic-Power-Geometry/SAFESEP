from safesep.authority_closure_certificate import *

def test_163_homogeneous_not_obstructed():
    C=("w0",); d={"w0":"R"}; assert not closure_obstructed(C,d,[])

def test_164_blocked_root_has_q_separator():
    W,d,A=family(10,False); assert not closure_obstructed(W,d,A)

def test_165_open_closure_grants_alpha():
    W,d,A=family(10,True); assert "alpha" in authority_closure(W,A)

def test_166_blocked_closure_no_alpha():
    W,d,A=family(10,False); assert "alpha" not in authority_closure(W,A)

def test_167_open_unlocks_k():
    W,d,A=family(10,True); assert "k" in available_separators(W,d,A)

def test_168_blocked_k_stays_locked():
    W,d,A=family(10,False); assert "k" not in available_separators(W,d,A)

def test_169_after_q_rest_blocked_is_obstructed():
    W,d,A=family(100,False); rest=tuple(w for w in W if w!="w0")
    assert closure_obstructed(rest,d,A)

def test_170_after_q_rest_open_not_obstructed():
    W,d,A=family(100,True); rest=tuple(w for w in W if w!="w0")
    assert not closure_obstructed(rest,d,A)

def test_171_cheapest_unresolved_200():
    W,d,A=family(100,False); assert cheapest_unresolved(W,d,A)=={"name":"q","cost":1.0,"worst_incompatible_pairs":9900}

def test_172_chain_closure():
    W,d,A=family(4,False); same=tuple("same" for _ in W)
    a=Action("a",1,same,grants=frozenset({"x"})); b=Action("b",1,same,frozenset({"x"}),frozenset({"alpha"}))
    assert "alpha" in authority_closure(W,A+(a,b))

def test_173_unseeded_cycle_no_progress():
    W,d,A=family(4,False); same=tuple("same" for _ in W)
    a=Action("a",1,same,frozenset({"y"}),frozenset({"x"})); b=Action("b",1,same,frozenset({"x"}),frozenset({"y"}))
    assert authority_closure(W,A+(a,b))==frozenset()

def test_174_seeded_cycle_progress():
    W,d,A=family(4,False); same=tuple("same" for _ in W)
    a=Action("a",1,same,frozenset({"y"}),frozenset({"x"})); b=Action("b",1,same,frozenset({"x"}),frozenset({"y"}))
    assert {"x","y"} <= authority_closure(W,A+(a,b),frozenset({"x"}))

def test_175_action_order_invariance():
    W,d,A=family(20,True); assert authority_closure(W,A)==authority_closure(W,tuple(reversed(A)))

def test_176_world_order_invariance():
    W,d,A=family(20,True); assert available_separators(W,d,A)==available_separators(tuple(reversed(W)),d,A)

def test_177_scale_sweep():
    for n in (2,4,8,16,32,64,128):
        W,d,A=family(n,False); rest=tuple(w for w in W if w!="w0"); assert closure_obstructed(rest,d,A)

def test_178_large_10000_diagnostic():
    W,d,A=family(5000,False); assert cheapest_unresolved(W,d,A)=={"name":"q","cost":1.0,"worst_incompatible_pairs":24995000}
