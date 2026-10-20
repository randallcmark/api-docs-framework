# API documentation framework

A research-backed framework for engineers and agents improving REST platform documentation. It serves product people assessing capabilities and engineers building direct-client or partner integrations across HR, business management, and fintech.

The unit of work is an integrated use case or workflow. Readers need a connected explanation from capability fit and conceptual model through implementation, testing, operation, and change.

## Current status

Comparative research is underway: all 36 candidates have entry/index screening, 15 are selected for focused deeper comparison, and five documentation traces record their inspected stages and gaps. The library contains 12 patterns, including four practices corroborated across independent providers. The rubric remains uncalibrated, and no reader-task benefit is claimed.

Start here:

1. [Project brief](docs/project-brief.md) — agreed objective, constraints, and scope.
2. [Research protocol](research/protocol.md) — selection, collection, analysis, and evidence standards.
3. [Comparative findings](research/comparisons.md) — current conclusions, scope traps and framework implications.
4. [Screening and selection](research/screening.md) — all 36 candidates and the 15-provider focus sample.
5. [Documentation traces](research/journeys.md) — connected routes with verification, recovery and migration gaps.
6. [Initial research sample](research/sample.md) — the preserved first milestone.
7. [Worked example](examples/payroll-onboarding/README.md) — evidence, discovery, drafting, and review on a fictional platform.
8. [Next work](docs/roadmap.md) — remaining research and implementation milestones.

## Repository contents

| Path | Purpose |
| --- | --- |
| `research/candidates.json` | Candidate universe; proposed documentation entry points are not assumed verified |
| `research/screening.json` | Evidence-bound screening outcomes and deeper-study selection reasons |
| `research/journeys.json` | Inspected stages, partial/untraced coverage, visible links and research jumps |
| `research/access-checks.json` | Published access-instruction checks and their local snapshot hashes |
| `research/sources.json` | Deliberately selected official pages and capture targets |
| `research/captures.json` | Retrieval metadata and content hashes for local snapshots |
| `research/evidence.json` | Reviewed observations with source locators and limitations |
| `patterns/library.json` | Provisional rules, applicability, questions, and evaluation links |
| `evaluation/rubric.md` | Anchored criteria, issue severity, and evidence requirements |
| `templates/change-brief.md` | Minimum context before drafting a coherent change |
| `templates/review-packet.md` | Short PR context and decisions needed from reviewers |
| `workflows/engineer-agent.md` | Discovery, authoring, evaluation, and review procedure |
| `scripts/` | Bounded source capture and repository consistency checks |

## Local use

Python 3.12 or later; no third-party packages or credentials required.

```bash
python scripts/validate.py
python scripts/capture_sources.py --list
python scripts/capture_sources.py --ids gusto-onboarding hibob-start
```

Capture only fetches selected manifest URLs. It does not discover or recursively crawl links. HTTP failures remain recorded as failures; a fetched page is not automatically a reviewed example. Raw third-party material stays in the ignored local `research/snapshots/` directory. Tracked evidence uses short paraphrases and source links.

The project is stored in the private [randallcmark/api-docs-framework](https://github.com/randallcmark/api-docs-framework) repository. Full third-party source snapshots remain in the ignored local cache. No publishing policy, automated publication, or numerical pass threshold has been agreed.
