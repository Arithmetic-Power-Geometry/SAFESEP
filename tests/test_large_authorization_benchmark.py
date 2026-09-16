"""Large-scale structural SAFESEP benchmark.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

These tests validate analytic invariants at up to 10,000 explicit possible
worlds without invoking the exponential exact solver. The exact solver is
covered separately on smaller instances.
"""
from safesep.families import finite_family, infinite_family
from safesep.cheapest import diagnose_experiment


def test_large_matched_family_structural_invariants():
    """Significance: incidence separation survives to 10,000 worlds."""
    for n in (100, 250, 500, 1000, 2500, 5000):
        a, b = finite_family(n), infinite_family(n)
        assert a.worlds == b.worlds
        assert a.decisions == b.decisions
        assert len(a.worlds) == 2 * n
        assert tuple(e.cost for e in a.experiments) == tuple(e.cost for e in b.experiments) == (1.0, 1.0)
        assert tuple(e.outcomes for e in a.experiments) == tuple(e.outcomes for e in b.experiments)
        assert tuple(len(e.admissible) for e in a.experiments) == tuple(len(e.admissible) for e in b.experiments) == (2*n, 2*n-1)

        e1a, e2a = a.experiments
        e1b, e2b = b.experiments
        residual = frozenset(w for w in a.worlds if w != "r0")
        assert e1a.is_admissible_on(a.worlds)
        assert e1b.is_admissible_on(b.worlds)
        assert e2a.is_admissible_on(residual)
        assert not e2b.is_admissible_on(residual)

        da = diagnose_experiment(a, e1a)
        db = diagnose_experiment(b, e1b)
        assert da == db
        assert da.cost == 1.0
        assert da.incompatible_branches == 1
        assert da.worst_incompatible_pairs == n * (n - 1)


def test_large_family_constructive_safe_tree_and_obstruction():
    """Significance: constructive proof obligations hold independently of DP solver."""
    for n in (100, 1000, 5000):
        a, b = finite_family(n), infinite_family(n)
        residual = a.worlds - {"r0"}
        e2a = a.experiments[1]
        e2b = b.experiments[1]
        # A: after e1's residual outcome, e2 is legal and its outcomes are exactly decisions.
        assert e2a.is_admissible_on(residual)
        for w in residual:
            assert e2a.outcome(w) == a.decisions[w]
        # B: r1 remains possible after e1 but blocks e2, while no third probe exists.
        assert "r1" in residual
        assert "r1" not in e2b.admissible
        assert len(b.experiments) == 2
