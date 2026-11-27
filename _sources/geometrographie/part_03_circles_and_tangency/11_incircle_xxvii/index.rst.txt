:layout: book
:canonical_id: Prob. XXVII
:order: 1
:folio: 0031

.. _lemoine-11_incircle_xxvii-en:
.. _geometrographie-part-03-en:
.. _geometrographie-unit-3-en:
.. _lemoine-en-circles-tangents-incircle:

Problem XXVII: Inscribe a Circle in a Given Triangle ABC
========================================================

.. folio:: 0031
   :page: p. 15

**XXVII.** — *Inscribe a circle in a given triangle ABC.*

Whether it is a question of an inscribed circle or an escribed circle, the classical method by the bisectors of the angles of the triangle leads to the symbol:

:math:`\mathrm{Op.} : (6R_1 + 3R_2 + 11C_1 + 10C_3)` ; simplicity 30 ; exactitude 17 ; 3 straight lines, 10 circles.

If one wished to trace the three other tangent circles, one would have to add in addition: :math:`\mathrm{op.} : (12R_1 + 6R_2 + 16C_1 + 13C_3)`. In all, consequently:

:math:`\mathrm{Op.} : (18R_1 + 9R_2 + 27C_1 + 23C_3)` ; simplicity 77 ; exactitude 45 ; 18 straight lines, 23 circles.

Here is a simpler solution, yet one which would certainly not occur to the mind unless one directed attention toward the systematic search for the simplicity of the construction (*fig. 1*).

.. container:: lemoine-plate-pair

   .. picture:: 0031.g1.png
      :alt: Archival 1893 engraving FIG. 1 of Problem XXVII showing the S = 23 incircle construction
      :caption: FIG. 1 archival scan (Paris 1893, fol. 0031, p. 15): Geometrographic semiperimeter-bisection incircle construction.

   .. picture:: 0031.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 1 (Problem XXVII incircle of triangle ABC)
      :caption: FIG. 1 vectorization: Exact SymPy calibration of ray BD, arc A(DE), perpendicular bisectors OR and OQ, and incircle O(OR) (S = 23).

I call :g:`P`, :g:`Q`, :g:`R` the points of contact of the inscribed circle on :g:`BC`, :g:`CA`, :g:`AB`, and :g:`O` the center of this circle.

On :g:`BA`, in the direction :g:`BA`, I take :math:`AD = AC`; on :g:`BA`, in the direction :g:`BA`, I take :math:`BE = BC` — :math:`\mathrm{op.} : (4C_1 + 2C_3)`.

I describe :g:`A(DE)`, which cuts :g:`AB` at :g:`R'` (:g:`R'` lies in the direction :g:`AB`) and :g:`AC` at :g:`Q'` (:g:`Q'` lies in the direction :g:`AC`) — :math:`\mathrm{op.} : (3C_1 + C_3)`; it is evident that :math:`AR = AQ = \frac{b + c - a}{2}` and that, consequently, :g:`R` and :g:`Q` are the midpoints of :math:`AR'` and :math:`AQ'`; :g:`O` is therefore the center of the circle circumscribed about triangle :math:`AQ'R'`.

I trace :math:`R'(DE)`, which cuts :g:`A(DE)` in two points; joining these points gives a locus of :g:`O` — :math:`\mathrm{op.} : (2R_1 + R_2 + C_1 + C_3)`.

I trace :math:`Q'(DE)`, which cuts :g:`A(DE)` in two points; joining these points gives another locus of :g:`O` — :math:`\mathrm{op.} : (2R_1 + R_2 + C_1 + C_3)`.

I describe :g:`O(OR)`, which is the required circle — :math:`\mathrm{op.} : (2C_1 + C_3)`.

:math:`\mathrm{Op.} : (4R_1 + 2R_2 + 11C_1 + 6C_3)` ; simplicity 23 ; exactitude 15 ; 2 straight lines, 6 circles.

By applying the *continuous transformation* (see *A. F.*, Congress of Marseille, 1891), one arrives immediately at the construction required to draw an escribed circle; it has the same symbol as that for drawing the inscribed circle.

.. folio:: 0032
   :page: p. 16

If one wishes to draw all four tangent circles, it is better to begin with the three escribed circles and finish with the inscribed circle by joining :math:`AO_a`, :math:`BO_b`, etc.

One has:

:math:`\mathrm{Op.} : (18R_1 + 9R_2 + 26C_1 + 13C_3)` ; simplicity 66 ; exactitude 44 ; 9 straight lines, 13 circles.

.. picture:: /_static/figures/fig_incircle_lemoine.svg
   :alt: Explanatory diagram comparing the S = 23 incircle synthesis with the classical S = 30 construction
   :caption: Companion explanatory diagram: Incenter X(1) and incircle contact radius ID compared against the classical 10-circle textbook method (S = 30 vs. S = 23).
