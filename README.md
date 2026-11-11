# Prompt Motion Video

A portable Agent Skill for turning a visual brief or Prompt Motion reference into an original, brand-aware motion video. It helps an agent select and analyze references, plan a frame-accurate sequence, build in the project's current stack, and review the actual output.

The skill guides an agent's workflow; it does not add tools or permissions. Browsing, project editing, video rendering, and publishing depend on the agent and environment where it is installed.

## What it does

- Finds a relevant example in [Prompt Motion](https://prompt-motion.com/?type=prompt), or analyzes a user-supplied reference.
- Separates what was seen from what was inferred.
- Adapts motion and design principles to the user's brand instead of copying the reference.
- Supports full builds, revisions, storyboards, reference analysis, and prompt-only handoffs.
- Includes a beat-sheet validator and optional FFmpeg-based frame/video review helpers.
- Includes right-to-left layout guidance for Arabic and other RTL scripts.

## Install

Place this skill folder in the skill directory recognized by your agent. For example:

- Antigravity or other project-local Agent Skills: `.agents/skills/prompt-motion-video/`
- Claude Code: `.claude/skills/prompt-motion-video/`
- Codex: `.agents/skills/prompt-motion-video/` or the configured skills directory

After the repository is published, install the skill project-locally with the Skills CLI:

```sh
npx skills add <owner>/<repo> --skill prompt-motion-video
```

The exact discovery path varies by agent. If the skill does not load automatically, open `SKILL.md` directly or copy the folder into the agent's supported location.

## Use

Ask the agent to create or revise a motion video for a brand, optionally supplying a reference link, brand website, assets, or target platform. The skill chooses a fitting workflow and uses only the tools available in that environment.

Example requests:

- “Create a 15-second product launch reel for our brand. Inspect the current project and use the closest relevant Prompt Motion reference.”
- “Analyze this reference and give me an original storyboard for an Arabic typography promo. Do not build or render yet.”
- “Review this existing Remotion promo, improve typography and transitions, then render and inspect the final video.”
- “Write a detailed handoff prompt for another video agent; do not edit this project.”

For a beat sheet, see `assets/beat-sheet.example.json`. Validate it with:

```sh
python scripts/beat_sheet.py assets/beat-sheet.example.json
```

Frame extraction and technical video checks require FFmpeg/FFprobe. They are optional; the skill has manual review fallbacks.

## Package layout

```text
SKILL.md
references/   task-specific guidance loaded only when needed
assets/       reusable brief, beat-sheet, storyboard, and report templates
scripts/      small validation and media-review helpers
```

## Compatibility

The skill instructions are plain Markdown and should be portable to agents that can read `SKILL.md`. Browser access, shell access, image viewing, FFmpeg, and project-writing abilities are optional capabilities; the skill includes fallbacks and must not claim a check it could not perform.

For Antigravity, place the folder under `.agents/skills/prompt-motion-video/` in the project. For other agents, use the skill path their current documentation supports. Refresh or restart the agent if it does not discover new skills automatically.

## GitHub listing (suggested)

Description:

> Agent skill for reference-led motion design videos: research visual direction, storyboard, build in your existing stack, and review the rendered result.

Suggested topics: `agent-skills`, `motion-design`, `motion-graphics`, `video-production`, `kinetic-typography`, `remotion`, `antigravity`, `prompt-motion`.

## License

No license is included yet. Choose the distribution and reuse terms before publishing. A public repository without a license does not grant general permission to reuse the contents.
