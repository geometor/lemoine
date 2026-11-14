=========
changelog
=========

0.1.1 (2026-11-13)
------------------

- **added**: Added track-aware primary-source folio map (``resources/geometrographie/folio_map.json``) resolving 30/30 folio directives to verified French text loci and archival source lines.

0.1.0 (2026-11-12)
------------------

* **4-Track Synchronized Book Codex** (``docsrc/geometrographie/``, ``:layout: book``):
  * Added runtime ``fr`` (``"French (1902)"``) companion track registration in ``geometor.lemoine.sphinx_ext`` alongside ``en``, ``summary``, and ``notes`` across four canonical units (``unit-1-operations``, ``unit-2-euclid-benchmarks``, ``unit-3-circles-tangency-golden``, ``unit-4-minimal-instruments``).
* **Dual Minimal-Instrument Constructibility Concordance**:
  * Curated 26 folio-verified construction benchmarks in ``resources/geometrographie/concordance.json`` mapping Euclid's *Elements*, ``geometor/elements``, and ``geometor/etc`` across Lemoine's *Géométrographie* (1892/1902), Mascheroni's *La Geometria del Compasso* (1797 / Fazzari 1901), and Steiner's *Die geometrischen Constructionen* (1833 / Ostwald 1895).
  * Added SHA-256 verified UTF-8 archival witnesses in ``resources/geometrographie/sources/`` and full scholarly apparatus (``persons.json``, ``citations.json``, ``glossary.json``).
* **Standalone ``.euclid-graphic`` SVG Plates**:
  * Implemented ``scripts/build_figures.py`` using exact SymPy coordinates to emit 9 theme-adaptive ``.euclid-graphic`` SVGs in ``docsrc/_static/figures/`` with zero embedded Python in treatise RST.
* **Python Package & Verification Suite**:
  * Implemented ``geometor.lemoine`` (``concordance``, ``compile_codex``, ``sphinx_ext``, ``cli``) and ``tests/test_lemoine.py``.
