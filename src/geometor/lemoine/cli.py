"""Command-line interface for GEOMETOR Lemoine apparatus compilation and verification."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from geometor.lemoine.compile_codex import compile_apparatus_rst, verify_codex_tracks
from geometor.lemoine.concordance import (
    CODEX_UNITS,
    default_repo_root,
    load_apparatus,
    verify_concordance,
    verify_sources_manifest,
)


def build_parser() -> argparse.ArgumentParser:
    """Build the ``geometor-lemoine`` CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="geometor-lemoine",
        description="GEOMETOR Lemoine Digital Scriptorium Codex & Minimal-Instrument Concordance CLI.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Optional path to geometor/lemoine repository root.",
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("summary", help="Print apparatus, concordance, and operation-saving statistics.")
    sub.add_parser("compile-apparatus", help="Compile concordance, bibliography, persons, and glossary RST files.")
    sub.add_parser("verify", help="Verify sources SHA-256 manifest, operation counts, SVGs, and 4-track codex integrity.")
    return parser


def cmd_summary(repo_root: Path) -> int:
    """Display summary metrics for the Lemoine codex and concordance."""
    app = load_apparatus(repo_root)
    classical_s = sum(e.classical_ops.s for e in app.entries if e.unit_id != "unit-4-minimal-instruments")
    lemoine_s = sum(e.lemoine_ops.s for e in app.entries if e.unit_id != "unit-4-minimal-instruments")
    saved = classical_s - lemoine_s

    print("GEOMETOR • lemoine — Géométrographie (1902) Codex Summary")
    print(f"  Units                : {len(CODEX_UNITS)} (4 synchronized tracks: en, fr, summary, notes)")
    print(f"  Concordance entries  : {len(app.entries)}")
    print(f"  Persons registry     : {len(app.persons)}")
    print(f"  Bibliography entries : {len(app.citations)}")
    print(f"  Technical glossary   : {len(app.glossary)}")
    print(
        f"  Ruler-and-compass S  : {classical_s} classical -> {lemoine_s} Lemoine (net saving: {saved} operations)"
    )
    return 0


def cmd_compile_apparatus(repo_root: Path) -> int:
    """Compile apparatus RST pages and mirror JSON apparatus files."""
    written = compile_apparatus_rst(repo_root)
    for path in written:
        print(f"Wrote {path.relative_to(repo_root)}")
    return 0


def cmd_verify(repo_root: Path) -> int:
    """Run all integrity checks across sources, concordance, codex tracks, and SVGs."""
    errors: list[str] = []
    errors.extend(verify_sources_manifest(repo_root))
    app = load_apparatus(repo_root)
    errors.extend(verify_concordance(app))
    errors.extend(verify_codex_tracks(repo_root))

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(
        f"OK: Verified {len(app.entries)} concordance benchmarks, 3 archival witnesses, "
        f"{len(CODEX_UNITS) * 4} codex track files, and standalone .euclid-graphic SVGs."
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    root = args.root or default_repo_root()
    command = args.command or "summary"

    if command == "summary":
        return cmd_summary(root)
    if command == "compile-apparatus":
        return cmd_compile_apparatus(root)
    if command == "verify":
        return cmd_verify(root)
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
