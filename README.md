# API documentation framework

A research-backed prompt library and review framework for REST API platform documentation. Use it to improve existing docs or introduce a new use case or domain, from product fit and concepts through integration, verification, recovery and change.

This is a guided workflow for an engineer working with an agent. It produces a supported brief, a bounded MDX change and a short review packet. Product and engineering answer consequential questions; a fresh evaluator reviews the result independently. It is not an automated documentation service.

## Start here

The [prompt library](prompts/README.md) is the main entry point. The prompts are ordinary Markdown: read or copy them into your existing agent. **No installation, Python, model SDK or framework API key is required for prompt-only use.** Use an agent that can read the files you provide; its own service requirements still apply.

Choose one coherent reader outcome, such as assessing and implementing an expense-export workflow. Start with:

- The intended reader, outcome and known scope. A loose request is enough to begin discovery.
- The relevant OpenAPI, source/deployment evidence, existing docs and shared platform guidance, with paths and revisions where available.
- Existing product decisions and people who can answer product or engineering questions. Missing inputs stay explicit; the agent must not invent them.
- Your documentation repository's MDX conventions and actual build/check commands.

Give the authoring agent this instruction, replacing the brackets:

```text
Read [framework path]/AGENTS.md and [framework path]/prompts/README.md.
Follow prompts 01–03 for this reader outcome: [outcome and audience].
Framework root: [framework path]. Target docs repository: [target path].
Inputs: [OpenAPI, relevant code/deployment evidence, existing docs and decisions,
with paths/revisions]. Output workspace: [private change-workspace path].
Reuse known answers. Ask only consequential missing product/engineering questions.
Keep unsupported claims unresolved. Prepare the complete independent-review
inputs, then pause for a fresh evaluator. Do not substitute a self-score.
```

Keep target-platform inputs, answers and results in that platform's private workspace. They do not need to be copied into this framework repository.

## The workflow

| Stage | What happens | What you keep |
| --- | --- | --- |
| [1. Discover](prompts/01-discover.md) | Inspect evidence; ask focused questions about intent, behavior and gaps | Evidence inventory, [change brief](templates/change-brief.md), question/answer log |
| [2. Plan](prompts/02-plan.md) | Select relevant patterns and the smallest coherent page change | Page/dependency plan and concrete reader acceptance checks |
| [3. Draft](prompts/03-draft.md) | Produce supported MDX in the target site's conventions | Changed pages, claim-to-evidence map, actual check results and review inputs |
| [4. Evaluate separately](prompts/04-evaluate.md) | Start a fresh agent context with the frozen task, evidence, diff and [rubric](evaluation/rubric.md) | Criterion profile, located findings, owner questions and readiness |
| [5. Revise and hand off](prompts/05-revise-and-handoff.md) | Resolve findings or record decisions needed; recheck affected content | Short [human review packet](templates/review-packet.md) and actual diff |

The evaluator must receive the supporting evidence and shared pages, not just the new prose. Keep author self-scores and previous findings out of its first pass. Preserve its original assessment before revisions. Existing repository owners approve changes; there is no overall passing score or automatic publication gate.

For a concrete example, follow the [completed fictional expense-export pilot](examples/expense-export-pilot/README.md). Its owner answers are authored fixtures, not real interviews or proof of reader benefit.

## Run your own dry run

Follow the [private trial guide](evaluation/trial/README.md), starting with the [blank plan](evaluation/trial/plan-template.md). Preserve the existing documentation as a baseline, pin the framework and target inputs, run one bounded workflow, and keep baseline and revised assessments separate. Close the [result record](evaluation/trial/results-template.md) before tuning the framework.

You can use a checkout or an unpacked portable trial pack. In a pack, read the top-level `TRIAL_README.md` and `freeze.json` first; `framework/` contains the pinned source. No target-platform dry run has been performed or pre-filled.

## Dependencies and optional tools

| Use | Required |
| --- | --- |
| Read/copy the prompts and review manually | Your chosen agent, supplied files and product/engineering answers; no framework runtime |
| Build a hash-bound review packet or run repository checks | Python **3.12+**, standard library only; no `pip install` |
| Run regression tests / build a portable frozen trial ZIP | Python **3.12+** and Git; ZIP preparation also needs the pinned commit locally; no model calls |
| Refresh optional comparative-research captures | Python **3.12+** and network access to selected source URLs |
| Build/test the generated documentation | The target site's own MDX renderer, components and checks; these are not supplied here |

There is no Node/npm requirement, bundled LLM, provider SDK or model orchestration in this framework. If your target site needs Node or other tools, use its own setup instructions. The Python tools do not generate prose or call a model.

From the framework root:

```bash
python scripts/validate.py
python -m unittest discover -s scripts -p 'test_*.py'
```

The default validator reports missing optional research snapshots; it does not fetch them. This does not prevent a dry run. To prepare review inputs for a real change, create a manifest using the [documented format](prompts/README.md#prepare-an-independent-review):

```bash
python scripts/prepare_doc_review.py \
  --manifest /path/to/private-change/review-manifest.json \
  --output /path/to/private-change/review-input.json
```

The builder verifies declared hashes, includes selected evidence and shared content, and creates before/after diffs. It does not discover the complete change set or assess correctness. Give its output to the fresh evaluator. An output file must be new so original records are preserved.

Optional pack preparation, from a Git checkout containing the frozen commit:

```bash
python scripts/prepare_trial_pack.py --output /tmp/api-docs-trial.zip
```

## Explore the framework

| Path | Purpose |
| --- | --- |
| [Prompts](prompts/README.md) | Copyable instructions and review-input preparation |
| [Workflow](workflows/engineer-agent.md) and [templates](templates/change-brief.md) | Responsibilities, brief and handoff structure |
| [Pattern library](patterns/library.json) | Conditional rules, discovery questions and evidence links |
| [Evaluation rubric](evaluation/rubric.md) | Anchored criteria, severity and evidence requirements |
| [Practice cases](evaluation/calibration/README.md) | Fictional examples and preserved separate-evaluator runs |
| [Research findings](research/comparisons.md) and [follow-up](research/follow-up.md) | Observed conventions, gaps and limits |
| [Research protocol](research/protocol.md) and [screening](research/screening.md) | Provenance, provider selection and evidence standards |
| [Project brief](docs/project-brief.md) and [roadmap](docs/roadmap.md) | Scope and remaining work |

Research currently spans 36 screened candidates, 15 selected providers and five documented traces. The library has 12 patterns; four practices have cross-provider corroboration. Ten fictional cases and two separate-agent runs inform interpretation, but the wider rubric remains uncalibrated and no reader-task improvement is claimed.

Named providers and official source links are retained as research provenance, not platform endorsements or text to copy. Full third-party snapshots stay in an ignored local cache and are excluded from the portable pack. Optional capture commands are listed in the [research protocol](research/protocol.md).

Repository content uses role-based language and relative links. A portable ZIP excludes Git metadata and local untracked files. Sharing or forking a Git repository still exposes its existing GitHub ownership and commit history; content cleanup does not rewrite those records.
