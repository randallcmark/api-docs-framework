# Comparative findings and framework implications

This pass screens all 36 candidates, selects 15 for focused deeper comparison, and records five documentation traces. The repository now holds 94 selected source captures and 57 scoped observations. Four candidates remain retrieval-limited in this collection method. These are research results about documentation, not provider rankings, completed integrations or reader tests.

Start with the findings below. Use the [screening ledger](screening.md), [journey records](journeys.md) and [evidence index](evidence.md) for supporting detail.

## Four practices supported across independent platforms

**Route from a business question toward implementation.** Square and SumUp provide business-domain or task routes; Stripe offers outcome-specific starting points; Revolut names integrated use cases. The reusable rule is to connect the capability question with an implementation route. The sources do not establish one universally effective menu or page hierarchy. See P01 in the [pattern library](../patterns/library.md#p01-route-from-business-outcomes-into-implementation).

**Separate operation success from business completion.** Square distinguishes creating an order, paying it and completing fulfillment. Gusto connects company setup with subsequent approval. Wise explains that sending a payout does not establish its arrival in the recipient's account. A generator needs an explicit answer about what each signal establishes and what remains. See [P03](../patterns/library.md#p03-distinguish-request-success-from-workflow-completion).

**Choose access using the integration actor and account context.** HiBob distinguishes client/internal and partner access. Gusto separates application and company actions. Wise distinguishes an organization's own payouts from customer-profile payouts. HubSpot distinguishes single-account access from multi-account distribution. These support asking who acts for whom before writing authentication instructions. They do not supply another platform's permission model. See [P04](../patterns/library.md#p04-route-authorization-by-actor-and-account-context).

**Connect an API change to affected clients and action.** Gusto identifies impacted endpoints and migration steps. Personio explains changes to identifiers, approval defaults and overnight attendance. Cloudflare identifies a changed representation and a client alternative during mixed rollout. Compatibility guidance must tell readers what affects them and what to do. See [P07](../patterns/library.md#p07-connect-changes-to-applicability-and-reader-action).

These four practices are marked `corroborated` under the research protocol. None is calibrated, task-tested or proven to reduce review time. The other eight patterns remain observed proposals.

## Three additions to discovery

**Synchronization is part of the product contract.** Merge distinguishes synchronization cadence from completion time. Personio connects initial population to employee/employment events. Codat explains dataset freshness, asynchronous refresh, deletion and the risk of comparing datasets synchronized at different times. Ask which system owns changes, what establishes completeness, how stale data may be, and how disconnects or deletions are handled. See [P10](../patterns/library.md#p10-explain-synchronization-and-data-freshness).

**Business time needs explicit semantics.** A suspension recorded now may take effect later; a payout marked sent may not be received; a work period may cross midnight or be attributed to another business date. Ask about occurrence, effective date, delivery, timezone and exceptional transitions only where they matter to the task. See [P11](../patterns/library.md#p11-make-business-time-and-state-meaning-explicit).

**A demonstration needs a stated boundary.** Codat's financing guide excludes production product design and due diligence. Finch distinguishes manual quickstart authorization from production automation. Gusto routes a first-call walkthrough to deeper guidance, while Plaid documents sandbox limits. A completed sample should not imply a launch-ready product. See [P12](../patterns/library.md#p12-state-the-boundary-of-a-demonstration); Finch is supporting screening evidence, not a corroboration claim for that pattern.

## Content functions to preserve

| Function | Reader need | Required input beyond raw schema |
| --- | --- | --- |
| Capability and domain overview | Can this support our use case, with what boundaries? | Supported scenarios, availability, integration models and exclusions |
| Concept | What do entities, actors, states and relationships mean? | Business meaning, ownership, identifier scope and lifecycle decisions |
| Workflow | How does our integrated outcome happen? | Prerequisites, responsibilities, choices, sequence, completion and recovery |
| Reference | How do we use this operation or field correctly? | Business effect, consequential conditions, permissions, defaults, units, side effects and relevant examples |
| Error catalog and troubleshooting | What happened, how do we distinguish causes, and what should we do? | Stable diagnostic data, supported recovery, escalation context and consequences |
| Release communication | What changed, who is affected and what action is needed? | Confirmed applicability, compatibility, dates where relevant and migration/verification steps |
| Tooling | What does this tool enable, how do we set it up and verify it? | Supported tasks/clients, access context, environment, lifecycle and troubleshooting |

These are content functions, not a compulsory page tree. SumUp's CLI announcement provides capability-oriented release information inside a changelog. Square separates release information by technology surface. The framework should evaluate the required reader information rather than enforce identical filenames or duplicate pages.

## A consequential scope trap

Codat's separately inspected reconciled-invoices feature requires accounting and banking sources. Its invoice-financing demo setup enables accounting and disables banking. Combining nearby documentation without preserving feature applicability would invent a prerequisite. Evidence must be attached to a specific capability and workflow, not merely to a provider or domain. Compare [E43](evidence.md#e43-codat-invoice-setup) and [E45](evidence.md#e45-codat-ar).

Similarly, an error catalog can identify causes without teaching complete recovery. Codat's table distinguishes unsupported, unsynced, disabled or failed data. GitHub's troubleshooting additionally takes a symptom such as missing results through pagination and authorization checks. The rubric should assess the path needed by the task rather than award completeness for the presence of an Errors page.

## What the route inspection establishes

The five traces cover Gusto company onboarding, Wise enterprise/embedded payouts, Personio shift planning, HubSpot records/relationships and Codat's financing demo. Among 33 recorded source-to-source connections, 28 are visible links in the captured representation and five are explicit research jumps. Visibility can include navigation; it is not a usability result.

Gaps are retained per stage. Examples include untraced test scenarios, incomplete access setup, uninspected migration announcements, and Personio flowchart images whose branch logic was not visually inspected. Some links target versioned routes; equivalence to an unversioned page is not assumed. An apparent HubSpot previous-version link targets the same guide and requires investigation. None of these establishes that an entire provider lacks the corresponding documentation.

## Next work

Close the task-critical gaps in selected traces before using them as benchmark journeys. Prioritize verification and migration paths, a complete support/escalation example, exact endpoint/event semantics, and content parity for diagram-dependent or versioned routes. Then create short calibration cases for incorrect completion claims, missing context, stale data, misleading examples and sound concise documentation. Measure evaluator disagreement and review effort before choosing acceptance thresholds or automating gates.
