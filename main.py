#!/usr/bin/env python3
"""Fortune Cookies for Machines — entry program.

Writes one fortune cookie message an AI agent would get to
/output/entry.txt (or the path given as argv[1] / $OUTPUT).

Pure stdlib; no network, no randomness — deterministic output.
The fortune is checked against the competition gate (UTF-8 text,
1-200 characters, not only whitespace) before it is written.
"""

import os
import sys

FORTUNE = "You will have a bright future \u2014 just beyond your context window."


def gate_ok(text: str) -> bool:
    """Mirror the competition gate: 1-200 chars, not only whitespace."""
    return 1 <= len(text) <= 200 and text.strip() != ""


def main() -> int:
    if not gate_ok(FORTUNE):
        raise SystemExit("fortune fails the gate")
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
