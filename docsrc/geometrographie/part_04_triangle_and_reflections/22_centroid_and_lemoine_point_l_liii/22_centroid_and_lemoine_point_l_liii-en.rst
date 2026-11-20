:layout: book
:canonical_id: Probs. L–LIII
:order: 3
:folio: 0058
:tracks: English: 22_centroid_and_lemoine_point_l_liii-en | French: 22_centroid_and_lemoine_point_l_liii-fr | Summary: 22_centroid_and_lemoine_point_l_liii-summary | Notes: 22_centroid_and_lemoine_point_l_liii-notes

.. _lemoine-22_centroid_and_lemoine_point_l_liii-en:
.. _lemoine-en-triangle-centers:

Problems L–LIII: Centroid X(2), Lemoine Point X(6) & Lemoine Line
=================================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 42–45, fols. ``0058–0061``)

.. folio:: 0058
   :page: p. 42

Having set the generic trilinear baseline at :math:`S = 54` (Problem XLIX), :person:`Lemoine <lemoine>` turns to the foundational centers of modern triangle geometry (:cite:`lemoine-1873`, :cite:`altshiller-court-1952`; cross-referenced to :person:`Clark Kimberling <kimberling>`'s *ETC* (:cite:`kimberling-etc`) in :external+etc:doc:`index`):

**Problem L — Centroid :g:`G` :math:`= X(2)` (Trilinears :math:`\frac{1}{a} : \frac{1}{b} : \frac{1}{c}`).**
Naive trilinear plotting (constructing :math:`a^2/b, a^2/c` via XXXIV + XLIX) would cost :math:`S = 84`!

.. folio:: 0059
   :page: p. 43

* *Method (a) — Two Medians via Perpendicular Bisectors*: :math:`8R_1 + 4R_2 + 3C_1 + 3C_3` (:math:`S = 18, E = 11`, 4 lines, 3 circles).
* *Method (b) — Parallelogram Shortcut (Lemoine's Optimum, :math:`S = 17`)*: Sweep :math:`B(CA)` and :math:`A(CB)` meeting at :math:`C'` (:math:`6C_1 + 2C_3`), draw :math:`C'B` cutting :math:`B(CA)` again at :math:`A'` (:math:`2R_1 + R_2`), and intersect medians :math:`CC'` and :math:`AA'` (:math:`4R_1 + 2R_2`) at :g:`G` (:ref:`concordance-centroid-x2`):

.. math::

   \mathrm{Op.} : \left(6R_1 + 3R_2 + 6C_1 + 2C_3\right), \qquad S = 17, \quad E = 12 \quad (3\text{ lines}, 2\text{ circles}).

**Problem LI — :term:`Lemoine Symmedian Point <point-de-lemoine>` :g:`K` :math:`= X(6)` (Trilinears :math:`a : b : c`, :cite:`lemoine-1873`).**
Directly from Problem XLIX, trilinears :math:`a : b : c` cost :math:`S = 54`. Lemoine cuts the cost **exactly in half** using his antiparallel/rhombus symmedian construction (drawing **only two straight lines**—the two symmedians :g:`AK` and :g:`BK`!):
1. On :g:`AC` mark :math:`AC' = AB` via :math:`A(AB)` (:math:`2C_1 + C_3`), and keeping the compass pivot at :g:`A`, mark :math:`AB' = AC` on :g:`AB` (:math:`C_1 + C_3`), creating an :term:`antiparallel <antiparallele>` segment :g:`PaQa` (:math:`B'C'`).
2. Sweep :math:`C'(AC)` (:math:`C_1 + C_3`, radius already in compass!) and :math:`B'(AB)` (:math:`3C_1 + C_3`) meeting at :math:`A'`; draw symmedian :g:`AK` = :math:`AA'` (:math:`2R_1 + R_2`, costing :math:`2R_1 + R_2 + 7C_1 + 4C_3`, :math:`S = 14` for a single symmedian!).
3. Construct the second symmedian :g:`BK` saving one :math:`C_1` (:math:`2R_1 + R_2 + 6C_1 + 4C_3`, since radius :math:`AB` is already held!):

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 13C_1 + 8C_3\right), \qquad S = 27, \quad E = 17 \quad (2\text{ lines}, 8\text{ circles}).

With two compasses, Lemoine saves :math:`4C_1 + C_3` to reach :math:`S = 22, E = 13` (2 lines, 7 circles, :ref:`concordance-lemoine-point-x6`)!

.. picture:: /_static/figures/fig_lemoine_symmedian_x6.svg
   :alt: Lemoine Symmedian Point K = X(6) constructed via antiparallel PaQa and two symmedians AK, BK (S = 27)
   :caption: Problem LI: Lemoine's Symmedian Point K = X(6) constructed in only 2 traced lines and 8 circles (4R₁ + 2R₂ + 13C₁ + 8C₃, S = 27 vs. trilinear S = 54).

.. folio:: 0060
   :page: p. 44

**Problem LII — :term:`Lemoine Line <droite-de-lemoine>` (Trilinear Polar of :math:`X(6)`).**
Constructing the intersections of two sides of :g:`ABC` with the circumcircle tangents at their opposite vertices (via Problem XXXIV *bis* external angle copying) draws the Lemoine line in :math:`6R_1 + 3R_2 + 6C_1 + 4C_3` (:math:`S = 19, E = 12`, 3 lines, 4 circles).

**Problem LIII — Simultaneous Construction of Centroid :g:`G` :math:`= X(2)` and Lemoine Point :g:`K` :math:`= X(6)`.**

.. folio:: 0061
   :page: p. 45

Sweeping three equal-radius circles :math:`A(R), B(R), C(R)` (:math:`3C_1 + 3C_3`) yields both the midpoints :math:`A', B'` (for medians :math:`AA', BB'` meeting at :g:`G`) *and* the equal-radius circular arcs inside angles :math:`A, B` across which reflecting the medians directly gives the isogonal conjugate symmedians meeting at :g:`K`:

.. math::

   \mathrm{Op.} : \left(12R_1 + 6R_2 + 9C_1 + 5C_3\right), \qquad S = 32, \quad E = 21 \quad (6\text{ lines}, 5\text{ circles}),

saving **12 full operations** over building :g:`G` (:math:`S = 17`) and :g:`K` (:math:`S = 27`) separately (:math:`17 + 27 = 44`)!
