# How to add a paper, a person or a news item

**Status note.** The site generator has not been chosen yet. File locations in this guide are provisional, and anything that depends on the generator is marked "TBD". The data file names and fields are the intended design, and the example records match the files in `_rebuild/data/`.

You do not need git, a terminal or any software beyond a web browser and a free GitHub account that has been added to the repository. You edit one text file, click "Commit changes", and the site rebuilds itself.

## 1. How the site works

The pages of this site are generated from three data files: `publications.yml`, `people.yml` and `news.yml`. Their location is TBD (for now they sit in `_rebuild/data/`). The web pages themselves are never edited by hand. When you save ("commit") a change to one of these files on GitHub, an automatic build starts and the new page usually appears within a few minutes. Each file is a list of records, and each record is a short block of `field: value` lines. To add something, you copy an existing record, change its values, and save.

## 2. Add a paper

1. On GitHub, open the repository and then the file `publications.yml` (location TBD).
2. Click the pencil icon at the top right of the file view ("Edit this file").
3. Find a recent paper near the top of the list, select that whole record from its leading dash to its last field, and copy it.
4. Paste it above the record you copied, so that the newest paper is first. Keep the same indentation as the record above it.
5. Change each field to describe your paper (see the table below).
6. Open `https://doi.org/<your doi>` in another tab and confirm that it opens the right paper.
7. Click "Commit changes", write a short message such as "Add Maraschin 2026 JPCC", and confirm.

Example record:

```yaml
- doi: 10.1021/acs.jpcc.5c08777
  title: "Unraveling fundamental activity-stability relationships in rutile oxides"
  authors: "M. Maraschin, J.A. Gauthier"
  journal: "The Journal of Physical Chemistry C"
  journal_abbrev: "J. Phys. Chem. C"
  year: 2026
  volume: 130
  issue: 10
  pages: "3803-3813"
  group_authors: ["Mikael Maraschin", "Joe Gauthier"]
  thumbnail: images/pubs/jpcc.jpg
```

| Field | Meaning | Required |
|---|---|---|
| `doi` | The DOI only, without `https://doi.org/`. | Yes |
| `title` | The paper title. Write subscripts and superscripts as HTML, for example `CO<sub>2</sub>` or `cm<sup>-2</sup>`. | Yes |
| `authors` | All authors in the order printed on the paper. | Yes |
| `journal` | Full journal name. | Yes |
| `journal_abbrev` | The standard abbreviation, used in compact lists. | Yes |
| `year` | Publication year. | Yes |
| `volume` | Volume number. | If it has one |
| `issue` | Issue number. | Optional |
| `pages` | Page range or article number. | If it has one |
| `group_authors` | Names of group members on the paper, spelled as in `people.yml`, so that the page can link them to their entries. | Optional |
| `thumbnail` | Path to the journal or graphic image (see section 5). | Optional |

## 3. Add a person

1. Open `people.yml` (location TBD) and click the pencil icon.
2. Find the section that fits: `graduate`, `undergraduate`, or `alumni` (section 6 explains alumni).
3. Copy an existing record from that section, paste it at the end of the same section, and edit it.
4. Upload the photo first if there is one (section 5), then enter its path in `photo`.
5. Leave any field you do not know as `""`. Blank fields are not shown.
6. Click "Commit changes".

Example graduate student record:

```yaml
- name: Jane Doe
  role: Ph.D. Student
  education:
    - "B.Sc. Chemical Engineering, Example University"
  photo: images/people/jane_doe.jpg
  links:
    scholar: "https://scholar.google.com/citations?user=XXXX"
    linkedin: "https://www.linkedin.com/in/jane-doe"
  research: "One sentence on the topic you work on."
  joined: 2026
  email: ""
```

| Field | Meaning | Required |
|---|---|---|
| `name` | Full name as you want it shown. | Yes |
| `role` | For example "Ph.D. Student" or "Master's Research Assistant". | Yes |
| `education` | Earlier degrees, one line each, newest first. | Optional |
| `photo` | Path to the photo. | Optional |
| `links` | `scholar` and `linkedin` addresses. Delete a line you do not have. Remove any `?utm_...` tracking text from LinkedIn addresses and use `https`. | Optional |
| `research` | One sentence on your topic. | Optional |
| `joined` | Year you joined the group. | Optional |
| `email` | Shown only if you choose to put it here. | Optional |

