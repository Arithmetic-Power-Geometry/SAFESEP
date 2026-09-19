# SAFESEP-II autonomous pass V6 — global cycles can vanish after evidence

## Proposition: global precedence acyclicity is not necessary
There is a four-world, three-probe system with a cycle in every static separator cover but with a safe adaptive resolving policy.

Let initial authority be {x,y}. Four worlds require four distinct decisions.

- root r requires no token and partitions {0,1}|{2,3}.
- p requires x, separates 0 from 1, and revokes y.
- q requires y, separates 2 from 3, and revokes x.

Any static family covering all incompatible pairs needs r,p,q. Because p revokes y required by q and q revokes x required by p, its global evidence-precedence graph contains p<->q and is cyclic.

Nevertheless the adaptive policy is safe:
1. execute r;
2. on branch {0,1}, execute p and stop;
3. on branch {2,3}, execute q and stop.

The destructive interaction is unreachable within any single execution branch.

## Consequence
The correct object is not a global precedence graph. It must be indexed by the current compatible-world branch. Evidence can discharge obligations and thereby delete precedence constraints before a conflicting probe becomes relevant.

## Candidate definition: Branch-Conditioned Evidence Precedence (BCEP)
At joint state (C,A), retain only decision-incompatible pairs inside C. A probe requirement is resolution-relevant on C only if it participates in a continuation needed to discharge at least one surviving incompatible pair. Precedence constraints should be generated only among probes whose obligations can coexist on the same reachable branch.

## Exact-theorem target
For a restricted class with world-independent one-shot authority effects, seek:
safe resolvability iff there exists a branch-indexed separator cover whose precedence graph is acyclic at every reachable branch after discharged obligations are removed.

This is not yet proved and may collapse to a restatement of the exact AND/OR policy recursion. The next novelty test is whether BCEP admits a certificate strictly smaller than the full policy tree and a polynomial verifier.

## Paper gate
CLOSE, BUT NOT OPEN. We now have:
- V3: pairwise availability is insufficient;
- V5: acyclic static precedence is sufficient;
- V6: global acyclicity is not necessary because evidence branching can erase conflicts.

Begin writing only if BCEP can be defined non-circularly and proved exact for a meaningful class, or if the minimal certificate/verification problem itself yields a sharp complexity theorem.
