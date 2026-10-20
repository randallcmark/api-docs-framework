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
| recovery | [gusto-errors](https://docs.gusto.com/embedded-payroll/docs/errors), [gusto-error-categories](https://docs.gusto.com/embedded-payroll/docs/error-categories) | **partial** — Category-specific messages and selected actions are inspected; complete onboarding recovery, retry safety and blocker resolution remain partial. |
| change | [gusto-upgrade](https://docs.gusto.com/embedded-payroll/docs/version-upgrade-guide), [gusto-changelog](https://docs.gusto.com/embedded-payroll/changelog/v2025-11-15) | **inspected** — Versioned impact and required migration actions are inspected, without independent release verification. |

**Research jumps:** `gusto-onboarding` → `gusto-company-events`.

**Lesson:** A status reference needs its workflow context; accepted setup, completed steps and business approval must remain distinct.

**Remaining limits:**

- No API calls, approval simulation or reader tests.
- Full prerequisite tax/bank/form references, blocker resolution and ambiguous-write recovery were not all followed.

## J02 Enterprise and embedded cross-border payouts

**Reader:** Product planner choosing an integration model and engineer building payouts

**Outcome:** Choose sender/account context, connect transfer resources, and understand tracking and testing boundaries.

| Stage | Inspected sources | Coverage and limit |
| --- | --- | --- |
| scope and concepts | [screen-wise](https://docs.wise.com/), [wise-send](https://docs.wise.com/guides/product/send-money) | **inspected** — Resources, partner models, corridors and changing requirements are explained. |
| access | [wise-enterprise](https://docs.wise.com/guides/product/send-money/use-cases/enterprise-payouts), [wise-embedded](https://docs.wise.com/guides/product/send-money/use-cases/embedded-payouts), [wise-oauth-setup](https://docs.wise.com/guides/developer/auth-and-security/oauth-2-setup) | **partial** — Integration-model token choice, invalidation, rotation and support diagnostics are inspected; certificates and complete onboarding are not. |
| workflow | [wise-enterprise](https://docs.wise.com/guides/product/send-money/use-cases/enterprise-payouts), [wise-embedded](https://docs.wise.com/guides/product/send-money/use-cases/embedded-payouts), [wise-send](https://docs.wise.com/guides/product/send-money) | **inspected** — Recipient-first and quote-first steps connect recipient, quote, transfer and funding. |
| reference and events | [wise-transfer-reference](https://docs.wise.com/api-reference/standard-transfer/transfercreate), [wise-tracking](https://docs.wise.com/guides/product/send-money/tracking/track-transfers) | **inspected** — A concrete transfer operation, event subscriptions, correlation and failure handling are inspected. |
| verification | [wise-statuses](https://docs.wise.com/guides/product/send-money/tracking/transfer-statuses), [wise-simulation](https://docs.wise.com/api-reference/simulation/simulationtransferstatechange), [wise-payout-failures](https://docs.wise.com/guides/product/send-money/tracking/payout-failures) | **inspected** — State and payout-failure simulation steps plus expected webhook are inspected, not executed. |
| recovery | [wise-tracking](https://docs.wise.com/guides/product/send-money/tracking/track-transfers), [wise-statuses](https://docs.wise.com/guides/product/send-money/tracking/transfer-statuses), [wise-payout-failures](https://docs.wise.com/guides/product/send-money/tracking/payout-failures), [wise-oauth-setup](https://docs.wise.com/guides/developer/auth-and-security/oauth-2-setup) | **partial** — Failure-event semantics, provider-retry code, fallback and support diagnostics inspected; full reconciliation and all caller recovery paths remain untraced. |
| change | [wise-changelog](https://docs.wise.com/changelog), [wise-global-versioning](https://docs.wise.com/guides/developer/global-versioning) | **partial** — Named replacement and token-model changes connect to policy; global versioning excludes webhooks. Full integration migration is not traced. |

**Research jumps:** None among the recorded connections.

**Lesson:** Common workflow structure can coexist with materially different sender, funding and customer-profile responsibilities.

**Remaining limits:**

- No live/sandbox API calls, token flow or reader tests.
- Full certificate setup, reconciliation and selected-version/event migration are not traced.

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
| recovery | [personio-events](https://developer.personio.de/docs/event-driven-data-from-personio), [personio-handling](https://developer.personio.de/docs/handling-logic), [personio-handling-v2](https://developer.personio.de/v2.0/docs/handling-logic) | **partial** — Three linked diagrams visually inspected (M01–M03); captured versioned and unversioned Markdown bodies are identical. Branch details and an offboarding end-label ambiguity remain; no complete handler/recovery validation. |
| change | [personio-change](https://developer.personio.de/changelog/deprecation-of-attendances-and-projects-v1-endpoints) | **partial** — Attendance/project migration is inspected as an adjacent shift-planning concern; not a complete migration of this whole integration. |

**Research jumps:** `personio-events` → `personio-handling`.

**Lesson:** An integration guide can expose product decisions about roles, eligibility, custom fields and termination behavior that schemas leave unexplained.

**Remaining limits:**

- No event handler, sandbox workflow or reader test.
- Authentication destination and all exact event contracts remain partially traced.
- Diagram end-label ambiguity is recorded, not corrected by inference; equality of two handling-guide captures does not establish all versioned-route equivalence.

## J04 Create CRM records and connect relationships

**Reader:** Client or multi-account partner planner and integration engineer

**Outcome:** Understand CRM entities, select an access model and implement record/relationship operations.

| Stage | Inspected sources | Coverage and limit |
| --- | --- | --- |
| scope and concepts | [hubspot-crm-model](https://developers.hubspot.com/docs/api-reference/latest/crm/understanding-the-crm) | **inspected** — Objects, records, properties, relationships and identifier scope are explained. |
| access | [hubspot-auth](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/overview) | **inspected** — Single-account static access and multi-account OAuth are distinguished. |
| workflow | [hubspot-objects](https://developers.hubspot.com/docs/api-reference/latest/crm/using-object-apis) | **inspected** — Creation and retrieval connect required object properties and associations. |
| reference and events | [hubspot-associations](https://developers.hubspot.com/docs/api-reference/latest/crm/associations/associate-records/guide) | **inspected** — Relationship direction, category/type discovery and request examples are inspected; events are outside the selected task. |
| verification | [hubspot-test-account-walkthrough](https://developers.hubspot.com/blog/how-to-safely-experiment-with-ai-in-hubspot-before-you-touch-real-data) | **partial** — Official walkthrough covers test-account setup, seeded data and single-record results, but is an AI/workflow example; a REST record/association test procedure remains untraced. |
| recovery | [hubspot-errors](https://developers.hubspot.com/docs/api-reference/error-handling) | **inspected** — Access errors, transient errors and batch partial-success guidance are inspected, without execution. |
| change | [hubspot-objects](https://developers.hubspot.com/docs/api-reference/latest/crm/using-object-apis), [hubspot-validation-change](https://developers.hubspot.com/changelog/crm-api-write-validation-enforcement) | **partial** — Linked validation notice names account conditions, affected version, input/permission actions and corrected retries. Full date-based version migration is not inspected. |

**Research jumps:** `screen-hubspot` → `hubspot-crm-model`; `hubspot-auth` → `hubspot-test-account-walkthrough`.

**Lesson:** Reference usability depends on semantic identifiers, relationship direction and distribution-aware access, not field descriptions alone.

**Remaining limits:**

- No account setup, API calls or reader test.
- REST record/association verification and complete date-based migration remain untraced.
- Current association navigation behavior has not been interactively verified.

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
| recovery | [codat-troubleshooting](https://docs.codat.io/lending/troubleshooting/), [codat-freshness](https://docs.codat.io/using-the-api/queueing-data-syncs/), [codat-data-troubleshooting](https://docs.codat.io/using-the-api/get-data-troubleshooting) | **partial** — Validation-log applicability and freshness prerequisites inspected; the additional page covers one warning, not all stale/failed dataset recovery. |
| change | [codat-change-policy](https://docs.codat.io/using-the-api/change-policy) | **partial** — Platform compatibility, notice and opt-in policy inspected; invoice-financing-specific change applicability/migration remains untraced. |

**Research jumps:** `screen-codat` → `codat-invoice-guide`; `codat-invoice-decision` → `codat-freshness`.

**Lesson:** Adjacent capabilities must keep their own prerequisites: the separately inspected reconciled-invoices feature requires banking plus accounting; this demo setup enables accounting and disables banking.

**Remaining limits:**

- No demo execution, production authorization setup or reader test.
- Exact operation/event contracts and feature-specific migration remain partial.
- Adjacent reconciled-invoice prerequisites cannot be assumed for this accounting-only demo.
