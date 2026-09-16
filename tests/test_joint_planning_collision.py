"""Tests 37-40: attack joint coupling with a full combined-state planner."""
from safesep.joint_coupling import (
    cheapest_unresolved_experiment,
    matched_joint_pair,
    residual_resolvable,
    separate_marginals,
)
from safesep.joint_planning_baseline import (
    combined_state_contingent_resolvable,
    joint_state_signature,
)


def test_37_cheapest_experiment_still_q_and_leaves_incompatibility():
    A, B = matched_joint_pair(100)
    da = cheapest_unresolved_experiment(A)
    db = cheapest_unresolved_experiment(B)
    assert da == db
    assert da["name"] == "q"
    assert da["cost"] == 1.0
    assert da["unresolved_branches"] == 1
    assert da["worst_incompatible_pairs"] == 100 * 99


def test_38_combined_state_planner_exactly_reproduces_separation():
    A, B = matched_joint_pair(50)
    assert residual_resolvable(A) is True
    assert residual_resolvable(B) is False
    assert combined_state_contingent_resolvable(A) is True
    assert combined_state_contingent_resolvable(B) is False


def test_39_separate_marginals_match_but_full_joint_state_does_not():
    A, B = matched_joint_pair(50)
    assert separate_marginals(A) == separate_marginals(B)
    assert joint_state_signature(A) != joint_state_signature(B)


def test_40_10000_world_collision_and_cheapest_probe():
    A, B = matched_joint_pair(5000)
    assert len(A.worlds) == len(B.worlds) == 10000
    assert separate_marginals(A) == separate_marginals(B)
    da = cheapest_unresolved_experiment(A)
    db = cheapest_unresolved_experiment(B)
    assert da == db
    assert da["name"] == "q" and da["cost"] == 1.0
    assert da["worst_incompatible_pairs"] == 5000 * 4999
    assert combined_state_contingent_resolvable(A) is True
    assert combined_state_contingent_resolvable(B) is False
