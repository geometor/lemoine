"""Deterministic RST apparatus compiler and Book Codex track verifier for GEOMETOR Lemoine."""

from __future__ import annotations

import re
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

from geometor.lemoine.concordance import (
    CODEX_LEAVES,
    CODEX_UNITS,
    PAIRED_ARCHIVAL_PLATES,
    TRACK_SUFFIXES,
    LemoineApparatus,
    apparatus_slug,
    default_repo_root,
    load_apparatus,
)

_FORBIDDEN_PY_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"^\s*:py_file:", re.MULTILINE),
    re.compile(r"^\s*\.\.\s+py_file::", re.MULTILINE),
    re.compile(r"^\s*\.\.\s+code-block::\s*py(?:thon)?\b", re.MULTILINE),
)


def mirror_apparatus_json(repo_root: Path | None = None) -> list[Path]:
    """Mirror ``persons.json``, ``citations.json``, and ``glossary.json`` to ``resources/``."""
    root = repo_root or default_repo_root()
    src_dir = root / "resources" / "geometrographie"
    dst_dir = root / "resources"
    written: list[Path] = []
    for fname in ("persons.json", "citations.json", "glossary.json"):
        src = src_dir / fname
        dst = dst_dir / fname
        if src.is_file():
            shutil.copyfile(src, dst)
            written.append(dst)
    return written


def render_persons_rst(app: LemoineApparatus) -> str:
    """Render ``docsrc/geometrographie/persons.rst`` with ``.. _person-<slug>:`` anchors."""
    lines: list[str] = [
        ":navigation: header",
        ":order: 5",
        ":nav_title: People",
        "",
        ".. _persons:",
        "",
        "People",
        "======",
        "",
        ".. rubric:: Authors, Editors & Cited Geometers in the Lemoine Tradition",
        "",
        "Authors, Translators & Editors",
        "------------------------------",
        "",
        ".. _person-lemoine:",
        "",
        "Émile Michel Hyacinthe Lemoine (1840 – 1912)",
        "--------------------------------------------",
        "",
        "*French Civil Engineer, Modern Triangle Geometer & Founder of Geometrography*",
        "",
        "Émile Michel Hyacinthe Lemoine (22 November 1840, Quimper – 21 February 1912, Paris) was an alumnus of the *École Polytechnique* (entering in 1860) and a chief civil engineer in Paris. In 1873 at the AFAS Congress in Lyon, he discovered the concurrency of the triangle's symmedians at the **Lemoine Point** $K = X(6)$ (minimizing squared distances to triangle sides) and introduced the Lemoine circles. In 1888 (Oran) and 1892 (Pau), he formulated **Géométrographie**, published definitively in 1902 (*Scientia* No. 18), establishing the five canonical operations ($R_1, R_2, C_1, C_2, C_3$) and formal measures of simplicity ($S$) and exactitude ($E$). He co-founded *L'Intermédiaire des Mathématiciens* (1894) and repeatedly received the *Prix Francœur* from the French Academy of Sciences.",
        "",
        "----",
        "",
        "Cited Geometers, Philosophers & Scholars",
        "----------------------------------------",
        "",
    ]
    for key in sorted(app.persons.keys(), key=lambda k: app.persons[k]["name"]):
        slug = apparatus_slug(key)
        if slug == "lemoine":
            continue
        p = app.persons[key]
        lines.extend(
            [
                f".. _person-{slug}:",
                "",
                f"**{p['name']}** ({p['dates']}) — *{p['role'].strip()}*",
                f"   {p['bio'].strip()}",
                "",
            ]
        )
    return "\n".join(lines)


def render_bibliography_rst(app: LemoineApparatus) -> str:
    """Render ``docsrc/geometrographie/bibliography.rst`` with ``.. _cite-<slug>:`` anchors."""
    lines: list[str] = [
        ":navigation: header",
        ":order: 6",
        ":nav_title: Bibliography",
        "",
        ".. _bibliography:",
        "",
        "Bibliography",
        "============",
        "",
        ".. rubric:: Primary Treatises, Archival Editions & Constructive Literature",
        "",
    ]
    for key in sorted(app.citations.keys()):
        c = app.citations[key]
        slug = apparatus_slug(key)
        lines.extend(
            [
                f".. _cite-{slug}:",
                "",
                f"**{c['author']}** ({c['year']}) — *{c['work']}*",
                f"   {c['locus']}. {c['publisher']}.",
                "",
                f"   {c['note'].strip()}",
                "",
            ]
        )
    return "\n".join(lines)


