"""Matched-summary separation for SAFESEP.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

The two problems below have the same worlds, decisions, experiment names,
costs, outcome maps, and root-level admissibility counts.  Consequently they
have the same unconstrained decision-tree problem and the same one-step closed
resolution statistic.  They differ only in WHICH worlds admit the second
probe.  SAFESEP sees this incidence structure; scalar summaries do not.
"""
from math import inf
from .model import Experiment, Problem
from .solver import solve_safesep, solve_unconstrained, solve_one_step_closed


def matched_finite_problem():
    W = frozenset({"w1", "w2", "w3", "w4"})
    D = {"w1": "R", "w2": "R", "w3": "W", "w4": "W"}
    # e1 is universally safe but not a one-step resolver: {w1} | {w2,w3,w4}.
    e1 = Experiment("e1", 1.0,
                    {"w1": "a", "w2": "b", "w3": "b", "w4": "b"}, W)
    # e2 separates R from W on the residual branch and is admissible exactly
    # on that residual branch. Root admissibility count = 3.
    e2 = Experiment("e2", 1.0,
                    {"w1": "r", "w2": "r", "w3": "w", "w4": "w"},
                    frozenset({"w2", "w3", "w4"}))
    return Problem(W, D, (e1, e2))


def matched_infinite_problem():
    W = frozenset({"w1", "w2", "w3", "w4"})
    D = {"w1": "R", "w2": "R", "w3": "W", "w4": "W"}
    # Identical e1.
    e1 = Experiment("e1", 1.0,
                    {"w1": "a", "w2": "b", "w3": "b", "w4": "b"}, W)
    # Identical cost and outcome map; still admissible in exactly 3/4 worlds,
    # but the missing admissibility is w2, which remains in e1's residual
    # decision-critical branch. Therefore no safe second step exists.
    e2 = Experiment("e2", 1.0,
                    {"w1": "r", "w2": "r", "w3": "w", "w4": "w"},
                    frozenset({"w1", "w3", "w4"}))
    return Problem(W, D, (e1, e2))


def coarse_signature(p: Problem):
    """Statistics intentionally blind to world-by-world admissibility incidence."""
    return {
        "n_worlds": len(p.worlds),
        "decision_multiset": tuple(sorted(p.decisions.values())),
        "experiment_costs": tuple(e.cost for e in p.experiments),
        "outcome_maps": tuple(tuple(sorted(e.outcomes.items())) for e in p.experiments),
        "admissibility_counts": tuple(len(e.admissible) for e in p.experiments),
        "unconstrained_cost": solve_unconstrained(p),
        "one_step_closed_cost": solve_one_step_closed(p),
    }


def verify_matched_separation():
    A, B = matched_finite_problem(), matched_infinite_problem()
    sig_a, sig_b = coarse_signature(A), coarse_signature(B)
    sa, sb = solve_safesep(A)[0], solve_safesep(B)[0]
    return {
        "coarse_signatures_equal": sig_a == sig_b,
        "signature": sig_a,
        "finite_safesep": sa,
        "infinite_safesep": sb,
        "separated": sig_a == sig_b and sa < inf and sb == inf,
    }
