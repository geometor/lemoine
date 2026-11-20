:layout: book
:canonical_id: Prob. XXVIII
:order: 2
:folio: 0032
:tracks: English: 12_capable_segment_xxviii-en | French: 12_capable_segment_xxviii-fr | Summary: 12_capable_segment_xxviii-summary | Notes: 12_capable_segment_xxviii-notes

.. _lemoine-12_capable_segment_xxviii-en:

Problem XXVIII: Circular Segment Capable of a Given Angle
=========================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, p. 16, fols. ``0032``)

.. folio:: 0032
   :page: p. 16

**Problem XXVIII (Euclid III.33 — Describe Upon Given Segment :g:`AB` a Circular Segment Capable of Given Angle :g:`C` = :math:`\angle DCE`).**
Classical textbooks copy angle :math:`\angle DCE` at :g:`A` to draw the tangent to the sought circle, erect a perpendicular to that tangent at :g:`A`, draw the perpendicular bisector of :g:`AB`, and finally trace the arc—requiring three straight lines and a high circle count.

On folio ``0032`` (p. 16, **FIG. 2**), :person:`Lemoine <lemoine>` eliminates the tangent line completely by observing that the inscribed angle :math:`\angle ABD` subtended on circle :g:`A(AB)` equals :math:`90^\circ - \alpha` when arc :g:`BD` equals :math:`2\alpha`—so the single chord :g:`BD` directly intersects the perpendicular bisector :g:`PQ` of :g:`AB` at the exact center :g:`O`!

1. Sweep :g:`A(AB)` and :g:`B(AB)` (:math:`3C_1 + 2C_3`) meeting at :g:`P` and :g:`Q`, and draw the perpendicular bisector :g:`PQ` (:math:`2R_1 + R_2`).
2. Retaining the **exact same radius** :math:`AB`, sweep :g:`C(AB)` (:math:`C_1 + C_3`) centered at the vertex of the given angle :math:`\angle DCE`, cutting its arms at :g:`D_ang` and :g:`E`.
3. Capture chord :math:`DE` and double it across :g:`E` onto :g:`C(AB)` at :g:`F` (:math:`3C_1 + C_3`), giving the doubled chord :math:`DF` subtending :math:`2\angle DCE`.
4. Transfer chord :math:`DF` from :g:`B` onto :g:`A(AB)` at :g:`D` (:math:`3C_1 + C_3`) and draw :g:`BD` (:math:`2R_1 + R_2`) meeting :g:`PQ` at the exact center :g:`O`!
5. Sweep the capable arc :g:`O(OA)` (:math:`2C_1 + C_3`) over :g:`AB`:

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 11C_1 + 6C_3\right) \quad [\text{or } 12C_1\text{ when }AB\text{ is reset}], \qquad S = 23, \quad E = 15 \quad (2\text{ lines}, 6\text{ circles}).

.. container:: lemoine-plate-pair

   .. picture:: 0032.g1.png
      :alt: Archival 1893 engraving FIG. 2 of Problem XXVIII showing the segment capable of angle DCE on chord AB
      :caption: FIG. 2 archival scan (Paris 1893, fol. 0032, p. 16): Segment capable of angle DCE on chord AB.

   .. picture:: 0032.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 2 (Problem XXVIII circular segment capable of angle DCE)
      :caption: FIG. 2 vectorization: Doubled-angle chord transfer from C(AB) onto A(AB) locating center O = BD ∩ PQ directly without tracing the tangent.
