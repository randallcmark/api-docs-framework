# Demonstration evaluation

Scope: compare the drafts against `openapi.json`, `decisions.json` and the stated task at `fixture-v1`, using the provisional rubric. This comparison was authored as part of the example, not obtained from independent reviewers or reader testing.

## Findings in the initial draft

| ID | Finding and evidence | Consequence | Required change |
| --- | --- | --- | --- |
| F01 | `before.mdx` treats a successful submission as activation and payroll readiness. The POST contract returns `202` and `pending_review`; decisions D01–D02 separate onboarding from payroll execution. | Material: a reader plans the wrong lifecycle and may attempt a subsequent workflow prematurely. | Explain acceptance, review states, completion and the separate payroll dependency. |
| F02 | The draft prescribes an API key. Both operations use tenant-bound OAuth in the fixture; D03 confirms this partner path. | Material: the reader chooses an unsupported access path. | Identify OAuth, tenant binding and operation-specific scopes. |
| F03 | Safe arbitrary retries and real-time webhooks are promised without contract support. D05 provides a status-read and contact fallback; D06 establishes the supported status path. | Material: the reader relies on an invented delivery or resubmission guarantee. | Remove promises and document the confirmed recovery path. |
| F04 | Instant approval and sandbox equivalence conflict with D04 and D07. | Material: planning and launch confidence exceed the evidence. | State timing limits and the simulation boundary. |
| F05 | Generic promotional language obscures the task and duplicates none of the necessary prerequisites or outcomes. | Editorial plus the task gaps recorded above. | Use a task title, concrete actions and observable results. |

These are documentation findings within a fictional scenario, not confirmed vulnerabilities or real platform defects.

## Criterion profile

| Criterion | Before | After | Evidence or remaining limitation |
| --- | --- | --- | --- |
| R01 Capability fit | 0, incorrect | 2 | Scope and separate payroll dependency now agree with D01–D02. |
| R02 Conceptual model | 0, missing | 2 | Company meaning, tenant context and statuses are explained. |
| R03 Workflow completeness | 0, incorrect | 2 | Submission connects to status interpretation and a completion condition. |
| R04 Technical accuracy | 0, incorrect | 2 within fixture | Operations and response examples match the fictional contract. No implementation or runtime comparison exists. |
| R05 Access and boundaries | 0, incorrect | 2 within fixture | OAuth, scopes and client-tenant context agree with D03 and the contract. |
| R06 Verification | 0, incorrect | Unverified | The revised guide identifies expected results and simulation limits, but no executable environment or scenario instructions exist for this fixture. |
| R07 Recovery and operation | 0, incorrect | 2 within fixture | D05 supplies the explicit status-read/contact fallback without inventing idempotency. |
| R08 Findability and coherence | 1 | 2 locally | The two revised pages link workflow, reference and state interpretation. Site-wide navigation and search are untested. |
| R09 Language and structure | 0, incorrect promises | 2 | Task wording replaces unsupported promises; a human style calibration has not occurred. |
| R10 Change communication | Not applicable | Not applicable | No real release or migration is being communicated. |
| R11 Developer tooling | Not applicable | Not applicable | No SDK, CLI, skill or MCP setup is part of this bounded change. |

No average or passing score is assigned. No 3 ratings are claimed. For a real submission, example execution and environment-specific testing remain verification work before recommending publication. The fixture's next status is `needs_answers` about test setup, not automatic acceptance.

## What this demonstrates

The researcher supplies a pattern about completion, but the platform evidence supplies actual statuses and behavior. Product questions expose gaps that prose polishing would miss. The resulting review can focus on state semantics, access boundaries and verification rather than reconstructing the assignment.

Whether this reduces reviewer time or improves reader outcomes requires a separate measured comparison; document length and score changes alone cannot establish that.
