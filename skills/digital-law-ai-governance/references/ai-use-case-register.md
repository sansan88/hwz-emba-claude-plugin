# AI Use Case Register — Why and How

The register is the single most operationally important artifact in an AI governance program. Without it, every other component (approvals, audits, incident management, training, vendor management) operates blind.

## What it is

A live inventory of every AI system used or deployed by the organization. Owned by the AI governance function. Updated continuously, not annually.

## What it captures (per entry)

For each AI system:

**Identification**
- Use case ID (unique, persistent)
- Name (short, memorable)
- Status (proposed, approved, in-production, deprecated)
- First deployed date
- Sunset / next review date

**Business**
- Business unit owner
- Business sponsor (senior accountable)
- Operational owner
- Purpose (one-sentence)
- Affected user populations (employees, customers, third parties)
- Volume (decisions/predictions/generations per period)

**Technical**
- AI capability used (classical ML, deep learning, LLM, agentic, etc.)
- Model provenance (in-house, vendor, open-weights, etc.)
- Vendor (if applicable) and contract reference
- Data sources (with sensitivity classification)
- Decision logic (advisory, recommend-with-override, autonomous)
- Human oversight design summary

**Compliance**
- EU AI Act classification (prohibited / high-risk / limited / minimal) with rationale
- Provider or deployer status under the Act
- Conformity assessment status (if high-risk provider)
- Fundamental rights impact assessment status (if applicable)
- DPIA status (if processing personal data)
- Legal basis for processing (if personal data)
- Sectoral compliance status (e.g., model risk management for financial services)
- AI Act Art. 26 obligations met (if deployer of high-risk)
- Art. 27 fundamental rights impact assessment done (if applicable)

**Risk**
- Identified risks
- Mitigations in place
- Residual risk rating
- Known incidents

**Governance**
- Approval date and approver
- Last review date and reviewer
- Audit findings (if any)
- Sunset clause / criteria for revocation

## Where it lives

- Single source of truth, accessible to AI governance, legal, security, internal audit, business sponsors
- Typically a database (Notion, ServiceNow, dedicated GRC tool, or purpose-built register)
- Read access broader than write access
- Audit trail of changes preserved

## Workflow integration

The register is not a static document. It is the operational core:

- **New use case proposal** → register entry created (status: proposed)
- **Approval workflow** → register entry updated through review steps
- **Deployment** → status moves to in-production
- **Quarterly review** → status, risk, and incidents updated
- **Significant change** (model update, scope change) → re-review triggered
- **Incident** → recorded against the use case
- **Audit** → findings recorded
- **Sunset** → status moves to deprecated, data handling triggered

## Discoverability — finding the use cases that are not in the register

The first time you build a register, the hard work is finding the AI uses that are not yet visible. Channels:

- **Procurement scan** — any contract mentioning AI, ML, prediction, automation, intelligent
- **Vendor self-disclosure request** — write to all software vendors and ask which of their products incorporate AI; how that AI processes your data; under what model
- **SaaS tool inventory** — most enterprise SaaS now has AI features; document which are enabled
- **Business unit survey** — but treat self-reports with caution; many use cases are not labeled "AI"
- **Network scan** — identify which AI vendor domains are being hit from corporate networks (with employee notice)
- **HR/IT ticket scan** — requests to install or access AI tools

Expect the first inventory to find use cases the governance function did not know about. That is the point.

## Common register failures

- **Built once, then frozen.** A snapshot, not a live system. Useless within 6 months.
- **Too granular or too coarse.** Each "use case" should be discrete enough that classification and approval make sense for it. Avoid both "we use AI" (too coarse) and one entry per individual model call (too granular).
- **Owned by IT only.** Without business sponsorship, the register reports the IT view but misses the business reality of how AI is used.
- **No teeth.** If unregistered AI use carries no consequence, the register stays incomplete.

## The 90-day starter

For an organization without a register today:

- **Week 1–2:** Define the register schema. Pick the tool. Define the owner.
- **Week 3–6:** Discovery. Find existing AI uses through the channels above. Aim for breadth over depth — get the names in first, populate fields next.
- **Week 7–10:** Classification. Walk through each entry with legal/governance to assign AI Act class and risk rating.
- **Week 11–12:** First review. Identify the high-risk entries that need immediate attention (impact assessment, oversight design, etc.).

At day 90, the register exists, the riskiest cases are identified, the governance function is operating on real data rather than impressions.
