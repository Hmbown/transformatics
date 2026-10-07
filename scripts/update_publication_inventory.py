#!/usr/bin/env python3
"""Regenerate the public publication inventory.

The inventory records every file included in the public textbook snapshot with
its SHA-256 hash and size, together with the source revision and the scope
notes. It contains no machine-specific paths or personal information.

Usage: python scripts/update_publication_inventory.py

Only stdlib is required so that the check can run before dependencies are
installed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path, PurePosixPath

SCHEMA = "transformatics.publication_inventory.v1"
INVENTORY_REL = "docs/PUBLICATION_INVENTORY.json"

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "_site",
    "review",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".lake",
    "node_modules",
}

EXCLUDED_FILES = {
    ".DS_Store",
    INVENTORY_REL,
}

# Generated output kept out of commits (see the matching .gitignore files).
EXCLUDED_PATHS = {
    "textbook/film/out",
}

SCOPE = (
    "Curated public teaching snapshot. Includes the textbook, every source "
    "listed in textbook/claims.json and the files those sources link to, the "
    "scoped Lean formalizations and their receipts, the focused reproduction "
    "tests and experiments for cited claims, artifact receipts cited by the "
    "register, and the attribution, license and release metadata."
)

EXCLUDED_SCOPE = [
    "Git history, the former virtual environment, caches and build output",
    "The pre-publication operational log and the earlier status snapshots",
    "The full research graph and the route ledger",
    "Large numerical checkpoints and generated audio/video",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect(root: Path):
    """Return (files, symlinks) for the snapshot.

    files: {relative_posix_path: {"sha256": ..., "size": ...}}
    symlinks: {relative_posix_path: target_string}
    """
    root = root.resolve()
    files: dict[str, dict[str, object]] = {}
    symlinks: dict[str, str] = {}

    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        current = Path(dirpath)
        rel_dir = current.relative_to(root)
        dirnames[:] = sorted(
            name
            for name in dirnames
            if name not in EXCLUDED_DIRS
            and (rel_dir / name).as_posix() not in EXCLUDED_PATHS
            and not (rel_dir == Path(".") and name == ".git")
        )
        for name in sorted(filenames):
            path = current / name
            rel = PurePosixPath(rel_dir.as_posix()) / name if rel_dir.as_posix() != "." else PurePosixPath(name)
            rel_str = rel.as_posix()
            if name == ".DS_Store" or rel_str in EXCLUDED_FILES:
                continue
            if path.is_symlink():
                symlinks[rel_str] = os.readlink(path)
                continue
            if not path.is_file():
                continue
            files[rel_str] = {
                "sha256": sha256_file(path),
                "size": path.stat().st_size,
            }
    return dict(sorted(files.items())), dict(sorted(symlinks.items()))


def load_existing(path: Path) -> dict:
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=None, help="repository root (default: script's parent)")
    parser.add_argument("--source-repository", default=None)
    parser.add_argument("--source-branch", default=None)
    parser.add_argument("--source-commit", default=None)
    parser.add_argument("--source-commit-date", default=None)
    parser.add_argument("--source-base-commit", default=None)
    parser.add_argument("--source-base-branch", default=None)
    parser.add_argument("--edition", default=None)
    parser.add_argument("--prepared", default=None)
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    inventory_path = root / INVENTORY_REL
    existing = load_existing(inventory_path)

    source = dict(existing.get("source") or {})
    for key, value in (
        ("repository", args.source_repository),
        ("branch", args.source_branch),
        ("commit", args.source_commit),
        ("commit_date", args.source_commit_date),
        ("base_commit", args.source_base_commit),
        ("base_branch", args.source_base_branch),
    ):
        if value:
            source[key] = value

    files, symlinks = collect(root)
    total_bytes = sum(int(entry["size"]) for entry in files.values())

    inventory = {
        "schema": SCHEMA,
        "edition": args.edition or existing.get("edition") or "First public teaching edition",
        "prepared": args.prepared or existing.get("prepared"),
        "public_repository": existing.get("public_repository") or "Hmbown/transformatics",
        "public_url": existing.get("public_url") or "https://github.com/Hmbown/transformatics",
        "source": source,
        "scope": existing.get("scope") or SCOPE,
        "excluded_scope": existing.get("excluded_scope") or EXCLUDED_SCOPE,
        "counts": {
            "files": len(files),
            "symlinks": len(symlinks),
            "bytes": total_bytes,
        },
        "symlinks": symlinks,
        "files": files,
        "generated_by": "scripts/update_publication_inventory.py",
    }

    inventory_path.parent.mkdir(parents=True, exist_ok=True)
    inventory_path.write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"Wrote {INVENTORY_REL}: {len(files)} files, {len(symlinks)} symlinks, "
        f"{total_bytes} bytes"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
