:layout: book
:canonical_id: Probs. XXX–XXXII
:order: 4
:folio: 0035
:tracks: English: 14_multiples_and_division_xxx_xxxii-en | French: 14_multiples_and_division_xxx_xxxii-fr | Summary: 14_multiples_and_division_xxx_xxxii-summary | Notes: 14_multiples_and_division_xxx_xxxii-notes

.. _lemoine-14_multiples_and_division_xxx_xxxii-en:

Problems XXX–XXXII: Segment Division & Parallels
================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 19–20, fols. ``0035–0036``)

.. folio:: 0035
   :page: p. 19

**Problem XXX — Construct Segment :math:`CD = n \cdot AB` (:math:`n`-Fold Multiple).**
Drawing an arbitrary carrier line (:math:`R_2`) and applying Application VIII's :math:`n`-fold stepping rule (p. 6) yields:
1. *Without marking intermediate divisions*: :math:`\mathrm{Op.} : [R_2 + (n + 2)C_1 + C_2]`.
2. *Marking every intermediate division*: :math:`\mathrm{Op.} : [R_2 + (n + 1)C_1 + C_2 + nC_3]`.

**Problem XXXI (Euclid VI.9 — Construct :math:`CD = \frac{1}{n} AB`).**
Trace two arbitrary intersecting lines :math:`OH, OL` (:math:`2R_2`), lay off :math:`AB` as :math:`OH` (:math:`3C_1 + C_3`), step an arbitrary compass opening :math:`n` times along :math:`OL` marking only the last two divisions :math:`K` and :math:`L` (:math:`2C_1 + nC_3`), and through :math:`K` draw the parallel to un-traced :math:`LH` (:math:`2R_1 + R_2 + 6C_1 + 2C_3`, Problem XVII remark) cutting :math:`OH` at :math:`G` so :math:`GH = \frac{1}{n} AB`:

.. folio:: 0036
   :page: p. 20

.. math::

   \mathrm{Op.} : \left[2R_1 + 3R_2 + 11C_1 + (n + 3)C_3\right], \qquad S = 19 + n, \quad E = n + 10 \quad (3\text{ lines}, n+3\text{ circles}).

For special integers (:math:`n = 2, 3, 4, 2^p`, or :math:`n = 10, 15` later in **FIG. 10**), dedicated geometric configurations beat this general Thales formula substantially.

**Problem XXXII (Euclid VI.10 — Divide Segment :math:`AB` into :math:`p` Parts Proportional to :math:`n_1, n_2, \dots, n_p`).**
Draw ray :math:`BX` through :math:`B` (:math:`R_1 + R_2`), lay off :math:`BN_1 = n_1, \dots, N_{p-1}N_p = n_p` sequentially along :math:`BX` (:math:`p[3C_1 + C_3]`), join :math:`AN_p` (:math:`2R_1 + R_2`), and copy angle :math:`\angle BN_pA` at each division point :math:`N_{p-1}, \dots, N_1` (:math:`2(p-1)R_1 + (p-1)R_2 + (2p+1)C_1 + (2p-1)C_3`):

.. math::

   \mathrm{Op.} : \left[(2p + 1)R_1 + (p + 1)R_2 + (5p + 1)C_1 + (3p - 1)C_3\right], \qquad S = 11p + 2, \quad E = 7p + 2.

In the rich philosophical footnote (*) on folio ``0036`` (p. 20), :person:`Lemoine <lemoine>` states two foundational operational laws:
1. **Multiple Compasses**: Although single-compass execution is the default, keeping a second compass holding a recurring radius saves :math:`2C_1` every time that opening would otherwise be reset.
2. **Independence of Execution Order from Proof Order**: The sequence of strokes on the drawing sheet need *not* follow the linear sequence of deductive reasoning—if a proof reveals several circles of equal radius whose centers are already determined, the draftsman should sweep **all** of them before altering the compass aperture!
