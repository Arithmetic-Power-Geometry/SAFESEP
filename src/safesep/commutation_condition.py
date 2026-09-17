"""Authorization-specific commutation conditions for SAFESEP.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Apache-2.0.

This module makes the MCAS normal-form assumptions explicit as local
commutation obligations.  It is deliberately conservative: passing the
checker is a sufficient structural certificate for the existing closure-first
normal form, not a claim that every system outside the class is unresolvable.
"""
from .closure_exactness import compare_solvers, is_authority_only


def commutation_obligations(probes):
    """Return named obligations and whether each is satisfied.

    Current Probe semantics already encode world-independent requirements and
    grants and have no revocation field.  The nontrivial obligation checked
    here is separation of authority progress from informative sensing.
    """
    return {
        "monotone_authority": all(not hasattr(p, "revokes") for p in probes),
        "world_independent_authority": all(not isinstance(getattr(p, "grants", None), tuple) for p in probes),
        "authority_progress_is_observation_constant": all(is_authority_only(p) or not p.grants for p in probes),
    }


def commutation_certificate(probes):
    o=commutation_obligations(probes)
    return all(o.values()), o


def certified_compare(worlds, decisions, probes, tokens=frozenset()):
    """Compare closure-first and exact search and expose certificate status."""
    cert, obligations=commutation_certificate(probes)
    closure, exact=compare_solvers(worlds, decisions, probes, tokens)
    return {"certified":cert,"obligations":obligations,"closure_first":closure,"exact":exact,"agree":closure==exact}
