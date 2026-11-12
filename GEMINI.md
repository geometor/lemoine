# GEOMETOR • lemoine

Scholarly Digital Scriptorium Book Codex (`:layout: book`) and Dual Minimal-Instrument Constructibility Concordance for **Émile Lemoine's** *Géométrographie, ou Art des constructions géométriques* (1888 / 1892 / Collection *Scientia* No. 18, 1902), paired with **Lorenzo Mascheroni's** *La Geometria del Compasso* (1797) and **Jakob Steiner's** *Die geometrischen Constructionen* (1833).

## Repository Layout

- `src/geometor/lemoine/`:
  - `concordance.py`: `OpCount` operation-vector algebra (`S = l1+l2+m1+m2+m3`, `E = l1+m1+m2`, `lines = l2`, `circles = m3`), `ConcordanceEntry`, `LemoineApparatus`, and SHA-256 `sources_manifest.json` verification.
  - `compile_codex.py`: Deterministic compiler generating `docsrc/geometrographie/{concordance,bibliography,persons,glossary}.rst`, mirroring JSON apparatus to `resources/`, and verifying 4-track synchronization, `.euclid-graphic` SVG layers, and zero embedded Python in treatise RST.
  - `sphinx_ext.py`: Runtime registration of the `fr` (`"French (1902)"`) Book Codex track in `photon_platform.publish.book` and offline-safe local intersphinx binding across sister `geometor/*` repositories.
  - `cli.py`: `geometor-lemoine` CLI (`summary`, `compile-apparatus`, `verify`).
- `scripts/build_figures.py`: Exact SymPy generator emitting all 9 standalone theme-adaptive `.euclid-graphic` SVG plates into `docsrc/_static/figures/`.
- `resources/geometrographie/`:
  - `concordance.json`, `persons.json`, `citations.json`, `glossary.json`, `sources_manifest.json`
  - `sources/`: UTF-8 primary archival witnesses (`lemoine_geometrographie_fr.txt`, `mascheroni_1797_compasso_it.txt`, `steiner_1833_constructionen_de.txt`; raw `.pdf` scans are git-ignored).
- `docsrc/geometrographie/`: 4-unit, 4-track synchronized Book Codex (`-en.rst`, `-fr.rst`, `-summary.rst`, `-notes.rst`) + critical apparatus.
- `tests/test_lemoine.py`: Comprehensive verification suite.

## Architectural Mandates

1. **Zero Embedded Python in Historical Codex RST**: Never embed `py_file` or `.. code-block:: python` inside `docsrc/geometrographie/`. Generate figures exclusively as standalone `.euclid-graphic` SVGs via `scripts/build_figures.py` and embed with `.. picture:: /_static/figures/<name>.svg`.
2. **Multimodal Scan Fidelity**: All operation counts, problem numbers, and citations are verified directly from 300 DPI page scans rather than unverified OCR.
3. **Offline Sandbox Commands**:
   ```bash
   pytest
   ruff check src scripts tests
   publish build
   ```
