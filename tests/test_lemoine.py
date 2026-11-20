"""Comprehensive test suite for GEOMETOR Lemoine Digital Scriptorium Codex & Concordance."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from types import SimpleNamespace

from geometor.lemoine import (
    CODEX_LEAVES,
    CODEX_UNITS,
    PAIRED_ARCHIVAL_PLATES,
    TRACK_SUFFIXES,
    OpCount,
    __version__,
    apparatus_slug,
    compile_apparatus_rst,
    configure_local_intersphinx,
    default_repo_root,
    load_apparatus,
    register_french_book_track,
    verify_codex_tracks,
    verify_concordance,
    verify_sources_manifest,
)
from geometor.lemoine.cli import main as cli_main

REPO_ROOT = default_repo_root()


def test_version_and_repo_root() -> None:
    assert __version__ == "0.1.5"
    assert (REPO_ROOT / "pyproject.toml").is_file()
    assert len(CODEX_UNITS) == 4
    assert len(CODEX_LEAVES) == 25
    assert len(PAIRED_ARCHIVAL_PLATES) == 11
    assert TRACK_SUFFIXES == ("en", "fr", "summary", "notes")


def test_opcount_algebra_validation() -> None:
    # Lemoine Problem LI (X(6)): 4R1 + 2R2 + 13C1 + 8C3 -> S=27, E=17, 2 lines, 8 circles
    valid = OpCount(
        r1=4, r2=2, c1=13, c2=0, c3=8, s=27, e=17, lines=2, circles=8,
        symbol="4R_1 + 2R_2 + 13C_1 + 8C_3",
    )
    assert valid.validate() == []

    bad_s = OpCount(
        r1=4, r2=2, c1=13, c2=0, c3=8, s=28, e=17, lines=2, circles=8,
        symbol="4R_1 + 2R_2 + 13C_1 + 8C_3",
    )
    assert any("Simplicity mismatch" in msg for msg in bad_s.validate())

    bad_e = OpCount(
        r1=4, r2=2, c1=13, c2=0, c3=8, s=27, e=19, lines=2, circles=8,
        symbol="4R_1 + 2R_2 + 13C_1 + 8C_3",
    )
    assert any("Exactitude mismatch" in msg for msg in bad_e.validate())

    bad_lc = OpCount(
        r1=4, r2=2, c1=13, c2=0, c3=8, s=27, e=17, lines=3, circles=7,
        symbol="4R_1 + 2R_2 + 13C_1 + 8C_3",
    )
    errs = bad_lc.validate()
    assert any("Traced line count" in msg for msg in errs)
    assert any("Traced circle count" in msg for msg in errs)


def test_sources_manifest_sha256_integrity() -> None:
    assert verify_sources_manifest(REPO_ROOT) == []


def test_concordance_and_minimal_instrument_subspaces() -> None:
    app = load_apparatus(REPO_ROOT)
    assert verify_concordance(app) == []
    assert len(app.entries) >= 24

    by_id = {e.id: e for e in app.entries}

    # Compass-only benchmarks must have zero straightedge operations (r1 = r2 = 0)
    for cid in (
        "point-reflection",
        "circle-inversion",
        "mascheroni-midpoint-line-intersection",
    ):
        op = by_id[cid].lemoine_ops
        assert op.r1 == 0 and op.r2 == 0 and op.lines == 0
        assert op.circles > 0

    # Pure straightedge benchmarks must have zero compass operations (c1 = c2 = c3 = 0)
    for sid in (
        "polar-of-point",
        "harmonic-conjugate",
        "steiner-parallel-circle-meet",
    ):
        op = by_id[sid].lemoine_ops
        assert op.c1 == 0 and op.c2 == 0 and op.c3 == 0 and op.circles == 0
        assert op.lines > 0

    # Standard ruler-and-compass Lemoine syntheses never exceed classical simplicity S
    for entry in app.entries:
        if entry.id not in ("mascheroni-midpoint-line-intersection", "steiner-parallel-circle-meet"):
            assert entry.delta_s >= 0, f"{entry.id} had negative saving {entry.delta_s}"


def test_mirrored_apparatus_and_deterministic_compilation() -> None:
    written = compile_apparatus_rst(REPO_ROOT)
    assert len(written) == 3

    for fname in ("persons.json", "citations.json", "glossary.json"):
        primary = (REPO_ROOT / "resources" / "geometrographie" / fname).read_text(encoding="utf-8")
        mirrored = (REPO_ROOT / "resources" / fname).read_text(encoding="utf-8")
        assert primary == mirrored


def test_all_rst_apparatus_roles_resolve() -> None:
    app = load_apparatus(REPO_ROOT)
    person_slugs = {apparatus_slug(k) for k in app.persons}
    cite_slugs = {apparatus_slug(k) for k in app.citations}
    term_slugs = {apparatus_slug(k) for k in app.glossary}

    role_re = re.compile(r":(person|cite|term):`([^`]+)`")

    def extract_target(raw: str) -> str:
        m = re.search(r"<([^>]+)>", raw)
        key = m.group(1) if m else raw
        return apparatus_slug(key)

    for rst_path in sorted((REPO_ROOT / "docsrc").rglob("*.rst")):
        text = rst_path.read_text(encoding="utf-8")
        for role, raw_val in role_re.findall(text):
            slug = extract_target(raw_val)
            if role == "person":
                assert slug in person_slugs, f"Unresolved :person:`{raw_val}` -> '{slug}' in {rst_path}"
            elif role == "cite":
                assert slug in cite_slugs, f"Unresolved :cite:`{raw_val}` -> '{slug}' in {rst_path}"
            elif role == "term":
                assert slug in term_slugs, f"Unresolved :term:`{raw_val}` -> '{slug}' in {rst_path}"


def test_standalone_and_paired_archival_plates_with_zero_orphans() -> None:
    # 1. All 9 standalone explanatory SVGs in docsrc/_static/figures/
    fig_dir = REPO_ROOT / "docsrc" / "_static" / "figures"
    svgs = sorted(fig_dir.glob("*.svg"))
    assert len(svgs) == 9

    for svg_path in svgs:
        content = svg_path.read_text(encoding="utf-8")
        root = ET.fromstring(content)
        assert "euclid-graphic" in root.attrib.get("class", "")
        layer_ids = [el.attrib.get("id") for el in root if el.tag.endswith("g")]
        assert layer_ids == ["elements", "graphics", "highlights", "points", "labels"]

    # 2. All 11 paired archival bitmaps (.g1.png) + calibrated SVGs (.g1.svg)
    codex_dir = REPO_ROOT / "docsrc" / "geometrographie"
    expected_paired: set[Path] = set()
    for part_id, leaf_id, folio in PAIRED_ARCHIVAL_PLATES:
        leaf_dir = codex_dir / part_id / leaf_id
        png_path = leaf_dir / f"{folio}.g1.png"
        svg_path = leaf_dir / f"{folio}.g1.svg"
        assert png_path.is_file() and png_path.stat().st_size > 1024
        assert svg_path.is_file()
        expected_paired.add(png_path.resolve())
        expected_paired.add(svg_path.resolve())

        root = ET.fromstring(svg_path.read_text(encoding="utf-8"))
        assert "euclid-graphic" in root.attrib.get("class", "")
        layer_ids = [el.attrib.get("id") for el in root if el.tag.endswith("g")]
        assert layer_ids == ["elements", "graphics", "highlights", "points", "labels"]

    # 3. Every .. picture:: resolves cleanly, no forbidden :align:/:width:, zero orphans
    pic_re = re.compile(r"^\s*\.\.\s+picture::\s+(\S+)", re.MULTILINE)
    forbidden_opt_re = re.compile(r"^\s*\.\.\s+picture::[^\n]*\n(?:\s+:[^\n]+\n)*?\s+:(?:align|width):", re.MULTILINE)
    referenced_static: set[str] = set()
    referenced_paired: set[Path] = set()

    for rst_path in sorted((REPO_ROOT / "docsrc").rglob("*.rst")):
        text = rst_path.read_text(encoding="utf-8")
        assert not forbidden_opt_re.search(text), f"Forbidden :align:/:width: on .. picture:: in {rst_path}"
        for pic in pic_re.findall(text):
            if pic.startswith("/"):
                target = REPO_ROOT / "docsrc" / pic.lstrip("/")
                assert target.is_file(), f"Missing static figure {pic} referenced in {rst_path}"
                referenced_static.add(target.name)
            else:
                target = (rst_path.parent / pic).resolve()
                assert target.is_file(), f"Missing paired plate {pic} referenced in {rst_path}"
                referenced_paired.add(target)

    assert len(referenced_static) == 9
    assert referenced_paired == expected_paired


def test_atomic_leaves_monotonic_folios_and_legacy_anchors() -> None:
    codex_dir = REPO_ROOT / "docsrc" / "geometrographie"
    folio_re = re.compile(r"^\s*\.\.\s+folio::\s+(\d{4})", re.MULTILINE)
    anchor_re = re.compile(r"^\.\.\s+_([a-z0-9-]+):", re.MULTILINE)

    en_folios_seen: set[int] = set()
    fr_folios_seen: set[int] = set()
    all_anchors: set[str] = set()
    prev_start = 0

    for part_id, leaf_id, start_folio, _title in CODEX_LEAVES:
        start_num = int(start_folio)
        assert start_num >= prev_start, f"Non-monotonic start folio on {leaf_id}: {start_num} < {prev_start}"
        prev_start = start_num

        for suffix in TRACK_SUFFIXES:
            p = codex_dir / part_id / leaf_id / f"{leaf_id}-{suffix}.rst"
            text = p.read_text(encoding="utf-8")
            all_anchors.update(anchor_re.findall(text))
            fids = [int(f) for f in folio_re.findall(text)]
            assert fids, f"Missing .. folio:: directive in {p}"
            if suffix == "en":
                en_folios_seen.update(fids)
            elif suffix == "fr":
                fr_folios_seen.update(fids)

    expected_print_folios = set(range(17, 83))
    assert expected_print_folios.issubset(en_folios_seen)
    assert expected_print_folios.issubset(fr_folios_seen)

    legacy_anchors = {
        "geometrographie-part-01-en",
        "geometrographie-part-01-fr",
        "geometrographie-part-01-summary",
        "geometrographie-part-01-notes",
        "geometrographie-unit-1-en",
        "geometrographie-part-02-en",
        "geometrographie-part-02-fr",
        "geometrographie-unit-2-en",
        "geometrographie-part-03-en",
        "geometrographie-part-03-fr",
        "geometrographie-unit-3-en",
        "lemoine-en-genesis",
        "lemoine-en-ideal-postulates",
        "lemoine-en-five-operations",
        "lemoine-en-symbol-coefficients",
        "lemoine-en-fundamental-table",
        "lemoine-en-copy-angle-triangles",
        "lemoine-en-parallel-tarry",
        "lemoine-en-bisector-reflection",
        "lemoine-en-perpendiculars-bisector",
        "lemoine-en-circles-tangents-incircle",
        "lemoine-en-proportions-golden",
        "lemoine-en-projective-inversive",
        "lemoine-en-triangle-centers",
        "lemoine-fr-genesis",
        "lemoine-fr-five-operations",
        "lemoine-fr-parallel-tarry",
        "lemoine-fr-proportions-golden",
        "lemoine-fr-triangle-centers",
    }
    assert legacy_anchors.issubset(all_anchors)


def test_codex_tracks_and_zero_embedded_python() -> None:
    assert verify_codex_tracks(REPO_ROOT) == []


def test_french_book_track_registration() -> None:
    publish_src = REPO_ROOT.parents[1] / "photon-platform" / "publish" / "src"
    if publish_src.is_dir() and str(publish_src) not in sys.path:
        sys.path.insert(0, str(publish_src))
    from photon_platform.publish import book

    register_french_book_track()
    found_docs = {
        f"geometrographie/{part}/{leaf}/{leaf}-{suffix}"
        for part, leaf, _folio, _title in CODEX_LEAVES
        for suffix in TRACK_SUFFIXES
    }
    env = SimpleNamespace(found_docs=found_docs)

    for part, leaf, _folio, _title in CODEX_LEAVES:
        for suffix in TRACK_SUFFIXES:
            active_doc = f"geometrographie/{part}/{leaf}/{leaf}-{suffix}"
            tracks = book.detect_companion_tracks(env, active_doc)
            keys = [t["key"] for t in tracks]
            assert keys == ["en", "fr", "summary", "notes"]
            active_keys = [t["key"] for t in tracks if t["active"]]
            assert active_keys == [suffix]


def test_local_intersphinx_drops_none_inventories() -> None:
    mapping = {
        "python": ("https://docs.python.org/3", None),
        "sympy": ("https://docs.sympy.org/latest", None),
    }
    configure_local_intersphinx(mapping, REPO_ROOT)
    assert "python" not in mapping
    assert "sympy" not in mapping
    for _uri, inv in mapping.values():
        assert inv is not None and Path(inv).is_file()


def test_cli_commands() -> None:
    assert cli_main(["--root", str(REPO_ROOT), "summary"]) == 0
    assert cli_main(["--root", str(REPO_ROOT), "verify"]) == 0
