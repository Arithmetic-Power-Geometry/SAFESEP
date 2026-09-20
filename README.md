# SAFESEP

SAFESEP is a reproducible research repository for **safe separability under authorization-sensitive evidence acquisition**. It contains the formal models, exact solvers, regression tests, exhaustive validation slices, randomized differential tests, and controlled capability-gate artifacts used across the SAFESEP research line.

## SAFESEP-II — revocable authority

**Mohammad Amir Khusru Akhtar (2026). _Safe Separability under Revocable Authority: Destructive Evidence Coupling, Branch-Conditioned Adaptivity, and a Fixed-Parameter Behavioral Kernel_ (Version V1). Zenodo.**

DOI: https://doi.org/10.5281/zenodo.22852609

SAFESEP-II studies finite deterministic, one-shot evidence probes whose fixed world-independent authority effects may include requirements, grants, and revocations. The target is decision separation rather than exact world identification.

The paper establishes:
- a three-world pairwise/global obstruction under destructive evidence coupling;
- an acyclic evidence-precedence sufficient certificate;
- a four-world example showing that global acyclicity is not necessary under adaptive branching;
- an exact decision-obligation quotient;
- irrelevant-authority erasure;
- dynamic behavioral probe equivalence;
- the bound `Bell(2k) * 2^(3r)` on behavioral probe types; and
- fixed-parameter tractability in `k+r` for the stated restricted model.

### Validation reported in SAFESEP-II

| Validation target | Cases |
|---|---:|
| Acyclic precedence certificate | 5,184 |
| Dynamic duplicate quotient | 1,728 |
| Dynamic-type hardening | 5,184 |
| Randomized differential tests | 2,500 |
| Controlled scenario predictions | 3 scenario families |

The randomized battery uses seed `20260919`. The independent world-state AND/OR solver is retained as the reference oracle.

### Controlled systems scope

The controlled systems realization uses **app/controller-owned capability gates**. It is not presented as evidence for undocumented Android permission behavior. A complementary Android/Pixel testbed studies delegated authority across security-state transitions such as locking, process death, reboot, and changes in authorization state.

## SAFESEP-I — monotone predecessor

SAFESEP-II continues the earlier monotone SAFESEP result:

**Mohammad Amir Khusru Akhtar (2026). _Safe Separability for Autonomous Authorization: Branch-Relative Authority Closure Under Decision-Critical Uncertainty_ (Version V1). Zenodo.**

DOI: https://doi.org/10.5281/zenodo.22828708

SAFESEP-I establishes Branch-Relative Authority Closure under its restricted monotone, world-independent authority semantics. SAFESEP-II crosses that boundary by admitting revocation.

## Model boundary

The SAFESEP-II theorem is restricted to:
- explicit finite worlds;
- deterministic observations;
- one-shot probes;
- world-independent requirements, grants, and revocations;
- idempotent set-valued authority updates; and
- no hidden effects beyond observation, authority update, and probe consumption.

It does **not** cover stochastic observations, reusable probes, quantitative or consumable resources, world-dependent authority effects, dynamically created probes, time-varying observation maps, or hidden side effects.

The FPT bound is structural rather than a claim of practical efficiency for large parameter values.

## Repository organization

- `src/` — formal solvers and supporting implementation.
- `tests/` — regression, exhaustive, and differential validation.
- `results/` — retained research records and validation outputs.
- `experiments/` — controlled systems protocols and artifacts.
- `data/` — generated validation data and retained SAFESEP-I artifacts.

Some files under `results/` preserve the chronological research/falsification record and therefore use historical names such as “attack,” “gate,” or versioned passes. Those names describe the development history; they are **not author instructions and are not current manuscript claims**. The authoritative SAFESEP-II claims and scope are the V1 paper and this README.

## Citation

Akhtar, M. A. K. (2026). *Safe Separability under Revocable Authority: Destructive Evidence Coupling, Branch-Conditioned Adaptivity, and a Fixed-Parameter Behavioral Kernel* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.22852609

Machine-readable citation metadata are provided in `CITATION.cff`.

## License

See `LICENSE`.
