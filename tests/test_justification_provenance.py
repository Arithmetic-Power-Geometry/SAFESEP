from math import inf
from safesep.justification import matched_provenance_pair, solve_jr_safesep


def test_matched_belief_different_authority_provenance_separates_resolution():
    """Significance: identical epistemic uncertainty can differ in authority closure."""
    a,b = matched_provenance_pair()
    assert a.worlds == b.worlds
    assert a.decisions == b.decisions
    assert [(e.name,e.cost,e.outcomes) for e in a.experiments] == [(e.name,e.cost,e.outcomes) for e in b.experiments]
    assert solve_jr_safesep(a) == 1.0
    assert solve_jr_safesep(b) == inf


def test_cheapest_information_structure_is_identical_despite_provenance_split():
    """Ignoring authority provenance, both instances expose the same cheapest experiments."""
    a,b = matched_provenance_pair()
    assert [(e.name,e.cost) for e in a.experiments] == [(e.name,e.cost) for e in b.experiments]
    assert min(e.cost for e in a.experiments) == min(e.cost for e in b.experiments) == 1.0
