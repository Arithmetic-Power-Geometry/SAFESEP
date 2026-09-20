"""Behavioral probe-type quotient for SAFESEP-II."""
from __future__ import annotations

from collections.abc import Iterable

from .revocation_exact import RevProbe, World


def probe_type(
    p: RevProbe,
    relevant_worlds: frozenset[World],
    relevant_tokens: frozenset[str],
):
    """Canonical behavior visible to the current normalized state.

    Outcome labels are canonicalized to a partition signature, since only equality
    of outcomes matters for filtering compatible worlds/obligations.
    """
    om = p.outcome_map()
    label_ids = {}
    next_id = 0
    obs = []
    for w in sorted(relevant_worlds, key=repr):
        raw = om[w]
        if raw not in label_ids:
            label_ids[raw] = next_id
            next_id += 1
        obs.append(label_ids[raw])
    return (
        p.requires & relevant_tokens,
        p.grants & relevant_tokens,
        p.revokes & relevant_tokens,
        tuple(obs),
    )


def deduplicate_probe_types(
    probes: tuple[RevProbe, ...],
    relevant_worlds: frozenset[World],
    relevant_tokens: frozenset[str],
) -> tuple[RevProbe, ...]:
    seen = set()
    out = []
    for p in probes:
        t = probe_type(p, relevant_worlds, relevant_tokens)
        if t not in seen:
            seen.add(t)
            out.append(p)
    return tuple(out)
