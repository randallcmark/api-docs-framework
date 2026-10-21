"""Original fictional excerpt, revision expense-export-7. Not a runnable service.

Deployment and policy omitted from this excerpt must be confirmed separately.
Helpers, storage and provider clients are intentionally not implemented here.
"""


def create_export(company_id, body, key, token):
    require_scope(token, "expense_exports:write")
    require_company_consent(token, company_id)
    prior = find_key(company_id, key)
    if prior:
        if prior.body_digest != digest(body):
            return conflict("idempotency_conflict")
        return accepted({"jobId": prior.job_id})
    rows = approved_not_exported_expenses(
        company_id, body["startDate"], body["endDate"], timezone="UTC",
        start_inclusive=True, end_exclusive=True,
    )
    job = enqueue_export(company_id, rows)
    save_key(company_id, key, digest(body), job.id)
    return accepted({"jobId": job.id})


def run_export(job, adapter):
    # This creates a draft batch. It does not post a ledger or make a payment.
    result = adapter.create_draft_expense_batch(job.rows)
    record_state(job.id, "succeeded", externalBatchId=result.batch_id)


class SandboxAdapter:
    def create_draft_expense_batch(self, rows):
        # No provider connection or real accounting batch is created in sandbox.
        return DraftBatch(batch_id="sandbox-draft-001")

# Provider errors are mapped to failed with error.code. This excerpt does not
# establish whether a provider may already have created a batch on timeout.
# Key retention, failure recovery and deployment are not established here.
