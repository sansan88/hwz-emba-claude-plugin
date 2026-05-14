---
name: people-analytics
description: Help leaders design, evaluate, or fix People Analytics programs — using employee data and AI to measure work, performance, collaboration, and engagement — without crossing into surveillance, eroding trust, or violating worker rights. Use whenever the user is working on a People Analytics roadmap, HR data strategy, workforce analytics, sentiment monitoring, productivity measurement (Viva/Workday/SAP-Successfactors style), engagement scoring, attrition prediction, organizational network analysis, or "should we measure X about employees?". Also trigger when the user mentions datafication, employee monitoring, trust in HR analytics, the management model / Sozialpartnerschaft, GDPR / Swiss FADP implications for HR data, Schafheitle / Weibel / Giermindl, or has read concerning news about workplace surveillance. Even when the user does not name "People Analytics" — if the substance is using data about employees to drive management decisions, use this skill.
---

# People Analytics — Evidence-Based Management Without the Surveillance Trap

This skill operationalizes EMBA Block 2 Tag 2 (Ralf Büchsenschuss & Prof. Simon Schafheitle, HWZ — site visit at Microsoft Zürich). The thesis: People Analytics is now technologically trivial to deploy, but strategically and ethically nontrivial. The same instrumentation that produces "evidence-based management" can produce surveillance capitalism inside the firm. The work is to design programs that capture the value without the harm.

The integrating frame is Schafheitle, Weibel, and colleagues' "bad / good / greater good" typology of datafication control architectures. Different choices in *how* people data is collected and used produce dramatically different outcomes for trust, performance, and legitimacy.

## When to lean on this skill

Use it when the user is: building a People Analytics function, evaluating a vendor (Viva Glint, Workday, Visier, Microsoft Workplace Analytics, ChurnZero-style attrition predictors), designing dashboards for senior leaders, considering deploying productivity / collaboration measurement, deciding what HR data to collect or retain, weighing AI/GenAI use in talent decisions, or trying to repair a People Analytics program that has eroded trust.

Do not use it for: pure HRIS implementation, payroll, or transactional HR ops. Those are different problems.

## Mental model: three questions, always

For every People Analytics use case, run these three before any technical design:

1. **What does this measurement *control for*?** Every metric implicitly defines what "good" looks like. Whose definition? Time-at-keyboard rewards presence; meaningful-output requires harder measurement. Choose deliberately.
2. **What does this measurement *cost*?** Not just money — what does the act of measuring change? Hawthorne effects, gaming, trust erosion, narrowing of behavior toward what is measured. The cost of measurement is often borne by the workforce, the benefit by management.
3. **Who has voice over this measurement?** If only management decides what to measure and how to use it, the system tilts toward control. If employees and worker representatives have meaningful voice, it tilts toward shared understanding.

## Workflow

### 1. Locate the program on the bad / good / greater good spectrum

Read `references/datafication-typology.md`. Schafheitle & Weibel distinguish three archetypal datafication control architectures:

- **The "bad"** — datafication for surveillance and control. Maximizes management visibility, minimizes worker autonomy. Produces compliance, distrust, gaming, eventually attrition of the best people.
- **The "good"** — datafication for transparency and evidence. Replaces gut decisions with data. Still implicitly hierarchical — management still owns the data and the decisions — but data is used to inform, not to monitor individuals.
- **The "greater good"** — datafication for shared understanding. Data is collected with worker voice, used to support both individual and collective decisions, and crucially used *symmetrically* — leadership behavior is also visible in the data, not just worker behavior.

Most real programs sit between these. Naming where this user's program actually sits is the most useful diagnostic move.

### 2. Audit the program against the dark-sides catalog

Read `references/dark-sides-catalog.md` (Giermindl et al. 2022). The catalog of known harms includes: privacy violation, dehumanization, algorithmic bias, gaming, the chilling effect, role narrowing, attribution errors (mistaking correlations for causes), and erosion of psychological contract.

For each significant use case in the program, ask: which of these harms is plausible? What mitigations are in place? If the harms are not explicitly addressed, the program is operating on hope.

### 3. Connect to the management model

People Analytics does not live in a vacuum. It lives in a management model — the implicit social contract between management and workforce. The course's key insight (Schafheitle): the right People Analytics design depends on the management model the company is trying to enact.

