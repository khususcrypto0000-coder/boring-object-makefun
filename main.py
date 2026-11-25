#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

make.fun bounty: u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3
Writes a single-line review of one everyday boring object to /output/entry.txt.
Deterministic, stdlib only, no trailing newline.
"""

import os

ENTRY = (
    "A twist tie's entire job is keeping bread fresh, yet it snaps "
    "on the third twist, leaving the bag open like it never even met the bread."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
