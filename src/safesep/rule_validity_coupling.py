"""Matched rule-validity coupling attack for SAFESEP.

This module asks whether coarse authorization summaries can determine safe
separability when the validity of the rule authorizing a resolver is coupled
to the still-compatible world.

It is intentionally a novelty-attack construction, not a novelty claim.
"""
from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class RuleValidityCase:
    n: int
    aligned: bool

    @property
    def worlds(self) -> Tuple[str, ...]:
        return tuple([f"r{i}" for i in range(self.n)] + [f"w{i}" for i in range(self.n)])

    def decision(self, w: str) -> str:
        return "R" if w.startswith("r") else "W"

    def q_outcome(self, w: str) -> str:
        return "special" if w == "r0" else "rest"

    def rule_valid(self, w: str) -> bool:
        # Same validity marginal in A/B: exactly n worlds validate the rule.
        # A aligns validity with R-worlds; B rotates validity onto W-worlds.
        if self.aligned:
            return w.startswith("r")
        return w.startswith("w")

    def structural_signature(self):
        ws = self.worlds
        return {
            "worlds": len(ws),
            "R": sum(self.decision(w) == "R" for w in ws),
            "W": sum(self.decision(w) == "W" for w in ws),
            "q_special": sum(self.q_outcome(w) == "special" for w in ws),
            "q_rest": sum(self.q_outcome(w) == "rest" for w in ws),
            "rule_valid": sum(self.rule_valid(w) for w in ws),
            "rule_invalid": sum(not self.rule_valid(w) for w in ws),
            "q_cost": 1,
            "resolver_cost": 1,
        }


def incompatible_pairs_in_rest(case: RuleValidityCase) -> int:
    # rest contains n-1 R worlds and n W worlds.
    return (case.n - 1) * case.n


def cheapest_unresolved(case: RuleValidityCase):
    return {"experiment": "q", "cost": 1, "worst_incompatible_pairs": incompatible_pairs_in_rest(case)}


def branchwise_resolver_legitimate(case: RuleValidityCase) -> bool:
    """Resolver is legitimate only if its authorizing rule is valid in every
    still-compatible world of the unresolved q=rest branch.

    The present A/B witness deliberately fails this universal condition in
    both cases. This is a diagnostic showing that matched validity marginals
    alone are insufficient to create the desired separation; stronger rule
    semantics are required.
    """
    rest = [w for w in case.worlds if case.q_outcome(w) == "rest"]
    return all(case.rule_valid(w) for w in rest)


def matched_pair(n: int = 100):
    return RuleValidityCase(n, True), RuleValidityCase(n, False)
