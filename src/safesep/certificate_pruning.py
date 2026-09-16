"""Compare a structural authorization-cut precheck with full joint-state search.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

This module does not claim asymptotic superiority. It instruments explored joint states
so the claimed benefit is empirical pruning on certified blocked instances only.
"""
from functools import lru_cache
from .dynamic_authority_cut import incompatible_pairs, executable, progress_children, dynamic_cut_certificate


def full_joint_search(P):
    visiting=set(); expanded=0
    @lru_cache(maxsize=None)
    def win(C,tokens):
        nonlocal expanded
        C=frozenset(C); tokens=frozenset(tokens); expanded += 1
        if not incompatible_pairs(P,C): return True
        key=(C,tokens)
        if key in visiting: return False
        visiting.add(key)
        try:
            for e in P.probes:
                if not executable(e,tokens): continue
                children=progress_children(e,C,tokens)
                if not children: continue
                if all(win(B,T) for B,T in children): return True
            return False
        finally: visiting.discard(key)
    ok=win(frozenset(P.worlds),P.initial_tokens)
    return {"resolvable":ok,"expanded_states":expanded}


def cut_precheck(P,cut):
    c=dynamic_cut_certificate(P,frozenset(cut))
    return {"blocked":bool(c["certificate"]),
            "reachable_critical_states_checked":c["reachable_critical_states_without_cut"]}
