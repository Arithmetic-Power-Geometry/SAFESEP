"""World-Indexed Branch-Relative Authority Closure (WI-BRAC).

Research implementation. Authority is tracked separately for each possible world;
world-dependent monotone grants are never unioned across unresolved worlds.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache

@dataclass(frozen=True)
class WIProbe:
    name: str
    outcomes: tuple[str, ...]
    requires: frozenset[str]
    grants: tuple[frozenset[str], ...]

    def __post_init__(self):
        if len(self.outcomes) != len(self.grants):
            raise ValueError("outcomes and grants must have one entry per world")

AuthorityVector = tuple[frozenset[str], ...]

def resolved(branch: frozenset[int], decisions: tuple[str, ...]) -> bool:
    return len({decisions[w] for w in branch}) <= 1

def legitimate(branch: frozenset[int], authority: AuthorityVector, p: WIProbe) -> bool:
    return all(p.requires <= authority[w] for w in branch)

def apply_grants(branch: frozenset[int], authority: AuthorityVector, p: WIProbe) -> AuthorityVector:
    out = list(authority)
    for w in branch:
        out[w] = out[w] | p.grants[w]
    return tuple(out)

def partitions(branch: frozenset[int], p: WIProbe) -> tuple[frozenset[int], ...]:
    buckets: dict[str, set[int]] = {}
    for w in branch:
        buckets.setdefault(p.outcomes[w], set()).add(w)
    return tuple(frozenset(v) for _, v in sorted(buckets.items()))

def branch_constant(branch: frozenset[int], p: WIProbe) -> bool:
    return len({p.outcomes[w] for w in branch}) == 1

def wi_closure(branch: frozenset[int], authority: AuthorityVector,
               probes: tuple[WIProbe, ...]) -> AuthorityVector:
    """Least fixed point of legitimate branch-constant monotone grants."""
    cur = authority
    while True:
        nxt = cur
        for p in probes:
            if branch_constant(branch, p) and legitimate(branch, nxt, p):
                nxt = apply_grants(branch, nxt, p)
        if nxt == cur:
            return cur
        cur = nxt

def exact_resolvable(decisions: tuple[str, ...], probes: tuple[WIProbe, ...],
                     initial: AuthorityVector) -> bool:
    root = frozenset(range(len(decisions)))

    @lru_cache(None)
    def rec(branch: frozenset[int], authority: AuthorityVector) -> bool:
        if resolved(branch, decisions):
            return True
        for p in probes:
            if not legitimate(branch, authority, p):
                continue
            new_a = apply_grants(branch, authority, p)
            kids = partitions(branch, p)
            if len(kids) == 1 and new_a == authority:
                continue
            if all(rec(k, new_a) for k in kids):
                return True
        return False
    return rec(root, initial)

def wi_brac_resolvable(decisions: tuple[str, ...], probes: tuple[WIProbe, ...],
                       initial: AuthorityVector) -> bool:
    root = frozenset(range(len(decisions)))

    @lru_cache(None)
    def rec(branch: frozenset[int], authority: AuthorityVector) -> bool:
        authority = wi_closure(branch, authority, probes)
        if resolved(branch, decisions):
            return True
        for p in probes:
            if branch_constant(branch, p) or not legitimate(branch, authority, p):
                continue
            new_a = apply_grants(branch, authority, p)
            if all(rec(k, new_a) for k in partitions(branch, p)):
                return True
        return False
    return rec(root, initial)
