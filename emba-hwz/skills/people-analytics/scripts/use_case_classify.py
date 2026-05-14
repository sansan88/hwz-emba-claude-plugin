#!/usr/bin/env python3
"""
use_case_classify.py — Classify a People Analytics use case against the
bad/good/greater-good typology and apply the trust filter to produce a
risk-graded verdict. Use during pre-deployment review or program audit.

Usage:
    python use_case_classify.py <input.yaml> [--output <out.md>]

YAML schema:
    use_case:
      name: str
      description: str
      data_sources: [str, ...]
      granularity: individual | team | org
      transparent: yes | partial | no
      worker_voice: meaningful | advisory | none
      individual_use: yes | no
      symmetric_leaders: yes | partly | no
      purpose_limited: strict | flexible | open
      worst_case_use: str
      reversibility: yes | principle | no
      automated_decision: yes | partial | no
      legal_basis: str
      dpia_done: yes | no
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


def classify_typology(uc: dict) -> tuple[str, list[str]]:
    """Return (type, rationale_lines)."""
    rationale = []
    individual = uc.get("individual_use", "yes") == "yes"
    symmetric = uc.get("symmetric_leaders", "no")
    voice = uc.get("worker_voice", "none")

    if individual and symmetric == "no" and voice == "none":
        rationale.append("Individual-level data, no leader symmetry, no worker voice → control-architecture pattern.")
        return ("bad", rationale)

    if not individual and symmetric in ("partly", "no"):
        rationale.append("Aggregated only, no/partial symmetry → evidence-architecture pattern.")
        return ("good", rationale)

    if symmetric == "yes" and voice == "meaningful":
        rationale.append("Symmetric measurement and meaningful worker voice → shared-understanding architecture.")
        return ("greater_good", rationale)

    rationale.append("Mixed signals — partial symmetry or partial voice. Drifting between types; design choice still open.")
    return ("mixed", rationale)


def trust_filter(uc: dict) -> tuple[str, list[str]]:
    """Apply the trust filter; return (verdict, flag_lines)."""
    flags: list[str] = []

    if uc.get("transparent") not in ("yes",):
        flags.append("Transparency: not full. Workers cannot understand what is collected and why.")
    if uc.get("worker_voice") not in ("meaningful",):
        flags.append("Worker voice: not meaningful. Program will rely on management goodwill only.")
    if uc.get("individual_use") == "yes" and uc.get("symmetric_leaders") in ("no", "partly"):
        flags.append("Individual-level measurement without symmetric leadership measurement. Asymmetric risk to trust.")
    if uc.get("purpose_limited") == "open":
        flags.append("Purpose is open-ended. High risk of surveillance creep.")
    if uc.get("reversibility") == "no":
        flags.append("Not reversible. Data once collected cannot be deleted easily.")
    if uc.get("automated_decision") == "yes":
        flags.append("Fully automated individual decision. Likely triggers Art. 22 GDPR / revFADP requirements.")
    if uc.get("dpia_done") != "yes":
        flags.append("DPIA not completed. High-risk processing without impact assessment.")
    if not uc.get("legal_basis"):
        flags.append("Legal basis not stated.")

    if len(flags) == 0:
        return ("green", flags)
    if len(flags) <= 2:
        return ("yellow", flags)
    return ("red", flags)


def render(spec: dict) -> str:
    uc = spec.get("use_case", {}) or {}
    name = uc.get("name", "Unnamed use case")
    desc = uc.get("description", "")

    out = []
    out.append(f"# Use case review — {name}\n\n")
    out.append(f"> {desc}\n\n")

    typology, type_lines = classify_typology(uc)
    out.append(f"## Typology classification: **{typology.replace('_', ' ').upper()}**\n\n")
    for line in type_lines:
        out.append(f"- {line}\n")
    out.append("\n")

    verdict, flag_lines = trust_filter(uc)
    out.append(f"## Trust filter verdict: **{verdict.upper()}**\n\n")
    if flag_lines:
        out.append("Flags raised:\n\n")
        for f in flag_lines:
            out.append(f"- {f}\n")
        out.append("\n")
    else:
        out.append("All filter questions answered acceptably.\n\n")

    out.append("## Recommended next steps\n\n")
    if verdict == "red":
        out.append("- **Do not deploy as designed.** Re-scope to address the flagged issues, or drop the use case.\n")
        out.append("- If proceeding, document why each flag is acceptable in writing.\n")
    elif verdict == "yellow":
        out.append("- **Deploy only with explicit mitigations** for each flag, with named owners and verification.\n")
        out.append("- Schedule a 90-day post-deployment review.\n")
    else:
        out.append("- **Deploy.** Schedule annual review and bias audit (if model-based).\n")

    if typology == "bad":
        out.append("- Even if technically deployable, reconsider whether the program design is consistent with the company's stated management model.\n")
    if typology == "mixed":
        out.append("- The use case is drifting between architectures. Design choice still open — pick deliberately rather than defaulting.\n")

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
