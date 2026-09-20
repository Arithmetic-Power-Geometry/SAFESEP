# SAFESEP-II controlled systems protocol

## Purpose

The controlled systems realization tests whether the formal SAFESEP-II transition semantics can be instantiated in an executable environment. It is not evidence that Android itself implements the theorem or that deployed Android applications necessarily exhibit destructive evidence coupling.

## Authority resources

Two independently revocable resources, `X` and `Y`, are represented using explicit app/controller-owned capability gates. Recorded state includes the compatible-world branch, unresolved obligations, authority before and after each probe, selected probe, deterministic outcome, and terminal decision or dead end.

## Scenario A — destructive evidence coupling

Three worlds require different decisions. Probe `P` requires `X`, separates `{a}|{b,c}`, and revokes `Y`. Probe `Q` requires `Y`, separates `{a,b}|{c}`, and revokes `X`. With initial authority `{X,Y}`, either first probe leaves an unresolved branch while destroying the authority required by the other probe. Exact prediction: **unresolvable**.

## Scenario B — one-way precedence

One probe revokes authority required by another without reciprocal revocation. Exact prediction: **resolvable** in the safe precedence order.

## Scenario C — branch-conditioned adaptivity

A root probe separates four worlds into two branches. Only the branch-relevant destructive probe is then required. Exact prediction: **resolvable** because the conflicting probes occur on disjoint execution paths.

## Verification

Recorded transitions are replayed against the formal compatible-world and authority-update equations. Policy-level predictions are checked independently by the exact AND/OR solver.

## Android/Pixel scope

The repository's complementary Android/Pixel work studies delegated authority across security-state transitions such as locking, process death, reboot, and authorization-state changes. SAFESEP-II does not treat app-owned capability gates as undocumented Android OS permissions and does not claim prevalence of the theoretical failure in deployed Android applications.

## Citation

Akhtar, M. A. K. (2026). *Safe Separability under Revocable Authority: Destructive Evidence Coupling, Branch-Conditioned Adaptivity, and a Fixed-Parameter Behavioral Kernel* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22852609
