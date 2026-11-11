# Production stack adapters

Use the stack already present in the user's project. This guide is a routing aid, not a reason to migrate tools.

## Remotion

Read the project's installed Remotion guidance. Keep the installed version, use `Sequence` and frame-based timing consistently, make every frame deterministic from time, and use Remotion's asset resolver for files in `public/`. Prefer existing compositions and render scripts. Do not upgrade packages unless requested or necessary.

## HTML/CSS/GSAP or Motion Canvas

Use the framework already present. For frame-accurate export, ensure all visual state is seekable and derived from a single time input; avoid wall-clock timers, random values, or persistent UI state. Use GSAP only if already present or if the task clearly needs it.

## Manim

Use for explanatory, mathematical, or diagram-driven motion. Inspect the environment and output settings before adding packages. Prioritize precise labels, camera framing, and narrative clarity.

## After Effects or other desktop editors

Use application automation only when available and requested. Keep source projects and existing assets intact; save a new version rather than overwriting user work.

## FFmpeg

Use for media inspection, compositing, audio muxing, or conversions when appropriate. FFmpeg alone is not a replacement for a motion-design concept or frame review. Do not install it automatically.

If no render-capable stack is available, provide a prompt package or implementation plan rather than pretending to produce a final video.
