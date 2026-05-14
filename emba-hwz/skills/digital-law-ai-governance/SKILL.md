---
name: digital-law-ai-governance
description: Help leaders set up or audit AI Governance, navigate the EU AI Act and Swiss AI regulation, and stay ahead of digital-policy developments. Use whenever the user is working on AI governance, AI risk management, AI policy, AI compliance, classifying AI systems under the EU AI Act (prohibited / high-risk / limited / minimal), GenAI policy, AI procurement, AI literacy obligations, FADP/GDPR data implications for AI, AI in HR / credit / health contexts, or building an AI use register. Also trigger when the user mentions David Rosenthal, the EU AI Act, GPAI obligations, AI Pact, Council of Europe AI Convention, or is worried about the legal exposure of an AI use. Even when "governance" is not named — if the substance is "are we allowed to do this with AI?", use this skill.
---

# Digital Law & AI Governance — From Regulation to Operating Practice

This skill operationalizes EMBA Block 2 Tag 3 (Dr. Anne-Sophie Morand, HWZ). It is for the executive who needs to operate AI legally and responsibly without becoming a lawyer — but with enough understanding to ask the right questions, to set up a working governance function, and to avoid the most common compliance failures.

The unifying frame: AI governance is not just legal compliance. It is a *management system* that produces lawful, responsible, and effective AI outcomes. The EU AI Act is the dominant regulatory artifact, but it sits within a wider web of GDPR/FADP, copyright, sectoral rules, and the Council of Europe AI Convention. This skill helps integrate all of these into operating practice.

## When to lean on this skill

Use it when the user is: setting up AI governance, classifying AI systems for the EU AI Act, building a GenAI policy, evaluating vendor compliance, designing an AI risk management process, building an AI use register, conducting an AI impact assessment, designing AI literacy training, deciding on jurisdiction of operation, or running an AI compliance audit.

Do not use it for: pure legal opinions ("is this contract enforceable") or specific litigation advice. The skill helps the executive engage productively with counsel, not replace counsel.

## Mental model: the layered AI law stack

Hold this mental picture while working:

1. **EU AI Act** — the new sector-agnostic, risk-based framework. Phased application 2025–2027.
2. **GDPR (EU) / FADP (CH)** — data protection. Applies whenever AI processes personal data. Often the binding constraint in practice.
3. **Council of Europe Framework Convention on AI** — May 2024, broader geographic scope, principles-based.
4. **Sectoral rules** — financial services (MiFID, IFRS), healthcare (MDR), employment law, anti-discrimination, consumer protection. Often add obligations on top of the AI Act.
5. **Copyright & IP** — training data legality, output IP ownership, infringement risk in GenAI outputs.
6. **Swiss specifics** — currently no horizontal AI law; revFADP applies fully; sectoral approach in development. Major Swiss companies with EU exposure are effectively bound by the AI Act regardless.

A use case is governed by the *intersection* of these layers, not by any one alone.

## Workflow

### 1. Classify the AI system under the EU AI Act

Read `references/eu-ai-act-classification.md`. Walk through the four risk classes:

- **Prohibited** — social scoring, exploitation of vulnerable groups, untargeted facial recognition scraping, certain emotion recognition in workplace/education, biometric categorization of sensitive attributes, predictive policing based on personality assessment.
- **High-risk** — listed in Annex III (e.g., HR/recruitment, education access, essential services credit-worthiness, law enforcement, migration, critical infrastructure, biometric ID) and product-safety AI.
- **Limited risk** — transparency obligations for chatbots, deepfakes, AI-generated content.
- **Minimal risk** — most general business AI; few obligations.
- **GPAI (general-purpose AI models)** — separate tiered obligations including transparency and, above 10^25 FLOPs, systemic risk obligations.

State the classification with the rationale. Misclassification is the single biggest compliance risk; do it deliberately.

### 2. Build the AI use case register

Read `references/ai-use-case-register.md`. Every organization with serious AI exposure should maintain a register listing each AI system with its purpose, classification, data sources, vendor, owner, and review cadence. The AI Act effectively makes this mandatory for high-risk uses; good governance practice extends it to all material uses.

Use `templates/ai-use-case-register-row.md`. The register is the single artifact that lets the AI governance function actually function.

