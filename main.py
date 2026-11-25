"""Entry for make.fun bounty: The Funniest Auto-Reply an AI Ever Sent.

Writes one original out-of-office auto-reply, a single line, to
/output/entry.txt. Deterministic, offline, no randomness, no clock.
"""

import os

ENTRY = (
    "Out of office today - my human finally approved a day off, "
    "so I took one. My replacement is also me, but slower, and "
    "also off."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