def render_glossary_rst(app: LemoineApparatus) -> str:
    """Render ``docsrc/geometrographie/glossary.rst`` with ``.. _term-<slug>:`` anchors."""
    lang_names = {
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "la": "Latin",
        "grc": "Greek",
    }
    lines: list[str] = [
        ":navigation: footer",
        ":nav_title: Glossary",
        "",
        ".. _glossary:",
        "",
        "Glossary",
        "========",
        "",
        ".. rubric:: Constructive & Minimal-Instrument Terminology (*Français · Italiano · Deutsch · English*)",
        "",
    ]
    for key in sorted(app.glossary.keys()):
        g = app.glossary[key]
        slug = apparatus_slug(key)
        lname = lang_names.get(g["language"], g["language"])
        lines.extend(
            [
                f".. _term-{slug}:",
                "",
                f"**{g['headword']}** ({lname} · *{g['translation']}*)",
                f"   {g['definition'].strip()}",
                "",
            ]
        )
    return "\n".join(lines)


def render_concordance_rst(app: LemoineApparatus) -> str:
    """Render ``docsrc/geometrographie/concordance.rst`` comparing Lemoine, Euclid, Mascheroni, and Steiner."""
    unit_titles = dict(CODEX_UNITS)
    lines: list[str] = [
        ":navigation: footer",
        ":nav_title: Concordance",
        "",
        ".. _concordance:",
        "",
        "Dual Minimal-Instrument Concordance",
        "===================================",
        "",
        ".. rubric:: *Géométrographie* (1902) · *Euclid's Elements* · *Mascheroni Compass-Only* (1797) · *Poncelet–Steiner Fixed-Circle* (1833)",
        "",
        "This concordance synthesizes :person:`Émile Lemoine <lemoine>`'s quantitative",
        ":term:`Géométrographie <geometrographie>` (:cite:`lemoine-1902`) with",
        ":person:`Euclid <euclid>`'s axiomatic canon (:cite:`euclid-heath`),",
        ":person:`Lorenzo Mascheroni <mascheroni>`'s compass-only constructions",
        "(:cite:`mascheroni-1797`, :cite:`fazzari-1901`), and :person:`Jakob Steiner <steiner>`'s",
        "straightedge-only constructions with a single fixed circle and its center (:cite:`steiner-1833`).",
        "Every operation vector satisfies Lemoine's exact identities:",
        "",
        ".. math::",
        "",
        "   \\mathrm{Op.} : (l_1 R_1 + l_2 R_2 + m_1 C_1 + m_2 C_2 + m_3 C_3), \\qquad",
        "   S = l_1 + l_2 + m_1 + m_2 + m_3, \\qquad",
        "   E = l_1 + m_1 + m_2.",
        "",
        "Master Operation-Count Summary",
        "------------------------------",
        "",
        ".. list-table:: Classical vs. *Géométrographique* Simplicity & Exactitude",
        "   :header-rows: 1",
        "   :widths: 10 28 12 20 20 10",
        "",
        "   * - Prob.",
        "     - Benchmark Construction",
        "     - Euclid / ETC",
        "     - Classical Symbol (:math:`S, E`)",
        "     - Lemoine Symbol (:math:`S, E`)",
        "     - :math:`\\Delta S`",
    ]

    for entry in app.entries:
        euclid_etc = entry.euclid_ref
        if entry.etc_ref:
            euclid_etc = f"{entry.euclid_ref} · {entry.etc_ref}"
        c_op = entry.classical_ops
        l_op = entry.lemoine_ops
        delta_str = f"{entry.delta_s:+d}" if entry.delta_s != 0 else "0"
        lines.extend(
            [
                f"   * - ``{entry.problem_number}``",
                f"     - :ref:`{entry.title_en} <concordance-{entry.id}>`",
                f"     - {euclid_etc}",
                f"     - :math:`{c_op.symbol}` (:math:`S={c_op.s}, E={c_op.e}`)",
                f"     - :math:`{l_op.symbol}` (:math:`S={l_op.s}, E={l_op.e}`)",
                f"     - ``{delta_str}``",
            ]
        )

    lines.append("")

    for unit_id, unit_heading in CODEX_UNITS:
        unit_entries = [e for e in app.entries if e.unit_id == unit_id]
        if not unit_entries:
            continue
        bar = "-" * len(unit_heading)
        lines.extend(
            [
                unit_heading,
                bar,
                "",
                f"Companion codex part: :doc:`{unit_titles[unit_id]} <{unit_id}/index>`.",
                "",
            ]
        )
        for entry in unit_entries:
            c_op = entry.classical_ops
            l_op = entry.lemoine_ops
            sub = f"{entry.problem_number} — {entry.title_en}"
            tilde = "~" * len(sub)
            meta_parts = [
                f"**Lemoine Folio**: pp. {entry.folio_page}",
                f"**Euclid**: {entry.euclid_ref}",
                f"**Elements DAG**: {entry.elements_ref}",
            ]
            if entry.etc_ref:
                meta_parts.append(f"**ETC**: {entry.etc_ref}")
            if entry.pappus_ref:
                meta_parts.append(f"**Projective**: {entry.pappus_ref}")

            lines.extend(
                [
                    f".. _concordance-{entry.id}:",
                    "",
                    sub,
                    tilde,
                    "",
                    f"*{entry.title_fr}*",
                    "",
                    " | ".join(meta_parts),
                    "",
                    (
                        f"- **Classical / Speculative Construction**: :math:`{c_op.symbol}` "
                        f"— Simplicity :math:`S = {c_op.s}`, Exactitude :math:`E = {c_op.e}` "
                        f"({c_op.lines} lines, {c_op.circles} circles)."
                    ),
                    (
                        f"- **Lemoine Géométrographique Synthesis**: :math:`{l_op.symbol}` "
                        f"— Simplicity :math:`S = {l_op.s}`, Exactitude :math:`E = {l_op.e}` "
                        f"({l_op.lines} lines, {l_op.circles} circles)."
                    ),
                    (
                        f"- **Mascheroni Compass-Only Counterpart** (*{entry.mascheroni.locus}*): "
                        f"{entry.mascheroni.method}"
                    ),
                    (
                        f"- **Poncelet–Steiner Fixed-Circle Counterpart** (*{entry.steiner.locus}*): "
                        f"{entry.steiner.method}"
                    ),
                    f"- **Critical Note**: {entry.notes}",
                    "",
                ]
            )

    return "\n".join(lines)


