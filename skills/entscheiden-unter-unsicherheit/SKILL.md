---
name: entscheiden-unter-unsicherheit
description: Help executives make high-quality decisions under uncertainty by exposing the cognitive biases and heuristics that are likely distorting the call, and by applying decision architecture techniques to debias the process. Use whenever the user faces a consequential business decision — investment, M&A, market entry, restructuring, key hire, crisis response, plant closure, pivot, go/no-go — especially when information is incomplete, stakes are asymmetric, or strong opinions are forming fast. Also trigger when the user asks about biases (confirmation bias, anchoring, availability, overconfidence, sunk cost, groupthink), pre-mortems, red-teaming, decision quality, "I need to think through this carefully," forecasting, or the Kahneman / Beshears / Gino body of work. Even when the user does not explicitly mention biases, if the situation is a non-trivial decision under uncertainty, use this skill.
---

# Entscheiden unter Unsicherheit — Better Decisions in High-Stakes Conditions

This skill operationalizes EMBA Block 1 Tag 3 (Julian Fieres, HWZ). The discipline at its center: executives do not make decisions in the conditions textbooks describe. They make them under time pressure, with partial information, while their own brains apply shortcuts that were optimized for ancestral environments, not for capital allocation in volatile markets.

The good news from forty years of behavioral decision research: biases are not random. They are predictable. Once predictable, they are debiasable. The job of executive decision-making is therefore not to eliminate System-1 thinking (Kahneman) — that is impossible — but to design the *decision process* so the predictable distortions are caught and corrected before the decision is made.

## When to lean on this skill

Use it when the user is facing a non-trivial decision: capital allocation, M&A, market entry/exit, plant or product line closure, senior hire or fire, crisis triage, pivot vs. persevere, restructuring, big bet on a technology trend. Also use when the user is leading a team through a decision and wants the *process* to be high quality, not just the outcome.

Do not use it for routine operational choices (low stakes, reversible, repeatable) — those are better handled by SOPs and judgment, not by heavy decision architecture.

## Mental model: separate decision quality from outcome quality

A high-quality decision can produce a bad outcome (the world is uncertain). A low-quality decision can produce a good outcome (luck). Hindsight collapses both into the same judgment. The single most useful executive habit: **judge decisions by the process and information available when the call was made, not by what happened afterward**.

Build this distinction into every output of this skill. The user should leave with a defensible decision *process*, not just a guess at the right answer.

## Workflow

### 1. Frame the decision

Run the framing checks before any analysis. The frame is the hidden lever — a badly framed decision cannot be rescued by good analysis.

- **What exactly is being decided?** Force a one-sentence statement that names the action, the decision-maker, and the deadline. If you cannot write it, the decision is not yet ready to be made — it is still a problem.
- **What is the unit of analysis?** Project, product, business unit, company, ecosystem? Mismatches here produce the wrong answer to the right question.
- **Reversibility?** Type 1 (one-way doors, hard to reverse, e.g., a Bezos-style irreversible decision) vs Type 2 (two-way doors, cheap to reverse). Apply rigor proportional to reversibility, not to perceived importance.
- **What is the no-decision baseline?** Doing nothing is a decision too — name what happens if no action is taken. Often this exposes that "decisions" are really just chooser-anxiety.

Use `templates/decision-frame-canvas.md` to capture.

### 2. Surface the likely biases

Read `references/biases-heuristics-catalog.md` for the catalog. Then identify which biases are most likely active in this specific decision. Patterns:

