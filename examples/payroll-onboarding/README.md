# Worked example of an onboarding documentation change

This constructed example demonstrates the framework from evidence to review. The platform, API, product answers and documents are fictional, original fixtures. No real customer platform, provider implementation, live API or independently measured improvement is represented.

## Follow the evidence chain

1. [Research evidence](../../research/evidence.json) E07 observes Gusto's separation of submission, prerequisites and completion. E02 observes Square's explanation of operation effect. These motivate [pattern P03](../../patterns/library.md#p03-distinguish-request-success-from-workflow-completion); they supply no facts about this fictional API.
2. The [fictional OpenAPI contract](openapi.json) describes submission and status operations. [Product and engineering answers](decisions.json) supply the example's meaning, scope and recovery policy.
3. The [change brief](change-brief.md) records the reader task, evidence and required changes.
4. [Before](before.mdx) shows a confident draft with unsupported promises. [After](after.mdx) connects supported steps to observable outcomes and a [reference](reference.mdx).
5. The [evaluation](evaluation.md) explains concrete defects, changed criteria and what remains unverified. The [review packet](review-packet.md) directs limited human attention to the consequential passages.

The evaluation is an authored demonstration. It is not an independent evaluator run or human calibration. The request snippets use the reserved `.test` domain and cannot call a real service. No requests, credentials, company records, financial operations or tooling installations were executed.
