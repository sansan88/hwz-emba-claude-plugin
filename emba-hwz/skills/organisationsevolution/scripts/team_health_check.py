#!/usr/bin/env python3
"""
team_health_check.py — Run the compound (Hackman + Google Aristotle) team
diagnostic and produce a written report with the binding constraint identified
and recommended actions.

Usage:
    python team_health_check.py <input.yaml> [--output <out.md>]

YAML schema:
    team_name: str
    scores:                          # each 1-5
      # Hackman structural conditions
      real_team: int
      compelling_direction: int
      enabling_structure: int
      supportive_context: int
      coaching_available: int
      # Performance factors
      psychological_safety: int
      dependability: int
      structure_clarity: int
      meaning: int
      impact: int
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


DIMENSIONS = [
    ("real_team", "Real team (bounded, stable, interdependent)", "Hackman structural"),
    ("compelling_direction", "Compelling direction", "Hackman structural"),
    ("enabling_structure", "Enabling structure (composition, task, norms)", "Hackman structural"),
    ("supportive_context", "Supportive organizational context", "Hackman structural"),
    ("coaching_available", "Coaching available when needed", "Hackman structural"),
    ("psychological_safety", "Psychological safety", "Performance factor"),
    ("dependability", "Dependability", "Performance factor"),
    ("structure_clarity", "Structure & clarity", "Performance factor"),
    ("meaning", "Meaning", "Performance factor"),
    ("impact", "Impact", "Performance factor"),
]


RECOMMENDATIONS = {
    "real_team": "Confirm membership, work boundaries, and interdependence. A working group is not a team; redesign or rename.",
    "compelling_direction": "Sharpen the team's purpose into something specific, challenging, and consequential. Avoid generic mission statements.",
    "enabling_structure": "Review composition (size 5-8, right skills), task design (whole, meaningful), and explicit working agreements.",
    "supportive_context": "Surface what the surrounding organization is doing that works against this team. Address with senior sponsor.",
    "coaching_available": "Identify external or internal coaching support. Schedule periodic team-coaching sessions, not just individual.",
    "psychological_safety": "Run a structured safety conversation. Identify behaviors that erode it. Senior leaders model fallibility and curiosity.",
    "dependability": "Make commitments explicit (working agreements). Surface and address pattern of broken commitments. Address chronic underperformance directly.",
    "structure_clarity": "Clarify goals, roles, and execution plan. Document. Revisit when conditions change.",
    "meaning": "Connect each member's work to something they personally care about. Surface the contribution beyond the task.",
    "impact": "Surface where the team's work actually shapes outcomes. If impact is genuinely unclear, the team may be working on the wrong thing.",
}


def render(spec: dict) -> str:
    scores = spec.get("scores", {}) or {}
    name = spec.get("team_name", "(team)")

    out = []
    out.append(f"# Team health check — {name}\n\n")

    out.append("## Scores (1–5)\n\n")
    out.append("| Dimension | Score | Category |\n")
    out.append("|-----------|-------|----------|\n")
    for key, label, cat in DIMENSIONS:
        s = scores.get(key, 0)
        out.append(f"| {label} | {s} | {cat} |\n")
    out.append("\n")

    valid_scores = [(key, label, scores.get(key, 0)) for key, label, _ in DIMENSIONS if scores.get(key) is not None]
    avg = sum(s for _, _, s in valid_scores) / len(valid_scores) if valid_scores else 0
    out.append(f"**Average score:** {avg:.1f}\n\n")

    sorted_scores = sorted(valid_scores, key=lambda x: x[2])
    out.append("## Lowest-scoring dimensions (likely binding constraints)\n\n")
    for key, label, s in sorted_scores[:3]:
        out.append(f"- **{label}** — score {s}\n")
    out.append("\n")

    out.append("## Recommended actions on the lowest scores\n\n")
    for key, label, s in sorted_scores[:3]:
        out.append(f"### {label}\n\n{RECOMMENDATIONS.get(key, '')}\n\n")

    out.append("## Interpretation\n\n")
    if avg >= 4:
        out.append("- This team is high-performing on the diagnostic. Suitable as a focal team for evolution work.\n")
        out.append("- Maintain attention to the dimensions — conditions degrade if unattended.\n")
    elif avg >= 3:
        out.append("- Mixed picture. Address the binding constraints before piling additional transformation work on this team.\n")
    elif avg >= 2:
        out.append("- This team has substantial development work to do. Using it as a transformation lever right now will likely fail.\n")
        out.append("- Fix the structural conditions first; performance factors will follow.\n")
    else:
        out.append("- This team is in serious difficulty. Either rebuild it (membership, charter, conditions) or do not rely on it as a transformation lever.\n")

    notes = spec.get("notes", "")
    if notes:
        out.append("\n## Notes\n\n")
        out.append(notes + "\n")

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
