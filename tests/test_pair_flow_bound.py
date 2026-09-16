from math import isinf
from safesep.pair_flow_bound import *


def test_123_zero_mass_zero_bound():
    ws=["r0","r1"]
    assert pair_flow_lower_bound(ws,lambda w:"R",[])["steps_lb"]==0


def test_124_pair_mass_binary_exact():
    ws,d,_=balanced_family(100)
    assert incompatible_pair_mass(ws,d)==10000


def test_125_cheapest_unresolved_q_200():
    ws,d,acts=balanced_family(100)
    x=cheapest_unresolved_experiment(ws,d,acts)
    assert x["name"]=="q" and x["cost"]==1.0 and x["worst_incompatible_pairs"]==9900


def test_126_q_reduction_exact_200():
    ws,d,acts=balanced_family(100)
    assert worst_pair_reduction(ws,d,acts[0])==100


def test_127_illegitimate_probe_has_zero_capacity():
    ws,d,_=balanced_family(8)
    a=Action("x",1,lambda w:w[0],lambda w:w!="r0")
    assert worst_pair_reduction(ws,d,a)==0


def test_128_true_noop_has_zero_capacity():
    ws,d,_=balanced_family(8)
    a=Action("noop",1,lambda w:"same",lambda w:True)
    assert worst_pair_reduction(ws,d,a)==0


def test_129_perfect_resolver_capacity_all_pairs():
    ws,d,_=balanced_family(8)
    a=Action("perfect",2,lambda w:d(w),lambda w:True)
    assert worst_pair_reduction(ws,d,a)==incompatible_pair_mass(ws,d)


def test_130_perfect_resolver_lb_one():
    ws,d,_=balanced_family(8)
    a=Action("perfect",2,lambda w:d(w),lambda w:True)
    z=pair_flow_lower_bound(ws,d,[a])
    assert z["steps_lb"]==1 and z["cost_lb"]==2


def test_131_no_progress_is_infinite_obstruction():
    ws,d,_=balanced_family(8)
    a=Action("noop",1,lambda w:"same",lambda w:True)
    assert isinf(pair_flow_lower_bound(ws,d,[a])["steps_lb"])


def test_132_monotonic_mass_under_partition():
    for n in range(2,65):
        ws,d,acts=balanced_family(n)
        m=incompatible_pair_mass(ws,d)
        for a in acts:
            assert max(incompatible_pair_mass(b,d) for b in branches(ws,a))<=m


def test_133_q_formula_sweep():
    for n in range(2,129):
        ws,d,acts=balanced_family(n)
        q=acts[0]
        assert worst_pair_reduction(ws,d,q)==n
        assert max(incompatible_pair_mass(b,d) for b in branches(ws,q))==n*(n-1)


def test_134_renaming_invariance():
    ws,d,acts=balanced_family(32)
    base=pair_flow_lower_bound(ws,d,acts)
    # Reverse world order: semantic result must not depend on representation order.
    rev=pair_flow_lower_bound(list(reversed(ws)),d,acts)
    assert base==rev


def test_135_action_order_invariance():
    ws,d,acts=balanced_family(32)
    assert pair_flow_lower_bound(ws,d,acts)==pair_flow_lower_bound(ws,d,list(reversed(acts)))


def test_136_cost_scaling():
    ws,d,acts=balanced_family(16)
    z=pair_flow_lower_bound(ws,d,acts)
    scaled=[Action(a.name,a.cost*7,a.outcome,a.legitimate) for a in acts]
    zs=pair_flow_lower_bound(ws,d,scaled)
    assert zs["steps_lb"]==z["steps_lb"]
    assert zs["cost_lb"]==7*z["cost_lb"]


def test_137_large_10000_cheapest_q():
    ws,d,acts=balanced_family(5000)
    x=cheapest_unresolved_experiment(ws,d,acts)
    assert x=={"name":"q","cost":1.0,"worst_incompatible_pairs":24995000}


def test_138_large_10000_mass_and_q_capacity():
    ws,d,acts=balanced_family(5000)
    assert incompatible_pair_mass(ws,d)==25000000
    assert worst_pair_reduction(ws,d,acts[0])==5000
    assert 25000000-5000==24995000
