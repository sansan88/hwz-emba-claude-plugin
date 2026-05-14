#!/usr/bin/env python3
"""
practice_tracker.py — Maintain a simple daily self-leadership practice log,
with weekly and 8-week summary reports.

Usage:
    python practice_tracker.py log [--date YYYY-MM-DD] [--minutes N] [--practice NAME] [--notes "..."]
    python practice_tracker.py report [--last-weeks N]

Stores log in ~/.self_leadership_log.json by default; pass --file to override.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta
from pathlib import Path


DEFAULT_LOG = Path.home() / ".self_leadership_log.json"


def load_log(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_log(path: Path, entries: list[dict]) -> None:
    path.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")


def cmd_log(args: argparse.Namespace) -> int:
    path = Path(args.file)
    entries = load_log(path)
    today = args.date or date.today().isoformat()
    entry = {
        "date": today,
        "minutes": args.minutes,
        "practice": args.practice or "breathing",
        "notes": args.notes or "",
    }
    entries = [e for e in entries if e["date"] != today]
    entries.append(entry)
    entries.sort(key=lambda e: e["date"])
    save_log(path, entries)
    print(f"Logged practice on {today}: {entry['minutes']} min of {entry['practice']}")
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    path = Path(args.file)
    entries = load_log(path)
    if not entries:
        print("No log entries yet. Run with `log` to add one.")
        return 0

    today = date.today()
    weeks = args.last_weeks
    cutoff = today - timedelta(weeks=weeks)
    recent = [e for e in entries if date.fromisoformat(e["date"]) >= cutoff]

    if not recent:
        print(f"No entries in the last {weeks} weeks.")
        return 0

    total_days = weeks * 7
    practiced_days = len(set(e["date"] for e in recent))
    total_minutes = sum(e.get("minutes", 0) for e in recent)
    rate = practiced_days / total_days * 100
    avg_minutes = total_minutes / practiced_days if practiced_days else 0

    print(f"\nSelf-leadership practice report — last {weeks} weeks (cutoff {cutoff.isoformat()})\n")
    print(f"- Days practiced: **{practiced_days} of {total_days}** ({rate:.0f}%)")
    print(f"- Total minutes: **{total_minutes}**")
    print(f"- Average per practice day: **{avg_minutes:.1f} minutes**")

    # Streak detection
    streaks: list[int] = []
    current = 0
    prev = None
    for d in sorted(set(e["date"] for e in entries)):
        d_date = date.fromisoformat(d)
        if prev is not None and (d_date - prev).days == 1:
            current += 1
        else:
            if current > 0:
                streaks.append(current)
            current = 1
        prev = d_date
    if current > 0:
        streaks.append(current)
    longest = max(streaks) if streaks else 0

    # Active streak
    last_date = date.fromisoformat(entries[-1]["date"])
    active = 0
    cursor = today
    practiced_dates = {e["date"] for e in entries}
    while cursor.isoformat() in practiced_dates:
        active += 1
        cursor -= timedelta(days=1)
    print(f"- Longest streak overall: **{longest} days**")
    print(f"- Current active streak: **{active} days**")

    if rate >= 80:
        print("\n✅ The practice is established. Consider deepening — longer sits, retreat, additional practice forms.")
    elif rate >= 50:
        print("\n⚠️ The practice is partially established. Identify what is blocking the missed days.")
    else:
        print("\n❌ The practice is not established. Reduce to the minimum viable version (3 minutes) until consistency is built.")

    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", default=str(DEFAULT_LOG))
    sub = ap.add_subparsers(dest="cmd", required=True)

    log_p = sub.add_parser("log")
    log_p.add_argument("--date", help="YYYY-MM-DD (default: today)")
    log_p.add_argument("--minutes", type=int, default=10)
    log_p.add_argument("--practice", default=None)
    log_p.add_argument("--notes", default=None)
    log_p.set_defaults(func=cmd_log)

    rep_p = sub.add_parser("report")
    rep_p.add_argument("--last-weeks", type=int, default=8)
    rep_p.set_defaults(func=cmd_report)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
