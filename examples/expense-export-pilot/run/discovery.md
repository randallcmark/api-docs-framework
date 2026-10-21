# Discovery — author pass

Applied [prompt 1](../../../prompts/01-discover.md) to REQUEST-1, API-3, IMPL-7 and the current guide/shared pages before incorporating the fictional owner answers. This is an agent exercise, not a real product/engineering interview.

The reader is a multi-company partner planning and implementing one company's expense export. REQUEST-1 calls the outcome reimbursement, while API-3 and IMPL-7 support creating an accounting draft batch and do not make payments or post the ledger. Product must confirm the intended documentation outcome. The token's broad consent does not authorize the signed-in user's selected company; the existing access page already supplies that answer, so no owner question is needed.

## Supported findings

- API-3 ExportRequest and IMPL-7 `approved_not_exported_expenses` establish UTC start-inclusive/end-exclusive filtering, not both-inclusive dates.
- API-3 Accepted and IMPL-7 `accepted` establish asynchronous acceptance. The current completion claim is incorrect.
- IMPL-7 `create_draft_expense_batch` creates a draft batch, not a ledger posting or payment. SandboxAdapter never contacts a provider.
- API-3's active-key same-body replay is useful, but neither it nor IMPL-7 establishes retention. The blanket new-key retry and failed-job retry claims are unsupported.
- Current auth and support guidance are useful and should be retained. Tooling, broad FAQs, unrelated payroll instructions and a platform changelog are unnecessary for this correction.

## Owner questions

Q1 — **Product:** The request says reimbursement, but the supplied operation creates a draft accounting batch and has no payment/posting effect. Should this guide promise accounting handoff, or is a separate supported reimbursement workflow required? This sets the title, capability-fit explanation and completion boundary. Do not invent that separate workflow.

Q2 — **Engineering:** For unknown create outcomes and failed jobs, what deployed key scope/retention and replay/reconciliation rules can be documented? API-3 only defines active-key replay; IMPL-7 omits retention, provider-timeout effects and deployment. We need a safe action after a timeout and after each supplied failure, rather than a conventional retry loop.

The source already settles operation names, date boundaries, job fields, declared scopes and the sandbox adapter's behavior. Ask no questions to repeat those facts. Supported page planning can proceed; dependent purpose/availability/recovery claims remain unresolved until the answers are incorporated.