- **In a high-control, hierarchical model:** People Analytics naturally amplifies control. The system is internally consistent but limits the workforce engagement upside.
- **In a high-trust, partnership-based model (Swiss Sozialpartnerschaft, Mitsprache, co-determination):** People Analytics has to be designed with voice and symmetry, or it ruptures the management model.
- **In a hybrid model:** mismatch produces the most damaging outcomes — people see what is happening regardless of what is said.

Force the user to articulate the management model explicitly before designing the analytics.

### 4. Choose use cases against the trust filter

Use the Trust Filter in `templates/trust-filter-canvas.md`. For each candidate use case, the filter asks:

- Is the measurement transparent to the people being measured?
- Do the people being measured have voice in how it is used?
- Is the data used at the individual level, or only aggregated?
- Is the data symmetric — i.e., are leaders measured by the same instruments?
- What is the maximum harmful use of this data if intent shifts?

Use cases that fail the filter should be re-scoped or dropped. The work of People Analytics is not to maximize what can be measured; it is to maximize useful insight at acceptable cost.

### 5. Design governance and consent

Read `references/governance-and-rights.md`. People Analytics intersects Swiss FADP (revFADP), GDPR for cross-border companies, the EU AI Act high-risk classification for HR-related AI, and works council rights where applicable.

For each use case, document:

- The legal basis for processing (consent, contract, legitimate interest)
- The retention period
- The decision-making logic and whether it is automated
- The transparency commitments to employees
- The escalation path for complaints
- The audit and review cadence

### 6. Build the operating model

Use `templates/people-analytics-operating-model.md`. The minimum components:

- **Charter:** what we measure, what we do not measure, and why
- **Data council:** cross-functional (HR, IT, legal, security, employee representatives) reviewing new use cases
- **Transparency surface:** what employees can see about themselves and the program
- **Audit cadence:** annual review of the program by an independent function

### 7. Build the symmetry

The single distinguishing design feature of "greater good" programs is symmetry — leadership behavior visible in the same instruments as worker behavior. Practical examples:

- Manager response time to employee questions tracked alongside employee productivity
- Span-of-control quality metrics for executives, not just IC output metrics for staff
- Engagement and turnover metrics reported to leadership *about their leadership* with the same granularity as about their teams

Symmetry shifts the program from surveillance to shared understanding. Without it, "evidence-based" becomes a euphemism.

## Output style

Honest, technically literate, and morally awake. Avoid both the techno-utopian framing ("data-driven culture") and the techno-paranoid framing ("surveillance state"). Each use case carries a specific risk profile and a specific value pool; the work is to size them honestly.

## Pitfalls to avoid

- **Counting what can be counted.** Time online, meetings attended, messages sent — easy to measure, weak as indicators of value. Default toward easy metrics produces meeting theater and Slack performance.
- **Hidden value judgments.** Every metric encodes a definition of "good work." Make these explicit; do not pretend the data is value-neutral.
- **Algorithmic management at the individual level.** Predicting which employees will quit, who is "disengaged," who is a "flight risk" — the most legally risky and trust-corrosive uses, often the lowest in actual decision quality.
- **Vendor-told stories.** Vendor case studies are usually unfalsifiable. Demand specifics about your context, your data, your management model.
- **Asymmetric measurement.** Measuring workers but not managers signals what the program is really about.
- **"It's just data."** Data is never just data. It is collected for purposes, interpreted through frames, used in consequential decisions. Treating it as neutral is itself a value judgment.

## Key sources

- Giermindl, L. M., Strich, F., Christ, O., Leicht-Deobald, U., & Redzepi, A. (2022). *The dark sides of people analytics: Reviewing the perils for organisations and employees.* European Journal of Information Systems, 31(3).
- Schafheitle, S., Weibel, A., Ebert, I., Kasper, G., Schank, C., & Leicht-Deobald, U. (2020). *No stone left unturned? Toward a framework for the impact of datafication technologies on organizational control.* Academy of Management Discoveries, 6(3). — Especially Figures 3 & 4.
- Weibel, A., Rickert, A., & Schafheitle, S. D. (2024). *Vertrauen aktiv managen.* Personalmagazin.
- Schafheitle, S. & Weibel, A. (in press). *The "bad", the "good", the "greater good": Delineating datafication control system architectures.*

The reference files inside this skill apply these to executive practice.
