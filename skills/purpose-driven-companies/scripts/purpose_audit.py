#!/usr/bin/env python3
"""
purpose_audit.py — Audit a stated purpose against the operational and
behavioral tests, surface gaps, and recommend whether to close-the-gap,
update-the-purpose, acknowledge-the-journey, or quiet-the-claims.

Usage:
    python purpose_audit.py <input.yaml> [--output <out.md>]

YAML schema:
    company: str
    stated_purpose: str
    audit:
      journalist_test: pass | mixed | fail
      tradeoff_test:
        recent_decisions_purpose_shaped: yes | partially | no
        examples: [str, ...]
      whistleblower_test: pass | mixed | fail
      longitudinal_test:
        years_stable: int
      cost_test:
        what_purpose_costs_us: str
      internal_coherence:
        compensation: aligned | partial | misaligned
        hiring: aligned | partial | misaligned
        promotion: aligned | partial | misaligned
        capex: aligned | partial | misaligned
        speakup: aligned | partial | misaligned
      signature_programs:
        count: int
        examples: [str, ...]
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


def render(spec: dict) -> str:
    audit = spec.get("audit", {}) or {}
    out = []
    out.append(f"# Purpose audit — {spec.get('company', '(company)')}\n\n")
    out.append(f"**Stated purpose:**\n\n> {spec.get('stated_purpose', '')}\n\n")

    flags: list[str] = []
    pass_count = 0
    fail_count = 0

    # Each test
    out.append("## Test results\n\n")

    j = audit.get("journalist_test")
    if j == "pass":
        pass_count += 1
    elif j == "fail":
        fail_count += 1
        flags.append("Journalist test failed — operating behavior would expose gaps with stated purpose.")
    out.append(f"- **Journalist test:** {j or 'not assessed'}\n")

    t = audit.get("tradeoff_test", {}) or {}
    rd = t.get("recent_decisions_purpose_shaped")
    if rd == "yes":
        pass_count += 1
    elif rd == "no":
        fail_count += 1
        flags.append("No recent decisions shaped by purpose — purpose is decorative.")
    out.append(f"- **Trade-off test (recent decisions purpose-shaped):** {rd or 'not assessed'}\n")
    if t.get("examples"):
        for ex in t["examples"]:
            out.append(f"    - {ex}\n")

    w = audit.get("whistleblower_test")
    if w == "pass":
        pass_count += 1
    elif w == "fail":
        fail_count += 1
        flags.append("Whistleblower test failed — internal-vs-external mismatch likely visible to employees.")
    out.append(f"- **Whistleblower test:** {w or 'not assessed'}\n")

    lt = audit.get("longitudinal_test", {}) or {}
    years = lt.get("years_stable", 0)
    if years >= 5:
        pass_count += 1
    elif years < 3:
        fail_count += 1
        flags.append(f"Purpose unstable — only {years} years of consistent articulation.")
    out.append(f"- **Longitudinal test:** {years} years stable\n")

    ct = audit.get("cost_test", {}) or {}
    cost = ct.get("what_purpose_costs_us", "")
    if cost and cost.lower() not in ("nothing", "none", ""):
        pass_count += 1
        out.append(f"- **Cost test:** purpose costs us — {cost}\n")
    else:
        fail_count += 1
        flags.append("Cost test failed — if purpose costs nothing, it has no real claim on behavior.")
        out.append("- **Cost test:** no acknowledged cost; suspect decorative purpose\n")

    ic = audit.get("internal_coherence", {}) or {}
    out.append("- **Internal coherence:**\n")
    for dim in ["compensation", "hiring", "promotion", "capex", "speakup"]:
        val = ic.get(dim, "not assessed")
        out.append(f"    - {dim.capitalize()}: {val}\n")
        if val == "misaligned":
            fail_count += 1
            flags.append(f"Internal coherence — {dim} misaligned with purpose.")
        elif val == "aligned":
            pass_count += 1

    sp = audit.get("signature_programs", {}) or {}
    sp_count = sp.get("count", 0)
    if sp_count >= 2:
        pass_count += 1
    else:
        fail_count += 1
        flags.append(f"Only {sp_count} signature programs — purpose is anchored on too thin a base.")
    out.append(f"- **Signature programs:** {sp_count}\n")
    if sp.get("examples"):
        for ex in sp["examples"]:
            out.append(f"    - {ex}\n")

    out.append("\n## Flags\n\n")
    if flags:
        for f in flags:
            out.append(f"- ⚠️ {f}\n")
    else:
        out.append("- ✅ No major flags — purpose appears operationally supported.\n")

    out.append("\n## Recommendation\n\n")
    if fail_count >= 5:
        out.append("**Quiet the claims or fundamentally rebuild.**\n\n")
        out.append("The gap between stated purpose and operating behavior is large enough that continued amplification of purpose communication carries reputational and increasingly legal risk. Either:\n\n")
        out.append("- Quiet external purpose claims while structurally addressing the gap\n")
        out.append("- Update the purpose to one that genuinely fits current operations\n")
        out.append("- Commit to a multi-year close-the-gap program with honest milestone communication\n")
    elif fail_count >= 3:
        out.append("**Close the gap with operational commitments.**\n\n")
        out.append("The purpose is plausible but not yet operationally supported. The work is structural — compensation, hiring, decision rights, capital allocation — not communication.\n")
    elif fail_count >= 1:
        out.append("**Reinforce with specific moves.**\n\n")
        out.append("The purpose is largely supported. Address the specific gaps flagged. Consider strengthening signature programs.\n")
    else:
        out.append("**Maintain and deepen.**\n\n")
        out.append("Purpose is well-grounded. Annual review to confirm continued alignment. Consider whether the next phase of the purpose work is depth or visibility.\n")

    out.append(f"\n**Summary:** {pass_count} tests passed, {fail_count} tests failed.\n")

    if spec.get("notes"):
        out.append("\n## Notes\n\n")
        out.append(spec["notes"] + "\n")

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
