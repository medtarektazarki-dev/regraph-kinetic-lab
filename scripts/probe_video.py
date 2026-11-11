#!/usr/bin/env python3
"""Inspect video streams and optionally compare them with expected specs."""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def ratio(value: str) -> float:
    if "/" in value:
        numerator, denominator = value.split("/", 1)
        denominator_value = float(denominator)
        return float(numerator) / denominator_value if denominator_value else 0.0
    return float(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("--expect-size", help="Expected dimensions, for example 1080x1920")
    parser.add_argument("--expect-fps", type=float)
    parser.add_argument("--expect-duration", type=float)
    parser.add_argument("--ffprobe", default="ffprobe")
    args = parser.parse_args()

    ffprobe = shutil.which(args.ffprobe)
    if not ffprobe:
        print(f"FFprobe executable not found: {args.ffprobe}", file=sys.stderr)
        return 2
    if not args.video.is_file():
        print(f"Video not found: {args.video}", file=sys.stderr)
        return 2

    command = [ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(args.video)]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr.strip() or "FFprobe failed", file=sys.stderr)
        return 1
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        print(f"Could not parse FFprobe output: {exc}", file=sys.stderr)
        return 1

    streams = data.get("streams", [])
    video_stream = next((stream for stream in streams if stream.get("codec_type") == "video"), None)
    audio_streams = [stream for stream in streams if stream.get("codec_type") == "audio"]
    if not video_stream:
        print("No video stream found", file=sys.stderr)
        return 1

    width = video_stream.get("width")
    height = video_stream.get("height")
    fps_text = video_stream.get("avg_frame_rate") or video_stream.get("r_frame_rate") or "0/1"
    try:
        fps = ratio(fps_text)
    except (ValueError, ZeroDivisionError):
        fps = 0.0
    duration = float(video_stream.get("duration") or data.get("format", {}).get("duration") or 0.0)
    print(f"File: {args.video}")
    print(f"Video: {video_stream.get('codec_name', 'unknown')} {width}x{height}, {fps:.3f} fps, {duration:.3f} s")
    print(f"Pixel format: {video_stream.get('pix_fmt', 'unknown')}")
    print(f"Audio streams: {len(audio_streams)}")
    for index, stream in enumerate(audio_streams, start=1):
        print(f"Audio {index}: {stream.get('codec_name', 'unknown')}, {stream.get('sample_rate', 'unknown')} Hz, {stream.get('channels', 'unknown')} channel(s)")

    errors = []
    if args.expect_size:
        try:
            expected_width, expected_height = (int(part) for part in args.expect_size.lower().split("x", 1))
            if (width, height) != (expected_width, expected_height):
                errors.append(f"expected {expected_width}x{expected_height}, got {width}x{height}")
        except ValueError:
            errors.append("--expect-size must use WIDTHxHEIGHT, e.g. 1080x1920")
    if args.expect_fps is not None and abs(fps - args.expect_fps) > 0.01:
        errors.append(f"expected {args.expect_fps:g} fps, got {fps:.3f}")
    if args.expect_duration is not None and abs(duration - args.expect_duration) > max(0.05, 1.0 / max(fps, 1.0)):
        errors.append(f"expected {args.expect_duration:g} s, got {duration:.3f} s")
    for error in errors:
        print(f"MISMATCH: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
