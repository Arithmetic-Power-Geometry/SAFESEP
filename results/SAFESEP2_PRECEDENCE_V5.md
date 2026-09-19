# SAFESEP-II autonomous pass V5 — evidence precedence

## Static noninterference is too strong
A probe p may revoke authority required by q without causing failure if q can safely execute before p. Therefore pairwise noninterference is not necessary even for simple resolvable systems.

Minimal pattern:
- p requires x, separates {0}|{1,2}, revokes y;
- q requires y, separates {0,1}|{2}, does not revoke x.
The static noninterference certificate rejects {p,q}, but q followed by p resolves all three worlds.

## Evidence-precedence graph
For a selected separator family S, add precedence edge q -> p whenever p revokes a token required by q. The edge means q must execute before p.

## Proposition: acyclic separator-cover soundness
Assume:
1. authority effects are world-independent;
2. every selected probe is initially executable;
3. selected probes collectively separate every decision-incompatible pair;
4. the evidence-precedence graph is acyclic.

Then the instance is safely resolvable.

### Proof
Take a topological ordering of the precedence graph. Consider a selected probe q when reached. Any earlier selected probe p that could revoke a token required by q would induce q -> p, contradicting the topological order. Hence q remains executable. Execute selected probes in topological order, stopping on any decision-homogeneous branch. If two worlds requiring different decisions survived all executed selected probes, they would have identical outcomes under the full selected family, contradicting pair coverage. Thus every surviving terminal branch is decision-homogeneous.

## Relation to V3
The V3 destructive-coupling counterexample induces a 2-cycle: q -> p and p -> q. The cycle is an explicit certificate of why no fixed ordering of those two separators works.

## Falsification
A complete 5,184-system three-world/two-probe battery is added for deterministic binary observations, requirements in {none,x,y}, and revocations in {none,x,y}. Every instance accepted by the acyclic certificate is required to resolve under the independent exact AND/OR oracle.

## Important limitation
Acyclicity is sufficient, not claimed necessary. Adaptive branching can avoid executing some mutually conflicting probes on branches where their obligations disappear. Therefore cyclic global precedence may still coexist with a valid branch-relative policy.

## Next target
Find the smallest exact-resolvable instance with no acyclic static separator cover. Such a witness would isolate the value of branch-relative scheduling. Use it to define a branch-conditioned precedence certificate and attack exactness.

## Paper gate
NOT YET. If branch-conditioned precedence yields an iff theorem for a meaningful revocation class and survives exhaustive search/prior-art, begin Paper II immediately.
