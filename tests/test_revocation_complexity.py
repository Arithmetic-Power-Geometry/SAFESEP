from safesep.revocation_complexity import (
    fixed_depth_state_upper_bound,
    normalized_state_upper_bound,
)


def test_normalized_state_bound():
    assert normalized_state_upper_bound(3, 2, 4) == 512


def test_fixed_depth_bound_is_polynomial_in_m_for_fixed_depth():
    # 2^(k+r) * (C(10,0)+C(10,1)+C(10,2))
    assert fixed_depth_state_upper_bound(3, 2, 10, 2) == 32 * 56


def test_depth_zero_and_clipping():
    assert fixed_depth_state_upper_bound(2, 1, 5, 0) == 8
    assert fixed_depth_state_upper_bound(0, 0, 3, 99) == 8
