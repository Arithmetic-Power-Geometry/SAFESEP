from safesep.recursive_obstruction import *
from safesep.dynamic_pair_flow import family, Probe, decisions, analytic_large


def test_147_homogeneous_terminal_resolves():
    C=("w0","w1"); d={"w0":"R","w1":"R"}
    assert recursive_resolvable(C,d,())


def test_148_critical_no_action_obstructed():
    C=("w0","w1"); d={"w0":"R","w1":"W"}
    assert recursive_obstruction(C,d,())


def test_149_open_token_flow_resolves():
    C,d,p=family(8,True)
    assert recursive_resolvable(C,d,p)


def test_150_blocked_token_flow_obstructed():
    C,d,p=family(8,False)
    assert recursive_obstruction(C,d,p)


def test_151_token_only_progress_is_not_dropped():
    C,d,p=family(4,True)
    fetch=[e for e in p if e.name=="fetch"][0]
    ch=progress_children(fetch,C,frozenset())
    assert len(ch)==1 and ch[0][0]==tuple(sorted(C)) and "alpha" in ch[0][1]


def test_152_true_noop_is_dropped():
    C,d,p=family(4,False)
    fetch=[e for e in p if e.name=="fetch"][0]
    assert progress_children(fetch,C,frozenset())==()


def test_153_cheapest_unresolved_dynamic_family():
    C,d,p=family(100,True)
    assert cheapest_unresolved_exact(C,d,p)=={"name":"q","cost":1.0,"worst_incompatible_pairs":9900}


def test_154_parameterized_open_sweep():
    for n in range(2,33):
        C,d,p=family(n,True)
        assert recursive_resolvable(C,d,p)


def test_155_parameterized_blocked_sweep():
    for n in range(2,33):
        C,d,p=family(n,False)
        assert recursive_obstruction(C,d,p)


def test_156_perfect_resolver_without_token():
    n=12; C=tuple(f"w{i}" for i in range(2*n)); d=decisions(n)
    out=tuple("R" if i<n else "W" for i in range(2*n))
    k=Probe("k",2.0,out)
    assert recursive_resolvable(C,d,(k,))


def test_157_unavailable_perfect_resolver_obstructs():
    n=12; C=tuple(f"w{i}" for i in range(2*n)); d=decisions(n)
    out=tuple("R" if i<n else "W" for i in range(2*n))
    k=Probe("k",2.0,out,frozenset({"alpha"}))
    assert recursive_obstruction(C,d,(k,))


def test_158_action_order_invariance():
    C,d,p=family(10,True)
    assert recursive_resolvable(C,d,p)==recursive_resolvable(C,d,tuple(reversed(p)))


def test_159_world_order_invariance():
    C,d,p=family(10,True)
    assert recursive_resolvable(C,d,p)==recursive_resolvable(tuple(reversed(C)),d,p)


def test_160_initial_token_restores_resolution():
    C,d,p=family(10,False)
    assert recursive_resolvable(C,d,p,frozenset({"alpha"}))


def test_161_10000_world_cheapest_q_analytic_and_direct():
    n=5000; C,d,p=family(n,True)
    z=cheapest_unresolved_exact(C,d,p)
    assert z=={"name":"q","cost":1.0,"worst_incompatible_pairs":24995000}
    assert analytic_large(n)["q_worst_pairs"]==24995000


def test_162_large_structural_open_blocked_authority_difference():
    n=5000
    Co,do,po=family(n,True); Cb,db,pb=family(n,False)
    fo=[e for e in po if e.name=="fetch"][0]
    fb=[e for e in pb if e.name=="fetch"][0]
    assert "alpha" in progress_children(fo,Co,frozenset())[0][1]
    assert progress_children(fb,Cb,frozenset())==()
