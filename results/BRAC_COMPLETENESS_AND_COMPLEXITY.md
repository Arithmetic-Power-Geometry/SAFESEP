# BRAC completeness and complexity attack

## Scope

This result applies only to the explicit finite-world `Probe` semantics used by
the SAFESEP BRAC implementation:

1. probe requirements are world-independent token requirements;
2. grants are world-independent;
3. authority is monotone (tokens are added, never revoked);
4. probe outcomes may depend on the world;
5. execution only refines the compatible-world branch and never changes the
   underlying world's required decision.

World-dependent grants, revocation, destructive actions, and policy changes are
outside this theorem.

## Theorem 1 — Monotone resolution criterion

Let `T*` be the least fixed point obtained from the initial authority set by
repeatedly adding the grants of every probe whose requirements are already
contained in the current token set. Let `E*` be the probes whose requirements
are contained in `T*`.

The initial branch is safely resolvable **iff** every pair of compatible worlds
requiring different authorization decisions is distinguished by the outcome of
at least one probe in `E*`.

### Proof

**Necessity.** Consider an incompatible pair `u,v`. Any safe resolving policy
must eventually put them in different observation branches. Therefore some
executed probe has different outcomes on `u` and `v`. Every executed probe
is authority-reachable from the initial token set through monotone,
world-independent grants, hence belongs to `E*`. So every incompatible pair
is separated by an `E*` probe.

**Sufficiency.** Execute authority-reachable probes in any fair order, repeating
the process whenever a newly executed probe adds tokens. Requirements depend
only on tokens and grants are identical in every compatible world, so executing
a legitimate probe cannot make another legitimate probe illegitimate. Outcomes
only refine the current branch. Eventually every probe in `E*` can be
executed. At a terminal observation-signature branch, any two surviving worlds
have identical outcomes for every probe in `E*`. By the pair-separation
hypothesis they therefore cannot require different decisions. Every leaf is
decision-homogeneous, giving a safe resolving tree.

## Corollary 1 — BRAC completeness in the implemented monotone model

Exact joint-state search resolves an initial state iff BRAC resolves it.

BRAC closure merely executes currently branch-constant members of the same
monotone authority-reachable action family early. This cannot remove authority
or merge branches. Informative probes remain available and carry their
world-independent grants to every child. The theorem above therefore
characterizes both solvers by the same pair-separation condition.

This upgrades the manuscript's current one-directional BRAC soundness statement
to an iff result **for the implemented monotone, world-independent Probe
semantics only**.

## Complexity

Let `n=|W|`, `m=|E|`, and let `k` be the number of distinct authority
tokens explicitly appearing in the input.

Boolean resolvability is polynomial-time decidable. A straightforward
implementation computes token closure in at most `k` effective token-growth
rounds and then checks at most `n(n-1)/2` world pairs against at most `m`
probes. With set operations made explicit, a conservative bound is polynomial
in the encoded input size; the dominant simple pair scan is `O(n^2 m)` after
authority closure.

This does **not** make optimal SAFESEP cheap. Once the objective asks for a
minimum-cost or minimum-worst-case resolving tree, ordinary optimal binary
decision-tree construction is embedded as the special case with no authority
tokens and all probes initially legitimate. Classical optimal binary
decision-tree construction is NP-complete (Hyafil & Rivest, 1976), so costed
SAFESEP inherits a hard optimization core. We do not claim a new hardness
result from that inheritance.

## Falsification

Permanent regression:
- informative monotone grant chain;
- unreachable required token;
- exhaustive 3-world / 2-probe enumeration over all binary outcome maps,
  one-token requirement flags, one-token grant flags, and all nonconstant
  binary decision maps.

The exhaustive battery checks 6,144 systems and requires exact joint-state
search, BRAC, and the polynomial pair criterion to agree on every system.

## Scientific consequence

This is both a positive and a negative result.

Positive: BRAC completeness can be proved cleanly for the repository's current
monotone world-independent semantics.

Negative: boolean resolvability in that restricted semantics is structurally
simpler than the general contingent-planning problem. The paper should not
suggest that its boolean decision problem inherits the 2-EXPTIME complexity of
general partial-observability conditional planning.

The remaining difficult frontier is cost-optimal resolution and richer
authority semantics (especially revocation and world-dependent authority),
where the monotone pair criterion no longer applies.
