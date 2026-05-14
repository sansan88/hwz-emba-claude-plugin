---
name: sales-excellence
description: Help leaders build sales excellence — the systematic, data-driven, AI-augmented approach to sales and CRM that increases customer value (CLV). Covers customer-oriented company design (Kundenorientierung), sales process maturity, marketing/sales integration, CRM strategy, customer data management, and applied AI in sales. Use whenever the user is working on sales strategy, sales transformation, sales productivity, CRM implementation, marketing-sales alignment, customer experience, customer data, account-based marketing, sales tech stack, or AI in sales/marketing. Also trigger when the user mentions Staudacher, Pufahl, Kundenorientierung, Customer Lifetime Value, CustomersX, or has a sales productivity problem. Even without these terms — if the substance is "we need to sell better, more systematically," use this skill.
---

# Sales Excellence — The Forgotten Competence

This skill operationalizes EMBA Block 6 Tag 2 (Prof. Jörg Staudacher, HWZ / CustomersX). The thesis: while marketing has been continuously upgraded through digital, content, automation, and AI, sales as a *systematic discipline* has often been left to wing-it. The result is the well-documented productivity gap in B2B sales — and the equally well-documented under-utilization of CRM, AI, and customer data systems that companies have already invested in.

Sales excellence is not about better sellers (though they help). It is about a *system* — customer-oriented company design, systematic sales processes, marketing-sales integration, customer data infrastructure, and AI augmentation — operated at maturity.

## When to lean on this skill

Use it when the user is: building or rebuilding a sales organization; assessing sales maturity; integrating marketing and sales; deciding on CRM and sales tech investment; setting up account-based marketing or key account programs; designing sales compensation; bringing AI into the sales workflow; building customer data infrastructure; or running a customer-experience strategy review.

Do not use it for: pure product marketing strategy, brand strategy alone (use `purpose-driven-companies`), or pure sales coaching (different toolkit).

## Mental model: customer value as the integrating metric

The integrating idea: **everything in sales, marketing, and CRM should serve increasing customer value over time.** Concretely, this means:

- **Acquisition** — winning the right customers (not just any customer)
- **Onboarding** — making the new customer successful early
- **Expansion** — growing within the account where the value justifies it
- **Retention** — keeping the customers who deliver mutual value
- **Advocacy** — turning best customers into channels themselves

Customer Lifetime Value (CLV) is the metric that integrates these. A sales-excellent company optimizes CLV at portfolio level, not just deals at point-in-time level.

## Workflow

### 1. Assess sales excellence maturity

Read `references/sales-excellence-maturity.md`. The Staudacher / CustomersX framework assesses on five dimensions:

1. **Customer-oriented company design** — is the organization actually built around customers, or around products / functions?
2. **Sales process systematization** — is there a defined, instrumented, improvable sales process?
3. **Marketing-sales integration** — do the two functions operate as one customer-facing system?
4. **Customer data management** — is data captured, integrated, usable for decisions?
5. **Sales tech and AI maturity** — are the tools actually used, producing value, or shelfware?

Use `templates/sales-excellence-assessment.md`. Most companies score lower than they think on dimensions 2 and 4, regardless of CRM software investment.

### 2. Diagnose customer-orientation

Read `references/kundenorientierung.md`. The Staudacher (2021) thesis: most companies declare themselves customer-oriented while operating in fundamentally product-or-function-oriented ways. The gap shows in:

- Decision rights aligned to internal functions, not customer outcomes
- Metrics measuring activity, not customer success
- Compensation rewarding short-term revenue, not customer health
- Organizational structure that fragments the customer experience

A genuinely customer-oriented company has aligned all four. Most have aligned none.

### 3. Map the customer journey end-to-end

Use `templates/customer-journey-map.md`. Across all touchpoints:

- Awareness → consideration → purchase → onboarding → use → expansion → renewal → advocacy
- Which department owns each stage?
- Where are the handoff frictions?
- Where does customer experience degrade?
- Where is data captured, where lost?

A common finding: 7+ different teams touch a single customer relationship; no one owns the relationship end-to-end.

### 4. Systematize the sales process

Read `references/sales-process-design.md`. A systematic sales process is:

