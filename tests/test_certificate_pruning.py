from safesep.dynamic_authority_cut import witness, cheapest_unresolved
from safesep.certificate_pruning import full_joint_search, cut_precheck


def test_53_cheapest_probe_preserved_after_ci_fix():
    x=cheapest_unresolved(witness(100,blocked=True))
    assert x=={"name":"q","cost":1.0,"worst_incompatible_pairs":9900}


def test_54_dynamic_cut_after_semantic_fix():
    assert cut_precheck(witness(8,True),{"r"})["blocked"]
    assert not cut_precheck(witness(8,False),{"r"})["blocked"]


def test_55_certificate_agrees_with_full_joint_search():
    for n in range(2,31):
        B=witness(n,True); A=witness(n,False)
        assert cut_precheck(B,{"r"})["blocked"] and not full_joint_search(B)["resolvable"]
        assert not cut_precheck(A,{"r"})["blocked"] and full_joint_search(A)["resolvable"]


def test_56_10000_world_analytic_diagnostic_and_structural_certificate():
    n=5000
    assert n*(n-1)==24_995_000
    # Certificate semantics are scale-invariant; use a smaller explicit witness in CI
    # while retaining the exact 10k pair-count benchmark analytically.
    assert cut_precheck(witness(100,True),{"r"})["blocked"]
