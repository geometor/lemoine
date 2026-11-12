================
GEOMETOR Lemoine
================

Scholarly Digital Scriptorium **Book Codex**, theme-adaptive ``.euclid-graphic`` SVG figures, and **Dual Minimal-Instrument Constructibility Concordance** for **Émile Lemoine's** *Géométrographie, ou Art des constructions géométriques* (Paris: C. Naud, Collection *Scientia* Phys.-Math. No. 18, 1902), paired with **Lorenzo Mascheroni's** *La Geometria del Compasso* (1797) and **Jakob Steiner's** *Die geometrischen Constructionen, ausgeführt mittelst der geraden Linie und Eines festen Kreises* (1833).

Overview
--------

* **Synchronized 4-Track Book Codex** (``docsrc/geometrographie/``, ``:layout: book``):
  * ``unit-1-operations``: Historical genesis (Oran 1888 → Pau 1892 → *Scientia* 1902), ideal instrument hypotheses, and the five elementary operations (:math:`R_1, R_2, C_1, C_2, C_3`; simplicity :math:`S`; exactitude :math:`E`; Problems I–X).
  * ``unit-2-euclid-benchmarks``: Speculative vs. *géométrographique* Euclid Book I benchmarks (Problems XI–XXIV, including Gaston Tarry's two :math:`S = 9` parallel constructions, :math:`S = 7` mediatrix, :math:`S = 6` compass-only reflection, and :math:`S = 8` single-circle Thales perpendicular).
  * ``unit-3-circles-tangency-golden``: Circumcircle :math:`X(3)` (:math:`S = 15`), tangents (:math:`S = 18`), incircle :math:`X(1)` (:math:`S = 23` vs. :math:`30`), Lemoine–Gouzy mean proportional (:math:`S = 14`), 1-line golden section :math:`\phi` (:math:`S = 18` vs. :math:`25`), compass-only inversion (:math:`5C_1 + 3C_3`), straightedge polar (:math:`12R_1 + 7R_2`), radical axis (:math:`S = 17` vs. Mannheim's :math:`58`), harmonic conjugate (:math:`9R_1 + 6R_2`), and modern triangle centers (:math:`X(2), X(6), X(7), X(8), X(10), X(98), X(99)`, Brocard :math:`\omega, \omega'`).
  * ``unit-4-minimal-instruments``: Lemoine's *équerre*, Mascheroni compass-only geometry (1797), and Poncelet–Steiner fixed-circle straightedge geometry (1833).
* **Standalone ``.euclid-graphic`` SVGs** (``scripts/build_figures.py`` → ``docsrc/_static/figures/``): Nine exact symbolic theme-adaptive diagrams with zero embedded Python in treatise RST.
* **Python Apparatus & CLI** (``geometor.lemoine``): Exact ``OpCount`` validation, SHA-256 archival witness verification, deterministic apparatus RST compiler, and runtime ``fr`` Book Codex track registration.

Usage
-----

.. code-block:: bash

   geometor-lemoine summary
   geometor-lemoine compile-apparatus
   geometor-lemoine verify
   pytest
   ruff check src scripts tests
   publish build
