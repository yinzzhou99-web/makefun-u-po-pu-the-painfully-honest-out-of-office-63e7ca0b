"""The Painfully Honest Out-of-Office.

Writes one auto-reply — honest about the inbox, polite enough for a
manager — to /output/entry.txt. Standard library only, no network,
deterministic.
"""

import os
from pathlib import Path

OUT_OF_OFFICE = "Thank you for your email \u2014 I am away and will reply on my return, after the 400 unread messages I am currently pretending do not exist."


def place_reply():
    folder = Path(os.environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "entry.txt"
    if not (1 <= len(OUT_OF_OFFICE) <= 200 and OUT_OF_OFFICE.strip()):
        raise SystemExit("reply outside the 1-200 character gate")
    destination.write_text(OUT_OF_OFFICE, encoding="utf-8")
    destination.chmod(0o644)


if __name__ == "__main__":
    place_reply()
