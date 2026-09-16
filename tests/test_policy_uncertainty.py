# Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.
from safesep.policy_uncertainty import make_case, cheapest_unresolved, incompatible_pairs, second_order_state_size


def test_61_cheapest_experiment_under_policy_uncertainty():
    c=make_case(100); d=cheapest_unresolved(c)
    assert d["name"]=="q" and d["cost"]==1.0
    assert d["worst_incompatible_pairs"]==9900
    assert d["policies_remaining"]==2


def test_62_policy_identity_is_part_of_possible_world_state():
    c=make_case(100)
    assert second_order_state_size(c)==200
    assert incompatible_pairs(c)==10000


def test_63_observation_leaves_decision_and_policy_uncertainty():
    c=make_case(100)
    rest=[w for w in c.worlds if c.q_outcome[w]=="rest"]
    assert incompatible_pairs(c,rest)==9900
    assert len({c.policy[w] for w in rest})==2


def test_64_policy_uncertainty_10000_world_stress():
    c=make_case(5000); d=cheapest_unresolved(c)
    assert len(c.worlds)==10000
    assert d["name"]=="q" and d["cost"]==1.0
    assert d["worst_incompatible_pairs"]==24995000
    assert d["policies_remaining"]==2
