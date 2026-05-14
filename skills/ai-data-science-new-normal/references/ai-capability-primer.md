# AI Capability Primer for Executives

This reference is for the executive who needs to understand what AI does at the operating level — enough to make business decisions, not enough to write training code. Skip the mathematics. Keep the mental models that matter.

## What AI is — and is not

**AI is not** a single technology. It is a label that covers a stack of approaches with very different properties.

**The currently relevant clusters:**

1. **Classical machine learning** — supervised models (random forests, gradient boosting, linear models) trained on tabular data to predict an outcome. Boring, well-understood, still creates more business value in aggregate than any other AI category. Examples: credit risk, churn, demand forecasting, fraud detection.
2. **Deep learning for perception** — convolutional neural networks for images, sequence models for time series and audio. Mature for narrow tasks. Examples: medical imaging, defect detection, speech recognition.
3. **Large language models (LLMs) and GenAI** — transformer-based models trained on internet-scale text/code/image data. Capable of generation, summarization, retrieval, basic reasoning. Examples: customer support, knowledge work co-pilots, document generation.
4. **Agentic AI** — LLMs equipped with tools, memory, and multi-step planning. Emerging capability, currently real for narrow workflows, brittle for general tasks. Examples: research agents, structured data extraction pipelines, customer service triage.
5. **Optimization & reinforcement learning** — algorithms that find best policies under constraints. Mature in specific industries (logistics, ad bidding). Examples: route optimization, inventory, pricing.

Different problems need different clusters. Vendor pitches that conflate them are the first signal something is off.

## Agrawal et al.'s "prediction machines" framing

The most useful executive frame: AI is mostly about **drastically reducing the cost of prediction**. When prediction becomes cheap, decisions that depend on prediction become better — and decisions that did not previously involve prediction may now become predictable.

The corollary: judgment, action, and data become more valuable as prediction gets cheaper. Strategic implications:

- Tasks built around prediction get cheaper and better. Demand forecasting, credit scoring, ad targeting, defect detection.
- Tasks that depend on judgment about *what to do* with predictions become more valuable. Strategy, ethics, decision rights.
- Data infrastructure becomes the binding constraint — because cheap prediction needs data.

GenAI extends the same logic to *generation* — text, code, images, structured documents. The same economic logic applies: the cost of generation collapses, the value of judgment about quality, originality, and authority rises.

## How a machine "learns" — the only part executives need to know

A model is a function with adjustable parameters. Training is the process of adjusting those parameters so that the function produces outputs close to the right answers on labeled examples. Inference is using the trained function on new data.

The practical implications:

- **Models are only as good as their training data.** Bias in, bias out. Stale data, stale predictions.
- **Models generalize within their training distribution.** They do not extrapolate well to genuinely new situations. The "in-distribution" assumption is invisible until it breaks.
- **Models do not "know" things; they pattern-match.** GenAI hallucinations are a special case of this — confident pattern-matching that produces plausible nonsense.
- **Models drift.** The world changes; the model doesn't. Productionized AI requires monitoring and retraining.

## What modern AI is actually good at

In rough order of reliability for business decisions:

- **Pattern recognition in well-structured data.** Mature. ROI is real if the use case is well-scoped.
- **Routine generation in standard formats.** Reasonably mature. Drafts, summaries, extractions.
- **Speeding up knowledge work as a co-pilot.** Useful, but value depends heavily on workflow integration and user adoption.
- **Narrow agentic tasks.** Emerging. Brittle outside the scoped workflow.
- **General reasoning.** Unreliable. Don't bet a business decision on a model's chain-of-thought.

## What modern AI is unreliable at (as of mid-2026)

- **High-stakes single-shot decisions where the failure mode is silent.** A wrong prediction with high confidence is the dangerous failure pattern.
- **Tasks requiring up-to-date world knowledge** beyond training data, unless explicitly grounded in retrieval.
- **Reasoning chains longer than a few steps** without external verification.
- **Tasks requiring stable identity or memory across sessions** without engineered memory systems.
- **Adversarial robustness** — well-crafted inputs can flip outputs.

## The question to ask any AI vendor

The single most useful disambiguating question: **"On our data, in our environment, what error rate should we expect, and what is the failure mode?"**

Specific, real, falsifiable. Vendors that cannot answer should not be paid until they can.

## Data dependencies

Every AI capability has a data dependency. The "what data" question is the strategy question.

- **Internal proprietary data** — your competitive moat. Quality varies. Often locked in systems that don't talk to each other.
- **Vendor / SaaS data** — increasingly important. Watch for data residency, IP, and competitive sensitivity.
- **Public / scraped data** — useful for general-capability models, often not the differentiator.
- **Synthetic data** — fine for some tasks (training, augmentation), dangerous for others (validating in-distribution performance).

A common executive mistake: assuming the company has the data needed for a use case. Verify. Data audits are unglamorous and indispensable.

## When this primer is enough

This primer is enough to:
- Read a vendor pitch critically
- Decide whether a proposed use case is in the realistic envelope of current capability
- Ask the right questions in an AI strategy meeting
- Distinguish hype from substance

It is not enough to:
- Make model selection decisions (that needs an ML engineer)
- Estimate compute costs accurately
- Design a serving infrastructure
- Audit a model for bias or robustness

For those, get an ML engineer. The job of the executive is to make sure the right ones are hired and listened to.