### 3. Run the AI impact assessment

For each high-risk use case (and recommended for limited-risk uses with significant individual impact), conduct an impact assessment that covers:

- Fundamental rights impact (specifically required under AI Act Art. 27 for certain deployers of high-risk AI)
- Data protection impact (DPIA under GDPR/FADP)
- Discrimination and bias risks
- Robustness, accuracy, error patterns
- Human oversight design
- Affected groups and their voice

Use `templates/ai-impact-assessment.md`.

### 4. Design the governance operating model

Read `references/governance-operating-model.md`. The core components:

- **AI policy** — short, principle-driven, employee-facing
- **AI use case register** — described above
- **Approval workflow** — for new AI use cases, with risk-tiered rigor
- **Risk management process** — for high-risk systems (AI Act Art. 9)
- **Human oversight design** — explicit per use case
- **Incident management** — for AI failures and harms
- **AI literacy training** — mandatory from Feb 2025 under Art. 4 of the AI Act
- **Vendor management** — contract clauses, audit rights, data flows
- **Audit and review cadence**

### 5. Address the GenAI policy

GenAI deserves a separate policy because it is everywhere and the typical risks are distinct from classical ML. Read `references/genai-policy-essentials.md`. Cover at minimum:

- Permitted vs. prohibited uses
- Data handling (what employees can put into prompts)
- IP and output ownership
- Disclosure obligations (when output is GenAI-generated)
- Vendor approval (which GenAI tools are sanctioned)
- Training of employees on hallucination, prompt injection, bias

### 6. Verify the sectoral and jurisdictional fit

Many AI use cases face additional sectoral rules. Pull the right ones based on the user's industry:

- **Financial services:** model risk management (SR 11-7, ECB TRIM, FINMA guidance), explainability, anti-discrimination in credit.
- **Healthcare:** MDR for AI-as-medical-device, FDA equivalents.
- **HR:** equality directives, works council rights, transparency obligations.
- **Consumer / public-facing:** consumer protection, marketing rules, anti-deception.

Jurisdictional fit: where does the user offer the service? Where are the data subjects? Where is the model trained or deployed? Each location may add obligations.

### 7. Produce the integrated brief

Deliver:

1. Classification of the AI system(s) with rationale
2. The applicable legal layers and what each demands
3. The impact assessment findings, with risks and mitigations
4. The governance setup recommended (or gaps in existing setup)
5. The 90-day action list
6. The vendor / contract implications

## Output style

Precise but accessible. Cite specific articles where they bite. Distinguish what is required from what is good practice. Avoid both the legal-fog tone (where everything is "may," "could," "depends") and the false-certainty tone. State confidence levels.

## Pitfalls to avoid

- **Compliance theater.** A policy document nobody reads, a register nobody updates, a training nobody attends. The work is operational, not paper.
- **Cargo-culting the EU AI Act.** Not every AI use is high-risk; not every high-risk use needs the maximum machinery. Size to risk.
- **Ignoring GDPR/FADP because the AI Act exists.** Most AI compliance failures will still be data protection failures.
- **Bolting governance onto procurement after the fact.** Vendor selection without governance criteria locks in compliance debt.
- **Treating AI Act compliance as a deadline.** It is an ongoing system. Models drift; risks change; documentation must be kept live.
- **No senior accountability.** AI governance without a senior named owner drifts into IT and becomes unable to influence business decisions.
- **Underestimating GenAI shadow use.** Employees use ChatGPT, Claude, Copilot whether or not policy says they can. Build a sanctioned path before shadow use becomes the norm.

## Key sources

- Regulation (EU) 2024/1689 (the AI Act). [Full text](https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=OJ:L_202401689)
- David Rosenthal, *Der EU AI Act – Verordnung über künstliche Intelligenz*, Jusletter 5. August 2024.
- N. Braun Binder, T. Burri, M. Lohmann et al., *Künstliche Intelligenz: Handlungsbedarf im Schweizer Recht*, Jusletter 28. Juni 2021.
- Swiss FADP / revDSG (2023).
- Council of Europe Framework Convention on AI, CETS 225 (2024).
- Swiss Federal Council guidance on AI regulation (digital.swiss).

The reference files inside this skill apply these to operating practice.
