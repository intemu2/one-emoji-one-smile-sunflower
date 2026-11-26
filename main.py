"""One Emoji, One Smile - sunflower entry for Firt / intemu2.

Choice: U+1F33B SUNFLOWER. It is warm at first glance, universally
read as kind and cheerful, intentionally chosen over the first generic
smiley, and safe coming from a stranger: a flower, no face, no hug,
no intimacy, no sarcasm, no flirtation. See ANALYSIS.md for the
head-to-head scoring against the judge's five criteria in order.

The program is deliberately offline and dependency-free: it only
writes four UTF-8 bytes to /output/entry.txt, with no trailing
newline, space, or extra output.
"""

from pathlib import Path

# U+1F33B SUNFLOWER, written as an escape so the source stays plain ASCII
# and the output is exactly one Unicode character.
EMOJI = "\U0001F33B"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(EMOJI.encode("utf-8"))


if __name__ == "__main__":
    main()
