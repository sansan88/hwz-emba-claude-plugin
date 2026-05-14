#!/usr/bin/env python3
"""
diagnostic_checklist.py — Run an interactive Heifetz adaptive-vs-technical
diagnostic for a stated challenge. Produces a written verdict plus suggested
next steps.

Usage:
    python diagnostic_checklist.py                 # interactive prompt
    python diagnostic_checklist.py --input <yaml>  # answers as YAML
    python diagnostic_checklist.py --output <md>   # save verdict to file

YAML schema:
    challenge: str
    answers:
      solution_known: yes|partly|no
      who_changes: nobody|some|the_owners
      expert_solvable: yes|partly|no
      resistance_type: execution|emotional|both
      losses_involved: none|some|significant
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


QUESTIONS = [
    (
        "solution_known",
        "Is the solution known (or knowable by an expert)?",
        ["yes", "partly", "no"],
        {"yes": 0, "partly": 1, "no": 2},
    ),
    (
        "who_changes",
        "Whose values or behavior have to change for this to be solved?",
        ["nobody", "some", "the_owners"],
        {"nobody": 0, "some": 1, "the_owners": 2},
    ),
    (
        "expert_solvable",
        "Can an expert solve this without the team learning?",
        ["yes", "partly", "no"],
        {"yes": 0, "partly": 1, "no": 2},
    ),
    (
        "resistance_type",
        "What kind of resistance does this work meet?",
        ["execution", "emotional", "both"],
        {"execution": 0, "emotional": 2, "both": 1},
    ),
    (
        "losses_involved",
        "Are people losing something (status, identity, certainty, habit)?",
        ["none", "some", "significant"],
        {"none": 0, "some": 1, "significant": 2},
    ),
]


@dataclass
class Verdict:
    challenge: str
    score: int
    classification: str
    rationale: list[str]
    next_steps: list[str]


def classify(score: int) -> str:
    if score <= 3:
        return "technical"
    if score <= 6:
        return "mixed (technical + adaptive components)"
    return "adaptive"


def diagnose(challenge: str, answers: dict) -> Verdict:
    score = 0
    rationale = []
    for key, prompt, _opts, mapping in QUESTIONS:
        a = answers.get(key)
        if a not in mapping:
            raise ValueError(f"Missing or invalid answer for {key}: {a!r}")
        delta = mapping[a]
        score += delta
        rationale.append(f"- {prompt} → answered **{a}** (+{delta})")
    classification = classify(score)

    next_steps: list[str] = []
    if classification == "technical":
        next_steps.extend([
            "Assign clear ownership and resource the work like a project.",
            "Identify the right expertise; bring it in.",
            "Do not over-engineer the change management — this is execution.",
        ])
    elif "mixed" in classification:
        next_steps.extend([
            "Separate the technical and adaptive components explicitly.",
            "Run the technical part as a project. Run the adaptive part as a leadership engagement.",
            "Name to the team which parts are which — they will otherwise pull everything toward the technical (easier) frame.",
            "Identify whose values and behaviors have to shift, including the leader's own.",
        ])
    else:
        next_steps.extend([
            "Resist the urge to solve this with policy, training, or an expert. Those will be necessary but insufficient.",
            "Identify the adaptive work: whose beliefs, habits, loyalties, or practices must change?",
            "Surface the losses involved — adaptive change always means giving something up. Name what.",
            "As the leader, identify how *you* are part of the system that must change. Lead from that recognition.",
            "Regulate the heat: enough discomfort to mobilize, not so much that the team shuts down.",
            "Build pacing into the work. Adaptive change moves at the speed of the conversations the leader is willing to have.",
        ])

    return Verdict(
        challenge=challenge,
        score=score,
        classification=classification,
        rationale=rationale,
        next_steps=next_steps,
    )


def render(v: Verdict) -> str:
    out = []
    out.append(f"# Heifetz diagnostic: {v.challenge}\n\n")
    out.append(f"**Verdict:** {v.classification} (score {v.score}/10)\n\n")
    out.append("## Rationale\n\n")
    out.extend(line + "\n" for line in v.rationale)
    out.append("\n## Suggested next steps\n\n")
    for s in v.next_steps:
        out.append(f"- {s}\n")
    return "".join(out)


def interactive() -> tuple[str, dict]:
    challenge = input("Describe the challenge in one sentence: ").strip()
    answers: dict = {}
    for key, prompt, opts, _mapping in QUESTIONS:
        opts_str = " / ".join(opts)
        while True:
            a = input(f"{prompt} ({opts_str}): ").strip().lower()
            if a in opts:
                answers[key] = a
                break
            print(f"  Please answer with one of: {opts_str}")
    return challenge, answers


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", type=Path, help="YAML file with challenge + answers")
    ap.add_argument("--output", type=Path, help="Write verdict to this markdown file (default: stdout)")
    args = ap.parse_args()

    if args.input:
        if yaml is None:
            print("PyYAML required for --input: pip install pyyaml --break-system-packages", file=sys.stderr)
            return 2
        data = yaml.safe_load(args.input.read_text(encoding="utf-8"))
        challenge = data["challenge"]
        answers = data["answers"]
    else:
        challenge, answers = interactive()

    verdict = diagnose(challenge, answers)
    md = render(verdict)
    if args.output:
        args.output.write_text(md, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
