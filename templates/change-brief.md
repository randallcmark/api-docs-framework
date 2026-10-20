# Documentation change brief

One brief per coherent change. Reuse established platform and domain decisions by reference; keep this brief short enough to read before the diff. The agent prepares it and asks people only for missing consequential answers.

- **Reader and outcome:** Who is integrating, who is assessing fit, and what should they accomplish?
- **Capability and applicability:** What exists now? Which integration models, environments, regions or entitlements affect this task?
- **Concept and workflow:** Which entities and actors matter? Who owns data? What is the sequence and observable completion condition? Link reusable domain knowledge.
- **Evidence and decisions:** Pin specification/code/doc revisions and product answers. Distinguish verified behavior, approved intent, planned behavior and unknowns. List consequential conflicts.
- **Proposed change:** Which existing pages change and why? Which new pages are necessary? What related references, navigation, events or release communication are affected?
- **Acceptance and verification:** What must a product reader decide and an engineer do? Which checks establish this? What cannot be checked yet?
- **Questions and owner:** For each unresolved item, give the focused question, existing evidence, impact, required answer owner and affected content. Ask the highest-impact questions first.

Conditional discovery prompts:

- **Synchronized data:** What establishes completeness and freshness? Who owns changes, and what happens on deletion or lost access?
- **Business time:** When does a change take effect? Which business date/timezone applies, and can a state reverse?
- **Demonstrations:** What production responsibilities does the sample omit? Which test result establishes only simulated behavior?
- **Adjacent capabilities:** Are these prerequisites actually required for this use case, or copied from a related feature?

Draft only supported portions when questions remain. Do not write around an unknown with confident prose. Split unrelated outcomes if reviewers would need to reconstruct several domains in one pass. A multi-page workflow can remain one change when its context and acceptance criteria are shared.
