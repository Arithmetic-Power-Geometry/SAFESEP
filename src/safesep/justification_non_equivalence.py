"""Matched proof-structure attack for SAFESEP.

This module tests whether two systems with the same extensional authorization
relation can differ solely because one has a grounded finite justification and
the other only a self-supporting cycle.  It is retained as a prior-art
collision experiment, not as a novelty claim: proof-carrying authorization and
formally founded trust-management systems already make proof structure and
proof validity explicit.
"""
from dataclasses import dataclass
from typing import Dict, FrozenSet, Mapping, Tuple


@dataclass(frozen=True)
class ProofCase:
    worlds: Tuple[str, ...]
    decisions: Mapping[str, str]
    q_outcome: Mapping[str, str]
    q_cost: float
    extensional_authorized: bool
    proof_edges: FrozenSet[Tuple[str, str]]
    axioms: FrozenSet[str]


def make_case(n: int = 100, grounded: bool = True) -> ProofCase:
    if n < 2:
        raise ValueError("n must be >= 2")
    rs = tuple(f"r{i}" for i in range(n))
    ws = tuple(f"w{i}" for i in range(n))
    worlds = rs + ws
    decisions = {w: ("R" if w.startswith("r") else "W") for w in worlds}
    q_outcome = {w: ("special" if w == "r0" else "rest") for w in worlds}
    # Both cases expose the same extensional authorization bit.  Only the
    # provenance/proof graph differs.
    if grounded:
        edges = frozenset({("credential", "authorize")})
        axioms = frozenset({"credential"})
    else:
        edges = frozenset({("authorize", "support"), ("support", "authorize")})
        axioms = frozenset()
    return ProofCase(worlds, decisions, q_outcome, 1.0, True, edges, axioms)


def incompatible_pairs(case: ProofCase, subset=None) -> int:
    xs = tuple(subset or case.worlds)
    r = sum(case.decisions[w] == "R" for w in xs)
    w = len(xs) - r
    return r * w


def cheapest_unresolved(case: ProofCase) -> Dict[str, float]:
    branches: Dict[str, list] = {}
    for w, o in case.q_outcome.items():
        branches.setdefault(o, []).append(w)
    worst = max(incompatible_pairs(case, b) for b in branches.values())
    return {"name": "q", "cost": case.q_cost, "worst_incompatible_pairs": worst}


def grounded_closure(case: ProofCase) -> FrozenSet[str]:
    known = set(case.axioms)
    changed = True
    while changed:
        changed = False
        for premise, conclusion in case.proof_edges:
            if premise in known and conclusion not in known:
                known.add(conclusion)
                changed = True
    return frozenset(known)


def has_grounded_authorization(case: ProofCase) -> bool:
    return "authorize" in grounded_closure(case)


def extensional_signature(case: ProofCase):
    counts = {"R": 0, "W": 0}
    for d in case.decisions.values():
        counts[d] += 1
    branch_sizes: Dict[str, int] = {}
    for o in case.q_outcome.values():
        branch_sizes[o] = branch_sizes.get(o, 0) + 1
    return (len(case.worlds), tuple(sorted(counts.items())), tuple(sorted(branch_sizes.items())), case.q_cost, case.extensional_authorized)
