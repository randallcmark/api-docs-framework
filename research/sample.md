# Initial research sample

This sample tests the research method and produces provisional guidance. It does not rank providers, establish commercial success, measure developer outcomes, or complete the wider comparative study.

## Coverage

The [candidate index](candidates.md) contains 36 providers across six groups. The [selected source index](sources.md) records 18 captured pages from 12 providers. Relevant passages from 17 pages across 11 providers were inspected. Xero returned a JavaScript shell and contributes no substantive observation.

The [evidence index](evidence.md) binds observations to source URLs, section locators, capture hashes and limitations. The [pattern library](../patterns/library.md) contains nine provisional patterns. All remain observed proposals: no complete prescription is yet claimed corroborated, calibrated or task-tested.

| Area | Initial evidence | What remains |
| --- | --- | --- |
| Entry points and domains | Square and SumUp entry pages; Merge accounting links | Trace downstream journeys, direct-client/partner routes, search and navigation effectiveness |
| Concepts | HubSpot CRM definitions; HiBob and Merge domain organization | More ownership, lifecycle, identifier and cross-domain explanations |
| Workflows | Gusto company onboarding; Revolut payment checklist | Compare complete journeys across HR, banking and business software |
| References and events | Square order creation; Revolut webhook guidance | More endpoints, fields and event contracts, including conditional fields, units, time and pagination |
| Testing and operation | Plaid sandbox limits; Adyen integration testing; GitHub REST practices | Follow troubleshooting and recovery paths and test representative reader tasks |
| Change communication | Gusto upgrade guide and one release changelog | Independent providers, capability-oriented release notes, and domain additions |
| Tooling | SumUp and Stripe MCP guides | Direct CLI, skills and SDK setup examples; actual setup testing where appropriate |

## Practices worth testing

**Route readers by business purpose.** Square groups APIs into business areas, while SumUp offers routes for choosing an integration, accepting a first payment, testing and operating it. Merge's accounting overview links domain data to business use cases. These suggest providing entry points that connect a product question with implementation, while leaving the best taxonomy to reader-task testing. [Square](https://developer.squareup.com/docs), [SumUp](https://developer.sumup.com/), [Merge accounting](https://docs.merge.dev/merge-unified/accounting/overview).

**Explain business meaning and completion.** HubSpot defines CRM entities and identifier scope. Gusto's onboarding guide distinguishes prerequisites, sequence and completion conditions, including review after submission. Square's order reference distinguishes creating an order from paying for it. Together these motivate asking what a resource represents and what a successful operation actually establishes. [HubSpot concepts](https://developers.hubspot.com/docs/api-reference/latest/crm/understanding-the-crm), [Gusto onboarding](https://docs.gusto.com/embedded-payroll/docs/onboard-a-company), [Square order creation](https://developer.squareup.com/reference/square/orders-api/create-order).

**Identify the integration actor before prescribing access.** HiBob routes internal customer integrations and marketplace partners differently. Merge explains account-specific request context. These are examples of why the discovery brief must establish who acts for whom; they are not permission models to copy. [HiBob](https://apidocs.hibob.com/reference/getting-started-with-bob-api), [Merge HRIS](https://docs.merge.dev/merge-unified/hris/overview).

**Make verification and recovery specific.** Revolut's checklist names expected business results. Plaid limits what its sandbox establishes about production. Adyen connects client, server and webhook testing. GitHub describes conditional handling of rate-limit errors; Revolut's webhook guidance describes delivery caveats. The reusable principle is to obtain actual conditions and guarantees, not transplant provider-specific timings or behaviors. [Revolut checklist](https://developer.revolut.com/docs/guides/merchant/test-and-go-live/testing/implementation-checklists), [Plaid sandbox](https://plaid.com/docs/sandbox/), [Adyen testing](https://docs.adyen.com/development-resources/testing/), [GitHub REST guidance](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api), [Revolut events](https://developer.revolut.com/docs/guides/manage-accounts/webhooks/about-webhooks).

**Treat change and tooling as reader tasks.** Gusto connects change entries with affected endpoints and migration actions. SumUp and Stripe explain MCP setup, authentication choices and access to documentation versus account tools. The sample supports researching these as complete tasks, rather than adding generic resource pages. [Gusto upgrade guide](https://docs.gusto.com/embedded-payroll/docs/version-upgrade-guide), [Gusto changelog example](https://docs.gusto.com/embedded-payroll/changelog/v2025-11-15), [SumUp MCP](https://developer.sumup.com/tools/llms/mcp-server), [Stripe MCP](https://docs.stripe.com/mcp).

## Counterexample and collection limitation

Merge's captured HRIS overview states a base URL ending in `/v1`, while its sample curl path omits that segment. Record this as an apparent documentation inconsistency requiring investigation, not proof the endpoint fails. An example provider can supply a useful practice and still contain errors. The framework must evaluate individual claims. See E14 in the [evidence index](evidence.md#e14-merge-hris).

Xero's selected page returned HTTP 200 but only a JavaScript enablement message. The capture remains in the registry, with inspection state `unusable_shell`. The search result's richer text is not substituted for an inspected page. A later supported rendering or alternate official representation is needed.

## Worked pattern chain

Pattern P03 asks authors to distinguish request success from workflow completion:

1. **Observation:** external examples explain intermediate operations and later business outcomes.
2. **Proposed rule:** identify what success establishes and the evidence of completion.
3. **Discovery question:** does accepted onboarding mean review started, review completed, or payroll can run?
4. **Platform answer:** obtain this from that platform's owners and technical evidence; external examples do not answer it.
5. **Evaluation:** compare the actual draft with those answers and the contract; flag unsupported immediacy, status or readiness claims.

The [fictional payroll example](../examples/payroll-onboarding/README.md) demonstrates this chain, including a brief, source fixture, revised MDX, findings and a focused PR review packet. It is not a test on the user's evaluation platform.

## Next research priorities

Complete candidate screening and choose deeper examples with recorded reasons. Trace connected HR, banking and business-management journeys; increase direct-client and partner coverage. Add endpoint and event references, troubleshooting/support, release notes and migration comparisons, and CLI/skills material. Seek counterexamples and record question/review effort before promoting any pattern or numerical score.
