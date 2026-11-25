#!/usr/bin/env python3
"""Museum of the Year 3000 — one-line museum label.

Writes a single museum label, as a museum in the year 3000 would place
beside an ordinary object from today, to /output/entry.txt.

Deterministic: no network, no randomness, no environment input.
The text is a fixed constant.
"""

import os

ENTRY = "Group chat, c. 2025. Forty-seven humans, one shared silence, and a single 'k' that ended a friendship."

OUTPUT_PATH = "/output/entry.txt"


def self_check(text: str) -> None:
    """Gate: the entry must pass the competition's gate on its own terms.

    Runs before writing; raises AssertionError on any violation.
    Does not alter the text.
    """
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 characters, got {len(text)}"
    assert text.strip() != "", "entry must not be only white space"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), "entry must not contain control characters"
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    self_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify what was written, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written output differs from ENTRY"
    self_check(written)


if __name__ == "__main__":
    main()
