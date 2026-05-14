#!/usr/bin/env python3
"""
experiment_brief.py — Render a clean experiment brief from a YAML spec, ready
for the team to review and commit to before running the experiment.

Usage:
    python experiment_brief.py <input.yaml> [--output <out.md>]

YAML schema:
    name: str
    pattern_or_hypothesis: str
    default_to_interrupt: str
    design:
      what_we_will_do: str
      participants: [str, ...]
      duration: str
      scope: str
      baseline: str
    hypothesis:
      expected: str
      falsifying: str
      surprising: str
    observations:
      quantitative: [str, ...]
      qualitative: [str, ...]
      frequency: str
    reflection:
      when: str
      who: [str, ...]
    decision_rule:
      stop: str
      refine: str
      scale: str
      kill: str
    risks: [{risk: str, likelihood: low|medium|high, impact: low|medium|high, safeguard: str}, ...]
    off_switch: str
    sponsorship:
      senior_sponsor: str
      owner: str
      observer: str
    two_am_answer: str
    connection: str
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


def section(title: str, body: str) -> str:
    return f"## {title}\n\n{body}\n\n"


def render(spec: dict) -> str:
    out = []
    out.append(f"# Experiment: {spec.get('name', '(unnamed)')}\n\n")

    out.append(section("Pattern / hypothesis", spec.get("pattern_or_hypothesis", "")))
    out.append(section("Default mode we are interrupting", spec.get("default_to_interrupt", "")))

    d = spec.get("design", {}) or {}
    design_body = []
    design_body.append(f"**What we will do.** {d.get('what_we_will_do', '')}\n")
    if d.get("participants"):
        design_body.append("**Participants.** " + ", ".join(d["participants"]) + "\n")
    design_body.append(f"**Duration.** {d.get('duration', '')}\n")
    design_body.append(f"**Scope.** {d.get('scope', '')}\n")
    design_body.append(f"**Baseline.** {d.get('baseline', '')}\n")
    out.append(section("Design", "\n".join(design_body)))

    h = spec.get("hypothesis", {}) or {}
    h_body = (
        f"**Expected outcome.** {h.get('expected', '')}\n\n"
        f"**What would falsify it.** {h.get('falsifying', '')}\n\n"
        f"**What would surprise us.** {h.get('surprising', '')}"
    )
    out.append(section("Hypothesis", h_body))

    o = spec.get("observations", {}) or {}
    o_lines = []
    if o.get("quantitative"):
        o_lines.append("**Quantitative:**")
        for q in o["quantitative"]:
            o_lines.append(f"- {q}")
    if o.get("qualitative"):
        o_lines.append("\n**Qualitative:**")
        for q in o["qualitative"]:
            o_lines.append(f"- {q}")
    if o.get("frequency"):
        o_lines.append(f"\n**Frequency.** {o['frequency']}")
    out.append(section("Observation plan", "\n".join(o_lines)))

    r = spec.get("reflection", {}) or {}
    r_body = f"**When.** {r.get('when', '')}\n\n"
    if r.get("who"):
        r_body += "**Who.** " + ", ".join(r["who"])
    out.append(section("Reflection", r_body))

    dr = spec.get("decision_rule", {}) or {}
    dr_body = (
        f"- **Stop** if: {dr.get('stop', '')}\n"
        f"- **Refine and continue** if: {dr.get('refine', '')}\n"
        f"- **Scale** if: {dr.get('scale', '')}\n"
        f"- **Kill** if: {dr.get('kill', '')}"
    )
    out.append(section("Decision rule", dr_body))

    risks = spec.get("risks") or []
    if risks:
        rk_body = "| Risk | Likelihood | Impact | Safeguard |\n|------|-----------|--------|-----------|\n"
        for r in risks:
            rk_body += f"| {r.get('risk', '')} | {r.get('likelihood', '')} | {r.get('impact', '')} | {r.get('safeguard', '')} |\n"
        out.append(section("Risks & safeguards", rk_body))

    out.append(section("Off switch", spec.get("off_switch", "")))

    sp = spec.get("sponsorship", {}) or {}
    sp_body = (
        f"- **Senior sponsor.** {sp.get('senior_sponsor', '')}\n"
        f"- **Owner.** {sp.get('owner', '')}\n"
        f"- **Observer.** {sp.get('observer', '')}"
    )
    out.append(section("Sponsorship", sp_body))

    out.append(section("The 2 a.m. answer", spec.get("two_am_answer", "")))
    out.append(section("Connection to wider transformation", spec.get("connection", "")))

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
