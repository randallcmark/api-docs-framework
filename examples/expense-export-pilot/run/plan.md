# Bounded change plan

Applied [prompt 2](../../../prompts/02-plan.md) after incorporating the authored ANSWERS-1 fixtures. The inputs and prompt hashes are recorded in the evidence index; this is a manual agent workflow exercise, not a production integration.

| Page | Action and purpose | Evidence/dependency |
| --- | --- | --- |
| Guide | Revise misleading reimbursement framing; connect eligibility, date range, request, job result, sandbox and recovery | API-3, IMPL-7, P1/E1; shared auth/support |
| Operation reference | Add request fields and operation effects, status meanings, active-key conflict, scopes and response examples | API-3 plus E1 for operational semantics beyond schema |
| Company access | Retain and link rather than duplicate | Existing shared page already covers partner/session and company consent |
| Integration support | Retain and link for unresolved create/provider effects | E1 and existing shared page |

Apply P01 outcome routing, P03 request versus workflow completion, P04 company access, P05 sandbox verification, P06 conditional recovery, P09 reference semantics and P11 date boundaries. These patterns motivate checks; all product facts come from the fictional evidence. P07 change communication and P08 tooling do not trigger new content because this is a documentation correction and no tool is offered.

The guide will use a short purpose/limit introduction, relevant prerequisites, one sequence, a state table, bounded verification and two recovery branches. The reference will cover only these two operations and fields that matter. No mandatory FAQ or site-wide rewrite is justified. Cross-links connect guide/reference and shared access/support.

Acceptance/checks: compare date boundaries and field names to API-3; verify example IDs/states and scopes; compare all completion/retry claims to IMPL-7 and E1; check local links and exact diff coverage. Do not call the `.test` endpoints, claim provider simulation execution, or infer MDX build success. A fresh evaluator receives the supported brief, source artifacts, actual diff and shared content, excluding the author discovery/plan/claim map and any self-score.
