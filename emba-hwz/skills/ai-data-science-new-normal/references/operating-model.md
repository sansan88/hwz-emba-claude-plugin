# AI Operating Models — Choosing Deliberately

Once an organization has multiple AI use cases, the question shifts from "how do we do this one project" to "how do we do AI as an ongoing capability". This is the operating model question. Most companies drift into a default without choosing. The default is rarely optimal.

## The four main patterns

### Pattern 1 — Fully centralized
A single AI/data team owns all AI work across the company. Business units submit requests.

- **Pros:** Talent concentration, shared standards, easier governance, lower MLOps overhead.
- **Cons:** Bottleneck. Business units feel served, not enabled. Use cases without internal champions don't get built. Talent burns out from request load.
- **Best when:** Early in the journey, small org, limited talent, high regulatory governance need.

### Pattern 2 — Fully federated
Each business unit hires its own AI talent and runs its own projects.

- **Pros:** Business context preserved. Use cases match domain reality. No central bottleneck.
- **Cons:** No shared standards. Duplicated effort. Inconsistent quality. Smaller BUs underinvest. Models cannot be shared. Governance gaps.
- **Best when:** Very large, diversified holding-company structures with weak central technology.

### Pattern 3 — Hub-and-spoke (Fountaine/McCarthy/Saleh)
A central hub provides deep capability (ML engineering, MLOps, governance, data platform, training); embedded spokes in business units own use cases and combine business context with hub support.

- **Pros:** Balances depth and breadth. Standards plus context. Scales reasonably.
- **Cons:** Requires deliberate design of decision rights and handoffs; otherwise becomes either fully centralized or fully federated by default.
- **Best when:** Mid-sized to large organizations, mid-maturity, multi-business-unit structure. Now the most common pattern in serious AI adopters.

### Pattern 4 — Platform-driven
A small platform team builds the underlying AI/data platform. Product teams (with AI talent inside) build use cases on top of the platform autonomously.

- **Pros:** Highest scale. Use cases launch in weeks. Less coordination needed.
- **Cons:** Requires a mature platform to exist first. Requires AI literacy in product teams.
- **Best when:** Mature digital-native or transformed organizations with strong product-engineering cultures.

## How to choose

Match the model to maturity:

| Maturity score | Recommended model |
|----------------|-------------------|
| ≤ 2 | Centralized hub; few projects; build the team |
| 2–3 | Hub forming; spokes emerging; deliberate handoffs |
| 3–4 | Hub-and-spoke running; standards mature |
| 4+ | Platform-driven; spokes are largely autonomous |

The most expensive mistakes:

- Starting with a federated model when the company has no AI capability anywhere yet — leads to nothing real being built and lots of vendor spend.
- Staying centralized when the volume has grown beyond the hub's capacity — leads to bottlenecks and shadow AI.
- Drifting into hybrid without deliberate decision rights — produces conflict and finger-pointing.

## Decision rights — the work most organizations skip

Whatever model is chosen, write down the answers:

1. **Use case approval:** who decides which AI use cases get done? (Usually a steering committee with business and AI representation.)
2. **Production deployment:** who signs off that a model is fit to go live? (Hub for quality, business for fitness-for-purpose, governance for compliance.)
3. **Model retirement:** who decides when to deprecate a model that is no longer adding value or is drifting?
4. **Override and intervention:** who can override an AI decision in production? Under what circumstances? Logged?
5. **Vendor selection:** who decides build vs. buy for a given capability?
6. **Ethics escalation:** who handles concerns about bias, fairness, harm? With what authority?

Vague answers here are where AI programs get stuck politically. Write them down.

## The hub composition

For a typical hub-and-spoke at mid-maturity:

- **AI/ML engineers** — model development, training pipelines.
- **Data engineers** — pipelines, quality, infrastructure.
- **MLOps engineers** — productionization, monitoring, retraining.
- **Data platform engineers** — the platform itself.
- **AI product manager(s)** — use case prioritization, value capture.
- **Responsible AI / governance lead** — bias, fairness, compliance, ethics review.
- **Senior research / applied science** — for the genuinely novel work.

Hubs that are pure-research without product management produce papers, not products. Hubs that are pure-engineering without research are limited in what they can take on. Balance matters.

## Spoke composition

Each business unit running serious AI work needs:

- A senior business sponsor — who is accountable for value capture.
- A use case owner — typically a product manager or business analyst with AI literacy.
- One or two embedded data/ML engineers — close to the domain.
- A clear connection to the hub for shared resources.

Spokes without senior sponsorship are weather vanes — they spin with whatever pulls them.

## Governance overlay

Regardless of operating model, four governance functions need to exist:

1. **Use case prioritization** (where the portfolio decisions get made)
2. **Model risk and ethics review** (especially for high-risk classes under EU AI Act)
3. **Data governance** (quality, access, privacy)
4. **Vendor management** (third-party AI dependencies)

These can sit inside the hub, inside a separate governance function, or be hybrid. They should be named — not implicit.
