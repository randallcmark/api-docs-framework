# Connected documentation traces

These are inspected documentation routes with explicit gaps, not completed integrations or tested user journeys. An inspected procedure was read, not executed. Visible links can occur in navigation; their placement and usability are untested. Research jumps are not evidence that the site has no path.

## J01 Company onboarding through approval

**Reader:** Partner product planner and embedded-payroll engineer

**Outcome:** Plan company onboarding and connect its steps, access context and approval signals.

| Stage | Inspected sources | Coverage and limit |
| --- | --- | --- |
| scope and concepts | [gusto-onboarding](https://docs.gusto.com/embedded-payroll/docs/onboard-a-company) | **inspected** — Legal/company setup, dependencies and approval stages are connected in the guide. |
| access | [gusto-quickstart](https://docs.gusto.com/embedded-payroll/docs/quickstart), [gusto-auth](https://docs.gusto.com/embedded-payroll/docs/authentication-and-authorization) | **inspected** — Application and company token contexts are explicit. |
| workflow | [gusto-onboarding](https://docs.gusto.com/embedded-payroll/docs/onboard-a-company) | **inspected** — The guide supplies order, parallel work and completion conditions. |
| reference and events | [gusto-status-reference](https://docs.gusto.com/embedded-payroll/reference/get-v1-company-onboarding-status), [gusto-company-events](https://docs.gusto.com/embedded-payroll/docs/company-events) | **inspected** — Readiness fields and approval/event meanings are inspected together with the guide. |
| verification | [gusto-quickstart](https://docs.gusto.com/embedded-payroll/docs/quickstart) | **partial** — Environment and first-call setup is inspected; a full approval simulation procedure is not traced. |
| recovery | [gusto-quickstart](https://docs.gusto.com/embedded-payroll/docs/quickstart), [gusto-errors](https://docs.gusto.com/embedded-payroll/docs/errors) | **partial** — Symptoms and error shapes are inspected; linked category-specific recovery remains untraced. |
| change | [gusto-upgrade](https://docs.gusto.com/embedded-payroll/docs/version-upgrade-guide), [gusto-changelog](https://docs.gusto.com/embedded-payroll/changelog/v2025-11-15) | **inspected** — Versioned impact and required migration actions are inspected, without independent release verification. |

**Research jumps:** `gusto-onboarding` → `gusto-company-events`.

**Lesson:** A status reference needs its workflow context; accepted setup, completed steps and business approval must remain distinct.

**Remaining limits:**

- No API calls, approval simulation or reader tests.
- Full prerequisite tax/bank/form references and error-category recovery were not all followed.

## J02 Enterprise and embedded cross-border payouts

**Reader:** Product planner choosing an integration model and engineer building payouts

**Outcome:** Choose sender/account context, connect transfer resources, and understand tracking and testing boundaries.

| Stage | Inspected sources | Coverage and limit |
| --- | --- | --- |
| scope and concepts | [screen-wise](https://docs.wise.com/), [wise-send](https://docs.wise.com/guides/product/send-money) | **inspected** — Resources, partner models, corridors and changing requirements are explained. |
| access | [wise-enterprise](https://docs.wise.com/guides/product/send-money/use-cases/enterprise-payouts), [wise-embedded](https://docs.wise.com/guides/product/send-money/use-cases/embedded-payouts) | **partial** — Ownership and profile contexts are inspected; complete OAuth/certificate setup is not. |
| workflow | [wise-enterprise](https://docs.wise.com/guides/product/send-money/use-cases/enterprise-payouts), [wise-embedded](https://docs.wise.com/guides/product/send-money/use-cases/embedded-payouts), [wise-send](https://docs.wise.com/guides/product/send-money) | **inspected** — Recipient-first and quote-first steps connect recipient, quote, transfer and funding. |
| reference and events | [wise-transfer-reference](https://docs.wise.com/api-reference/standard-transfer/transfercreate), [wise-tracking](https://docs.wise.com/guides/product/send-money/tracking/track-transfers) | **inspected** — A concrete transfer operation, event subscriptions, correlation and failure handling are inspected. |
| verification | [wise-statuses](https://docs.wise.com/guides/product/send-money/tracking/transfer-statuses), [wise-simulation](https://docs.wise.com/api-reference/simulation/simulationtransferstatechange) | **inspected** — Valid simulated transitions and prerequisites are inspected; no simulation was run. |
| recovery | [wise-tracking](https://docs.wise.com/guides/product/send-money/tracking/track-transfers), [wise-statuses](https://docs.wise.com/guides/product/send-money/tracking/transfer-statuses) | **partial** — Ordering, payout failure/refund and exceptional state guidance is inspected; linked reconciliation procedures are not all followed. |
| change | Not traced | **untraced** — A version picker is not a migration path; change guidance is not traced for this workflow. |

**Research jumps:** None among the recorded connections.

**Lesson:** Common workflow structure can coexist with materially different sender, funding and customer-profile responsibilities.

**Remaining limits:**

- Recipient/quote/funding endpoint details, complete access setup and change guidance remain untraced.
- No bank, transfer, webhook or simulation action was performed.

## J03 Shift planning synchronization with HR

**Reader:** Partner product owner and engineer integrating shift planning

**Outcome:** Understand role boundaries, initial employee data and later employment/absence changes.

| Stage | Inspected sources | Coverage and limit |
| --- | --- | --- |
| scope and concepts | [personio-prerequisites](https://developer.personio.de/docs/introduction-and-prerequisites), [personio-initial-sync](https://developer.personio.de/docs/initial-core-data-sync) | **inspected** — Roles, app responsibilities and person/employment concepts are explicit. |
| access | [personio-prerequisites](https://developer.personio.de/docs/introduction-and-prerequisites) | **partial** — Key/account prerequisites are inspected; linked token setup is not followed. |
| workflow | [personio-initial-sync](https://developer.personio.de/docs/initial-core-data-sync), [personio-events](https://developer.personio.de/docs/event-driven-data-from-personio) | **inspected** — Initial population connects to event-driven updates and employment variants. |
| reference and events | [personio-person-reference](https://developer.personio.de/v2.0/reference/get_v2-persons), [personio-events](https://developer.personio.de/docs/event-driven-data-from-personio) | **partial** — One versioned persons reference and linked event semantics are inspected; not all versioned event contracts are followed. |
| verification | Not traced | **untraced** — A reproducible scenario/sandbox verification path is not inspected. |
| recovery | [personio-events](https://developer.personio.de/docs/event-driven-data-from-personio), [personio-handling](https://developer.personio.de/docs/handling-logic) | **partial** — Lifecycle scenarios are named; detailed image flowcharts and delivery-recovery logic remain uninspected. |
| change | [personio-change](https://developer.personio.de/changelog/deprecation-of-attendances-and-projects-v1-endpoints) | **partial** — Attendance/project migration is inspected as an adjacent shift-planning concern; not a complete migration of this whole integration. |

**Research jumps:** `personio-events` → `personio-handling`.

**Lesson:** An integration guide can expose product decisions about roles, eligibility, custom fields and termination behavior that schemas leave unexplained.

**Remaining limits:**

- Detailed diagrams were not visually inspected.
- Some guide links target versioned routes; their equivalence to unversioned pages is not assumed.
- No employee data, synchronization or authentication was exercised.

## J04 Create CRM records and connect relationships

**Reader:** Client or multi-account partner planner and integration engineer

**Outcome:** Understand CRM entities, select an access model and implement record/relationship operations.

| Stage | Inspected sources | Coverage and limit |
| --- | --- | --- |
| scope and concepts | [hubspot-crm-model](https://developers.hubspot.com/docs/api-reference/latest/crm/understanding-the-crm) | **inspected** — Objects, records, properties, relationships and identifier scope are explained. |
| access | [hubspot-auth](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/overview) | **inspected** — Single-account static access and multi-account OAuth are distinguished. |
| workflow | [hubspot-objects](https://developers.hubspot.com/docs/api-reference/latest/crm/using-object-apis) | **inspected** — Creation and retrieval connect required object properties and associations. |
| reference and events | [hubspot-associations](https://developers.hubspot.com/docs/api-reference/latest/crm/associations/associate-records/guide) | **inspected** — Relationship direction, category/type discovery and request examples are inspected; events are outside the selected task. |
| verification | Not traced | **untraced** — A dedicated developer-account/test scenario is not traced. |
| recovery | [hubspot-errors](https://developers.hubspot.com/docs/api-reference/error-handling) | **inspected** — Access errors, transient errors and batch partial-success guidance are inspected, without execution. |
| change | [hubspot-objects](https://developers.hubspot.com/docs/api-reference/latest/crm/using-object-apis) | **partial** — The guide identifies version-dependent validation and links an announcement; the announcement itself is not inspected. |

**Research jumps:** `screen-hubspot` → `hubspot-crm-model`.

**Lesson:** Reference usability depends on semantic identifiers, relationship direction and distribution-aware access, not field descriptions alone.

**Remaining limits:**

- The general entry does not directly link the selected concept page in the captured representation; the initial route is a research jump.
- A previous-version association link appears self-referential and needs investigation.
- No CRM requests, test-account setup or migration execution.

## J05 A bounded invoice-financing demonstration

**Reader:** Backend engineer exploring an accounting-backed lending use case with product planners

**Outcome:** Follow a demonstration from accounting connection to data-backed decision without mistaking it for a complete lending product.

| Stage | Inspected sources | Coverage and limit |
| --- | --- | --- |
| scope and concepts | [codat-invoice-guide](https://docs.codat.io/lending/guides/invoice-finance/introduction/) | **inspected** — Audience, sample outcome and exclusions are explicit. |
| access | [codat-invoice-setup](https://docs.codat.io/lending/guides/invoice-finance/setting-up/) | **partial** — Testing account and auth-flow configuration are inspected; full production authorization is not. |
| workflow | [codat-invoice-setup](https://docs.codat.io/lending/guides/invoice-finance/setting-up/), [codat-invoice-decision](https://docs.codat.io/lending/guides/invoice-finance/process-invoice/) | **inspected** — The walkthrough connects company creation, accounting data and the demonstration decision. |
| reference and events | [codat-invoice-decision](https://docs.codat.io/lending/guides/invoice-finance/process-invoice/) | **partial** — The guide distinguishes demo endpoints from platform operations; dedicated endpoint schemas were not inspected. |
| verification | [codat-invoice-setup](https://docs.codat.io/lending/guides/invoice-finance/setting-up/), [codat-invoice-decision](https://docs.codat.io/lending/guides/invoice-finance/process-invoice/) | **inspected** — The documented sandbox walkthrough and expected result are inspected; the demo was not run. |
| recovery | [codat-troubleshooting](https://docs.codat.io/lending/troubleshooting/), [codat-freshness](https://docs.codat.io/using-the-api/queueing-data-syncs/) | **partial** — Data state and error causes are inspected; the catalog does not supply every corrective procedure. |
| change | Not traced | **untraced** — Release/migration guidance for this demonstration is not traced. |

**Research jumps:** `screen-codat` → `codat-invoice-guide`; `codat-invoice-decision` → `codat-freshness`.

**Lesson:** Adjacent capabilities must keep their own prerequisites: the separately inspected reconciled-invoices feature requires banking plus accounting; this demo setup enables accounting and disables banking.

**Remaining limits:**

- Codat AR reconciliation is a separate comparison, not a prerequisite silently added to the financing demo.
- Dedicated operation schemas, full recovery and change guidance remain untraced.
- No account setup, demo execution or lending decision occurred.
