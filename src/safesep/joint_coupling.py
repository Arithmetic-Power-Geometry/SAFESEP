"""Matched-marginal information-authority coupling witness.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

This module tests a deliberately narrow structural claim: separate information
and authority marginals need not determine adaptive resolvability when an
experiment outcome controls which authority token becomes available.
"""
from dataclasses import dataclass
from typing import Dict, FrozenSet, Mapping, Tuple


@dataclass(frozen=True)
class JointCase:
    worlds: Tuple[str, ...]
    decisions: Mapping[str, str]
    q_outcome: Mapping[str, str]
    q_cost: float
    # token yielded by each q outcome
    outcome_token: Mapping[str, str]
    # resolver authorized by token
    token_resolver: Mapping[str, str]


def matched_joint_pair(n: int = 50):
    """Return A_n/B_n with matched separate marginals but different alignment.

    q isolates r0 and leaves a decision-critical residual branch. Both cases
    have tokens {alpha,beta} and resolvers {resolve_rest, resolve_special}, with
    identical one-to-one authority marginals. A aligns the residual outcome
    with resolve_rest; B swaps token yield across q outcomes.
    """
    if n < 2:
        raise ValueError("n must be >=2")
    rs = tuple(f"r{i}" for i in range(n))
    ws = tuple(f"w{i}" for i in range(n))
    worlds = rs + ws
    decisions = {w: ("R" if w.startswith("r") else "W") for w in worlds}
    q_outcome = {w: ("special" if w == "r0" else "rest") for w in worlds}
    authority = {"alpha": "resolve_rest", "beta": "resolve_special"}
    A = JointCase(worlds, decisions, q_outcome, 1.0,
                  {"special": "beta", "rest": "alpha"}, authority)
    B = JointCase(worlds, decisions, q_outcome, 1.0,
                  {"special": "alpha", "rest": "beta"}, authority)
    return A, B


def incompatible_pair_count(case: JointCase, branch: FrozenSet[str]) -> int:
    r = sum(case.decisions[w] == "R" for w in branch)
    x = len(branch) - r
    return r * x


def cheapest_unresolved_experiment(case: JointCase):
    """The construction has one root unresolved informative experiment q."""
    branches: Dict[str, set] = {}
    for w in case.worlds:
        branches.setdefault(case.q_outcome[w], set()).add(w)
    unresolved = [frozenset(b) for b in branches.values()
                  if len({case.decisions[w] for w in b}) > 1]
    return {"name": "q", "cost": case.q_cost,
            "unresolved_branches": len(unresolved),
            "worst_incompatible_pairs": max((incompatible_pair_count(case, b) for b in unresolved), default=0)}


def separate_marginals(case: JointCase):
    """Summaries that intentionally forget outcome-to-token alignment."""
    branch_sizes = sorted(sum(1 for w in case.worlds if case.q_outcome[w] == o)
                          for o in set(case.q_outcome.values()))
    return {
        "worlds": len(case.worlds),
        "decision_counts": tuple(sorted((d, list(case.decisions.values()).count(d)) for d in set(case.decisions.values()))),
        "branch_sizes": tuple(branch_sizes),
        "tokens": tuple(sorted(case.outcome_token.values())),
        "authority_targets": tuple(sorted(case.token_resolver.values())),
        "authority_edge_count": len(case.token_resolver),
        "q_cost": case.q_cost,
    }


def residual_resolvable(case: JointCase) -> bool:
    """Whether q's decision-critical residual branch receives its resolver."""
    token = case.outcome_token["rest"]
    return case.token_resolver[token] == "resolve_rest"
