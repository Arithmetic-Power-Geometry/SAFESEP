"""Branch-relative authority closure (BRAC) for SAFESEP.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Apache-2.0.

BRAC generalizes MCAS operationally without claiming generic planning novelty:
at each belief branch, repeatedly execute legitimate actions whose outcomes are
constant on that *current branch* and whose only progress is monotone authority
gain. Globally informative actions may therefore enter closure after earlier
observations. The exact solver remains the reference oracle.
"""
from functools import lru_cache
from .dynamic_pair_flow import children, branchwise_legitimate, incompatible_pair_count


def branch_constant(e, B):
    return len({e.outcome(w) for w in B}) == 1


def branch_authority_closure(B, tokens, probes):
    T=set(tokens)
    changed=True
    while changed:
        changed=False
        for e in probes:
            if branch_constant(e,B) and e.requires <= T:
                nt=T|set(e.grants)
                if nt != T:
                    T=nt
                    changed=True
    return frozenset(T)


def brac_resolves(C,d,probes,tokens=frozenset()):
    C=tuple(C)
    @lru_cache(None)
    def rec(B,T):
        if incompatible_pair_count(B,d)==0:
            return True
        Tc=branch_authority_closure(B,frozenset(T),probes)
        for e in probes:
            if branch_constant(e,B) or not branchwise_legitimate(e,Tc):
                continue
            bs=children(e,B,Tc)
            if len(bs)<2:
                continue
            if all(rec(tuple(ch),tuple(sorted(nt))) for ch,nt in bs):
                return True
        return False
    return rec(C,tuple(sorted(tokens)))
