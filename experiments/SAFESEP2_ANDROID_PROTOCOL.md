# SAFESEP-II controlled real-system validation protocol

## Goal

Validate the paper's central systems claim in a controlled executable setting: evidence acquisition can be individually legitimate yet globally unsafe because executing one probe can revoke authority needed by a still-unresolved decision obligation; branch-conditioned acquisition can avoid unnecessary destructive probes.

This experiment is validation of the SAFESEP-II semantics, not evidence that Android itself implements the theorem.

## Experimental architecture

Use a small Android test application plus a deterministic host-side controller.

### Authority resources
Represent two independently revocable capabilities using Android runtime permissions or app-owned capability gates:
- X: capability required by probe P;
- Y: capability required by probe Q.

The controller records before and after every probe:
- compatible-world branch;
- unresolved decision obligations;
- capability/permission state;
- selected probe;
- observed outcome;
- capability state after the probe;
- terminal decision or dead end.

### Scenario A — destructive evidence coupling

Worlds: a,b,c.
Required decisions: A,B,C.

P:
- requires X;
- observation partition {a}|{b,c};
- revokes/disables Y after execution.

Q:
- requires Y;
- observation partition {a,b}|{c};
- revokes/disables X after execution.

Initial authority: {X,Y}.

Expected result:
- every incompatible pair has an initially legitimate separating probe;
- choosing P first leaves the b/c obligation but destroys Q authority;
- choosing Q first leaves the a/b obligation but destroys P authority;
- no safe policy exists.

This realizes the pairwise-global failure proposition.

### Scenario B — one-way precedence

Choose probes such that P revokes authority required by Q but Q does not revoke authority required by P.

Expected result:
- P then Q fails;
- Q then P succeeds;
- logged trace agrees with the precedence edge Q -> P.

This realizes the acyclic-precedence sufficient construction.

### Scenario C — branch-conditioned adaptivity

Worlds: 0,1,2,3.
Root probe R requires no destructive authority and partitions
    {0,1}|{2,3}.

P resolves 0 versus 1 and uses/revokes X.
Q resolves 2 versus 3 and uses/revokes an authority resource conflicting with P.

Expected result:
- a static global family may contain a conflict/cycle;
- after R, only the branch-relevant probe is executed;
- both branches resolve safely;
- the unused conflicting probe is never executed on that path.

This realizes the adaptivity separation.

## Implementation rule

Prefer actual Android permission transitions where they can be triggered deterministically and safely by the test harness. Where Android does not expose a suitable self-revocation transition for a capability, use an explicit app-owned capability gate whose state transition is logged and externally verifiable. Do not misdescribe a simulated capability as an OS permission.

## Measurements

For every run emit machine-readable JSON/CSV with:
- scenario;
- world;
- step;
- compatible set;
- obligation count;
- authority-before;
- probe;
- outcome;
- grants;
- revocations;
- authority-after;
- remaining probes;
- terminal status.

Primary correctness checks:
1. trace replay matches the formal transition function;
2. exact solver prediction matches observed success/dead-end status;
3. precedence scenario succeeds only in the safe order;
4. adaptive scenario executes only the branch-required destructive probe.

Secondary measurements:
- number of probes executed;
- peak unresolved obligations;
- authority tokens lost;
- wall-clock overhead (descriptive only).

## Replication matrix

Run every world in every scenario repeatedly with clean app/controller reset between runs. Keep deterministic logical outcomes; repetitions test integration reproducibility, not statistical uncertainty.

## Paper evidence gate

The systems section is ready only when:
- raw traces are committed;
- a replay script verifies every transition;
- expected and observed terminal states agree for all runs;
- experiment command is documented;
- CI verifies trace replay.

## Claim discipline

The experiment demonstrates realizability of SAFESEP-II's authority-sensitive evidence semantics. It does not establish prevalence in deployed Android applications, does not benchmark security of Android, and does not imply that all permission systems exhibit destructive evidence coupling.
