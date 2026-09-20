from safesep.revocation_frontier import (
    blocking_witnesses,
    requirement_disjoint_revocation,
)


def test_irrelevant_revocation_is_locally_commutation_safe():
    req = {"sense": {"camera"}, "resolve": {"resolver"}}
    assert requirement_disjoint_revocation({"legacy"}, req)
    assert blocking_witnesses({"legacy"}, req) == {}


def test_revoking_future_requirement_is_rejected():
    req = {"resolve": {"x"}, "audit": {"receipt"}}
    assert not requirement_disjoint_revocation({"x"}, req)
    assert blocking_witnesses({"x"}, req) == {"resolve": frozenset({"x"})}


def test_multiple_tokens_and_arbitrary_probe_names():
    req = {"p": {"a", "b"}, "q": {"c"}, "r": set()}
    assert not requirement_disjoint_revocation({"b", "z"}, req)
    assert blocking_witnesses({"b", "z"}, req) == {"p": frozenset({"b"})}


def test_blocking_witnesses_accepts_one_shot_requirement_iterables():
    req = {"resolve": iter(["x"])}
    assert blocking_witnesses({"x"}, req) == {"resolve": frozenset({"x"})}
