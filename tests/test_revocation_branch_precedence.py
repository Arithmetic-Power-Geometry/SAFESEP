from safesep.revocation_exact import RevProbe, exact_revocation_resolves
from safesep.revocation_order import has_acyclic_separator_cover


def test_global_precedence_cycle_can_be_harmless_after_branch_split():
    # r separates the two regions. p is needed only on {0,1}; q only on {2,3}.
    # p and q destroy each other's authority, so the global precedence graph cycles,
    # but no execution branch ever needs both.
    W = frozenset({0, 1, 2, 3})
    D = {0: "A", 1: "B", 2: "C", 3: "D"}
    A = frozenset({"x", "y"})
    probes = (
        RevProbe("r", ((0, 0), (1, 0), (2, 1), (3, 1))),
        RevProbe(
            "p", ((0, 0), (1, 1), (2, 0), (3, 0)),
            frozenset({"x"}), revokes=frozenset({"y"})
        ),
        RevProbe(
            "q", ((0, 0), (1, 0), (2, 0), (3, 1)),
            frozenset({"y"}), revokes=frozenset({"x"})
        ),
    )
    assert not has_acyclic_separator_cover(W, D, probes, A)
    assert exact_revocation_resolves(W, D, probes, A)
