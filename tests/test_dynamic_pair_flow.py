from safesep.dynamic_pair_flow import *

# 107-110 core diagnostic/certificate

def test_107_cheapest_unresolved_q_200():
    W,d,E=family(100,True)
    assert cheapest_unresolved(W,d,E)=={"name":"q","cost":1.0,"worst_incompatible_pairs":9900}

def test_108_blocked_cheapest_same():
    W,d,E=family(100,False)
    assert cheapest_unresolved(W,d,E)=={"name":"q","cost":1.0,"worst_incompatible_pairs":9900}

def test_109_blocked_cut_certificate():
    W,d,E=family(12,False); assert cut_blocked(W,d,E,{"k"}) is True

def test_110_open_cut_not_blocked_by_token_only_transition():
    W,d,E=family(12,True); assert cut_blocked(W,d,E,{"k"}) is False

# 111-114 parameter sweep / soundness regressions

def test_111_parameter_sweep_cheapest():
    for n in range(2,65):
        W,d,E=family(n,True); x=cheapest_unresolved(W,d,E)
        assert x["name"]=="q" and x["cost"]==1.0 and x["worst_incompatible_pairs"]==n*(n-1)

def test_112_parameter_sweep_certificate():
    for n in range(2,65):
        W,d,E=family(n,False); assert cut_blocked(W,d,E,{"k"})
        W,d,E=family(n,True); assert not cut_blocked(W,d,E,{"k"})

def test_113_token_only_state_is_reached():
    W,d,E=family(4,True); states=list(reachable_without(W,d,E,{"k"}))
    assert any(T==frozenset({"alpha"}) for _,T in states)

def test_114_true_noop_does_not_create_state():
    W,d,E=family(4,False); states=list(reachable_without(W,d,E,{"k"}))
    assert all(T==frozenset() for _,T in states)

# 115-118 matched-information invariants

def test_115_raw_information_maps_match():
    A=family(20,True)[2]; B=family(20,False)[2]
    assert [(e.name,e.cost,e.outcomes,e.requires) for e in A]==[(e.name,e.cost,e.outcomes,e.requires) for e in B]

def test_116_action_counts_and_costs_match():
    A=family(50,True)[2]; B=family(50,False)[2]
    assert len(A)==len(B)==3 and [e.cost for e in A]==[e.cost for e in B]==[1.0,1.0,1.0]

def test_117_only_authority_flow_differs():
    A=family(10,True)[2]; B=family(10,False)[2]
    assert A[0]==B[0] and A[2]==B[2]
    assert A[1].name==B[1].name=="fetch" and A[1].outcomes==B[1].outcomes
    assert A[1].grants==frozenset({"alpha"}) and B[1].grants==frozenset()

def test_118_resolver_is_initially_illegitimate_both():
    for flag in (True,False):
        W,d,E=family(8,flag); assert not branchwise_legitimate(E[2],frozenset())

# 119-122 scale/stress and analytic invariants

def test_119_1000_world_stress():
    W,d,E=family(500,True); assert cheapest_unresolved(W,d,E)["worst_incompatible_pairs"]==249500

def test_120_2000_world_stress():
    W,d,E=family(1000,True); assert cheapest_unresolved(W,d,E)["worst_incompatible_pairs"]==999000

def test_121_5000_world_stress():
    W,d,E=family(2500,True); assert cheapest_unresolved(W,d,E)["worst_incompatible_pairs"]==6247500

def test_122_10000_world_analytic_stress():
    x=analytic_large(5000)
    assert x=={"worlds":10000,"q_cost":1.0,"q_worst_pairs":24995000}
