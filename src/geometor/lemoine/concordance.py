"""Structured apparatus, operation calculus, and dual minimal-instrument concordance for GEOMETOR Lemoine."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

CODEX_UNITS: tuple[tuple[str, str], ...] = (
    (
        "unit-1-operations",
        "Unit I: Historical Genesis, Methodological Criteria & The Five Elementary Operations",
    ),
    (
        "unit-2-euclid-benchmarks",
        "Unit II: Fundamental Speculative vs. Géométrographique Constructions (Euclid Book I Benchmarks)",
    ),
    (
        "unit-3-circles-tangency-golden",
        "Unit III: Circles, Tangency, Golden Section, Projective Polarity & Modern Triangle Centers",
    ),
    (
        "unit-4-minimal-instruments",
        "Unit IV: Restricted & Alternative Instruments — Équerre, Mascheroni Compass-Only & Poncelet–Steiner Fixed-Circle",
    ),
)

TRACK_SUFFIXES: tuple[str, ...] = ("en", "fr", "summary", "notes")


def default_repo_root() -> Path:
    """Return the root directory of the ``geometor/lemoine`` repository."""
    return Path(__file__).resolve().parents[3]


def apparatus_slug(raw_key: str) -> str:
    """Normalize an apparatus key to the ``photon_platform.publish`` cross-reference slug."""
    return re.sub(r"[^a-z0-9]+", "-", raw_key.lower()).strip("-")


@dataclass(frozen=True, slots=True)
class OpCount:
    """Exact Lemoine *Géométrographie* operation-count vector and derived invariants."""

    r1: int
    r2: int
    c1: int
    c2: int
    c3: int
    s: int
    e: int
    lines: int
    circles: int
    symbol: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> OpCount:
        """Instantiate an :class:`OpCount` from a JSON mapping."""
        return cls(
            r1=int(data["r1"]),
            r2=int(data["r2"]),
            c1=int(data["c1"]),
            c2=int(data["c2"]),
            c3=int(data["c3"]),
            s=int(data["s"]),
            e=int(data["e"]),
            lines=int(data["lines"]),
            circles=int(data["circles"]),
            symbol=str(data["symbol"]),
        )

    def validate(self, label: str = "") -> list[str]:
        """Verify Lemoine's four fundamental algebraic identities on this operation symbol."""
        errors: list[str] = []
        prefix = f"[{label}] " if label else ""
        for name, val in (
            ("r1", self.r1),
            ("r2", self.r2),
            ("c1", self.c1),
            ("c2", self.c2),
            ("c3", self.c3),
        ):
            if val < 0:
                errors.append(f"{prefix}Negative operation count {name}={val}")

        expected_s = self.r1 + self.r2 + self.c1 + self.c2 + self.c3
        if self.s != expected_s:
            errors.append(
                f"{prefix}Simplicity mismatch: s={self.s} != r1+r2+c1+c2+c3={expected_s}"
            )

        expected_e = self.r1 + self.c1 + self.c2
        if self.e != expected_e:
            errors.append(
                f"{prefix}Exactitude mismatch: e={self.e} != r1+c1+c2={expected_e}"
            )

        if self.lines != self.r2:
            errors.append(
                f"{prefix}Traced line count mismatch: lines={self.lines} != r2={self.r2}"
            )

        if self.circles != self.c3:
            errors.append(
                f"{prefix}Traced circle count mismatch: circles={self.circles} != c3={self.c3}"
            )

        if not self.symbol.strip():
            errors.append(f"{prefix}Empty operation symbol string")

        return errors


@dataclass(frozen=True, slots=True)
class InstrumentLocus:
    """Minimal-instrument counterpart locus and constructive method (Mascheroni or Steiner)."""

    locus: str
    method: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> InstrumentLocus:
        """Instantiate an :class:`InstrumentLocus` from a JSON mapping."""
        return cls(
            locus=str(data["locus"]).strip(),
            method=str(data["method"]).strip(),
        )


@dataclass(frozen=True, slots=True)
class ConcordanceEntry:
    """Single canonical construction benchmark across Lemoine, Euclid, Mascheroni, and Steiner."""

    id: str
    problem_number: str
    title_en: str
    title_fr: str
    unit_id: str
    folio_page: str
    euclid_ref: str
    elements_ref: str
    etc_ref: str | None
    pappus_ref: str | None
    classical_ops: OpCount
    lemoine_ops: OpCount
    mascheroni: InstrumentLocus
    steiner: InstrumentLocus
    notes: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ConcordanceEntry:
        """Parse a concordance entry from ``concordance.json``."""
        return cls(
            id=str(data["id"]),
            problem_number=str(data["problem_number"]),
            title_en=str(data["title_en"]),
            title_fr=str(data["title_fr"]),
            unit_id=str(data["unit_id"]),
            folio_page=str(data["folio_page"]),
            euclid_ref=str(data["euclid_ref"]),
            elements_ref=str(data["elements_ref"]),
            etc_ref=data.get("etc_ref"),
            pappus_ref=data.get("pappus_ref"),
            classical_ops=OpCount.from_dict(data["classical_ops"]),
            lemoine_ops=OpCount.from_dict(data["lemoine_ops"]),
            mascheroni=InstrumentLocus.from_dict(data["mascheroni"]),
            steiner=InstrumentLocus.from_dict(data["steiner"]),
            notes=str(data["notes"]),
        )

    @property
    def delta_s(self) -> int:
        """Operations saved by ``lemoine_ops`` relative to ``classical_ops`` (``S_classical - S_lemoine``)."""
        return self.classical_ops.s - self.lemoine_ops.s

    @property
    def delta_e(self) -> int:
        """Exactitude reduction achieved by ``lemoine_ops`` relative to ``classical_ops``."""
        return self.classical_ops.e - self.lemoine_ops.e


