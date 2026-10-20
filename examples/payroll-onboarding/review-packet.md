# Review packet for company onboarding documentation

The change helps a partner product lead understand review dependencies and a partner engineer submit company onboarding and interpret completion. Review [the revised guide](after.mdx) and [supporting reference](reference.mdx); [the brief](change-brief.md) records scope.

## Decisions needed

For a real platform, engineering must supply the actual test environment and scenario steps, validate examples against implementation, and confirm tenant and retry behavior. Fixture answers are illustrative and are not human approvals. No actual publication recommendation is made.

## Review focus

1. Confirm that [completion](after.mdx#determine-completion) means onboarding approval and preserves the separate payroll-validation requirement.
2. Confirm that the access path is per-client-tenant OAuth with the stated scopes.
3. Confirm the [failure guidance](after.mdx#handle-failures-and-test-limits), especially the uncertain-submission fallback and sandbox boundary.

## Evidence and checks

- Evidence: `openapi.json` and decisions D01–D07 at `fixture-v1`.
- Research: P03 and P04 guide what to explain; they do not establish fictional platform facts.
- Evaluation: [demonstration findings](evaluation.md). The misleading claims in the original draft have been replaced within the fixture's scope; R06 remains unverified.
- Performed: local artifact consistency and supporting-file/link checks through the repository validator.
- Unperformed: API requests, MDX compilation, independent evaluation, reviewer-time measurement and reader-task tests.

Recommended next action: obtain a runnable test scenario and actual evidence before treating this as a real documentation submission. No gate or publishing automation is enabled.
