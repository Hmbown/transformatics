# Build and edit the textbook

The book starts with finite transformations, flows, exact transfer, composition
errors, and scaling. Fluid mechanics and interactive visual lessons follow.
The [preface](chapters/index.md) and [reading map](chapters/reader-map.md) offer
routes through the material.

Chapter Markdown lives in `chapters/`. `book.json` controls reading order;
`course-outline.json` records prerequisites and learning objectives. The editable
claim register is `claims.json`; `claims.md` is generated from it.

From the repository root, using Python 3.11 or later:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r textbook/requirements.txt -r tests/requirements.txt
python scripts/build_textbook.py
python -m http.server 8000 --directory textbook/_site
```

The builder produces the static reader in ignored `_site/`, including search,
typeset equations, downloadable Markdown, course metadata, and linked source
notes. It validates source hashes, claim dependencies, and local links. MathJax
3.2.2 loads from a pinned CDN. The fluid laboratory uses browser modules and a
worker, so serve it over HTTP. See its [numerical notes](assets/fluid/README.md).

To update a mathematical claim, review its source and hypotheses, update
`claims.json` and its source hashes, then run:

```sh
python scripts/build_textbook.py --update-claim-index
python scripts/update_publication_inventory.py
python -m pytest -q tests/test_publication_inventory.py tests/test_publication_privacy.py
node textbook/assets/fluid/checks.js
```

Inspect the affected pages and exercise solutions. The register distinguishes
local results, imported results, numerical evidence, and open questions.

The [English and Mandarin films](film/README.md) have a separate rendering
workflow. Generated media are not committed.
