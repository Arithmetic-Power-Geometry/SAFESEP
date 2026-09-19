import random

from safesep.revocation_dynamic_types import dynamic_type_quotient_resolves
from safesep.revocation_exact import RevProbe, exact_revocation_resolves


def _subset(rng, tokens, p=0.35):
    return frozenset(t for t in tokens if rng.random() < p)


def _random_probe(rng, name, worlds, tokens):
    # 2- or 3-valued deterministic observations.
    arity = rng.choice((2, 3))
    outcomes = tuple((w, rng.randrange(arity)) for w in worlds)
    return RevProbe(
        name,
        outcomes,
        _subset(rng, tokens),
        _subset(rng, tokens),
        _subset(rng, tokens),
    )


def _renamed_duplicate(p, name):
    # Preserve partition while changing raw outcome labels.
    labels = {}
    next_label = 100
    out = []
    for w, o in p.outcomes:
        if o not in labels:
            labels[o] = next_label
            next_label += 7
        out.append((w, labels[o]))
    return RevProbe(name, tuple(out), p.requires, p.grants, p.revokes)


def test_randomized_dynamic_kernel_differential():
    rng = random.Random(20260919)
    checked = 0
    for case in range(2500):
        n = rng.choice((3, 4))
        worlds = tuple(range(n))
        W = frozenset(worlds)
        tokens = ("x", "y", "z")
        A = _subset(rng, tokens, p=0.65)

        # Ensure at least two decision labels while allowing repeats.
        while True:
            D = {w: rng.randrange(min(3, n)) for w in worlds}
            if len(set(D.values())) >= 2:
                break

        m = rng.choice((2, 3, 4))
        probes = [_random_probe(rng, f"p{i}", worlds, tokens) for i in range(m)]

        # In about one third of cases inject an exact behavioral duplicate.
        if rng.random() < 0.34:
            j = rng.randrange(len(probes))
            probes.append(_renamed_duplicate(probes[j], f"dup{j}"))

        probes = tuple(probes)
        exact = exact_revocation_resolves(W, D, probes, A)
        quotient = dynamic_type_quotient_resolves(W, D, probes, A)
        assert quotient == exact, (
            f"case={case} W={W} D={D} A={A} probes={probes} "
            f"exact={exact} quotient={quotient}"
        )
        checked += 1

    assert checked == 2500
