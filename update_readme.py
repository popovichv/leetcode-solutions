"""Regenerate the Solved table in README.md from the files in problems/.

Each problem file is the single source of truth for its row:

    # 14. Longest Common Prefix        ->  number, title
    **Difficulty:** `Easy`             ->  difficulty
    **Topics:** `String`               ->  topics
    Time complexity: `O(s*m)`, where   ->  time
    Space complexity: `O(m)`           ->  space

When a problem documents several methods, the last one under `## Code` feeds
the table, so each file should build up to its preferred solution.

Usage:
    py update_readme.py            rewrite the table
    py update_readme.py --check    exit 1 if the table is out of date
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROBLEMS_DIR = ROOT / "problems"
README = ROOT / "README.md"

HEADING_RE = re.compile(r"^#\s+(\d+)\.\s+(.+?)\s*$")
META_RE = re.compile(r"\*\*Difficulty:\*\*\s*`([^`]+)`\s*\*\*Topics:\*\*([^\n]+)")
TAG_RE = re.compile(r"`([^`]+)`")
COMPLEXITY_RE = re.compile(r"^(Time|Space) complexity:\s*`([^`]+)`", re.MULTILINE)
HEADERS = ("#", "Problem", "Difficulty", "Topics", "Time", "Space")
SECTION_HEADING = "## Solved"


class ProblemError(Exception):
    """A problem file does not follow the layout documented in the README."""


def parse_problem(path: Path) -> tuple[int, list[str]]:
    """Return the problem's number and the table row describing it."""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    heading = HEADING_RE.match(lines[0])
    if heading is None:
        raise ProblemError("first line must be `# <number>. <Title>`")
    number, title = int(heading[1]), heading[2]

    prefix = path.stem.split("-")[0]
    if f"{number:04d}" != prefix:
        raise ProblemError(f"heading says {number}, filename says {prefix}")

    # The tag lines sit between the title and the first "## " section.
    meta = META_RE.search(text.partition("\n## ")[0])
    if meta is None:
        raise ProblemError(
            "expected '**Difficulty:** `<Difficulty>`' and "
            "'**Topics:** `<Topic>` ...' lines under the heading"
        )

    topics = TAG_RE.findall(meta[2])
    if not topics:
        raise ProblemError("the '**Topics:**' line lists no `<Topic>` tags")

    code = text.partition("\n## Code\n")[2]
    if not code:
        raise ProblemError("no '## Code' section")

    # Take the last Time/Space pair, so a file documenting several methods
    # reports the one it builds up to.
    found = COMPLEXITY_RE.findall(code)
    if [kind for kind, _ in found[-2:]] != ["Time", "Space"]:
        raise ProblemError("no 'Time complexity: `...`' / 'Space complexity: `...`' pair found")

    return number, [
        str(number),
        f"[{title}](problems/{path.stem}.md)",
        meta[1],
        ", ".join(topics),
        f"`{found[-2][1]}`",
        f"`{found[-1][1]}`",
    ]


def render_table(rows: list[list[str]]) -> str:
    table = [list(HEADERS), *rows]
    widths = [max(len(row[i]) for row in table) for i in range(len(HEADERS))]
    table.insert(1, ["-" * width for width in widths])
    return "\n".join(
        "| " + " | ".join(cell.ljust(w) for cell, w in zip(row, widths)) + " |" for row in table
    )


def replace_section(text: str, section: str) -> str:
    """Swap in the new section, keeping everything before and after it."""
    lines = text.split("\n")
    start = next(i for i, line in enumerate(lines) if line.startswith(SECTION_HEADING))
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))

    before = "\n".join(lines[:start]).rstrip("\n")
    after = "\n".join(lines[end:]).strip("\n")
    return "\n\n".join(part for part in (before, section, after) if part) + "\n"


def main(argv: list[str]) -> int:
    problems = []
    for path in sorted(PROBLEMS_DIR.glob("*.md")):
        try:
            problems.append(parse_problem(path))
        except ProblemError as error:
            print(f"error: {path.name}: {error}", file=sys.stderr)
            return 1

    problems.sort()
    rows = [row for _, row in problems]
    section = f"{SECTION_HEADING} ({len(rows)})\n\n{render_table(rows)}"

    text = README.read_text(encoding="utf-8")
    if SECTION_HEADING not in text:
        print(f"error: README.md has no '{SECTION_HEADING}' heading", file=sys.stderr)
        return 1

    updated = replace_section(text, section)
    if updated == text:
        print(f"README.md is up to date ({len(rows)} problems)")
        return 0

    if "--check" in argv:
        print("error: README.md is out of date; run `py update_readme.py`", file=sys.stderr)
        return 1

    README.write_text(updated, encoding="utf-8", newline="\n")
    print(f"README.md updated ({len(rows)} problems)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
