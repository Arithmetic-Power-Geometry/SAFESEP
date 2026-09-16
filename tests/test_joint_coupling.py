"""Tests 33-36: joint information-authority coupling."""
from safesep.joint_coupling import (
    matched_joint_pair, cheapest_unresolved_experiment,
    separate_marginals, residual_resolvable,
)


def test_33_cheapest_experiment_same_and_leaves_incompatible_worlds():
    A, B = matched_joint_pair(100)
    a = cheapest_unresolved_experiment(A)
    b = cheapest_unresolved_experiment(B)
    assert a == b
    assert a["name"] == "q" and a["cost"] == 1.0
    assert a["unresolved_branches"] == 1
    assert a["worst_incompatible_pairs"] == 100 * 99


def test_34_separate_information_and_authority_marginals_match():
    A, B = matched_joint_pair(100)
    assert separate_marginals(A) == separate_marginals(B)


def test_35_joint_alignment_changes_resolvability():
    A, B = matched_joint_pair(50)
    assert residual_resolvable(A)
    assert not residual_resolvable(B)


def test_36_scale_to_10000_worlds():
    A, B = matched_joint_pair(5000)
    assert len(A.worlds) == len(B.worlds) == 10000
    assert separate_marginals(A) == separate_marginals(B)
    assert cheapest_unresolved_experiment(A) == cheapest_unresolved_experiment(B)
    assert cheapest_unresolved_experiment(A)["worst_incompatible_pairs"] == 5000 * 4999
    assert residual_resolvable(A) and not residual_resolvable(B)
