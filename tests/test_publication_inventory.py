"""Check the committed publication inventory against the checkout.

Focused, stdlib-only checks:
  * the inventory covers exactly the snapshot files (same paths and SHA-256);
  * recorded symlinks stay inside the repository;
  * no machine paths, caches or build output appear in the inventory;
  * every claim-register source path is present in the inventory.

These checks verify packaging metadata, not any mathematical result.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "docs" / "PUBLICATION_INVENTORY.json"
CLAIMS = ROOT / "notes" / "claims.json"

ABSOLUTE_PATH_PATTERN = re.compile(r"(/Users/|/Volumes/|/home/|/private/|[A-Za-z]:\\)")
CACHE_MARKERS = ("__pycache__", ".DS_Store", "_site/", ".venv/", ".pytest_cache/", "node_modules/")

REQUIRED_FILES = {
    "LICENSE",
    "CITATION.cff",
    "README.md",
    "notes/claims.json",
    "notes/claims.md",
    "notes/requirements.txt",
    "scripts/build_notes.py",
}


def _load_updater():
    path = ROOT / "scripts" / "update_publication_inventory.py"
    spec = importlib.util.spec_from_file_location("update_publication_inventory", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def load_inventory() -> dict:
    assert INVENTORY.is_file(), "docs/PUBLICATION_INVENTORY.json is missing"
    return json.loads(INVENTORY.read_text(encoding="utf-8"))


def test_inventory_matches_checkout():
    inventory = load_inventory()
    updater = _load_updater()
    files, symlinks = updater.collect(ROOT)

    recorded = inventory["files"]
    assert set(recorded) == set(files), (
        "inventory path set differs from checkout: "
        f"missing={sorted(set(files) - set(recorded))[:10]} "
        f"extra={sorted(set(recorded) - set(files))[:10]}"
    )
    for rel, entry in files.items():
        assert recorded[rel]["sha256"] == entry["sha256"], f"hash mismatch: {rel}"
        assert recorded[rel]["size"] == entry["size"], f"size mismatch: {rel}"

    assert inventory.get("symlinks", {}) == symlinks
    for rel, target in symlinks.items():
        resolved = (ROOT / rel).resolve()
        assert resolved.is_relative_to(ROOT.resolve()), f"symlink escapes repository: {rel}"
        assert resolved.is_file(), f"symlink target missing: {rel} -> {target}"


def test_inventory_counts_and_metadata():
    inventory = load_inventory()
    assert inventory["schema"] == "transformatics.publication_inventory.v1"
    assert inventory["public_repository"] == "Hmbown/transformatics"
    assert inventory["public_url"] == "https://github.com/Hmbown/transformatics"
    assert inventory["source"].get("description"), "source scope is not recorded"
    assert inventory["counts"]["files"] == len(inventory["files"])
    assert inventory["counts"]["bytes"] == sum(
        int(entry["size"]) for entry in inventory["files"].values()
    )


def test_no_machine_paths_or_caches():
    text = INVENTORY.read_text(encoding="utf-8")
    assert not ABSOLUTE_PATH_PATTERN.search(text), "machine path found in inventory"
    for marker in CACHE_MARKERS:
        assert marker not in text, f"cache/build marker found in inventory: {marker}"


def test_required_publication_files_present():
    inventory = load_inventory()
    present = set(inventory["files"]) | set(inventory.get("symlinks", {}))
    missing = sorted(REQUIRED_FILES - present)
    assert not missing, f"required publication files missing: {missing}"


def test_claim_sources_are_in_inventory():
    inventory = load_inventory()
    claims = json.loads(CLAIMS.read_text(encoding="utf-8"))
    sources = claims.get("source_sha256", {})
    missing = sorted(path for path in sources if path not in inventory["files"])
    assert not missing, f"claim sources absent from inventory: {missing}"


def test_inventory_hashes_are_well_formed():
    inventory = load_inventory()
    for rel, entry in inventory["files"].items():
        digest = entry["sha256"]
        assert isinstance(digest, str) and len(digest) == 64
        int(digest, 16)
        assert int(entry["size"]) >= 0, f"negative size: {rel}"
