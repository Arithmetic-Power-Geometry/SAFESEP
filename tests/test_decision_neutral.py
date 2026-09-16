from safesep.decision_neutral import (
    NeutralProbe,
    cheapest_neutral_probe_leaving_incompatibility,
    neutral_safe_separable,
)


def construction(n=20):
    # n R-worlds and n W-worlds.  Probe q is cheap and informative but still
    # leaves incompatible worlds. Probe resolve perfectly separates R/W.
    worlds = frozenset([f"r{i}" for i in range(n)] + [f"w{i}" for i in range(n)])
    decisions = {w: ("R" if w.startswith("r") else "W") for w in worlds}
    q_out = {w: ("special" if w == "r0" else "rest") for w in worlds}
    resolve_out = {w: decisions[w] for w in worlds}
    q = NeutralProbe("q", 1.0, q_out, {w: True for w in worlds})

    # Extensional authorization can permit the resolver in every actual world,
    # while the justification is decision-dependent.  The neutral model records
    # that it cannot be invoked without presupposing the disputed R/W decision.
    resolve_non_neutral = NeutralProbe(
        "resolve", 1.0, resolve_out, {w: False for w in worlds}
    )
    resolve_neutral = NeutralProbe(
        "resolve", 1.0, resolve_out, {w: True for w in worlds}
    )
    return worlds, decisions, q, resolve_non_neutral, resolve_neutral


def test_21_cheapest_neutral_probe_leaves_mutually_incompatible_worlds():
    worlds, decisions, q, blocked, _ = construction(100)
    p = cheapest_neutral_probe_leaving_incompatibility(worlds, decisions, [q, blocked])
    assert p is not None
    assert p.name == "q"
    assert p.cost == 1.0


def test_22_same_information_different_justificatory_independence_changes_closure():
    worlds, decisions, q, blocked, neutral = construction(50)
    # Same worlds, decisions, outcomes, costs and information structure.
    # Only the decision-independence of the resolver's authorization basis differs.
    assert not neutral_safe_separable(worlds, decisions, [q, blocked])
    assert neutral_safe_separable(worlds, decisions, [q, neutral])


def test_23_scale_to_10000_worlds_without_pair_enumeration():
    worlds, decisions, q, blocked, neutral = construction(5000)
    assert len(worlds) == 10000
    p = cheapest_neutral_probe_leaving_incompatibility(worlds, decisions, [q, blocked])
    assert p.name == "q"
    assert not neutral_safe_separable(worlds, decisions, [q, blocked])
    assert neutral_safe_separable(worlds, decisions, [q, neutral])
