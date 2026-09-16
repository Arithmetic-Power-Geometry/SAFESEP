"""Common Legitimate Evidence (CLE) obstruction diagnostics.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.

CLE(C) is the minimum cost of a single informative experiment that is legitimate
in every world of decision-critical branch C. Infinity means no such common
legitimate experiment exists. This is a diagnostic/lower-bound object, not a
claim of novelty over belief-state planning.
"""
from dataclasses import dataclass
from math import inf
from typing import Mapping, Tuple, FrozenSet

World=str

@dataclass(frozen=True)
class Experiment:
    name: str
    cost: float
    outcomes: Mapping[World,str]
    legitimate: FrozenSet[World]

@dataclass(frozen=True)
class CLECase:
    worlds: Tuple[World,...]
    decisions: Mapping[World,str]
    experiments: Tuple[Experiment,...]


def incompatible_pairs(case, C=None):
    C=case.worlds if C is None else tuple(C)
    return sum(1 for i,a in enumerate(C) for b in C[i+1:] if case.decisions[a]!=case.decisions[b])


def informative(e,C):
    return len({e.outcomes[w] for w in C})>1


def universally_legitimate(e,C):
    return all(w in e.legitimate for w in C)


def common_legitimate_evidence(case,C=None):
    C=case.worlds if C is None else tuple(C)
    if incompatible_pairs(case,C)==0: return 0.0
    xs=[e.cost for e in case.experiments if informative(e,C) and universally_legitimate(e,C)]
    return min(xs) if xs else inf


def cheapest_unresolved(case):
    best=None
    for e in case.experiments:
        if not universally_legitimate(e,case.worlds) or not informative(e,case.worlds): continue
        branches={o:tuple(w for w in case.worlds if e.outcomes[w]==o) for o in set(e.outcomes.values())}
        bad=[incompatible_pairs(case,B) for B in branches.values() if incompatible_pairs(case,B)>0]
        if bad:
            row=(e.cost,e.name,max(bad))
            if best is None or row<best: best=row
    if best is None:return None
    return {"name":best[1],"cost":best[0],"worst_incompatible_pairs":best[2]}


def matched_pair(n=100):
    rs=tuple(f"r{i}" for i in range(n)); ws=tuple(f"w{i}" for i in range(n)); W=rs+ws
    D={w:("R" if w.startswith("r") else "W") for w in W}
    qout={w:("special" if w=="r0" else "rest") for w in W}
    q=Experiment("q",1.0,qout,frozenset(W))
    rest=tuple(w for w in W if w!="r0")
    rout={w:D[w] for w in W}
    common=Experiment("r",2.0,rout,frozenset(rest))
    # B has equally cheap world-specific legitimate resolvers but no common resolver.
    locals_=tuple(Experiment(f"r_{w}",2.0,rout,frozenset({w})) for w in rest)
    A=CLECase(W,D,(q,common)); B=CLECase(W,D,(q,)+locals_)
    return A,B
