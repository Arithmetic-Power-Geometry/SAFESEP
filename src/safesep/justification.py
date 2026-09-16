"""Justification-relative safe separability (JRSS) research prototype.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.
"""
from dataclasses import dataclass
from math import inf


@dataclass(frozen=True)
class JExperiment:
    name: str
    cost: float
    outcomes: dict
    required_tokens: frozenset
    grants_by_outcome: dict


@dataclass(frozen=True)
class JProblem:
    worlds: frozenset
    decisions: dict
    experiments: tuple
    initial_tokens: frozenset

    def homogeneous(self, C):
        return len({self.decisions[w] for w in C}) <= 1


def successors(C, tokens, e):
    if not e.required_tokens.issubset(tokens):
        return None
    groups = {}
    for w in C:
        o = e.outcomes[w]
        groups.setdefault(o, set()).add(w)
    out = []
    for o, ws in groups.items():
        if frozenset(ws) == C:
            continue
        out.append((frozenset(ws), tokens | frozenset(e.grants_by_outcome.get(o, ()))) )
    return out


def solve_jr_safesep(problem):
    memo, visiting = {}, set()
    def V(C, tokens):
        key = (C, tokens)
        if problem.homogeneous(C): return 0.0
        if key in memo: return memo[key]
        if key in visiting: return inf
        visiting.add(key)
        best = inf
        for e in problem.experiments:
            kids = successors(C, tokens, e)
            if not kids: continue
            vals = [V(c, q) for c, q in kids]
            if vals and all(v < inf for v in vals):
                best = min(best, e.cost + max(vals))
        visiting.remove(key)
        memo[key] = best
        return best
    return V(problem.worlds, problem.initial_tokens)


def matched_provenance_pair():
    """Same worlds/information/probes/costs; only authority provenance differs."""
    W = frozenset({"r0", "r1", "w0", "w1"})
    D = {"r0":"R", "r1":"R", "w0":"W", "w1":"W"}
    e1 = JExperiment(
        "metadata", 1.0,
        {"r0":"solo", "r1":"res", "w0":"res", "w1":"res"},
        frozenset(), {"solo":frozenset(), "res":frozenset()})
    e2 = JExperiment(
        "protected_evidence", 1.0,
        {"r0":"R", "r1":"R", "w0":"W", "w1":"W"},
        frozenset({"purpose:resolve"}), {})
    A = JProblem(W,D,(e1,e2),frozenset({"purpose:resolve"}))
    B = JProblem(W,D,(e1,e2),frozenset())
    return A,B
