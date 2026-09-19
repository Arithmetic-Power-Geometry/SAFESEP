"""Complexity bounds for the SAFESEP-II normalized exact state space."""
from __future__ import annotations

from math import comb


def normalized_state_upper_bound(k: int, r: int, m: int) -> int:
    """Crude exact-search state bound: 2^k obligation sets x 2^r authority x 2^m unused probes."""
    if min(k, r, m) < 0:
        raise ValueError("parameters must be nonnegative")
    return 1 << (k + r + m)


def fixed_depth_state_upper_bound(k: int, r: int, m: int, ell: int) -> int:
    """Bound when at most ell probes may be executed.

    Unused-probe sets reachable within depth ell correspond to choosing at most
    ell executed probes, hence sum_{i=0}^ell C(m,i).
    """
    if min(k, r, m, ell) < 0:
        raise ValueError("parameters must be nonnegative")
    ell = min(ell, m)
    histories = sum(comb(m, i) for i in range(ell + 1))
    return (1 << (k + r)) * histories
