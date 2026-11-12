"""Independent explicit finite-world oracle, not imported from SAFESEP."""
import itertools, random, functools
R=random.Random(20261112)
def solve(ds,obs,req,grants,nq,mode='exact',mcas=False):
 n=len(ds); ne=len(obs); full=(1<<n)-1
 def parts(C,e):
  z={}
  for w in range(n):
   if C>>w&1:z[obs[e][w]]=z.get(obs[e][w],0)|(1<<w)
  return tuple(z.values())
 def closure(C,A):
  while True:
   B=A
   for e in range(ne):
    if (req[e]&A)==req[e] and len(parts(C,e))==1:A|=grants[e]
   if A==B:return A
 @functools.lru_cache(None)
 def exact(C,A):
  if len({ds[w] for w in range(n) if C>>w&1})==1:return True
  for e in range(ne):
   if req[e]&A!=req[e]:continue
   kids=parts(C,e);B=A|grants[e]
   if all((k,B)!=(C,A) for k in kids) and all(exact(k,B) for k in kids):return True
  return False
 @functools.lru_cache(None)
 def brac(C,A):
  A=closure(C,A)
  if len({ds[w] for w in range(n) if C>>w&1})==1:return True
  for e in range(ne):
   if req[e]&A!=req[e]:continue
   kids=parts(C,e)
   if len(kids)>1 and all(brac(k,A|grants[e]) for k in kids):return True
  return False
 @functools.lru_cache(None)
 def msolver(C,A):
  A=closure(C,A)
  if len({ds[w] for w in range(n) if C>>w&1})==1:return True
  for e in range(ne):
   if req[e]&A!=req[e] or grants[e]:continue
   kids=parts(C,e)
   if len(kids)>1 and all(msolver(k,A) for k in kids):return True
  return False
 return exact(full,0), (msolver(full,0) if mcas else brac(full,0))

def check():
 N=0;M=0
 for n in (2,3,4):
  for _ in range(1600):
   ne=3;nq=2
   ds=[R.randrange(2) for _ in range(n)]
   obs=[[R.randrange(2) for _ in range(n)] for _ in range(ne)]
   req=[R.randrange(1<<nq) for _ in range(ne)]
   grants=[R.randrange(1<<nq) for _ in range(ne)]
   a,b=solve(ds,obs,req,grants,nq)
   assert a==b,(n,ds,obs,req,grants,a,b)
   N+=1
   # MCAS: E0 constant, E1 grant-free
   obs2=[([R.randrange(2)]*n if e==0 else obs[e]) for e in range(ne)]
   gr2=[grants[0],0,0]
   a,b=solve(ds,obs2,req,gr2,nq,mcas=True)
   assert a==b,(n,ds,obs2,req,gr2,a,b)
   M+=1
 # explicit witness with exact solver and naive sensor-only
 ds=[0,1,0,1];obs=[[0,0,1,1],[0,0,1,1],[0,1,0,1]];req=[0,0,1];gr=[0,1,0]
 a,b=solve(ds,obs,req,gr,1)
 assert (a,b)==(True,True)
 naive,_=solve(ds,obs,req,[0,0,0],1)
 assert naive is False
 print(f'PASS: {N} BRAC vs exact; {M} MCAS vs exact; explicit witness exact=True BRAC=True naive=False; seed=20261112')
if __name__=='__main__':check()
