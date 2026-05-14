# Building the AI Use Case Portfolio

The single biggest determinant of AI value capture is which use cases the company chooses to pursue. This reference operationalizes use case selection and portfolio design.

## Step 1 — Source candidate use cases

Three productive sourcing channels, in order of yield:

1. **Listen to the operators.** The frontline people who do the work daily know where prediction would help, where they spend time on repetitive judgment, where errors cost real money. Spend a day with them.
2. **Walk the value chain.** Map the business as a sequence of activities. For each, ask: where would cheaper prediction or faster generation move the metric? Watch for high-volume, repeatable, data-rich choke points.
3. **Look at decisions getting made by gut.** Wherever experienced humans currently make decisions by feel — sales lead scoring, pricing, inventory, hiring shortlists — there is often a candidate use case.

What does *not* yield good use cases: starting from technology ("we should use LLMs somewhere"), copying competitor announcements, or running a brainstorming workshop without operator presence.

## Step 2 — Classify each candidate

Davenport & Ronanki's three-category frame, lightly adapted:

| Category | What | Example |
|----------|------|---------|
| **Process automation** | Replace structured human work with a deterministic-or-AI process | Invoice classification, KYC document extraction |
| **Cognitive insight** | Predict, classify, recommend at scale | Churn prediction, demand forecast, fraud detection |
| **Cognitive engagement** | Interact with humans (customers, employees) at scale | Support co-pilot, internal knowledge agent |

Cross-cutting GenAI extension:

| Category | What | Example |
|----------|------|---------|
| **Knowledge work augmentation** | LLM-powered co-pilots embedded in white-collar workflows | Sales prep, research summarization, contract review |
| **Content generation** | Routine media/copy/code production | Marketing variants, code scaffolding, report drafting |

The classification matters because each category has different success conditions, ROI patterns, and risks.

## Step 3 — Score each candidate

Two axes, each scored 1–5:

**Value (1=marginal, 5=transformational)**
- Size of the impacted activity or revenue/cost pool
- Strength of the link from AI capability to business metric
- Defensibility of the value capture (is it commoditized?)

**Feasibility (1=hard, 5=ready)**
- Data availability and quality
- Maturity of the underlying AI capability for this task
- Required change in business process / decision rights
- Regulatory / risk exposure
- Internal sponsor presence and seniority

A useful sanity check: score each candidate honestly against both. Plot on a 2x2 grid. The candidates with high value AND high feasibility belong in the portfolio first. Resist the urge to bias toward high-value, low-feasibility because they sound exciting.

## Step 4 — Compose the portfolio

A balanced portfolio at the start of an AI journey:

- **2–3 quick wins** — high feasibility, modest-to-real value, short time-to-value (3–6 months). Build muscle, generate trust, create reference points.
- **1–2 strategic plays** — high value, harder, 12–18 month horizon. The bets that justify the program.
- **0–1 moonshots** — transformational if they work, plausibly do not. Only if the org has the capacity to absorb failure publicly.

For a more mature organization (already shipped multiple AI products), shift more weight to strategic plays.

The most common composition error: 100% moonshots. They fail to ship in year one, the program loses credibility, the budget is cut before the strategic plays mature. Quick wins keep the program alive long enough for the strategic plays to compound.

## Step 5 — Define the kill criteria

For every use case in the portfolio, define upfront:

- **Path-to-production** — what does "successful" look like as a product or process change, with KPI targets, by when?
- **Kill criteria** — what observation by what date would make us stop?

Without kill criteria, POCs zombie indefinitely. The discipline of writing them down before starting is the discipline that separates capable AI organizations from POC factories.

## The economics filter

Run this check on every use case before adding it to the portfolio:

1. **What is the marginal benefit of getting this right?** Dollar value per correct prediction or generation.
2. **What is the marginal cost of getting it wrong?** Asymmetric error costs change the design — a false positive on fraud is fine, a false negative is not.
3. **What is the volume?** Tiny volumes don't justify ML investment; high volumes do.
4. **What is the alternative?** What is the cost / quality of the human baseline or the simple-rules baseline? If a 20-line SQL rule does 80% of the job, an ML model has to clear a high bar.

Many "AI projects" do not pass this filter. That is fine — better to know early.

## The change-cost filter

The Fountaine/McCarthy/Saleh point. AI value is captured only if a business process or decision actually changes. The filter:

- **Who has to use the output?** Name them.
- **What do they lose?** Status, autonomy, role identity, comfort.
- **Who owns making the change stick?** A senior business sponsor — not the AI team.
- **What is the explicit decision right between the AI output and the human?** Override allowed? Logged?

Use cases without a clear answer to all four are not ready. They become products without users.

## Worked example portfolio (illustrative, for a B2B services firm)

| # | Use case | Category | Value | Feasibility | Notes |
|---|----------|----------|-------|-------------|-------|
| 1 | Proposal drafting co-pilot | Knowledge work | 4 | 4 | Quick win, clear adoption owner |
| 2 | Project profitability prediction | Cognitive insight | 4 | 3 | Strategic; needs data integration |
| 3 | Account intelligence agent | Cognitive engagement | 3 | 4 | Quick win, sales-led |
| 4 | Dynamic resourcing recommendations | Cognitive insight | 5 | 2 | Strategic play; depends on #2 |
| 5 | Autonomous client research agent | Agentic | 5 | 1 | Moonshot; revisit in 12 months |

This is a portfolio. "We will do AI" is not.
