from itertools import product
from safesep.world_indexed_brac import WIProbe, exact_resolvable, wi_brac_resolvable

E=frozenset()
D=("deny","allow")
I=(E,E)
outs=list(product("01", repeat=2))
grants=list(product((E,frozenset({"x"})), repeat=2))
reqs=(E,frozenset({"x"}))
checked=0
for o1,o2,g1,g2,r1,r2 in product(outs,outs,grants,grants,reqs,reqs):
    ps=(WIProbe("p1",tuple(o1),r1,tuple(g1)), WIProbe("p2",tuple(o2),r2,tuple(g2)))
    if exact_resolvable(D,ps,I) != wi_brac_resolvable(D,ps,I):
        raise SystemExit(f"COUNTEREXAMPLE: {ps}")
    checked += 1
print(f"WI-BRAC exact agreement: {checked} systems")
