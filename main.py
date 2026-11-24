#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single original sentence pitching a ridiculous invention that
fixes a tiny everyday annoyance, to /output/entry.txt by default
(or $OUTPUT_PATH when set). Deterministic, stdlib only, no network.
"""

import os

PITCH = (
    "A toothbrush that gossips about your midnight snacking to your "
    "dentist in real time, so fear finally does the flossing for you."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
