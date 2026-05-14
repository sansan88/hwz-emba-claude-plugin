---
name: zukunftsforschung
description: Apply futures research (Zukunftsforschung) and scenario thinking to strategic business questions. Use whenever the user is working on long-horizon strategy, scenario planning, megatrend analysis, "what if 2030/2035/2040" questions, future-proofing a business model, building an inspirational vision, dealing with VUCA/uncertainty at the strategic level, or wants to move from fear-based to hope-based future framing. Also trigger when the user mentions Andreas Krafft, Hoffnungsbarometer, swissfuture, alternative futures, possible/probable/preferable futures, or wants to run a futures workshop. Even if the user does not say "Zukunftsforschung" explicitly — if the task is about exploring multiple long-term futures rather than a single forecast, use this skill.
---

# Zukunftsforschung — Strategic Futures Thinking

This skill operationalizes the content of EMBA Block 1 Tag 1 (Dr. Andreas Krafft, HWZ): the Swiss school of futures research with its emphasis on the psychology of future thinking, megatrends, and the deliberate cultivation of hope-based agency in conditions of deep uncertainty.

The core thesis: in a VUCA world, **how leaders look at the future** (with hope, fear, or indifference) determines how the organization thinks and acts today. Futures work is therefore both an analytical and a psychological discipline.

## When to lean on this skill

Use it when the user asks about: 2030/2035/2040 strategy, scenario planning, megatrend analysis, future-proofing a portfolio or business model, board-level "what should we worry about?" questions, vision workshops, transformation kick-offs, change-readiness, leading through fear, or building hopeful narratives for a workforce. It is the wrong tool for short-cycle forecasting, financial projections, or single-point predictions — those need different methods.

## Mental model: the three layers of futures work

Always work all three layers — skipping any of them is the most common failure mode of corporate scenario exercises.

1. **Analytical layer** — Megatrends, weak signals, drivers of change. The "outside-in" view of what could happen.
2. **Possible / probable / preferable layer** — Out of the cone of possibilities, which futures are merely possible, which are probable, and which are preferable? This is the bridge between analysis and intention.
3. **Psychological layer** — The Hoffnungsbarometer perspective: how the team feels about the future shapes what they will do. Fear narrows attention, hope expands it. Without working this layer, even a brilliant scenario set won't move people.

When delivering an output, make this three-layer logic visible to the user — it is what distinguishes Zukunftsforschung from generic strategy consulting.

## Workflow

Follow this sequence; adapt depth to the user's actual ask.

### 1. Frame the futures question

Help the user state a sharp, time-bounded question. Bad: "What is the future of our company?" Good: "Which futures should our B2B SaaS product strategy be robust against in the 7-year horizon to 2032?"

Probe for: time horizon, geography, decision the work needs to inform, the unit of analysis (industry, company, product, role), and existing assumptions to surface. Without a sharp question, the work drifts.

### 2. Build the megatrend / driver landscape

Identify the relevant trends. Read `references/megatrends.md` for the swissfuture / Roos (2018) catalog and the STEEP+L structure (Social, Technological, Economic, Environmental, Political, Legal). For each trend, capture:

- Trajectory and uncertainty
- Time-to-impact for the user's context
- Whether it is a **driver** (causal force) or a **symptom**

The deliverable here is a trend map, not a list. Push the user to cluster and to identify which trends amplify or dampen each other.

### 3. Construct alternative futures

Use one of the two construction methods documented in `references/szenario-methoden.md`:

- **2x2 axes-of-uncertainty matrix** when there are two clearly dominant uncertainties
- **Archetype scenarios** (growth, collapse, discipline, transformation — Dator's four) when no two uncertainties dominate

Generate **3–4 scenarios**, each with: a name, a one-paragraph narrative, the key signals that would tell you this future is materializing, and the implications for the user's decision.

Avoid the most common trap: producing one "good" scenario and one "bad" one with two filler scenarios. Each scenario must be internally consistent, plausible, and meaningfully different in its strategic implications.

### 4. Apply the psychological layer

This is the step most strategy work skips. Read `references/psychologie-zukunftsdenken.md`.

For each scenario, surface:

- What does it activate in the team? Hope, fear, indifference, defensive optimism?
- Where is hopelessness lurking that will block action?
- Which scenario, if it dominates the team's imagination, will distort decisions?

Then help the user construct a **hopeful narrative** — not naive optimism, but Krafft's "fundierte Hoffnung": a credible, agency-preserving story about how the organization moves through these futures. Use the template in `templates/hoffnung-narrative.md`.

### 5. Derive robust moves and signals to watch

For each scenario, identify:

- **No-regret moves** — actions that pay off in every scenario
- **Option-creating moves** — investments that buy the right to act later
- **Scenario-specific moves** — bets that only make sense if a specific future materializes
- **Watch-list signals** — observable indicators that would shift probability mass between scenarios

Use the canvas in `templates/szenario-workshop-canvas.md` to capture this. The `scripts/scenario_brief.py` script renders a clean markdown brief from a YAML input.

## Output style

Outputs from this skill should read like a strategist talking to an executive, not like an academic paper. Concrete. Time-stamped. Honest about uncertainty without hiding behind it. Always end with the "so what" — what should the user actually do on Monday.

When the user shares a real strategic question, deliver:

1. A reframed, sharper version of their question
2. A trend map (text or compact table)
3. 3–4 scenarios with narratives and implications
4. A psychological read of the scenario set
5. A short list of no-regret moves and signals to watch

## Pitfalls to avoid

- **Confusing forecast with scenario.** A forecast says what will happen. A scenario says what could happen and why. Never collapse a scenario set back to a single most-likely line.
- **Megatrend listicles.** Reciting "AI, demographics, climate, geopolitics" without making them concrete for the user's context is theatre. Always operationalize.
- **Skipping the psychological layer** because it feels soft. It is what makes scenario work actually change behavior.
- **Optimism-by-decree.** Hope is grounded in agency, not in cheerleading. If the analysis is bleak, name it, then ask what agency remains.

## Key sources operationalized in this skill

- Krafft, A. (2022). *Unsere Hoffnungen, unsere Zukunft: Erkenntnisse aus dem Hoffnungsbarometer.* Springer. → psychological layer.
- Roos, G.T. (2018). *Megatrends und Herausforderungen für die Schweiz.* swissfuture / digitalswitzerland. → trend catalog for Swiss context.
- Swissfuture (2014). *Wertewandel in der Schweiz 2030. Vier Szenarien.* → archetype example for value-driven scenarios.

Reference files in this skill distill and apply these sources for business use.
