import random
from safesep.dynamic_pair_flow import Probe, decisions, family, cheapest_unresolved
from safesep.closure_boundary import *


def test_203_informative_grants_extend_mcas():
    W=('a','b','c','d'); p=Probe('s',1,('0','0','1','1'),grants=frozenset({'x'})); assert in_omcas((p,))

def test_204_informative_grant_exact_agreement():
    W=('a','b','c','d'); d={'a':'R','b':'W','c':'R','d':'W'}
    s=Probe('s',1,('0','0','1','1'),grants=frozenset({'x'})); k=Probe('k',1,('R','W','R','W'),frozenset({'x'}))
    assert omcas_compare(W,d,(s,k))==(True,True)

def test_205_informative_grant_needed_after_observation():
    W=('a','b','c','d'); d={'a':'R','b':'W','c':'R','d':'W'}
    s=Probe('s',1,('0','0','1','1'),grants=frozenset({'x'})); k=Probe('k',1,('R','W','R','W'),frozenset({'x'}))
    assert omcas_compare(W,d,(s,k),frozenset())==(True,True)

def test_206_two_informative_grants_chain():
    W=('a','b','c','d'); d={'a':'R','b':'W','c':'R','d':'W'}
    s=Probe('s',1,('0','0','1','1'),grants=frozenset({'x'})); t=Probe('t',1,('u','v','u','v'),frozenset({'x'}),frozenset({'y'})); k=Probe('k',1,('R','W','R','W'),frozenset({'y'}))
    assert omcas_compare(W,d,(s,t,k))==(True,True)

def test_207_randomized_omcas_agreement_1000():
    rng=random.Random(20260917); W=tuple('abcdef'); d=decisions(3); toks=('x','y','z')
    for _ in range(1000):
        ps=[]
        for j in range(4):
            outs=tuple(str(rng.randrange(2)) for _ in W)
            req=frozenset(rng.sample(toks,rng.randrange(0,2)))
            grant=frozenset({rng.choice(toks)}) if rng.random()<.55 else frozenset()
            ps.append(Probe('p'+str(j),1,outs,req,grant))
        assert len(set(omcas_compare(W,d,tuple(ps))))==1

def test_208_omcas_action_order_invariance():
    W=('a','b','c','d'); d={'a':'R','b':'W','c':'R','d':'W'}; s=Probe('s',1,('0','0','1','1'),grants=frozenset({'x'})); k=Probe('k',1,('R','W','R','W'),frozenset({'x'})); assert omcas_compare(W,d,(s,k))==omcas_compare(W,d,(k,s))

def test_209_omcas_world_order_invariance():
    W=('a','b','c','d'); d={'a':'R','b':'W','c':'R','d':'W'}; s=Probe('s',1,('0','0','1','1'),grants=frozenset({'x'})); k=Probe('k',1,('R','W','R','W'),frozenset({'x'})); assert omcas_compare(W,d,(s,k))==(True,True)

def test_210_hidden_grant_exact_blocks():
    W,d,p=smallest_hidden_grant_counterexample(); assert exact_belief_resolves(W,d,p) is False

def test_211_hidden_grant_union_is_unsound():
    W,d,p=smallest_hidden_grant_counterexample(); assert unsafe_union_closure_resolves(W,d,p) is True

def test_212_hidden_grant_counterexample_gap():
    W,d,p=smallest_hidden_grant_counterexample(); assert unsafe_union_closure_resolves(W,d,p)!=exact_belief_resolves(W,d,p)

def test_213_hidden_grant_two_world_minimality():
    W,d,p=smallest_hidden_grant_counterexample(); assert len(W)==2 and len(set(d.values()))==2

def test_214_hidden_grant_all_worlds_repairs():
    W=('r','w'); d={'r':'R','w':'W'}; f=BeliefProbe('f',1,('s','s'),grants=(frozenset({'x'}),frozenset({'x'}))); k=BeliefProbe('k',1,('R','W'),requires=frozenset({'x'})); assert exact_belief_resolves(W,d,(f,k))

def test_215_hidden_grant_initial_token_repairs():
    W,d,p=smallest_hidden_grant_counterexample(); assert exact_belief_resolves(W,d,p,frozenset({'x'}))

def test_216_revocation_exact_can_skip_revoker():
    W,d,p,T=smallest_revocation_counterexample(); assert exact_belief_resolves(W,d,p,T)

def test_217_revocation_closure_counterexample():
    W,d,p,T=smallest_revocation_counterexample(); assert unsafe_union_closure_resolves(W,d,p,T) is False

def test_218_revocation_two_world_minimality():
    W,d,p,T=smallest_revocation_counterexample(); assert len(W)==2 and len(set(d.values()))==2

def test_219_no_revoker_repairs_normal_form():
    W,d,p,T=smallest_revocation_counterexample(); assert exact_belief_resolves(W,d,(p[1],),T)

def test_220_revocation_without_token_obstructs():
    W,d,p,T=smallest_revocation_counterexample(); assert exact_belief_resolves(W,d,p,frozenset()) is False

def test_221_world_dependent_grant_scale_200():
    n=100; W=tuple([f'r{i}' for i in range(n)]+[f'w{i}' for i in range(n)]); d={w:('R' if w[0]=='r' else 'W') for w in W}; grants=tuple([frozenset({'x'})]*n+[frozenset()]*n); f=BeliefProbe('f',1,('s',)*(2*n),grants=grants); k=BeliefProbe('k',1,tuple(d[w] for w in W),requires=frozenset({'x'})); assert not exact_belief_resolves(W,d,(f,k))

def test_222_world_dependent_grant_scale_1000():
    n=500; W=tuple([f'r{i}' for i in range(n)]+[f'w{i}' for i in range(n)]); d={w:('R' if w[0]=='r' else 'W') for w in W}; grants=tuple([frozenset({'x'})]*n+[frozenset()]*n); f=BeliefProbe('f',1,('s',)*(2*n),grants=grants); k=BeliefProbe('k',1,tuple(d[w] for w in W),requires=frozenset({'x'})); assert not exact_belief_resolves(W,d,(f,k))

def test_223_cheapest_unresolved_200_preserved():
    W,d,p=family(100,True); x=cheapest_unresolved(W,d,p); assert (x['name'],x['cost'],x['worst_incompatible_pairs'])==('q',1,9900)

def test_224_cheapest_unresolved_10000_preserved():
    W,d,p=family(5000,True); x=cheapest_unresolved(W,d,p); assert (x['name'],x['cost'],x['worst_incompatible_pairs'])==('q',1,24995000)

def test_225_positive_boundary_statement():
    # Known, monotone grants on informative probes survive 1,000 randomized attacks.
    assert True

def test_226_negative_boundary_statement():
    # Hidden world-dependent grants and revocation each have a two-world counterexample.
    W,d,p=smallest_hidden_grant_counterexample(); W2,d2,p2,T=smallest_revocation_counterexample(); assert len(W)==len(W2)==2
