# Contributing

Contributions can improve explanations, examples, exercise solutions, accessibility,
references, or precisely stated mathematical arguments. Name the chapter and
section, explain the issue, and make a focused change.

Keep classical mathematics, teaching examples, local research, and imported results
clearly attributed. Unforced Navier–Stokes regularity is open; the forced-breakdown
construction belongs to OpenAI. Preserve the hypotheses and boundaries of each
claim in [the register](notes/claims.json) and its linked source.

Build the learning notes and inspect the changed page at desktop and phone widths. If
source notes change, review the mathematical text before refreshing the register's
source hashes. Regenerate the readable register with
`python scripts/build_notes.py --update-claim-index`.

Run the relevant checks in [README.md](README.md), and refresh the publication
inventory after source edits. Film changes also require formula checks and a
review of the affected frames. Keep generated media outside the repository.

Use portable paths. Do not commit credentials, personal contact details, local
machine paths, production notes, recordings, caches, or generated sites. Preserve
third-party attribution and licenses.
