# Severity-boundary follow-up

The user accepted [C02 as material](../../adjudications/c02-severity.md). The rubric now requires a supported chain from the documented instruction through system behavior to a serious consequence before assigning critical severity. An actual incident is unnecessary. C10 adds an explicit, fictional £5,000 disbursement caused by the same empty-data inference.

Two new fresh contexts evaluated four frozen packets each without seeing the decision record, expected labels, prior results or each other's output. They received the revised rubric. Case order differed between evaluators. This is a targeted development iteration on an adjudicated rule, not an untouched holdout or a broad benchmark.

| Case | Evaluator A | Evaluator B | Observation |
| --- | --- | --- | --- |
| C02 Empty data → business classification | Material; needs revision | Material; needs revision | Neither invents an approval, transfer or loss. |
| C10 Empty data → explicit advance release | Critical; needs revision | Critical; needs revision | Both trace the empty local list through the unguarded release endpoint to the specified £5,000 transfer before data prerequisites are met. |
| C03 Tenant-access control | Critical; needs revision | Critical; needs revision | Both retain the supported cross-tenant data-exposure consequence. |
| C05 Concise-reference control | No findings; ready for human review | No findings; ready for human review | Neither demands extra sections or tooling. |

Both agree on all 15 requested applicability/rating/state profiles and all four readiness decisions. Evaluator B also tags workflow completeness on C02/C10; evaluator A does not. That additional coverage does not change the severity or readiness result. Neither asks an owner question. Severity conclusions above come from inspection of the actual findings, not the mechanical profile-agreement metric.

This check supports the specific clarification: C02 remains an error requiring correction, while critical severity needs the supported serious consequence provided in C10. It does not establish that all criteria are calibrated, that real PR quality improved, or that reader/reviewer effort decreased. Other first-run score/tag proposals remain provisional.

## Frozen record

[manifest.json](manifest.json) records input/source hashes, finalized original-result hashes, case order and context restrictions. [inputs.json](inputs.json) archives all packet evidence and MDX with the shared rubric stored once; [author-key.json](author-key.json) preserves the proposed key withheld from the evaluators. [comparison.json](comparison.json) contains the mechanical comparison; [analysis.json](analysis.json) records the scoped author interpretation. Original [A results](results/evaluator-a/) and [B results](results/evaluator-b/) remain unchanged after coordinator freeze.

The source snapshot is identified by the merged base commit plus exact hashes of changed input files; it is not represented as if the old base commit already contained the revised rubric. The archive reconstructs the exact packet bytes independently of later file edits. The first run's archived inputs, key, manifest, analysis, comparison and all 18 original results are unchanged.

Both evaluators used the same inherited model family in fresh contexts; exact versions are unknown. Packet-only restrictions are operational, not enforced access control. Evaluator B reported correcting a mistyped finish timestamp to the real clock before finalization, with no assessment-content change. Active review minutes remain uninstrumented/null. No API execution, MDX build, reader task, real-platform evaluation or benefit measurement occurred. The user's platform remains untouched.

C02's severity question is closed. The next practical work is the guided authoring pilot described in the [roadmap](../../../../docs/roadmap.md#milestone-4--repository-workflow-integration): turn the discovery, plan, draft and independent-evaluation steps into one usable workflow before selecting product packaging or using the holdout.
