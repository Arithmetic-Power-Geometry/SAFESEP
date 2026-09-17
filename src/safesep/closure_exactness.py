"""Exactness class for authority-closure SAFESEP certificates.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Apache-2.0.

Restricted class MCAS (Monotone Closure-then-Authorized Sensing):
1. authority-only actions have one observation and add tokens monotonically;
2. their requirements/grants are world-independent;
3. sensing actions do not change authority;
4. sensing legitimacy depends only on the current token set;
5. authority-only actions do not change the compatible-world set.

In MCAS, saturating authority closure before choosing a sensing action is without
loss of resolvability.  This module checks the class and compares a closure-first
solver with an exact joint-state solver.
"""
from functools import lru_cache
from .dynamic_pair_flow import children, branchwise_legitimate, incompatible_pair_count


def is_authority_only(e):
    return len(set(e.outcomes)) == 1


def in_mcas(probes):
    # Probe representation already makes requirements/grants world-independent.
    # MCAS additionally forbids authority grants on informative probes.
    return all(is_authority_only(e) or not e.grants for e in probes)


def authority_closure(tokens, probes):
    T=set(tokens)
    changed=True
    while changed:
        changed=False
        for e in probes:
            if is_authority_only(e) and e.requires <= T:
                nt=T|set(e.grants)
                if nt != T:
                    T=nt; changed=True
    return frozenset(T)


def closure_first_resolves(C,d,probes,tokens=frozenset()):
    C=tuple(C)
    @lru_cache(None)
    def rec(B,T):
        if incompatible_pair_count(B,d)==0: return True
        Tc=authority_closure(frozenset(T),probes)
        for e in probes:
            if is_authority_only(e) or not branchwise_legitimate(e,Tc): continue
            bs=children(e,B,Tc)
            if len(bs)<2: continue
            if all(rec(tuple(ch),tuple(sorted(nt))) for ch,nt in bs): return True
        return False
    return rec(C,tuple(sorted(tokens)))


def exact_resolves(C,d,probes,tokens=frozenset()):
    C=tuple(C)
    @lru_cache(None)
    def rec(B,T):
        if incompatible_pair_count(B,d)==0: return True
        Ts=frozenset(T)
        for e in probes:
            if not branchwise_legitimate(e,Ts): continue
            bs=children(e,B,Ts)
            progress=[(tuple(ch),nt) for ch,nt in bs if tuple(ch)!=B or nt!=Ts]
            if not progress: continue
            # For a deterministic authority-only transition there is one child.
            if len(bs)==1:
                ch,nt=bs[0]
                if rec(tuple(ch),tuple(sorted(nt))): return True
            elif all(rec(tuple(ch),tuple(sorted(nt))) for ch,nt in bs):
                return True
        return False
    return rec(C,tuple(sorted(tokens)))


def compare_solvers(C,d,probes,tokens=frozenset()):
    return closure_first_resolves(C,d,probes,tokens), exact_resolves(C,d,probes,tokens)
