:layout: book
:canonical_id: Probs. XXI–XXIV
:order: 5
:folio: 0028
:tracks: English: 09_circumcircle_angle_bisectors_xxi_xxiv-en | French: 09_circumcircle_angle_bisectors_xxi_xxiv-fr | Summary: 09_circumcircle_angle_bisectors_xxi_xxiv-summary | Notes: 09_circumcircle_angle_bisectors_xxi_xxiv-notes

.. _lemoine-09_circumcircle_angle_bisectors_xxi_xxiv-en:

Problems XXI–XXIV: Circumcircle & Angle Bisectors
=================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 12–14, fols. ``0028–0030``)

.. folio:: 0028
   :page: p. 12

**Problem XXI (Euclid IV.5 — Circumcircle & Circumcenter :math:`X(3)` Through Three Points :math:`A, B, C`).**
Open the compass to a single arbitrary radius :math:`R` greater than half of both :math:`AB` and :math:`BC`. Sweep :math:`B(R)` once (:math:`C_1 + C_3`), then :math:`A(R)` and :math:`C(R)` (:math:`2C_1 + 2C_3`). Sharing :math:`B(R)` across both perpendicular bisectors cuts the auxiliary circle count from four to three; tracing the two mediatrices (:math:`4R_1 + 2R_2`) fixes circumcenter :math:`O = X(3)` (:cite:`kimberling-etc`, :external+etc:doc:`index`), and sweeping :math:`O(A)` (:math:`2C_1 + C_3`) completes the circumcircle (saving 2 operations over textbook :math:`S = 17`, :ref:`concordance-circumcircle`):

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 5C_1 + 4C_3\right), \qquad S = 15, \quad E = 9 \quad (2\text{ lines}, 4\text{ circles}).

**Problem XXII (Euclid I.9 — Angle Bisector of :math:`\angle BAC`).**
Keeping one single sufficient radius :math:`R` for the initial arc centered at vertex :math:`A` (:math:`C_1 + C_3`, cutting the arms at :math:`B` and :math:`C`) and for both intersecting arcs :math:`B(R)` and :math:`C(R)` (:math:`2C_1 + 2C_3`), then joining :math:`A` to their intersection (:math:`2R_1 + R_2`), yields:

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 3C_1 + 3C_3\right), \qquad S = 9, \quad E = 5 \quad (1\text{ line}, 3\text{ circles}),

saving one :math:`C_1` over Euclid I.9 (:math:`S = 10`, :ref:`concordance-angle-bisector`).

.. folio:: 0029
   :page: p. 13

If the angle is specified merely by three unjoined points :math:`B, A, C`, Lemoine traces :math:`AB` (:math:`2R_1 + R_2`), sweeps :math:`A(AC)` cutting :math:`AB` at :math:`C'` (:math:`2C_1 + C_3`), sweeps :math:`C(AC)` and :math:`C'(AC)` meeting at :math:`D`, and traces :math:`AD` (:math:`2R_1 + R_2 + 2C_1 + 2C_3`), totaling :math:`4R_1 + 2R_2 + 4C_1 + 3C_3` (:math:`S = 13, E = 8`, 2 lines, 3 circles).

**Problem XXIII (Euclid III.30 — Bisect a Given Circular Arc).**
Assuming the circle's center is known (otherwise Problem XIX adds :math:`4R_1 + 2R_2 + 3C_2 + 3C_3`), perpendicular bisection of the chord joining the arc's endpoints takes :math:`2R_1 + R_2 + 2C_1 + 2C_3` (:math:`S = 7, E = 4`, 1 line, 2 circles).

**Problem XXIV — Bisector of the Angle Between Two Lines :math:`AB, CD` Whose Intersection :math:`X` Is Inaccessible.**
From an indeterminate point :math:`A` on :math:`AB`, sweep :math:`A(R)` cutting :math:`CD` at :math:`C` and :math:`AB` at :math:`B`, and with the same radius sweep :math:`C(R)` cutting :math:`CD` at :math:`D` (:math:`C_1 + C_2 + 2C_3`). Sweep :math:`B(R)` cutting :math:`C(R)` at :math:`J`, and :math:`D(R)` cutting :math:`A(R)` at :math:`I` (:math:`2C_1 + 2C_3`); trace :math:`AJ` and :math:`CI` (:math:`4R_1 + 2R_2`), meeting at a point :math:`M` on the required bisector! Sweep :math:`M(R')` cutting :math:`AB` at :math:`H` and :math:`CD` at :math:`G` (:math:`C_1 + C_3`), find one equidistant point :math:`M'` from :math:`G, H`, and join :math:`MM'` (:math:`2R_1 + R_2 + 2C_1 + 2C_3`):

.. math::

   \mathrm{Op.} : \left(6R_1 + 3R_2 + 6C_1 + C_2 + 7C_3\right), \qquad S = 23, \quad E = 13 \quad (3\text{ lines}, 7\text{ circles}).

.. folio:: 0030
   :page: p. 14

Page 14 concludes the preliminary angle-and-arc block and opens the circle-tangency sequence (Problems XXV–XXVI).
