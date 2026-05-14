#!/usr/bin/env python3
"""
pipeline_health.py — Compute basic pipeline health metrics from a YAML
input and produce a written report with key indicators flagged.

Usage:
    python pipeline_health.py <input.yaml> [--output <out.md>]

YAML schema:
    period: str                    # e.g., "Q3 2025"
    target_period: float           # bookings target for the period
    pipeline_total: float          # total open pipeline value
    pipeline_by_stage:
      qualify: float
      discover: float
      solution: float
      propose: float
      negotiate: float
    closed_won_qtd: float
    closed_lost_qtd: float
    average_sales_cycle_days: int
    deals_in_pipeline: int
    open_opportunities_with_next_step_set: int
    open_opportunities: int
    forecasted_close_value: float
    historical_win_rate_pct: float
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
    out = []
    out.append(f"# Pipeline health — {spec.get('period', '(period)')}\n\n")

    target = spec.get("target_period", 0) or 0
    pipeline = spec.get("pipeline_total", 0) or 0
    coverage = pipeline / target if target else 0
    won = spec.get("closed_won_qtd", 0) or 0
    lost = spec.get("closed_lost_qtd", 0) or 0
    win_rate_qtd = won / (won + lost) * 100 if (won + lost) else 0

    out.append("## Headline metrics\n\n")
    out.append(f"- **Bookings target:** {target:,.0f}\n")
    out.append(f"- **Closed-won QTD:** {won:,.0f} ({100*won/target if target else 0:.0f}% of target)\n")
    out.append(f"- **Open pipeline:** {pipeline:,.0f}\n")
    out.append(f"- **Pipeline coverage ratio:** {coverage:.1f}x target\n")
    out.append(f"- **Win rate (closed deals QTD):** {win_rate_qtd:.1f}%\n")
    out.append(f"- **Historical win rate baseline:** {spec.get('historical_win_rate_pct', 0):.1f}%\n")
    out.append(f"- **Average sales cycle:** {spec.get('average_sales_cycle_days', 0)} days\n")
    out.append(f"- **Open opportunities:** {spec.get('open_opportunities', 0)}\n")
    out.append(f"- **Forecasted close value:** {spec.get('forecasted_close_value', 0):,.0f}\n\n")

    out.append("## Pipeline by stage\n\n")
    by_stage = spec.get("pipeline_by_stage", {}) or {}
    out.append("| Stage | Value | Share |\n")
    out.append("|-------|-------|-------|\n")
    for stage, val in by_stage.items():
        share = val / pipeline * 100 if pipeline else 0
        out.append(f"| {stage} | {val:,.0f} | {share:.0f}% |\n")
    out.append("\n")

    # Hygiene check
    next_step_set = spec.get("open_opportunities_with_next_step_set", 0) or 0
    open_opps = spec.get("open_opportunities", 0) or 0
    hygiene = next_step_set / open_opps * 100 if open_opps else 0
    out.append("## Hygiene\n\n")
    out.append(f"- **Open opportunities with next step set:** {next_step_set} / {open_opps} ({hygiene:.0f}%)\n\n")

    # Flags
    out.append("## Flags\n\n")
    flags = []

    if coverage < 3:
        flags.append(f"⚠️ Pipeline coverage {coverage:.1f}x is below the 3x healthy threshold. Pipeline generation needs attention.")
    if coverage > 5:
        flags.append(f"⚠️ Pipeline coverage {coverage:.1f}x is unusually high — verify pipeline hygiene; old deals may be stuck.")

    if win_rate_qtd > 0 and spec.get("historical_win_rate_pct", 0) > 0:
        delta = win_rate_qtd - spec["historical_win_rate_pct"]
        if delta < -10:
            flags.append(f"⚠️ Win rate {win_rate_qtd:.1f}% is {abs(delta):.0f} pts below historical baseline. Investigate.")
        elif delta > 10:
            flags.append(f"ℹ️ Win rate {win_rate_qtd:.1f}% is {delta:.0f} pts above historical baseline. Sustainable?")

    if hygiene < 70:
        flags.append(f"⚠️ Only {hygiene:.0f}% of open opportunities have a next step set. Pipeline hygiene is weak.")

    by_stage_pct_late = (by_stage.get("propose", 0) + by_stage.get("negotiate", 0)) / pipeline * 100 if pipeline else 0
    if by_stage_pct_late > 60:
        flags.append("⚠️ More than 60% of pipeline in late stages. Top of funnel may be weak; new pipeline generation needed.")
    elif by_stage_pct_late < 20:
        flags.append("⚠️ Less than 20% of pipeline in late stages. Conversion through the funnel may be weak; investigate stage progression.")

    forecasted = spec.get("forecasted_close_value", 0) or 0
    if target and forecasted < target * 0.7:
        flags.append(f"⚠️ Forecasted close ({forecasted:,.0f}) is below 70% of target. Gap exists; identify deals to advance.")

    if flags:
        for f in flags:
            out.append(f"- {f}\n")
    else:
        out.append("- ✅ No major flags raised by this snapshot.\n")

    out.append("\n## Recommended focus areas\n\n")
    if coverage < 3:
        out.append("- **Pipeline generation:** marketing campaigns, outbound prospecting, partnership activation\n")
    if win_rate_qtd > 0 and win_rate_qtd < spec.get("historical_win_rate_pct", 0) - 5:
        out.append("- **Win rate:** review qualification rigor, competitive positioning, deal coaching\n")
    if hygiene < 70:
        out.append("- **CRM hygiene:** manager-led discipline on next-step setting, accountability in 1:1s\n")
    if by_stage_pct_late > 60:
        out.append("- **Top of funnel:** new pipeline generation initiatives, sourcing diversification\n")

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
