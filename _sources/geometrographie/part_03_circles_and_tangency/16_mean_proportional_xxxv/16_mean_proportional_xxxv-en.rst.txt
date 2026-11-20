:layout: book
:canonical_id: Prob. XXXV
:order: 6
:folio: 0040
:tracks: English: 16_mean_proportional_xxxv-en | French: 16_mean_proportional_xxxv-fr | Summary: 16_mean_proportional_xxxv-summary | Notes: 16_mean_proportional_xxxv-notes

.. _lemoine-16_mean_proportional_xxxv-en:

Problem XXXV: Mean Proportional Between Two Segments
====================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 24–27, fols. ``0040–0043``)

.. folio:: 0040
   :page: p. 24

**Problem XXXV (Euclid II.14 / VI.13 — Construct the Mean Proportional :math:`X = \sqrt{M \cdot N}` Between Two Given Segments :math:`M > N`).**
Lemoine audits **five** distinct methods across four pages (pp. 24–27), demonstrating dramatically how textbook favorites can lag ten full operations behind the true optimum:

* **Methods (a) & (b) — Classical Right-Triangle Altitude & Circle Tangent (pp. 24–25)**: Even after reusing :math:`A(M)` to find the midpoint of diameter :math:`AC`, the classical semicircle altitude (a) costs :math:`4R_1 + 3R_2 + 10C_1 + C_2 + 6C_3` (:math:`S = 24, E = 15`, 3 lines, 6 circles), and the classical secant-tangent method (b) costs :math:`4R_1 + 3R_2 + 12C_1 + C_2 + 7C_3` (:math:`S = 27, E = 17`, or :math:`S = 25` with two compasses). Contrary to *Rouché et de Comberousse* (1re partie, p. 152), both classical methods are nearly equivalent—and both are *very poor* graphically!

.. folio:: 0041
   :page: p. 25

* **Methods (c) & (c₁) — The Optimal Lemoine–Gouzy Construction (:math:`S = 14, E = 9`, p. 25)**:
  Trace an arbitrary line :math:`AB` (:math:`R_2`), lay off :math:`AB = M` via :math:`A(M)` (:math:`2C_1 + C_2 + C_3`), sweep :math:`B(N)` cutting segment :math:`BA` internally at :math:`C`, and with the **same radius** :math:`N` sweep :math:`C(N)` cutting :math:`B(N)` at :math:`P, Q` (:math:`4C_1 + 2C_3`). Trace perpendicular bisector :math:`PQ` (:math:`2R_1 + R_2`) cutting :math:`A(M)` at :math:`H`: because :math:`BH` projects onto :math:`BC/2 = N/2` inside circle :math:`A(M)` of radius :math:`M`, similar isosceles triangles yield :math:`BH = \sqrt{M \cdot N}`!

.. math::

   \mathrm{Op.} : \left(2R_1 + 2R_2 + 6C_1 + C_2 + 3C_3\right), \qquad S = 14, \quad E = 9 \quad (2\text{ lines}, 3\text{ circles}).

Lemoine generously credits :person:`Edm.-Auguste Gouzy <gouzy>` of Lausanne (*Nouvelles Annales*, 1857, p. 125) for first stating the underlying geometric idea (which gave :math:`S = 15` in Gouzy's verbal order, refined by Lemoine to :math:`S = 14`, cutting classical :math:`S = 24` by 42% and halving the circle count from 6 to 3, :ref:`concordance-mean-proportional`).

.. folio:: 0042
   :page: p. 26

* **Method (d) — Chord-Reflection Synthesis (FIG. 6, p. 26, :math:`S = 18`)**: Draw an arbitrary circle :g:`O(OB)` of radius larger than :math:`M/2` carrying chord :g:`CB` :math:`= M`, mark :g:`K` on :g:`CB` with :math:`BK = N`, reflect :g:`K` across radius :math:`OB` using :g:`B(N)` and :g:`O(OK)`, and draw the perpendicular chord :g:`KA` cutting :g:`O(OB)` at :g:`A`: by similar right/isosceles triangles, :g:`AB` :math:`= \sqrt{M \cdot N}`!

.. container:: lemoine-plate-pair

   .. picture:: 0042.g1.png
      :alt: Archival 1893 engraving FIG. 6 of Problem XXXV(d) showing chord-reflection mean proportional AB = sqrt(MN)
      :caption: FIG. 6 archival scan (Paris 1893, fol. 0042, p. 26): Mean proportional AB = √(MN) via chord CB = M and reflection line KA.

   .. picture:: 0042.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 6 (Problem XXXV(d) mean proportional AB)
      :caption: FIG. 6 vectorization: Exact circle O(OB), chord CB = M, arcs B(N) and O(OK) fixing KA ⊥ OB, and target chord AB = √(MN) (S = 18).

.. folio:: 0043
   :page: p. 27

* **Method (e) — Léon Colette's 1892 Symmetric Chord Synthesis (FIG. 7, p. 27, :math:`S = 18`)**: From top point :g:`A` of circle :g:`O(OA)`, strike equal chords :g:`AB` :math:`= AC = M` and smaller arcs :g:`A(N)` marking :g:`D` on :g:`AB` and :g:`E` on :g:`AC` (and :g:`F, G` on the circle). The horizontal transversal :g:`DE` intersects circle :g:`O(OA)` at :g:`M` and :g:`N`, yielding :g:`AM` :math:`= AN = \sqrt{M \cdot N}`!

.. container:: lemoine-plate-pair

   .. picture:: 0043.g1.png
      :alt: Archival 1893 engraving FIG. 7 of Problem XXXV(e) showing Léon Colette's symmetric mean proportional AM = sqrt(MN)
      :caption: FIG. 7 archival scan (Paris 1893, fol. 0043, p. 27): Léon Colette's symmetric chord construction of AM = √(MN).

   .. picture:: 0043.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 7 (Problem XXXV(e) Léon Colette's mean proportional)
      :caption: FIG. 7 vectorization: Exact symmetric chords AB = AC = M, AD = AE = N, and horizontal line DE cutting O(OA) at M, N with AM = √(MN).
