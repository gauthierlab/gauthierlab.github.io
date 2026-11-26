#!/usr/bin/env python3
"""Regenerate the "Journal Publications" section of publications.html
from _rebuild/data/publications.yml.

Usage (from the repository root):  python3 _rebuild/build_publications.py

Everything between the BEGIN/END marker comments in publications.html is
replaced (the journal list, and the conference/submitted/preprint lists). Edit the data file, not the generated markup. Requires PyYAML.
"""
import html
import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / "publications.html"
DATA = ROOT / "_rebuild" / "data" / "publications.yml"
BEGIN = "<!-- BEGIN generated publications (edit _rebuild/data/publications.yml) -->"
END = "<!-- END generated publications -->"
PI_FAMILY = "Gauthier"
EAGER = 2  # the first two cover images load immediately; the rest are lazy


def compact(name):
    """'J. A. Gauthier' -> 'J.A. Gauthier' (initials closed up, family name kept)."""
    parts = name.split(" ")
    initials = [p for p in parts if re.fullmatch(r"(?:[^\W\d_]\.-?)+", p)]
    rest = parts[len(initials):]
    return "".join(initials) + (" " if initials and rest else "") + " ".join(rest)


def author_html(rec):
    group = set(rec.get("group_authors") or [])
    out = []
    for a in rec["authors"]:
        text = html.escape(compact(a), quote=False)
        if a in group or a.split(" ")[-1] == PI_FAMILY:
            text = "<b>" + text + "</b>"
        out.append(text)
    return ", ".join(out)


def venue(rec):
    bits = [rec["journal_abbrev"], str(rec["year"])]
    for key in ("volume", "pages"):
        if rec.get(key):
            bits.append(str(rec[key]))
    return ", ".join(bits) + "."


def entry(rec, lazy):
    url = "https://doi.org/" + rec["doi"]
    alt = html.escape(rec["journal_abbrev"])
    lazy_attr = ' loading="lazy"' if lazy else ""
    i = " " * 21
    return (
        f'{i}<div class="row-fluid publication-entry">\n'
        f'{i}   <div class="span3">\n'
        f'{i}      <a href="{url}" class="thumbnail">\n'
        f'{i}      <img class="publications-thumb" src="{rec["thumbnail"]}" alt="{alt}"{lazy_attr}/>\n'
        f'{i}      </a>\n'
        f'{i}   </div>\n'
        f'{i}   <div class="span9">\n'
        f'{i}      <h4>{rec["title"]}</h4>\n'
        f'{i}      <p>{author_html(rec)}</p>\n'
        f'{i}      <a href="{url}">{html.escape(venue(rec))}</a>\n'
        f'{i}   </div>\n'
        f'{i}</div>\n'
    )


def build(records):
    years = sorted({r["year"] for r in records}, reverse=True)
    out, n = [], 0
    for y in years:
        i = " " * 18
        out.append(f'{i}<section id="{y}">\n{i}   <h3 class="pub-year">{y}</h3>\n')
        blocks = []
        for r in records:
            if r["year"] == y:
                blocks.append(entry(r, lazy=n >= EAGER))
                n += 1
        out.append((" " * 21 + "<hr>\n").join(blocks))
        out.append(f"{i}</section>\n{i}<hr>\n")
    return "".join(out), years, n


OTHER_BEGIN = "<!-- BEGIN generated lists (edit _rebuild/data/publications.yml) -->"
OTHER_END = "<!-- END generated lists -->"
OTHER = [("conference", "Conference and Workshop Papers"),
         ("submitted", "Submitted Manuscripts"),
         ("preprints", "Preprints and Data")]


def other_lists(data):
    i = " " * 15
    out = []
    for key, heading in OTHER:
        items = data.get(key) or []
        if not items:
            continue
        out.append(f'{i}<section id="{key}">\n{i}   <div class="page-header">\n{i}      <h2>{heading}</h2>\n{i}   </div>\n{i}   <ol>\n')
        for it in items:
            line = f'{author_html(it)}. "{it["title"]}." {it["note"]}'
            if it.get("link"):
                line += f' <a href="{html.escape(it["link"])}">{html.escape(it.get("link_text", "Link"))}</a>'
            out.append(f'{i}      <li class="publication">{line}</li>\n')
        out.append(f'{i}   </ol>\n{i}</section>\n{i}<hr>\n')
    return "".join(out)


def main():
    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    body, years, n = build(data["published"])
    page = PAGE.read_text(encoding="utf-8")
    a, b = page.index(BEGIN), page.index(END)
    page = page[: a + len(BEGIN)] + "\n" + body + " " * 18 + page[b:]
    a, b = page.index(OTHER_BEGIN), page.index(OTHER_END)
    page = page[: a + len(OTHER_BEGIN)] + "\n" + other_lists(data) + " " * 15 + page[b:]
    PAGE.write_text(page, encoding="utf-8")
    print(f"wrote {n} publications in {len(years)} year sections: {years}")
    print("If a year was added or removed, update the year list in the page sidebar.")


if __name__ == "__main__":
    main()
