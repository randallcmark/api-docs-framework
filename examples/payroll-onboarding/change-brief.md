# Change brief for submitting company onboarding

- **Reader and outcome:** A partner product lead plans company onboarding; a partner engineer submits an existing, prepared company and determines whether onboarding has completed. The company is a legal employer within one client tenant.
- **Scope:** Explain submission and status checking. Company creation, tax/bank setup and running payroll are separate workflows. An `approved` onboarding status does not establish that a payroll run can execute.
- **Evidence:** `openapi.json` and `decisions.json` are fictional fixtures at `fixture-v1`. Product answers define the meaning and scope; engineering answers define intended implemented behavior within the scenario. Neither establishes a deployed API.
- **Proposed change:** Replace unsupported immediate-activation and real-time-event promises in `before.mdx`. Keep one bounded workflow guide and a supporting reference; no new platform-wide FAQ or tooling page.
- **Acceptance:** Readers distinguish request acceptance from onboarding completion, choose the tenant-scoped access path, interpret each documented state and avoid blind resubmission. Product readers see the separate dependency on payroll validation and the absence of a fixed approval SLA.
- **Verification:** Static comparison against the fictional contract and recorded decisions. HTTP execution, MDX build and reader testing remain unperformed.
- **Questions:** The initial questions and supplied fixture answers appear in `decisions.json`. A real implementation pass must verify those answers against source and tests and obtain actual approval; fixture owner labels are not people who answered in this session.
