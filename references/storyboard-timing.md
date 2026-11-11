# Storyboard and timing

## Beat sheet

Use `assets/beat-sheet.example.json`. Each beat has a name, start frame (inclusive), end frame (exclusive), purpose, copy, motion, and transition. The composition has one frame rate and total frame count. Frame numbers—not decimal seconds—are the final timing authority.

Compute seconds as `frames / fps`. For a continuous full-length sequence, the first beat begins at frame 0 and the final beat ends at `duration_frames`. If transitions overlap, encode the overlap deliberately and note it; do not let accidental gaps or overlaps emerge from rounded seconds.

## Reading and pacing

- Match time to the amount and complexity of on-screen copy. A short headline can land quickly; multi-line copy needs a readable hold.
- Establish an opening hook, develop the idea, deliver a strongest moment, and resolve the brand/message.
- Give each beat a reason to exist. Avoid static holds that outlast reading, but allow a purposeful end-card hold.
- If audio is used, align major transitions to measured musical or speech events rather than guessed BPM.
- Validate safe areas against the chosen platform and placement; platform UI guidance changes and ad guidance may differ from organic content.
