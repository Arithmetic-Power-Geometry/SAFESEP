from math import inf

from safesep.cheapest import cheapest_experiment_leaving_incompatibility, cheapest_one_step_resolver
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


def test_parameterized_construction_invariants():
    """Executable proof obligations for the A_n/B_n construction."""
    for n in range(2, 51):
        a, b = finite_family(n), infinite_family(n)
        e1a, e2a = a.experiments
        e1b, e2b = b.experiments
        residual = a.worlds - {"r0"}

        # Same observable/information structure and aggregate authority statistics.
        assert a.worlds == b.worlds
        assert a.decisions == b.decisions
        assert e1a.outcomes == e1b.outcomes
        assert e2a.outcomes == e2b.outcomes
        assert e1a.cost == e1b.cost == 1.0
        assert e2a.cost == e2b.cost == 1.0
        assert len(e1a.admissible) == len(e1b.admissible) == 2 * n
        assert len(e2a.admissible) == len(e2b.admissible) == 2 * n - 1

        # e1 is safe at the root and leaves exactly the decision-critical residual branch.
        assert e1a.is_admissible_on(a.worlds)
        assert {w for w in a.worlds if e1a.outcome(w) == "residual"} == residual
        assert not a.decision_homogeneous(residual)

        # The entire separation is incidence: A admits e2 on the residual branch; B does not.
        assert e2a.is_admissible_on(residual)
        assert not e2b.is_admissible_on(residual)
        assert "r1" in residual and "r1" not in e2b.admissible

        # e2's outcome is exactly the required authorization decision.
        assert all(e2a.outcome(w) == a.decisions[w] for w in a.worlds)
        assert all(e2b.outcome(w) == b.decisions[w] for w in b.worlds)


def test_cheapest_experiment_question_on_matched_families():
    """The cheapest safe informative root probe can be identical while SafeSep differs."""
    for n in (2, 3, 5, 10, 20, 50):
        a, b = finite_family(n), infinite_family(n)
        da = cheapest_experiment_leaving_incompatibility(a, require_admissible=True)
        db = cheapest_experiment_leaving_incompatibility(b, require_admissible=True)
        assert da is not None and db is not None
        assert da.name == db.name == "e1"
        assert da.cost == db.cost == 1.0
        assert da.admissible and db.admissible
        assert da.incompatible_branches == db.incompatible_branches == 1
        assert da.worst_incompatible_pairs == db.worst_incompatible_pairs == n * (n - 1)

        # No currently admissible one-step resolver exists in either family.
        assert cheapest_one_step_resolver(a, require_admissible=True) is None
        assert cheapest_one_step_resolver(b, require_admissible=True) is None

        # Yet adaptive safe resolvability separates them.
        assert solve_safesep(a)[0] == 2.0
        assert solve_safesep(b)[0] == inf
