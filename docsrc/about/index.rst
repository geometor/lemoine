:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor.lemoine`` establishes a rigorous, folio-verified Digital Scriptorium edition of **Émile Lemoine's** foundational treatise *Géométrographie, ou Art des constructions géométriques* (Paris: C. Naud, Collection *Scientia* No. 18, 1902), synthesizing the earlier milestones of the *Note d'Oran* (AFAS 1888) and the *Mémoire de Pau* (AFAS 1892 / Gauthier-Villars 1893). This edition unites quantitative geometric construction complexity with minimal-instrument constructibility, establishing the operational metrics that measure how synthetic constructions are physically and algorithmically executed.

The treatise decomposes every classical ruler-and-compass construction into five irreducible elementary acts (:math:`R_1, R_2, C_1, C_2, C_3`), defining an operational calculus that assigns to every geometric construction a rigorous **coefficient of simplicity** (:math:`S = l_1 + l_2 + m_1 + m_2 + m_3`) and **coefficient of exactitude** (:math:`E = l_1 + m_1 + m_2`). By parsing historical propositions, enunciations, operational vectors, and comparative benchmark problems into addressable semantic elements, this digital edition transforms Lemoine's constructive calculus into a computable graph.

Within the GEOMETOR research ecosystem, *Géométrographie* serves as the foundational bridge connecting the axiomatic canon of Euclid's *Elements* (:external+elements:doc:`index`), the modern triangle center taxonomy of Kimberling's *Encyclopedia of Triangle Centers* (:external+etc:doc:`index`), and the classical projective lemmas of Pappus of Alexandria (:external+pappus:doc:`index`). Furthermore, through its **Dual Minimal-Instrument Concordance**, it projects Euclidean benchmarks simultaneously onto the compass-only subspace of Lorenzo Mascheroni (1797) and the single-fixed-circle straightedge subspace of Jean-Victor Poncelet (1822) and Jakob Steiner (1833).

The GEOMETOR Mission
--------------------

The GEOMETOR project, conceived and directed by **phi ARCHITECT**, is dedicated to a multi-generational synthesis of geometry, computation, and symbolic reasoning. At its core, the project operates across three foundational pillars:

Extracting Historical Semantic Knowledge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Moving beyond passive page scans and superficial OCR, GEOMETOR recovers the living deductive architecture of more than 2,300 years of geometric, axiomatic, and philosophical treatises. From ancient Greek codices and Renaissance folios to nineteenth-century synthetic treatises, our Digital Scriptorium elevates prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic knowledge graphs. Every proposition, step, enunciation, and justification is isolated, verified, and interconnected across history.

Exact Symbolic Grounding (``geometor.model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Geometry in GEOMETOR is never approximated through floating-point fuzz or numerical instability. Constructions are anchored in 100% exact symbolic algebra via `SymPy` and Norman Wildberger's Rational Trigonometry invariants (quadrance, spread, and cross-ratio) over exact algebraic number fields. By eliminating rounding errors entirely, geometric configurations retain absolute fidelity, allowing geometric proofs, collinearities, and concyclicities to be verified symbolically with mathematical certainty.

Repurposing Knowledge Across Mediums
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The extracted semantic graphs and exact algebraic models are re-deployed across a unified computational medium: synchronized multi-track **Book Codices** and EPUB 3 editions published with `photon-platform/publish`; computable deductive canons (such as ``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, and ``geometor.divine``); interactive SVG laboratories powered by ``geometor.explorer``; ultra-high-definition (QHD) visual broadcasts; and neuro-symbolic program synthesis guided by ``geometor.seer`` across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

Following the GEOMETOR Digital Scriptorium Iron Law, all operation vectors, problem numbers, and citations in this edition were visually verified page-by-page from 300 DPI archival page scans across three public-domain sources, with UTF-8 transcriptions and SHA-256 checksums recorded in ``resources/geometrographie/sources_manifest.json``:

* **Émile Lemoine**, *Géométrographie, ou Art des constructions géométriques* (Paris: C. Naud, Éditeur, Collection *Scientia*, Série Physico-Mathématique, n° 18, 1902; 88 pp.), collated against *La Géométrographie ou l'Art des constructions géométriques* (Pau: AFAS, 1892; Paris: Gauthier-Villars, 1893).
* **Lorenzo Mascheroni**, *La Geometria del Compasso* (Pavia: Pietro Galeazzi, 1797; collated with the critical edition by Gaetano Fazzari, Palermo: Era Nova, 1901).
* **Jakob Steiner**, *Die geometrischen Constructionen, ausgeführt mittelst der geraden Linie und Eines festen Kreises* (Berlin: Ferdinand Dümmler, 1833; Ostwald's Klassiker der exakten Wissenschaften Nr. 60, edited by A. J. von Oettingen, Leipzig: Wilhelm Engelmann, 1895).

Child Essays & Monographic Studies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :doc:`Émile Lemoine (1840–1912) <emile-lemoine>` — Life, modern triangle geometry (:math:`X(6)`), *L'Intermédiaire des Mathématiciens*, and the invention of *Géométrographie*.
* :doc:`Mascheroni (1797) & Poncelet–Steiner (1833) <mascheroni-steiner>` — Minimal-instrument constructibility from Georg Mohr and Lorenzo Mascheroni to Jakob Steiner and August Adler.
* :doc:`Textual Stemma & Archival Provenance <textual-genesis>` — Oran (1888) → Pau (1892/1893) → *Scientia* No. 18 (1902), 300 DPI multimodal scan verification, and SHA-256 source witnesses.

.. toctree::
   :maxdepth: 1
   :hidden:

   emile-lemoine
   mascheroni-steiner
   textual-genesis