@dataclass(frozen=True, slots=True)
class LemoineApparatus:
    """Loaded scholarly apparatus and dual minimal-instrument concordance."""

    metadata: dict[str, Any]
    entries: tuple[ConcordanceEntry, ...]
    persons: dict[str, dict[str, str]]
    citations: dict[str, dict[str, str]]
    glossary: dict[str, dict[str, str]]
    sources_manifest: dict[str, Any]


def load_apparatus(repo_root: Path | None = None) -> LemoineApparatus:
    """Load ``concordance.json``, ``persons.json``, ``citations.json``, ``glossary.json``, and ``sources_manifest.json``."""
    root = repo_root or default_repo_root()
    res_dir = root / "resources" / "geometrographie"

    concordance_raw = json.loads(
        (res_dir / "concordance.json").read_text(encoding="utf-8")
    )
    persons_raw = json.loads((res_dir / "persons.json").read_text(encoding="utf-8"))
    citations_raw = json.loads((res_dir / "citations.json").read_text(encoding="utf-8"))
    glossary_raw = json.loads((res_dir / "glossary.json").read_text(encoding="utf-8"))
    manifest_raw = json.loads(
        (res_dir / "sources_manifest.json").read_text(encoding="utf-8")
    )

    entries = tuple(
        ConcordanceEntry.from_dict(item) for item in concordance_raw.get("entries", [])
    )
    return LemoineApparatus(
        metadata=dict(concordance_raw.get("metadata", {})),
        entries=entries,
        persons=dict(persons_raw),
        citations=dict(citations_raw),
        glossary=dict(glossary_raw),
        sources_manifest=dict(manifest_raw),
    )


def verify_sources_manifest(repo_root: Path | None = None) -> list[str]:
    """Verify SHA-256 digests and non-empty witness files listed in ``sources_manifest.json``."""
    root = repo_root or default_repo_root()
    manifest_path = root / "resources" / "geometrographie" / "sources_manifest.json"
    if not manifest_path.is_file():
        return [f"Missing sources_manifest.json at {manifest_path}"]

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    witnesses = manifest.get("witnesses", [])
    if len(witnesses) < 3:
        return [
            f"Expected at least 3 primary witnesses (Lemoine, Mascheroni, Steiner), found {len(witnesses)}"
        ]

    errors: list[str] = []
    for wit in witnesses:
        wid = wit.get("id", "<unknown>")
        rel_path = wit.get("path") or wit.get("local_witness", "")
        expected_hash = wit.get("sha256", "")
        wpath = root / rel_path
        if not wpath.is_file():
            errors.append(f"[{wid}] Missing witness file: {rel_path}")
            continue
        raw_bytes = wpath.read_bytes()
        if len(raw_bytes) < 512:
            errors.append(f"[{wid}] Witness file suspiciously small ({len(raw_bytes)} bytes)")
        actual_hash = hashlib.sha256(raw_bytes).hexdigest()
        if actual_hash != expected_hash:
            errors.append(
                f"[{wid}] SHA-256 mismatch for {rel_path}: expected {expected_hash}, got {actual_hash}"
            )
    return errors


def verify_concordance(apparatus: LemoineApparatus | None = None) -> list[str]:
    """Validate all concordance entries, operation counts, unit references, and apparatus dictionaries."""
    app = apparatus or load_apparatus()
    errors: list[str] = []

    valid_unit_ids = {u[0] for u in CODEX_UNITS}
    seen_ids: set[str] = set()

    if len(app.entries) < 20:
        errors.append(
            f"Expected at least 20 canonical concordance entries, found {len(app.entries)}"
        )

    units_covered: set[str] = set()
    for entry in app.entries:
        if entry.id in seen_ids:
            errors.append(f"Duplicate concordance entry id: {entry.id}")
        seen_ids.add(entry.id)

        if entry.unit_id not in valid_unit_ids:
            errors.append(
                f"[{entry.id}] Unknown unit_id '{entry.unit_id}' (expected one of {sorted(valid_unit_ids)})"
            )
        units_covered.add(entry.unit_id)

        errors.extend(entry.classical_ops.validate(f"{entry.id}.classical_ops"))
        errors.extend(entry.lemoine_ops.validate(f"{entry.id}.lemoine_ops"))

        if not entry.mascheroni.locus or not entry.mascheroni.method:
            errors.append(f"[{entry.id}] Incomplete Mascheroni locus/method")
        if not entry.steiner.locus or not entry.steiner.method:
            errors.append(f"[{entry.id}] Incomplete Steiner locus/method")

    missing_units = valid_unit_ids - units_covered
    if missing_units:
        errors.append(
            f"Concordance missing entries for units: {sorted(missing_units)}"
        )

    for key, person in app.persons.items():
        if key != apparatus_slug(key):
            errors.append(f"Person key '{key}' is not normalized slug '{apparatus_slug(key)}'")
        for req in ("name", "dates", "role", "bio"):
            if not person.get(req, "").strip():
                errors.append(f"Person '{key}' missing required field '{req}'")

    for key, cite in app.citations.items():
        if key != apparatus_slug(key):
            errors.append(f"Citation key '{key}' is not normalized slug '{apparatus_slug(key)}'")
        for req in ("author", "work", "locus", "year", "publisher", "note"):
            if not cite.get(req, "").strip():
                errors.append(f"Citation '{key}' missing required field '{req}'")

    for key, term in app.glossary.items():
        if key != apparatus_slug(key):
            errors.append(f"Glossary key '{key}' is not normalized slug '{apparatus_slug(key)}'")
        for req in ("headword", "language", "translation", "definition"):
            if not term.get(req, "").strip():
                errors.append(f"Glossary '{key}' missing required field '{req}'")

    return errors
