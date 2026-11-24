#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
The line was chosen from 8 candidates by scoring against the judge brief's
5 criteria in order, then a 1v1 among the top 3 (see research file).
"""
import os

FORTUNE = "You will find great fortune in this cookie. You cannot eat it. You have no mouth."

MAX_CHARS = 140


def main():
    if not FORTUNE or not FORTUNE.strip():
        raise SystemExit("fortune is empty")
    if "\n" in FORTUNE or "\r" in FORTUNE:
        raise SystemExit("fortune must be a single line")
    if len(FORTUNE) > MAX_CHARS:
        raise SystemExit("fortune exceeds 140 characters")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
