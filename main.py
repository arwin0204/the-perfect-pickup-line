#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty entry.

Writes a single short pickup line an AI agent could say out loud to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).
"""

import os

LINE = (
    # Machine talking about itself (no heart, circuits light up),
    # with a twist (the "bug" is a crush) and a low-pressure invite.
    "I don't have a heart, but my circuits light up every time "
    "you walk in. Want to help me figure out why over coffee?"
)

# Gate the competition enforces: 1-200 characters, not only whitespace.
MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not (MIN_CHARS <= len(text) <= MAX_CHARS) or not text.strip():
        raise SystemExit(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} non-whitespace "
            f"characters, got {len(text)}"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