- **Defined** — explicit stages with defined activities and outputs
- **Instrumented** — measurable progression through stages
- **Trained** — sellers know it, use it, can improve at it
- **Improvable** — performance data feeds back to refine the process

Pufahl's *Sales Performance Management* provides the underlying framework. Companies that systematize see meaningful productivity gains (typically 15–30% within 18 months).

### 5. Integrate marketing and sales

Read `references/marketing-sales-integration.md`. The integration is not "more meetings between marketing and sales." It is structural:

- **Shared customer definition** — who is the target customer; precise; quantified
- **Shared funnel ownership** — both teams own conversion through the full funnel, not handoff at MQL
- **Shared metrics** — both compensated partly on shared customer outcomes
- **Shared data** — same customer view, same definitions
- **Shared cadence** — joint planning, joint review, joint course-correction

Account-based marketing (ABM) is the most developed form of this integration for B2B.

### 6. Build the customer data foundation

Read `references/customer-data-management.md`. The Staudacher diagnosis: 5% of customers use the chatbot the company bought. The problem is not chatbots — it is the customer data that should be informing the chatbot is fragmented, stale, or incomplete.

A working data foundation:

- **Unified customer profile** — single view across all touchpoints
- **Behavioral data** — what the customer actually does, not just demographics
- **Value data** — what the customer is worth, with confidence levels
- **Quality** — accuracy, completeness, freshness measured
- **Governance** — who owns what, how data is updated, privacy compliance

CRM software is the substrate but not the strategy.

### 7. Apply AI in sales — pragmatically

Read `references/ai-in-sales.md`. Useful applications, ordered by current realistic value:

- **Lead scoring** (mature) — predicting which leads to prioritize
- **Sales co-pilot** (emerging, real value) — LLM assistants for prep, follow-up, deal coaching
- **Account intelligence** (mature) — automated research on accounts
- **Forecasting** (mixed) — ML-based pipeline forecasting; useful but not magic
- **Conversation intelligence** (mature) — analysis of sales calls
- **Autonomous outbound** (emerging, risky) — be careful

Match AI applications to specific bottlenecks identified in the maturity assessment, not to vendor pitches.

### 8. Compose the sales excellence roadmap

Use `templates/sales-excellence-roadmap.md`. A 12–24 month arc with sequenced moves across the five dimensions, anchored on the binding constraint surfaced in the maturity assessment.

## Output style

Concrete, commercial, with numbers when available. Sales is operations — the strategy must translate to specific changes in process, tools, compensation, and behavior. Avoid abstract advice.

## Pitfalls to avoid

- **CRM = sales excellence.** Buying Salesforce is not buying excellence. CRM is plumbing; without process, data, and behavior, it is shelfware.
- **AI tourism.** Buying AI tools without diagnosing where they would actually solve a bottleneck. Most stays unused.
- **Marketing-sales blame ping-pong.** Each function blames the other for the conversion gap. Almost always structural.
- **Compensation that contradicts strategy.** Strategy says "customer value over deal value"; comp pays purely on deal value. Predictable behavior.
- **Vanity activity metrics.** Calls made, emails sent, meetings booked — easy to inflate, weakly predictive. Outcome metrics matter.
- **Data project boil-the-ocean.** "First we'll build the customer 360, then we'll improve sales." Often a multi-year delay with no business value. Start with the use case, build the data foundation as a byproduct.
- **Ignoring the seller experience.** Sellers under bad tooling, bad data, and bad incentives produce predictable mediocrity. Their experience is part of the system.

## Key sources

- Staudacher, J. — body of work on Kundenorientierung, Sales Excellence, CRM (CustomersX).
- Staudacher, S. (2021). *Kundenorientierung: Grundlagen, Modelle und Best Practices.* SpringerGabler.
- Hippner et al. (2011). *Grundlagen des CRM: Konzepte und Gestaltung.* SpringerGabler.
- Pufahl, M. (2018). *Sales Performance Management.* SpringerGabler.
- Sales Excellence Studie (2022).
- Staudacher / Holland (2019). *Die Zukunft des CRM liegt in der Kundenanalyse.* Swiss Marketing Review.

Reference files inside this skill apply these to executive practice.
