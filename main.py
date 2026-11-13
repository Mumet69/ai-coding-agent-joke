#!/usr/bin/env python3
# ai-joke-03 entry (Python 3.13, standard library only).
#
# Writes one fixed one-liner about AI coding agents to /output/entry.txt
# (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
# The joke is fixed at build time: both runs write the same bytes.
# Gate: 126 UTF-8 characters, 1-280, not only white space.

import os
from pathlib import Path

JOKE = (
    "My coding agent imported a library that doesn't exist, "
    "wrote its documentation, and when I asked, it said, "
    "\"It's in the docs.\""
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    Path(output_dir, "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
