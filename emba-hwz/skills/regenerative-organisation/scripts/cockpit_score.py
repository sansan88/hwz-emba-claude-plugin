#!/usr/bin/env python3
"""
cockpit_score.py — Render a cockpit assessment from YAML scores, with pattern
diagnosis (Financial dominance, Stated values gap, Multi-stakeholder, Distressed).

Usage:
    python cockpit_score.py <input.yaml> [--output <out.md>]

YAML schema:
    company: str
    scores:                      # each 1-5
      financial_returns: int
      customer_value: int
      employee_experience: int
      suppliers_partners: int
      environment: int
      community_society: int
      governance_integrity: int
      resilience: int
    aspiration_gaps:            # 1-5, how large the stated-vs-reality gap is
      (same keys)
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


INSTRUMENTS = [
    ("financial_returns", "Financial returns"),
    ("customer_value", "Customer value"),
    ("employee_experience", "Employee experience"),
    ("suppliers_partners", "Suppliers & partners"),
    ("environment", "Environment"),
    ("community_society", "Community & society"),
    ("governance_integrity", "Governance & integrity"),
    ("resilience", "Resilience"),
]


def diagnose(scores: dict, gaps: dict) -> tuple[str, list[str]]:
    fin = scores.get("financial_returns", 0)
    others = [scores.get(k, 0) for k, _ in INSTRUMENTS if k != "financial_returns"]
    avg_others = sum(others) / len(others) if others else 0

    avg_gap = sum(gaps.values()) / len(gaps) if gaps else 0

    rationale: list[str] = []
    if fin >= 4 and avg_others <= 2.5:
        rationale.append("Strong financial returns, weak on other instruments. Pattern A — financial dominance.")
        return ("financial_dominance", rationale)
    if avg_gap >= 3 and any(g >= 4 for g in gaps.values()):
        rationale.append("Large gaps between stated aspirations and lived reality on multiple instruments. Pattern B — stated values, behavior gap.")
        return ("stated_values_gap", rationale)
    avg_all = (fin + sum(others)) / 8
    if avg_all >= 3.5 and all(s >= 3 for s in scores.values()):
        rationale.append("Genuine performance across multiple instruments with explicit trade-off conversations. Pattern C — multi-stakeholder.")
        return ("multi_stakeholder", rationale)
    if avg_all <= 2:
        rationale.append("Weak across most instruments. Pattern D — distressed.")
        return ("distressed", rationale)
    rationale.append("Mixed pattern. Surface the specific instruments most needing structural attention.")
    return ("mixed", rationale)


def render(spec: dict) -> str:
    scores = spec.get("scores", {}) or {}
    gaps = spec.get("aspiration_gaps", {}) or {}

    out = []
    out.append(f"# Cockpit assessment — {spec.get('company', '(company)')}\n\n")

    out.append("## Scores (1–5)\n\n")
    out.append("| Instrument | Current | Aspiration gap |\n")
    out.append("|------------|---------|-----------------|\n")
    for key, label in INSTRUMENTS:
        s = scores.get(key, 0)
        g = gaps.get(key, 0)
        out.append(f"| {label} | {s} | {g} |\n")
    out.append("\n")

    pattern, rationale = diagnose(scores, gaps)
    out.append(f"## Pattern diagnosis: **{pattern.replace('_', ' ').upper()}**\n\n")
    for r in rationale:
        out.append(f"- {r}\n")
    out.append("\n")

    # Largest gaps
    sorted_gaps = sorted(
        [(label, gaps.get(key, 0)) for key, label in INSTRUMENTS],
        key=lambda x: -x[1],
    )
    out.append("## The three largest aspiration gaps\n\n")
    for label, val in sorted_gaps[:3]:
        out.append(f"- **{label}** — gap {val}\n")
    out.append("\n")

    sorted_scores = sorted(
        [(label, scores.get(key, 0)) for key, label in INSTRUMENTS],
        key=lambda x: x[1],
    )
    out.append("## The three lowest current scores\n\n")
    for label, val in sorted_scores[:3]:
        out.append(f"- **{label}** — current {val}\n")
    out.append("\n")

    out.append("## Recommendations\n\n")
    if pattern == "financial_dominance":
        out.append("- The strategic risk is hidden in the dimensions not being watched. Begin structural investment in 2–3 weakest instruments before they become crises.\n")
        out.append("- Pattern A is what produces the Credit Suisse / Boeing-style failures over a decade. The financial picture looks fine until it doesn't.\n")
    elif pattern == "stated_values_gap":
        out.append("- The gap between aspiration and reality is the most acute internal credibility risk. Either narrow the gap with structural change, or revise the aspiration to match capability.\n")
        out.append("- Greenwashing-adjacent disclosure risk is real. CSRD / IFRS S2 require honest disclosure.\n")
    elif pattern == "multi_stakeholder":
        out.append("- The organization is operating closer to a regenerative pattern. The work is to deepen, not to bolt on. Examine the trade-off discipline.\n")
    elif pattern == "distressed":
        out.append("- Stabilization is the priority. Regenerative direction is the destination, not the immediate work.\n")
    elif pattern == "mixed":
        out.append("- Mixed pattern. Focus the work on the structural causes of the lowest-score instruments rather than spreading energy across all of them.\n")

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
