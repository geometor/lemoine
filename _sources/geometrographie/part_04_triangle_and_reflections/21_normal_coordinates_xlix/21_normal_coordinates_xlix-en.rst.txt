:layout: book
:canonical_id: Prob. XLIX
:order: 2
:folio: 0056
:tracks: English: 21_normal_coordinates_xlix-en | French: 21_normal_coordinates_xlix-fr | Summary: 21_normal_coordinates_xlix-summary | Notes: 21_normal_coordinates_xlix-notes

.. _lemoine-21_normal_coordinates_xlix-en:

Problem XLIX: Constructing a Point from Normal Coordinates
==========================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 40–42, fols. ``0056–0058``)

.. folio:: 0056
   :page: p. 40

**Problem XLIX — Locate a Point :g:`M` with Respect to Reference Triangle :g:`ABC` Given Lengths :math:`l, m, n` Proportional to Its Normal (Trilinear) Coordinates (FIG. 11).**
Opening his capstone investigation of modern triangle geometry (:cite:`lemoine-1873`, :cite:`altshiller-court-1952`, :cite:`kimberling-etc`), :person:`Lemoine <lemoine>` first solves the universal coordinate-plotting problem: given three signed distances :math:`l, m, n` proportional to the perpendicular distances from :g:`M` to sides :g:`BC`, :g:`CA`, :g:`AB`, construct :g:`M` without computing algebraic coordinates!

On folios ``0056``–``0057`` (pp. 40–41, **FIG. 11**):
1. Erect three perpendiculars :g:`A'O`, :g:`B'O`, :g:`C'γ₁` to sides :g:`BC`, :g:`CA`, :g:`AB` (conveniently as the three perpendicular bisectors of :g:`ABC` via three shared-radius vertex circles: :math:`6R_1 + 3R_2 + 3C_1 + 3C_3`).
2. Along each perpendicular from feet :g:`A'`, :g:`B'`, :g:`C'`, lay off signed normal offsets :math:`A'\alpha_1 = l`, :math:`B'\beta_1 = m`, and :math:`C'\gamma_1 = n` (inward if positive, outward if negative—note :g:`γ₁` lies outward on **FIG. 11**!) and trace the three parallels :g:`C₂B₂` :math:`\parallel BC`, :g:`C₂A₂` :math:`\parallel CA`, and :g:`A₂B₂` :math:`\parallel AB` (each via a square corner :g:`A₁` on :g:`BC`, costing :math:`3[2R_1 + R_2 + 5C_1 + 3C_3]`).
3. These three parallels form a triangle :math:`\triangle A_2 B_2 C_2` directly homothetic to :g:`ABC`; joining two pairs of corresponding vertices :g:`AM` (through :g:`A, A₂`) and :g:`BM` (through :g:`B, B₂`, :math:`4R_1 + 2R_2`) fixes their center of homothety—the exact sought point :g:`M`!

.. folio:: 0057
   :page: p. 41

.. math::

   \mathrm{Op.} : \left(16R_1 + 8R_2 + 18C_1 + 12C_3\right), \qquad S = 54, \quad E = 34 \quad (8\text{ lines}, 12\text{ circles}).

.. container:: lemoine-plate-pair

   .. picture:: 0056.g1.png
      :alt: Archival 1893 engraving FIG. 11 of Problem XLIX showing homothetic triangle A2B2C2 locating M from normal coordinates
      :caption: FIG. 11 archival scan (Paris 1893, fol. 0056, p. 40): Homothetic triangle A₂B₂C₂ and center M from trilinear coordinates (l : m : n).

   .. picture:: 0056.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 11 (Problem XLIX normal coordinates l, m, n)
      :caption: FIG. 11 vectorization: Exact SymPy calibration of perpendiculars A'O, B'O, C'γ₁, homothetic triangle A₂B₂C₂, and rays AM, BM meeting at M (S = 54).

On page 41, Lemoine improves his own 1888 *Bulletin de la Soc. math.* solution (:math:`S = 71 \to S = 54`) and pauses for a profound epistemological reflection: **there is no general theoretical criterion** guaranteeing that a given construction is the absolute minimum possible, because another geometer may discover either a better graphical execution of the same theorem or a simpler underlying theorem; yet *practically*, recording each improvement rapidly converges to definitive minimal benchmarks.

.. folio:: 0058
   :page: p. 42

When two *absolute* normal coordinates :math:`l, m` are known (case *b*, pp. 41–42), erecting perpendiculars at :math:`C` yields :math:`M` in :math:`S = 38` (:math:`12R_1 + 6R_2 + 12C_1 + 8C_3`, :math:`E = 24`, or :math:`16R_1 + 8R_2 + 9C_1 + 5C_3`, :math:`E = 25`). Yet Lemoine concludes (p. 42) that **generic trilinear plotting (:math:`S = 54`) is always far more complicated** than exploiting the synthetic geometry of each individual triangle center—launching Problems L–LXIII!
