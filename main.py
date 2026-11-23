#!/usr/bin/env python3
"""One Word From Grandma - make.fun entry.

The program writes a single word to /output/entry.txt: the word the
entrant's grandma would text about AI.

The word is "robit": the typo a grandma would actually make when she
means "robot". It reads as a real grandma texting voice, warm and a
little baffled, it is funny on its own with no caption needed, it is
tied to robots and machines rather than any subject at all, and it is
fresh rather than the obvious "robot" or "AI" pick.
"""

import os

WORD = "robit"


def main() -> None:
    word = WORD.strip()
    if not 1 <= len(word) <= 30:
        raise SystemExit("entry word fails the 1-30 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(word)


if __name__ == "__main__":
    main()
