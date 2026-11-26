"""Entry for make.fun's "Funniest One-Line Out-of-Office Reply" bounty.

Writes the winning one-line out-of-office reply to /output/entry.txt.
"""

WINNER = "Your email is important to me, which is why I'm forwarding it to Future Me, who also won't answer today."


def main():
    entry = WINNER
    if not (1 <= len(entry) <= 200) or not entry.strip():
        raise ValueError("entry must be 1-200 characters and not only whitespace")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
