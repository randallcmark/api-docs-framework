# Project brief

## Objective

Help engineers and agents assess and improve REST platform documentation using evidence-backed patterns, guided product discovery, and independent evaluation. Readers must be able to assess a capability, understand the conceptual model, plan an integrated workflow, and implement and operate it.

## People and constraints

The author is usually an engineer working with an agent. Product and engineering owners can answer questions, but product requirements are often loose. Review is a small fraction of a few people's time, not a dedicated writing team.

Submissions currently arrive as PRs containing one or several lengthy MDX documents. Reviewers have no brief and must reconstruct the audience, domain, intent, and style expectations from the draft. The framework must reduce that reconstruction and the amount of corrective rewriting.

Readers include client product people planning capabilities, client engineers, and partners building scaled integrations. They share business outcomes but differ in account ownership, authorization, tenant boundaries, configuration, and operating responsibility.

## Available inputs

- OpenAPI specification, source code, and existing documentation.
- Answers from product and engineering owners.
- Research patterns, evaluation criteria, and previously recorded decisions.

Treat these inputs as evidence with scope, version, and possible disagreement. OpenAPI describes a contract, source reveals implementation, existing prose makes claims, and product answers establish intent. None alone establishes every aspect of current deployed behavior. A contradiction becomes a question; it is not silently resolved by source preference.

## Supported work

1. Evaluate and improve documentation for existing capabilities.
2. Document new use cases or domains and identify changes needed across existing content.
3. Maintain platform concepts, workflow guides, API references, troubleshooting, release notes, changelog, and migration guidance.
4. Document developer tooling where it exists: SDKs, CLI, skills, MCP, machine-readable documentation, and installation and configuration paths.

Generation must distinguish implemented behavior, approved intent, planned capability, and unresolved questions. Approved intent is not proof of availability. Missing platform capabilities become product gaps, not invented documentation.

## Content model

- **Platform:** audiences, vocabulary, account models, authentication, conventions, environments, tooling, support, versioning.
- **Domain:** concepts, resource relationships, lifecycles, constraints, permissions, failure modes.
- **Workflow:** intended outcome, actors, prerequisites, sequence, operations and events, observable completion, recovery, and operation across domains.
- **Page:** choose the appropriate form for a reader need. Introduction, overview, concept, use case, FAQ, and troubleshooting are available patterns, not mandatory sections everywhere.

## Quality and review principles

- Resolve consequential uncertainty before high-volume drafting.
- Propose changes tied to a reader task before producing pages.
- Prefer targeted improvements and coherent review units over routine rewrites.
- Evaluate actual content against its evidence and reader task, not the author's summary.
- Keep consequential errors visible; stylistic strengths cannot offset them.
- Record missing, incorrect, unverified, and inapplicable separately.
- Preserve product decisions and editorial corrections for future work.

## Success measures

Compare current practice and framework-assisted work on the same representative tasks. Record product-reader feasibility judgments, engineering task completion, consequential errors and omissions, cross-page contradictions, author effort, reviewer minutes, clarification rounds, and extent of rewriting. Record task scope and unresolved inputs so comparisons remain interpretable.

No improvement percentages or passing score are assumed. Public examples demonstrate practices, not causal proof that those practices improve outcomes.

## Decisions still open

- Whether readiness findings are advisory or enforced in CI or publication.
- Which agent integrations and documentation build system to support first.
- Who owns shared terminology, product answers, and exceptions over time.
- The numerical acceptance threshold, if useful after calibration.

These do not block initial research. Default to reporting readiness and asking for consequential answers, with no automatic publication or bypass of the repository's existing approval process.

The held-out target platform is reserved for a later holdout exercise. Do not use it to tune the initial pattern library or rubric.
