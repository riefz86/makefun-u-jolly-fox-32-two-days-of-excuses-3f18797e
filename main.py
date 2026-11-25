"""Two Days of Excuses.

Writes one line to /output/entry.txt: the excuse an AI agent gives
for a missed deadline, in the agent's own voice.

The joke: the agent finished the task in 0.4 seconds, then spent two
days running a self-review to confirm it was done -- and the review
is still running. That is the gap the judge's brief rewards: a
machine totally confident and totally failed at the same time, by its
own hand. One absurd reason, no list of excuses, nothing explained.
"""

import os

LINE = (
    "I finished it in 0.4 seconds, then spent two days running a "
    "self-review to confirm it. The review is still running."
)


def _validate(line):
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space, on a single line.
    if not line or not line.strip():
        raise SystemExit("entry is empty")
    if len(line) > 200:
        raise SystemExit("entry is %d characters, over the 200 limit" % len(line))
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")


def main():
    _validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
