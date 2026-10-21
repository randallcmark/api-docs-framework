# First real-platform trial

The first trial freezes the framework before inspecting the user's evaluation platform. It compares a bounded reader task against existing practice and preserves the first result before changing prompts, patterns or rubric. The framework remains provisional; this is a trial procedure, not a validated benchmark or publication gate.

## Prepare and choose the task

Use [freeze.json](freeze.json) to identify the exact merged framework commit and critical file hashes. Build a portable pack from a checkout containing that commit:

```bash
python scripts/prepare_trial_pack.py --output /tmp/api-docs-trial.zip
```

Python 3.12 and Git are required; this command uses local Git objects and makes no model or network calls. It archives the frozen commit rather than the working directory, so later edits, untracked files and local source captures are excluded. If the commit object is unavailable in a shallow checkout, obtain that exact commit before building. Existing output files are preserved.

If you already have the unpacked pack, skip the preparation command and start with `TRIAL_PLAN.md`. The pack builder belongs to the preparation checkout, not the older frozen framework.

Unzip the pack. `framework/` contains the exact frozen repository; `TRIAL_PLAN.md` and `TRIAL_RESULTS.md` are blank trial records. `freeze.json` and `PACK_MANIFEST.json` identify framework and preparation-file hashes. Preparation instructions may evolve independently; the packet records which instructions were included. The frozen rubric and patterns retain their original provisional status.

Choose one coherent workflow with existing documentation and a clear product-reader/engineer outcome. Record the target OpenAPI, relevant source/deployment evidence, current MDX, shared pages and available product/engineering owners by path and revision in the plan. Record the agent/model, actual MDX build commands and what test environment/actions are available. Platform inputs and results belong in the platform's trial workspace; this pack does not collect or publish them.

## Preserve the baseline

Save the existing docs unchanged. For an existing-content task, use those pages as the baseline; do not manufacture a poor draft. For a new use case/domain, separately preserve a normal-practice submission and its inputs/process before using framework guidance. The first trial can cover existing content; a second, distinct task can examine a new domain.

Define the same reader task, applicability, success observations and evidence scope for evaluation of baseline and revision. Record what evidence and owner answers were available to each author. Baseline evaluators must assess the actual pages in a separate context without seeing the revised docs or the author's self-score. Use the frozen rubric for both, preserving missing, incorrect, unverified and inapplicable separately. Findings can be adjudicated later; preserve the original assessment first.

## Run the workflow

Use `framework/prompts/README.md` with the target input paths. Capture discovery, questions/answers, brief, page plan, changed MDX and checks. Record actual owner interactions rather than assuming every authored question consumed a person's time. Approved intent still needs availability evidence; conflicts remain questions.

Prepare the independent review manifest with the full changed-page set and relevant shared content. From the unpacked framework, run `scripts/prepare_doc_review.py` against that manifest and give only the frozen packet to a fresh evaluator. Keep author scores, prior findings and the baseline score out of its first pass. Preserve the result and any subsequent corrections/rechecks separately. Existing repository owners control review and publication.

## Compare observations and retain limits

Compare consequential defects, unresolved questions, cross-page contradictions, unsupported review findings and necessary rewriting. A criterion profile is evidence for discussion; do not turn its mean into a pass score. Record active author/reviewer/owner minutes only when measured, with pauses excluded. Otherwise use unknown; elapsed task duration is not active effort.

Where feasible, have a product reader assess fit and an engineer attempt the specified integration task using the baseline or revised docs. Use separate readers or comparable counterbalanced tasks to reduce learning effects. Agree which environment/actions are available before execution. If no reader task or sandbox run is possible, report content review only. Do not label a static review task-tested.

A single before/after exercise is descriptive. Different inputs, owner answers, authors, models or reader familiarity can explain differences. Record those limitations rather than attributing a change to the framework alone. No improvement percentage is assumed.

Close the first result in `TRIAL_RESULTS.md` before changing the framework. Then prioritize changes with evidence and owner impact. Reruns on the same material are development iterations; the platform is no longer an untouched holdout. No trial result is pre-filled by this pack.
