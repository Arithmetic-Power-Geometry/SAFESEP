"""Authorization pair-flow lower bound.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Apache-2.0.

This module studies a restricted terminal-resolver model.  Information probes
shrink a compatible-world branch; resolver actions terminate it.  An action is
usable at C only when legitimate in every w in C.

The key quantity is the incompatible-pair mass
    M(C)=|{ {u,v}: D(u)!=D(v) }|.
For a legitimate informative action e, Delta_e(C)=M(C)-max_o M(C_e,o).
If every legitimate progress action removes at most delta incompatible pairs
in the worst branch, any resolving policy needs at least ceil(M/delta) such
progress steps (unit costs).  This is a lower bound, not a novelty claim.
"""
from dataclasses import dataclass
from math import ceil
from typing import Callable, Iterable

@dataclass(frozen=True)
class Action:
    name: str
    cost: float
    outcome: Callable[[str], str]
    legitimate: Callable[[str], bool]


def incompatible_pair_mass(worlds: Iterable[str], decision: Callable[[str], str]) -> int:
    ws=list(worlds)
    counts={}
    for w in ws:
        counts[decision(w)]=counts.get(decision(w),0)+1
    total=len(ws)
    return (total*total-sum(v*v for v in counts.values()))//2


def branches(worlds, action):
    out={}
    for w in worlds:
        out.setdefault(action.outcome(w),[]).append(w)
    return list(out.values())


def universally_legitimate(worlds, action):
    return all(action.legitimate(w) for w in worlds)


def worst_pair_reduction(worlds, decision, action):
    m=incompatible_pair_mass(worlds,decision)
    if m==0 or not universally_legitimate(worlds,action):
        return 0
    bs=branches(worlds,action)
    if len(bs)<2:
        return 0
    return m-max(incompatible_pair_mass(b,decision) for b in bs)


def pair_flow_lower_bound(worlds, decision, actions):
    m=incompatible_pair_mass(worlds,decision)
    if m==0:
        return {"pair_mass":0,"max_worst_reduction":0,"steps_lb":0,"cost_lb":0.0}
    candidates=[]
    for a in actions:
        d=worst_pair_reduction(worlds,decision,a)
        if d>0:
            candidates.append((a,d))
    if not candidates:
        return {"pair_mass":m,"max_worst_reduction":0,"steps_lb":float("inf"),"cost_lb":float("inf")}
    delta=max(d for _,d in candidates)
    min_cost=min(a.cost for a,_ in candidates)
    steps=ceil(m/delta)
    return {"pair_mass":m,"max_worst_reduction":delta,"steps_lb":steps,"cost_lb":steps*min_cost}


def cheapest_unresolved_experiment(worlds, decision, actions):
    best=None
    for a in actions:
        if not universally_legitimate(worlds,a):
            continue
        bs=branches(worlds,a)
        if len(bs)<2:
            continue
        worst=max(incompatible_pair_mass(b,decision) for b in bs)
        if worst<=0:
            continue
        row=(a.cost,a.name,worst)
        if best is None or row<best:
            best=row
    if best is None:
        return None
    return {"name":best[1],"cost":best[0],"worst_incompatible_pairs":best[2]}


def balanced_family(n: int):
    """2n worlds, binary decisions, q isolates r0; binary probes refine index bits."""
    assert n>=2
    worlds=[f"r{i}" for i in range(n)]+[f"w{i}" for i in range(n)]
    decision=lambda w: "R" if w[0]=="r" else "W"
    q=Action("q",1.0,lambda w:"special" if w=="r0" else "rest",lambda w:True)
    # Bit probes are universally legitimate and deliberately cost 1.
    bits=max(1,(n-1).bit_length())
    acts=[q]
    for b in range(bits):
        acts.append(Action(f"bit{b}",1.0,lambda w,b=b: str((int(w[1:])>>b)&1),lambda w:True))
    return worlds,decision,acts
