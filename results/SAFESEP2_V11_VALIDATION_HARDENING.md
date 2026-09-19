# SAFESEP-II V11 validation hardening

This pass deliberately adds no new conceptual result. It attacks the dynamic behavioral-type theorem at two weak points.

## Attack A: branch-created equivalence
Two probes may be behaviorally different at the parent but become identical after a root observation removes worlds. The dynamic quotient must recompute types on the child branch and may then merge them without changing exact resolvability.

A four-world regression exercises exactly this case.

## Attack B: grants and revocations together
The previous exhaustive slice emphasized requirements/revocations. The strengthened battery gives the duplicated probe every combination of:
- binary observation map over three worlds;
- requirement in {none,x,y};
- grant in {none,x,y};
- revoke in {none,x,y};
with three decision maps and an arbitrary binary observation map for a third probe.

Total strengthened comparisons:
    3 * 8 * 8 * 3 * 3 * 3 = 5,184.

Every case compares the dynamic type quotient directly with the independent exact AND/OR solver.

## Validation rule
Any disagreement blocks the FPT theorem and blocks paper drafting around that theorem. Passing this battery is evidence, not proof; the mathematical induction must still be hardened separately.

## Next gate after CI
If the complete repository CI passes:
1. freeze theorem assumptions precisely;
2. write a formal lemma/proof for dynamic duplicate elimination;
3. derive the explicit FPT kernel/state bound without hiding m in preprocessing;
4. run focused prior-art comparison;
5. build the controlled Android/MCP realization;
6. then draft Paper II.
