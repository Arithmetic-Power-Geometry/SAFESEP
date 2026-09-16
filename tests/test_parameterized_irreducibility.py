from math import inf

from safesep.families import finite_family, infinite_family
from safesep.irreducibility import coarse_signature
from safesep.solver import solve_safesep, solve_unconstrained, solve_one_step_closed


def test_parameterized_matched_summary_irreducibility_family():
    """Significance test: scalar summaries cannot determine safe resolvability."""
    for n in range(2, 21):
        a, b = finite_family(n), infinite_family(n)
        assert coarse_signature(a) == coarse_signature(b)
        assert solve_unconstrained(a) == solve_unconstrained(b) == 1.0
        assert solve_one_step_closed(a) == solve_one_step_closed(b) == inf
        assert solve_safesep(a)[0] == 2.0
        assert solve_safesep(b)[0] == inf


def test_family_scales_world_count_without_changing_separation():
    for n in (2, 3, 5, 10, 20, 50):
        a, b = finite_family(n), infinite_family(n)
        assert len(a.worlds) == len(b.worlds) == 2 * n
        assert tuple(len(e.admissible) for e in a.experiments) == tuple(len(e.admissible) for e in b.experiments)
        assert solve_safesep(a)[0] == 2.0
        assert solve_safesep(b)[0] == inf
