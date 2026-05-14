# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This repo contains the source for a **Claude Code / Cowork plugin** named `emba-hwz`. It is not an application — there is no build, server, or test suite. Each "feature" is a *skill*: a markdown-driven instruction bundle that Claude loads at runtime when its `description` matches the user's request.

The plugin operationalizes 16 modules of Sandro's HWZ Executive MBA Advanced Management Program. The full module → skill mapping lives in [`README.md`](./README.md).

## Repository layout

The repo root holds the **marketplace manifest** and maintainer docs; the actual plugin source lives in a nested `emba-hwz/` subdirectory. This split is intentional: it lets the repo act as a **single-plugin Claude Code marketplace** while keeping the plugin source in the same shape the Cowork zip expects, so the same directory tree feeds both install paths. The `"./emba-hwz"` relative source in `marketplace.json` is also broadly compatible across Claude Code versions (older versions rejected the root-shorthand `"."`).

- `.claude-plugin/marketplace.json` — marketplace manifest (lists the `emba-hwz` plugin with `source: "./emba-hwz"`)
- `emba-hwz/.claude-plugin/plugin.json` — plugin manifest (`name`, `version`, `description`, `keywords`)
- `emba-hwz/commands/emba-<skill-name>.md` — one slash command per skill, prefixed `emba-` so all 16 surface together when the user types `/emba-`. Each command is a thin wrapper whose body instructs Claude to invoke the matching skill with `$ARGUMENTS`.
- `emba-hwz/skills/<skill-name>/` — one directory per skill, all following the same anatomy:
  - `SKILL.md` — entry point with YAML frontmatter (`name`, `description`) + workflow body
  - `references/*.md` — deep-dive docs Claude loads on demand
  - `templates/*.md` — fill-in canvases for executive use
  - `scripts/*.py` + `scripts/*.example.yaml` — standalone Python renderers (YAML → markdown brief)
- `README.md` — module → skill mapping and maintenance notes (lives at the repo root, maintainer-facing only)
- `CLAUDE.md` — this file (repo root, maintainer-facing only)
- `emba-hwz.plugin` — packaged zip for offline distribution (the `emba-hwz/` subdirectory zipped as-is)

## How skill triggering works (critical context)

The `description:` field in each SKILL.md frontmatter is the **only** triggering mechanism — Claude scans descriptions to decide whether to load a skill. When editing skills:

- The description must list *concrete trigger phrases, names, and frameworks* the user is likely to say (German + English, person names like "Krafft", "Hoffnungsbarometer", framework names, scenario phrases like "what if 2030"). See `skills/zukunftsforschung/SKILL.md` for the canonical example.
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
- **Localized refreshes.** The `## Maintenance` section of `README.md` lists items that drift over time (AI Act timeline, SBTi methodology, scandal cases, megatrend catalog). Update the specific reference file, not the whole skill.
- **Bilingual content.** Skills mix German module names and English operational guidance — keep that pattern; do not translate one into the other.
- **Skill independence.** Skills should compose at the user's request (e.g. `zukunftsforschung` + `strategie-als-kompass`) but each must stand alone. Don't introduce hard cross-references that break a skill when used in isolation.

## Installation paths

There are three ways to install the plugin, all consuming the same source:

1. **Marketplace (GitHub):** in Claude Code, run `/plugin marketplace add sansan88/hwz-emba-claude-plugin`, then `/plugin install emba-hwz@hwz-emba-marketplace`. Driven by root `.claude-plugin/marketplace.json` pointing at the nested `emba-hwz/` directory.
2. **Marketplace (local path):** `/plugin marketplace add /path/to/this/repo` for testing without pushing. Same files as (1).
3. **Cowork local plugin upload:** upload `emba-hwz.plugin` (the zip) in Cowork under *Plugins → Add local plugin*. Cowork unpacks the zip and registers the skills. The zip wraps the same `emba-hwz/` directory as in the repo — Cowork expects this shape.

## Re-packaging the zip

When you change skills, rebuild `emba-hwz.plugin` so it stays in sync. Since the `emba-hwz/` directory in the repo is already in the shape Cowork expects, the rebuild is a one-liner from the repo root:

```
rm -f emba-hwz.plugin && zip -r emba-hwz.plugin emba-hwz -x '*.DS_Store'
```

Bump `version` in `emba-hwz/.claude-plugin/plugin.json` before re-packaging — there is now a single source of truth for the plugin manifest, but the zip must be regenerated for the new version to reach Cowork users.
