# AI Governance Operating Model — Components and Decisions

A practical operating model for AI governance in a mid-to-large organization. Not the only model — but a working starting point that meets EU AI Act obligations and reflects emerging good practice.

## Why a separate AI governance function exists

Three reasons that justify the overhead:

1. **Regulatory complexity** spans legal, data protection, security, ethics, sectoral, IP. No single existing function owns all of them.
2. **Cross-cutting nature** — AI sits in every business unit; without a horizontal function, standards fragment.
3. **Speed of change** — both technology and regulation change yearly; a function dedicated to keeping the operating model current is required.

Companies that try to bolt AI governance onto an existing function (usually IT or risk) typically discover the bolt-on is insufficient within 12–18 months.

## Components

### 1. AI policy (employee-facing)

A short document (2–4 pages) stating the company's AI principles, permitted and prohibited uses, decision rights, and how to get an AI use case approved. Written in plain language. Signed by the CEO or equivalent — signaling matters.

What it covers:
- Why we use AI
- Principles (typically: human-centered, fair, transparent, accountable, lawful, secure)
- What is forbidden (clear examples)
- The approval path for new AI use cases
- The escalation path for concerns
- Sanctioned vs unsanctioned AI tools

### 2. AI use case register

A live inventory of every AI system in use across the company. For each:
- Name, owner, business unit
- Purpose and AI capability used
- Risk classification under the AI Act
- Data sources and flows
- Vendor (if applicable) and contract reference
- Decision rights (autonomous vs human-in-loop)
- Impact assessment reference
- Review date and sunset clause
- Incident history

Maintained by the AI governance function. Updated on every new use case approval and on quarterly review of existing ones.

### 3. Approval workflow

Risk-tiered approval depth:

- **Minimal risk** (most internal tools, GenAI co-pilots within sanctioned vendors): fast track — registration, light review.
- **Limited risk** (customer-facing chatbots, content generation with disclosure obligations): medium review including transparency check.
- **High risk** (HR AI, credit scoring, biometrics, regulated sectors): full review including risk management system, impact assessment, human oversight design, vendor diligence.
- **Prohibited or near-prohibited**: senior leadership approval and counsel sign-off mandatory.

Approval bodies:
- Fast track: AI governance lead alone
- Medium: AI governance lead + DPO or legal review
- High-risk: AI governance committee (cross-functional: AI/data, legal/DPO, security, business sponsor, ethics)
- Senior: AI governance committee + executive sponsor + counsel

### 4. Risk management process (AI Act Art. 9)

For high-risk systems, a documented risk management process running across the system's lifecycle. Includes:
- Identification and analysis of known and foreseeable risks
- Estimation and evaluation of risks
- Risk mitigation measures
- Residual risks evaluated against acceptable level
- Continuous, iterative — not a one-off

Integrate with existing enterprise risk management where possible.

### 5. Human oversight design

For each AI system, document:
- Who can override the AI output
- Under what circumstances they will override (clear criteria)
- How the override is logged and reviewed
- Whether the oversight is meaningful or token

Token oversight (rubber-stamping AI decisions) does not meet AI Act obligations and produces neither compliance nor good decisions. Audit periodically.

### 6. Incident management

A defined process for AI incidents:
- What counts as an AI incident (errors above threshold, bias findings, harm to affected persons, security compromises, regulatory inquiries)
- Reporting channel
- Triage and severity scoring
- Investigation and root cause
- Remediation
- For high-risk systems: external reporting obligations (Art. 73, 15 days for serious incidents)

### 7. AI literacy training

To meet Art. 4: documented training for all employees dealing with AI. Tiered:
- **Tier 1** (all staff): basics — what AI is, what it is not, common failure modes, the company's policy, sanctioned tools, what to do if you see a problem.
- **Tier 2** (deployers/operators of AI systems): system-specific training on operation, limitations, oversight.
- **Tier 3** (high-risk system operators): detailed training on the specific system, conformity obligations, incident handling.

Records kept. Refresh annually or on material change.

### 8. Vendor management

AI vendor contracts must include:
- Description of the AI system, including capability and limitations
- Data flows (what the vendor receives, retains, processes)
- Sub-processors disclosure
- Training data lineage (especially for GPAI)
- Audit rights
- Incident notification obligations
- Liability for AI Act non-compliance
- Termination rights and data return

For GenAI vendors specifically:
- IP indemnification for outputs
- Data residency for prompts and outputs
- Whether prompts are used for training (must usually be opt-out)
- Logging and retention

### 9. Audit and review

Cadence:
- **Quarterly:** review of new use cases in the register
- **Semi-annual:** review of high-risk systems for drift, incidents, performance
- **Annual:** full program audit by independent function (internal audit or external)
- **Triggered:** review on significant change (model update, scope change, incident)

## Roles and accountability

A workable role split:

| Role | Owner | Accountability |
|------|-------|----------------|
| AI governance lead | Senior, reports to CRO / GC / COO | Operating model, policy, approvals |
| Data protection officer | Existing DPO | GDPR/FADP compliance for AI use cases |
| AI ethics lead | Often combined with governance lead in smaller orgs | Bias audits, fundamental rights assessments |
| AI security lead | Existing CISO function | Adversarial robustness, prompt injection, data exfiltration |
| Business sponsor (per use case) | Senior business owner | Value capture, fitness for purpose, adoption |
| Use case owner (per use case) | Operational owner | Day-to-day operation, oversight execution |
| Internal audit | Existing function | Independent program review |

The senior owner (governance lead) should sit at C-1, not buried in IT. AI governance lacks teeth otherwise.

## What "good" looks like at 12 months

- Every material AI use in the company is in the register
- New use cases are approved through documented workflow, with median time-to-approval that does not bottleneck business
- High-risk systems have impact assessments and human oversight design documented
- AI literacy training is complete for all staff with a refresh cadence
- One independent audit has been conducted and remediations are tracked
- The CEO can say in front of a regulator or journalist what the company does with AI and how it is governed

If most of these are absent at 12 months, the program is at risk.

## Common scaling failures

- **Approval body becomes a bottleneck** — fast-track tier missing or unused.
- **Register goes stale** — no one is paid to maintain it; it becomes a snapshot from launch.
- **Governance separates from business** — the function says no a lot, business routes around it (shadow AI).
- **Compliance theater** — documents exist, behavior unchanged.

The fix in each case: build the function with business partnership built in. Governance that enables value capture by making the path-to-yes clear is sustainable. Governance that only says no is not.
