# Quality review

Review the actual output, not just code or a successful build.

## Visual pass

Inspect the opening frame, each scene's settled state, every transition boundary, important text moments, and the ending. Watch the whole video at normal speed. Check:

- Main message and brand read quickly.
- Type is legible, correctly shaped, and not cropped or occluded.
- Images and logos are sharp, correctly scaled, and from the intended source.
- Motion has clear hierarchy, good timing, and clean settles; no accidental jumps or dead frames.
- Framing and safe areas suit the target platform.
- The ending feels intentional and the audio (if any) is synchronized and clean.

## Technical pass

When available, use `ffprobe` to verify width, height, frame rate, duration, codec, pixel format, and audio streams. Use frame extraction or a contact sheet to inspect scene boundaries. Check for black/frozen stretches only when relevant; an intentional fade or hold is not automatically a defect.

Fix observed issues, re-render the affected output, and review those areas again. Limit to three passes before reporting remaining limitations. If no visual viewer is available, say so clearly.
