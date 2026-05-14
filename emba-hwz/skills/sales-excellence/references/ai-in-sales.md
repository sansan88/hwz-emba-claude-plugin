# AI in Sales — Pragmatic Applications

The hype cycle is loud. The actual applications producing value today are specific, scoped, and integrated with the sales workflow. This reference is operational, ordered by current realistic value.

## Mature applications (produce real value, available today)

### Lead scoring
Predicting which leads are most likely to convert, based on firmographic, behavioral, and historical data.

**Value:** higher conversion rates by focusing on best leads. Better seller experience by reducing time on weak leads.

**Implementation:** mature; standard feature in major marketing automation and CRM platforms. Requires reasonable lead history data to train.

**Risks:** overfitting to historical patterns; risk of underweighting non-traditional patterns.

### Account intelligence
Automated research on accounts — news, financial signals, hiring patterns, technology stack, leadership changes.

**Value:** sellers walk into meetings with current context. Better personalization.

**Implementation:** mature; multiple vendors (ZoomInfo, Cognism, Apollo, LinkedIn Sales Navigator).

**Risks:** automated personalization can feel hollow; quality of insights varies.

### Conversation intelligence
Recording and analyzing sales calls — talk ratios, keyword detection, deal-stage signals.

**Value:** coaching for managers; pattern detection across the team; deal risk signals.

**Implementation:** mature (Gong, Chorus, Salesloft); requires legal and consent infrastructure.

**Risks:** chilling effect on conversation if used punitively; privacy considerations.

### Sales co-pilot (GenAI-based)
LLM assistants embedded in seller workflow — draft emails, summarize calls, prep for meetings, generate proposals.

**Value:** 20–40% time savings on administrative tasks (varies). Higher quality output for less effort.

**Implementation:** maturing rapidly. Available in major CRM platforms. Microsoft Copilot for Sales, Salesforce Einstein, Gong Engage, etc.

**Risks:** hallucinations in customer-facing output; over-reliance reducing seller skill; data exposure to vendors.

## Useful but mixed-record applications

### Forecasting
ML-based pipeline forecasting, going beyond seller commits.

**Value:** more accurate forecast; visibility into pipeline health.

**Implementation:** mixed. Best when sales data quality is high; struggles in companies with sparse, irregular CRM updates.

**Risks:** false precision; sellers gaming the system once they understand it.

### Next-best-action recommendations
AI suggesting what action to take with a given account/opportunity.

**Value:** consistent application of best practices; useful for newer sellers.

**Implementation:** mixed quality. Best when historical pattern data is rich; weak in companies without enough data.

**Risks:** recommendations that don't match local context; over-mechanizing the seller role.

### Pricing optimization
Dynamic pricing recommendations based on account, deal characteristics, competitive intelligence.

**Value:** margin protection; consistency across the sales team.

**Implementation:** B2B contexts often lack enough data; B2C and high-volume B2B more amenable.

**Risks:** customer perception of inconsistency; mis-pricing relative to value.

## Emerging applications (caution warranted)

### Autonomous outbound
AI agents conducting outbound prospecting — sequencing, responding, qualifying.

**Value claim:** scale beyond what human sellers can do.

**Reality:** technology exists; quality varies enormously. Customer experience often poor. Risk of damaging brand at scale.

**Recommendation:** if used, narrow scope, low stakes, with human oversight. Not for high-value accounts.

### AI-led customer conversations
Voice agents handling customer interactions end-to-end.

**Value claim:** 24/7 availability, scalability.

**Reality:** for narrow, structured interactions (basic questions, scheduling), works. For nuanced sales conversations, fails or produces customer frustration.

**Recommendation:** complement, not replace, human sellers for value-rich relationships.

### Predictive deal scoring with action triggers
AI predicting deal outcomes and automatically triggering interventions.

**Value claim:** save at-risk deals.

**Reality:** technology exists but most companies lack the integration to act on the signals well.

**Recommendation:** start with signal generation; build human-driven action; only automate triggers after pattern validation.

## Implementation principles

### 1. Start from bottlenecks, not from vendor pitches
What is genuinely slow or hard in your sales process? Where would AI augmentation actually move a metric? Start there.

### 2. Integrate into existing workflow
AI tools that require sellers to leave their workflow and use a separate tool are predictably underused. Tools embedded in CRM / email / calendar are used.

### 3. Pilot, measure, iterate
Don't roll out company-wide before knowing it works. Pilot with 2–3 sellers. Measure rigorously. Expand based on evidence.

### 4. Train sellers explicitly
AI tools that aren't trained on are not used. Or worse — used badly. Build the training into adoption.

### 5. Watch the data flow
What data goes into the vendor? What stays? What is used for training their broader models? Important for IP, privacy, competitive sensitivity.

### 6. Resist boil-the-ocean
Pick 1–2 AI applications to do well, not 10 to do poorly. Sequencing is everything.

### 7. Mind the seller experience
AI is a force-multiplier or a force-divider depending on implementation. The good versions make sellers' lives easier; the bad versions add steps. Choose carefully.

## AI in marketing-sales integration

Where AI particularly shines:

- **Account intelligence shared between marketing and sales** — same insight, both functions act on it coherently
- **Content recommendation** — surfacing the right content for the right moment in the customer journey
- **Lead-to-account matching** — connecting inbound interest to existing account context
- **Multi-touch attribution** — sorting out which marketing investments are producing pipeline

These applications require the data foundation work. AI without data is theater.

## How to use this in the workflow

In step 7 of the SKILL.md workflow:

1. Identify the specific bottlenecks in the user's sales motion
2. For each bottleneck, evaluate whether mature AI applications would help
3. Recommend 1–2 specific applications to pilot, not 10
4. Build the measurement around each pilot
5. Resist the urge to layer AI on top of unsystematic process — sequence matters

The companies that get most value from AI in sales are not the ones who bought the most. They are the ones who solved the process and data foundations first, then layered AI selectively.
