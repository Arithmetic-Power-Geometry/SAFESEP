"""Dynamic legitimate-pair-flow certificates for SAFESEP.

The module tracks decision-incompatible pairs together with authority tokens.  It
provides a sound *cut* certificate: if every complete resolution must cross a
set K of probes, but no K probe is branchwise legitimate in any decision-
critical joint state reachable without K, safe resolution is impossible.

This is intentionally a certificate/lower-bound layer, not a claim that joint
state planning itself is new.
"""
from dataclasses import dataclass
from itertools import product

@dataclass(frozen=True)
class Probe:
    name: str
    cost: float
    outcomes: tuple
    requires: frozenset = frozenset()
    grants: frozenset = frozenset()

    def outcome(self, w):
        return self.outcomes[int(w[1:])]


def decisions(n):
    return {f"w{i}": ("R" if i < n else "W") for i in range(2*n)}


def incompatible_pair_count(C, d):
    r=sum(d[w]=="R" for w in C); z=len(C)-r
    return r*z


def branchwise_legitimate(e, tokens):
    return e.requires <= tokens


def children(e, C, tokens):
    buckets={}
    for w in C: buckets.setdefault(e.outcome(w), []).append(w)
    nt=frozenset(set(tokens)|set(e.grants))
    return [(tuple(v),nt) for v in buckets.values()]


def cheapest_unresolved(C,d,probes,tokens=frozenset()):
    best=None
    for e in probes:
        if not branchwise_legitimate(e,tokens): continue
        bs=children(e,C,tokens)
        if len(bs)<2: continue
        worst=max(incompatible_pair_count(c,d) for c,_ in bs)
        if worst<=0: continue
        row=(e.cost,e.name,worst)
        if best is None or row<best: best=row
    return None if best is None else {"name":best[1],"cost":best[0],"worst_incompatible_pairs":best[2]}


def reachable_without(C,d,probes,cut):
    """Finite BFS over joint (belief,tokens), excluding cut probes."""
    start=(tuple(C),frozenset()); q=[start]; seen={start}
    while q:
        state=q.pop(0); yield state
        B,T=state
        for e in probes:
            if e.name in cut or not branchwise_legitimate(e,T): continue
            for ch in children(e,B,T):
                if ch==state: continue
                if ch not in seen: seen.add(ch); q.append(ch)


def cut_blocked(C,d,probes,cut):
    """True when no cut probe is legitimate in any reachable critical state."""
    by={e.name:e for e in probes}
    for B,T in reachable_without(C,d,probes,cut):
        if incompatible_pair_count(B,d)==0: continue
        if any(branchwise_legitimate(by[k],T) for k in cut): return False
    return True


def family(n=100, open_case=True):
    """Matched information family with a token-only transition.

    q isolates w0 and leaves the large incompatible rest branch.  resolver k
    perfectly separates decisions but requires alpha.  OPEN has fetch_alpha;
    BLOCKED has a same-cost true no-op fetch_dummy.  Thus raw q/k information
    is matched while authority-flow reachability differs.
    """
    W=tuple(f"w{i}" for i in range(2*n)); d=decisions(n)
    qout=tuple("special" if i==0 else "rest" for i in range(2*n))
    kout=tuple("R" if i<n else "W" for i in range(2*n))
    same=tuple("same" for _ in W)
    q=Probe("q",1.0,qout)
    k=Probe("k",1.0,kout,frozenset({"alpha"}))
    fetch=Probe("fetch",1.0,same,grants=frozenset({"alpha"}) if open_case else frozenset())
    return W,d,(q,fetch,k)


def analytic_large(n):
    return {"worlds":2*n,"q_cost":1.0,"q_worst_pairs":n*(n-1)}
