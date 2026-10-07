"""Publication checks for accidental personal paths and generated/private files.

These checks cover common packaging mistakes. Run a dedicated secret scanner
as well when preparing a release.
"""

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MACHINE_PATH = re.compile(
    r"/(?:Users|Volumes|home)/[A-Za-z0-9_.-]+/"
    r"|[A-Za-z]:\\Users\\[A-Za-z0-9_.-]+\\"
    r"|~/(?:Desktop|Documents|Downloads|Library)/"
)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
TOKEN = re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,}|AKIA[A-Z0-9]{16})\b")
PRIVATE_KEY = re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----")
MEDIA = {".mp4", ".mov", ".mkv", ".mp3", ".wav", ".aiff", ".onnx"}
SOURCE_SUFFIXES = {".md", ".json", ".py", ".js", ".mjs", ".html", ".css", ".lean", ".toml", ".yml", ".yaml", ".txt"}


def publication_files():
    inventory = json.loads((ROOT / "docs/PUBLICATION_INVENTORY.json").read_text())
    return [ROOT / p for p in inventory["files"]] + [ROOT / "docs/PUBLICATION_INVENTORY.json"]


def test_no_personal_paths_or_secret_patterns():
    for path in publication_files():
        text = path.read_text(encoding="utf-8")
        relative = str(path.relative_to(ROOT))
        assert not MACHINE_PATH.search(text), f"personal machine path: {relative}"
        assert not TOKEN.search(text), f"credential-shaped token: {relative}"
        # Construct the marker so this test does not contain a key header itself.
        if path != Path(__file__):
            assert not PRIVATE_KEY.search(text), f"private key header: {relative}"
        for email in EMAIL.findall(text):
            assert email.endswith("@users.noreply.github.com"), f"email address: {relative}"


def test_no_generated_media_or_private_configuration():
    for path in publication_files():
        relative = path.relative_to(ROOT)
        assert path.suffix.lower() not in MEDIA, f"generated media: {relative}"
        assert path.stat().st_size < 5 * 1024 * 1024, f"unexpectedly large source: {relative}"
        assert not any(part.startswith(".env") for part in relative.parts), f"environment file: {relative}"
        assert path.name not in {".DS_Store", "HANDOFF.md", "AGENTS.md", "CLAUDE.md"}, f"local working record: {relative}"


def test_local_source_links_resolve():
    # Require a filename extension: raw mathematical products such as [A](t)
    # in the research notes are not file links.
    for path in publication_files():
        if path.suffix != ".md":
            continue
        for url in re.findall(r"\]\(([^\s)]+)\)", path.read_text()):
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if target.suffix not in SOURCE_SUFFIXES:
                continue
            assert target.is_relative_to(ROOT), f"link leaves repository: {path.relative_to(ROOT)}"
            assert target.is_file(), f"broken source link in {path.relative_to(ROOT)}: {url}"
