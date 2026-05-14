# EU AI Act — Classification and Key Obligations

This reference is for the executive who needs to classify an AI system correctly and understand the operational obligations that follow. It is not a substitute for the full Regulation (EU) 2024/1689 or for counsel — it is a workable mental map.

## The four risk classes plus GPAI

The Act applies a risk-based architecture to AI **systems** placed on the EU market or whose outputs are used in the EU. Separately, it regulates general-purpose AI **models**.

### Class 1 — Prohibited (Art. 5)

These AI practices are forbidden, with few narrow exceptions. Examples:

- **Subliminal manipulation** beyond awareness causing harm
- **Exploitation of vulnerabilities** (age, disability, social/economic situation)
- **Social scoring** by public or private actors based on personal characteristics, leading to detrimental treatment
- **Predictive policing** based solely on profiling/personality assessment
- **Untargeted scraping** of facial images from the internet/CCTV for facial recognition databases
- **Emotion recognition** in workplace and education (with narrow medical/safety exceptions)
- **Biometric categorization** inferring race, political opinions, union membership, religion, sex life
- **Real-time remote biometric identification** in publicly accessible spaces for law enforcement (with narrow exceptions)

Prohibitions apply from **2 February 2025**. Penalties up to €35M or 7% of global turnover.

For business: most companies will not be touching prohibited practices, but emotion recognition in HR/education is the most common surprise hit. Check carefully if any HR analytics or training tool claims to infer emotional states.

### Class 2 — High-risk (Art. 6 + Annex III)

Two paths to high-risk classification:

**Path A:** AI used as a safety component of a product covered by EU product safety legislation (e.g., medical devices, machinery, toys, automotive).

**Path B:** AI listed in Annex III, including:

- **Biometrics** (identification, categorization, emotion recognition outside prohibited contexts)
- **Critical infrastructure** management
- **Education and vocational training** — admission, evaluation, monitoring, exam integrity
- **Employment** — recruitment, selection, decisions on promotion/termination, task allocation, performance evaluation, monitoring
- **Essential services** — credit-worthiness, life and health insurance pricing
- **Law enforcement**
- **Migration, asylum, border control**
- **Administration of justice and democratic processes**

Note: a system may fall in Annex III categories but not be high-risk if it is purely preparatory, narrow procedural, etc. (Art. 6(3)). The deployer must document the reasoning.

**Obligations for providers of high-risk systems** (the entity placing the system on the market):
- Risk management system across the lifecycle (Art. 9)
- Data governance — training data quality, bias mitigation (Art. 10)
- Technical documentation (Art. 11, Annex IV)
- Logging (Art. 12)
- Transparency and instructions for use (Art. 13)
- Human oversight (Art. 14)
- Accuracy, robustness, cybersecurity (Art. 15)
- Quality management system (Art. 17)
- Registration in EU database (Art. 49)
- Conformity assessment before market placement (Art. 43)
- Post-market monitoring (Art. 72) and incident reporting (Art. 73)

**Obligations for deployers (users) of high-risk systems** (Art. 26-27):
- Use according to instructions
- Human oversight by qualified persons
- Input data appropriateness
- Monitoring of operation, reporting of serious incidents and risks
- For certain deployers (public authorities and certain private actors using AI in employment, essential services, credit): **fundamental rights impact assessment** (Art. 27)
- Inform employees and worker representatives before deploying high-risk AI in the workplace

Most obligations apply from **2 August 2026**. High-risk AI embedded in regulated products: **2 August 2027**.

### Class 3 — Limited risk (Art. 50)

Transparency obligations:

- Chatbots / interactive AI must inform users they are interacting with AI (unless obvious)
- Deepfakes must be labeled as artificially generated/manipulated
- AI-generated text on matters of public interest must be labeled (with exceptions for editorial control)
- Emotion recognition or biometric categorization systems must inform affected persons

Applies from **2 August 2026**.

### Class 4 — Minimal risk

No specific AI Act obligations. Most general business AI (spam filters, recommendation engines for non-sensitive contexts) sits here. Voluntary codes of conduct encouraged.

### GPAI models (Art. 51-55)

Separate tiered regime for **general-purpose AI models** (foundation models like GPT, Claude, Llama):

**All GPAI models:**
- Technical documentation
- Information to downstream providers
- Copyright policy
- Summary of training data

**GPAI with systemic risk** (above 10^25 FLOPs training compute, or designated):
- Additional model evaluations including adversarial testing
- Systemic risk assessments and mitigations
- Serious incident reporting
- Cybersecurity protections

GPAI obligations apply from **2 August 2025**.

## Common classification pitfalls

- **Assuming "we don't make AI, we use it" puts you outside scope.** Deployers have substantial obligations under Art. 26-27, especially for HR-related AI.
- **Misclassifying HR/recruitment AI as limited or minimal.** It is high-risk.
- **Treating internal-only deployment as out of scope.** Internal HR AI is in scope if the data subjects are in the EU.
- **Confusing GPAI obligations with downstream system obligations.** If you use a GPAI model in a product or service, both regimes apply: the GPAI provider has model-level obligations; you, as the downstream system provider, may have system-level obligations.
- **Missing the workplace consultation obligation.** Deploying high-risk AI in the workplace requires informing affected employees and worker reps *before* deployment.

## Timeline (key dates)

| Date | What applies |
|------|--------------|
| 2 Feb 2025 | Prohibitions; AI literacy obligations |
| 2 Aug 2025 | GPAI obligations; governance rules |
| 2 Aug 2026 | High-risk system obligations (Annex III paths); transparency obligations |
| 2 Aug 2027 | High-risk in regulated products (Annex I path) |

## Geographic scope and Swiss companies

The AI Act applies to:
- Providers placing AI on the EU market (regardless of provider location)
- Deployers established in the EU
- Providers and deployers whose AI **outputs are used in the EU**

The third trigger means many Swiss companies are de facto bound: if their AI tool's outputs reach EU employees, customers, or partners, the Act applies.

Pragmatic implication: most Swiss companies of meaningful size should design to AI Act standards regardless of whether a Swiss horizontal law exists.

## AI literacy obligation (Art. 4)

A frequently overlooked but easy-to-comply-with obligation, in force from Feb 2025: providers and deployers must ensure that staff dealing with AI have sufficient AI literacy for their role, considering their context, the AI systems used, and the persons or groups affected.

There is no prescriptive curriculum. Practical interpretation:
- Documented training on AI fundamentals for staff who deploy or use AI
- Role-specific training for those operating high-risk systems
- Records of training completion
- Refresh cadence

This is the cheapest single piece of compliance to do. Do it.

## How to use this in the workflow

In step 1 of the SKILL.md workflow, walk through the classification for each AI use case the user has named. State:

1. Which class it falls in (with article reference)
2. Why (the specific Annex III path or feature)
3. Whether the user is provider, deployer, or both
4. Which obligations apply and by when
5. Where the conformity / impact assessment gaps are

Classification with rationale is the single most useful artifact to produce.
