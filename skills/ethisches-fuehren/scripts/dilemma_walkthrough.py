#!/usr/bin/env python3
"""
dilemma_walkthrough.py — Walk through an ethical dilemma analysis with structured
prompts. Produces a written reflection artifact.

Usage:
    python dilemma_walkthrough.py                 # interactive
    python dilemma_walkthrough.py --input <yaml>  # from YAML
    python dilemma_walkthrough.py --output <md>   # write to file
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


QUESTIONS = [
    ("situation", "Describe the situation clearly, without framing it for a particular answer:"),
    ("is_dilemma", "Is this genuinely a dilemma (two legitimate values in tension), or is it a temptation (you know the right answer but are looking for permission)?"),
    ("option_a", "Option A — describe the action and what it honors / what it violates:"),
    ("option_b", "Option B — describe the action and what it honors / what it violates:"),
    ("affected", "Who is specifically affected by this decision? Name them where possible:"),
    ("consequentialist", "Consequentialist lens — which option produces better outcomes overall?"),
    ("deontological", "Deontological lens — which option honors duties and rights?"),
    ("virtue", "Virtue lens — which option does a person of good character take?"),
    ("mentor_test", "The mentor test — what would your most respected mentor advise?"),
    ("press_test", "The press test — what would you be comfortable defending publicly?"),
    ("regret_test", "The regret test — which regret will be harder to live with?"),
    ("integrity_test", "The integrity test — which option is consistent with who you are trying to be?"),
    ("cost_acknowledgment", "Acknowledgment of cost — name what you give up in the option you are leaning toward:"),
    ("decision", "The decision — what you will do, with awareness of what it costs:"),
    ("first_action", "The first concrete action — what you do in the next 24 hours:"),
    ("documentation", "The brief written record of your reasoning, for yourself:"),
]


def gather_interactive() -> dict:
    answers: dict = {}
    print("\nEthical dilemma walk-through\n")
    print("Take your time. The point is honest engagement, not speed.\n")
    for key, prompt in QUESTIONS:
        print(prompt)
        print("(enter blank line when finished)")
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line.strip() == "":
                if lines:
                    break
                continue
            lines.append(line)
        answers[key] = "\n".join(lines)
        print()
    return answers


def render(answers: dict) -> str:
    out = []
    out.append("# Dilemma reflection\n\n")
    sections = {
        "situation": "## The situation",
        "is_dilemma": "## Dilemma or temptation?",
        "option_a": "## Option A",
        "option_b": "## Option B",
        "affected": "## Who is affected",
        "consequentialist": "## Consequentialist lens",
        "deontological": "## Deontological lens",
        "virtue": "## Virtue lens",
        "mentor_test": "## Mentor test",
        "press_test": "## Press test",
        "regret_test": "## Regret test",
        "integrity_test": "## Integrity test",
        "cost_acknowledgment": "## Cost of the choice",
        "decision": "## The decision",
        "first_action": "## First concrete action",
        "documentation": "## Written record",
    }
    for key, _ in QUESTIONS:
        out.append(sections[key] + "\n\n")
        out.append(answers.get(key, "") + "\n\n")

    out.append("---\n\n")
    out.append("_Revisit this in 90 days. The decisions we live well with are usually the ones we made with awareness of cost, not the ones we pretended cost nothing._\n")
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    if args.input:
        if yaml is None:
            print("PyYAML required for --input", file=sys.stderr)
            return 2
        answers = yaml.safe_load(args.input.read_text(encoding="utf-8"))
    else:
        answers = gather_interactive()

    md = render(answers)
    if args.output:
        args.output.write_text(md, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
