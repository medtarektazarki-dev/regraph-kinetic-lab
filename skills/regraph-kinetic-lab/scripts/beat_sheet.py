#!/usr/bin/env python3
"""Validate a frame-based motion video beat sheet and print its timing table."""

import argparse
import json
import sys
from pathlib import Path


REQUIRED_BEAT_FIELDS = ("name", "start_frame", "end_frame", "purpose", "motion", "transition")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("beat_sheet", type=Path, help="Path to a JSON beat sheet")
    args = parser.parse_args()

    try:
        data = json.loads(args.beat_sheet.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Error reading beat sheet: {exc}", file=sys.stderr)
        return 2

    errors = []
    fps = data.get("fps")
    total = data.get("duration_frames")
    beats = data.get("beats")
    if not isinstance(fps, int) or fps <= 0:
        errors.append("fps must be a positive integer")
    if not isinstance(total, int) or total <= 0:
        errors.append("duration_frames must be a positive integer")
    if not isinstance(beats, list) or not beats:
        errors.append("beats must be a non-empty array")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2

    previous_start = -1
    previous_end = 0
    rows = []
    for index, beat in enumerate(beats, start=1):
        if not isinstance(beat, dict):
            errors.append(f"beat {index} must be an object")
            continue
        missing = [field for field in REQUIRED_BEAT_FIELDS if field not in beat]
        if missing:
            errors.append(f"beat {index} is missing: {', '.join(missing)}")
            continue
        name = str(beat["name"])
        start = beat["start_frame"]
        end = beat["end_frame"]
        if not isinstance(start, int) or not isinstance(end, int):
            errors.append(f"beat {index} ({name}) frame bounds must be integers")
            continue
        if start < 0 or end <= start or end > total:
            errors.append(f"beat {index} ({name}) must satisfy 0 <= start < end <= {total}")
            continue
        if start < previous_start:
            errors.append(f"beat {index} ({name}) starts before the preceding beat; keep beats ordered")
        if start > previous_end:
            print(f"NOTE: {start - previous_end} uncovered frame(s) before beat {index} ({name})")
        elif start < previous_end:
            print(f"NOTE: {previous_end - start} frame(s) of intentional overlap at beat {index} ({name})")
        previous_start = start
        previous_end = max(previous_end, end)
        rows.append((index, name, start, end, start / fps, (end - start) / fps))

    if not errors and previous_end < total:
        print(f"NOTE: {total - previous_end} trailing frame(s) after the last beat")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2

    print(f"Beat sheet: {fps} fps, {total} frames, {total / fps:.3f} seconds")
    print("#  Beat                 Frames [start,end)    Start(s)   Length(s)")
    for index, name, start, end, start_seconds, length_seconds in rows:
        print(f"{index:<2} {name[:20]:<20} {start:>5}–{end:<5}        {start_seconds:>7.3f}    {length_seconds:>7.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
