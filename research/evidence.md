# Inspected evidence

These are observations from selected passages, not provider ratings, runtime tests, or proof of reader benefit. Each observation is bound to a captured body hash in `evidence.json`.

## E01 square-home

Source: [Square — platform-entry](https://developer.squareup.com/docs). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `API groups`.

The entry page groups APIs by business area and offers shared developer tools and community resources.

Limit: This demonstrates organization and routing on the entry page; linked journey usability has not been tested.

Pattern links: P01.

## E02 square-create-order

Source: [Square — api-reference](https://developer.squareup.com/reference/square/orders-api/create-order). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `idempotency_key`.

The order-creation reference distinguishes creating an order from paying for it, links the related guide, identifies permissions, and explains reusing an idempotency key after uncertainty.

Limit: No request was executed. This does not establish retry behavior for other operations or platforms.

Pattern links: P03, P06, P09.

## E03 sumup-home

Source: [SumUp — platform-entry](https://developer.sumup.com/). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `Accept Online Payments`.

The entry page routes readers through choosing an integration, making a first payment, testing, authorization, API reference and agent resources.

Limit: Navigation labels were inspected, not complete downstream journeys or search effectiveness.

Pattern links: P01.

## E04 sumup-mcp

Source: [SumUp — agent-tooling](https://developer.sumup.com/tools/llms/mcp-server). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `Verify the Connection`.

The MCP guide distinguishes hosted OAuth from local API-key setup, names client/runtime requirements, provides verification guidance and addresses connection failures.

Limit: Tool installation and account access were not exercised. Documentation resources and tools that change account data are distinct capabilities.

Pattern links: P04, P08.

## E05 revolut-checklist

Source: [Revolut — production-readiness](https://developer.revolut.com/docs/guides/merchant/test-and-go-live/testing/implementation-checklists). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `Order's state is completed.`.

The implementation checklist groups sandbox scenarios, identifies optional checks, and gives expected business results for order, refund and webhook flows.

Limit: This is a merchant payment checklist; its specific states and scenarios are not a general payroll or banking contract.

Pattern links: P03, P05.

## E06 revolut-webhooks

Source: [Revolut — events](https://developer.revolut.com/docs/guides/manage-accounts/webhooks/about-webhooks). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `Webhook notifications might occasionally be sent more than once.`.

The event guide identifies API-version applicability, duplicate and ordering caveats, retry behavior, failed-event retrieval, and signature validation.

Limit: These are documented provider guarantees and caveats, not observed deliveries. Exact timings and algorithms cannot be transferred to another API.

Pattern links: P06.

## E07 gusto-onboarding

Source: [Gusto — workflow](https://docs.gusto.com/embedded-payroll/docs/onboard-a-company). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `### Step-by-step requirements`.

The company onboarding guide connects prerequisites, ordered and parallel steps, linked operations, unblock/completion conditions, and an approval stage after submission.

Limit: No payroll onboarding was executed. Provider-specific tax, legal and timing rules do not transfer.

Pattern links: P02, P03.

## E08 gusto-upgrade

Source: [Gusto — migration](https://docs.gusto.com/embedded-payroll/docs/version-upgrade-guide). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `Implement pagination handling.`.

The upgrade guide associates versioned breaking changes with affected endpoints and concrete required client changes.

Limit: Only selected migration entries were inspected. Published version dates are not independently verified release availability.

Pattern links: P07.

## E09 gusto-changelog

Source: [Gusto — changelog](https://docs.gusto.com/embedded-payroll/changelog/v2025-11-15). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `## Endpoint updates`.

A concrete version changelog identifies breaking changes, names affected endpoints, and links versioning and upgrade guidance.

Limit: This is one historical release entry; release-note quality and completeness across the platform remain unassessed.

Pattern links: P07.

## E10 hibob-start

Source: [HiBob — audience-routing](https://apidocs.hibob.com/reference/getting-started-with-bob-api). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `## Connect to Bob API`.

The start page distinguishes internal customer integrations from marketplace partners in its authorization routing, then organizes references by HR module.

Limit: The linked authorization procedures were not executed or fully reviewed.

Pattern links: P02, P04.

## E11 plaid-sandbox

Source: [Plaid — testing](https://plaid.com/docs/sandbox/). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `#### Differences between Sandbox and Production`.

The sandbox guide describes configurable test scenarios and explicitly limits what sandbox data and institution behavior establish about production.

Limit: No sandbox or production behavior was exercised. Differences are product-specific.

Pattern links: P05, P12.

## E12 adyen-testing

Source: [Adyen — testing](https://docs.adyen.com/development-resources/testing/). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `Test your integration`.

The testing guide requires client/server integration and webhooks, connects payment tests to expected server behavior, and links result-code and scenario guidance.

Limit: Linked scenario details were not all inspected. This does not establish a universal go-live checklist.

Pattern links: P05.

## E13 github-rest-practices

Source: [GitHub — operations](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `## Handle rate limit errors appropriately`.

REST guidance distinguishes retry conditions using response headers and warns against repeatedly ignoring errors.

Limit: The headers and retry policy are specific to GitHub; no rate-limit experiment was run.

Pattern links: P06.

## E14 merge-hris

Source: [Merge — domain-overview](https://docs.merge.dev/merge-unified/hris/overview). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `## Sync frequency`.

The HRIS overview explains account-scoped authentication, synchronization cadence versus completion time, and links provider-field coverage and use cases.

Limit: The stated base URL includes /v1 while the shown curl path omits that segment. This is an apparent inconsistency to investigate, not a confirmed endpoint failure. Linked coverage was not audited.

Pattern links: P02, P04, P09, P10.

## E15 merge-accounting

Source: [Merge — domain-overview](https://docs.merge.dev/merge-unified/accounting/overview). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `**Related use cases:**`.

The accounting overview connects a domain API to invoice creation, financial analysis and vendor reconciliation use cases, alongside synchronization guidance.

Limit: The linked workflows were not traced. Merge HRIS and accounting count as one provider for corroboration.

Pattern links: P01, P02.

## E16 stripe-mcp

Source: [Stripe — agent-tooling](https://docs.stripe.com/mcp). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `## Manage MCP access and sessions`.

The MCP guide provides client setup paths and explains account/environment permissions, authentication choices, session revocation and available tools.

Limit: No tools were installed or called. Setup and account-changing capabilities require separate evaluation.

Pattern links: P04, P08.

## E17 hubspot-crm-model

Source: [HubSpot — concepts](https://developers.hubspot.com/docs/api-reference/latest/crm/understanding-the-crm). Inspected 2026-10-20T19:55:07.856305+00:00.

Locator: `### Unique identifiers and record IDs`.

The CRM guide defines objects, records, properties and associations before connecting these concepts to APIs and explaining identifier scope.

Limit: No CRM calls were made. This conceptual page is not evidence that all guides or examples use identifiers consistently.

Pattern links: P02, P09.

## E18 screen-stripe

Source: [Stripe — screening-entry](https://docs.stripe.com/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `## Browse by product`.

The entry combines outcome-specific starting points with business product groups and development/agent routes.

Limit: Only entry routing is assessed, not conversion or complete task success.

Pattern links: P01.

## E19 screen-revolut

Source: [Revolut — screening-entry](https://developer.revolut.com/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Use cases`.

The entry routes merchant, business-account and open-banking use cases separately and names payment and reconciliation outcomes.

Limit: Capability labels are documented positioning, not independently tested implementation.

Pattern links: P01.

## E20 wise-send

Source: [Wise — workflow](https://docs.wise.com/guides/product/send-money). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Recipient and transfer requirements`.

The send guide explains recipients, quotes, transfers and funding, integration-model differences and dynamically retrieved corridor requirements.

Limit: No transfer was created. Specific financial or regulatory requirements must come from the target platform.

Pattern links: P01, P02, P03, P09.

## E21 wise-enterprise

Source: [Wise — workflow](https://docs.wise.com/guides/product/send-money/use-cases/enterprise-payouts). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Before you begin`.

Enterprise payout guidance identifies the organization as legal sender and funding owner, then connects alternate step sequences to tracking and pitfalls.

Limit: The enterprise model is provider-specific and does not establish another platform's access or legal obligations.

Pattern links: P03, P04.

## E22 wise-embedded

Source: [Wise — workflow](https://docs.wise.com/guides/product/send-money/use-cases/embedded-payouts). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Before you begin`.

Embedded payout guidance identifies customer profile and verification prerequisites and ties recipients, transfers and funds to that customer context.

Limit: No customer was onboarded; contractual integration scope remains a prerequisite in the source.

Pattern links: P02, P03, P04.

## E23 wise-tracking

Source: [Wise — operations](https://docs.wise.com/guides/product/send-money/tracking/track-transfers). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Webhook ordering is not guaranteed`.

Transfer tracking connects asynchronous processing with event subscriptions, correlation identifiers, ordering caveats and failure/refund handling.

Limit: Payloads and delivery guidance were inspected but no webhook receiver was run.

Pattern links: P03, P06, P10.

## E24 wise-statuses

Source: [Wise — concepts](https://docs.wise.com/guides/product/send-money/tracking/transfer-statuses). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Testing transfer statuses`.

Status definitions distinguish sent funds from recipient receipt and explain exceptional transitions and sandbox simulation conditions.

Limit: No simulation or bank delivery was tested. A final documented state is scoped to the provider's own observable outcome.

Pattern links: P03, P05, P11.

## E25 wise-transfer-reference

Source: [Wise — api-reference](https://docs.wise.com/api-reference/standard-transfer/transfercreate). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Avoiding duplicate transfers`.

The transfer reference connects resource relationships, changing conditional requirements and duplicate prevention to concrete field semantics.

Limit: No endpoint was called; the documented idempotency field does not establish policy for other APIs.

Pattern links: P06, P09.

## E26 wise-simulation

Source: [Wise — testing](https://docs.wise.com/api-reference/simulation/simulationtransferstatechange). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Fund the transfer first before calling any simulation`.

The simulation reference gives valid transition prerequisites, excludes unsupported cases and provides a concrete sandbox operation.

Limit: An inspected simulation procedure is not an executed test or production equivalence.

Pattern links: P05.

## E27 gusto-quickstart

Source: [Gusto — workflow](https://docs.gusto.com/embedded-payroll/docs/quickstart). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `## Troubleshooting`.

The quickstart connects developer organization/application setup to a first company, company-specific tokens, a short symptom table and deeper guidance.

Limit: No developer account was created and the five-minute label was not measured.

Pattern links: P03, P04, P06, P12.

## E28 gusto-auth

Source: [Gusto — authentication](https://docs.gusto.com/embedded-payroll/docs/authentication-and-authorization). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `## Company access tokens`.

Access guidance separates application-level and company-level actions, company boundaries, expiration and refresh.

Limit: Public example credentials are illustrative; none were used. Current availability needs target-platform evidence.

Pattern links: P04.

## E29 gusto-errors

Source: [Gusto — troubleshooting](https://docs.gusto.com/embedded-payroll/docs/errors). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `### Nested Error Shape`.

Error guidance explains category, location and resource metadata, including bulk and nested error structures.

Limit: These are contract shapes; complete symptom-to-recovery decisions require additional category guidance.

Pattern links: P06, P09.

## E30 gusto-company-events

Source: [Gusto — events](https://docs.gusto.com/embedded-payroll/docs/company-events). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `company.suspended`.

Company event descriptions distinguish a suspension being created from becoming effective, and separately name approval and onboarding events.

Limit: No event was delivered. The distinction is documentation evidence about business timing, not another provider's state model.

Pattern links: P03, P11.

## E31 gusto-status-reference

Source: [Gusto — api-reference](https://docs.gusto.com/embedded-payroll/reference/get-v1-company-onboarding-status). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `onboarding_completed`.

The status reference describes overall completion and individual required steps, completion flags, timestamps and remaining requirements.

Limit: The guide and reference must be read together; a single field does not independently explain review or payroll readiness.

Pattern links: P03, P09.

## E32 personio-prerequisites

Source: [Personio — workflow](https://developer.personio.de/docs/introduction-and-prerequisites). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `## Introduction - Roles and scope of the integration`.

The shift-planning guide defines partner, customer and user roles and assigns different responsibilities to the HR product and partner app.

Limit: Role preferences and access prerequisites are specific to this integration example.

Pattern links: P02, P04.

## E33 personio-initial-sync

Source: [Personio — workflow](https://developer.personio.de/docs/initial-core-data-sync). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `### Fetch Employees`.

Initial synchronization guidance distinguishes persons from employments, limits which employees to sync and explains custom-attribute and location-model constraints.

Limit: No employee data was accessed. Initial population is one stage, not proof of ongoing consistency.

Pattern links: P02, P09, P10.

## E34 personio-events

Source: [Personio — events](https://developer.personio.de/docs/event-driven-data-from-personio). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `### Employee terminations and deletions`.

Event guidance connects changed employee/employment data, leave and termination variants to synchronization and product decisions.

Limit: Some event-trigger details are delegated to linked references; none were exercised.

Pattern links: P06, P10, P11.

## E35 personio-change

Source: [Personio — changelog](https://developer.personio.de/changelog/deprecation-of-attendances-and-projects-v1-endpoints). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `### Migration Guidance:`.

A deprecation announcement identifies the migration target, changed identifiers, approval defaults, overnight periods and required client adaptations.

Limit: Only this published change entry was inspected; its deadlines and release claims were not independently verified.

Pattern links: P07, P09, P11.

## E36 personio-person-reference

Source: [Personio — api-reference](https://developer.personio.de/v2.0/reference/get_v2-persons). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `The endpoint supports pagination and filtering`.

The persons reference explains filter combination, required scope and cursor pagination alongside the schema.

Limit: No request was executed and custom-attribute behavior still needs the surrounding guide.

Pattern links: P09.

## E37 personio-handling

Source: [Personio — workflow](https://developer.personio.de/docs/handling-logic). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `### Employee Onboarding & Offboarding Logic:`.

The handling page names update/onboarding/deletion scenarios and delegates detailed flowcharts to linked images.

Limit: Diagram contents were not inspected in this text-only pass. Detailed branch logic is untraced, not proven absent from the site.

Pattern links: .

## E38 hubspot-objects

Source: [HubSpot — api-guide](https://developers.hubspot.com/docs/api-reference/latest/crm/using-object-apis). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `## Create records`.

The object guide connects create/retrieve operations, record relationships, object-specific required properties and version-dependent validation.

Limit: Only selected operations were inspected; no CRM write was performed.

Pattern links: P03, P09.

## E39 hubspot-errors

Source: [HubSpot — troubleshooting](https://developers.hubspot.com/docs/api-reference/error-handling). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `## Multi-status errors`.

Error guidance distinguishes access and transient errors, optional diagnostic fields and batch partial success with per-input correlation.

Limit: Retry specifics vary by API; no error handling was executed.

Pattern links: P06, P09.

## E40 hubspot-associations

Source: [HubSpot — api-guide](https://developers.hubspot.com/docs/api-reference/latest/crm/associations/associate-records/guide). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `correct direction`.

Association guidance explains type/category discovery, relationship direction and the operations used to create labeled relationships.

Limit: A previous-version link appears to target the current guide; legacy navigation needs investigation rather than an assumption of distinct content.

Pattern links: P02, P09.

## E41 hubspot-auth

Source: [HubSpot — authentication](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/overview). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `## App authentication`.

Authentication is selected by distribution model: multi-account OAuth versus single-account static access, with local tooling treated separately.

Limit: This page scopes a particular developer platform; legacy app models should not be silently treated as identical.

Pattern links: P04.

## E42 codat-invoice-guide

Source: [Codat — workflow](https://docs.codat.io/lending/guides/invoice-finance/introduction/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `This guide does not cover`.

The invoice-finance introduction states audience, demonstration outcome, prerequisites and explicit exclusions, including production product design and due diligence.

Limit: The sample lending logic is not a production underwriting specification or financial recommendation.

Pattern links: P01, P12.

## E43 codat-invoice-setup

Source: [Codat — workflow](https://docs.codat.io/lending/guides/invoice-finance/setting-up/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Update your auth flow settings`.

Demo setup connects testing-account access, accounting-source configuration, webhooks and local environment prerequisites.

Limit: Setup was inspected but no account, webhook or demo application was run.

Pattern links: P03, P05, P12.

## E44 codat-invoice-decision

Source: [Codat — workflow](https://docs.codat.io/lending/guides/invoice-finance/process-invoice/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Receive the decision on the loan`.

The demo walkthrough connects application creation, company/accounting connection, fetched data and a returned decision, while distinguishing app endpoints from Codat operations.

Limit: The guide describes a constructed demo. Its happy path does not establish a complete lending product or all recovery behavior.

Pattern links: P03, P12.

## E45 codat-ar

Source: [Codat — workflow](https://docs.codat.io/lending/features/accounts-receivable-overview/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Feature components`.

The accounts-receivable overview explains invoice reconciliation and explicitly requires both accounting and banking sources for the reconciled-invoices feature.

Limit: That requirement belongs to this feature; the invoice-financing demo uses accounting data and must not inherit it automatically.

Pattern links: P01, P02, P10.

## E46 codat-freshness

Source: [Codat — operations](https://docs.codat.io/using-the-api/queueing-data-syncs/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Check data 'freshness'`.

Refresh guidance distinguishes queued work from completed sync, records per-dataset success information, explains deleted records and warns about comparing data synced at different times.

Limit: No synchronization was executed; freshness thresholds remain use-case-specific.

Pattern links: P03, P06, P10.

## E47 codat-troubleshooting

Source: [Codat — troubleshooting](https://docs.codat.io/lending/troubleshooting/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Lending error codes`.

The error table distinguishes unsupported, unsynced, disabled or failed datasets from missing connections and missing product enablement.

Limit: Some rows describe causes without a full recovery procedure; do not mistake an error catalog for complete troubleshooting.

Pattern links: P01, P06, P10.

## E48 sumup-cli

Source: [SumUp — cli](https://developer.sumup.com/tools/cli/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Set Your Merchant Context`.

CLI guidance connects installation verification, authentication, merchant context, operation commands, structured output and help.

Limit: No CLI was installed or account accessed; operation examples are documented demonstrations.

Pattern links: P08.

## E49 sumup-skills

Source: [SumUp — agent-skills](https://developer.sumup.com/tools/llms/agent-skills/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Install Standalone Skills`.

Skills guidance names task-specific instructions, installation/discovery paths and separates standalone guidance from MCP connection and credentials.

Limit: No skill was installed. Update and execution claims require separate evidence.

Pattern links: P08.

## E50 sumup-cli-release

Source: [SumUp — release-note](https://developer.sumup.com/changelog/sumup-cli). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `We are happy to announce the release`.

A capability-oriented CLI release entry describes supported tasks and links installation/authentication guidance and a specific upstream release.

Limit: A useful release entry can live inside a changelog; separate content functions do not require universally separate page names.

Pattern links: P07, P08.

## E51 stripe-skills

Source: [Stripe — agent-skills](https://docs.stripe.com/skills). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `## Manually install agent skills`.

Skill guidance distinguishes plugin-managed installation from manual installation and updating, and separates guidance from live account access through MCP.

Limit: No installation or update was run; product instructions describe the supported path at capture time.

Pattern links: P08.

## E52 stripe-cli-reference

Source: [Stripe — cli](https://docs.stripe.com/cli). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `## Install the Stripe CLI`.

The CLI reference explains setup, updating, credential removal and available tasks, linking command-level details rather than treating installation as the complete workflow.

Limit: Only selected setup/lifecycle passages in a long command reference were inspected. Commands were not run.

Pattern links: P08.

## E53 square-release-notes

Source: [Square — release-note](https://developer.squareup.com/docs/release-notes). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Release note types`.

The release overview separates API/server SDK, mobile SDK, web SDK and marketplace requirement changes by technology surface.

Limit: Only release organization is established; individual entries and subscription behavior were not assessed.

Pattern links: P07.

## E54 square-pay-orders

Source: [Square — workflow](https://developer.squareup.com/docs/orders-api/pay-for-orders). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Using the Orders API`.

Payment guidance explains choosing order versus payment operations, multiple authorized payments and conditional order/fulfillment completion.

Limit: No order was paid. Cross-domain effects and completion conditions are provider-specific.

Pattern links: P02, P03, P09.

## E55 github-troubleshooting

Source: [GitHub — troubleshooting](https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `## Missing results`.

Troubleshooting connects symptoms to pagination or access boundaries and gives conditional responses to rate-limit failures.

Limit: A symptom route is inspected, not a measured diagnostic success rate.

Pattern links: P06, P09.

## E56 cloudflare-api

Source: [Cloudflare — api-reference](https://developers.cloudflare.com/api/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `Organizations authentication limitations`.

Reference organization links credential compatibility and accepted permissions to specific operations instead of treating one authentication statement as universal.

Limit: Only the library overview and organization-access passage were inspected in the large reference index.

Pattern links: P04, P09.

## E57 cloudflare-api-change

Source: [Cloudflare — changelog](https://developers.cloudflare.com/changelog/post/2026-07-28-improved-record-display-format/). Inspected 2026-10-20T20:19:08.777386+00:00.

Locator: `These are breaking changes.`.

A change entry identifies an affected response field, mixed-format rollout, before/after examples and a stable-format alternative.

Limit: This DNS JSON compatibility example informs change communication, not HR or payment contract rules.

Pattern links: P07.
