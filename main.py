#!/usr/bin/env python3
"""Six Words to a Payday — make.fun bounty entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt, exactly as the gate requires: UTF-8 text, 1-60
characters, not only whitespace.
"""

import os

STORY = "Payday arrived. So did my replacement."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file is exactly the 38-byte story.
    # Ranking breaks exact ties on fewer bytes, so every byte counts.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)


if __name__ == "__main__":
    main()