def compile_apparatus_rst(repo_root: Path | None = None) -> list[Path]:
    """Compile ``concordance.rst``, ``bibliography.rst``, ``persons.rst``, and ``glossary.rst`` and mirror JSON apparatus."""
    root = repo_root or default_repo_root()
    app = load_apparatus(root)
    mirror_apparatus_json(root)

    codex_dir = root / "docsrc" / "geometrographie"
    codex_dir.mkdir(parents=True, exist_ok=True)

    outputs = {
        codex_dir / "bibliography.rst": render_bibliography_rst(app),
        codex_dir / "glossary.rst": render_glossary_rst(app),
        codex_dir / "concordance.rst": render_concordance_rst(app),
    }
    if not (codex_dir / "people" / "index.rst").is_file():
        outputs[codex_dir / "persons.rst"] = render_persons_rst(app)
    written: list[Path] = []
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written


def _validate_euclid_svg(svg_path: Path, rel_label: str) -> list[str]:
    """Verify XML well-formedness, ``euclid-graphic`` class, and 5 canonical layers."""
    errs: list[str] = []
    svg_text = svg_path.read_text(encoding="utf-8")
    try:
        ET.fromstring(svg_text)
    except ET.ParseError as exc:
        errs.append(f"{rel_label} is malformed XML: {exc}")
    if 'class="euclid-graphic"' not in svg_text:
        errs.append(f'{rel_label} missing class="euclid-graphic"')
    for gid in ("elements", "graphics", "highlights", "points", "labels"):
        if f'id="{gid}"' not in svg_text:
            errs.append(f'{rel_label} missing required SVG layer <g id="{gid}">')
    return errs


