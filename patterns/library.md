# Provisional pattern library

12 patterns: 4 corroborated, 8 observed. Corroboration means independent documentation examples support a practice; it does not establish calibration, task success or causal benefit. Source examples and project requirements inform these conditional rules.

## P01 Route from business outcomes into implementation

Status: corroborated.

**Reader problem:** Product readers and engineers cannot locate a capability through endpoint names alone.

**Applies when:** A platform exposes multiple domains or integration paths.

**Rule:** Provide meaningful domain or outcome entry points and connect them to concepts, workflow guides and references. Reuse shared platform essentials.

**Discovery questions:**

- Which outcomes are supported now, and which are outside scope?
- Which integration choices change prerequisites or implementation?

**Evaluation:** Attempt to navigate from a stated business outcome to its conceptual explanation and implementation path. Record the route and missing links.

Rubric criteria: R01, R08.

Evidence: [E01](../research/evidence.md#e01-square-home), [E03](../research/evidence.md#e03-sumup-home), [E15](../research/evidence.md#e15-merge-accounting), [E18](../research/evidence.md#e18-screen-stripe), [E19](../research/evidence.md#e19-screen-revolut), [E20](../research/evidence.md#e20-wise-send), [E42](../research/evidence.md#e42-codat-invoice-guide), [E45](../research/evidence.md#e45-codat-ar), [E47](../research/evidence.md#e47-codat-troubleshooting).

**Limits and comparisons still needed:** These examples use different routing levels. They do not establish the effectiveness of one universal navigation taxonomy. Full journeys and search need testing.

**Corroboration basis:** Square and SumUp business/outcome entry routes, Stripe task-specific starts, and Revolut use-case routes all link a product question toward implementation. Labels and exact information architectures differ; navigation effectiveness remains untested.

## P02 Establish the domain model before the call sequence

Status: observed.

**Reader problem:** Readers can execute calls without understanding what entities represent or how a workflow fits the product.

**Applies when:** The task depends on domain concepts, resource relationships or lifecycle interpretation.

**Rule:** Explain the task-relevant actors, entities, identifiers, relationships and states. Ask owners about source of truth and ownership where implementation evidence is insufficient.

**Discovery questions:**

- What does each resource represent in business terms?
- Which entity and account scope an identifier?
- Who owns each change and what marks the business outcome complete?

**Evaluation:** Have a reader explain the model and identify the correct entity and state for the task. Compare with technical evidence and approved product answers.

Rubric criteria: R02, R03, R08.

Evidence: [E07](../research/evidence.md#e07-gusto-onboarding), [E10](../research/evidence.md#e10-hibob-start), [E14](../research/evidence.md#e14-merge-hris), [E15](../research/evidence.md#e15-merge-accounting), [E17](../research/evidence.md#e17-hubspot-crm-model), [E20](../research/evidence.md#e20-wise-send), [E22](../research/evidence.md#e22-wise-embedded), [E32](../research/evidence.md#e32-personio-prerequisites), [E33](../research/evidence.md#e33-personio-initial-sync), [E40](../research/evidence.md#e40-hubspot-associations), [E45](../research/evidence.md#e45-codat-ar), [E54](../research/evidence.md#e54-square-pay-orders), [E60](../research/evidence.md#e60-personio-handling-v2).

**Limits and comparisons still needed:** The sampled pages demonstrate parts of the model, not a complete universal structure. Data ownership questions also derive from this project's requirements.

## P03 Distinguish request success from workflow completion

Status: corroborated.

**Reader problem:** A successful API response can be mistaken for a completed business outcome.

**Applies when:** An operation creates an intermediate resource or a workflow includes asynchronous or human steps.

**Rule:** State what each operation accomplishes, what remains, and how readers can observe completion. Connect prerequisites, branches, operations and events as needed.

**Discovery questions:**

- What exactly does a successful response establish?
- Which state, event or other signal demonstrates completion?
- What must happen before the next step, and who performs it?

**Evaluation:** Trace the workflow to a supported observable completion condition. Reject unsupported claims of immediacy or readiness.

Rubric criteria: R03, R04, R06.

Evidence: [E02](../research/evidence.md#e02-square-create-order), [E05](../research/evidence.md#e05-revolut-checklist), [E07](../research/evidence.md#e07-gusto-onboarding), [E20](../research/evidence.md#e20-wise-send), [E21](../research/evidence.md#e21-wise-enterprise), [E22](../research/evidence.md#e22-wise-embedded), [E23](../research/evidence.md#e23-wise-tracking), [E24](../research/evidence.md#e24-wise-statuses), [E27](../research/evidence.md#e27-gusto-quickstart), [E30](../research/evidence.md#e30-gusto-company-events), [E31](../research/evidence.md#e31-gusto-status-reference), [E38](../research/evidence.md#e38-hubspot-objects), [E43](../research/evidence.md#e43-codat-invoice-setup), [E44](../research/evidence.md#e44-codat-invoice-decision), [E46](../research/evidence.md#e46-codat-freshness), [E54](../research/evidence.md#e54-square-pay-orders), [E67](../research/evidence.md#e67-wise-payout-failures).

**Limits and comparisons still needed:** The observed workflows differ. A synchronous one-call task needs only a concise expected result, not a manufactured state diagram.

**Corroboration basis:** Square distinguishes order creation from payment/completion; Gusto distinguishes onboarding steps/submission from approval; Wise distinguishes transfer processing/sent funds from recipient receipt. These independently support separating operation success from the business completion condition.

## P04 Route authorization by actor and account context

Status: corroborated.

**Reader problem:** A generic token example can conceal differences between internal integrations and multi-customer partners.

**Applies when:** Access methods, account scope, deployment environment or permissions differ by integration model.

**Rule:** Identify the integration actor and account context before choosing credentials, consent and permissions. Explain transitions and limits only where supported.

**Discovery questions:**

- Is this accessing the client's own account or acting for multiple customers?
- Which permissions and account context does each operation require?
- What differs between sandbox and production or hosted and local tooling?

**Evaluation:** Check that a reader can choose the correct supported access path and that request examples preserve the intended account and scope.

Rubric criteria: R05, R11.

Evidence: [E04](../research/evidence.md#e04-sumup-mcp), [E10](../research/evidence.md#e10-hibob-start), [E14](../research/evidence.md#e14-merge-hris), [E16](../research/evidence.md#e16-stripe-mcp), [E21](../research/evidence.md#e21-wise-enterprise), [E22](../research/evidence.md#e22-wise-embedded), [E27](../research/evidence.md#e27-gusto-quickstart), [E28](../research/evidence.md#e28-gusto-auth), [E32](../research/evidence.md#e32-personio-prerequisites), [E41](../research/evidence.md#e41-hubspot-auth), [E56](../research/evidence.md#e56-cloudflare-api), [E59](../research/evidence.md#e59-wise-changelog), [E61](../research/evidence.md#e61-hubspot-validation-change), [E65](../research/evidence.md#e65-wise-oauth-setup).

**Limits and comparisons still needed:** Authentication patterns are product-specific. These observations do not establish another platform's permission model.

**Corroboration basis:** HiBob routes internal clients versus partners; Gusto separates system versus company context; Wise separates organizational and end-customer payout context; HubSpot selects access by distribution model. Each makes the integration actor/account context relevant to access.

## P05 Test the reader task and explain simulation limits

Status: observed.

**Reader problem:** A successful sample request does not establish that an integrated workflow works in production.

**Applies when:** The task has test environments, simulated data, asynchronous signals or consequential failure scenarios.

**Rule:** Describe relevant test setup, expected business results and representative failure cases, and state which production behaviors the environment cannot establish.

**Discovery questions:**

- How can a developer reproduce success and relevant failure?
- What must the backend, event consumer or UI observe?
- Which production constraints cannot be reproduced here?

**Evaluation:** Check that the test plan exercises the stated workflow and observable results. Record unexecuted examples and test-environment limits explicitly.

Rubric criteria: R06, R07.

Evidence: [E05](../research/evidence.md#e05-revolut-checklist), [E11](../research/evidence.md#e11-plaid-sandbox), [E12](../research/evidence.md#e12-adyen-testing), [E24](../research/evidence.md#e24-wise-statuses), [E26](../research/evidence.md#e26-wise-simulation), [E43](../research/evidence.md#e43-codat-invoice-setup), [E66](../research/evidence.md#e66-hubspot-test-account-walkthrough), [E67](../research/evidence.md#e67-wise-payout-failures).

**Limits and comparisons still needed:** A checklist, a sandbox caveat and an integration test guide support different parts of the rule. Do not copy payment-specific cases into HR tasks.

## P06 Describe recovery with actual guarantees and conditions

Status: observed.

**Reader problem:** Generic advice to retry can create duplicate effects, loops or incorrect state assumptions.

**Applies when:** The workflow encounters transient errors, ambiguous outcomes, events or synchronization.

**Rule:** Document applicable retry conditions, idempotency behavior, duplicate and ordering semantics, and diagnosis or reconciliation paths using platform evidence.

**Discovery questions:**

- Which operations are safe to repeat, with what key and scope?
- Can events repeat or arrive out of order?
- How should a caller distinguish rejection, acceptance and an unknown outcome?

**Evaluation:** Compare each operational claim with the contract, implementation and approved policy. Walk one relevant failure scenario to a concrete recovery or support action.

Rubric criteria: R04, R07.

Evidence: [E02](../research/evidence.md#e02-square-create-order), [E06](../research/evidence.md#e06-revolut-webhooks), [E13](../research/evidence.md#e13-github-rest-practices), [E23](../research/evidence.md#e23-wise-tracking), [E25](../research/evidence.md#e25-wise-transfer-reference), [E27](../research/evidence.md#e27-gusto-quickstart), [E29](../research/evidence.md#e29-gusto-errors), [E34](../research/evidence.md#e34-personio-events), [E39](../research/evidence.md#e39-hubspot-errors), [E46](../research/evidence.md#e46-codat-freshness), [E47](../research/evidence.md#e47-codat-troubleshooting), [E55](../research/evidence.md#e55-github-troubleshooting), [E58](../research/evidence.md#e58-gusto-error-categories), [E60](../research/evidence.md#e60-personio-handling-v2), [E61](../research/evidence.md#e61-hubspot-validation-change), [E63](../research/evidence.md#e63-codat-data-troubleshooting), [E65](../research/evidence.md#e65-wise-oauth-setup), [E67](../research/evidence.md#e67-wise-payout-failures).

**Limits and comparisons still needed:** Never transfer exact retry delays, limits, signature algorithms or idempotency lifetimes from a reference provider.

## P07 Connect changes to applicability and reader action

Status: corroborated.

**Reader problem:** Readers know something changed but cannot determine impact or migrate safely.

**Applies when:** A capability, behavior, field, endpoint, availability or supported version changes.

**Rule:** Identify affected versions or audiences, changed behavior and required action; link factual change entries to migration instructions and relevant references.

**Discovery questions:**

- Who is affected and from which confirmed release or version?
- What breaks or changes behavior?
- What action and verification are required, and by when if a deadline exists?

**Evaluation:** Trace a change entry to its affected contract and concrete action. Separate a capability-oriented release explanation from a factual changelog and a migration procedure.

Rubric criteria: R04, R10.

Evidence: [E08](../research/evidence.md#e08-gusto-upgrade), [E09](../research/evidence.md#e09-gusto-changelog), [E35](../research/evidence.md#e35-personio-change), [E50](../research/evidence.md#e50-sumup-cli-release), [E53](../research/evidence.md#e53-square-release-notes), [E57](../research/evidence.md#e57-cloudflare-api-change), [E58](../research/evidence.md#e58-gusto-error-categories), [E59](../research/evidence.md#e59-wise-changelog), [E61](../research/evidence.md#e61-hubspot-validation-change), [E62](../research/evidence.md#e62-codat-change-policy), [E64](../research/evidence.md#e64-wise-global-versioning).

**Limits and comparisons still needed:** Content functions can share a page or changelog. Provider naming does not determine structure. The impact-to-action rule is corroborated; exact release governance and review policy remain product-specific.

**Corroboration basis:** Gusto names affected endpoints and migration actions, Personio names affected API behaviors and required client adaptations, and Cloudflare identifies changed representation and a client alternative. This supports the impact-to-action rule; separate release-note/changelog filenames are not required.

## P08 Document the complete tooling setup path

Status: observed.

**Reader problem:** Installation snippets omit access choices, verification, supported contexts or recovery.

**Applies when:** A supported SDK, CLI, skill, MCP server or other developer tool is relevant to the reader task.

**Rule:** Explain purpose, prerequisites, installation or connection, environment and access choice, verification, and common failures. Distinguish documentation access from tools that read or change platform data.

**Discovery questions:**

- Which tool exists and which task does it support?
- Which client/runtime versions, environment and credentials are supported?
- How can the reader verify setup with a low-impact action and revoke access where applicable?

**Evaluation:** Follow the relevant supported setup path using documented prerequisites when an environment is available. Otherwise assess content and label execution unverified.

Rubric criteria: R05, R06, R11.

Evidence: [E04](../research/evidence.md#e04-sumup-mcp), [E16](../research/evidence.md#e16-stripe-mcp), [E48](../research/evidence.md#e48-sumup-cli), [E49](../research/evidence.md#e49-sumup-skills), [E50](../research/evidence.md#e50-sumup-cli-release), [E51](../research/evidence.md#e51-stripe-skills), [E52](../research/evidence.md#e52-stripe-cli-reference).

**Limits and comparisons still needed:** CLI and skill examples are inspected alongside MCP; complete setup, revocation and troubleshooting still need execution and task-specific comparison. Static instructions do not establish data access or installed tools.

## P09 Explain reference semantics beyond field types

Status: observed.

**Reader problem:** Schema-shaped references omit why or how an operation or field participates in a business task.

**Applies when:** Readers must choose operations, identifiers, fields or options to implement the task.

**Rule:** Explain business effect, consequential conditions and scope, applicable side effects and recovery semantics; connect reference entries to relevant concepts and workflows.

**Discovery questions:**

- What does this operation achieve and what does it leave for later?
- Which field conditions, identifier scopes, units or defaults affect the outcome?
- Where can a reader see the surrounding workflow?

**Evaluation:** Use the reference to answer a task-specific choice the schema alone cannot answer. Compare examples with the contract and implementation; investigate inconsistencies.

Rubric criteria: R02, R04, R08.

Evidence: [E02](../research/evidence.md#e02-square-create-order), [E14](../research/evidence.md#e14-merge-hris), [E17](../research/evidence.md#e17-hubspot-crm-model), [E20](../research/evidence.md#e20-wise-send), [E25](../research/evidence.md#e25-wise-transfer-reference), [E29](../research/evidence.md#e29-gusto-errors), [E31](../research/evidence.md#e31-gusto-status-reference), [E33](../research/evidence.md#e33-personio-initial-sync), [E35](../research/evidence.md#e35-personio-change), [E36](../research/evidence.md#e36-personio-person-reference), [E38](../research/evidence.md#e38-hubspot-objects), [E39](../research/evidence.md#e39-hubspot-errors), [E40](../research/evidence.md#e40-hubspot-associations), [E54](../research/evidence.md#e54-square-pay-orders), [E55](../research/evidence.md#e55-github-troubleshooting), [E56](../research/evidence.md#e56-cloudflare-api).

**Limits and comparisons still needed:** Only one endpoint reference is inspected so far. Model guides and domain overviews supply related examples, not endpoint-level corroboration.

## P10 Explain synchronization and data freshness

Status: observed.

**Reader problem:** An integration can return data successfully while using incomplete, stale or mutually inconsistent datasets.

**Applies when:** A workflow reads replicated data, aggregates sources or synchronizes changes between systems.

**Rule:** Explain initial and incremental synchronization, ownership, relevant freshness/completeness signals, deletion and reconnection behavior, and how the workflow detects or recovers from incomplete data. Do not invent an acceptable lag.

**Discovery questions:**

- Which system owns each field and change?
- What establishes a complete initial sync, and what triggers later updates?
- Which datasets must be coherent for this outcome, and what lag is acceptable?
- How are deletions, terminations, rehires and lost connections handled?
- Do diagrams and machine-readable or versioned pages preserve the same decision-critical branches?

**Evaluation:** Trace initial data and one relevant update or deletion through to the consumer. Check whether the reader can distinguish no data, inaccessible data, unsupported capability, in-progress sync and failed sync.

Rubric criteria: R01, R02, R03, R06, R07.

Evidence: [E14](../research/evidence.md#e14-merge-hris), [E23](../research/evidence.md#e23-wise-tracking), [E33](../research/evidence.md#e33-personio-initial-sync), [E34](../research/evidence.md#e34-personio-events), [E45](../research/evidence.md#e45-codat-ar), [E46](../research/evidence.md#e46-codat-freshness), [E47](../research/evidence.md#e47-codat-troubleshooting), [E60](../research/evidence.md#e60-personio-handling-v2), [E63](../research/evidence.md#e63-codat-data-troubleshooting).

**Limits and comparisons still needed:** Merge describes cadence, Personio describes employment synchronization, and Codat explains dataset coherence. They cover different parts of the rule; domain owners must supply lag and ownership requirements. Personio diagram inspection establishes that branching is absent from surrounding prose, not that every renderer loses the images or that all versioned routes agree.

## P11 Make business time and state meaning explicit

Status: observed.

**Reader problem:** Readers confuse recorded changes, effective changes, delivered events and the eventual business outcome.

**Applies when:** A task has effective dates, asynchronous states, scheduled changes, rollbacks or cross-day time periods.

**Rule:** Define the relevant timestamps, business dates and state meanings, including what a signal does and does not establish. Explain applicable ordering, effective-date and exceptional-transition behavior.

**Discovery questions:**

- When does a change take effect versus become recorded or delivered?
- Which timezone or business date governs the outcome?
- Can a terminal-looking state reverse, or mean something less than end-user completion?
- How should clients interpret overnight periods or scheduled transitions?

**Evaluation:** Choose a relevant boundary case, such as future-effective suspension, overnight work or a payout that is sent but not received. Verify that the documented interpretation matches platform evidence.

Rubric criteria: R02, R03, R04, R06, R07.

Evidence: [E24](../research/evidence.md#e24-wise-statuses), [E30](../research/evidence.md#e30-gusto-company-events), [E34](../research/evidence.md#e34-personio-events), [E35](../research/evidence.md#e35-personio-change).

**Limits and comparisons still needed:** The sampled sources illustrate distinct time/state boundaries. This is a proposed conditional rule, not a universal lifecycle or date-format prescription.

## P12 State the boundary of a demonstration

Status: observed.

**Reader problem:** Readers or agents treat a quickstart or sandbox happy path as a complete production product or integration.

**Applies when:** A guide uses a demo, simplified authorization, simulated data or a deliberately narrow example.

**Rule:** State what the example establishes, its prerequisites and exclusions, which steps are simplified, and where the production workflow differs. Link the next relevant implementation or verification guidance.

**Discovery questions:**

- Which outcome is this example actually demonstrating?
- What production responsibilities or decisions does it omit?
- Which credentials, data, approval or failure paths are simplified?

**Evaluation:** Ask what a reader could wrongly infer from completing the example. Confirm that consequential exclusions and production differences are explicit and linked to the right next task.

Rubric criteria: R01, R03, R06, R09.

Evidence: [E11](../research/evidence.md#e11-plaid-sandbox), [E27](../research/evidence.md#e27-gusto-quickstart), [E42](../research/evidence.md#e42-codat-invoice-guide), [E43](../research/evidence.md#e43-codat-invoice-setup), [E44](../research/evidence.md#e44-codat-invoice-decision), [E66](../research/evidence.md#e66-hubspot-test-account-walkthrough).

**Limits and comparisons still needed:** Scope statements in public examples do not prove that readers notice or understand the boundaries; reader-task testing is still required.
