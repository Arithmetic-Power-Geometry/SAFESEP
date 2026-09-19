"""Conservative SAFESEP-II checker for locally commutation-safe revocation.

This is intentionally a sufficient syntactic test, not a completeness solver.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping


def requirement_disjoint_revocation(
    revoked: Iterable[str],
    remaining_requirements: Mapping[str, Iterable[str]],
) -> bool:
    """Return True iff no revoked token is required by any remaining probe."""
    r = frozenset(revoked)
    return all(r.isdisjoint(reqs) for reqs in remaining_requirements.values())


def blocking_witnesses(
    revoked: Iterable[str],
    remaining_requirements: Mapping[str, Iterable[str]],
) -> dict[str, frozenset[str]]:
    """Return probes whose requirements intersect the proposed revocation."""
    r = frozenset(revoked)
    return {
        probe: frozenset(reqs) & r
        for probe, reqs in remaining_requirements.items()
        if frozenset(reqs) & r
    }
