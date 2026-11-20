:layout: book
:canonical_id: Prob. XXIX
:order: 3
:folio: 0032
:tracks: English: 13_common_tangents_xxix-en | French: 13_common_tangents_xxix-fr | Summary: 13_common_tangents_xxix-summary | Notes: 13_common_tangents_xxix-notes

.. _lemoine-13_common_tangents_xxix-en:

Problem XXIX: Common Tangents to Two Circles
============================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 16–19, fols. ``0032–0035``)

.. folio:: 0032
   :page: p. 16

**Problem XXIX — Trace the Common Tangents to Two Given Circles :g:`O` and :g:`O'` (of Radii :math:`R, r`).**
Across four pages (pp. 16–19), Lemoine conducts a tour-de-force comparative audit of the **two classical approaches** to common tangents across all four relative configurations (exterior circles, intersecting circles, externally tangent, internally tangent):

.. folio:: 0033
   :page: p. 17

1. **First Method — Concentric Sum/Difference Circles :math:`O(R \pm r)` (p. 17)**:
   Drawing line of centers :g:`OO'`, marking :math:`B', B''` at distances :math:`R \mp r`, bisecting :math:`OO'` at :math:`\omega`, sweeping :math:`\omega(\omega O)` across :math:`O(R - r)` and :math:`O(R + r)`, drawing the four radii to contact points, and erecting the four perpendiculars yields the tabular tally on folio ``0033`` (p. 17):
   * *All 4 common tangents (exterior circles)*: :math:`24R_1 + 12R_2 + 13C_1 + 8C_3` (:math:`S = 57, E = 37`, 12 lines, 8 circles).
   * *Only 2 exterior (or 2 interior) tangents*: :math:`12R_1 + 6R_2 + 10C_1 + 6C_3` (:math:`S = 34, E = 22`, 6 lines, 6 circles).
   * *Intersecting circles (2 exterior tangents)*: :math:`14R_1 + 7R_2 + 10C_1 + 6C_3` (:math:`S = 37, E = 24`).
   * *Externally tangent circles (3 tangents)*: :math:`16R_1 + 8R_2 + 12C_1 + 8C_3` (:math:`S = 44, E = 28`).

.. folio:: 0034
   :page: p. 18

2. **Second Method — Homothety / :term:`Centers of Similitude <aehnlichkeitspunkte>` :g:`V` and :g:`V₁` (pp. 18–19, FIG. 3)**:
   Instead of constructing concentric circles :math:`O(R \pm r)`, Lemoine locates the external and internal centers of similitude :g:`V` and :g:`V₁` directly by sweeping **60° equilateral compass strikes** along the line of centers :g:`OO'` (cutting :g:`O` at :g:`A₁`, :g:`A` and :g:`O'` at :g:`A'`, :g:`A'₁`):
   * Sweep :g:`A(AO)` to mark :g:`α` at :math:`+60^\circ` on circle :g:`O` and :g:`A₁(A₁O)` to mark :g:`α₁` at :math:`-120^\circ`; sweep :g:`A'₁(A'₁O')` to mark :g:`α'` at :math:`+60^\circ` on circle :g:`O'`.
   * Because radii :math:`O\alpha \parallel O'\alpha'` (same sense) and :math:`O\alpha_1 \parallel O'\alpha'` (opposite sense), the two transversals :g:`αV` (through :g:`α, α'`) and :g:`α₁α'` intersect :g:`OO'` directly at the external center of similitude :g:`V` and internal center of similitude :g:`V₁` (costing only :math:`6R_1 + 3R_2 + 4C_1 + 2C_3`, :math:`S = 15`, reused later in Problem XLIV!).
   * Drawing the tangents from :g:`V` and :g:`V₁` to circle :g:`O` (Problem XXVI) then yields all four common tangents in **10 lines and 7 circles**—slashing simplicity from :math:`S = 57` down to **:math:`S = 46`**!

.. container:: lemoine-plate-pair

   .. picture:: 0034.g1.png
      :alt: Archival 1893 engraving FIG. 3 of Problem XXIX showing homothety centers V and V1 of circles O and O'
      :caption: FIG. 3 archival scan (Paris 1893, fol. 0034, p. 18): Centers of similitude V, V₁ via 60° parallel radii Oα, Oα₁, O'α'.

   .. picture:: 0034.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 3 (Problem XXIX centers of similitude V and V1)
      :caption: FIG. 3 vectorization: Exact 60° strike arcs A(AO), A₁(A₁O), A'₁(A'₁O') determining parallel radii and homothety centers V, V₁.

.. folio:: 0035
   :page: p. 19

Page 19 completes the case table for the Second Method:
* *Only 2 exterior (or 2 interior) tangents*: :math:`8R_1 + 4R_2 + 11C_1 + 5C_3` (:math:`S = 28, E = 19`, 4 lines, 5 circles—saving 6 operations over Method 1's :math:`S = 34`!).
* *Intersecting circles*: :math:`S = 28` (:math:`E = 19` with 5 circles, or :math:`E = 18` with 6 circles via Problem XXVI 2°).
* *Externally tangent circles*: :math:`S = 41` (:math:`E = 27` or :math:`E = 26`).
