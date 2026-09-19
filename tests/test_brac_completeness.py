from itertools import product

from safesep.branch_relative_closure import brac_resolves
from safesep.closure_exactness import exact_resolves
from safesep.dynamic_pair_flow import Probe
from safesep.monotone_resolution import pairwise_resolvable, reachable_token_closure


def P(name, outcomes, req=False, grant=False):
    return Probe(
        name, 1.0, tuple(outcomes),
        frozenset({"x"}) if req else frozenset(),
        frozenset({"x"}) if grant else frozenset(),
    )


def test_informative_grant_chain_is_captured():
    W=("w0","w1","w2","w3")
    d={"w0":"R","w1":"W","w2":"R","w3":"W"}
    root=P("root",("L","L","R","R"))
    grant=P("grant",("0","1","0","1"),grant=True)
    resolver=P("resolver",("R","W","R","W"),req=True)
    ps=(root,grant,resolver)
    assert pairwise_resolvable(W,d,ps)
    assert brac_resolves(W,d,ps)==exact_resolves(W,d,ps)==True


def test_unreachable_requirement_blocks_pair():
    W=("w0","w1")
    d={"w0":"R","w1":"W"}
    locked=P("locked",("R","W"),req=True)
    assert reachable_token_closure(frozenset(),(locked,))==frozenset()
    assert not pairwise_resolvable(W,d,(locked,))
    assert brac_resolves(W,d,(locked,))==exact_resolves(W,d,(locked,))==False


def test_exhaustive_three_world_two_probe_semantics():
    # 8 binary outcome maps x 2 requirement states x 2 grant states = 32
    # probe types.  All ordered pairs of probe types and all 6 nonconstant
    # binary decision maps are checked: 32^2 * 6 = 6,144 systems.
    W=("w0","w1","w2")
    outcomes=list(product(("0","1"), repeat=3))
    types=[(o,r,g) for o in outcomes for r in (False,True) for g in (False,True)]
    decisions=[
        {w:("R" if bits[i] else "W") for i,w in enumerate(W)}
        for bits in product((0,1), repeat=3)
        if len(set(bits))>1
    ]
    checked=0
    for a in types:
        p0=P("a",*a)
        for b in types:
            p1=P("b",*b)
            ps=(p0,p1)
            for d in decisions:
                poly=pairwise_resolvable(W,d,ps)
                exact=exact_resolves(W,d,ps)
                brac=brac_resolves(W,d,ps)
                assert poly==exact==brac
                checked += 1
    assert checked==6144


def test_decision_labels_are_not_reserved_strings():
    W=("w0","w1","w2")
    d={"w0":"READ","w1":"WRITE","w2":"DELETE"}
    none=()
    assert not pairwise_resolvable(W,d,none)
    assert not exact_resolves(W,d,none)
    assert not brac_resolves(W,d,none)

    identify=P("identify",("0","1","2"))
    assert pairwise_resolvable(W,d,(identify,))
    assert exact_resolves(W,d,(identify,))
    assert brac_resolves(W,d,(identify,))
