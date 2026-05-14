#!/usr/bin/env python3
"""
use_case_score.py — Score and rank a set of AI use cases by feasibility and
value, render a markdown report with the 2x2 grid and portfolio composition.

Usage:
    python use_case_score.py <input.yaml> [--output <out.md>]

YAML schema:
    use_cases:
      - name: str
        category: str         # process_automation | cognitive_insight | cognitive_engagement | knowledge_augmentation | content_generation | agentic
        value:
          size: int           # 1-5
          link: int           # 1-5  strength of link from capability to metric
          defensibility: int  # 1-5
        feasibility:
          data: int           # 1-5
          capability_maturity: int  # 1-5
          change_cost: int    # 1-5  (5 = low change cost; 1 = high)
          regulatory: int     # 1-5  (5 = low risk)
          sponsorship: int    # 1-5
        notes: str
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


def avg(d: dict) -> float:
    vals = [v for v in d.values() if isinstance(v, (int, float))]
    return sum(vals) / len(vals) if vals else 0.0


def classify(value: float, feasibility: float) -> str:
    if value >= 4 and feasibility >= 4:
        return "Strategic play (high value, ready)"
    if value >= 3 and feasibility >= 4:
        return "Quick win"
    if value >= 4 and feasibility <= 3:
        return "Moonshot — high value, hard"
    if value <= 2 and feasibility <= 2:
        return "De-prioritize"
    return "Build feasibility first"


def render(spec: dict) -> str:
    use_cases = spec.get("use_cases", []) or []
    enriched = []
    for uc in use_cases:
        v = avg(uc.get("value", {}) or {})
        f = avg(uc.get("feasibility", {}) or {})
        enriched.append({
            "name": uc.get("name", "?"),
            "category": uc.get("category", "?"),
            "value": v,
            "feasibility": f,
            "classification": classify(v, f),
            "notes": uc.get("notes", ""),
        })

    enriched.sort(key=lambda x: (x["value"] + x["feasibility"]), reverse=True)

    out = ["# AI use case portfolio — scored and classified\n\n"]
    out.append("| Use case | Category | Value | Feasibility | Classification |\n")
    out.append("|----------|----------|-------|-------------|----------------|\n")
    for uc in enriched:
        out.append(
            f"| {uc['name']} | {uc['category']} | {uc['value']:.1f} | {uc['feasibility']:.1f} | {uc['classification']} |\n"
        )
    out.append("\n")

    # Composition summary
    out.append("## Portfolio composition\n\n")
    counts: dict[str, int] = {}
    for uc in enriched:
        counts[uc["classification"]] = counts.get(uc["classification"], 0) + 1
    for k, v in counts.items():
        out.append(f"- {k}: **{v}**\n")
    out.append("\n")

    out.append("## Recommendations\n\n")
    qw = sum(1 for uc in enriched if uc["classification"] == "Quick win")
    sp = sum(1 for uc in enriched if uc["classification"] == "Strategic play (high value, ready)")
    ms = sum(1 for uc in enriched if uc["classification"] == "Moonshot — high value, hard")

    if qw < 2:
        out.append("- ⚠️ Fewer than 2 quick wins. Portfolio needs more near-term wins to build credibility.\n")
    if sp < 1:
        out.append("- ⚠️ No strategic plays. Portfolio is short of the high-value bets that justify the program.\n")
    if ms > 1:
        out.append("- ⚠️ More than 1 moonshot. Trim — high-risk projects in excess of the org's risk tolerance kill programs.\n")
    if not any([qw < 2, sp < 1, ms > 1]):
        out.append("- ✅ Composition looks balanced. Confirm sponsorship and data dependencies before locking.\n")

    out.append("\n## Notes per use case\n\n")
    for uc in enriched:
        if uc["notes"]:
            out.append(f"- **{uc['name']}** — {uc['notes']}\n")

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
