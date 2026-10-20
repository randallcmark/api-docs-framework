# Provisional documentation rubric

Use this rubric to assess a coherent documentation change against its reader task and supporting evidence. It is a research draft, not a validated benchmark or an agreed publication gate.

## Evaluation record

Record the change and evidence revisions, reader task, relevant pages, evaluator and date. For each applicable criterion, include a rating, evidence locator, concrete finding, reader consequence and recommended fix. Inspect changed MDX and relevant linked pages; do not evaluate only the PR summary.

Record issue state independently: `incorrect`, `missing`, `unverified`, or `satisfied`. Mark a whole criterion `not_applicable` only with a reason. An unreachable page or unavailable evidence is `unverified`, not `not_applicable`.

## Rating anchors

| Rating | Meaning |
| --- | --- |
| 0 | Applicable information is absent or contradicted by available evidence; the reader cannot safely rely on it |
| 1 | Some useful information exists, but a consequential ambiguity or gap remains for the stated task |
| 2 | The reader can answer the criterion's question for the stated task, with appropriate supporting evidence and no known consequential gap |
| 3 | Meets 2 and clearly handles the task's relevant variants or boundary conditions, supported by specific evidence or verification |
| Unverified | Available evidence cannot establish the result; do not assign a numerical score |
| Not applicable | The criterion does not apply to this task; record why |

A 3 does not require longer prose or extra sections. A concise limitation can be sufficient. Score 0 findings must say whether the issue is missing or incorrect. Mixed evidence must remain explicit; use the consequential unresolved issue to constrain the criterion rating.

Do not compute an overall pass from a mean. Report the criterion profile, consequential findings and unresolved questions. Numerical thresholds can be considered after calibration.

## Criteria

| ID | Reader question and minimum adequate evidence | Relevant variants for a stronger result |
| --- | --- | --- |
| R01 Capability fit | Can I tell whether this supports my intended outcome? Scope, supported scenario, important limitations and availability are explicit and grounded in product answers and technical evidence. | Direct-client versus partner constraints, regions or entitlements where relevant. |
| R02 Conceptual model | Can I explain the entities, actors, ownership, relationships and lifecycle states involved? Definitions agree with the domain brief and implementation evidence. | Cross-domain terminology, source-of-truth decisions and identifier relationships. |
| R03 Workflow completeness | Can I plan the sequence and responsibilities? Prerequisites, steps, relevant operations/events and observable business completion are connected. | Parallel work, asynchronous states, branch conditions and human steps. |
| R04 Technical accuracy | Do operations, fields, examples and stated effects match the applicable API contract and implementation evidence? Required inputs, conditional fields, units and relevant defaults are explained. | Side effects, idempotency and version-dependent behavior where applicable. |
| R05 Access and boundaries | Can I choose the right authorization model, permissions and account/tenant context? Claims are supported by applicable authentication and authorization evidence. | Multi-customer partners, credential lifecycle and scope transitions. |
| R06 Verification | Can I test the task and recognize success? Examples are internally consistent, expected results are given, and relevant sandbox limits are explicit. | Failure simulation and verification of asynchronous completion. Execution must be recorded to claim an example was run. |
| R07 Recovery and operation | Can I diagnose and recover from consequential failures? Guidance explains relevant errors, retry conditions and status/log/support routes without inventing guarantees. | Duplicate handling, out-of-order events, reconciliation and disconnects as relevant. |
| R08 Findability and coherence | Can product and engineering readers reach the relevant explanation and move between capability, concept, guide and reference? Terminology and linked content agree. | Cross-domain journeys and clear routing for different integration models. |
| R09 Language and structure | Can readers identify decisions, actions, expected results and limitations without filler or unsupported promises? Structure fits the page's purpose; terminology is consistent. | Ambiguous language resolved with concrete conditions; concise reuse of shared guidance. |
| R10 Change communication | For a platform change, can readers identify applicability, compatibility impact, required action and migration guidance? Links and dates agree with confirmed release information. | Clear distinction between capability-oriented release notes, factual changelog entries and actionable migration instructions. |
| R11 Developer tooling | Where tooling is relevant and exists, can readers install/configure it, choose an environment and access scope, verify connection, and troubleshoot? Supported clients and versions are grounded in actual tooling evidence. | CLI, skills and MCP lifecycle differences; documentation access distinguished from account-changing tools. |

## Consequence and readiness

- **Critical:** evidence shows a claim would cause materially wrong financial behavior, unauthorized access, sensitive-data exposure, or a similarly serious outcome for the documented task. Explain the concrete path; do not escalate from a hypothetical possibility alone.
- **Material:** the task cannot be reliably planned, completed, verified or recovered using the documentation, or a consequential product claim is unresolved.
- **Editorial:** local language, formatting or minor consistency issue without a consequential effect on the task.

Recommend `needs_answers` when consequential behavior cannot be established and `needs_revision` when established defects need correction. Recommend `ready_for_human_review` when no known critical/material defects remain and the evidence packet is complete for its scope. This is not a claim that the documentation is infallible or a publication approval. Enforcement remains an open project decision.

Route product-intent questions to product owners, implementation questions to engineering, and standard exceptions to the designated documentation owner. Fix objective editorial findings before handoff when practical. Ask reviewers for decisions with evidence and impact; do not hand them an undifferentiated backlog.

## Calibration procedure

Choose short practice cases covering a wrong claim, missing completion conditions, a sound concise guide and an intentionally inapplicable criterion. Have evaluators assess the same evidence and task separately. Compare criterion interpretation, severity, evidence selection, review time and false positives. Adjudicate disagreements, record anchors and revise the rubric before using scores for acceptance.

The worked payroll example is a constructed demonstration, not a second independent evaluation or a calibration result. Freeze rubric and pattern revisions before the user's holdout evaluation.
