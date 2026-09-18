from safesep.dynamic_pair_flow import Probe, family, cheapest_unresolved
from safesep.closure_exactness import exact_resolves
from safesep.branch_relative_closure import branch_constant, branch_authority_closure, brac_resolves


def W4():
    W=tuple(f"w{i}" for i in range(4))
    d={"w0":"R","w1":"R","w2":"W","w3":"W"}
    return W,d


def test_251_globally_informative_can_be_branch_constant():
    W,d=W4(); e=Probe("g",1,("a","a","b","b"),grants=frozenset({"x"}))
    assert not branch_constant(e,W)
    assert branch_constant(e,("w0","w1"))


def test_252_branch_constant_grant_enters_closure():
    W,d=W4(); e=Probe("g",1,("a","a","b","b"),grants=frozenset({"x"}))
    assert "x" in branch_authority_closure(("w0","w1"),frozenset(),(e,))


def test_253_branch_relative_chain_repairs_informative_grant_case():
    W,d=W4()
    split=Probe("split",1,("L","L","R","R"))
    grant=Probe("grant",1,("u","u","v","v"),grants=frozenset({"x"}))
    k=Probe("k",1,("R","R","W","W"),frozenset({"x"}))
    p=(split,grant,k)
    assert brac_resolves(W,d,p)==exact_resolves(W,d,p)==True


def test_254_no_authority_path_blocks_both():
    W,d=W4(); k=Probe("k",1,("R","R","W","W"),frozenset({"x"}))
    assert brac_resolves(W,d,(k,))==exact_resolves(W,d,(k,))==False


def test_255_initial_authority_repairs_both():
    W,d=W4(); k=Probe("k",1,("R","R","W","W"),frozenset({"x"}))
    t=frozenset({"x"})
    assert brac_resolves(W,d,(k,),t)==exact_resolves(W,d,(k,),t)==True


def test_256_branch_relative_multigrant_fixed_point():
    W,d=W4()
    a=Probe("a",1,("L","L","R","R"),grants=frozenset({"x"}))
    b=Probe("b",1,("L","L","R","R"),frozenset({"x"}),frozenset({"y"}))
    assert {"x","y"} <= branch_authority_closure(("w0","w1"),frozenset(),(a,b))


def test_257_unseeded_constant_cycle_does_not_invent_authority():
    W,d=W4()
    a=Probe("a",1,("s",)*4,frozenset({"y"}),frozenset({"x"}))
    b=Probe("b",1,("s",)*4,frozenset({"x"}),frozenset({"y"}))
    assert branch_authority_closure(W,frozenset(),(a,b))==frozenset()


def test_258_seeded_constant_cycle_closes():
    W,d=W4()
    a=Probe("a",1,("s",)*4,frozenset({"y"}),frozenset({"x"}))
    b=Probe("b",1,("s",)*4,frozenset({"x"}),frozenset({"y"}))
    assert branch_authority_closure(W,frozenset({"y"}),(a,b))==frozenset({"x","y"})


def test_259_probe_order_invariance():
    W,d=W4()
    a=Probe("a",1,("s",)*4,grants=frozenset({"x"}))
    k=Probe("k",1,("R","R","W","W"),frozenset({"x"}))
    assert brac_resolves(W,d,(a,k))==brac_resolves(W,d,(k,a))==True


def test_260_exhaustive_small_outcome_patterns_against_exact():
    # Within monotone world-independent Probe semantics, enumerate all binary
    # outcomes for one possible grant action and one pure sensing action.
    W,d=W4()
    for mask1 in range(16):
        o1=tuple("1" if mask1&(1<<i) else "0" for i in range(4))
        for mask2 in range(16):
            o2=tuple("1" if mask2&(1<<i) else "0" for i in range(4))
            g=Probe("g",1,o1,grants=frozenset({"x"}))
            s=Probe("s",1,o2)
            k=Probe("k",1,("R","R","W","W"),frozenset({"x"}))
            assert brac_resolves(W,d,(g,s,k))==exact_resolves(W,d,(g,s,k))


def test_261_branch_specific_authority_after_observation():
    W,d=W4()
    s=Probe("s",1,("a","a","b","b"))
    g=Probe("g",1,("x","x","y","y"),grants=frozenset({"t"}))
    k=Probe("k",1,("R","R","W","W"),frozenset({"t"}))
    assert brac_resolves(W,d,(s,g,k))==exact_resolves(W,d,(s,g,k))


def test_262_redundant_branch_grant_harmless():
    W,d=W4()
    a=Probe("a",1,("s",)*4,grants=frozenset({"t"}))
    b=Probe("b",1,("s",)*4,grants=frozenset({"t"}))
    k=Probe("k",1,("R","R","W","W"),frozenset({"t"}))
    assert brac_resolves(W,d,(a,b,k))==exact_resolves(W,d,(a,b,k))==True


def test_263_cheapest_200_preserved():
    W,d,p=family(100,True); x=cheapest_unresolved(W,d,p)
    assert (x["name"],x["cost"],x["worst_incompatible_pairs"])==("q",1,9900)


def test_264_cheapest_1000_preserved():
    W,d,p=family(500,True); x=cheapest_unresolved(W,d,p)
    assert (x["name"],x["cost"],x["worst_incompatible_pairs"])==("q",1,249500)


def test_265_cheapest_5000_preserved():
    W,d,p=family(2500,True); x=cheapest_unresolved(W,d,p)
    assert (x["name"],x["cost"],x["worst_incompatible_pairs"])==("q",1,6247500)


def test_266_cheapest_10000_preserved():
    W,d,p=family(5000,True); x=cheapest_unresolved(W,d,p)
    assert (x["name"],x["cost"],x["worst_incompatible_pairs"])==("q",1,24995000)
