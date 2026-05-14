# GenAI Policy Essentials

A separate reference because GenAI (LLMs, image gen, GenAI in productivity tools, GenAI in customer service) deserves its own policy. The risks are distinct from classical ML, and employees use these tools every day whether or not policy says they can.

## The core problem

GenAI is the first AI technology to be both:
- **Useful out of the box** for general knowledge work without training a model
- **Available to every employee on day one** via consumer interfaces (chat.openai.com, claude.ai, copilot.microsoft.com, etc.)

That combination produces shadow use. Policies that try to ban GenAI without offering a sanctioned alternative fail predictably — employees use it anyway, but now without governance visibility.

## The right strategic posture

**Enable, channel, govern.** Pick sanctioned tools, train employees on safe use, monitor for prohibited use, iterate.

Three things to avoid:
1. **Full ban without alternative.** Produces shadow use.
2. **Free-for-all without policy.** Produces incidents.
3. **Policy without sanctioned tools.** Same as #1.

## Components of a GenAI policy

### 1. Sanctioned tools

Name the specific products approved for company use, with the data tier each is approved for. Example:

| Tool | Sanctioned for | Not for |
|------|----------------|---------|
| Microsoft 365 Copilot (M365 tenancy) | Internal data, customer correspondence, code (with review) | Highly confidential data, PII outside standard processing |
| ChatGPT Enterprise / Team | Same as Copilot | Same restrictions |
| Public ChatGPT / Claude / Gemini | Non-sensitive tasks, public information | Any company data, customer data, code |

Update list quarterly.

### 2. Data handling rules

What can employees put into GenAI prompts? Tiered guidance:

- **Public information** — fine in any sanctioned tool
- **Internal information** — only in tools with proper data residency and no-training commitments
- **Confidential information** — only with explicit approval and DPO review
- **Special-category personal data** (health, biometric, etc.) — never without specific legal basis
- **Customer data** — only in tools with appropriate processing agreements
- **Proprietary code** — only in approved code-aware tools (Copilot, Cursor Enterprise, etc.) with the no-training commitment

The simplest test: "If this prompt content leaked publicly tomorrow, what damage would it cause?" Above a threshold, do not paste it.

### 3. IP and output handling

- **Outputs are not automatically copyrighted in most jurisdictions.** Treat as draft material, requiring human authorship contribution before claiming copyright.
- **Outputs may infringe third-party IP.** Code or content that closely resembles training data can be infringing. Review outputs as you would review any draft.
- **Vendor IP indemnification** — check whether the vendor indemnifies you for IP claims arising from outputs. Microsoft and OpenAI offer this for enterprise tiers; consumer tiers do not.
- **For client-facing deliverables:** GenAI-assisted work should typically be disclosed per the client's own policy or per professional obligations (some bar associations now require disclosure).

### 4. Transparency obligations

Under EU AI Act Art. 50 and equivalent:
- AI-generated text on matters of public interest must be labeled (with editorial-control exception)
- Deepfakes must be labeled
- AI chatbots must disclose

Internally, the practical rule: when GenAI has materially produced content presented as the work of a person, disclose. Norms here are still forming; conservative defaults are wiser than aggressive.

### 5. Prohibited uses

A clear list. Typical:
- Generating content that infringes third-party IP
- Producing deceptive content (deepfakes, impersonation)
- Decisions about individuals' employment, credit, healthcare, or rights without human-in-loop
- Output used unchecked in safety-critical contexts
- Code generation for security-sensitive components without review
- Generation of content involving minors that could be misused
- Generation of content that violates company anti-discrimination or anti-harassment policies

### 6. Hallucination and verification expectations

Train employees that GenAI outputs are *drafts to verify*, not *truths to repeat*. Verification expectations by use:

- **Internal brainstorming** — light verification, low risk
- **Customer-facing content** — full verification of facts, names, numbers
- **Legal, medical, financial advice** — full domain expert review
- **Code** — testing and security review
- **Citations and references** — every citation verified to its source (GenAI fabricates plausible citations frequently)

### 7. Vendor and prompt-injection safety

For GenAI integrated in business workflows (not just standalone chat):
- Inputs from untrusted sources (web pages, emails, documents) can carry prompt-injection attacks
- Treat untrusted input as untrusted; do not let GenAI agents take consequential actions based on untrusted instructions
- Security review for any GenAI agent with access to action tools (sending email, accessing files, making purchases)

### 8. Training and literacy

Employees should be trained on:
- How GenAI works at a basic level (pattern-matching, not knowing)
- Why hallucinations happen and how to spot them
- Prompt injection and what to avoid
- The sanctioned tools and when to use which
- Reporting channel for concerns or incidents

Cover Art. 4 AI literacy obligation with this same training.

## Common failure modes

- **The vague policy.** "Use GenAI responsibly" — meaningless. Employees need specifics.
- **The unenforceable policy.** "No GenAI without manager approval" — manager has no time, employee uses ChatGPT anyway.
- **The reactive policy.** Policy written after a specific incident, narrowly addressing that incident, missing the systemic issue.
- **The frozen policy.** Written once, never updated. GenAI capability and risk landscape changes too fast for that.

A working GenAI policy is short, specific, refreshed quarterly, and tied to actually sanctioned tools.

## How to use this in the workflow

When the user asks about GenAI policy:
1. Diagnose the current state (no policy / vague / specific / sanctioned tools in place)
2. Identify which components are missing
3. Draft the components in order of risk reduction: sanctioned tools and data tiers first, prohibited uses second, training and transparency third
4. Build the review cadence

A 4-page document beats a 40-page document for adoption.
