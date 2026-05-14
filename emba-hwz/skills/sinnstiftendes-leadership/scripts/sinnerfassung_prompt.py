#!/usr/bin/env python3
"""
sinnerfassung_prompt.py — Walk a user (interactively or from a YAML spec)
through the four-question Sinnerfassungsmethode and produce a written
reflection artifact.

Usage:
    python sinnerfassung_prompt.py                  # interactive
    python sinnerfassung_prompt.py --input <file>   # from YAML
    python sinnerfassung_prompt.py --output <file>  # write to file
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from textwrap import indent

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


QUESTIONS = [
    ("situation", "Describe the situation in one paragraph (the situation as it actually is, not your framing of it):"),
    ("kann", "Was kann ich tun? — What can I actually do here? List the real options, including the unattractive ones:"),
    ("moechte", "Was möchte ich tun? — What do I want to do? Where is my energy, what pulls me? Which values are activated?"),
    ("darf", "Was darf ich tun? — What may I do? What are my obligations, ethical considerations, real constraints?"),
    ("soll", "Was soll ich tun? — Given the above, what should I do? The action I can stand behind with inner consent."),
    ("inner_consent", "Inner-consent check: read the integrated action above; is inner consent present? (yes / mixed / no, plus explanation):"),
    ("first_step", "The first concrete step — what you do in the next 24 hours that begins to act this integration:"),
]


def gather_interactive() -> dict:
    answers: dict = {}
    print("\nSinnerfassungsmethode — four questions for finding meaning in a decision\n")
    for key, prompt in QUESTIONS:
        print(prompt)
        lines = []
        print("(enter blank line when finished)")
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
    out.append("# Sinnerfassung — reflection artifact\n\n")
    headings = {
        "situation": "## The situation",
        "kann": "## Was kann ich tun?",
        "moechte": "## Was möchte ich tun?",
        "darf": "## Was darf ich tun?",
        "soll": "## Was soll ich tun?",
        "inner_consent": "## Inner-consent check",
        "first_step": "## First concrete step",
    }
    for key, _ in QUESTIONS:
        out.append(headings[key])
        out.append("\n\n")
        out.append(answers.get(key, "") + "\n\n")

    out.append("---\n\n")
    out.append("_Walk this through again in 2 weeks. Meaning is renewable; check that the action still carries inner consent in light of what you learn between now and then._\n")
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", type=Path, help="YAML file with answers (skip interactive)")
    ap.add_argument("--output", type=Path, help="Write artifact to this file (default: stdout)")
    args = ap.parse_args()

    if args.input:
        if yaml is None:
            print("PyYAML required for --input mode", file=sys.stderr)
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
