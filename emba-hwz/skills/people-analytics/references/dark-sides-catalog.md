# The Dark Sides of People Analytics

Operationalized from Giermindl et al. (2022). A catalog of known harms for use in pre-deployment audits and ongoing program review.

The point of the catalog is not to scare leaders away from People Analytics. It is to make the harms visible so they can be mitigated before they accumulate.

## Privacy violation
**What happens:** Data is collected or combined in ways that exceed what employees reasonably expect or have consented to.

**Diagnostic question:** If an employee read the full list of what is collected about them, would they be surprised? If yes, that surprise is a measure of the gap between the implicit social contract and the actual practice.

**Mitigation:** Plain-language transparency disclosures. Sunset clauses on data retention. Data minimization — collect only what is needed for the named purpose, retain only as long as needed.

## Dehumanization
**What happens:** People reduced to scores or categories. The unique, situated, contextual nature of human work flattened into comparable metrics.

**Diagnostic question:** Could a sensitive manager describe an individual employee in richer terms than the metrics allow? If the metrics replace, rather than supplement, that richer description, dehumanization is the result.

**Mitigation:** Reserve algorithmic outputs as inputs to human judgment, not substitutes. Forbid individual rankings derived purely from metrics. Train managers to use data as one input among many.

## Algorithmic bias
**What happens:** Models trained on historical decision patterns inherit and amplify the biases in those patterns. Hiring, promotion, performance review, attrition prediction — all vulnerable.

**Diagnostic question:** Has any model in the program been audited for disparate impact on protected groups? If not, assume bias is present until proven otherwise.

**Mitigation:** Independent bias audits. Counterfactual testing. Data lineage transparency. Explicit fairness criteria documented and reviewed.

## Gaming
**What happens:** Workers optimize the measurement rather than the underlying value. Goodhart's Law in action: when a measure becomes a target, it ceases to be a good measure.

**Diagnostic question:** Are there cheap workarounds that game the metric? If yes, they will be found.

**Mitigation:** Multiple uncorrelated metrics for the same outcome. Periodic refresh of metrics so adaptation cannot stabilize. Triangulation with qualitative signals.

## Chilling effect
**What happens:** Workers self-censor or behave defensively because they know they are being measured. Risk-taking and dissent decline. The measurement itself produces conformity.

**Diagnostic question:** Are dissenting views still surfaced in this team? Is risk-taking still happening? If both declining over time, suspect chilling.

**Mitigation:** Protect channels for anonymous feedback. Symmetric measurement (leaders visible too). Explicit "off-the-record" zones for exploratory work. Reward generative dissent visibly.

## Role narrowing
**What happens:** Workers focus on what is measured at the expense of work that matters but is not measured. Mentoring, knowledge-sharing, customer-relationship investments, exploratory work — first casualties.

**Diagnostic question:** What work do good employees do that does not show up in any metric? Is that work decreasing?

**Mitigation:** Periodically retire metrics that are no longer pulling their weight. Explicit "unmeasured but important" line items in performance conversations. Promotion and reward criteria that include unmeasured contributions.

## Attribution errors
**What happens:** Correlations are read as causation. "Employees who attend Slack at high frequency have higher engagement scores — let's encourage more Slack attendance." The arrow may go either way, or both may be driven by a third variable.

**Diagnostic question:** Has the team distinguished correlation from causation in the major analytical claims? Has anyone made interventions based on findings without testing the causal hypothesis?

**Mitigation:** Train analysts on causal inference. Where possible, run small randomized experiments. Caveat the language in dashboards — "associated with," not "causes."

## Erosion of psychological contract
**What happens:** The implicit understanding of what the employer owes the employee (and vice versa) shifts. Workers feel watched, not trusted. The cost shows up in attrition, disengagement, and downstream legal action.

**Diagnostic question:** Has employee trust in the company changed since the program was introduced? Are senior people leaving?

**Mitigation:** This is the integration of all the others. The cumulative experience of how data is collected and used determines whether the contract is honored or eroded. Audit trust signals (eNPS, free-text comments, exit interviews) for shifts.

## Surveillance creep
**What happens:** A use case is approved for purpose A, then quietly extended to purpose B. Each step is small; the cumulative shift is large.

**Diagnostic question:** Has any data source been used for purposes beyond what was originally communicated to employees? If yes, the social contract has been silently rewritten.

**Mitigation:** Strict purpose limitation. New use of existing data requires a fresh approval and a fresh communication. Default sunset clauses.

## Vendor lock-in to ethical posture
**What happens:** The company adopts a vendor whose product design encodes a particular ethical stance. The vendor's defaults become the company's practice.

**Diagnostic question:** What does the vendor's product enable by default? What does it forbid? Are those defaults what we would choose if we were designing the system ourselves?

**Mitigation:** Vendor evaluation against a clear ethical specification, not just feature lists. Insist on configurability of ethically loaded defaults.

## How to use this catalog in the workflow

For each significant use case in the program, run through this list. For each harm:

- **Likelihood** in this use case (low / medium / high)
- **Severity** if it materializes (low / medium / high)
- **Current mitigation** in place
- **Owner** for the mitigation

Use cases with high-likelihood × high-severity harms and no mitigation are not ready to deploy. Document and decide.
