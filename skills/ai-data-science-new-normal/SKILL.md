---
name: ai-data-science-new-normal
description: Help business leaders shape AI and data science strategy at the organizational level — building use case portfolios, assessing AI maturity, designing the operating model, and asking the right questions when confronted with vendor pitches or internal AI proposals. Use whenever the user is working on an AI strategy, AI roadmap, AI use case selection, AI maturity assessment, AI-powered organization design, ML project scoping, vendor evaluation, "where should we apply AI in our business?", or wants to understand what AI / ML / GenAI can and cannot do at a level deep enough to make business decisions. Also trigger when the user mentions prediction machines (Agrawal/Gans/Goldfarb), the Fountaine/McCarthy/Saleh AI-powered organization article, AI ROI, AI center of excellence, hub-spoke AI operating models, or proof-of-concept fatigue. Use it even when the user does not say "AI strategy" explicitly — if the substance is "what should we do with AI?" or "is this AI project worth doing?", use this skill.
---

# AI & Data Science as the New Normal — Strategic Operating Lens

This skill operationalizes EMBA Block 2 Tag 1 (Dr. Marcel Blattner, HWZ). It is built for non-technical executives who need to make consequential AI decisions — about strategy, investment, use cases, vendors, and operating model — without becoming ML engineers, but also without being snowed by buzzwords.

The thesis Fountaine, McCarthy, & Saleh (2019) made the dominant frame: **the binding constraint on AI value is not technology, it is culture, operating model, and use case discipline.** This skill keeps that thesis as the spine.

## When to lean on this skill

Use it when the user is: shaping an AI strategy, choosing AI use cases, evaluating a vendor or internal proposal, designing an AI operating model (centralized, federated, hub-and-spoke), assessing AI maturity, prioritizing an AI roadmap, sizing investment, or trying to translate a buzzword-heavy proposal into a concrete decision.

Do not use it for: pure technical ML problem-solving ("how do I tune this model"), specific data engineering tasks, or implementation-level coding. Those need a different toolkit.

## Mental model: the three layers of AI value capture

Hold these three together. Skipping any one is why most AI investments fail to land.

1. **Capability layer** — what AI/ML/GenAI can technically do for the user's specific problem class. Most often this is prediction or generation; sometimes retrieval, classification, or optimization.
2. **Use case layer** — which business problems are worth pointing AI at, given economics, data availability, change cost, and risk. This is the prioritization layer.
3. **Organizational layer** — what the company has to be like to capture value from AI: data foundation, talent, operating model, decision rights, ways of working. Fountaine et al.'s domain. The most common failure layer.

When delivering an output, walk all three. If the user is missing one layer, name the gap.

## Workflow

### 1. Decode the actual question

AI conversations are noisy. Strip away the buzzwords and identify what the user is really asking. Common patterns:

- "What's our AI strategy?" → usually means: which use cases, how much investment, what operating model.
- "Should we build or buy?" → usually means: build/buy/partner for which capabilities, with what data implications.
- "Is this vendor real?" → usually means: do their claims match the underlying capability, are the use cases mature, what is the path to value.
- "Should we do this AI POC?" → usually means: is this worth doing as a real product, or is it POC theatre.

Sharp questions get sharp answers. Restate the question explicitly to the user before answering.

### 2. Demystify the capability

Read `references/ai-capability-primer.md` for the operating-level mental model of how modern ML and GenAI work, framed for executives. Then say to the user, in plain language:

- What class of problem this AI capability addresses (prediction, generation, classification, retrieval, optimization, agentic action)
- What data it needs and where that data has to come from
- What it cannot do reliably (the failure modes that matter for business decisions)
- What the realistic accuracy / quality envelope is

A vendor pitch that does not survive this translation should fail this filter.

### 3. Build the use case portfolio

Read `references/use-case-portfolio.md`. The discipline: do not collect AI use cases the way one collects pokemon. Build a portfolio sized to the company's maturity, with explicit ROI and feasibility ratings.

Use the canvas in `templates/use-case-canvas.md` for each candidate use case. The portfolio should include:

