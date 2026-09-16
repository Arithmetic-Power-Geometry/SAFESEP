"""Unbounded authorization-legitimacy premium witness.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

This is a controlled theorem construction.  An unconstrained perfect resolver u has
cost 1 but is not legitimate.  The legitimate route must acquire n independent
authority tokens (cost 1 each) before executing a cost-1 resolver.  Hence U_n=1,
S_n=n+1, and Lambda_n=n.  The construction is deliberately compared against
cost-sensitive trust negotiation and conformant planning; the generic fact that
constraints can increase optimal plan cost is not claimed novel.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class PremiumFamily:
    n: int

    @property
    def worlds(self):
        return tuple(f"r{i}" for i in range(self.n)) + tuple(f"w{i}" for i in range(self.n))

    def decision(self, w):
        return "R" if w.startswith("r") else "W"

    def q_outcome(self, w):
        return "special" if w == "r0" else "rest"


def incompatible_pairs_in_rest(case: PremiumFamily) -> int:
    # rest has n-1 R worlds and n W worlds
    return (case.n - 1) * case.n


def cheapest_unresolved(case: PremiumFamily):
    return {"experiment": "q", "cost": 1.0,
            "worst_incompatible_pairs": incompatible_pairs_in_rest(case)}


def unconstrained_resolution_cost(case: PremiumFamily) -> float:
    # Perfect decision resolver, ignoring authorization legitimacy.
    return 1.0


def authorization_safe_resolution_cost(case: PremiumFamily) -> float:
    # n token-acquisition actions + one final resolver.
    return float(case.n + 1)


def legitimacy_premium(case: PremiumFamily) -> float:
    return authorization_safe_resolution_cost(case) - unconstrained_resolution_cost(case)


def token_requirements(case: PremiumFamily):
    return tuple(f"alpha{i}" for i in range(case.n))


def theorem_holds(case: PremiumFamily) -> bool:
    return (unconstrained_resolution_cost(case) == 1.0 and
            authorization_safe_resolution_cost(case) == case.n + 1 and
            legitimacy_premium(case) == case.n)
