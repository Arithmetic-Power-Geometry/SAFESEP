from itertools import product
from safesep.world_indexed_brac import WIProbe, exact_resolvable, wi_brac_resolvable

E=frozenset()

def test_world_dependent_grants_are_not_unsafely_unioned():
    decisions=("deny","allow")
    grant=WIProbe("grant",("same","same"),E,(frozenset({"x"}),E))
    resolver=WIProbe("resolver",("0","1"),frozenset({"x"}),(E,E))
    initial=(E,E)
    assert exact_resolvable(decisions,(grant,resolver),initial) is False
    assert wi_brac_resolvable(decisions,(grant,resolver),initial) is False

def test_world_dependent_extra_grants_can_close_safely():
    decisions=("deny","allow")
    grant=WIProbe("grant",("same","same"),E,
                  (frozenset({"x","a"}),frozenset({"x","b"})))
    resolver=WIProbe("resolver",("0","1"),frozenset({"x"}),(E,E))
    initial=(E,E)
    assert exact_resolvable(decisions,(grant,resolver),initial)
    assert wi_brac_resolvable(decisions,(grant,resolver),initial)

def test_exhaustive_two_world_two_probe_agreement():
    decisions=("deny","allow")
    initial=(E,E)
    outcome_patterns=list(product("01", repeat=2))
    grant_patterns=list(product((E,frozenset({"x"})), repeat=2))
    reqs=(E,frozenset({"x"}))
    checked=0
    for o1,o2,g1,g2,r1,r2 in product(outcome_patterns,outcome_patterns,
                                      grant_patterns,grant_patterns,reqs,reqs):
        p1=WIProbe("p1",tuple(o1),r1,tuple(g1))
        p2=WIProbe("p2",tuple(o2),r2,tuple(g2))
        ex=exact_resolvable(decisions,(p1,p2),initial)
        wi=wi_brac_resolvable(decisions,(p1,p2),initial)
        assert wi == ex, (p1,p2,ex,wi)
        checked += 1
    assert checked == 1024
