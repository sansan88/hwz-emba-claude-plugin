#!/usr/bin/env python3
"""
scenario_brief.py — Render a clean executive-ready markdown brief from a YAML
scenario specification.

Usage:
    python scenario_brief.py <input.yaml> [--output <output.md>]

The YAML schema (see scenario_brief.example.yaml for a worked example):

    decision_question: str            # The sharp question this set informs
    horizon: str                      # e.g., "2032"
    method: "2x2" | "archetypes"
    axes:                             # only if method == "2x2"
      axis_1:
        name: str
        endpoints: [str, str]
      axis_2:
        name: str
        endpoints: [str, str]
    scenarios:                        # 3-4 scenarios
      - name: str
        headline: str
        narrative: str
        features:
          market: str
          customers: str
          competition: str
          regulation: str
          technology: str
        signals: [str, ...]
        implications: [str, ...]
        psychological_read: str
    moves:
      no_regret: [str, ...]
      option_creating: [str, ...]
      scenario_specific: [{trigger: str, move: str}, ...]
    watch_list: [str, ...]
    integrating_narrative:
      hard_truths: str
      agency: str
      identity: str
      first_move: str
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    print("PyYAML is required: pip install pyyaml --break-system-packages", file=sys.stderr)
    sys.exit(1)


def _section(title: str, body: str) -> str:
    return f"## {title}\n\n{body}\n\n"


def render(spec: dict) -> str:
    out = []
    out.append(f"# Scenario brief — {spec.get('decision_question', '(no question stated)')}\n")
    out.append(f"_Horizon: **{spec.get('horizon', 'unspecified')}**_\n\n")

    method = spec.get("method", "unspecified")
    out.append(f"_Method: {method}_\n\n")

    if method == "2x2" and "axes" in spec:
        axes = spec["axes"]
        a1 = axes.get("axis_1", {})
        a2 = axes.get("axis_2", {})
        out.append("### Driving uncertainties\n\n")
        out.append(f"- **{a1.get('name', '?')}**: {a1.get('endpoints', ['?', '?'])[0]} ←→ {a1.get('endpoints', ['?', '?'])[1]}\n")
        out.append(f"- **{a2.get('name', '?')}**: {a2.get('endpoints', ['?', '?'])[0]} ←→ {a2.get('endpoints', ['?', '?'])[1]}\n\n")

    scenarios = spec.get("scenarios", [])
    out.append("## Scenarios\n\n")
    for s in scenarios:
        out.append(f"### {s.get('name', 'Unnamed scenario')}\n")
        out.append(f"**Headline.** {s.get('headline', '')}\n\n")
        out.append(f"{s.get('narrative', '')}\n\n")
        feats = s.get("features", {}) or {}
        if feats:
            out.append("**Distinctive features**\n\n")
            for k, v in feats.items():
                out.append(f"- {k.capitalize()}: {v}\n")
            out.append("\n")
        if s.get("signals"):
            out.append("**Signals it is materializing**\n\n")
            for sig in s["signals"]:
                out.append(f"- {sig}\n")
            out.append("\n")
        if s.get("implications"):
            out.append("**Implications for our decision**\n\n")
            for imp in s["implications"]:
                out.append(f"- {imp}\n")
            out.append("\n")
        if s.get("psychological_read"):
            out.append(f"**Psychological read.** {s['psychological_read']}\n\n")

    moves = spec.get("moves", {}) or {}
    if moves:
        out.append("## Move portfolio\n\n")
        if moves.get("no_regret"):
            out.append("**No-regret moves**\n\n")
            for m in moves["no_regret"]:
                out.append(f"- {m}\n")
            out.append("\n")
        if moves.get("option_creating"):
            out.append("**Option-creating moves**\n\n")
            for m in moves["option_creating"]:
                out.append(f"- {m}\n")
            out.append("\n")
        if moves.get("scenario_specific"):
            out.append("**Scenario-specific moves**\n\n")
            for m in moves["scenario_specific"]:
                out.append(f"- _{m.get('trigger', '?')}_ → {m.get('move', '?')}\n")
            out.append("\n")

    watch = spec.get("watch_list") or []
    if watch:
        out.append("## Watch list\n\n")
        for w in watch:
            out.append(f"- [ ] {w}\n")
        out.append("\n")

    narrative = spec.get("integrating_narrative") or {}
    if narrative:
        out.append("## Integrating narrative\n\n")
        out.append(f"**What is genuinely hard.** {narrative.get('hard_truths', '')}\n\n")
        out.append(f"**Where our agency lies.** {narrative.get('agency', '')}\n\n")
        out.append(f"**Who we want to be while navigating this.** {narrative.get('identity', '')}\n\n")
        out.append(f"**The first move that proves this is real.** {narrative.get('first_move', '')}\n\n")

    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", type=Path, help="YAML scenario spec")
    ap.add_argument("--output", type=Path, default=None, help="Output markdown file (default: stdout)")
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