- **2–3 quick wins** (high feasibility, modest but real value, short time-to-value). These build capability and trust.
- **1–2 strategic plays** (high value, harder, longer). These are the bets.
- **Optional: 1 moonshot** (transformational if it works, plausibly does not work). Only if the company has the capacity to absorb failure.

The single most common executive mistake here: choosing only moonshots because they are exciting, then losing the support of the rest of the business when none of them ships in year one.

### 4. Assess AI maturity

Use the framework in `references/ai-maturity-assessment.md`. Maturity sits on five dimensions: strategy, data foundation, talent, operating model, culture. The score reveals what the company can actually do *now*, vs. what it could plan to do over 18–36 months.

Mismatched ambition and maturity is the most common failure mode of AI strategies. A company at maturity level 1 cannot execute a level-4 strategy, no matter how good the slides.

### 5. Design the operating model

Read `references/operating-model.md`. The Fountaine/McCarthy/Saleh hub-and-spoke model is the most widely adopted pattern:

- **Hub** — center of excellence with deep ML, data engineering, MLOps, governance, ethics talent
- **Spokes** — embedded teams in business units that own use cases, with domain context
- **Gates** — clear hand-off points and shared standards

Other patterns (centralized, fully federated, project-based) work in specific contexts. Pick deliberately, do not drift into one.

### 6. Address the culture & change layer

This is where most AI initiatives die. Fountaine et al.'s observation: technology is rarely the bottleneck. The bottleneck is decision rights, incentives, and the willingness of business owners to actually use the AI outputs in their work.

For each significant use case, surface:
- Who has to change their behavior for value to be captured?
- What loss does that behavior change involve (status, autonomy, role definition)?
- Who owns the use case end-to-end — both technical and business?
- What is the explicit decision rights map between the AI hub and the business unit?

### 7. Produce the integrated brief

Deliver:

1. Sharpened question
2. Capability assessment in plain language
3. Use case portfolio (3–6 use cases, classified)
4. Maturity assessment with honest scoring
5. Operating model recommendation
6. The 90-day moves to get started
7. The change/culture risks and mitigation

## Output style

Plain language. Treat AI as a tool that needs business judgment, not as a magical force. Be honest when the question is misframed. Quantify carefully — vendor-style ROI claims (3x revenue, 50% efficiency) are usually fabricated; honest ranges with confidence levels are more credible and more useful.

## Pitfalls to avoid

- **Solution looking for a problem.** "We need an AI strategy" is not a use case. Start from business problems, not from the technology.
- **POC theatre.** Endless proofs-of-concept that never become products. Discipline: every POC must have a defined path-to-production and a kill criterion.
- **Boil-the-ocean data project.** "First we'll build the data lake, then we'll do AI." Often becomes a multi-year delay with no business value. Better: pick a thin slice, build the data foundation as a byproduct of solving a real use case.
- **Outsourcing thinking to vendors.** A vendor pitch is not a strategy. Demand specifics about your data, your use case, your integration.
- **Ignoring the change layer.** An AI model that produces a great prediction nobody acts on creates zero value.
- **Hype-cycle whiplash.** Last year it was LLMs, this year it is agents, next year it will be something else. Anchor on the durable underlying capability (prediction, generation, classification) rather than the buzzword of the quarter.
- **Treating GenAI as a substitute for understanding.** GenAI is a co-pilot for many knowledge tasks but introduces specific failure modes (hallucination, prompt brittleness, IP/data exposure) that need governance.

## Key sources

- Fountaine, T., McCarthy, B., & Saleh, T. (2019). *Building the AI-Powered Organization.* HBR.
- Agrawal, A., Gans, J., & Goldfarb, A. (2018). *Prediction Machines.* (Heath 2019 review in JITCAR.)
- Davenport, T. & Ronanki, R. (2018). *AI for the Real World.* HBR. (Use case classification.)
- McKinsey State of AI annual reports, for current adoption benchmarks.

Reference files inside this skill apply these to executive practice.
