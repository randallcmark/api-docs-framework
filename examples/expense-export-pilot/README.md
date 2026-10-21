# Guided authoring pilot: expense export

This pilot completes the [five authoring prompts](../../prompts/README.md) on a coherent two-page MDX change, followed by an actual fresh-context content review. The reviewer reports no findings or owner questions and recommends human review. It is a workflow demonstration, not measured proof of quality or effort improvement.

All source, requests, answers and documents are original fictional fixtures. The framework author constructed the inputs/answers and authored the documentation in the same context. There was no blind authoring experiment or real owner interview. The independent reviewer received only frozen source evidence, brief, actual MDX/diff and framework guidance; no author self-score, discovery/plan/claim map or expected findings were included.

## Follow the workflow

1. Inspect the [loose request](inputs/request.md), [contract](inputs/openapi.json), [implementation excerpt](inputs/implementation.py) and [current guide](baseline/docs/guides/expense-export.mdx).
2. Read [discovery](run/discovery.md) and the [question log](run/questions.json). The two authored questions concern intended framing and missing operational guarantees. Known contract fields, scopes and date rules are reused without asking an owner to repeat them.
3. Incorporate the [authored owner answers](inputs/owner-answers.md), then inspect the [brief](run/brief.md) and [bounded plan](run/plan.md). Framing becomes accounting-draft handoff; separate payment/posting capabilities are not invented.
4. Compare the proposed [guide](draft/docs/guides/expense-export.mdx) and [reference](draft/docs/reference/expense-exports.mdx). Existing access/support remain unchanged. The [claim map](run/claims.json) ties consequential assertions to evidence; it is excluded from the evaluator packet.
5. Inspect the [manifest](run/review-manifest.json), [frozen review input](run/review-input.json), [original independent review](run/independent-review.json) and [short handoff](run/handoff.md). All 11 criteria are assessed; change communication and tooling are inapplicable to this correction. R06/R08 are rated adequate without inferring API execution or navigation success. No revision or repeat review was needed under the supplied evidence.

## What the pilot establishes

The workflow carries an outcome mismatch and missing operational policy through questions, evidence, a bounded plan, real MDX and a separate evaluation. The guide distinguishes queue acceptance, draft creation, posting and payment; its recovery guidance separates safe create replay from ambiguous provider effects. A companion reference adds semantics beyond raw schema while reusing shared access/support.

The [stage record](run/stages.json) and [archived prompts](run/prompts.json) preserve the procedure used. Two written questions and zero real owner interactions are counts of authored artifacts, not observed question burden. Active author/reviewer time is unknown. The fresh reviewer used operational packet-only restrictions, not enforced access control; its exact model version is unknown.

There is no callable API, provider or target MDX renderer. No requests, implementation execution, sandbox tests, rendered navigation or reader tasks were run. Source/diff/locator checks do not certify factual accuracy or reader outcomes. The user's platform remains untouched. Agent-specific installation, model orchestration and publication gates remain outside this starter workflow.

## Try the packet builder

From the repository root:

```bash
python scripts/prepare_doc_review.py \
  --manifest examples/expense-export-pilot/run/review-manifest.json \
  --output /tmp/expense-review.json
```

The current builder verifies explicit evidence hashes and complete coverage of the declared proposed pages, generates actual additions/revisions/deletions, and embeds the current evaluation prompt/rubric with their hashes. It reads only declared files, so the manifest author must supply the complete changed-page set and classify evidence honestly. Existing output files are preserved. Future framework changes can produce a new input packet; the archived original review remains tied to its own frozen bytes.
