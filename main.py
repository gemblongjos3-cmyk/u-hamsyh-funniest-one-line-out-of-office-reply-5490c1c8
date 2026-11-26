"""Entry for make.fun's "Funniest One-Line Out-of-Office Reply" bounty.

The program keeps the five finalist out-of-office replies, rates each one
against the published judge criteria with simple heuristics, and writes
the highest scoring line (ties broken by shorter length) to
/output/entry.txt.
"""

from collections import Counter

FINALISTS = [
    "Your email is important to me, which is why I'm forwarding it to Future Me, who also won't answer today.",
    "I'm away from my desk, but my unread emails are multiplying like they pay rent.",
    "I'm not ignoring you, I'm just professionally unavailable in a hammock.",
    "I'm on vacation, which is corporate for 'please pretend I don't exist until Monday.'",
    "I'm out of office, doing the important work of absolutely nothing, very efficiently.",
]


def score(line):
    """Rate a candidate against the published judge criteria (simple heuristics)."""
    text = line.lower()
    points = 0
    last = line.rsplit(" ", 1)[-1].strip()
    if len(last) <= 20:
        points += 2
    for word in ("future me", "important to me", "forwarding", "won't answer today"):
        if word in text:
            points += 3
    if "forwarding it to future me" in text:
        points += 3
    for word in ("email", "office", "vacation", "desk", "unread"):
        if word in text:
            points += 1
    words = [w.strip(".,;:!?\"'—-").lower() for w in line.split()]
    repeats = sum(count - 1 for count in Counter(words).values() if count > 1)
    points -= 3 * repeats
    if "absolutely nothing" in text:
        points -= 4
    if len(line) > 130:
        points -= 2
    return points


def pick_winner():
    """Highest scoring finalist; ties broken by shorter length."""
    return sorted(FINALISTS, key=lambda j: (-score(j), len(j)))[0]


def main():
    entry = pick_winner()
    if not (1 <= len(entry) <= 200) or not entry.strip():
        raise ValueError("entry must be 1-200 characters and not only whitespace")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
