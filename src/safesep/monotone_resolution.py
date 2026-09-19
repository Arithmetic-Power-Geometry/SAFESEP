"""Polynomial resolvability criterion for the monotone SAFESEP Probe model.

For the explicit finite-world Probe semantics:
- requirements and grants are world-independent;
- authority changes only by monotone token addition;
- executing a probe never enlarges the compatible-world set.

Under these assumptions, boolean safe resolvability is equivalent to:
(1) compute the least token closure using every authority-reachable probe; and
(2) require every decision-incompatible pair of worlds to be separated by at
    least one probe whose requirements are contained in that closure.

This is a structural simplification of resolvability, not a claim that optimal
costed decision-tree construction is easy.
"""
from .dynamic_pair_flow import incompatible_pair_count


def reachable_token_closure(tokens, probes):
    """Least fixed point of world-independent monotone grants."""
    T = set(tokens)
    changed = True
    while changed:
        changed = False
        for e in probes:
            if e.requires <= T:
                nt = T | set(e.grants)
                if nt != T:
                    T = nt
                    changed = True
    return frozenset(T)


def executable_probes(tokens, probes):
    T = reachable_token_closure(tokens, probes)
    return T, tuple(e for e in probes if e.requires <= T)


def pairwise_resolvable(C, decision, probes, tokens=frozenset()):
    """Polynomial criterion for boolean resolvability."""
    C = tuple(C)
    if incompatible_pair_count(C, decision) == 0:
        return True
    _, enabled = executable_probes(tokens, probes)
    for i, u in enumerate(C):
        for v in C[i + 1:]:
            if decision[u] == decision[v]:
                continue
            if not any(e.outcome(u) != e.outcome(v) for e in enabled):
                return False
    return True


def unresolved_pairs(C, decision, probes, tokens=frozenset()):
    """Return incompatible pairs not separable by any authority-reachable probe."""
    _, enabled = executable_probes(tokens, probes)
    bad = []
    C = tuple(C)
    for i, u in enumerate(C):
        for v in C[i + 1:]:
            if decision[u] != decision[v] and not any(
                e.outcome(u) != e.outcome(v) for e in enabled
            ):
                bad.append((u, v))
    return tuple(bad)
