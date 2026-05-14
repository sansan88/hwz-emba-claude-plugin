#!/usr/bin/env python3
"""
strategy_narrative.py — Compose the integrating strategic narrative from a
YAML spec containing status quo, environment, Zukunftsbild, objectives, and
trade-offs. Produces a clean markdown narrative that senior leaders can use
as the verbal version of the strategy.

Usage:
    python strategy_narrative.py <input.yaml> [--output <out.md>]

YAML schema:
    company: str
    horizon: str          # e.g., "2032"
    status_quo_summary: str
    hardest_truths: [str, ...]
    environment_summary: str
    zukunftsbild:
      headline: str
      known_for: str
      customers: str
      employees: str
      engine: str
      stopped_doing: [str, ...]
      identity: str
    why_this_matters: str
    objectives:
      - name: str
        outcome: str
        why: str
    trade_offs: [str, ...]
    first_moves: [{what: str, who: str, by_when: str}, ...]
    cultural_implications: str
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
    out = []
    out.append(f"# Strategic narrative — {spec.get('company', '(company)')}\n\n")
    out.append(f"_Horizon: **{spec.get('horizon', 'unspecified')}**_\n\n")

    out.append("## 1. Where we are\n\n")
    out.append(spec.get("status_quo_summary", "") + "\n\n")

    truths = spec.get("hardest_truths") or []
    if truths:
        out.append("**The hardest truths we have to face:**\n\n")
        for t in truths:
            out.append(f"- {t}\n")
        out.append("\n")

    out.append("## 2. What is moving in the world that matters\n\n")
    out.append(spec.get("environment_summary", "") + "\n\n")

    z = spec.get("zukunftsbild", {}) or {}
    out.append("## 3. Where we are going\n\n")
    out.append(f"**Headline.** {z.get('headline', '')}\n\n")
    out.append(f"**What we will be known for.** {z.get('known_for', '')}\n\n")
    out.append(f"**Who we serve and how.** {z.get('customers', '')}\n\n")
    out.append(f"**Our work for employees.** {z.get('employees', '')}\n\n")
    out.append(f"**Our economic engine.** {z.get('engine', '')}\n\n")
    if z.get("stopped_doing"):
        out.append("**What we will have stopped doing:**\n\n")
        for s in z["stopped_doing"]:
            out.append(f"- {s}\n")
        out.append("\n")
    out.append(f"**Our identity.** {z.get('identity', '')}\n\n")

    out.append("## 4. Why this matters\n\n")
    out.append(spec.get("why_this_matters", "") + "\n\n")

    objs = spec.get("objectives") or []
    if objs:
        out.append("## 5. The choices we are making — strategic objectives\n\n")
        for o in objs:
            out.append(f"### {o.get('name', '(unnamed)')}\n")
            out.append(f"**Outcome.** {o.get('outcome', '')}\n\n")
            out.append(f"**Why this one.** {o.get('why', '')}\n\n")

    tradeoffs = spec.get("trade_offs") or []
    if tradeoffs:
        out.append("## 6. And what we are choosing not to do\n\n")
        for t in tradeoffs:
            out.append(f"- {t}\n")
        out.append("\n")

    cult = spec.get("cultural_implications", "")
    if cult:
        out.append("## 7. What this asks of us\n\n")
        out.append(cult + "\n\n")

    moves = spec.get("first_moves") or []
    if moves:
        out.append("## 8. The first concrete moves\n\n")
        out.append("| What | Who | By when |\n")
        out.append("|------|-----|---------|\n")
        for m in moves:
            out.append(f"| {m.get('what', '')} | {m.get('who', '')} | {m.get('by_when', '')} |\n")
        out.append("\n")

    out.append("---\n\n")
    out.append("_The verbal version of this narrative should fit in 7 minutes spoken. If yours is longer, distill until it does._\n")
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
