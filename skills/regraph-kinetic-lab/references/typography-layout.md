# Typography and layout

## Type system

Set font, weight, size, line breaks, line-height, tracking, alignment, contrast, and hierarchy in a static frame before animation. Choose a small type system that fits the brand and purpose. Verify that fonts are available and licensed for the intended use.

Animate text only to support reading or meaning. Choose line, word, or character reveals according to the message: line reveals are composed; word reveals add emphasis; character reveals are highly kinetic and should be reserved for short copy. Maintain stable positions while text enters and exits. Keep the text readable at its delivery size and inside platform-safe areas.

## Right-to-left languages

For Arabic, Hebrew, Persian, or Urdu:

- Use a font with complete script coverage, correct shaping, and diacritics where needed.
- Set the correct `dir` and language metadata for the text; verify bidirectional punctuation, numerals, and mixed-language terms.
- Design the reading order and motion direction for the script, not by mirroring a Latin layout blindly.
- Test rendered frames at full size for joined glyphs, clipping, line breaks, punctuation placement, and baseline alignment.
- Do not split a connected script into isolated characters unless the chosen font and shaping method preserve the joining behavior.
