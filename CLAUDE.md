# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This repo contains the source for a **Claude Code / Cowork plugin** named `emba-hwz`. It is not an application — there is no build, server, or test suite. Each "feature" is a *skill*: a markdown-driven instruction bundle that Claude loads at runtime when its `description` matches the user's request.

The plugin operationalizes 16 modules of Sandro's HWZ Executive MBA Advanced Management Program. The full module → skill mapping lives in [`README.md`](./README.md).

## Repository layout

The repo root *is* the plugin source (flat layout, no nested `emba-hwz/` directory). It also acts as a **single-plugin Claude Code marketplace** so the plugin can be added directly from GitHub.

- `.claude-plugin/marketplace.json` — marketplace manifest (lists the `emba-hwz` plugin with `source: "."`)
- `.claude-plugin/plugin.json` — plugin manifest (`name`, `version`, `description`, `keywords`)
- `skills/<skill-name>/` — one directory per skill, all following the same anatomy:
  - `SKILL.md` — entry point with YAML frontmatter (`name`, `description`) + workflow body
  - `references/*.md` — deep-dive docs Claude loads on demand
  - `templates/*.md` — fill-in canvases for executive use
  - `scripts/*.py` + `scripts/*.example.yaml` — standalone Python renderers (YAML → markdown brief)
- `README.md` — module → skill mapping and maintenance notes
- `emba-hwz.plugin` — packaged zip for offline distribution (contains a nested `emba-hwz/` directory with the same manifest inside)

## How skill triggering works (critical context)

The `description:` field in each SKILL.md frontmatter is the **only** triggering mechanism — Claude scans descriptions to decide whether to load a skill. When editing skills:

- The description must list *concrete trigger phrases, names, and frameworks* the user is likely to say (German + English, person names like "Krafft", "Hoffnungsbarometer", framework names, scenario phrases like "what if 2030"). See `skills/zukunftsforschung/SKILL.md` for the canonical example.
- The description should also tell Claude when **not** to use the skill (wrong tool for short-cycle forecasting, etc.).
- Skill bodies typically follow: *When to lean on this skill → Mental model → Workflow → Pitfalls*. Preserve this shape when editing.

## Scripts

Each skill's `scripts/<name>.py` is a self-contained Python 3 script that reads a YAML spec and renders an executive-ready markdown brief. They have no shared dependencies and no package layout — run directly:

```
python skills/<skill>/scripts/<script>.py <input.yaml> [--output <out.md>]
```

Each script has a sibling `<script>.example.yaml` documenting the schema. When modifying a script, update the example YAML and the schema docstring at the top of the script in lockstep.

## Editing conventions

- **Skills are documents, not code.** Most edits are to `SKILL.md`, `references/*.md`, or `templates/*.md`. There is no lint or type check — review prose carefully.
- **Localized refreshes.** The `## Maintenance` section of `README.md` lists items that drift over time (AI Act timeline, SBTi methodology, scandal cases, megatrend catalog). Update the specific reference file, not the whole skill.
- **Bilingual content.** Skills mix German module names and English operational guidance — keep that pattern; do not translate one into the other.
- **Skill independence.** Skills should compose at the user's request (e.g. `zukunftsforschung` + `strategie-als-kompass`) but each must stand alone. Don't introduce hard cross-references that break a skill when used in isolation.

## Installation paths

There are three ways to install the plugin, all consuming the same source:

1. **Marketplace (GitHub):** in Claude Code, run `/plugin marketplace add sansan88/hwz-emba-claude-plugin`, then `/plugin install emba-hwz@hwz-emba-marketplace`. Driven by `.claude-plugin/marketplace.json` + root `.claude-plugin/plugin.json`.
2. **Marketplace (local path):** `/plugin marketplace add /path/to/this/repo` for testing without pushing. Same files as (1).
3. **Cowork local plugin upload:** upload `emba-hwz.plugin` (the zip) in Cowork under *Plugins → Add local plugin*. Cowork unpacks the zip and registers the skills. The zip contains a nested `emba-hwz/` wrapper with its own `.claude-plugin/plugin.json` — Cowork expects this shape.

## Re-packaging the zip

When you change skills, rebuild `emba-hwz.plugin` so it stays in sync. The zip needs the nested `emba-hwz/` wrapper Cowork expects. From the repo root:

```
rm -rf /tmp/emba-hwz /tmp/emba-hwz.plugin
mkdir -p /tmp/emba-hwz/.claude-plugin
cp -r skills README.md /tmp/emba-hwz/
cp .claude-plugin/plugin.json /tmp/emba-hwz/.claude-plugin/
(cd /tmp && zip -r emba-hwz.plugin emba-hwz)
mv /tmp/emba-hwz.plugin .
```

The two `plugin.json` copies (root + zip) must stay identical — bump `version` in both when releasing.