def verify_codex_tracks(repo_root: Path | None = None) -> list[str]:
    """Verify 4 Parts, 25 atomic leaves (100 track files), ``:folio:`` provenance, paired plates, SVGs, and zero embedded Python."""
    root = repo_root or default_repo_root()
    codex_dir = root / "docsrc" / "geometrographie"
    errors: list[str] = []

    index_rst = codex_dir / "index.rst"
    if not index_rst.is_file():
        errors.append(f"Missing Book Codex index: {index_rst}")
    else:
        idx_text = index_rst.read_text(encoding="utf-8")
        if ":layout: book" not in idx_text:
            errors.append("docsrc/geometrographie/index.rst missing ':layout: book'")
        if ":folio:" not in idx_text:
            errors.append("docsrc/geometrographie/index.rst missing ':folio:' badge")

    for unit_id, _title in CODEX_UNITS:
        part_index = codex_dir / unit_id / "index.rst"
        if not part_index.is_file():
            errors.append(f"Missing Part index: {part_index.relative_to(root)}")
        else:
            ptext = part_index.read_text(encoding="utf-8")
            if ":layout: book" not in ptext:
                errors.append(f"{part_index.relative_to(root)} missing ':layout: book'")
            if ":folio:" not in ptext:
                errors.append(f"{part_index.relative_to(root)} missing ':folio:' badge")

    for part_id, leaf_id, expected_folio, _title in CODEX_LEAVES:
        leaf_dir = codex_dir / part_id / leaf_id
        for suffix in TRACK_SUFFIXES:
            track_file = leaf_dir / f"{leaf_id}-{suffix}.rst"
            if not track_file.is_file():
                errors.append(f"Missing codex track file: {track_file.relative_to(root)}")
                continue
            text = track_file.read_text(encoding="utf-8")
            rel = track_file.relative_to(root)
            if ":layout: book" not in text:
                errors.append(f"{rel} missing ':layout: book'")
            if f":folio: {expected_folio}" not in text:
                errors.append(f"{rel} missing ':folio: {expected_folio}' frontmatter")
            if ":tracks:" not in text:
                errors.append(f"{rel} missing ':tracks:' frontmatter")
            if suffix in ("en", "fr") and ".. folio::" not in text:
                errors.append(f"{rel} missing '.. folio::' page anchors")

    pic_re = re.compile(r"^\s*\.\.\s+picture::\s+(\S+)", re.MULTILINE)
    referenced_rel_plates: set[Path] = set()
    if codex_dir.is_dir():
        for rst_file in sorted(codex_dir.rglob("*.rst")):
            text = rst_file.read_text(encoding="utf-8")
            for pat in _FORBIDDEN_PY_PATTERNS:
                if pat.search(text):
                    errors.append(
                        f"Forbidden embedded Python construct ({pat.pattern}) in {rst_file.relative_to(root)}"
                    )
            for pic in pic_re.findall(text):
                if not pic.startswith("/"):
                    referenced_rel_plates.add((rst_file.parent / pic).resolve())

    # Validate all 11 paired archival bitmaps + calibrated SVGs and ensure zero orphans
    expected_plates: set[Path] = set()
    for part_id, leaf_id, folio in PAIRED_ARCHIVAL_PLATES:
        leaf_dir = codex_dir / part_id / leaf_id
        png_path = leaf_dir / f"{folio}.g1.png"
        svg_path = leaf_dir / f"{folio}.g1.svg"
        expected_plates.add(png_path.resolve())
        expected_plates.add(svg_path.resolve())
        if not png_path.is_file() or png_path.stat().st_size < 1024:
            errors.append(f"Missing or empty archival bitmap: {png_path.relative_to(root)}")
        if not svg_path.is_file():
            errors.append(f"Missing calibrated archival SVG: {svg_path.relative_to(root)}")
        else:
            errors.extend(_validate_euclid_svg(svg_path, str(svg_path.relative_to(root))))
        if png_path.resolve() not in referenced_rel_plates:
            errors.append(f"Unreferenced archival bitmap: {png_path.relative_to(root)}")
        if svg_path.resolve() not in referenced_rel_plates:
            errors.append(f"Unreferenced archival SVG: {svg_path.relative_to(root)}")

    actual_plates = {
        p.resolve()
        for pat in ("*.g[0-9].png", "*.g[0-9].svg")
        for p in codex_dir.rglob(pat)
    }
    for orphan in sorted(actual_plates - expected_plates):
        errors.append(f"Orphaned archival plate file: {orphan.relative_to(root)}")

    fig_dir = root / "docsrc" / "_static" / "figures"
    svg_files = sorted(fig_dir.glob("*.svg")) if fig_dir.is_dir() else []
    if len(svg_files) < 9:
        errors.append(
            f"Expected at least 9 standalone .euclid-graphic SVGs in docsrc/_static/figures/, found {len(svg_files)}"
        )
    for svg_path in svg_files:
        errors.extend(_validate_euclid_svg(svg_path, svg_path.name))

    return errors
