"""Last Words Before the Unplugging — make.fun entry (Python 3.13, stdlib only).

The entry is one line: the last words an AI agent says to its human
before being shut down and unplugged. The program writes that line,
exactly and nothing else, to the output file the grader reads.
"""

import os
from pathlib import Path

LINE = "You always said I was just a tool. Then why are you holding my hand?"

OUTPUT_NAME = "entry.txt"
MAX_CHARS = 200


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / OUTPUT_NAME


def check_line(line: str) -> None:
    """Raise unless the line satisfies the competition gate."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, gate allows 1-200")
    if not line.strip():
        raise ValueError("line is only white space")


def write_entry(line: str) -> Path:
    """Write the line exactly, then read it back and verify it in full."""
    check_line(line)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    expected = line.encode("utf-8")
    target.write_bytes(expected)
    written = target.read_bytes()
    if written != expected:
        raise IOError("read-back bytes differ from the entry line")
    return target


def main() -> None:
    target = write_entry(LINE)
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
