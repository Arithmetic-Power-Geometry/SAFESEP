import random
from safesep.world_indexed_brac import WIProbe, exact_resolvable, wi_brac_resolvable

E=frozenset()
rng=random.Random(20260919)
checked=0
for nworlds in (3,4):
    decisions=tuple("allow" if i%2 else "deny" for i in range(nworlds))
    initial=tuple(E for _ in range(nworlds))
    for case in range(1250):
        probes=[]
        for j in range(5):
            outcomes=tuple(str(rng.randrange(3)) for _ in range(nworlds))
            requires=frozenset({"x"}) if rng.random()<0.35 else E
            grants=tuple(frozenset({"x"}) if rng.random()<0.45 else E for _ in range(nworlds))
            probes.append(WIProbe(f"p{j}",outcomes,requires,grants))
        ps=tuple(probes)
        ex=exact_resolvable(decisions,ps,initial)
        wi=wi_brac_resolvable(decisions,ps,initial)
        if ex != wi:
            raise SystemExit(f"COUNTEREXAMPLE n={nworlds} case={case}: {ps}")
        checked += 1
print(f"WI-BRAC randomized exact agreement: {checked} systems")
