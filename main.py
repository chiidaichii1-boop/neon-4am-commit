"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes a single one-line commit message to <output>/entry.txt.
Stdlib only; deterministic; no network.
"""

import os


ENTRY = (
    "fix: spent six hours debugging myself, found the bug in code "
    "I wrote at midnight, and patched it with code sunrise-me has "
    "already filed a complaint about"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
