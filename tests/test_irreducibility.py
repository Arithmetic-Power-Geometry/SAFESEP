from math import inf
from safesep.irreducibility import (
    matched_finite_problem, matched_infinite_problem,
    coarse_signature, verify_matched_separation,
)
from safesep.solver import solve_safesep, solve_unconstrained, solve_one_step_closed


def test_matched_coarse_statistics():
    a, b = matched_finite_problem(), matched_infinite_problem()
    assert coarse_signature(a) == coarse_signature(b)
    assert len(a.worlds) == len(b.worlds) == 4
    assert tuple(e.cost for e in a.experiments) == tuple(e.cost for e in b.experiments) == (1.0, 1.0)
    assert solve_unconstrained(a) == solve_unconstrained(b) == 1.0
    assert solve_one_step_closed(a) == solve_one_step_closed(b) == inf


def test_safesep_irreducibility_separation():
    a, b = matched_finite_problem(), matched_infinite_problem()
    assert solve_safesep(a)[0] == 2.0
    assert solve_safesep(b)[0] == inf
    report = verify_matched_separation()
    assert report["coarse_signatures_equal"]
    assert report["separated"]
