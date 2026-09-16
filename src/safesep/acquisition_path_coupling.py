"""Matched proof existence with branchwise legitimate acquisition paths."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AcquisitionCase:
    n: int
    variant: str
    q_cost: float = 1.0

    @property
    def worlds(self):
        return tuple([f"r{i}" for i in range(self.n)] + [f"w{i}" for i in range(self.n)])

    def decision(self, w):
        return "R" if w.startswith("r") else "W"

    def q_outcome(self, w):
        return "special" if w == "r0" else "rest"

    def proof_exists(self):
        # Both systems have the same ordinary proof graph: component c entails resolver authorization.
        return True

    def proof_graph_signature(self):
        return (("c", "authorize_r"),)

    def component_obtainable_on_rest(self):
        # A: c has an independently legitimate acquisition route on the residual branch.
        # B: c exists and supports the same proof, but every acquisition route presupposes r.
        return self.variant == "A"

    def residual_resolvable(self):
        return self.proof_exists() and self.component_obtainable_on_rest()


def matched_pair(n=100):
    return AcquisitionCase(n, "A"), AcquisitionCase(n, "B")


def incompatible_pairs_after_q(case):
    # rest contains n-1 R worlds and n W worlds
    return (case.n - 1) * case.n


def cheapest_unresolved_experiment(case):
    return {"name": "q", "cost": case.q_cost,
            "worst_incompatible_pairs": incompatible_pairs_after_q(case)}


def coarse_signature(case):
    return {
        "worlds": 2 * case.n,
        "R": case.n,
        "W": case.n,
        "q_branch_sizes": (1, 2 * case.n - 1),
        "q_cost": case.q_cost,
        "proof_exists": case.proof_exists(),
        "proof_graph": case.proof_graph_signature(),
        "proof_component_count": 1,
    }
