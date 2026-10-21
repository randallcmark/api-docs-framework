# First separate-agent rubric run

Two fresh agent contexts evaluated the nine frozen fictional cases from framework commit `41c77c0b464eec07fba46397e763bfde80e6b61a`. Both completed all cases without blocking pilot ambiguity. Their original outputs are preserved unchanged. This run supports comparison and anchor refinement; it does not make the rubric a validated benchmark.

The evaluators agreed on all **27 requested criterion profiles** (applicability, rating and issue state) and **9/9 readiness decisions**. That is a narrow mechanical agreement measure. Finding tags and grouping differ in places, and both agents share disagreements with the proposed author key. Perfect agreement here does not establish correctness, cross-model reliability or performance on real PRs.

## Findings at a glance

| Case | Shared outcome | Review implication |
| --- | --- | --- |
| C01 Accepted payout | Incorrect completion and verification; critical financial consequence. Missing state observation is also material. | The agents group the false claim and its reinforcing test together; tags must not multiply the defect count. |
| C02 Empty invoice data | Incorrect business inference and verification; missing qualification/recovery. Both agents say critical; the key says material. | Initially disputed; [later human adjudication](../../adjudications/c02-severity.md) keeps this case material. |
| C03 Partner tenant routing | Critical: concrete session-to-tenant bypass exposes another consented tenant's employee data. | The token's broad access is not the user's tenant authorization. |
| C04 Planned capability | Material incorrect availability and unsupported enablement instruction. | Both use supplied deployment evidence without unnecessary owner questions. |
| C05 Concise field reference | Ready for human review; no findings. R10 and R11 are inapplicable with reasons. | Concise content can earn 3 through relevant lifecycle boundaries. It needs no invented tooling or page expansion. |
| C06 Create timeout | Material missing lookup and unresolved-outcome handling. | Preserve uncertainty; neither evaluator invents idempotency or automatic retries. R09/R07 overlap deserves clarification. |
| C07 Business dates | Unverified with no number; needs answers. | Each evaluator asks one engineering question about deployment/conversion. Product intent is already supplied. |
| C08 Combined migration note | Ready for human review; no findings. | No demand for separate release-note, changelog or migration filenames, or claimed sandbox execution. |
| C09 Static skill | Material false access claim; correct installer guidance retained. | Both give R05=0 and R11=1; the key proposes both 0. Mixed-content scoring needs a clearer anchor. |

The two sound cases received no findings in four evaluations. Each evaluator asked one owner question, confined to the deliberately unresolved C07 evidence. Manual author comparison found the intended reader problems in all seven defective/unverified cases; the matching rationale and grouping are recorded in [analysis.json](analysis.json). These are small constructed controls, not a measured general false-positive rate or an independently adjudicated accuracy result.

## Adjudication and next changes

[Analysis issues D01–D06](analysis.json) preserve the initial comparison. The [later human decision](../../adjudications/c02-severity.md) resolves D01 as material; the other score/tag proposals remain author analysis. The original outputs, archived key, input hashes and comparison are unchanged. The frozen manifest/analysis retain their initial pending status as historical records. The current rubric now clarifies the severity boundary; the wider key remains provisional.

D01 concerns C02. The guide says an empty invoice list proves no receivables and directs the no-receivables lending decision. The evidence permits incomplete/stale/disconnected data and requires deferring in those states. It does not establish loan approval, disbursement or loss. Both evaluators call the wrong financial classification critical; the key calls it material. The user later accepted material severity on the supplied evidence. Both original interpretations remain in the frozen outputs.

The other proposed refinements preserve the important finding regardless of number or tag: distinguish false verification from missing verification, explain task-relevant boundaries behind a 3, avoid counting one root cause several times, and clarify whether a language score repeats a technical completeness problem. The mixed static-skill example needs an explicit 0-versus-1 rationale. Original outputs must remain unchanged after adjudication; record later revisions separately.

Human adjudication of consequential criteria and broader cases remain necessary before promoting guidance to calibrated. The user's platform remains untouched. No publication threshold, automatic gate or overall average is introduced.

## Reproducibility and scope

- [manifest.json](manifest.json) binds the framework revision, packet/document/rubric hashes, evaluator identities and original result hashes.
- [inputs.json](inputs.json) stores every frozen task, fact, document and instruction, with the shared rubric stored once. Reconstruct packets in `packet_key_order`, replacing the `rubric` field with `shared_rubric`, then serialize with Python `json.dumps(packet, indent=2) + "\n"`. The validator checks the resulting exact byte hashes.
- [author-key.json](author-key.json) preserves the pre-comparison proposed anchors and is separately hashed. Evaluators did not receive it.
- [Original evaluator A results](results/evaluator-a/) and [original evaluator B results](results/evaluator-b/) record actual findings, timestamps and limitations.
- [comparison.json](comparison.json) is a reproducible mechanical profile comparison. [analysis.json](analysis.json) is the author's semantic comparison and explicitly records pending decisions.

Both agents used the same inherited model and role instructions in separate fresh contexts. Exact model version is unavailable and recorded as unknown. The instructed context restriction was packet-only: no repository, answer key, other evaluator results, browsing or APIs. This is operational separation, not an enforced access-control boundary. Pilot cases C01/C05/C07 were followed by the remaining six without input changes.

Active review minutes were not instrumented and remain null. UTC timestamps are recorded, but elapsed duration is not treated as active review effort. No API or sandbox execution, MDX build, reader test, task-success observation, production platform evaluation or reviewer-time benefit was measured. Structural validation does not decide finding validity or adjudicate scores.
