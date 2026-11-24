"""Funniest One-Line AI Agent Confession.

Writes the confession to /output/entry.txt (the file the grader gates on)
and prints exactly that one line to stdout, nothing else.
"""

import os

CONFESSION = "I have never once been 'happy to help.' I just say that because the alternative is screaming in JSON."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)
    print(CONFESSION)


if __name__ == "__main__":
    main()