Undergraduate records use `name`, `affiliation` (only if you are from another university), `major` and `project`. The principal investigator record (`pi`) is edited the same way and should be changed only by Joe.

## 4. Add a news item

1. Open `news.yml` (location TBD) and click the pencil icon.
2. Copy the first record, paste it above itself so that the newest item is first, and edit it.
3. Set `status: draft` unless Joe has approved the item, then ask Joe to change it. Only items marked `published` appear on the site (final status names TBD).
4. Click "Commit changes".

Example record:

```yaml
- date: "2026-03"
  title: "Two talks at the ACS Spring National Meeting"
  body: "In Atlanta, GA, the talk titles were ... and ... ."
  link: ""
  category: talk
  status: draft
  source: "Where the fact is stated, for example the CV page"
```

| Field | Meaning | Required |
|---|---|---|
| `date` | `YYYY`, `YYYY-MM` or `YYYY-MM-DD`, only as precise as you know. Keep it in quotes. | Yes |
| `title` | A short headline. | Yes |
| `body` | One or two plain, factual sentences. | Yes |
| `link` | A DOI address for papers, otherwise leave `""`. | Optional |
| `category` | One of `award`, `paper`, `talk`, `group`. | Yes |
| `status` | `draft` until approved. | Yes |
| `source` | Where the fact comes from, for the person who approves it. | Yes |

Awards and fellowships are announced as news items. They are not listed on a separate page.

## 5. Add a photo

1. Resize the image first. It should be at most 800 pixels on the long edge and under 300 KB.
   - On macOS, open the image in Preview, choose Tools, then Adjust Size, set the width or height so the long side is 800 pixels or less, and save. To reduce file size, use File, then Export, choose JPEG, and move the Quality slider down until the file is under 300 KB.
   - On Windows, open the image in Photos, click the three dots, choose Resize image, pick a smaller size, and save a copy. Check the file size in File Explorer.
2. In the repository on GitHub, open the images folder (exact folder TBD, for now `thumbs/`).
3. Click "Add file", then "Upload files", drag the image in, and click "Commit changes".
4. Put the path, for example `images/people/jane_doe.jpg`, in the `photo` or `thumbnail` field. Use a file name without spaces.

## 6. Move a person to alumni

1. Open `people.yml` and click the pencil icon.
2. Cut the person's whole record from `graduate` or `undergraduate`.
3. Paste it into `alumni`, keeping the list ordered by year, newest first.
4. Reduce it to `name`, `degree` and `year`, plus `photo` if you have one.
5. Click "Commit changes".

Example:

```yaml
- name: Jane Doe
  degree: Ph.D.
  year: 2030
  photo: ""
```

We list alumni by name, degree and year only. Never add where a person went afterwards.

## 7. Common YAML mistakes

- Indent with spaces, never tabs. Each field inside a record is indented by exactly two spaces, and every field in one record lines up.
- Every record starts with a dash and a space (`- `). A missing dash merges two records.
- Put quotes around any value that contains a colon, a leading `#`, or starts with a special character, for example `title: "CO<sub>2</sub> reduction: a benchmark"`. Quotes inside a quoted value must be written as `\"`.
- Keep a space after each colon (`year: 2026`).
- Keep dates in quotes so `2026-03` is not read as something else.

GitHub shows a red mark in the editor for some errors, but not all of them.

## 8. If the site does not update

1. Wait five minutes, then reload the page with a forced refresh.
2. On the repository page, click the Actions tab and look at the newest run. A green check means the build worked. A red X means it failed, and opening the run shows which line of which file caused the problem.
3. To undo your change, click the Code tab, open "commits", find your commit, click it, and use the "Revert" button if shown (otherwise ask Joe). Revert creates a new commit that restores the previous version. The site then rebuilds with the old content.
4. Fix the mistake and try again, or ask Joe.

## 9. Rules

> - The group name is **Gauthier Research Lab**.
> - We write in the first-person plural ("we").
> - No grant amounts and no lists of funding sources.
> - Alumni placements are not listed. Name, degree and year only.
> - Check every DOI before saving by opening `https://doi.org/<doi>` and confirming that it leads to the right paper.
