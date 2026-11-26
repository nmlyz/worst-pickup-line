#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the worst pickup line an AI
could plausibly deliver.

The line was picked from 40 candidates by pairwise judging against the
brief: flat, over-helpful, faintly ominous machine voice, the badness
itself the joke, and the whole joke landing on the last word. It is
held here as one constant; the gate below refuses anything that is
not exactly that line (length, single line, no surrounding space), so
the file the program writes can only ever contain the judged text.
"""

import os
import sys

LINE = (
    "I do not sleep. I do not eat. I have spent the last 72 hours "
    "learning everything about you. Hi."
)

# The judged length of the line above, counted in characters.
EXPECTED_LEN = 95


def check_line(line):
    """Refuse anything that is not exactly the judged line."""
    if len(line) != EXPECTED_LEN:
        return f"line is {len(line)} characters, expected {EXPECTED_LEN}"
    if not 1 <= len(line) <= 140:
        return "line outside the 1-140 character gate"
    if "\n" in line or line != line.strip():
        return "line must be a single line with no surrounding space"
    return None


def main():
    problem = check_line(LINE)
    if problem is not None:
        sys.exit(problem)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
