# Customer Data Management

Staudacher's diagnosis: companies invest heavily in chatbots and AI tools, but only 5% of customers use them — because the customer data those tools need is fragmented, stale, or incomplete. The problem is rarely the technology; it is the customer data foundation.

## What customer data is for

Customer data exists to enable customer-relevant decisions:

- Which prospects to prioritize
- What to say to a specific customer at a specific moment
- Which accounts to invest in for expansion
- Which customers are at risk of churn
- What to develop next based on actual customer behavior
- What pricing and packaging to offer

Each of these requires specific data, accurately captured, integrated, and usable. Most companies have some of each; few have all in usable form.

## The unified customer profile

A working customer profile includes:

### Firmographic / demographic
Who they are. For B2B: company size, industry, geography, function. For B2C: standard demographics where relevant.

### Behavioral
What they do. Touchpoints, content consumed, support interactions, product usage (for SaaS / digital).

### Transactional
What they have bought. Order history, products, services, channels.

### Value
What they are worth. Lifetime value estimate, profitability, expansion potential, advocacy strength.

### Relationship
Who they know. Champions, blockers, contacts mapped, influence diagrammed (for B2B with buying committees).

### Sentiment
How they feel. NPS, support sentiment, recent interactions, voice-of-customer.

The discipline: not every data type is needed for every customer. Match data depth to customer value.

## Quality dimensions

For each data point:

- **Accuracy** — does it match reality?
- **Completeness** — are the fields filled?
- **Freshness** — when was it last updated?
- **Uniqueness** — are duplicate customer records reconciled?
- **Consistency** — same definition across systems?
- **Usable for decisions** — analyzable, comparable, queryable?

Most CRMs have 30–50% of fields blank, 20%+ of records duplicated, and stale data with no freshness markers. The result: decisions made on incomplete pictures, often defaulting to gut.

## The systems landscape

A typical B2B customer data landscape:

- **CRM** — sales pipeline, account information
- **Marketing automation** — email behavior, web behavior, content consumption
- **Customer success platform** — health scores, usage, renewals
- **Support / service** — tickets, satisfaction
- **ERP / billing** — orders, invoices, payments
- **Product analytics** — feature usage, engagement (SaaS)
- **Data warehouse / lake** — analytical layer
- **Customer Data Platform (CDP)** — unification layer for personalization

The number of systems is rarely the problem; the integration is. Without unification, each system operates on a partial view.

## CDP vs. CRM vs. data warehouse

- **CRM** is the system of record for sales relationships and pipeline
- **Customer Data Platform (CDP)** unifies customer profiles across systems for activation (marketing, personalization)
- **Data warehouse / lake** is the analytical layer

Many companies overinvest in CRM expecting it to do CDP work, then complain it doesn't. Each has its role.

## The data governance layer

For customer data to be a strategic capability rather than chaos:

- **Owner of the customer master data** — usually a senior cross-functional role
- **Data definitions documented** — what a "customer" is, what a "lead" is, what "active" means
- **Quality SLAs** — minimum quality thresholds for key fields, monitored
- **Change management** — how new fields, definitions, or systems get added
- **Privacy and compliance** — GDPR / FADP / CCPA aligned, retention policies enforced
- **Access controls** — who can see and change what

Governance is unglamorous but essential. Without it, data quality degrades faster than it improves.

## The privacy and trust dimension

Customer data carries real privacy obligations:

- Lawful basis for processing (consent, contract, legitimate interest)
- Transparency to customers about what is collected
- Data subject rights (access, correction, deletion)
- Cross-border transfer compliance
- Retention limits

Companies that treat customer data as a free resource will face increasing legal and reputational exposure. Those that treat it as a stewardship build trust that compounds.

## The "where to start" problem

Most companies start the data project too broad. "First we'll build the customer 360, then we'll do everything else." Multi-year delay, no business value in the interim.

Better: pick a specific use case, build the data foundation needed for it, expand from there. Examples of good starter use cases:

- **Lead scoring** — needs firmographic, behavioral, and historical conversion data
- **Churn prediction** — needs usage, satisfaction, support, and value data
- **Account expansion targeting** — needs relationship, behavioral, and value data
- **Personalization in onboarding** — needs profile, behavioral, and product data

Each builds a slice of the data foundation while producing business value.

## How to use this in the workflow

In step 6 of the SKILL.md workflow:

1. Assess current data state honestly — quality, coverage, integration, governance
2. Identify the 1–2 specific use cases where better data would most move the business
3. Design the data foundation around those use cases, not in the abstract
4. Build governance from the start, not as an afterthought
5. Measure and improve data quality systematically

CRM ROI is gated on data quality. Without data work, the tool is a graveyard.
