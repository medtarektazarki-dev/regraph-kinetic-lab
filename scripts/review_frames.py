#!/usr/bin/env python3
"""Extract entry, midpoint, and exit frames for each beat using FFmpeg."""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("--beats", required=True, type=Path, help="JSON beat sheet")
    parser.add_argument("--out", required=True, type=Path, help="Output directory for PNG frames")
    parser.add_argument("--ffmpeg", default="ffmpeg", help="FFmpeg executable")
    args = parser.parse_args()

    ffmpeg = shutil.which(args.ffmpeg)
    if not ffmpeg:
        print(f"FFmpeg executable not found: {args.ffmpeg}", file=sys.stderr)
        return 2
    if not args.video.is_file():
        print(f"Video not found: {args.video}", file=sys.stderr)
        return 2
    try:
        data = json.loads(args.beats.read_text(encoding="utf-8"))
        beats = data["beats"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"Invalid beat sheet: {exc}", file=sys.stderr)
        return 2
    if not isinstance(beats, list) or not beats:
        print("Beat sheet must contain a non-empty beats array", file=sys.stderr)
        return 2

    args.out.mkdir(parents=True, exist_ok=True)
    count = 0
    for index, beat in enumerate(beats, start=1):
        try:
            start = int(beat["start_frame"])
            end = int(beat["end_frame"])
            name = str(beat.get("name", f"beat-{index:02d}"))
        except (KeyError, TypeError, ValueError) as exc:
            print(f"Invalid frame range in beat {index}: {exc}", file=sys.stderr)
            return 2
        if start < 0 or end <= start:
            print(f"Invalid frame range in beat {index}: [{start}, {end})", file=sys.stderr)
            return 2
        safe_name = "".join(char.lower() if char.isalnum() else "-" for char in name).strip("-")
        samples = [("entry", start), ("middle", start + (end - start - 1) // 2), ("exit", end - 1)]
        seen = set()
        for label, frame in samples:
            if frame in seen:
                continue
            seen.add(frame)
            output = args.out / f"{index:02d}-{safe_name}-{label}-f{frame:05d}.png"
            select_filter = f"select=eq(n\\,{frame})"
            command = [ffmpeg, "-hide_banner", "-loglevel", "error", "-i", str(args.video),
                       "-vf", select_filter, "-frames:v", "1", "-y", str(output)]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode != 0 or not output.exists():
                detail = result.stderr.strip() or "frame was not produced"
                print(f"Failed to extract frame {frame}: {detail}", file=sys.stderr)
                return 1
            print(output)
            count += 1
    print(f"Extracted {count} frame(s) to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
