from safesep.justification_non_equivalence import (
    cheapest_unresolved,
    extensional_signature,
    has_grounded_authorization,
    make_case,
)


def test_73_cheapest_unresolved_probe_still_q():
    c = make_case(100, grounded=True)
    assert cheapest_unresolved(c) == {
        "name": "q", "cost": 1.0, "worst_incompatible_pairs": 9900
    }


def test_74_extensional_authorization_is_matched():
    a = make_case(100, grounded=True)
    b = make_case(100, grounded=False)
    assert extensional_signature(a) == extensional_signature(b)
    assert a.extensional_authorized is b.extensional_authorized is True


def test_75_grounded_vs_self_supporting_proof_separates():
    a = make_case(100, grounded=True)
    b = make_case(100, grounded=False)
    assert has_grounded_authorization(a) is True
    assert has_grounded_authorization(b) is False


def test_76_ten_thousand_world_structural_stress():
    a = make_case(5000, grounded=True)
    b = make_case(5000, grounded=False)
    assert extensional_signature(a) == extensional_signature(b)
    assert cheapest_unresolved(a) == {
        "name": "q", "cost": 1.0, "worst_incompatible_pairs": 24995000
    }
    assert has_grounded_authorization(a) is True
    assert has_grounded_authorization(b) is False
