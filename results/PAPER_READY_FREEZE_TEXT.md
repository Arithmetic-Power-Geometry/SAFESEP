# SAFESEP paper-ready freeze text

This file is the authoritative revision patch for the manuscript
"Safe Separability for Autonomous Authorization: Branch-Relative Authority
Closure Under Decision-Critical Uncertainty".

## Abstract replacement

Autonomous agents increasingly act before all authorization-relevant facts are
known. The difficult case is not only whether an action is permitted, but
whether the agent may legitimately obtain the evidence needed to determine what
should be permitted. We formalize this circularity as safe separability:
compatible possible worlds may require different authorization decisions while
the actions needed to distinguish them are themselves authorization-sensitive.
A safe policy must resolve such decision-critical uncertainty using only probes
legitimate in every world still compatible with the current branch. We define
exact joint-state semantics over knowledge and authority and identify a
restricted Monotone Closure-then-Authorized Sensing class. A direct
generalization fails because an action that is globally informative may become
observation-constant after earlier evidence while remaining necessary for
authority progress. This motivates Branch-Relative Authority Closure (BRAC),
which recomputes authority closure after each observation. For the explicit
finite monotone, world-independent Probe model, we prove a stronger exactness
result: BRAC resolves an initial state if and only if exact joint-state search
does. Equivalently, after computing the least authority-reachable token closure,
safe boolean resolvability holds exactly when every pair of compatible worlds
requiring different decisions is separated by at least one authority-reachable
probe. This yields a polynomial-time boolean resolvability test in the explicit
representation, while cost-optimal adaptive tree construction retains a
classical hard decision-tree core. The characterization is supported by a new
6,144-system exhaustive comparison among the polynomial criterion, BRAC, and
exact search, in addition to the earlier 256-system and randomized batteries.
A defensive Android-emulator sanity workflow confirms a real synthetic
permission grant/revoke transition but is not treated as vulnerability evidence
or as validation beyond the theorem's monotone boundary. World-dependent grants
and revocation remain explicit counterexamples to the normalization.

## Contributions replacement

Our contributions are:

1. a formal safe-separability semantics for authorization decisions under
   incomplete knowledge, separating decision resolution from exact world
   identification;
2. exact joint knowledge-authority semantics used as a reference oracle for
   falsification;
3. MCAS closure exactness and minimal counterexamples showing why unrestricted
   informative authority changes, world-dependent grants, and revocation defeat
   naive closure;
4. BRAC, which recomputes authority closure after every observation and treats
   globally informative actions as authority-only when they become constant on
   the current branch;
5. a pair-separation characterization proving BRAC completeness for the
   explicit finite monotone, world-independent Probe model;
6. a polynomial-time criterion for boolean resolvability in that restricted
   explicit representation, separated explicitly from the harder cost-optimal
   adaptive-tree problem;
7. reproducible falsification including the earlier 256 four-world systems,
   1,250 deterministic randomized certified comparisons, a new 6,144-system
   exhaustive theorem battery, CI across Python 3.10--3.12, and a defensive
   Android-emulator permission-state sanity check.

## Replacement for Theorem 2

### Theorem 2 (Monotone pair-separation characterization)

Let W be finite and let the current branch be C. Assume that probe requirements
and grants are world-independent, authority changes only by monotone token
addition, no probe revokes authority, and probe execution only refines the
compatible-world branch. Starting from authority A, let T* be the least fixed
point obtained by repeatedly adding the grants of every probe whose
requirements are contained in the current token set. Let E* be the probes whose
requirements are contained in T*.

Then (C,A) is safely resolvable if and only if every pair u,v in C with
D(u) != D(v) is distinguished by at least one e in E*, i.e.
O_e(u) != O_e(v).

#### Proof

Necessity. Let u,v require different decisions. Any safe resolving policy must
eventually place them in different observation branches. Hence some probe
executed by that policy has different outcomes on u and v. Every executed probe
must be authority-reachable from A through monotone world-independent grants,
so it belongs to E*. Therefore every decision-incompatible pair is separated by
an E* probe.

Sufficiency. Execute authority-reachable probes in a fair order, reconsidering
the enabled set whenever a probe adds tokens. World-independent monotone grants
ensure that executing a legitimate probe cannot invalidate another legitimate
probe. Probe outcomes only refine the current branch. Thus every probe in E*
can eventually be executed. At any terminal observation-signature branch, two
surviving worlds have identical outcomes for every probe in E*. By hypothesis
such worlds cannot require different decisions. Every leaf is therefore
decision-homogeneous, giving a safe resolving tree. QED.

### Corollary 1 (BRAC exactness)

Under the assumptions of Theorem 2, BRAC resolves an initial joint state if and
only if exact joint-state search resolves it.

BRAC executes currently branch-constant members of the same monotone
authority-reachable action family early. Such execution cannot remove authority
or merge observation branches. Informative probes remain available and their
world-independent grants apply on every resulting child. Hence BRAC and exact
search satisfy the same pair-separation characterization.

