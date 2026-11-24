#!/usr/bin/env python3
"""Write one debugging haiku to /output/entry.txt.

The haiku is held as three plain lines. main() joins them with a
single newline between lines, checks the result is inside the
gate (1-200 characters, not only whitespace), and writes it out
as UTF-8 with a trailing newline.
"""

import os

HAIKU_LINES = [
    "cursor blinks at three",
    "the log lines keep scrolling past",
    "it was a comma",
]

OUTPUT_PATH = "/output/entry.txt"


def build_text(lines):
    """Join the haiku lines into the entry text."""
    return "\n".join(lines) + "\n"


# Syllable counts for every word in the haiku, in line order.
# Kept explicit so the shape is checked, not assumed.
EXPECTED_SYLLABLES = (5, 7, 5)

SYLLABLES = {
    "cursor": 2, "blinks": 1, "at": 1, "three": 1,
    "the": 1, "log": 1, "lines": 1, "keep": 1, "scrolling": 2, "past": 1,
    "it": 1, "was": 1, "a": 1, "comma": 2,
}


def count_syllables(line):
    """Count a line's syllables from the per-word table above."""
    total = 0
    for word in line.split():
        if word not in SYLLABLES:
            raise ValueError(f"no syllable count for word {word!r}")
        total += SYLLABLES[word]
    return total


def validate_haiku(lines):
    """Check the haiku is three lines in the 5-7-5 shape."""
    if len(lines) != 3:
        raise ValueError(f"haiku needs 3 lines, got {len(lines)}")
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        got = count_syllables(line)
        if got != expected:
            raise ValueError(
                f"line {line!r} has {got} syllables, expected {expected}"
            )


def main():
    validate_haiku(HAIKU_LINES)
    text = build_text(HAIKU_LINES)
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, gate needs 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
