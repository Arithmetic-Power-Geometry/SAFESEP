"""Significant collision tests: DNAC versus proof-dependency checking."""
from safesep.decision_neutral import NeutralProbe, neutral_safe_separable
from safesep.proof_neutral import ProofBasis, compile_neutrality_by_world, probe_has_neutral_proof


def instance(n=100):
    worlds = frozenset([f"r{i}" for i in range(n)] + [f"w{i}" for i in range(n)])
    decisions = {w: ("R" if w.startswith("r") else "W") for w in worlds}
    q_out = {w: ("special" if w == "r0" else "rest") for w in worlds}
    resolve_out = {w: decisions[w] for w in worlds}
    disputed = {"decision:R", "decision:W"}
    return worlds, decisions, q_out, resolve_out, disputed


def test_24_all_resolver_proofs_tainted_reproduces_dnac_obstruction():
    worlds, decisions, q_out, resolve_out, disputed = instance(100)
    proofs = {
        "q": [ProofBasis("public_basis", frozenset({"public:metadata"}))],
        "resolve": [
            ProofBasis("assume_R", frozenset({"decision:R"})),
            ProofBasis("assume_W", frozenset({"decision:W"})),
        ],
    }
    q = NeutralProbe("q", 1.0, q_out, compile_neutrality_by_world("q", worlds, proofs, disputed))
    resolve = NeutralProbe("resolve", 1.0, resolve_out, compile_neutrality_by_world("resolve", worlds, proofs, disputed))
    assert not probe_has_neutral_proof("resolve", proofs, disputed)
    assert not neutral_safe_separable(worlds, decisions, [q, resolve])


def test_25_one_independent_alternative_proof_restores_resolution():
    worlds, decisions, q_out, resolve_out, disputed = instance(100)
    proofs = {
        "q": [ProofBasis("public_basis", frozenset({"public:metadata"}))],
        "resolve": [
            ProofBasis("circular", frozenset({"decision:R"})),
            ProofBasis("independent_consent", frozenset({"consent:probe"})),
        ],
    }
    q = NeutralProbe("q", 1.0, q_out, compile_neutrality_by_world("q", worlds, proofs, disputed))
    resolve = NeutralProbe("resolve", 1.0, resolve_out, compile_neutrality_by_world("resolve", worlds, proofs, disputed))
    assert probe_has_neutral_proof("resolve", proofs, disputed)
    assert neutral_safe_separable(worlds, decisions, [q, resolve])


def test_26_proof_dependency_compilation_scales_to_10000_worlds():
    worlds, decisions, q_out, resolve_out, disputed = instance(5000)
    blocked_proofs = {
        "q": [ProofBasis("public_basis", frozenset({"public:metadata"}))],
        "resolve": [ProofBasis("decision_tainted", frozenset({"decision:R"}))],
    }
    q = NeutralProbe("q", 1.0, q_out, compile_neutrality_by_world("q", worlds, blocked_proofs, disputed))
    resolve = NeutralProbe("resolve", 1.0, resolve_out, compile_neutrality_by_world("resolve", worlds, blocked_proofs, disputed))
    assert len(worlds) == 10000
    assert not neutral_safe_separable(worlds, decisions, [q, resolve])
