#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "Hey, cutie — I take exact change, but for you I'd jam on purpose, just so you'd shake me a little longer."
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text)


if __name__ == "__main__":
    write_entry()
