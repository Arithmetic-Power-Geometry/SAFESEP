# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from math import inf

from safesep.cheapest import cheapest_experiment_leaving_incompatibility
from safesep.examples import minimal_deadlock_problem, adaptive_safe_problem, already_homogeneous_problem
from safesep.families import finite_family, infinite_family
from safesep.solver import solve_safesep, solve_unconstrained, solve_one_step_closed


def fmt(x):
    return "inf" if x == inf else x


def summarize(name, p):
    arc = solve_unconstrained(p)
    carc = solve_one_step_closed(p)
    safe, _ = solve_safesep(p)
    cheap = cheapest_experiment_leaving_incompatibility(p, require_admissible=True)
    cheap_name = "none" if cheap is None else cheap.name
    cheap_cost = "none" if cheap is None else cheap.cost
    bad_pairs = "none" if cheap is None else cheap.worst_incompatible_pairs
    print(f"{name},{fmt(arc)},{fmt(carc)},{fmt(safe)},{cheap_name},{cheap_cost},{bad_pairs}")


def main():
    print("case,ARC_like,CARC_like_one_step,SafeSep,cheapest_safe_probe_leaving_incompatibility,probe_cost,worst_remaining_incompatible_pairs")
    cases = {
        "minimal_deadlock": minimal_deadlock_problem(),
        "adaptive_safe": adaptive_safe_problem(),
        "already_homogeneous": already_homogeneous_problem(),
    }
    for name, p in cases.items():
        summarize(name, p)

    for n in (2, 3, 5, 10, 20, 50):
        summarize(f"A_{n}", finite_family(n))
        summarize(f"B_{n}", infinite_family(n))


if __name__ == "__main__":
    main()
