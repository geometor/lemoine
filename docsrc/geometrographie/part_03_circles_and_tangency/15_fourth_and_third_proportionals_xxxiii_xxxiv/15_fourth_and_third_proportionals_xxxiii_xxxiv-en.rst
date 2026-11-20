:layout: book
:canonical_id: Probs. XXXIII–XXXIV
:order: 5
:folio: 0037
:tracks: English: 15_fourth_and_third_proportionals_xxxiii_xxxiv-en | French: 15_fourth_and_third_proportionals_xxxiii_xxxiv-fr | Summary: 15_fourth_and_third_proportionals_xxxiii_xxxiv-summary | Notes: 15_fourth_and_third_proportionals_xxxiii_xxxiv-notes

.. _lemoine-15_fourth_and_third_proportionals_xxxiii_xxxiv-en:

Problems XXXIII–XXXIV bis: Fourth & Third Proportionals
=======================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 21–24, fols. ``0037–0040``)

.. folio:: 0037
   :page: p. 21

**Problem XXXIII (Euclid VI.12 — Fourth Proportional :math:`X = \frac{N \cdot P}{M}` to Three Segments :math:`M, N, P`).**
Lemoine investigates **four** distinct methods—Thales parallels (a), power of a point via secants (b, **FIG. 4**), inscribed antiparallel chords in an arbitrary circle (c, **FIG. 5**), and Mascheronian concentric circles (d, non-general):

* **Method (a) — Classical Thales Parallels**: Tracing two intersecting rays, transferring :math:`M, N, P`, and drawing the parallel costs :math:`4R_1 + 3R_2 + 11C_1 + C_2 + 6C_3` (:math:`S = 25, E = 16`, 3 lines, 6 circles).
* **Method (b) — Power of a Point :math:`RA \cdot RB = RC \cdot RD` (FIG. 4, p. 21)**: Draw two intersecting lines through :g:`R` (:math:`2R_2`); lay off :math:`RA = N, RB = P` on one line and :math:`RC = M` on the other. Pass a circle through :g:`A`, :g:`B`, and :g:`C`; its second intersection :g:`D` with line :g:`RC` yields :math:`RD = NP/M` (left panel: external point :g:`R`; right panel: internal point :g:`R`, :math:`S = 22, E = 14`, :ref:`concordance-fourth-proportional`):

.. math::

   \mathrm{Op.} : \left(2R_1 + 2R_2 + 11C_1 + C_2 + 6C_3\right), \qquad S = 22, \quad E = 14 \quad (2\text{ lines}, 6\text{ circles}).

.. container:: lemoine-plate-pair

   .. picture:: 0037.g1.png
      :alt: Archival 1893 engraving FIG. 4 of Problem XXXIII(b) showing power-of-a-point fourth proportional
      :caption: FIG. 4 archival scan (Paris 1893, fol. 0037, p. 21): Fourth proportional via intersecting secants (external R and internal R).

   .. picture:: 0037.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 4 (Problem XXXIII(b) power-of-a-point fourth proportional)
      :caption: FIG. 4 vectorization: Exact circles through A, B, C determining RD = NP/M in both external (left) and internal (right) chord configurations.

.. folio:: 0038
   :page: p. 22

* **Method (c) — Inscribed Circle Chords (FIG. 5, p. 22)**: Draw an arbitrary circle large enough to contain chords :math:`RA = N`, :math:`RB = P`, and :math:`RC = M` from a point :g:`R` on the circumference. Draw chord :g:`AB` and chord :g:`RC` meeting at :g:`H`—or specifically, place :math:`RA = N, RB = P` on opposite sides of :g:`R`, mark :math:`RC = M`, and draw the parallel/antiparallel chord so :math:`\triangle RAH \sim \triangle RCB`, reading :g:`RH` :math:`= NP/M` directly with **far fewer circles**!

.. container:: lemoine-plate-pair

   .. picture:: 0038.g1.png
      :alt: Archival 1893 engraving FIG. 5 of Problem XXXIII(c) showing inscribed-circle chord fourth proportional
      :caption: FIG. 5 archival scan (Paris 1893, fol. 0038, p. 22): Fourth proportional RH = NP/M via inscribed chords in one arbitrary circle.

   .. picture:: 0038.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 5 (Problem XXXIII(c) chord fourth proportional)
      :caption: FIG. 5 vectorization: Exact circle chords RA = N, RB = P, RC = M intersecting chord AB at H to yield RH = NP/M.

* **Method (d) — Concentric Circles (Non-General, :person:`Mascheroni <mascheroni>` § 93)**: Whenever :math:`M > \frac{1}{2}P` (or :math:`2N < M`), concentric circles deliver :math:`X` by compass alone, underscoring Lemoine's rule (p. 23) that restricted-domain tricks must never be substituted for general symbols unless their hypotheses are guaranteed!

.. folio:: 0039
   :page: p. 23

**Problem XXXIV (Euclid VI.11 — Third Proportional :math:`X = \frac{N^2}{M}`).**
Setting :math:`N = P` in XXXIII(c) yields Lemoine's simplest *general* construction—take equal chords :math:`RA = RB = N` on opposite sides of :math:`R` on an arbitrary circle, take chord :math:`RC = M`, and draw :math:`AB` and :math:`RC` meeting at :math:`H`, whence :math:`RH = N^2/M`:

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 5C_1 + C_2 + 3C_3\right), \qquad S = 15, \quad E = 10 \quad (2\text{ lines}, 3\text{ circles}).

When :math:`N < 2M`, an even simpler two-circle construction (:math:`B(M)`, :math:`A(N)` from :math:`A` on :math:`B(M)`, join :math:`BD` cutting :math:`A(N)` at :math:`C`) yields :math:`CD = N^2/M` in :math:`2R_1 + R_2 + 4C_1 + C_2 + 2C_3` (:math:`S = 10, E = 7`, 1 line, 2 circles!).

.. folio:: 0040
   :page: p. 24

**Problem XXXIV bis — Triangle Ratios :math:`\frac{b^2}{a}, \frac{c^2}{a}, \frac{bc}{a}`, etc., Inside a Traced Triangle :math:`ABC`.**
Copying :math:`\angle BAK = C` (with :math:`K` on :math:`BC`) yields **simultaneously** :math:`AK = \frac{bc}{a}` and :math:`BK = \frac{c^2}{a}` in a single angle-transfer symbol :math:`2R_1 + R_2 + 5C_1 + 3C_3` (:math:`S = 11, E = 7`)—an indispensable engine for triangle-center Problems L–LXIII!
