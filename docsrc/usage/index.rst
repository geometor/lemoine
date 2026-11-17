:navigation: header
:order: 20
:nav_title: Usage

.. _lemoine-usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the GEOMETOR Interactive Digital Edition

Welcome to the **GEOMETOR Lemoine** digital edition. This interactive edition unites Émile Lemoine's landmark treatise *Géométrographie, ou Art des constructions géométriques* (1902) with primary French source texts, modern English translations, operation-count algebra, and the Dual Minimal-Instrument Concordance to Lorenzo Mascheroni and Jakob Steiner.

Synchronized Reading Tracks
---------------------------

Every unit of the **Geometrography Codex** (:doc:`/geometrographie/index`) is organized across four synchronized reading tracks:

* **English (`-en`)**: Modern scholarly English translation translated directly from Lemoine's French text.
* **French (`-fr`)**: Verbatim primary French text edited from the 1902 *Scientia* edition (Paris: C. Naud).
* **Summary (`-summary`)**: Compact operational summaries isolating benchmark problems, operation counts, and simplicity/exactitude coefficients.
* **Notes (`-notes`)**: In-depth commentary detailing historical context, algebraic proofs, and links to classical and modern geometers.

Switch between tracks anytime using the track navigation bar at the top of each chapter page.

Primary-Source Folio Milestones
-------------------------------

The digital edition maintains strict correspondence with the primary French witnesses:

* **Archival Folio Anchors**: Marginal ``[p. N]`` milestone links correspond to original pagination in the 1902 *Scientia* imprint.
* **Source Manifest**: Every source document is cataloged and cryptographically verified in the SHA-256 manifest.

Interactive Diagrams & Deductive Links
--------------------------------------

Figures throughout the edition are rendered as responsive vector graphics:

* **Geometric Elements (``:g:``)**: In-text geometric labels connect directly to labeled construction lines, points, and circles.
* **Operation Formulas (``:eq:``)**: Operation symbols detail exact counts of straightedge operations (:math:`R_1, R_2`) and compass operations (:math:`C_1, C_2, C_3`), evaluating Simplicity :math:`S = l_1 + l_2 + m_1 + m_2 + m_3` and Exactitude :math:`E = l_1 + m_1 + m_2`.
* **Justifications (``:just:``)**: Inline citations connect operational steps directly to Euclid's *Elements* or Mascheroni's and Steiner's restricted-instrument theorems.

Full-Text Search with In-Page Highlighting
------------------------------------------

The built-in documentation search engine indexes all units, commentary notes, and module documentation.
Search queries pass search terms via `?highlight=`, highlighting queried expressions throughout the text.

Categories, Tags & Collection Views
-----------------------------------

Explore content through structured taxonomies:

* Filter treatises, notes, and logs by mathematical subject, historical era, or tag using the sidebar facets.
* On collection index pages like :doc:`/log/index`, use the view toggle buttons to display entries as **Cards**, **Banners**, or **Lists**.

People, Bibliography & Glossary Tooltips
----------------------------------------

Rich interconnected registers provide immediate context:

* **People (``:person:``)**: Hover or click names like :person:`Émile Lemoine <lemoine>`, :person:`Lorenzo Mascheroni <mascheroni>`, or :person:`Jakob Steiner <steiner>` to open detailed biographies in :doc:`/geometrographie/people/index`.
* **Citations (``:cite:``)**: Citations connect directly to full bibliographical records in :doc:`/geometrographie/bibliography`.
* **Terms (``:term:``)**: Foundational concepts like :term:`géométrographie <geometrographie>`, :term:`simplicité <simplicite>`, and :term:`exactitude <exactitude>` link to definitions in :doc:`/geometrographie/glossary`.
* **Display Themes**: Switch between Light and Dark display modes using the theme toggle in the header navigation bar.

Command-Line & Python API
-------------------------

The companion package ``geometor.lemoine`` provides exact algebraic verifiers for operation counts and simplicity metrics:

.. code-block:: bash

   # Run CLI help and inspect available tools
   /home/phi/PROJECTS/geometor/.venv/bin/python -m geometor.lemoine --help

   # Run test suite
   /home/phi/PROJECTS/geometor/.venv/bin/pytest

Explore complete module documentation in :doc:`/modules/index`.
