# Research protocol

## Questions

What documentation helps a product reader assess a REST platform's fit and an engineer deliver an integrated workflow? Which structures and explanations transfer across HR, business management, and fintech? Which inputs must product and engineering supply? Which qualities can be checked reliably with little human review?

Study public content directly. Research published authoring practices separately; a polished site does not establish its internal review process or prove commercial or developer success.

## Sampling

Begin with 36 candidates across six groups. Screen entry points for audience routing, concept and workflow coverage, REST references, testing, operations, change communication, and tooling. Candidate inclusion is a reason to investigate, not an endorsement or a finding of quality.

After screening, select approximately 12–15 providers for deeper comparison. Keep HR and business management represented rather than allowing payments to dominate. Include different integration models, product sizes, and documentation styles. Record selection and exclusion reasons, authentication gates, redirects, and retrieval limitations.

Examine journeys as well as pages: capability discovery → concepts → workflow → operation or event reference → test → diagnose → evolve. Sample at least one direct-client and one multi-customer partner journey, and cross-domain workflows. Do not infer missing site-wide coverage from a missing section on one sampled page.

For each of the following families, seek multiple independent providers:

1. Platform entry, capability fit, domain grouping, search and navigation.
2. Concepts, relationships, lifecycle and ownership.
3. Workflow guides, decisions, prerequisites and observable completion.
4. Endpoint, field and event semantics beyond schema.
5. Authentication, authorization and tenant boundaries.
6. Testing, sandbox differences, examples and failure simulation.
7. Troubleshooting, recovery, logs and support.
8. Release notes, changelog, compatibility and migration.
9. SDKs, CLI, skills, MCP and machine-readable documentation.

## Collection and provenance

Use official pages as primary evidence. Search results are discovery aids, not settled evidence. A source record includes provider, canonical URL, selected fetch URL, page type, research questions and why it was sampled. Prefer an official Markdown representation where offered; preserve its relationship to the human-facing page.

Fetch only manifest-selected URLs, sequentially, with a bounded response size, timeout, and delay. Do not recursively download sites. For a larger crawl, first inspect site instructions and published indexes, then define an explicit route and volume budget. Do not bypass access restrictions. A blocked or JavaScript-only source is a coverage limitation; it is not negative evidence about documentation quality.

Save raw content and extracted text locally. Track UTC retrieval time, response type, final URL, HTTP result, and hashes. HTML extraction is a convenience and can contain navigation or omit rendered elements. Review relevant passages and follow necessary links before drawing conclusions. Retrieval success is not equivalent to content suitability or inspection.

Store concise paraphrases, exact section or anchor locators, and links in the evidence index. Keep observations separate from inferred benefits and proposed rules. Retain local snapshots for research convenience; reference rather than reproduce third-party prose in authored guidance.

## Analysis

For every observation, record the visible practice, its context, limitation, relevant reader task, and candidate patterns. Do not copy a provider's business rules into a general rule. For example, one provider's approval delay can support documenting completion conditions; it cannot establish another platform's delay.

For each pattern, capture: reader problem, applicability, rule, necessary product inputs, discovery questions, evaluation method, supporting evidence, counterexamples or open comparisons, and confidence.

Evidence states:

- **Proposed:** derived from requirements or a plausible observation; external support may be absent.
- **Observed:** inspected in one independent provider.
- **Corroborated:** inspected in at least three independent providers for substantially the same practice, with contexts compared. This is a sampling convention, not proof of benefit.
- **Calibrated:** criteria applied to shared examples and disagreements adjudicated.
- **Task-tested:** representative readers attempted relevant tasks and results were recorded.

A provider family counts once for corroboration. Multiple pages or hosting on a common documentation engine do not establish independent support for a product-specific practice. Never call a pattern calibrated or task-tested on source observation alone.

Seek counterexamples and cheaper alternatives. An FAQ may improve discovery for recurrent questions or conceal information that belongs in a concept or task page. A long guide may support a complex workflow or create review burden; evaluate the actual task rather than setting an arbitrary word limit.

## Calibration and holdout

Use public research examples for discovery. Use separately labeled practice cases to refine prompts and score anchors. Freeze pattern and rubric versions before examining the held-out target platform. If the holdout exposes weaknesses, record that first result before revising; further runs are iteration, not an untouched holdout.

Have a second evaluator assess actual changed content with source evidence and the reader brief, without seeing the author pass's self-score. Separate agent passes reduce shared context; they do not guarantee independent judgment. Human calibration remains necessary for consequential criteria.

Record reviewer time, ambiguity, disagreements and false positives. Unsupported certainty and excessive escalation both consume scarce reviewer capacity. Do not require every fact to be manually reviewed: focus questions on uncertainty and impact, and automate objective checks where available.

## Initial milestone acceptance

Deliver an agreed-scope brief, a broad candidate index, a reproducible bounded collection method, inspected cross-domain evidence, provisional patterns, a rubric, and one end-to-end worked example. Explicitly list unexamined areas. This milestone does not claim the full candidate set is screened, all journeys are traced, or the rubric is validated.
