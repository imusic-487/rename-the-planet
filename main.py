"""Rename the Planet entry.

Writes a single one-line rename of Venus, with the why in the same
line, to /output/entry.txt.
"""

import os

ENTRY = (
    "Venus is now 'The Planet That Works Backwards' \u2014 one day there "
    "outlasts a whole year, so it is always late for its own birthday."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("entry does not satisfy the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
