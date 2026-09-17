from itertools import product
import random
from safesep.dynamic_pair_flow import Probe, family, decisions, cheapest_unresolved
from safesep.closure_exactness import *


def mk(n=3, grant=True):
    W,d,ps=family(n,open_case=grant)
    return W,d,ps


def test_179_open_exact_agreement():
    W,d,p=mk(5,True); assert compare_solvers(W,d,p)==(True,True)

def test_180_blocked_exact_agreement():
    W,d,p=mk(5,False); assert compare_solvers(W,d,p)==(False,False)

def test_181_open_is_mcas():
    assert in_mcas(mk()[2])

def test_182_blocked_is_mcas():
    assert in_mcas(mk(grant=False)[2])

def test_183_closure_unlocks_alpha():
    W,d,p=mk(); assert 'alpha' in authority_closure(frozenset(),p)

def test_184_noop_closure_stays_empty():
    W,d,p=mk(grant=False); assert authority_closure(frozenset(),p)==frozenset()

def test_185_parameter_agreement():
    for n in range(2,65):
        for g in (False,True):
            W,d,p=mk(n,g); assert len(set(compare_solvers(W,d,p)))==1

def test_186_action_order_invariance():
    W,d,p=mk(8,True); assert compare_solvers(W,d,p)==compare_solvers(W,d,tuple(reversed(p)))

def test_187_world_order_invariance():
    W,d,p=mk(8,True); assert compare_solvers(W,d,p)==compare_solvers(tuple(reversed(W)),d,p)

def test_188_initial_token_boundary():
    W,d,p=mk(8,False); assert compare_solvers(W,d,p,frozenset({'alpha'}))==(True,True)

def test_189_multistep_authority_chain():
    W=tuple(f'w{i}' for i in range(4)); d=decisions(2); same=('x',)*4
    a=Probe('a',1,same,grants=frozenset({'a'})); b=Probe('b',1,same,frozenset({'a'}),frozenset({'b'})); k=Probe('k',1,('R','R','W','W'),frozenset({'b'}))
    assert compare_solvers(W,d,(a,b,k))==(True,True)

def test_190_unseeded_cycle_obstructs():
    W=tuple(f'w{i}' for i in range(4)); d=decisions(2); same=('x',)*4
    a=Probe('a',1,same,frozenset({'b'}),frozenset({'a'})); b=Probe('b',1,same,frozenset({'a'}),frozenset({'b'})); k=Probe('k',1,('R','R','W','W'),frozenset({'a'}))
    assert compare_solvers(W,d,(a,b,k))==(False,False)

def test_191_seeded_cycle_resolves():
    W=tuple(f'w{i}' for i in range(4)); d=decisions(2); same=('x',)*4
    a=Probe('a',1,same,frozenset({'b'}),frozenset({'a'})); b=Probe('b',1,same,frozenset({'a'}),frozenset({'b'})); k=Probe('k',1,('R','R','W','W'),frozenset({'a'}))
    assert compare_solvers(W,d,(a,b,k),frozenset({'b'}))==(True,True)

def test_192_informative_grant_outside_class():
    W=tuple(f'w{i}' for i in range(4)); q=Probe('q',1,('a','a','b','b'),grants=frozenset({'x'})); assert not in_mcas((q,))

def test_193_exhaustive_small_mcas_agreement():
    # Enumerate small authority configurations around a fixed binary decision problem.
    W=tuple(f'w{i}' for i in range(4)); d=decisions(2); same=('s',)*4; kout=('R','R','W','W')
    for ga,gb,reqk in product((False,True),repeat=3):
        a=Probe('a',1,same,grants=frozenset({'a'}) if ga else frozenset())
        b=Probe('b',1,same,frozenset({'a'}),frozenset({'b'}) if gb else frozenset())
        k=Probe('k',1,kout,frozenset({'b'}) if reqk else frozenset())
        ps=(a,b,k); assert in_mcas(ps); assert len(set(compare_solvers(W,d,ps)))==1

def test_194_randomized_mcas_agreement_500():
    rng=random.Random(20260917); W=tuple(f'w{i}' for i in range(6)); d=decisions(3); same=('s',)*6; kout=('R',)*3+('W',)*3
    toks=('a','b','c')
    for _ in range(500):
        ps=[]
        for i,t in enumerate(toks):
            req=frozenset(rng.sample(toks,rng.randrange(0,2)))
            ps.append(Probe('f'+str(i),1,same,req,frozenset({t}) if rng.random()<.7 else frozenset()))
        ps.append(Probe('k',1,kout,frozenset(rng.sample(toks,rng.randrange(0,3)))))
        assert len(set(compare_solvers(W,d,tuple(ps))))==1

def test_195_cheapest_unresolved_200():
    W,d,p=family(100,True); x=cheapest_unresolved(W,d,p); assert x['name']=='q' and x['cost']==1 and x['worst_incompatible_pairs']==9900

def test_196_cheapest_unresolved_1000():
    W,d,p=family(500,True); assert cheapest_unresolved(W,d,p)['worst_incompatible_pairs']==249500

def test_197_cheapest_unresolved_2000():
    W,d,p=family(1000,True); assert cheapest_unresolved(W,d,p)['worst_incompatible_pairs']==999000

def test_198_cheapest_unresolved_5000():
    W,d,p=family(2500,True); assert cheapest_unresolved(W,d,p)['worst_incompatible_pairs']==6247500

def test_199_cheapest_unresolved_10000():
    W,d,p=family(5000,True); x=cheapest_unresolved(W,d,p); assert x['name']=='q' and x['worst_incompatible_pairs']==24995000

def test_200_closure_idempotent():
    W,d,p=mk(); A=authority_closure(frozenset(),p); assert authority_closure(A,p)==A

def test_201_closure_monotone():
    W,d,p=mk(); assert authority_closure(frozenset(),p) <= authority_closure(frozenset({'z'}),p)

def test_202_exactness_class_boundary_recorded():
    # Informative authority-changing actions are deliberately excluded from theorem class.
    W=tuple(f'w{i}' for i in range(4)); e=Probe('e',1,('0','0','1','1'),grants=frozenset({'x'})); assert in_mcas((e,)) is False
