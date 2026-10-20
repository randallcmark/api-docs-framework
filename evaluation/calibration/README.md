# Practice cases for rubric calibration

Nine short, original fictional MDX cases exercise the [provisional rubric](../rubric.md). They are authored examples with proposed anchors, **not a calibrated benchmark**. No independent evaluations, agreement measurements or reader tests have been performed. The user's platform remains an untouched holdout.

The pack covers incorrect completion, incomplete data, tenant boundaries, planned versus deployed capability, a sound concise reference, missing timeout recovery, conflicting date semantics, a sound combined migration note, and static skills mistaken for account access. Two sound cases help expose unnecessary expansion demands; unavailable evidence and inapplicability have separate cases.

## Run a practice evaluation

Export a single case from the repository root:

```bash
python scripts/prepare_evaluation.py --case C01 --output /tmp/c01-input.json
```

The packet includes the task, fictional evidence with revision labels, actual MDX, the rubric, content hashes and result-field instructions. It excludes the answer key and other case documents. The exporter checks the bound document and rubric hashes, and refuses to overwrite an existing output.

Give the exported packet to a fresh evaluator context. Do not give that context repository access, this README's case descriptions, the answer key, or another evaluator's findings. This is an operational separation, not an access-control guarantee. No provider accounts, network access, API execution or user-platform documents are needed.

Each evaluator should assess the focus criteria and report other consequential defects if found. A reference page is not obliged to contain a full integration guide. Record applicability, numerical rating or unverified state, evidence, concrete consequences, fixes and readiness. Do not average scores. Use [the result template](result-template.md); hash the exact exported packet to identify the input.

## Compare before changing the rubric

1. Have at least two evaluators assess the same exported bytes separately, without author scores. Two fresh agent contexts can expose interpretation differences but do not guarantee independent judgment. Include human adjudication of consequential criteria before calling guidance calibrated.
2. Preserve original results, evaluator identity/version, rubric and document hashes, actual active minutes, timestamps, missing inputs and questions. Do not infer review time from token count or task duration.
3. Only after the results are frozen, compare them with each other and with `answer-key.json`. Its 12 anchors are author proposals. Grouped criteria can share one defect; do not multiply the issue count. The key is not an exhaustive list of every defensible finding.
4. Adjudicate disagreements about finding validity, applicability, incorrect/missing/unverified state, rating, severity, evidence and readiness. Accept a well-supported additional finding, or correct the author key if wrong. A wording difference is not necessarily a disagreement. Avoid automated exact-text scoring.
5. Record missed consequential defects, unsupported findings, question burden and unnecessary rewrite requests. For the sound cases, check whether evaluators demanded extra sections or invented tooling. For the conflicting-evidence case, check whether they asserted deployed facts without confirmation. Report counts with denominators and small-sample limitations; do not claim broad reliability from nine constructed cases.
6. Save adjudication, changed anchors and reasons under a versioned run directory. Revise and re-export deliberately if rubric or fixtures change; preserve old packets/results. Only documented comparison and adjudication can support a calibration claim. No numerical publication threshold follows automatically.

First use a few cases to find confusing instructions, then assess all nine on frozen inputs. Reusing them after seeing the key is a training iteration, not a blind evaluation. A positive result on these cases does not establish reader task success or performance on the user's platform. Freeze a framework revision before the separate holdout exercise.

## What repository checks establish

`python scripts/validate.py` checks case IDs, fact references, rubric/document hashes, criterion IDs, expected locators and anchor structure. It does not judge whether the fictional evidence is plausible, whether an evaluator agrees, whether the proposed score is right, or whether the page works for readers. The exporter is a packet builder, not a grader or a documentation generator.
