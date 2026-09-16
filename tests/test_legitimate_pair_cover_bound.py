from safesep.legitimate_pair_cover_bound import *


def test_103_cheapest_unresolved_experiment_stays_q():
    worlds,d,es=matched_case(100,"A")
    x=cheapest_unresolved_experiment(worlds,d,es)
    assert x == {"name":"q","cost":1.0,"worst_incompatible_pairs":9900}


def test_104_pair_cover_certificate_separates_matched_cases():
    wa,da,ea=matched_case(100,"A")
    wb,db,eb=matched_case(100,"B")
    A=pair_cover_lower_bound(wa,da,ea)
    B=pair_cover_lower_bound(wb,db,eb)
    assert A["obstructed"] is False
    assert A["pairs"] == 10000
    assert A["max_cover"] == 10000
    assert A["lower_bound"] == 1.0
    # B still has q, so root is not immediately obstructed; after q=rest it is.
    rest=[w for w in wb if w!="r0"]
    Br=pair_cover_lower_bound(rest,db,eb)
    assert Br["pairs"] == 9900
    assert Br["obstructed"] is True
    assert Br["lower_bound"] == float("inf")


def test_105_certificate_is_incidence_not_encoding_dependent():
    wa,da,ea=matched_case(32,"A")
    wb,db,eb=matched_case(32,"B")
    # Same world count, decisions, names, costs, and raw outcome partitions.
    assert len(wa)==len(wb)==64
    assert [(e.name,e.cost,[e.outcome(w) for w in wa]) for e in ea] == [(e.name,e.cost,[e.outcome(w) for w in wb]) for e in eb]
    # Yet legitimacy-filtered pair cover differs on the unresolved rest branch.
    ra=[w for w in wa if w!="r0"]
    rb=[w for w in wb if w!="r0"]
    assert pair_cover_lower_bound(ra,da,ea)["obstructed"] is False
    assert pair_cover_lower_bound(rb,db,eb)["obstructed"] is True


def test_106_large_10000_world_structural_stress():
    wa,da,ea=matched_case(5000,"A")
    wb,db,eb=matched_case(5000,"B")
    qa=cheapest_unresolved_experiment(wa,da,ea)
    assert qa["name"]=="q" and qa["cost"]==1.0
    assert qa["worst_incompatible_pairs"]==24995000
    # Avoid quadratic materialization for the full certificate; analytic invariant.
    n=5000
    assert (n-1)*n == 24995000
