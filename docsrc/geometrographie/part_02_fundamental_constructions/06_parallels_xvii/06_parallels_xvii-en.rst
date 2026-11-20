:layout: book
:canonical_id: Prob. XVII
:order: 2
:folio: 0025
:tracks: English: 06_parallels_xvii-en | French: 06_parallels_xvii-fr | Summary: 06_parallels_xvii-summary | Notes: 06_parallels_xvii-notes

.. _lemoine-06_parallels_xvii-en:
.. _lemoine-en-parallel-tarry:

Problem XVII: Parallel Through an External Point
================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 9–10, fols. ``0025–0026``)

.. folio:: 0025
   :page: p. 9

**Problem XVII (Euclid I.31).** *Through a given point* :g:`A` *outside a traced straight line* :g:`BC`, *to draw a straight line parallel to* :g:`BC`.

* **Classical Alternate-Angle Method** (:math:`S = 11, E = 7`): Standard textbook execution (cf. :person:`Euclid <euclid>` I.31) costs :math:`2R_1 + R_2 + 5C_1 + 3C_3` (1 line, 3 circles). In footnote (*) on p. 9, Lemoine even remarks on the polar locus :math:`\rho = l / \sin(\omega/2)` swept by the opposite intersection :math:`D'` as the auxiliary radius varies.
* **Gaston Tarry's First Géométrographique Construction (Two Circles, :math:`S = 9, E = 6`)**: Communicated to :person:`Lemoine <lemoine>` by :person:`Gaston Tarry <tarry>`, draw an arbitrary circle passing through :g:`A` (:math:`C_1 + C_3`, Application V) cutting :g:`BC` in two points :math:`B` and :math:`C`. Capture chord :math:`BA` and sweep :math:`C(BA)` (:math:`3C_1 + C_3`) cutting the first circle at :g:`D`, and join :g:`AD` (:math:`2R_1 + R_2`):

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 4C_1 + 2C_3\right), \qquad S = 9, \quad E = 6 \quad (1\text{ line}, 2\text{ circles}).

* **Gaston Tarry's Second Géométrographique Construction (Single-Aperture Rhombus, :math:`S = 9, E = 5`)**: Open the compass to any sufficient radius :math:`R`. Sweep :g:`A(R)` (:math:`C_1 + C_3`) cutting :g:`BC` at :g:`P`; keeping the **same aperture** :math:`R`, sweep :g:`P(R)` (:math:`C_1 + C_3`) cutting :g:`BC` at :g:`Q`, and :g:`Q(R)` (:math:`C_1 + C_3`) cutting the first arc :g:`A(R)` at :g:`D`. Since :math:`PA = PQ = QD = DA = R`, quadrilateral :g:`APQD` is a rhombus, and joining :g:`AD` (:math:`2R_1 + R_2`) gives the required parallel:

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 3C_1 + 3C_3\right), \qquad S = 9, \quad E = 5 \quad (1\text{ line}, 3\text{ circles}).

.. picture:: /_static/figures/fig_parallel_comparison.svg
   :alt: Comparison of classical parallel construction (S = 11) and Gaston Tarry's single-aperture rhombus (S = 9, E = 5)
   :caption: Problem XVII: Classical S = 11 construction contrasted with Gaston Tarry's S = 9, E = 5 single-aperture rhombus APQD.

.. folio:: 0026
   :page: p. 10

**Remark on Un-Traced Lines (p. 10).** If the target line is given only by two points :math:`B, C` *without being traced*, drawing :math:`C(BA)` and :math:`A(BC)` meeting at :math:`D` (:math:`6C_1 + 2C_3`) and joining :math:`AD` (:math:`2R_1 + R_2`) costs :math:`2R_1 + R_2 + 6C_1 + 2C_3` (:math:`S = 11, E = 8`, 1 line, 2 circles)—and stopping at point :math:`D` alone matches :person:`Mascheroni <mascheroni>`'s compass-only parallelogram (:cite:`mascheroni-1797`, Libro IV, § 80)!
