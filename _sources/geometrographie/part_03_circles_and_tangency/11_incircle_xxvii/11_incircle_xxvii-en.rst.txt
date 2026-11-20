:layout: book
:canonical_id: Prob. XXVII
:order: 1
:folio: 0031
:tracks: English: 11_incircle_xxvii-en | French: 11_incircle_xxvii-fr | Summary: 11_incircle_xxvii-summary | Notes: 11_incircle_xxvii-notes

.. _lemoine-11_incircle_xxvii-en:
.. _geometrographie-part-03-en:
.. _geometrographie-unit-3-en:
.. _lemoine-en-circles-tangents-incircle:

Problem XXVII: Incircle & Excircles of a Triangle
=================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 15–16, fols. ``0031–0032``)

.. folio:: 0031
   :page: p. 15

**Problem XXVII (Euclid IV.4 — Incircle & Incenter :math:`O = X(1)` of Triangle :g:`ABC`).**
In standard textbooks, inscribing a circle in :g:`ABC` requires bisecting two angles (6 circles, 2 lines), dropping a full perpendicular from the incenter to one side (3 circles, 1 line), and tracing the incircle (1 circle)—costing :math:`6R_1 + 3R_2 + 11C_1 + 10C_3` (:math:`S = 30, E = 17`, 3 lines, 10 circles).

On folio ``0031`` (p. 15, **FIG. 1**), :person:`Lemoine <lemoine>` cuts **seven operations and four circles** using an astonishing metric-bisection synthesis that constructs the contact points :g:`Q` and :g:`R` directly from the semiperimeter identity :math:`AQ = AR = s - a = \frac{b + c - a}{2}`:

1. Extend ray :g:`BA` past :g:`A` and sweep :g:`A(AC)` (:math:`2C_1 + C_3`) to mark :g:`D` with :math:`AD = b`, and sweep :g:`B(BC)` (:math:`2C_1 + C_3`) to mark :g:`E` along ray :g:`BA` with :math:`BE = a`. The segment :math:`DE` equals :math:`b + c - a = 2(s - a)`!
2. Capture :math:`DE` and sweep :g:`A(DE)` (:math:`3C_1 + C_3`) cutting :g:`AB` at :g:`R'` and :g:`AC` at :g:`Q'`.
3. Retaining the exact same compass aperture :math:`DE`, sweep :math:`R'(DE)` and :math:`Q'(DE)` (:math:`2C_1 + 2C_3`) cutting :g:`A(DE)` in pairs determining the perpendicular bisectors of :math:`AR'` and :math:`AQ'`.
4. Draw those two perpendicular bisectors (:math:`4R_1 + 2R_2`); they pass through the exact incircle contact points :g:`R` and :g:`Q` and meet at the incenter :g:`O` (:math:`X(1)` in :external+etc:doc:`index`).
5. Sweep :g:`O(OR)` (:math:`2C_1 + C_3`) to trace the incircle tangent to :g:`BC` at :g:`P`, :g:`CA` at :g:`Q`, and :g:`AB` at :g:`R`:

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 11C_1 + 6C_3\right), \qquad S = 23, \quad E = 15 \quad (2\text{ lines}, 6\text{ circles}).

.. container:: lemoine-plate-pair

   .. picture:: 0031.g1.png
      :alt: Archival 1893 engraving FIG. 1 of Problem XXVII showing Lemoine's S = 23 incircle construction
      :caption: FIG. 1 archival scan (Paris 1893, fol. 0031, p. 15): Lemoine's semiperimeter-bisection incircle construction.

   .. picture:: 0031.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 1 (Problem XXVII incircle of triangle ABC)
      :caption: FIG. 1 vectorization: Exact SymPy calibration of ray BD, arc A(DE), perpendicular bisectors OR and OQ, and incircle O(OR) (S = 23).

.. folio:: 0032
   :page: p. 16

On page 16, Lemoine notes the companion angle-bisector optimization (illustrated below) and applies the identical principle to construct an **excircle** tangent to side :g:`BC` and the extensions of :g:`AB`, :g:`AC`, as well as all four tritangent circles simultaneously.

.. picture:: /_static/figures/fig_incircle_lemoine.svg
   :alt: Explanatory diagram comparing Lemoine's S = 23 incircle synthesis with classical S = 30 construction
   :caption: Companion explanatory diagram: Incenter X(1) and incircle contact radius ID compared against the classical 10-circle textbook method (S = 30 vs. S = 23).
