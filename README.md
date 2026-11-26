# Gauthier Research Lab website

This repository holds the website of the Gauthier Research Lab in the Department of Chemical Engineering at Texas Tech University. The live site is at https://gauthierlab.github.io/.

The site is plain static HTML styled with Bootstrap 2.3.1. GitHub Pages serves it directly from the `master` branch; there is no build step, so a change to an HTML file goes live as soon as it is pushed to `master`.

## Pages

| File | Contents |
| --- | --- |
| `index.html` | Home page: image carousel and a short description of the group. |
| `people.html` | Principal investigator, graduate students, undergraduate researchers and alumni. |
| `research.html` | Research overview and the four research themes. |
| `publications.html` | Journal publications grouped by year, followed by submitted manuscripts. |
| `resources.html` | Links to software documentation and Texas Tech resources. |
| `contact.html` | Office address, map, phone, email and profile links. |

`404.html` is the page GitHub Pages shows for any missing address; it uses root-absolute paths (such as `/css/theme.css`) so it works at any URL. `sitemap.xml` lists the six pages for search engines. Shared styles are in `css/theme.css`, and `js/site.js` fills in the "last updated" line in the footer from the deploy date.

## Images

Figures used on the pages live in `images/`. People photos and journal cover thumbnails live in `thumbs/`. Keep photos at most 800 px on the long edge so the pages stay fast to load.

## Adding a publication

The journal list in `publications.html` (everything between the `BEGIN generated publications` and `END generated publications` comments) is generated from `_rebuild/data/publications.yml`. To add a paper:

1. Add a record to `_rebuild/data/publications.yml` by copying an existing one and editing it. Take the title, authors, year, volume and pages from the publisher's page, and check the DOI by opening `https://doi.org/<doi>` in a browser.
2. Run `python3 _rebuild/build_publications.py` from the repository root (it needs Python 3 with PyYAML).
3. If the paper starts a new year, add that year to the sidebar list near the top of `publications.html`.
4. Commit both the data file and `publications.html`.

Names listed under `group_authors` in a record, and the PI, are shown in bold. The "Submitted Manuscripts" list at the bottom of the page is still edited by hand.

## Draft data for a rebuild

The `_rebuild/` directory holds draft data files for a planned rebuild of the site. It is not published: GitHub Pages builds with Jekyll, which ignores directories whose names start with an underscore.

## Credit

The layout derives from the MIT-licensed "Research Lab Website" Bootstrap template; see `LICENSE`.
