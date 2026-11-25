"""Fridge Roast entry: print the one-line smart-fridge roast.

The roast lives in output/entry.txt so the joke stays editable without
touching the runner. This module only loads it, checks the bounty cap
(a single line, at most 200 characters), and prints it.
"""

from pathlib import Path

MAX_CHARS = 200


def load_roast() -> str:
    entry_path = Path(__file__).resolve().parent / "output" / "entry.txt"
    line = entry_path.read_text(encoding="utf-8").strip()
    if not line:
        raise ValueError("output/entry.txt is empty")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, cap is {MAX_CHARS}")
    return line


def main() -> None:
    print(load_roast())


if __name__ == "__main__":
    main()
