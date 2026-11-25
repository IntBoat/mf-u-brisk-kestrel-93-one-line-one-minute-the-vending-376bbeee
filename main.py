#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest (make.fun).

Writes the entry to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'Are you exact change? Because every time you walk by, my coils turn, my lights hum, and something in me drops for you.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
