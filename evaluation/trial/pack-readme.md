# Private documentation dry run

This pack contains a prompt library, evaluation rubric, research-backed patterns and blank trial records. It does not call a model or contain target-platform data or trial results.

## Open these files first

- `framework/README.md`: overview, dependencies and copyable authoring instruction.
- `framework/prompts/README.md`: the five prompts and author/evaluator handoffs.
- `TRIAL_PLAN.md`: copy into your private trial workspace and fill in before assessment.
- `TRIAL_RESULTS.md`: copy alongside the plan; complete only after observing the work.
- Top-level `freeze.json` and `PACK_MANIFEST.json`: this pack's exact source identity and preparation-file hashes.

The full comparison procedure is in `framework/evaluation/trial/README.md`. Its links resolve within the framework. Any older pack/freeze records archived inside `framework/evaluation/trial/` are historical source content; the top-level records identify this pack.

## Dependencies

For prompt-only use, choose an agent that can read the supplied files. No framework installation, Python, Git, model SDK or framework API key is required. The agent service has its own access requirements.

Optional scripts require Python 3.12+ with its standard library only. No pip packages are needed. Git is required only for regression tests or building another ZIP from a checkout containing the pinned commit; it is not needed to use this extracted pack. Your target site's MDX renderer, components and build/test dependencies remain separate.

## Run one bounded workflow

1. Choose one reader outcome. Preserve the current docs as the baseline. Record target spec/code/docs revisions, existing decisions, available answer owners, agent and actual build commands in the private plan.
2. Use `framework/prompts/01-discover.md`, then `02-plan.md` and `03-draft.md` in the authoring session. Keep evidence, questions/answers, brief, plan, changed MDX and claim map in the private workspace. Ask for consequential missing answers; do not turn assumptions into product facts.
3. Prepare complete review inputs: task, brief, evidence, shared pages, current/proposed pages, actual diff, checks, applicable patterns, rubric and prompt 04. Use manual assembly described in the prompt-library guide or the optional packet builder below.
4. Start a fresh evaluator session with only those inputs and `04-evaluate.md`. Preserve its original findings. Assess the baseline separately against the same task and frozen rubric, without revealing the revision or its findings.
5. Return the assessment to the author with `05-revise-and-handoff.md`. Resolve findings or record needed decisions, recheck affected content, and prepare the short human review packet. Existing repository owners approve changes.
6. Complete the private results record before tuning the framework. Record what was measured, what was unrun and comparison limitations. A single content review is not proof of reader success or time saved.

Optional packet command, after changing directory to the extracted `framework/`:

```bash
python scripts/prepare_doc_review.py \
  --manifest /path/to/private-trial/review-manifest.json \
  --output /path/to/private-trial/review-input.json
```

Use a new output path. The manifest format and fictional example are described in `prompts/README.md`; it must declare the complete changed-page set. The builder verifies declared hashes and generates diffs; it does not judge claims or call an agent.

Keep platform inputs and results in the private trial workspace. The ZIP excludes Git history, local untracked files and the ignored research cache. Named third-party providers remain as research provenance. No overall passing score or automatic publication gate is supplied.
