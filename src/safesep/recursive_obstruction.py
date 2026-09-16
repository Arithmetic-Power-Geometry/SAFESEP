"""Recursive authorization-obstruction certificate for SAFESEP.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Apache-2.0.

This module gives an exact finite-state recursion over joint states (C,A).
It is deliberately presented as a semantic certificate/baseline, not as a
novelty claim: AND/OR game solving and contingent planning are established.
The value is that token-only authority transitions and sensing transitions are
handled by one recursion and can be cross-checked against SAFESEP search.
"""
from functools import lru_cache
from safesep.dynamic_pair_flow import incompatible_pair_count, branchwise_legitimate, children


def canonical_state(C, tokens=frozenset()):
    return (tuple(sorted(C)), frozenset(tokens))


def progress_children(e, C, tokens):
    """Return semantic progress successors; keep token-only progress, drop true no-op."""
    parent=canonical_state(C,tokens)
    out=[]
    for B,T in children(e,C,tokens):
        ch=canonical_state(B,T)
        if ch != parent:
            out.append(ch)
    return tuple(out)


def recursive_resolvable(C, d, probes, tokens=frozenset()):
    """Exact strong-resolution existence on finite monotone belief/token systems."""
    start=canonical_state(C,tokens)
    visiting=set()
    memo={}
    def solve(state):
        if state in memo: return memo[state]
        B,T=state
        if incompatible_pair_count(B,d)==0:
            memo[state]=True; return True
        if state in visiting:
            return False
        visiting.add(state)
        ok=False
        for e in probes:
            if not branchwise_legitimate(e,T):
                continue
            ch=progress_children(e,B,T)
            if not ch:
                continue
            if all(solve(x) for x in ch):
                ok=True; break
        visiting.remove(state)
        memo[state]=ok
        return ok
    return solve(start)


def recursive_obstruction(C,d,probes,tokens=frozenset()):
    return not recursive_resolvable(C,d,probes,tokens)


def cheapest_unresolved_exact(C,d,probes,tokens=frozenset()):
    """Cheapest currently legitimate informative probe leaving a critical branch."""
    best=None
    for e in probes:
        if not branchwise_legitimate(e,tokens): continue
        raw=children(e,C,tokens)
        if len(raw)<2: continue
        worst=max(incompatible_pair_count(B,d) for B,_ in raw)
        if worst<=0: continue
        row=(e.cost,e.name,worst)
        if best is None or row<best: best=row
    return None if best is None else {"name":best[1],"cost":best[0],"worst_incompatible_pairs":best[2]}
