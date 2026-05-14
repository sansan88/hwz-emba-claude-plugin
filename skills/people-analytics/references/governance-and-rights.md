# People Analytics Governance, Rights, and Legal Edges

This reference covers the legal and governance layer that any People Analytics program in Switzerland (with EU exposure) must honor. Not legal advice — pointers for executive design and for engaging counsel productively.

## The Swiss revFADP (Datenschutzgesetz, in force since September 2023)

Switzerland's revised Federal Act on Data Protection brings Swiss law closer to GDPR. Key relevances for People Analytics:

- **Personal data of employees** is fully covered. Special-category data (health, religion, union membership, biometric, genetic) has stricter requirements.
- **Information obligations** are extensive. Employees must be informed about purposes, retention, third parties, transfers.
- **Privacy impact assessments** (Datenschutz-Folgenabschätzung) are required for high-risk processing. Most algorithmic HR uses qualify.
- **Right to information** — employees can request what data the company holds about them.
- **Right to data portability** in some cases.
- **Automated individual decision-making** restrictions: decisions made solely by automated means with significant consequences need a legal basis and human override.

## GDPR for cross-border companies

Where Swiss companies have EU employees or EU customers, GDPR applies in parallel. Key Articles relevant for People Analytics:

- **Art. 6** — legal basis for processing (consent, contract, legitimate interest). Note: workplace consent is fragile because of the power imbalance — courts repeatedly find employee consent insufficient as a sole basis.
- **Art. 9** — special-category data (health, biometric, etc.) — additional safeguards.
- **Art. 22** — restrictions on automated individual decision-making.
- **Arts. 13–15** — transparency obligations.
- **Art. 35** — Data Protection Impact Assessment (DPIA) for high-risk processing.

## EU AI Act intersection (relevant from 2025–2027)

Most HR-related AI uses are classified as **high-risk** under the AI Act:

- AI for recruitment and selection
- AI for promotion, termination, task allocation
- AI for monitoring and evaluation of workers
- AI for performance scoring

Obligations for high-risk systems include risk management, data governance, technical documentation, human oversight, accuracy and robustness, transparency. These apply if the system is placed on the EU market or its outputs are used in the EU. Swiss companies operating across the border are bound.

## Worker representation rights

- **Switzerland:** No general works council right, but in companies with 50+ employees, Mitwirkungsgesetz gives workers right to information and consultation on certain matters including monitoring/measurement systems.
- **Germany, Austria, etc.:** Strong Betriebsrat / works council co-determination rights on monitoring systems. New monitoring or analytics systems frequently require works council agreement.
- **France:** CSE consultation obligations.
- **Sweden, Denmark, etc.:** Strong union role.

If the user operates in multiple jurisdictions, design to the highest standard — easier than running parallel programs.

## Governance functions to set up

Regardless of legal regime, four governance functions need to exist:

### 1. The data council
Cross-functional body that approves new People Analytics use cases. Composition:
- HR (use case owner)
- IT / data engineering
- Legal / data protection officer
- Information security
- Workforce representative (formal or informal)
- Optional: ethics/compliance

Decisions: approve, approve-with-conditions, reject, or defer.

### 2. The transparency surface
The default channel through which employees learn:
- What is measured about them
- Where the data comes from
- How long it is retained
- Who has access
- How it is used
- How to access their own data and request changes

Plain language. Updated when use cases change.

### 3. The audit cadence
- Annual internal audit of the program
- Periodic independent audit (every 2–3 years) by external party
- Bias audits for any model used in HR decisions, at least annually
- Sunset reviews for use cases (default 24 months unless re-approved)

### 4. The escalation channel
Named, accessible, low-friction channel for employees to raise concerns about People Analytics specifically. Concerns are tracked, patterns identified, responses documented. Outcome data shared back to the workforce in aggregate.

## The legitimate interest test

When using "legitimate interest" as a basis (rather than consent or contract), the three-part test:

1. **Purpose** — is the purpose legitimate?
2. **Necessity** — is the processing necessary for that purpose? Can the purpose be achieved less intrusively?
3. **Balancing** — do the company's interests outweigh the workers' rights and freedoms?

The balancing test is where most contested use cases fail. Productivity monitoring of individual workers, in particular, often fails on necessity (can be done at team level) and balancing (workers' interest in privacy outweighs marginal management benefit).

## The "would you publish it" test

A useful heuristic: would the company be comfortable describing the use case publicly, in detail, including who is measured, how, and what decisions are made? If the answer is no, the program is operating on opacity, which is a fragile foundation.

## Common compliance failures

- Treating workforce consent as a sufficient legal basis when it isn't
- Re-using data collected for purpose A for purpose B without fresh consent or basis
- Failing to do a DPIA before a major new use case
- Vendor contracts that don't specify data flows, retention, or sub-processors
- Cross-border transfers without proper safeguards
- No mechanism for employees to access their data or correct it
- Algorithmic decisions with no documented human-in-the-loop

## How to use this reference

In step 5 of the SKILL.md workflow, for each significant use case in the program:

1. Name the legal basis explicitly
2. Confirm the transparency commitment
3. Confirm retention period
4. Confirm whether the system makes automated decisions and whether human override is genuine
5. Confirm worker representation involvement where required
6. Confirm DPIA completion if high-risk

Programs that cannot answer these for each use case are operating with legal debt that will eventually be called.
