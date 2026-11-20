:layout: book
:canonical_id: Probs. XLVII–XLVIII
:order: 9
:folio: 0050
:tracks: English: 19_square_and_ellipse_axes_xlvii_xlviii-en | French: 19_square_and_ellipse_axes_xlvii_xlviii-fr | Summary: 19_square_and_ellipse_axes_xlvii_xlviii-summary | Notes: 19_square_and_ellipse_axes_xlvii_xlviii-notes

.. _lemoine-19_square_and_ellipse_axes_xlvii_xlviii-en:

Problems XLVII–XLVIII: Catalan's Square & Axes of an Ellipse
============================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 34–36, fols. ``0050–0052``)

.. folio:: 0050
   :page: p. 34

**Problem XLVII — Construct the Square :g:`ABCD` on Given Side :g:`AB` (:person:`Eugène Catalan <catalan>`'s 1847 Construction, FIG. 9).**
To locate the two opposite vertices :g:`C` and :g:`D` of the square erected on :g:`AB`, Lemoine analyzes :person:`Catalan <catalan>`'s ingenious four-circle construction (*Théorèmes et problèmes de Géométrie élémentaire*, 1847):

1. Retaining the single aperture :math:`AB`, sweep :g:`A(AB)` and :g:`B(AB)` meeting at equilateral vertex :g:`K`, then sweep :g:`K(AB)` cutting :g:`B(AB)` again at :g:`G` (:math:`4C_1 + 3C_3`).
2. Draw the **single straight line** :g:`AG` (:math:`2R_1 + R_2`), cutting :g:`A(AB)` at :g:`I` (the exact :math:`30^\circ` point!).
3. Capture chord :math:`KI` (which algebraically equals :math:`AB\sqrt{2 - \sqrt{3}}`, the exact side of a regular dodecagon!) and sweep :g:`K(KI)` (:math:`2C_1 + C_3`), cutting :g:`B(AB)` at :g:`C` and :g:`A(AB)` at :g:`D`:

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 6C_1 + 4C_3\right), \qquad S = 13, \quad E = 8 \quad (1\text{ line}, 4\text{ circles for vertices }C, D).

To trace the three remaining sides :g:`BC`, :g:`CD`, :g:`DA` adds :math:`6R_1 + 3R_2` (totaling :math:`8R_1 + 4R_2 + 6C_1 + 4C_3`, :math:`S = 22`, 4 lines, 4 circles—remarkably, Lemoine shows on p. 34 that the ordinary perpendicular erection builds the *fully traced* square in :math:`6R_1 + 3R_2 + 7C_1 + 5C_3`, :math:`S = 21`, so Catalan's elegance shines for locating the *vertices* :g:`C, D`, whereas ordinary erection edges it by 1 operation when all four sides must be ruled!).

.. container:: lemoine-plate-pair

   .. picture:: 0050.g1.png
      :alt: Archival 1893 engraving FIG. 9 of Problem XLVII showing Catalan's 4-circle square construction
      :caption: FIG. 9 archival scan (Paris 1893, fol. 0050, p. 34): Eugène Catalan's 1847 construction of square vertices C, D on AB.

   .. picture:: 0050.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 9 (Problem XLVII Catalan's square on AB)
      :caption: FIG. 9 vectorization: Exact SymPy calibration of A(AB), B(AB), K(AB), line AG fixing I, and circle K(KI) cutting vertices C and D (S = 13).

.. folio:: 0051
   :page: p. 35

**Problem XLVIII — Axes of an Ellipse in Position and Magnitude from Two Conjugate Semi-Diameters :math:`OA, OB` (:person:`Michel Chasles <chasles>`, *Aperçu historique*, Note 25).**
Here Lemoine delivers one of his sharpest indictments of speculative geometry! :person:`Chasles <chasles>`'s famous Note 25 construction erects a perpendicular at :math:`A` to :math:`OB`, lays off :math:`AC = AD = OB`, joins :math:`OC, OD`, and bisects :math:`\angle COD` and its supplement—stopping after :math:`10R_1 + 5R_2 + 10C_1 + 8C_3` (:math:`S = 33`) with the remark that *the sum :math:`OC + OD` equals the major axis and their difference :math:`OC - OD` equals the minor axis*.

Yet to actually *place* the semi-axes in position on the sheet requires sweeping :math:`O(OD)` across :math:`OC`, bisecting both :math:`CE` and :math:`CF`, and transferring each semi-axis onto the two bisector lines—an omitted tail costing :math:`4R_1 + 2R_2 + 11C_1 + 6C_3` (more than **two-thirds** of what Chasles had stated!), bringing Chasles's full execution to:

.. math::

   \mathrm{Op.} : \left(14R_1 + 7R_2 + 21C_1 + 14C_3\right), \qquad S = 56, \quad E = 35 \quad (7\text{ lines}, 14\text{ circles}).

.. folio:: 0052
   :page: p. 36

As Lemoine wryly observes (pp. 35–36), finding the *full* axes instead of the *semi-axes* in position *"is a mere detail for the speculative geometer, but by no means for the draftsman executing the plate"*—and on p. 36 Lemoine contrasts Chasles's :math:`S = 56` with simpler alternative ellipse-axis constructions (including the :math:`S = 34` Rytz/Mannheim-style synthesis), introducing the five *Principes* of Part IV.
