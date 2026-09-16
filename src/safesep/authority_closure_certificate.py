"""Authority-closure obstruction certificate for SAFESEP.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Apache-2.0.

The certificate deliberately handles zero-information authority actions before
asking whether any decision-separating experiment can become legitimate.
It is a compact sufficient deadlock certificate for monotone token systems,
not a replacement for general contingent planning.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Action:
    name: str
    cost: float
    outcomes: tuple
    requires: frozenset=frozenset()
    grants: frozenset=frozenset()

    def outcome(self,w): return self.outcomes[int(w[1:])]

def decision_map(n):
    return {f"w{i}":("R" if i<n else "W") for i in range(2*n)}

def pair_mass(C,d):
    r=sum(d[w]=="R" for w in C); return r*(len(C)-r)

def branches(C,a):
    z={}
    for w in C: z.setdefault(a.outcome(w),[]).append(w)
    return [tuple(v) for v in z.values()]

def legitimate(a,tokens): return a.requires <= tokens

def informative(C,a): return len(branches(C,a))>1

def authority_closure(C,actions,tokens=frozenset()):
    """Least monotone closure under legitimate zero-information token actions."""
    T=frozenset(tokens)
    changed=True
    while changed:
        changed=False
        for a in actions:
            if legitimate(a,T) and not informative(C,a):
                nt=T|a.grants
                if nt!=T: T=nt; changed=True
    return T

def available_separators(C,d,actions,tokens=frozenset()):
    T=authority_closure(C,actions,tokens)
    out=[]
    for a in actions:
        if not legitimate(a,T) or not informative(C,a): continue
        if max(pair_mass(b,d) for b in branches(C,a)) < pair_mass(C,d): out.append(a.name)
    return tuple(sorted(out))

def closure_obstructed(C,d,actions,tokens=frozenset()):
    if pair_mass(C,d)==0: return False
    return len(available_separators(C,d,actions,tokens))==0

def cheapest_unresolved(C,d,actions,tokens=frozenset()):
    T=authority_closure(C,actions,tokens)
    best=None
    for a in actions:
        if not legitimate(a,T) or not informative(C,a): continue
        worst=max(pair_mass(b,d) for b in branches(C,a))
        if worst<=0: continue
        row=(a.cost,a.name,worst)
        if best is None or row<best: best=row
    return None if best is None else {"name":best[1],"cost":best[0],"worst_incompatible_pairs":best[2]}

def family(n=100,open_case=True):
    W=tuple(f"w{i}" for i in range(2*n)); d=decision_map(n)
    q=Action("q",1.0,tuple("special" if i==0 else "rest" for i in range(2*n)))
    same=tuple("same" for _ in W)
    fetch=Action("fetch",1.0,same,grants=frozenset({"alpha"}) if open_case else frozenset())
    k=Action("k",2.0,tuple("R" if i<n else "W" for i in range(2*n)),requires=frozenset({"alpha"}))
    return W,d,(q,fetch,k)
