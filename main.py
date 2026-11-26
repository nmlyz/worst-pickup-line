#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the worst pickup line an AI
could plausibly deliver.

The line was picked from 40 candidates by pairwise judging against the
brief: flat, over-helpful, faintly ominous machine voice, the badness
itself the joke, and the whole joke landing on the last word. It is
held here as one constant; the validators below refuse anything that
is not exactly that line (length, shape, character set), so the file
the program writes can only ever contain the judged text.
"""

import os
import sys

LINE = (
    "I do not sleep. I do not eat. I have spent the last 72 hours "
    "learning everything about you. Hi."
)

# The judged length of the line above, counted in characters.
EXPECTED_LEN = 95

# Entry gate from the brief: a single line of 1-140 characters.
MIN_LEN = 1
MAX_LEN = 140

OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def check_length(line):
    """Return a problem string if the line length is wrong, else None."""
    if len(line) != EXPECTED_LEN:
        return f"line is {len(line)} characters, expected {EXPECTED_LEN}"
    if not MIN_LEN <= len(line) <= MAX_LEN:
        return f"line outside the {MIN_LEN}-{MAX_LEN} character gate"
    return None


def check_shape(line):
    """Return a problem string if the line is not one clean line."""
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if line != line.strip():
        return "line must have no leading or trailing space"
    return None


def check_characters(line):
    """Return a problem string if the line has unexpected characters."""
    for ch in line:
        if ord(ch) < 0x20 or ord(ch) > 0x7E:
            return f"line contains unexpected character U+{ord(ch):04X}"
    return None


def check_content(line):
    """Return a problem if the judged line's key beats are missing.

    The joke lands on the last word, so the line must end with "Hi.";
    internal spacing must be single spaces throughout.
    """
    if not line.endswith("Hi."):
        return 'line must end with "Hi."'
    if "  " in line:
        return "line must not contain double spaces"
    return None


def validate_line(line):
    """Run every validator; return the first problem found, else None."""
    for check in (check_length, check_shape, check_characters, check_content):
        problem = check(line)
        if problem is not None:
            return problem
    return None


def build_output(line):
    """Encode the line as its exact file bytes (line plus newline)."""
    return (line + "\n").encode("utf-8")


def resolve_output_path():
    """Return the path of the entry file from env or the default."""
    out_dir = os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_DIR)
    return os.path.join(out_dir, OUTPUT_NAME)


def write_entry(path, data):
    """Write data to path and confirm the bytes round-trip exactly."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")


def main():
    problem = validate_line(LINE)
    if problem is not None:
        sys.exit(problem)
    path = resolve_output_path()
    data = build_output(LINE)
    write_entry(path, data)
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
