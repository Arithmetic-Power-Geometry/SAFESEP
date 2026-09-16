from safesep.acquisition_path_coupling import matched_pair, coarse_signature, cheapest_unresolved_experiment


def test_77_cheapest_unresolved_probe_200_worlds():
    a, _ = matched_pair(100)
    assert cheapest_unresolved_experiment(a) == {"name":"q","cost":1.0,"worst_incompatible_pairs":9900}


def test_78_same_proof_existence_and_coarse_graph():
    a, b = matched_pair(100)
    assert coarse_signature(a) == coarse_signature(b)
    assert a.proof_exists() and b.proof_exists()
    assert a.proof_graph_signature() == b.proof_graph_signature()


def test_79_acquisition_path_separates_resolvability():
    a, b = matched_pair(100)
    assert a.component_obtainable_on_rest() is True
    assert b.component_obtainable_on_rest() is False
    assert a.residual_resolvable() is True
    assert b.residual_resolvable() is False


def test_80_large_10000_world_structural_stress():
    a, b = matched_pair(5000)
    assert coarse_signature(a) == coarse_signature(b)
    assert cheapest_unresolved_experiment(a)["cost"] == 1.0
    assert cheapest_unresolved_experiment(a)["worst_incompatible_pairs"] == 24_995_000
    assert a.residual_resolvable() and not b.residual_resolvable()
