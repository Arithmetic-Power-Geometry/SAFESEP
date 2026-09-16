"""Proof-dependency baseline for decision-neutral authorization.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.

This module intentionally tests whether the current DNAC criterion can be
compiled into ordinary authorization-proof dependency checking.  A probe is
proof-neutral iff at least one valid authorization proof avoids every disputed
decision premise.  This is a baseline/collision model, not a novelty claim.
"""
from dataclasses import dataclass
from typing import FrozenSet, Iterable, Mapping, Sequence


@dataclass(frozen=True)
class ProofBasis:
    name: str
    premises: FrozenSet[str]


def proof_is_decision_neutral(proof: ProofBasis, disputed: Iterable[str]) -> bool:
    """True iff this proof does not depend on any disputed decision premise."""
    return proof.premises.isdisjoint(frozenset(disputed))


def probe_has_neutral_proof(
    probe_name: str,
    proofs: Mapping[str, Sequence[ProofBasis]],
    disputed: Iterable[str],
) -> bool:
    """Existential semantics: one independent proof is sufficient."""
    return any(proof_is_decision_neutral(p, disputed) for p in proofs.get(probe_name, ()))


def compile_neutrality_by_world(
    probe_name: str,
    worlds: Iterable[str],
    proofs: Mapping[str, Sequence[ProofBasis]],
    disputed: Iterable[str],
):
    """Compile proof neutrality to the Boolean map used by NeutralProbe."""
    neutral = probe_has_neutral_proof(probe_name, proofs, disputed)
    return {w: neutral for w in worlds}
