# SAFESEP-II V11 randomized differential validation

## Status before this pass
After correcting the obligation-quotient terminal-progress bug, both repository workflows passed:
- full tests workflow run 326;
- BRAC completeness/theorem-falsification run 101.

The earlier failure was therefore retained as a useful regression lesson rather than hidden.

## New independent attack
Add 2,500 deterministic randomized instances comparing:
1. the original exact world-state AND/OR solver; and
2. the dynamic behavioral-kernel solver.

The generator varies:
- 3 or 4 worlds;
- repeated or distinct decision labels;
- 2 to 4 base probes;
- 2- or 3-valued deterministic observations;
- three authority tokens;
- arbitrary requirement, grant, and revoke subsets;
- arbitrary initial authority;
- injected exact behavioral duplicates in roughly one third of instances.

The seed is fixed at 20260919, making every failure reproducible.

## Interpretation
Agreement is falsification evidence, not proof. Any mismatch blocks the FPT claim until explained. A pass strengthens confidence that the dynamic quotient remains exact beyond the hand-constructed and exhaustive small slices.

## Next gate
If this randomized differential battery and full CI pass, move to controlled real-system realization. Do not add further abstract machinery unless a counterexample forces it.
