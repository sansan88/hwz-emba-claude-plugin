# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This repo contains the source for a **Claude Code / Cowork plugin** named `emba-hwz`. It is not an application — there is no build, server, or test suite. Each "feature" is a *skill*: a markdown-driven instruction bundle that Claude loads at runtime when its `description` matches the user's request.

The plugin operationalizes 16 modules of Sandro's HWZ Executive MBA Advanced Management Program. The full module → skill mapping lives in [`emba-hwz/README.md`](./emba-hwz/README.md).

## Repository layout

- `emba-hwz/.claude-plugin/plugin.json` — plugin manifest (name, version, description, keywords)
- `emba-hwz/skills/<skill-name>/` — one directory per skill, all following the same anatomy:
  - `SKILL.md` — entry point with YAML frontmatter (`name`, `description`) + workflow body
  - `references/*.md` — deep-dive docs Claude loads on demand
  - `templates/*.md` — fill-in canvases for executive use
  - `scripts/*.py` + `scripts/*.example.yaml` — standalone Python renderers (YAML → markdown brief)
- `emba-hwz.plugin` — packaged zip distributed via Cowork

## How skill triggering works (critical context)

The `description:` field in each SKILL.md frontmatter is the **only** triggering mechanism — Claude scans descriptions to decide whether to load a skill. When editing skills:

- The description must list *concrete trigger phrases, names, and frameworks* the user is likely to say (German + English, person names like "Krafft", "Hoffnungsbarometer", framework names, scenario phrases like "what if 2030"). See `emba-hwz/skills/zukunftsforschung/SKILL.md` for the canonical example.
- The description should also tell Claude when **not** to use the skill (wrong tool for short-cycle forecasting, etc.).
- Skill bodies typically follow: *When to lean on this skill → Mental model → Workflow → Pitfalls*. Preserve this shape when editing.

## Scripts

Each skill's `scripts/<name>.py` is a self-contained Python 3 script that reads a YAML spec and renders an executive-ready markdown brief. They have no shared dependencies and no package layout — run directly:

```
python emba-hwz/skills/<skill>/scripts/<script>.py <input.yaml> [--output <out.md>]
```

Each script has a sibling `<script>.example.yaml` documenting the schema. When modifying a script, update the example YAML and the schema docstring at the top of the script in lockstep.

## Editing conventions

- **Skills are documents, not code.** Most edits are to `SKILL.md`, `references/*.md`, or `templates/*.md`. There is no lint or type check — review prose carefully.
- **Localized refreshes.** The `## Maintenance` section of `emba-hwz/README.md` lists items that drift over time (AI Act timeline, SBTi methodology, scandal cases, megatrend catalog). Update the specific reference file, not the whole skill.
- **Bilingual content.** Skills mix German module names and English operational guidance — keep that pattern; do not translate one into the other.
- **Skill independence.** Skills should compose at the user's request (e.g. `zukunftsforschung` + `strategie-als-kompass`) but each must stand alone. Don't introduce hard cross-references that break a skill when used in isolation.

## Packaging

`emba-hwz.plugin` is the zipped `emba-hwz/` directory for Cowork installation. Re-zip after changes if you need to redistribute; the local Claude Code install reads `emba-hwz/` directly.
