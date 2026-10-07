# Transformatics

Learning notes, worked examples, exercises, and teaching films about finite
transformations, mathematical models, and fluid motion. Hunter Bown proposed this organizing viewpoint while
studying Navier–Stokes with AI tools. The underlying subjects are established
mathematics; the [reading guide](notes/chapters/references.md) names them in
their usual terms.

- [Read the learning notes](notes/chapters/index.md): worked examples, exercises,
  solutions, and interactive fluid and transformation demonstrations.
- [Film sources and instructions](notes/film/README.md): English and Mandarin
  full films and vertical shorts.
- [Watch the Mandarin short](https://www.bilibili.com/video/BV169pM6mEcp/).
- [Check a mathematical claim](notes/claims.md) against its linked source.

The films explain OpenAI's externally authored results on forced breakdown and
forced computation. This project did not solve Navier–Stokes. The three-dimensional
unforced regularity question remains open.

## Build the learning notes

Use Python 3.11 or later:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r notes/requirements.txt -r tests/requirements.txt
python scripts/build_notes.py
python -m http.server 8000 --directory notes/_site
```

Open http://localhost:8000. The chapter Markdown can also be read directly on
GitHub. See the [build guide](notes/README.md) for details.

## Contents and checks

`notes/` contains the learning notes, visual lessons, and film source. `references/`
contains the arguments cited in the notes. `formalization/`, `experiments/`, and
`artifacts/` retain the small source files and records needed to reproduce its
examples and scoped checks.

```sh
python scripts/update_publication_inventory.py
python -m pytest -q tests/test_publication_inventory.py tests/test_publication_privacy.py
node notes/assets/fluid/checks.js
node notes/film/checks.mjs
```

Generated sites, recordings, videos, and local review files stay outside Git.
See [CONTRIBUTING.md](CONTRIBUTING.md) for editing instructions and
[credits](notes/chapters/credits.md) for attribution.

Copyright 2026 ShannonTek. [MIT license](LICENSE); external sources retain
their own terms. [Citation metadata](CITATION.cff).
