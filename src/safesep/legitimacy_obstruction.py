"""Legitimacy-obstruction certificates for SAFESEP.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Apache-2.0.

For a decision-critical branch C and candidate resolving actions E, let
R(w) be the actions legitimate in world w.  A common legitimate resolver
exists iff intersection_w R(w) is nonempty.  Equivalently, with
A_w = E \ R(w), there is no common resolver iff union_w A_w = E.
Thus a minimum world witness for one-step authorization obstruction is exactly
a minimum set cover of E by the absence sets A_w.

This is an exact structural identity, not a claim that Set Cover is new.
"""
from itertools import combinations


def legitimate_actions(worlds, actions, legitimate):
    return {w: {e for e in actions if legitimate(w, e)} for w in worlds}


def common_legitimate_resolvers(worlds, actions, legitimate):
    worlds=list(worlds); actions=set(actions)
    if not worlds:
        return actions
    common=set(actions)
    for w in worlds:
        common &= {e for e in actions if legitimate(w,e)}
    return common


def absence_sets(worlds, actions, legitimate):
    actions=set(actions)
    return {w: actions-{e for e in actions if legitimate(w,e)} for w in worlds}


def minimum_obstruction_witness(worlds, actions, legitimate, max_exact_worlds=24):
    """Exact minimum witness for small branches; raises on intentionally large input."""
    worlds=list(worlds); actions=set(actions)
    if common_legitimate_resolvers(worlds,actions,legitimate):
        return None
    if len(worlds)>max_exact_worlds:
        raise ValueError("exact witness enumeration intentionally limited")
    absent=absence_sets(worlds,actions,legitimate)
    for k in range(1,len(worlds)+1):
        for S in combinations(worlds,k):
            covered=set().union(*(absent[w] for w in S))
            if covered==actions:
                return tuple(S)
    return None


def greedy_obstruction_witness(worlds, actions, legitimate):
    """Scalable cover heuristic; certificate is verified before return."""
    worlds=list(worlds); actions=set(actions)
    absent=absence_sets(worlds,actions,legitimate)
    uncovered=set(actions); chosen=[]
    while uncovered:
        w=max(worlds,key=lambda x: len(absent[x]&uncovered))
        gain=absent[w]&uncovered
        if not gain:
            return None
        chosen.append(w); uncovered-=gain; worlds.remove(w)
    return tuple(chosen)


def verify_obstruction_witness(witness, actions, legitimate):
    if witness is None:
        return False
    return not common_legitimate_resolvers(witness,actions,legitimate)


def matched_cover_family(n):
    """2n worlds and n resolvers; every world has local witnesses but no common one.

    r_i blocks e_i; w_i blocks e_(i+1 mod n).  The full branch has no common
    resolver, while each individual world admits n-1 resolvers.  For n>=2 the
    minimum obstruction witness has size n because r_0..r_(n-1) are needed to
    cover all resolver absences in this chosen subfamily.
    """
    worlds=[f"r{i}" for i in range(n)]
    actions=[f"e{i}" for i in range(n)]
    def legitimate(w,e):
        return e != f"e{int(w[1:])}"
    return worlds,actions,legitimate
