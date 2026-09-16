"""Dynamic branch-relative authorization-cut certificates.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

A certificate is evaluated on joint states (compatible worlds, authority tokens).
It is intentionally a sufficient impossibility certificate, not a new planner.
"""
from dataclasses import dataclass
from typing import FrozenSet, Mapping, Sequence, Tuple

World = str
Pair = Tuple[World, World]

@dataclass(frozen=True)
class Probe:
    name: str
    cost: float
    outcomes: Mapping[World, str]
    requires: FrozenSet[str] = frozenset()
    grants: Mapping[str, FrozenSet[str]] | None = None

@dataclass(frozen=True)
class Problem:
    worlds: Tuple[World, ...]
    decisions: Mapping[World, str]
    probes: Sequence[Probe]
    initial_tokens: FrozenSet[str] = frozenset()


def incompatible_pairs(P: Problem, C: FrozenSet[World]):
    xs = sorted(C)
    return frozenset((a,b) for i,a in enumerate(xs) for b in xs[i+1:]
                     if P.decisions[a] != P.decisions[b])


def executable(e: Probe, tokens: FrozenSet[str]) -> bool:
    return e.requires.issubset(tokens)


def separates(e: Probe, pair: Pair) -> bool:
    a,b = pair
    return e.outcomes[a] != e.outcomes[b]


def branches(e: Probe, C: FrozenSet[World]):
    outs = sorted({e.outcomes[w] for w in C})
    return [(o, frozenset(w for w in C if e.outcomes[w] == o)) for o in outs]


def next_tokens(e: Probe, outcome: str, tokens: FrozenSet[str]):
    if not e.grants:
        return tokens
    return tokens | e.grants.get(outcome, frozenset())


def cheapest_unresolved(P: Problem, C=None, tokens=None):
    C = frozenset(P.worlds) if C is None else frozenset(C)
    tokens = P.initial_tokens if tokens is None else frozenset(tokens)
    candidates=[]
    for e in P.probes:
        if not executable(e,tokens):
            continue
        bs=branches(e,C)
        if len(bs)<2:
            continue
        unresolved=[B for _,B in bs if incompatible_pairs(P,B)]
        if unresolved:
            candidates.append((e.cost,e.name,max(len(incompatible_pairs(P,B)) for B in unresolved)))
    if not candidates:
        return None
    c,n,w=min(candidates)
    return {"name":n,"cost":c,"worst_incompatible_pairs":w}


def reachable_without(P: Problem, forbidden: FrozenSet[str]):
    """Enumerate joint states reachable without using forbidden probes."""
    root=(frozenset(P.worlds),P.initial_tokens)
    seen={root}; stack=[root]
    while stack:
        C,tokens=stack.pop()
        for e in P.probes:
            if e.name in forbidden or not executable(e,tokens):
                continue
            bs=branches(e,C)
            if len(bs)<2:
                continue
            for o,B in bs:
                s=(B,next_tokens(e,o,tokens))
                if s not in seen:
                    seen.add(s); stack.append(s)
    return seen


def dynamic_cut_certificate(P: Problem, cut: FrozenSet[str]):
    """Sufficient obstruction certificate.

    Conditions:
    1) every decision-incompatible pair is separable only by probes in `cut`;
    2) no cut probe is executable in any decision-critical state reachable without cut.

    If both hold, autonomous resolution is impossible: any resolving policy must first
    use a cut probe, but no cut probe can be the first such probe.
    """
    root=frozenset(P.worlds)
    I=incompatible_pairs(P,root)
    noncut=[e for e in P.probes if e.name not in cut]
    mandatory=all(not any(separates(e,p) for e in noncut) for p in I)
    states=reachable_without(P,cut)
    blocked=True
    critical_states=0
    for C,tokens in states:
        if not incompatible_pairs(P,C):
            continue
        critical_states += 1
        if any(e.name in cut and executable(e,tokens) for e in P.probes):
            blocked=False; break
    return {"certificate": mandatory and blocked,
            "mandatory_cut": mandatory,
            "blocked_before_cut": blocked,
            "reachable_critical_states_without_cut": critical_states,
            "root_incompatible_pairs": len(I)}


def witness(n=100, blocked=True):
    """2n worlds. q is cheapest and leaves an incompatible residual branch.

    q grants alpha on the residual branch only in the open system. Resolver r
    requires alpha and is the only probe that separates every R/W pair.
    """
    rs=tuple(f"r{i}" for i in range(n)); ws=tuple(f"w{i}" for i in range(n))
    W=rs+ws; D={w:("R" if w.startswith("r") else "W") for w in W}
    qout={w:("special" if w=="r0" else "rest") for w in W}
    rout={w:D[w] for w in W}
    grants={"special":frozenset(),"rest":frozenset() if blocked else frozenset({"alpha"})}
    q=Probe("q",1.0,qout,frozenset(),grants)
    r=Probe("r",1.0,rout,frozenset({"alpha"}),{})
    return Problem(W,D,(q,r))
