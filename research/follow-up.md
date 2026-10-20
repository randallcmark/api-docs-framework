# Focused journey follow-up

This pass inspects ten additional official text pages and three linked diagrams across Gusto, Wise, Personio, HubSpot and Codat. It narrows gaps in the [five documentation traces](journeys.md); it does not complete the comparative research milestone. The pool remains 36 candidates and 15 selected providers. Totals are now 104 selected text sources and 67 observations, with 12 provisional patterns and four corroborated practices. No pattern confidence was upgraded in this pass.

## Findings that change how we review

**Error categories are useful evidence, but not automatically a recovery procedure.** Gusto's categories distinguish stale resource versions, missing access, service failure and warnings alongside a successful migration. Codat's additional read-troubleshooting page covers a single validation-warning category, directing the reader to logs and applicability. Neither justifies inventing a universal retry rule or marking every recovery gap closed. See [E58](evidence.md#e58-gusto-error-categories) and [E63](evidence.md#e63-codat-data-troubleshooting).

**Access rules must stay attached to the integration model and version.** Wise's token setup distinguishes the embedded model from other partner profile-level usage; its change index connects the update to the relevant guides. The setup page also connects invalidation causes to corrective actions and useful support diagnostics. This strengthens the access-context question without transferring Wise's token rules to another platform. See [E59](evidence.md#e59-wise-changelog) and [E65](evidence.md#e65-wise-oauth-setup).

**A failure signal is not simply another spelling of lifecycle state.** Wise documents payout failures that need not trigger a state change, multiple failure events, provider-managed retry for a named reason, and a simulation with an expected webhook. These support separate questions about event purpose, unknown codes, who retries and what establishes completion. A provider retry does not authorize a caller retry. See [E67](evidence.md#e67-wise-payout-failures).

**Version policy needs explicit boundaries.** Wise excludes webhooks and sensitive-card-details endpoints from its global-version policy. HubSpot's linked validation notice explains version, configured-account and token-context applicability, plus corrected-input retries. Codat's policy qualifies upstream-provider change promises. A policy page can support compatibility planning while leaving a selected feature migration untraced. See [E61](evidence.md#e61-hubspot-validation-change), [E62](evidence.md#e62-codat-change-policy) and [E64](evidence.md#e64-wise-global-versioning).

**Text extraction can miss the decision itself.** The Personio handling guide's three diagrams contain eligibility, record-existence and lifecycle branches absent from the surrounding prose. Both sampled guide routes returned byte-identical Markdown, which still references the images. This is equality of two captures, not all-route equivalence or evidence that agents cannot view images. The offboarding diagram has an onboarding end-label ambiguity; its intended correction remains unknown. Visual inspection and media provenance are in `media.json`, bound to [E60](evidence.md#e60-personio-handling-v2). Do not adopt the depicted deletion action as a universal retention rule.

**A test-account walkthrough is useful but task scope matters.** HubSpot's official article gives account setup, a small fake dataset and a single-record result check. It is an AI/workflow example. It helps establish a testing starting point but does not close the CRM REST record-and-association verification gap. See [E66](evidence.md#e66-hubspot-test-account-walkthrough).

## Remaining research

Gusto company-approval simulation, complete blocker handling, Personio test/auth/event contracts, Wise reconciliation and selected-version migration, HubSpot REST verification and full migration, and Codat exact operation/event contracts remain partial or untraced. Endpoint field semantics and support/escalation examples also need broader independent comparison. No account was created and no API, event handler, installer or sandbox simulation was run.

## Calibration preparation

The [practice pack](../evaluation/calibration/README.md) adds nine original fictional cases with bound evidence, actual MDX, isolated evaluator packets and a separate proposed answer key. It includes correct concise content and inapplicable criteria to expose excessive review demands as well as missed errors. It is ready for separate evaluation; it is not a calibration result. Reviewer-time reductions, agreement and reader outcomes remain unmeasured.

Capture and hash verification establish which representations were inspected. Source observations are paraphrased; full text and images stay in the ignored local cache. Diagram checks verify hashes, source links and recorded inspection, not semantic interpretation or accessibility compliance.
