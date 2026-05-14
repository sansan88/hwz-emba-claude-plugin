# AI Maturity Assessment

A working framework to honestly assess where the organization is *now* in AI capability. The framework: five dimensions, five levels each. The output is not a vanity score — it is a diagnostic of what the company can realistically execute in the next 12–24 months.

## The five dimensions

### 1. Strategy & alignment
How clear is the link between AI activity and business priorities?

- **Level 1 — Reactive:** Ad-hoc experiments, no shared narrative.
- **Level 2 — Aware:** AI mentioned in strategy decks; no operational link.
- **Level 3 — Aligned:** Defined AI priorities tied to 2–3 business goals.
- **Level 4 — Embedded:** AI strategy is a core component of business strategy; roadmap is integrated.
- **Level 5 — Generative:** AI capability shapes which strategic options the business pursues.

### 2. Data foundation
Does the organization have the data, in usable form, to do AI well?

- **Level 1 — Fragmented:** Data in silos, poor quality, no governance.
- **Level 2 — Defined:** Some critical datasets identified; quality issues known.
- **Level 3 — Available:** Core datasets accessible, documented, basic governance.
- **Level 4 — Integrated:** Data platform supports multi-domain use cases; lineage and quality monitoring.
- **Level 5 — Productized:** Data products with SLAs; data treated as a strategic asset.

### 3. Talent & skills
Does the organization have the people to build, deploy, and use AI?

- **Level 1 — Absent:** No internal ML capability; vendor-dependent for everything.
- **Level 2 — Spotty:** Pockets of capability; no shared standards.
- **Level 3 — Functioning:** Identifiable AI team; basic MLOps maturity.
- **Level 4 — Mature:** Senior ML/data engineering leadership; cross-functional collaboration is normal.
- **Level 5 — Distinctive:** Talent density is a competitive advantage; the company attracts senior talent on reputation.

### 4. Operating model
How is AI work organized and connected to the business?

- **Level 1 — Ad-hoc:** AI projects pop up from anywhere, succeed or fail in isolation.
- **Level 2 — Project-based:** Discrete AI projects, no shared infrastructure.
- **Level 3 — Hub or federated, partly:** A central function exists but business connection is weak, or the reverse.
- **Level 4 — Hub-and-spoke working:** Hub provides expertise and standards; spokes own use cases; clear handoffs.
- **Level 5 — Platform-driven:** Reusable AI platform plus mature operating model; new use cases launch in weeks not quarters.

### 5. Culture & ways of working
Does the organization actually use AI outputs and adapt as a result?

- **Level 1 — Resistant:** AI is seen as IT's problem or as a threat.
- **Level 2 — Curious:** Interest exists; behavior unchanged.
- **Level 3 — Adopting:** Specific teams use AI outputs in their decisions.
- **Level 4 — Adapting:** Processes and decision rights have been redesigned around AI.
- **Level 5 — Learning:** The organization continuously learns from AI outputs and updates models and processes; AI literacy is widespread.

## How to score

Score honestly. Each dimension at the level the *typical* state matches, not the best example. If the IT team has level-4 data foundation but the rest of the company has level-2, the org-wide score is closer to 2.

Average across dimensions is misleading. The binding constraint is the lowest score — that is where the company is actually stuck.

## What the score implies

- **Average ≤ 2:** Focus on quick wins, basic data foundation, hiring a small core team. Strategic plays are premature.
- **Average 2–3:** Build the use case portfolio carefully; invest in operating model; don't over-promise.
- **Average 3–4:** Scale; standardize; build a platform; widen the talent base.
- **Average 4+:** AI is a strategic lever; the competitive question is which proprietary capability or data set to build.

## What the framework will not tell you

This framework is a diagnostic, not a recipe. It tells you where you are. It does not tell you which use cases to pick — that is the use case portfolio work. It does not tell you what to sell — that is the strategy work. It tells you what the *organizational ground* can support.

A company at maturity level 2 attempting to execute a level-4 strategy will burn money. A company at level 4 executing level-2 strategy is leaving value uncaptured. Match the ambition to the maturity, and invest deliberately in raising maturity over 18–36 months.

## A common diagnostic trap

Executives consistently score their own organizations higher than internal practitioners do. When using this framework with an executive client, also collect a parallel score from the ML/data team if possible. The delta is itself diagnostic — large deltas suggest a culture / alignment problem worth surfacing.
