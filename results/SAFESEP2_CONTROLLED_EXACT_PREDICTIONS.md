# SAFESEP-II controlled experiment: independent formal predictions

The controlled systems harness is checked against the original exact AND/OR solver, not only against its own replay code.

Expected whole-instance resolvability:
- destructive coupling: FALSE;
- one-way precedence: TRUE;
- branch-conditioned adaptive scenario: TRUE.

This distinction matters. Trace replay checks that recorded transitions obey the semantics. The exact solver independently checks the existential policy-level prediction for the same formal instance.

Paper evidence should report both:
1. transition-level replay agreement; and
2. policy-level exact-solver agreement.

The capability gates in this experiment are app/controller-owned resources. They must not be described as Android OS permissions unless a separate Android permission implementation is actually executed and logged.
