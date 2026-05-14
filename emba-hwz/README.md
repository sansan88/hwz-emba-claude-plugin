# EMBA HWZ Plugin

A Cowork / Claude Code plugin containing 16 specialized skills derived from the Advanced Management Program EMBA at HWZ Zurich. Each skill operationalizes the content of one teaching day (or a multi-day module) for practical business application.

## Modules covered

| # | Skill | Module | Dozent/in |
|---|-------|--------|-----------|
| 01 | `zukunftsforschung` | B1T1 – Insights aus der Schweizer Zukunftsforschung | Krafft |
| 02 | `politische-rechtliche-landkarte` | B1T2 – (Menschen)rechtliche Landkarte & SDGs | Afflerbach, Oser, Nonnen |
| 03 | `entscheiden-unter-unsicherheit` | B1T3 – Entscheiden unter Unsicherheit | Fieres |
| 04 | `ai-data-science-new-normal` | B2T1 – AI & Data Science als New Normal | Blattner |
| 05 | `people-analytics` | B2T2 – People Analytics at Microsoft | Büchsenschuss, Schafheitle |
| 06 | `digital-law-ai-governance` | B2T3 – Digital Law & AI Governance | Morand |
| 07 | `strategie-als-kompass` | B3T1+2 – Strategic Power / Strategie als Kompass | Straub |
| 08 | `nachhaltigkeit-strategisch` | B3T3 – Nachhaltigkeit als Strategischer Plan | Fieres |
| 09 | `regenerative-organisation` | B4T1 – Zielbild re-generative Organisation | Weibel, Nonnen |
| 10 | `psychologie-veraenderung` | B4T2 – Psychologie der Veränderung | Berenbold |
| 11 | `organisationsevolution` | B4T3 – Transformative Organisationsevolution | Stoisser |
| 12 | `mindful-self-leadership` | B5T1 – Mindful (Self-)Leadership | Rieber, Sievers |
| 13 | `sinnstiftendes-leadership` | B5T2+3 – Sinnstiftendes Leadership & Dialog | Gross, Bauer |
| 14 | `purpose-driven-companies` | B6T1 – Purpose-driven Companies | Hügli |
| 15 | `sales-excellence` | B6T2 – Marketing & CRM / Sales Excellence | Staudacher |
| 16 | `ethisches-fuehren` | Themenübergreifend – Ethisches Führen | Palazzo |

## Skill anatomy

Each skill follows the same structure:

```
<skill-name>/
├── SKILL.md           — Main entry: when to trigger, mental model, workflow, pitfalls
├── references/        — Deep-dive documentation loaded as needed
│   └── *.md
├── templates/         — Fill-in canvases for executive use
│   └── *.md
└── scripts/           — Python helpers that render briefs/reports from YAML
    └── *.py
```

The SKILL.md `description` field is the primary triggering mechanism — when you ask Claude something that matches, the skill activates and Claude uses the workflow + references to deliver.

## Installation

### As a Cowork plugin
Install `emba-hwz.plugin` (the zip file) through Cowork's plugin management.

### As a local Claude Code plugin
Place the `emba-hwz` folder under your Claude Code plugins directory.

### As local skills (Cowork)
Place the `emba-hwz/skills/*` folders under Cowork's user skills directory.

## Usage examples

Once installed, ask Claude questions like:

- "Help me build a scenario plan for our 2030 product strategy" → triggers `zukunftsforschung`
- "I need to make a high-stakes decision with incomplete information" → triggers `entscheiden-unter-unsicherheit`
- "Draft an AI governance policy for our company" → triggers `digital-law-ai-governance`
- "What's the strategic positioning play for our market entry?" → triggers `strategie-als-kompass`
- "Help me think through our sustainability strategy" → triggers `nachhaltigkeit-strategisch`
- "We have a culture issue around speak-up — what should I do?" → triggers `ethisches-fuehren`
- "I need to lead a transformation that has stalled" → triggers `psychologie-veraenderung`
- "Help me develop a Zukunftsbild for our strategy retreat" → triggers `strategie-als-kompass`
- "Our People Analytics program has eroded trust — how do we fix it?" → triggers `people-analytics`
- "What does good work actually look like in our organization?" → triggers `regenerative-organisation`

Most skills work together. A serious strategy refresh will pull `zukunftsforschung` + `strategie-als-kompass` + possibly `nachhaltigkeit-strategisch` + `regenerative-organisation` into a coherent piece of work.

## Building blocks

Across the 16 skills, the plugin contains:

- **16 SKILL.md** files — the main entry points
- **71 reference documents** — operational depth on specific topics
- **41 template canvases** — fill-in tools for executive use
- **16 Python scripts** — YAML → markdown brief renderers for specific artifacts (scenario briefs, decision journals, AI use case classification, emissions summaries, etc.)

## Maintenance

The skills are written to be useful as the world changes. Specific things worth refreshing periodically:

- **AI Act timeline** in `digital-law-ai-governance` — application dates and case law
- **SBTi methodology** in `nachhaltigkeit-strategisch` — pathway updates
- **Scandal cases** in `ethisches-fuehren` — new cases that illustrate the patterns
- **Megatrend catalog** in `zukunftsforschung` — trends shift

The skill structure makes these refreshes localized — update the relevant reference file, not the whole skill.

## Origin

Built collaboratively between Sandro and Claude in Cowork mode, May 2026, from the curriculum PDFs and Sandro's notes for the HWZ Executive MBA Advanced Management Program. The skills represent operational versions of the academic content — designed to be useful in business decision-making rather than for exam preparation.
