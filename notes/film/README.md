# Teaching films

English and Mandarin films about motion, measurement, and two of OpenAI's
Navier–Stokes results. The full cut is about sixteen minutes; the vertical short
is about seventy seconds. The computation explanation starts with a small
program, 0 → 1 → 2 → stop, before relating its states to particle positions.

[Watch the Mandarin short on Bilibili](https://www.bilibili.com/video/BV169pM6mEcp/).

Transformatics is Hunter Bown's proposed organizing viewpoint. The forced results
belong to OpenAI; the three-dimensional unforced regularity question remains open.

## Sources

- OpenAI, [Finite time blowup for Navier–Stokes](https://openai.com/index/navier-stokes-solution/),
  with the [formal source](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
- [openai/math, family 376](https://github.com/openai/math/blob/adc7f124/lean/docs/376.md).
- `checks.mjs` checks the 23 formulas illustrated by the film.

The [short-film source comparison](accuracy.md) maps every scene to its source.

Taylor–Green and sliding-layer flows are exact teaching examples. Core sections,
box routes, and detector paths are labelled as schematics in the film.

## Narration and rendering

Requirements: Python 3.11+, Node.js 18+, FFmpeg, and Chromium through Playwright.
From `notes/film`, install the dependencies in a Python environment of your
choice and install the browser:

```sh
python -m pip install -r requirements.txt
npm ci
npx playwright install chromium
python zh.py
node checks.mjs
```

Use an output directory outside the checkout. For example, if the repository is
`transformatics/`, its sibling `transformatics-output/` can hold the renders:

```sh
python narrate.py --script script.json --out ../../../transformatics-output/full-en --voice en-US-GuyNeural --rate=-5%
python narrate.py --script script.zh.json --out ../../../transformatics-output/full-zh --voice zh-CN-YunyangNeural --rate=-5%
node inspect.mjs --out ../../../transformatics-output/full-en
node inspect.mjs --out ../../../transformatics-output/full-zh
node render.mjs --out ../../../transformatics-output/full-en --lang eng --name transformatics-film-en
node render.mjs --out ../../../transformatics-output/full-zh --lang chi --name transformatics-film-zh
```

For a short, use `short/script.en.json` or `short/script.zh.json` with its own
output directory. Inspect with `--short`; render with
`--page short.html --size 1080x1920`. `render.mjs --stills 20,61.5` captures selected
frames, and `--from 54 --to 60` makes a bounded preview.

The narrator sends the script text to the speech service. It uses standard
synthetic voices, keeps natural speech duration, and writes cached beats,
captions, a timeline, and audio measurements. Listen to the generated speech and
inspect the frames before sharing a render. The renderer records source hashes
and reports encoder failures.

`script.json` and `script.zh.json` contain the parallel scripts; `zh.py` guards the
translation against changed English scenes. `film.js` and `short.js` draw the
frames, and `labels.zh.js` translates on-screen labels. Generated recordings,
videos, caches, and review images stay out of Git.
