import random
from safesep.dynamic_pair_flow import Probe, family, cheapest_unresolved
from safesep.closure_exactness import compare_solvers
from safesep.commutation_condition import commutation_certificate, certified_compare


def tiny(n):
    # Probe.outcome indexes worlds by the numeric suffix, so use unique w0..w(2n-1)
    # identifiers.  Earlier r0/r1/w0/w1 aliases mapped r0 and w0 to the same
    # outcome slot and made valid authority tests appear unresolved.
    W=tuple(f'w{i}' for i in range(2*n))
    d={w:('R' if i<n else 'W') for i,w in enumerate(W)}
    return W,d


def decision_outcomes(W,d):
    return tuple(d[w] for w in W)


def chain(n, W=None, d=None):
    W,d = tiny(2) if W is None else (W,d)
    ps=[]
    for i in range(n):
        req=frozenset() if i==0 else frozenset({f't{i-1}'})
        ps.append(Probe(f'a{i}',1,('same',)*len(W),req,frozenset({f't{i}'})))
    ps.append(Probe('k',1,decision_outcomes(W,d),frozenset({f't{n-1}'})))
    return tuple(ps)


def test_227_empty_probe_set_certified(): assert commutation_certificate(())[0]
def test_228_pure_sensing_certified(): assert commutation_certificate((Probe('s',1,('0','1')),))[0]
def test_229_authority_only_grant_certified(): assert commutation_certificate((Probe('a',1,('x','x'),grants=frozenset({'t'})),))[0]
def test_230_informative_grant_rejected(): assert not commutation_certificate((Probe('s',1,('0','1'),grants=frozenset({'t'})),))[0]
def test_231_chain_one_agrees():
    W,d=tiny(2); p=chain(1,W,d); assert certified_compare(W,d,p)['agree']
def test_232_chain_two_agrees():
    W,d=tiny(2); p=chain(2,W,d); assert certified_compare(W,d,p)['agree']
def test_233_chain_eight_agrees():
    W,d=tiny(2); p=chain(8,W,d); assert certified_compare(W,d,p)['agree']
def test_234_missing_chain_token_blocks_both():
    W,d=tiny(2); p=(Probe('k',1,decision_outcomes(W,d),frozenset({'z'})),); assert compare_solvers(W,d,p)==(False,False)
def test_235_initial_token_resolves_both():
    W,d=tiny(2); p=(Probe('k',1,decision_outcomes(W,d),frozenset({'z'})),); assert compare_solvers(W,d,p,frozenset({'z'}))==(True,True)
def test_236_redundant_authority_grant_harmless():
    W,d=tiny(2); p=(Probe('a',1,('s',)*len(W),grants=frozenset({'x'})),Probe('b',1,('s',)*len(W),grants=frozenset({'x'})),Probe('k',1,decision_outcomes(W,d),frozenset({'x'}))); assert compare_solvers(W,d,p)==(True,True)
def test_237_authority_cycle_unseeded_blocks():
    W,d=tiny(2); p=(Probe('a',1,('s',)*len(W),frozenset({'y'}),frozenset({'x'})),Probe('b',1,('s',)*len(W),frozenset({'x'}),frozenset({'y'})),Probe('k',1,decision_outcomes(W,d),frozenset({'x'}))); assert compare_solvers(W,d,p)==(False,False)
def test_238_authority_cycle_seeded_resolves():
    W,d=tiny(2); p=(Probe('a',1,('s',)*len(W),frozenset({'y'}),frozenset({'x'})),Probe('b',1,('s',)*len(W),frozenset({'x'}),frozenset({'y'})),Probe('k',1,decision_outcomes(W,d),frozenset({'x'}))); assert compare_solvers(W,d,p,frozenset({'y'}))==(True,True)
def test_239_action_order_invariance():
    W,d=tiny(2); p=chain(3,W,d); assert compare_solvers(W,d,p)==compare_solvers(W,d,tuple(reversed(p)))
def test_240_world_renaming_invariance():
    W,d=tiny(2); p=chain(2,W,d); assert compare_solvers(W,d,p)==(True,True)
def test_241_random_certified_250():
    rng=random.Random(227241); W,d=tiny(3)
    for z in range(250):
        ps=[]
        for j in range(4):
            if rng.random()<.5:
                g=frozenset({f't{j}'}) if rng.random()<.7 else frozenset(); outs=('s',)*len(W)
            else:
                g=frozenset(); outs=tuple(str(rng.randrange(2)) for _ in W)
            ps.append(Probe(f'p{j}',1,outs,grants=g))
        assert commutation_certificate(tuple(ps))[0]
        assert certified_compare(W,d,tuple(ps))['agree']
def test_242_random_certified_1000():
    rng=random.Random(227242); W,d=tiny(2)
    for z in range(1000):
        a=Probe('a',1,('s',)*len(W),grants=frozenset({'x'}) if rng.random()<.5 else frozenset())
        k=Probe('k',1,tuple(rng.choice(('0','1')) for _ in W))
        assert certified_compare(W,d,(a,k))['agree']
def test_243_out_of_class_not_claimed_impossible():
    p=(Probe('s',1,('0','1'),grants=frozenset({'x'})),); assert commutation_certificate(p)[0] is False
def test_244_certificate_exposes_failed_obligation():
    p=(Probe('s',1,('0','1'),grants=frozenset({'x'})),); ok,o=commutation_certificate(p); assert not o['authority_progress_is_observation_constant']
def test_245_scale_200_cheapest():
    W,d,p=family(100,True); x=cheapest_unresolved(W,d,p); assert (x['name'],x['cost'],x['worst_incompatible_pairs'])==('q',1,9900)
def test_246_scale_1000_cheapest():
    W,d,p=family(500,True); x=cheapest_unresolved(W,d,p); assert (x['name'],x['cost'],x['worst_incompatible_pairs'])==('q',1,249500)
def test_247_scale_2000_cheapest():
    W,d,p=family(1000,True); x=cheapest_unresolved(W,d,p); assert x['worst_incompatible_pairs']==999000
def test_248_scale_5000_cheapest():
    W,d,p=family(2500,True); x=cheapest_unresolved(W,d,p); assert x['worst_incompatible_pairs']==6247500
def test_249_scale_10000_cheapest():
    W,d,p=family(5000,True); x=cheapest_unresolved(W,d,p); assert (x['name'],x['cost'],x['worst_incompatible_pairs'])==('q',1,24995000)
def test_250_certificate_is_sufficient_not_necessary_label():
    # A rejected system may still happen to agree on a particular instance.
    W=('w0','w1'); d={'w0':'R','w1':'W'}; p=(Probe('s',1,('R','W'),grants=frozenset({'x'})),); r=certified_compare(W,d,p); assert not r['certified'] and r['agree']
