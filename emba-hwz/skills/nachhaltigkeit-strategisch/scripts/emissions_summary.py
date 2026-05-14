#!/usr/bin/env python3
"""
emissions_summary.py — Render a clean executive emissions summary from a YAML
inventory, with scope breakdown, Scope 3 category detail, and trend.

Usage:
    python emissions_summary.py <input.yaml> [--output <out.md>]

YAML schema:
    base_year: int
    reporting_year: int
    company: str
    unit: str                         # e.g., "tCO2e"
    inventory:
      scope_1: float
      scope_2_location_based: float
      scope_2_market_based: float
      scope_3:                        # all 15 categories, optional
        purchased_goods_services: float
        capital_goods: float
        fuel_energy_not_in_1_2: float
        upstream_transport: float
        waste_operations: float
        business_travel: float
        employee_commuting: float
        upstream_leased: float
        downstream_transport: float
        processing_of_sold: float
        use_of_sold: float
        eol_of_sold: float
        downstream_leased: float
        franchises: float
        investments: float
    base_year_total: float
    target:
      scope_1_2_reduction_pct: float
      scope_3_reduction_pct: float
      target_year: int
      sbti: yes | submitted | validated | no
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


SCOPE_3_CATEGORIES = [
    ("purchased_goods_services", "1. Purchased goods & services"),
    ("capital_goods", "2. Capital goods"),
    ("fuel_energy_not_in_1_2", "3. Fuel & energy (not in 1 or 2)"),
    ("upstream_transport", "4. Upstream transport & distribution"),
    ("waste_operations", "5. Waste in operations"),
    ("business_travel", "6. Business travel"),
    ("employee_commuting", "7. Employee commuting"),
    ("upstream_leased", "8. Upstream leased assets"),
    ("downstream_transport", "9. Downstream transport & distribution"),
    ("processing_of_sold", "10. Processing of sold products"),
    ("use_of_sold", "11. Use of sold products"),
    ("eol_of_sold", "12. End-of-life of sold products"),
    ("downstream_leased", "13. Downstream leased assets"),
    ("franchises", "14. Franchises"),
    ("investments", "15. Investments"),
]


def render(spec: dict) -> str:
    unit = spec.get("unit", "tCO2e")
    inv = spec.get("inventory", {}) or {}
    s1 = inv.get("scope_1", 0) or 0
    s2_loc = inv.get("scope_2_location_based", 0) or 0
    s2_mkt = inv.get("scope_2_market_based", 0) or 0
    s3 = inv.get("scope_3", {}) or {}
    s3_total = sum(v for v in s3.values() if isinstance(v, (int, float)))
    total_loc = s1 + s2_loc + s3_total
    total_mkt = s1 + s2_mkt + s3_total

    out = []
    out.append(f"# Emissions summary — {spec.get('company', '')}\n\n")
    out.append(f"_Reporting year: **{spec.get('reporting_year', '')}**. Unit: {unit}._\n\n")

    out.append("## Scope breakdown\n\n")
    out.append(f"| Scope | {unit} | Share |\n")
    out.append("|-------|-------|-------|\n")
    out.append(f"| Scope 1 | {s1:,.0f} | {100*s1/total_loc:.1f}% |\n")
    out.append(f"| Scope 2 (location-based) | {s2_loc:,.0f} | {100*s2_loc/total_loc:.1f}% |\n")
    out.append(f"| Scope 2 (market-based) | {s2_mkt:,.0f} | _(market-based not counted in total)_ |\n")
    out.append(f"| Scope 3 | {s3_total:,.0f} | {100*s3_total/total_loc:.1f}% |\n")
    out.append(f"| **Total (location-based)** | **{total_loc:,.0f}** | 100% |\n")
    out.append(f"| Total (market-based) | {total_mkt:,.0f} | |\n\n")

    if s3_total > 0:
        out.append("## Scope 3 by category\n\n")
        s3_sorted = sorted(
            [(label, s3.get(key, 0) or 0) for key, label in SCOPE_3_CATEGORIES],
            key=lambda x: -x[1],
        )
        out.append(f"| Category | {unit} | Share of Scope 3 |\n")
        out.append("|----------|-------|-----------------|\n")
        for label, val in s3_sorted:
            if val > 0:
                out.append(f"| {label} | {val:,.0f} | {100*val/s3_total:.1f}% |\n")
        out.append("\n")

        top_two = s3_sorted[:2]
        top_share = sum(v for _, v in top_two) / s3_total
        out.append(f"_Note: top 2 Scope 3 categories ({', '.join(l for l, _ in top_two)}) account for {top_share*100:.0f}% of Scope 3 emissions._\n\n")

    base_total = spec.get("base_year_total")
    base_year = spec.get("base_year")
    if base_total:
        delta = (total_loc - base_total) / base_total * 100
        sign = "+" if delta >= 0 else ""
        out.append(f"## vs. base year ({base_year})\n\n")
        out.append(f"- Base year total: {base_total:,.0f} {unit}\n")
        out.append(f"- Current total: {total_loc:,.0f} {unit}\n")
        out.append(f"- Change: **{sign}{delta:.1f}%**\n\n")

    target = spec.get("target", {}) or {}
    if target:
        out.append("## Targets\n\n")
        if target.get("scope_1_2_reduction_pct") is not None:
            out.append(f"- Scope 1+2 reduction: **{target['scope_1_2_reduction_pct']}%** by {target.get('target_year', 'unspecified')} vs. base year\n")
        if target.get("scope_3_reduction_pct") is not None:
            out.append(f"- Scope 3 reduction: **{target['scope_3_reduction_pct']}%** by {target.get('target_year', 'unspecified')} vs. base year\n")
        out.append(f"- SBTi status: **{target.get('sbti', 'unspecified')}**\n\n")

    out.append("## Observations\n\n")

    if s3_total > total_loc * 0.5:
        out.append("- ⚠️ Scope 3 is more than 50% of total emissions. Scope 3 targets and reduction plan are essential for credible strategy.\n")
    if s3_total > total_loc * 0.4 and target.get("scope_3_reduction_pct") is None:
        out.append("- ⚠️ Scope 3 exceeds 40% threshold but no Scope 3 target stated. SBTi requires it; CSRD expects it.\n")
    if s2_loc != s2_mkt:
        out.append("- ℹ️ Location-based and market-based Scope 2 differ — likely renewable energy procurement is reducing market-based number. Both should be disclosed.\n")
    if base_total and total_loc > base_total * 0.95 and target.get("scope_1_2_reduction_pct", 0) > 0:
        out.append("- ⚠️ Emissions have not yet declined meaningfully against base year. Verify the strategy's annual reduction trajectory will hit the target.\n")

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
