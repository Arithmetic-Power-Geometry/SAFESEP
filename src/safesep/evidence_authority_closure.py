"""Evidence-authority closure for SAFESEP.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

This module models a recursive authority problem: executing a probe may require
evidence tokens, while acquiring those tokens may itself require authorized
probes.  Closure is computed from an exogenous seed set.  Cycles without a
seed do not self-authorize.
"""
from dataclasses import dataclass
from typing import FrozenSet, Iterable, Mapping, Sequence


@dataclass(frozen=True)
class AuthorityRule:
    probe: str
    requires: FrozenSet[str]


@dataclass(frozen=True)
class EvidenceYield:
    probe: str
    produces: FrozenSet[str]


def authority_closure(
    seed: Iterable[str],
    rules: Sequence[AuthorityRule],
    yields: Mapping[str, FrozenSet[str]],
) -> tuple[FrozenSet[str], FrozenSet[str]]:
    """Least fixed point from externally justified evidence.

    Returns (evidence, executable_probes). A rule fires only when all of its
    requirements are already in the closure. Purely circular support therefore
    cannot bootstrap itself.
    """
    evidence = set(seed)
    executable = set()
    changed = True
    while changed:
        changed = False
        for rule in rules:
            if rule.requires.issubset(evidence) and rule.probe not in executable:
                executable.add(rule.probe)
                before = len(evidence)
                evidence.update(yields.get(rule.probe, frozenset()))
                changed = changed or len(evidence) != before or True
    return frozenset(evidence), frozenset(executable)


def cheapest_executable_leaving_incompatibility(
    executable: Iterable[str], costs: Mapping[str, float], leaves_incompatible: Mapping[str, bool]
):
    """Cheapest executable probe that is known to leave an incompatible branch."""
    candidates = [p for p in executable if leaves_incompatible.get(p, False)]
    return min(candidates, key=lambda p: (costs[p], p), default=None)


def has_resolver(executable: Iterable[str], resolvers: Iterable[str]) -> bool:
    return bool(set(executable).intersection(resolvers))
