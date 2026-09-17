"""Boundary attacks for closure-first SAFESEP reasoning.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Apache-2.0.

The positive extension OMCAS allows monotone authority grants on informative
probes when the grant is known after the probe.  The negative boundary permits
world-dependent hidden grants and revocation and uses exact belief states over
(world, authority) pairs.
"""
from dataclasses import dataclass
from functools import lru_cache
from .closure_exactness import compare_solvers
from .dynamic_pair_flow import Probe, incompatible_pair_count


def in_omcas(probes):
    """Current Probe semantics are monotone: grants only, no revocation.

    Unlike MCAS, informative probes may grant authority. Requirements and grants
    remain world-independent, hence acquired authority is known to the agent.
    """
    return all(isinstance(p, Probe) for p in probes)


def omcas_compare(C, d, probes, tokens=frozenset()):
    return compare_solvers(C, d, probes, tokens)


@dataclass(frozen=True)
class BeliefProbe:
    name: str
    cost: float
    outcomes: tuple
    requires: frozenset = frozenset()
    grants: tuple = ()       # tuple[frozenset], one per world
    revokes: tuple = ()      # tuple[frozenset], one per world


def _g(p, i):
    return p.grants[i] if p.grants else frozenset()


def _r(p, i):
    return p.revokes[i] if p.revokes else frozenset()


def exact_belief_resolves(worlds, decision, probes, tokens=frozenset()):
    index={w:i for i,w in enumerate(worlds)}
    start=tuple((w, tuple(sorted(tokens))) for w in worlds)
    @lru_cache(None)
    def rec(state):
        ds={decision[w] for w,_ in state}
        if len(ds)<=1: return True
        for p in probes:
            if not all(p.requires <= frozenset(T) for _,T in state):
                continue
            buckets={}
            for w,T in state:
                i=index[w]; nt=(frozenset(T)-_r(p,i))|_g(p,i)
                buckets.setdefault(p.outcomes[i],[]).append((w,tuple(sorted(nt))))
            nxt=tuple(tuple(v) for v in buckets.values())
            if len(nxt)==1 and nxt[0]==state: continue
            if all(rec(s) for s in nxt): return True
        return False
    return rec(start)


def unsafe_union_closure_resolves(worlds, decision, probes, tokens=frozenset()):
    """Deliberately unsafe abstraction used only as a falsification baseline.

    It treats a hidden world-dependent authority grant as if a grant in any
    compatible world made the token globally available. Tests prove why this
    abstraction must never be used by SAFESEP.
    """
    T=set(tokens)
    changed=True
    while changed:
        changed=False
        for p in probes:
            if len(set(p.outcomes))==1 and p.requires <= T:
                add=set().union(*(_g(p,i) for i in range(len(worlds)))) if worlds else set()
                nt=(T-set().union(*(_r(p,i) for i in range(len(worlds)))))|add
                if nt!=T: T=nt; changed=True
    # after the unsafe closure, look for a universally-required informative separator
    for p in probes:
        if len(set(p.outcomes))>1 and p.requires <= T:
            ok=True
            by={}
            for i,w in enumerate(worlds): by.setdefault(p.outcomes[i],set()).add(decision[w])
            if all(len(v)<=1 for v in by.values()): return True
    return len({decision[w] for w in worlds})<=1


def smallest_hidden_grant_counterexample():
    """Two worlds are minimal because one world cannot be decision-critical."""
    W=('r','w'); d={'r':'R','w':'W'}
    fetch=BeliefProbe('fetch',1,('same','same'),grants=(frozenset({'x'}),frozenset()))
    k=BeliefProbe('k',1,('R','W'),requires=frozenset({'x'}))
    return W,d,(fetch,k)


def smallest_revocation_counterexample():
    W=('r','w'); d={'r':'R','w':'W'}
    revoke=BeliefProbe('revoke',1,('same','same'),revokes=(frozenset({'x'}),frozenset({'x'})))
    k=BeliefProbe('k',1,('R','W'),requires=frozenset({'x'}))
    return W,d,(revoke,k),frozenset({'x'})
