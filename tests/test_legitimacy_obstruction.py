from safesep.legitimacy_obstruction import *


def test_139_common_resolver_positive_boundary():
    ws=["a","b"]; es=["x","y"]
    leg=lambda w,e:e=="x"
    assert common_legitimate_resolvers(ws,es,leg)=={"x"}
    assert minimum_obstruction_witness(ws,es,leg) is None


def test_140_single_world_obstruction():
    ws=["a","b"]; es=["x","y"]
    leg=lambda w,e:not (w=="a")
    z=minimum_obstruction_witness(ws,es,leg)
    assert len(z)==1 and verify_obstruction_witness(z,es,leg)


def test_141_exact_cover_identity():
    ws,es,leg=matched_cover_family(6)
    z=minimum_obstruction_witness(ws,es,leg)
    assert len(z)==6 and verify_obstruction_witness(z,es,leg)


def test_142_every_world_locally_permissive_but_global_obstruction():
    ws,es,leg=matched_cover_family(12)
    assert all(len({e for e in es if leg(w,e)})==11 for w in ws)
    assert common_legitimate_resolvers(ws,es,leg)==set()


def test_143_exact_obstruction_number_sweep():
    for n in range(2,13):
        ws,es,leg=matched_cover_family(n)
        assert len(minimum_obstruction_witness(ws,es,leg))==n


def test_144_greedy_certificate_verified():
    ws,es,leg=matched_cover_family(128)
    z=greedy_obstruction_witness(ws,es,leg)
    assert len(z)==128 and verify_obstruction_witness(z,es,leg)


def test_145_renaming_invariance():
    ws,es,leg=matched_cover_family(10)
    z=minimum_obstruction_witness(ws,es,leg)
    assert len(z)==10
    assert len(minimum_obstruction_witness(list(reversed(ws)),list(reversed(es)),leg))==10


def test_146_large_10000_world_structural_certificate():
    # 10,000 controlled possible worlds represented as 5,000 resolver-blocking
    # witness types duplicated twice; no empirical semantics are asserted.
    n=5000
    es=[f"e{i}" for i in range(n)]
    ws=[f"r{i}" for i in range(n)] + [f"w{i}" for i in range(n)]
    def leg(w,e): return e != f"e{int(w[1:])}"
    assert common_legitimate_resolvers(ws,es,leg)==set()
    # A compact explicit witness using one copy of each blocker.
    witness=[f"r{i}" for i in range(n)]
    assert verify_obstruction_witness(witness,es,leg)
    assert all(sum(1 for e in es if leg(w,e))==n-1 for w in ("r0","w4999"))
