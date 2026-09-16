# SAFESEP Novelty and Prior-Art Report

**Date:** 16 September 2026  
**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**

## Executive finding
SAFESEP must not claim novelty for least privilege, task-scoped/JIT authorization, adaptive testing, active diagnosis, equivalence-class stopping, contingent or epistemic planning, history/provenance authorization, proof-carrying authorization, trust negotiation, cyclic credential detection, non-circular proof checking, or well-founded authorization semantics.

The original finite SAFESEP model is representable as strong contingent planning. Belief-relative authorization can be represented as epistemic preconditions. Justification/provenance state collides with history/provenance-aware authorization. The latest attack shows that the local Decision-Neutral Authority Closure test can be represented as proof-dependency checking when authorization proofs and disputed premises are explicit.

## Current surviving candidate
**Decision-Relative Authority Closure (DRAC): adaptive authorization resolution under proof-qualified evidence acquisition.**

For a decision-critical knowledge class `C`, candidate evidence probes may have multiple authorization proofs. A probe is eligible only if at least one valid proof does not depend on the unresolved decision. The agent adaptively selects probes, observes outcomes, updates `C`, and stops when all remaining worlds require the same authorization decision. The objective is minimum worst-case evidence cost.

The recurring cheapest-experiment diagnostic remains: find the cheapest eligible informative probe that still leaves a decision-incompatible branch. In the current construction this is `q` at cost 1.

## Latest executable collision
`src/safesep/proof_neutral.py` implements a proof-dependency baseline. Tests 24–26 show:
1. if all resolver proofs depend on disputed decision premises, the decision-neutral obstruction is reproduced;
2. if one alternative proof is independent, resolution is restored;
3. this compilation reproduces the obstruction on 10,000 explicit worlds.

This means local no-presupposition/proof-neutrality is not sufficient as a novelty claim.

## Real-data audit
AuthBench is a real public agent-permission benchmark with 120 tasks: 80 standard and 40 sensitive across 10 categories. It supplies gold read/write/execute permissions and constrained execution. It does not supply alternative authorization-proof graphs or decision-dependency labels, so it cannot honestly be used as direct DRAC ground truth without a justified mapping. The Amazon employee-access dataset likewise lacks proof-dependency structure. SAFESEP therefore separates real external-validity sources from controlled theorem benchmarks rather than fabricating missing labels.

## Stop criterion
**Status: not yet at the breakthrough stop point.**

The next result must be coupling-specific: a theorem, irreducibility result, or complexity result about adaptive decision resolution under proof-qualified evidence acquisition that is not merely inherited from proof-carrying authorization/trust management or from contingent/epistemic planning/adaptive diagnosis.

If such a result survives direct reduction attempts against those neighboring formalisms, the novelty search should stop and the manuscript should be written around that narrow result. Until then, describe DRAC as a research candidate, not a confirmed foundational breakthrough.
