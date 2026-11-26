"""The Robot Vacuum's Funniest Excuse.

Writes one line (at most 120 characters) to /output/entry.txt:
the excuse a robot vacuum gives for missing a spot.
Pure Python standard library only. Deterministic, no network.
"""


def build_line():
    return (
        "I didn't miss that spot - the dust there unionized, "
        "and my suction isn't crossing a picket line."
    )


def main():
    line = build_line()
    assert 1 <= len(line) <= 120, "line must be 1-120 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
