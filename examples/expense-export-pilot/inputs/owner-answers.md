# Fictional owner answers — ANSWERS-1

These answers are authored scenario fixtures used after the discovery pass. They are not answers from the user, interviews with real owners, observed production behavior or measurements of question burden.

## P1 — Product response to Q1

Owner: fictional expense product owner. Revision: expense-intent-2.

Frame this as exporting approved employee expenses to an accounting draft batch for review. The platform does not reimburse employees or post the batch to a ledger. Customer accounting staff review and post using their provider's own process; actual payment happens separately outside this platform. Do not invent a payment endpoint or provider-specific posting steps. The intended readers are partner planners and engineers; the guide starts after company access and an accounting connection are configured.

## E1 — Engineering response to Q2

Owner: fictional integration engineer. Revision: expense-operations-4. Deployment record: expense-api-3 and expense-export-7 are the currently deployed versions in this scenario. This declaration supplies fixture availability evidence; no real deployment is represented.

A key is scoped to company ID and retained for 24 hours from the first accepted request. Within that window, the identical key and body return the original job ID. A different body under that active key returns 409 and must not be treated as a new export. After an unknown create outcome, replay the same key/body within this window; never change the key merely because the response was lost. This deduplicates job creation, not every provider effect.

If you have the job ID, read its state. If the outcome remains unknown after the window, contact the assigned integration support channel with the company ID, request ID and original request time, plus the job ID if available. Do not blindly create a new export.

A failed `invalid_account_mapping` job has created no external batch. The company accounting administrator corrects the mapping in the configured connection under Settings → Expense mapping. After that correction, create a new job with a new key. Partners should not invent an API for this configuration step. A failed `provider_unavailable` job can have an unknown external outcome: a provider may already have created the draft before its response was lost. Do not automatically create another export or new key; ask integration support to reconcile the job and external batch first. No unconditional provider retry guarantee is offered.

Read job status as needed; this workflow supplies no webhook, fixed completion-time promise or universal polling interval. A production `succeeded` job with `externalBatchId` establishes creation of a draft batch, not ledger posting or employee payment. Sandbox success produces only the simulated batch ID from SandboxAdapter; no external batch or production authorization is proved.
