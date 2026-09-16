"""Tests 85-86: token-only transition soundness regression."""
from safesep.dynamic_authority_cut import Probe, Problem, dynamic_cut_certificate, resolvable_without
from safesep.certificate_pruning import full_joint_search


def credential_problem(include_noop=False):
    W=("r0","w0")
    D={"r0":"R","w0":"W"}
    same={w:"same" for w in W}
    decision={w:D[w] for w in W}
    fetch=Probe("credential_fetch",1.0,same,frozenset(),{"same":frozenset({"alpha"})})
    resolver=Probe("r",1.0,decision,frozenset({"alpha"}),{})
    probes=[fetch,resolver]
    if include_noop:
        probes.insert(0,Probe("noop",0.0,same,frozenset(),{}))
    return Problem(W,D,tuple(probes))


def test_85_token_only_credential_fetch_invalidates_false_deadlock_certificate():
    P=credential_problem()
    cert=dynamic_cut_certificate(P,frozenset({"r"}))
    # Removing r still prevents final resolution, so r is mandatory; however the
    # one-outcome credential fetch reaches alpha and makes r executable.
    assert cert["mandatory_cut"] is True
    assert cert["blocked_before_cut"] is False
    assert cert["certificate"] is False
    assert full_joint_search(P)["resolvable"] is True


def test_86_true_noop_is_skipped_without_loop_or_semantic_change():
    base=credential_problem(False)
    noop=credential_problem(True)
    assert full_joint_search(base)["resolvable"] is True
    assert full_joint_search(noop)["resolvable"] is True
    assert dynamic_cut_certificate(base,frozenset({"r"}))["certificate"] is False
    assert dynamic_cut_certificate(noop,frozenset({"r"}))["certificate"] is False
    assert resolvable_without(noop,frozenset({"r"})) is False
