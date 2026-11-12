"""GEOMETOR Lemoine: Digital Scriptorium Codex of Émile Lemoine's *Géométrographie* (1902)."""

from __future__ import annotations

from geometor.lemoine.compile_codex import (
    compile_apparatus_rst,
    mirror_apparatus_json,
    verify_codex_tracks,
)
from geometor.lemoine.concordance import (
    CODEX_UNITS,
    TRACK_SUFFIXES,
    ConcordanceEntry,
    InstrumentLocus,
    LemoineApparatus,
    OpCount,
    apparatus_slug,
    default_repo_root,
    load_apparatus,
    verify_concordance,
    verify_sources_manifest,
)
from geometor.lemoine.sphinx_ext import (
    configure_local_intersphinx,
    register_french_book_track,
)

__version__ = "0.1.0"

__all__ = [
    "CODEX_UNITS",
    "TRACK_SUFFIXES",
    "ConcordanceEntry",
    "InstrumentLocus",
    "LemoineApparatus",
    "OpCount",
    "__version__",
    "apparatus_slug",
    "compile_apparatus_rst",
    "configure_local_intersphinx",
    "default_repo_root",
    "load_apparatus",
    "mirror_apparatus_json",
    "register_french_book_track",
    "verify_codex_tracks",
    "verify_concordance",
    "verify_sources_manifest",
]
