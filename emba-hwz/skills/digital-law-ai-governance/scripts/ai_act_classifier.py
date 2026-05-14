#!/usr/bin/env python3
"""
ai_act_classifier.py — Walk through the EU AI Act classification for a given
AI system and produce a written classification with rationale and obligation
summary. Decision-support, not legal advice.

Usage:
    python ai_act_classifier.py <input.yaml> [--output <out.md>]

YAML schema:
    system:
      name: str
      description: str
      eu_market_or_outputs_used_in_eu: yes | no
      we_are: provider | deployer | both
      domain:                       # check all that apply
        biometrics: yes | no
        critical_infrastructure: yes | no
        education: yes | no
        employment_hr: yes | no
        essential_services_credit: yes | no
        law_enforcement: yes | no
        migration_border: yes | no
        justice_democratic: yes | no
        product_safety_component: yes | no
      uses:                          # check all that apply
        social_scoring: yes | no
        emotion_recognition_workplace_or_education: yes | no
        biometric_categorization_sensitive: yes | no
        facial_recognition_scraping: yes | no
        subliminal_manipulation_harm: yes | no
        vulnerability_exploitation: yes | no
        predictive_policing_profiling: yes | no
      interaction:
        chatbot: yes | no
        generates_content: yes | no
        deepfakes: yes | no
      is_gpai_model: yes | no
      gpai_systemic_risk: yes | no
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


def classify(s: dict) -> tuple[str, list[str], list[str]]:
    """Return (class, rationale_lines, obligations)."""
    rationale: list[str] = []
    obligations: list[str] = []

    if s.get("eu_market_or_outputs_used_in_eu") != "yes":
        rationale.append("AI Act does not apply by territorial scope (no EU market placement; outputs not used in EU).")
        return ("out_of_scope", rationale, ["Consider EU AI Act only if territorial scope changes; check sectoral/national law."])

    uses = s.get("uses", {}) or {}
    if any(uses.get(k) == "yes" for k in [
        "social_scoring",
        "emotion_recognition_workplace_or_education",
        "biometric_categorization_sensitive",
        "facial_recognition_scraping",
        "subliminal_manipulation_harm",
        "vulnerability_exploitation",
        "predictive_policing_profiling",
    ]):
        flagged = [k for k, v in uses.items() if v == "yes"]
        rationale.append(f"Use(s) match Art. 5 prohibition: {', '.join(flagged)}.")
        obligations.append("DO NOT DEPLOY. Counsel review required. Penalties up to €35M or 7% of global turnover.")
        return ("prohibited", rationale, obligations)

    domain = s.get("domain", {}) or {}
    high_risk_paths = [
        ("biometrics", "Annex III §1 — biometrics (identification, categorization, emotion recognition outside prohibited contexts)"),
        ("critical_infrastructure", "Annex III §2 — critical infrastructure"),
        ("education", "Annex III §3 — education and vocational training"),
        ("employment_hr", "Annex III §4 — employment, worker management, access to self-employment"),
        ("essential_services_credit", "Annex III §5 — access to essential services including credit"),
        ("law_enforcement", "Annex III §6 — law enforcement"),
        ("migration_border", "Annex III §7 — migration, asylum, border control"),
        ("justice_democratic", "Annex III §8 — administration of justice and democratic processes"),
    ]
    matched = [(k, label) for k, label in high_risk_paths if domain.get(k) == "yes"]
    if matched:
        for _, label in matched:
            rationale.append(f"Domain triggers high-risk classification under {label}.")
        if domain.get("product_safety_component") == "yes":
            rationale.append("Also high-risk via Annex I path (safety component of EU-regulated product). 2027 timeline.")
        obligations += [
            "Implement risk management system (Art. 9)",
            "Data governance and bias mitigation (Art. 10)",
            "Technical documentation (Art. 11, Annex IV)",
            "Logging (Art. 12)",
            "Transparency and instructions for use (Art. 13)",
            "Human oversight (Art. 14)",
            "Accuracy, robustness, cybersecurity (Art. 15)",
            "Quality management system (Art. 17) — providers",
            "Conformity assessment before market placement (Art. 43) — providers",
            "Post-market monitoring (Art. 72) and incident reporting (Art. 73)",
        ]
        if s.get("we_are") in ("deployer", "both"):
            obligations += [
                "Deployer obligations Art. 26: use per instructions, oversight, monitor",
                "Fundamental rights impact assessment (Art. 27) if applicable to your deployer category",
                "Inform employees and worker representatives before workplace deployment (Art. 26(7))",
            ]
        obligations.append("Most obligations apply from 2 August 2026; Annex I path: 2 August 2027.")
        return ("high_risk", rationale, obligations)

    if domain.get("product_safety_component") == "yes":
        rationale.append("High-risk via Annex I path (safety component of EU-regulated product).")
        obligations.append("Coordinate with sectoral product safety regime. Most obligations apply 2 August 2027.")
        return ("high_risk", rationale, obligations)

    interaction = s.get("interaction", {}) or {}
    if any(interaction.get(k) == "yes" for k in ["chatbot", "generates_content", "deepfakes"]):
        rationale.append("Interaction triggers Art. 50 transparency obligations (limited risk).")
        obligations += [
            "Inform users they are interacting with AI (chatbots) unless obvious",
            "Label deepfakes and AI-generated content on matters of public interest (with exceptions)",
            "Inform persons subject to emotion recognition or biometric categorization",
        ]
        obligations.append("Apply from 2 August 2026.")
        return ("limited_risk", rationale, obligations)

    rationale.append("No prohibited use, no high-risk domain, no transparency-triggering interaction.")
    obligations.append("Minimal risk — no specific AI Act obligations beyond Art. 4 AI literacy.")

    if s.get("is_gpai_model") == "yes":
        obligations.append("GPAI model obligations apply (Art. 51+): technical documentation, downstream information, copyright policy, training data summary. From 2 August 2025.")
        if s.get("gpai_systemic_risk") == "yes":
            obligations.append("Systemic-risk GPAI: model evaluations, systemic risk assessments, incident reporting, cybersecurity. From 2 August 2025.")

    obligations.append("Note: AI literacy obligation Art. 4 applies broadly from 2 February 2025.")

    return ("minimal_risk", rationale, obligations)


def render(spec: dict) -> str:
    s = spec.get("system", {}) or {}
    name = s.get("name", "Unnamed system")
    desc = s.get("description", "")

    cls, rationale, obligations = classify(s)

    out = []
    out.append(f"# EU AI Act classification — {name}\n\n")
    out.append(f"> {desc}\n\n")
    out.append(f"## Classification: **{cls.replace('_', ' ').upper()}**\n\n")
    out.append("## Rationale\n\n")
    for r in rationale:
        out.append(f"- {r}\n")
    out.append("\n## Applicable obligations\n\n")
    for o in obligations:
        out.append(f"- {o}\n")
    out.append("\n---\n\n")
    out.append("_Decision-support output. Not legal advice. Validate with counsel before relying on this for compliance._\n")
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
