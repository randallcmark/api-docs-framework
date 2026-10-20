# Provisional pattern library

All initial patterns are observed proposals. Their full prescriptions are not yet corroborated, calibrated or task-tested. Source examples and project requirements inform the rules; benefits remain hypotheses to evaluate.

## P01 Route from business outcomes into implementation

Status: observed.

**Reader problem:** Product readers and engineers cannot locate a capability through endpoint names alone.

**Applies when:** A platform exposes multiple domains or integration paths.

**Rule:** Provide meaningful domain or outcome entry points and connect them to concepts, workflow guides and references. Reuse shared platform essentials.

**Discovery questions:**

- Which outcomes are supported now, and which are outside scope?
- Which integration choices change prerequisites or implementation?

**Evaluation:** Attempt to navigate from a stated business outcome to its conceptual explanation and implementation path. Record the route and missing links.

Rubric criteria: R01, R08.

Evidence: [E01](../research/evidence.md#e01-square-home), [E03](../research/evidence.md#e03-sumup-home), [E15](../research/evidence.md#e15-merge-accounting).

**Limits and comparisons still needed:** These examples use different routing levels. They do not establish the effectiveness of one universal navigation taxonomy. Full journeys and search need testing.

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

Evidence: [E07](../research/evidence.md#e07-gusto-onboarding), [E10](../research/evidence.md#e10-hibob-start), [E14](../research/evidence.md#e14-merge-hris), [E15](../research/evidence.md#e15-merge-accounting), [E17](../research/evidence.md#e17-hubspot-crm-model).

**Limits and comparisons still needed:** The sampled pages demonstrate parts of the model, not a complete universal structure. Data ownership questions also derive from this project's requirements.

## P03 Distinguish request success from workflow completion

Status: observed.

**Reader problem:** A successful API response can be mistaken for a completed business outcome.

**Applies when:** An operation creates an intermediate resource or a workflow includes asynchronous or human steps.

**Rule:** State what each operation accomplishes, what remains, and how readers can observe completion. Connect prerequisites, branches, operations and events as needed.

**Discovery questions:**

- What exactly does a successful response establish?
- Which state, event or other signal demonstrates completion?
- What must happen before the next step, and who performs it?

**Evaluation:** Trace the workflow to a supported observable completion condition. Reject unsupported claims of immediacy or readiness.

Rubric criteria: R03, R04, R06.

Evidence: [E02](../research/evidence.md#e02-square-create-order), [E05](../research/evidence.md#e05-revolut-checklist), [E07](../research/evidence.md#e07-gusto-onboarding).

**Limits and comparisons still needed:** The observed workflows differ. A synchronous one-call task needs only a concise expected result, not a manufactured state diagram.

## P04 Route authorization by actor and account context

Status: observed.

**Reader problem:** A generic token example can conceal differences between internal integrations and multi-customer partners.

**Applies when:** Access methods, account scope, deployment environment or permissions differ by integration model.

**Rule:** Identify the integration actor and account context before choosing credentials, consent and permissions. Explain transitions and limits only where supported.

**Discovery questions:**

- Is this accessing the client's own account or acting for multiple customers?
- Which permissions and account context does each operation require?
- What differs between sandbox and production or hosted and local tooling?

**Evaluation:** Check that a reader can choose the correct supported access path and that request examples preserve the intended account and scope.

Rubric criteria: R05, R11.

Evidence: [E04](../research/evidence.md#e04-sumup-mcp), [E10](../research/evidence.md#e10-hibob-start), [E14](../research/evidence.md#e14-merge-hris), [E16](../research/evidence.md#e16-stripe-mcp).

**Limits and comparisons still needed:** Authentication patterns are product-specific. These observations do not establish another platform's permission model.

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

Evidence: [E05](../research/evidence.md#e05-revolut-checklist), [E11](../research/evidence.md#e11-plaid-sandbox), [E12](../research/evidence.md#e12-adyen-testing).

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

Evidence: [E02](../research/evidence.md#e02-square-create-order), [E06](../research/evidence.md#e06-revolut-webhooks), [E13](../research/evidence.md#e13-github-rest-practices).

**Limits and comparisons still needed:** Never transfer exact retry delays, limits, signature algorithms or idempotency lifetimes from a reference provider.

## P07 Connect changes to applicability and reader action

Status: observed.

**Reader problem:** Readers know something changed but cannot determine impact or migrate safely.

**Applies when:** A capability, behavior, field, endpoint, availability or supported version changes.

**Rule:** Identify affected versions or audiences, changed behavior and required action; link factual change entries to migration instructions and relevant references.

**Discovery questions:**

- Who is affected and from which confirmed release or version?
- What breaks or changes behavior?
- What action and verification are required, and by when if a deadline exists?

**Evaluation:** Trace a change entry to its affected contract and concrete action. Separate a capability-oriented release explanation from a factual changelog and a migration procedure.

Rubric criteria: R04, R10.

Evidence: [E08](../research/evidence.md#e08-gusto-upgrade), [E09](../research/evidence.md#e09-gusto-changelog).

**Limits and comparisons still needed:** Only one provider and selected entries currently support this pattern. The release-note distinction is a proposed framework rule awaiting broader comparison.

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

Evidence: [E04](../research/evidence.md#e04-sumup-mcp), [E16](../research/evidence.md#e16-stripe-mcp).

**Limits and comparisons still needed:** The initial sample covers MCP content. SDK, CLI and skill-specific rules still need direct examples and testing.

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

Evidence: [E02](../research/evidence.md#e02-square-create-order), [E14](../research/evidence.md#e14-merge-hris), [E17](../research/evidence.md#e17-hubspot-crm-model).

**Limits and comparisons still needed:** Only one endpoint reference is inspected so far. Model guides and domain overviews supply related examples, not endpoint-level corroboration.
