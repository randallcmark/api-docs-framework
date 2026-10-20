# Engineer and agent documentation workflow

Status: provisional manual workflow for repository-based MDX changes. Agent-specific installation and CI enforcement follow later, after research and calibration.

## 1. Establish the change and evidence

Select one integrated reader outcome. Read applicable repository instructions, platform decisions, OpenAPI, source and existing documentation. Pin revisions. Inventory consequential claims and disagreements. Existing docs are claims to assess, not an independent guarantee of correctness.

For existing content, establish a baseline with the same task and rubric intended for the revision. For a new domain, inspect impact on shared concepts, authorization, events, navigation, reference and release communication.

## 2. Prepare the brief and ask targeted questions

Populate the [change brief](../templates/change-brief.md) from evidence. Ask product or engineering owners only for consequential information the evidence cannot supply. Give the context, likely alternatives if helpful, impact and affected page. Record the answer, owner, date, scope and implementation status in reusable domain knowledge.

A product answer establishes intent; validate availability separately. Do not infer a retry guarantee, lifecycle, permission, supported use case or product promise because it is conventional elsewhere.

## 3. Propose the documentation change

State which pages to retain, revise, add, combine or remove, with reader-task justification. Prefer focused fixes over routine wholesale rewriting. Apply patterns by their conditions. Do not manufacture concepts, FAQs, CLIs or MCP guides to satisfy a universal checklist.

Keep coherent workflows connected across pages. Split unrelated outcomes or changes too large for their shared context to make review practical. There is no universal word or page quota; use scope, reader need and reviewer effort.

## 4. Draft and run objective checks

Write MDX using the project's actual component conventions. Connect business steps with operations, events, expected results and recovery. Cross-link shared guidance rather than duplicating it. Keep unresolved claims out of publication-ready prose and report them in the packet.

Run the repository's available build/lint, local links and terminology checks. Compare examples and endpoint claims to the pinned contract; execute safe examples in an appropriate test environment when available. Record what each check establishes. This starter repository has no MDX renderer or target API and does not pretend its consistency validator performs these checks.

## 5. Evaluate separately

Start a fresh evaluation pass with the reader brief, source evidence, actual MDX diff, relevant linked content and the [rubric](../evaluation/rubric.md). Exclude the author's self-score from the initial evaluator view. Assess consequential claims against evidence, then task completeness and editorial quality. Report evidence locators and actionable findings.

Do not call repeated agreement by the same model proof. Where answers are missing, return a focused question rather than polish. Resolve objective defects, then reevaluate affected criteria. Expand checks only when changes or uncertainty justify them.

## 6. Submit a reviewable PR

Attach the [review packet](../templates/review-packet.md). Provide specific decisions and passages that need human attention, plus evidence and check results. Do not force reviewers to infer intent from prose. Existing owners approve; automatic publication and enforced gates are not enabled by this framework.

After acceptance, preserve decisions and reusable corrections. When platform behavior changes, use the brief's dependencies to identify affected workflows and pages. This dependency process is manual initially; automated impact analysis is a later implementation candidate.