### Corollary 2 (Polynomial boolean resolvability)

Let n=|W| and m=|E|. After computing the least authority-reachable token closure,
boolean resolvability is decided by checking at most n(n-1)/2 world pairs
against at most m probes. The pair scan is O(n^2 m), and token closure is
polynomial in the explicit encoded input.

This result concerns boolean resolvability only. It does not imply that finding
a minimum-cost or minimum-worst-case adaptive resolving tree is polynomial.

## Complexity subsection

General conditional planning under partial observability has substantially
higher known complexity, but that result should not be transferred to the
restricted SAFESEP Probe model. In the explicit monotone world-independent
semantics studied here, Theorem 2 gives a polynomial boolean-resolvability
criterion. Cost optimization is different: when authority requirements and
grants are removed and all probes are initially legitimate, cost-optimal
SAFESEP contains ordinary optimal decision-tree construction as a special case.
Classical optimal binary decision-tree construction is NP-complete (Hyafil and
Rivest, 1976). We use that fact only to identify an inherited hard optimization
core; we do not claim a new hardness theorem. The complexity of richer SAFESEP
semantics with revocation or world-dependent authority effects is left open.

## Results addition: larger theorem falsification

A new exhaustive theorem battery enumerated 6,144 three-world/two-probe systems
over all binary outcome maps, one-token requirement flags, one-token grant
flags, and all nonconstant binary decision assignments. For every enumerated
system, three independently implemented decision procedures agreed:
(1) the polynomial pair-separation criterion, (2) exact joint-state search, and
(3) BRAC. A further regression verifies arbitrary decision alphabets rather
than reserving literal R/W labels. This battery supplements rather than replaces
the earlier 256 four-world outcome comparison and the 1,250 deterministic
randomized certified comparisons.

## Android validation paragraph

A defensive CI experiment was additionally run on an ephemeral Android
emulator using a minimal synthetic package declaring the CAMERA runtime
permission. The workflow installed the package, established a denied state,
granted the permission with package-manager tooling, verified the granted
state, revoked the permission, verified denial again, and uninstalled the
package. The successful transition is used only as a platform-semantics sanity
check showing that the experimental harness observes a real authority-state
change. It is not evidence of an Android vulnerability and does not extend the
BRAC theorem to revocation; indeed, revocation is deliberately outside the
monotone completeness assumptions.

## Related-work / novelty boundary replacement paragraph

SAFESEP does not claim novelty for belief-state contingent planning, sensing
actions, AND/OR policy search, protected credential disclosure, automated trust
negotiation, credential gathering, monotone authorization reasoning, or
classical optimal decision-tree hardness. These have established antecedents.
The contribution claimed here is narrower: an authorization-specific
decision-critical formulation in which evidence probes must be legitimate
across every world still compatible with the current branch, together with
exact joint knowledge-authority semantics, the MCAS-to-BRAC counterexample
progression, and the restricted pair-separation characterization and BRAC
exactness theorem. The counterexamples for world-dependent grants and
revocation are part of the claimed boundary rather than cases covered by the
normalization.

## Limitations replacement

First, the BRAC exactness theorem applies to the explicit finite Probe model
with monotone, world-independent authority effects, world-independent
requirements, and no revocation. World-dependent grants and revocation have
explicit counterexamples and require richer semantics. Second, the new 6,144
system exhaustive theorem battery remains a finite small-instance
falsification; larger evaluations use controlled structured families. Third,
the Android emulator experiment validates only a synthetic permission-state
transition and is neither a vulnerability claim nor a direct real-system
validation of the full SAFESEP evidence/authority interaction. Fourth, public
authorization benchmarks establish practical relevance but do not generally
provide the counterfactual world-by-probe legitimacy and authority-transition
labels required for theorem-level evaluation. Fifth, the polynomial result is
for boolean resolvability in the restricted explicit representation; optimal
costed policies and richer non-monotone semantics remain separate complexity
questions.

## Conclusion replacement

Authorization under uncertainty becomes circular when the evidence required to
determine permission is itself permission-sensitive. SAFESEP isolates this
circularity by requiring evidence probes to remain legitimate across the entire
unresolved branch. Exact joint-state search provides a reference semantics, and
BRAC exploits a restricted but useful structure: after observations narrow the
compatible worlds, actions that were globally informative may become
branch-constant while remaining useful for monotone authority progress.

For the explicit finite monotone, world-independent Probe model, the resulting
structure is stronger than empirical agreement alone. Safe boolean
resolvability is equivalent to authority-reachable separation of every
decision-incompatible world pair, BRAC is complete with respect to exact
joint-state search, and the boolean decision is polynomial-time checkable in
the explicit representation. Exhaustive and randomized falsification support
the implementation of this characterization, while world-dependent grants and
revocation expose its boundary. The resulting principle is therefore precise:
reconsider evidence actions after each observation relative to the remaining
worlds, but apply BRAC normalization only where authority evolution satisfies
the theorem's monotone world-independent assumptions.
