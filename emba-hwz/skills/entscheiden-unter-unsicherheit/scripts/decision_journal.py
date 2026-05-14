#!/usr/bin/env python3
"""
decision_journal.py — Render a decision journal entry as a clean markdown
artifact from a YAML spec. Use this to record consequential decisions before
their outcomes are known, so the epistemic state at the time of decision is
preserved for genuine after-action learning.

Usage:
    python decision_journal.py <input.yaml> [--output <out.md>]

YAML schema (see decision_journal.example.yaml for a worked example):

    date: YYYY-MM-DD
    decision_one_liner: str
    decision_maker: str
    decision_class:
      reversibility: one_way | two_way
      stakes: low | medium | high
      time_pressure: str
    options_considered:
      - name: str
        rejected_because: str   # null for chosen
    key_assumptions:
      - statement: str
        confidence: low | medium | high
        what_would_change_it: str
    strongest_case_against: str
    pre_mortem_top_risks: [str, ...]
    biases_active_and_counters: [{bias: str, counter_move: str}, ...]
    decision_rationale: str
    reversal_plan: str
    revisit_triggers: [str, ...]
    first_actions: [{what: str, who: str, by_when: str}, ...]
    epistemic_note: str
    revisit_date: YYYY-MM-DD
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("PyYAML required: pip install pyyaml --break-system-packages", file=sys.stderr)
    sys.exit(1)


def render(spec: dict) -> str:
    out: list[str] = []
    out.append(f"# Decision journal — {spec.get('decision_one_liner', '(unnamed)')}\n\n")
    out.append(f"**Date written:** {spec.get('date', '')}  \n")
    out.append(f"**Decision-maker:** {spec.get('decision_maker', '')}  \n")

    cls = spec.get("decision_class", {}) or {}
    out.append(f"**Reversibility:** {cls.get('reversibility', '')}  \n")
    out.append(f"**Stakes:** {cls.get('stakes', '')}  \n")
    out.append(f"**Time pressure:** {cls.get('time_pressure', '')}\n\n")

    out.append("## Options considered\n\n")
    for opt in spec.get("options_considered", []) or []:
        marker = "**chosen**" if not opt.get("rejected_because") else f"rejected — {opt['rejected_because']}"
        out.append(f"- **{opt.get('name', '?')}** — {marker}\n")
    out.append("\n")

    out.append("## Key assumptions\n\n")
    out.append("| Assumption | Confidence | What would change it |\n")
    out.append("|------------|------------|----------------------|\n")
    for a in spec.get("key_assumptions", []) or []:
        out.append(f"| {a.get('statement', '')} | {a.get('confidence', '')} | {a.get('what_would_change_it', '')} |\n")
    out.append("\n")

    out.append("## Strongest case against the chosen option\n\n")
    out.append(spec.get("strongest_case_against", "") + "\n\n")

    risks = spec.get("pre_mortem_top_risks") or []
    if risks:
        out.append("## Pre-mortem top risks\n\n")
        for r in risks:
            out.append(f"- {r}\n")
        out.append("\n")

    biases = spec.get("biases_active_and_counters") or []
    if biases:
        out.append("## Biases active and counter-moves\n\n")
        for b in biases:
            out.append(f"- **{b.get('bias', '')}** — counter: {b.get('counter_move', '')}\n")
        out.append("\n")

    out.append("## Decision rationale\n\n")
    out.append(spec.get("decision_rationale", "") + "\n\n")

    if spec.get("reversal_plan"):
        out.append("## Reversal plan\n\n")
        out.append(spec["reversal_plan"] + "\n\n")

    triggers = spec.get("revisit_triggers") or []
    if triggers:
        out.append("## Trigger conditions to revisit\n\n")
        for t in triggers:
            out.append(f"- {t}\n")
        out.append("\n")

    actions = spec.get("first_actions") or []
    if actions:
        out.append("## First actions\n\n")
        out.append("| What | Who | By when |\n")
        out.append("|------|-----|---------|\n")
        for a in actions:
            out.append(f"| {a.get('what', '')} | {a.get('who', '')} | {a.get('by_when', '')} |\n")
        out.append("\n")

    out.append("## Epistemic note (written before outcomes are known)\n\n")
    out.append(spec.get("epistemic_note", "") + "\n\n")

    if spec.get("revisit_date"):
        out.append(f"_Scheduled revisit: **{spec['revisit_date']}**_\n")

    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    spec = yaml.safe_load(args.input.read_text(encoding="utf-8"))
    md = render(spec)
    if args.output:
        args.output.write_text(md, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
