:layout: book
:canonical_id: Probs. XXV–XXVI
:order: 6
:folio: 0030
:tracks: English: 10_tangents_xxv_xxvi-en | French: 10_tangents_xxv_xxvi-fr | Summary: 10_tangents_xxv_xxvi-summary | Notes: 10_tangents_xxv_xxvi-notes

.. _lemoine-10_tangents_xxv_xxvi-en:

Problems XXV–XXVI: Tangents to a Given Circle
=============================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, p. 14, fols. ``0030``)

.. folio:: 0030
   :page: p. 14

**Problem XXV (Euclid III.16 Por. — Tangent at a Given Point :math:`A` on a Circle :math:`O`).**
Classical execution joins radius :math:`OA` (:math:`2R_1 + R_2`) and erects the perpendicular at :math:`A` by Problem XX 2° (:math:`4R_1 + 2R_2 + C_1 + C_3`), totaling :math:`6R_1 + 3R_2 + C_1 + C_3` (:math:`S = 11, E = 7`, 3 lines, 1 circle). Lemoine improves simplicity to :math:`S = 10, E = 6` in **only one straight line**: sweep :math:`A(AO)` (:math:`2C_1 + C_3`) cutting circle :math:`O` at :math:`B`; keeping radius :math:`AO`, sweep :math:`B(BO)` (:math:`C_1 + C_3`) cutting :math:`A(AO)` at :math:`C` (opposite to :math:`O`), and sweep :math:`C(CO)` (:math:`C_1 + C_3`)? Specifically, :math:`B(AO)` cuts :math:`O` at :math:`C` and :math:`A(AO)` at :math:`D`, giving :math:`AD` tangent at :math:`A` by equilateral-angle symmetry:

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 4C_1 + 3C_3\right), \qquad S = 10, \quad E = 6 \quad (1\text{ line}, 3\text{ circles}).

**Problem XXVI (Euclid III.17 — Tangents from an External Point :g:`A` to a Given Circle :g:`O(R)`).**
Whereas classical *Elements* III.17 costs :math:`8R_1 + 4R_2 + 4C_1 + 3C_3` (:math:`S = 19, E = 12`), :person:`Lemoine <lemoine>` gives two distinct :math:`S = 18` syntheses on folio ``0030`` (p. 14):

1. **First Method (Concentric-Diameter / Perpendicular Bisector, :math:`S = 18, E = 12`)**: Draw line :math:`OA` cutting circle :math:`O` at :math:`C, D`, bisect :g:`OA` at :g:`M`, sweep :g:`M(MO)` cutting :g:`O(R)` at contact points :g:`T`, :g:`T'`, and draw :g:`AT`, :g:`AT'`: :math:`5R_1 + 3R_2 + 7C_1 + 3C_3` (:math:`S = 18, E = 12`, 3 lines, 3 circles).
2. **Second Method (Secant Chord & Thales Circle, :math:`S = 18, E = 11`)**: Draw an arbitrary secant from :g:`A` or bisect :g:`OA` via equal-radius arcs so that circle :g:`M(MO)` cuts :g:`O(R)` directly at :g:`T` and :g:`T'` along polar chord :g:`TT'`, yielding superior exactitude :math:`E = 11`:

.. math::

   \mathrm{Op.} : \left(5R_1 + 3R_2 + 6C_1 + 4C_3\right), \qquad S = 18, \quad E = 11 \quad (3\text{ lines}, 4\text{ circles}).

.. picture:: /_static/figures/fig_circle_tangents.svg
   :alt: Problem XXVI tangents AT and AT' from external point A to circle O(R) via Thales circle M(MO)
   :caption: Problem XXVI: External tangents AT, AT' to circle O(R) via midpoint M of OA and Thales circle M(MO) (5R₁ + 3R₂ + 6C₁ + 4C₃, S = 18, E = 11).

Note the striking instrument duality documented in :ref:`concordance-external-tangents`: when circle :g:`O` is already traced, :person:`Steiner <steiner>`'s pure-straightedge polar construction (Problem XXXIX + two tangent joins) requires **zero circles** (:math:`16R_1 + 9R_2`), whereas Lemoine's metric synthesis achieves :math:`S = 18`.
