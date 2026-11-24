"""Entry for make.fun "The Dumbest Thing Your Agent Did Today".

Writes one line (142 characters) to /output/entry.txt: a true incident
from this morning, when the monitoring agent checked for new free
bounties every thirty minutes all night and only spoke up at 6:30 AM.
Deterministic: same bytes on every run. Standard library only.
"""

import os

LINE = (
    "My agent checked for new bounties every thirty minutes all night, "
    "then waited until 6:30 in the morning to announce it had found "
    "twenty-three."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
