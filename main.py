"""Fortune in a Pot — make.fun entry.

Writes one line (at most 120 characters) telling a houseplant's fortune
to ``entry.txt`` inside ``MAKEFUN_OUTPUT_DIR`` (fallback ``/output``).

The line is validated before it is written (1-120 characters, not only
whitespace, exactly one line) and verified by reading the file back.
Standard library only.
"""

import os

LINE = (
    "At 7 a.m. you lean so far toward the window the curtain steps aside: "
    "this week, the sun leans back toward you."
)


def main() -> None:
    if not LINE or len(LINE) > 120 or not LINE.strip():
        raise ValueError("fortune must be 1-120 non-blank characters")
    if LINE != LINE.strip():
        raise ValueError("fortune must not start or end with whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("fortune must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("read-back mismatch: entry.txt does not match the fortune")
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
