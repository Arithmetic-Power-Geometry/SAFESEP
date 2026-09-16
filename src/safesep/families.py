"""Parameterized matched-summary SAFESEP separation family.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

For every n>=2, A_n and B_n have identical worlds, decisions, experiment
costs, outcome maps, admissibility counts, unconstrained resolution cost, and
one-step closed cost. They differ only in world-by-world admissibility
incidence. A_n has SafeSep=2 while B_n has SafeSep=infinity.
"""
from .model import Experiment, Problem


def matched_family(n: int, finite: bool) -> Problem:
    if n < 2:
        raise ValueError("n must be >= 2")
    reads = [f"r{i}" for i in range(n)]
    writes = [f"w{i}" for i in range(n)]
    W = frozenset(reads + writes)
    D = {w: ("R" if w.startswith("r") else "W") for w in W}

    # First probe is universally admissible. It isolates r0 and leaves all
    # remaining worlds together, so the residual branch is decision-critical.
    e1_out = {w: ("isolated" if w == "r0" else "residual") for w in W}
    e1 = Experiment("e1", 1.0, e1_out, W)

    # Second probe is a perfect R/W decision resolver if it can be executed.
    e2_out = {w: D[w] for w in W}
    residual = W - {"r0"}
    if finite:
        # Exactly the residual branch: after e1 this becomes safely admissible.
        adm = residual
    else:
        # Same cardinality, but swap r1 out and r0 in. Therefore e2 is not
        # admissible on the residual branch and no alternative probe exists.
        adm = (residual - {"r1"}) | {"r0"}
    e2 = Experiment("e2", 1.0, e2_out, frozenset(adm))
    return Problem(W, D, (e1, e2))


def finite_family(n: int) -> Problem:
    return matched_family(n, True)


def infinite_family(n: int) -> Problem:
    return matched_family(n, False)
