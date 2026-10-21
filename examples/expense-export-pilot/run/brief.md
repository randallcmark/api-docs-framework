# Expense-export change brief

**Reader/outcome:** A multi-company partner planner decides whether accounting-draft export fits the customer's workflow; an engineer exports one company's approved expenses and recognizes draft creation. Actual reimbursement and ledger posting are outside this platform.

**Scope:** Start with company access and an accounting connection configured. One export queues eligible expenses in a UTC date range and produces a draft batch. Production completion is `succeeded` plus `externalBatchId`. Sandbox success is simulated. Reuse the existing company-access and support pages.

**Evidence:** API-3 is the contract; IMPL-7 shows draft creation and the sandbox boundary; ANSWERS-1 P1 establishes the intended accounting-handoff framing, and E1 supplies fictional current deployment, key retention and recovery behavior. REQUEST-1 and the current guide are claims to assess. All inputs are original fictional artifacts, not the user's platform or real deployment evidence. The evidence index pins their bytes.

**Decisions:** Q1 is answered by P1: accounting handoff, with review/posting and payment outside the platform. Q2 is answered by E1: company-scoped 24-hour key replay, separate failed-job recovery, and support reconciliation for ambiguous provider effects. No unsupported completion time, webhook, polling interval or universal retry is promised.

**Change:** Revise the existing guide and add one operation reference. Retain shared auth/support. No actual platform release, tooling installation, FAQ or separate payment guide is introduced.

**Acceptance:** A reader can distinguish queue acceptance, draft creation, ledger posting and payment; choose UTC start-inclusive/end-exclusive dates; preserve company context; replay an unknown create only under the stated key rules; route each supplied failure appropriately; and distinguish sandbox simulation from provider creation.

**Checks/limits:** Compare operations, fields and examples with the pinned contract and supplied implementation/answers; check local links and packet/diff integrity. There is no MDX renderer, deployed API or real provider for this fixture. No requests or tests of readers are performed. Unverified execution must remain explicit in the review record.
