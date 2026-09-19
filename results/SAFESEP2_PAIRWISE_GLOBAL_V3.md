# SAFESEP-II autonomous pass V3 — pairwise/global separation failure

## Proposition: pairwise evidence viability is insufficient under revocation

There is a three-world, two-probe instance in which every pair of worlds requiring different decisions is separated by an initially legitimate probe, yet no safe adaptive resolving policy exists.

Let W={0,1,2}, with three distinct required decisions. Initial authority is {x,y}.

- p requires x, has observation partition {0}|{1,2}, and revokes y.
- q requires y, has observation partition {0,1}|{2}, and revokes x.

Every incompatible pair is separated: (0,1) by p, (1,2) by q, and (0,2) by either. But if p is executed first, the surviving unresolved branch {1,2} requires q while y has been revoked. If q is executed first, the surviving unresolved branch {0,1} requires p while x has been revoked. Therefore no first action leads to a resolving policy.

This proves that the monotone SAFESEP-I pair-separation criterion does not extend to revocable authority merely by checking availability of pairwise separators.

## Significance
The obstruction is not "revocation exists"; that is established prior art. The SAFESEP-II-specific phenomenon is **destructive coupling among evidence obligations**: individually available decision-separating witnesses need not be jointly schedulable under authority loss.

## Novelty caution
This proposition alone is not enough for a paper. Destructive tests/resources and contingent planning can exhibit analogous global scheduling conflicts. The next target is an authorization-specific structural certificate or complexity boundary.

## Next theorem candidates
1. Noninterfering-separator class: if there exists a separator family covering all incompatible pairs and no member revokes a token required by another member on any branch where that obligation survives, test whether pair coverage becomes sufficient.
2. Bounded-revocation parameter r: determine whether exact safe resolvability is FPT in the number of revocable tokens.
3. Obligation-authority state compression: determine whether the exact state can be quotiented by surviving incompatible-pair obligations plus authority relevant to those obligations.

## Paper gate
NO PAPER YET. Write only if a nontrivial exact characterization, sharp complexity result, or provably sufficient compressed certificate survives exhaustive falsification and prior-art review.
