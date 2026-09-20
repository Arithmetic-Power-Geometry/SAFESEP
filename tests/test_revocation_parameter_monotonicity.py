from safesep.revocation_complexity import normalized_state_upper_bound


def test_parameter_monotonicity_by_set_inclusion():
    P0 = frozenset({frozenset((0, 1)), frozenset((0, 2)), frozenset((1, 2))})
    P1 = frozenset({frozenset((1, 2))})
    assert P1 <= P0
    assert {w for pair in P1 for w in pair} <= {w for pair in P0 for w in pair}

    reqs0 = (frozenset({"x"}), frozenset({"y"}), frozenset({"x", "z"}))
    reqs1 = reqs0[1:]
    R0 = frozenset().union(*reqs0)
    R1 = frozenset().union(*reqs1)
    assert R1 <= R0


def test_coarse_state_bound_is_parameter_only_after_type_kernel():
    # If T is already bounded by k,r, the remaining state count has no m term.
    k, r, T = 3, 2, 7
    assert normalized_state_upper_bound(k, r, T) == 1 << (k + r + T)
