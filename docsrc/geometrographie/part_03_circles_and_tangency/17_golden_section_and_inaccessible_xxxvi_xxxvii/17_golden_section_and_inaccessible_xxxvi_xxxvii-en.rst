:layout: book
:canonical_id: Probs. XXXVI–XXXVII
:order: 7
:folio: 0043
:tracks: English: 17_golden_section_and_inaccessible_xxxvi_xxxvii-en | French: 17_golden_section_and_inaccessible_xxxvi_xxxvii-fr | Summary: 17_golden_section_and_inaccessible_xxxvi_xxxvii-summary | Notes: 17_golden_section_and_inaccessible_xxxvi_xxxvii-notes

.. _lemoine-17_golden_section_and_inaccessible_xxxvi_xxxvii-en:
.. _lemoine-en-proportions-golden:

Problems XXXVI–XXXVII: Golden Section & Inaccessible Intersections
==================================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 27–28, fols. ``0043–0044``)

.. folio:: 0043
   :page: p. 27

**Problem XXXVI (Euclid II.11 & VI.30 — Divide Segment :g:`AB` in :term:`Extreme and Mean Ratio <moyenne-et-extreme-raison>`, Golden Section :math:`\phi = \frac{1 + \sqrt{5}}{2}`).**
Classical textbook execution erects perpendicular :math:`BC = AB/2` at :g:`B`, joins hypotenuse :math:`AC`, and transfers :math:`AC - BC` onto :g:`AB`—drawing **three straight lines and seven circles** (:math:`6R_1 + 3R_2 + 9C_1 + 7C_3`, :math:`S = 25, E = 15`, :ref:`concordance-golden-section`).

On folios ``0043``–``0044`` (pp. 27–28, **FIG. 8**), :person:`Lemoine <lemoine>` compares three syntheses and unveils his celebrated **one-line Golden Section** (Method *c*):

.. folio:: 0044
   :page: p. 28

1. Keeping the **single constant radius** :math:`AB`, sweep :g:`A(AB)` and :g:`B(AB)` meeting above at :g:`C'` and below at :g:`C`, then sweep :g:`C(AB)` and :g:`C'(AB)` (the latter cutting :g:`B(AB)` at :g:`D`, forming a :math:`30^\circ` tangent :g:`AD` to circle :g:`C(AB)` at :g:`A`!): :math:`4C_1 + 4C_3`.
2. Draw the **single straight line** :g:`AD` (:math:`2R_1 + R_2`), cutting :g:`A(AB)` at :g:`E`. Because :math:`\angle CAE = 90^\circ` and :math:`CA = AE = AB`, distance :math:`CE = AB\sqrt{2}`!
3. Capture :math:`CE` and sweep :g:`C(CE)` (:math:`2C_1 + C_3`), cutting ray :math:`BA` beyond :g:`A` at :g:`M`. In :math:`\triangle CAM`, :math:`CM^2 = 2AB^2`, altitude :math:`h = \frac{\sqrt{3}}{2}AB`, and horizontal base projection :math:`\frac{1}{2}AB + AM = \sqrt{2 - \frac{3}{4}}\,AB = \frac{\sqrt{5}}{2}\,AB`, whence **exact** :math:`AM = \frac{\sqrt{5} - 1}{2}\,AB = AB/\phi`!
4. Sweep :g:`A(AM)` (:math:`2C_1 + C_3`, or :math:`3C_1 + C_3` including pivot reset) cutting segment :g:`AB` internally at the exact **Golden Point** :g:`P` (:g:`AP` :math:`= AB/\phi`):

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 9C_1 + 6C_3\right), \qquad S = 18, \quad E = 11 \quad (1\text{ line}, 6\text{ circles}).

.. container:: lemoine-plate-pair

   .. picture:: 0044.g1.png
      :alt: Archival 1893 engraving FIG. 8 of Problem XXXVI(c) showing Lemoine's 1-line Golden Section of AB
      :caption: FIG. 8 archival scan (Paris 1893, fol. 0044, p. 28): Lemoine's 1-line, 6-circle Golden Section AP = AB/φ.

   .. picture:: 0044.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 8 (Problem XXXVI(c) Golden Section over Q(sqrt(3), sqrt(5)))
      :caption: FIG. 8 vectorization: Exact SymPy calibration over ℚ(√3, √5) tracing only line AD to yield AM = AP = AB/φ (S = 18).

In addition, Lemoine notes the companion perpendicular-bisector single-line variant (illustrated below, also :math:`S = 18, E = 11`, 1 line, 6 circles) where the single traced line is the perpendicular bisector :math:`MC` of :math:`AB`.

.. picture:: /_static/figures/fig_golden_section_lemoine.svg
   :alt: Explanatory schematic of the perpendicular-bisector 1-line Golden Section (S = 18)
   :caption: Companion explanatory diagram: Perpendicular-bisector 1-line Golden Section (also 2R₁ + R₂ + 9C₁ + 6C₃, S = 18, E = 11).

**Problem XXXVII — Through a Given Point :math:`A`, Draw the Line Aiming at the Inaccessible Intersection of Two Traced Lines :math:`D, D'`.**
Directly below **FIG. 8** on page 28, Lemoine evaluates the projective Desargues / harmonic-pencil construction using **pure straightedge** (zero circles!) when two lines meet off the drawing sheet, establishing the transition into the projective block of Problems XXXVIII–XLVI.
