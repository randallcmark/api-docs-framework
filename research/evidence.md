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

Pattern links: P05.

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

Pattern links: P02, P04, P09.

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
