:layout: book
:canonical_id: Prob. XVIII
:order: 3
:folio: 0026
:tracks: English: 07_bisector_reflection_xviii-en | French: 07_bisector_reflection_xviii-fr | Summary: 07_bisector_reflection_xviii-summary | Notes: 07_bisector_reflection_xviii-notes

.. _lemoine-07_bisector_reflection_xviii-en:
.. _lemoine-en-bisector-reflection:

Problems XVIII & XVIII bis: Perpendicular Bisector & Point Reflection
=====================================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, p. 10, fols. ``0026``)

.. folio:: 0026
   :page: p. 10

**Problem XVIII (Euclid I.10 — Perpendicular Bisector & Midpoint of :g:`AB`).**
*To trace the perpendicular at the midpoint of the segment joining two given points* :g:`A` *and* :g:`B` *(or to locate the midpoint* :g:`M` *of a traced segment* :g:`AB`).

Whereas :person:`Euclid <euclid>` sets the compass specifically to radius :math:`AB` (:math:`2C_1 + C_3` at :g:`A` then :math:`C_1 + C_3` at :g:`B`, costing :math:`2R_1 + R_2 + 3C_1 + 2C_3`, :math:`S = 8, E = 5`), :person:`Lemoine <lemoine>` notes that any *arbitrary* shared opening :math:`R > AB/2` suffices: sweep :g:`A(R)` (:math:`C_1 + C_3`) and :g:`B(R)` (:math:`C_1 + C_3`) intersecting at :g:`P` and :g:`Q`, and draw :g:`PQ` (:math:`2R_1 + R_2`) bisecting :g:`AB` into :g:`AM` and :g:`MB`:

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 2C_1 + 2C_3\right), \qquad S = 7, \quad E = 4 \quad (1\text{ line}, 2\text{ circles}).

.. picture:: /_static/figures/fig_perpendicular_bisector.svg
   :alt: Lemoine's S = 7 perpendicular bisector using arbitrary shared radius R > AB/2
   :caption: Problem XVIII: Arbitrary-radius perpendicular bisector PQ of AB (2R₁ + R₂ + 2C₁ + 2C₃, S = 7, E = 4 vs. Euclid's S = 8).

**Problem XVIII bis — Symmetric Reflection :math:`A'` of a Point :math:`A` Across a Traced Line :math:`BC` (Zero Straight Lines!).**
Classical textbooks drop a perpendicular from :math:`A` to :math:`BC`, extend it, and transfer the foot distance (:math:`S = 15`, 2 lines, 3 circles). Lemoine reflects :math:`A` **by compass alone without touching the straightedge**: place one compass leg at an indeterminate point on :math:`BC` (:math:`C_2`) and the other on :math:`A` (:math:`C_1`), sweep an arc (:math:`C_3`), and repeat from a second indeterminate point on :math:`BC` (:math:`C_1 + C_2 + C_3`). The second intersection of the two circles is the exact mirror image :math:`A'`:

.. math::

   \mathrm{Op.} : \left(2C_1 + 2C_2 + 2C_3\right), \qquad S = 6, \quad E = 4 \quad (0\text{ lines}, 2\text{ circles}).

When two determined points :math:`B, C` already lie on the mirror line, sweeping :math:`B(BA)` and :math:`C(CA)` costs :math:`4C_1 + 2C_3` (:math:`S = 6, E = 4`)—the exact compass-only reflection of :person:`Mascheroni <mascheroni>` (:cite:`mascheroni-1797`, Libro IV, § 78)!