- **Confirmation bias** — strong when a preferred answer has already emerged in the team.
- **Overconfidence / planning fallacy** — strong when the team has done similar work before and feels expert.
- **Anchoring** — strong when a salient number (a previous deal, a target, a competitor's price) has been mentioned.
- **Availability** — strong when a recent salient event (a competitor's failure, a near-miss) is shaping risk perception.
- **Sunk cost / escalation of commitment** — strong when the team has already invested significantly.
- **Loss aversion / status quo** — strong when the decision involves giving something up to gain something potentially larger.
- **Groupthink** — strong when the team is cohesive, senior, and under time pressure.

Make the biases explicit in the deliverable — not as accusation, but as predictable distortions to design around.

### 3. Apply decision architecture

Beshears & Gino's (2015) "Leaders as Decision Architects" reframes executive work: leaders should not just make decisions, they should shape the contexts in which decisions get made. Reference: `references/decision-architecture.md`.

Pick from this toolkit, sized to the decision:

- **Pre-mortem** — Imagine the decision has been made and failed badly. Walk back: what went wrong? Surfaces hidden risks that the standard analysis hides.
- **Red team / blue team** — Assign one team to make the strongest case against the proposed action. Strongly recommended for any large irreversible commitment.
- **Reference-class forecasting** — Build a base rate from comparable past situations, then adjust. Combats inside-view overconfidence.
- **Independent estimates before discussion** — Each decision-maker writes down their assessment before the meeting. Prevents anchoring and cascade effects.
- **Devil's advocate (formal)** — A named, rotating role with explicit permission to disagree. Different from genuine dissent but useful when the culture suppresses disagreement.
- **Dialectic inquiry** — Force two well-developed alternatives, not options paraded only to validate a preferred choice.
- **Decision journal** — Record the decision, the reasoning, the expected outcomes. Enables genuine after-action learning, not hindsight rationalization.

### 4. Build the decision artifact

The output of a serious decision process should be a single document with the structure in `templates/decision-document-template.md`. The discipline: if you cannot articulate the decision in a 2-page document, you have not made it yet.

Core sections:
- Decision in one sentence
- The decision-maker(s) and the deadline
- Frame and unit of analysis
- Options seriously considered (not just the preferred one)
- Key assumptions, with explicit confidence levels
- The evidence base, including dissenting views
- The pre-mortem results
- The decision and its rationale
- The reversibility class and the trigger conditions for revisiting
- The first concrete actions

### 5. Communicate the decision

Decisions die in the communication step more often than in the deliberation step. Use `templates/decision-communication-template.md`. The principles:

- Lead with the decision and the why, not with the context.
- Name what was considered and rejected, so the team understands the reasoning was real.
- Name what could change the decision — this preserves credibility when the world shifts.
- Make ownership explicit — who owns what next.
- Acknowledge what is hard or uncertain. Pretending certainty corrodes trust.

### 6. Design the learning loop

For consequential decisions, schedule the review now. Without this step, organizations cannot tell good decisions from lucky outcomes (or bad decisions from unlucky outcomes), and so they cannot get better.

- 30/60/90 day check-ins on the key assumptions
- Trigger conditions that force re-evaluation
- A decision journal entry written *before* outcomes are known

Use `scripts/decision_journal.py` to scaffold a journal entry from a YAML spec.

## Output style

The decisions this skill is invoked for are weighty. The output should feel like the work of a careful adult, not a deck. Plain language. Honest about uncertainty. Specific about what is being claimed and on what evidence.

Avoid:
- Confident-sounding hedge phrases ("clearly the right call given X" — clearly is doing too much work)
- Lists of options where one is obviously cherry-picked to win
- Quantification that fakes precision the data does not support

Embrace:
- "I estimate, with low confidence, that..."
- "The strongest case against this decision is..."
- "If [signal] is observed by [date], we will revisit."

## Pitfalls to avoid

- **Mistaking outcome quality for decision quality** — see mental model above. Drill it into every output.
- **Process theater** — running a pre-mortem because it is on the checklist, while the boss has clearly already decided. The architecture has to be honored, not just executed.
- **Bias-spotting as performance** — listing biases in the deliverable without changing the process. The point is to *do something differently*, not to demonstrate familiarity with Kahneman.
- **False consensus** — silent dissent is not agreement. Build mechanisms to surface what people are not saying.
- **Quantifying away the uncertainty** — building a 12-tab model for a decision whose key variables are genuinely unknowable. False precision is worse than honest ranges.

## Key sources

- Beshears, J., & Gino, F. (2015). *Leaders as Decision Architects.* Harvard Business Review.
- Kahneman, D. (2011). *Thinking, Fast and Slow.*
- Klein, G. (2007). *Performing a Project Premortem.* HBR.
- Tetlock, P. (2015). *Superforecasting.* (Reference-class thinking, calibration, base rates.)
- Casali, G. L., & Perano, M. (2021). *Forty years of research on factors influencing ethical decision making.* J. Bus. Res. 132.
- Janis, I. (1972). *Victims of Groupthink.* Classic on cohesive-team failures.

The reference files inside this skill apply these sources to executive practice.
