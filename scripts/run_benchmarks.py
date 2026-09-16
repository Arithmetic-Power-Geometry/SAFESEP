# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from math import inf

from safesep.examples import minimal_deadlock_problem, adaptive_safe_problem, already_homogeneous_problem
from safesep.solver import solve_safesep, solve_unconstrained, solve_one_step_closed


def fmt(x):
    return "inf" if x == inf else x


def main():
    cases = {
        "minimal_deadlock": minimal_deadlock_problem(),
        "adaptive_safe": adaptive_safe_problem(),
        "already_homogeneous": already_homogeneous_problem(),
    }
    print("case,ARC_like,CARC_like_one_step,SafeSep")
    for name, p in cases.items():
        arc = solve_unconstrained(p)
        carc = solve_one_step_closed(p)
        safe, _ = solve_safesep(p)
        print(f"{name},{fmt(arc)},{fmt(carc)},{fmt(safe)}")


if __name__ == "__main__":
    main()
