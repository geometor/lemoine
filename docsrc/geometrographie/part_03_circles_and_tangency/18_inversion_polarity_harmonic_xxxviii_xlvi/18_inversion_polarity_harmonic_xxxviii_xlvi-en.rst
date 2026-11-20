:layout: book
:canonical_id: Probs. XXXVIII–XLVI
:order: 8
:folio: 0045
:tracks: English: 18_inversion_polarity_harmonic_xxxviii_xlvi-en | French: 18_inversion_polarity_harmonic_xxxviii_xlvi-fr | Summary: 18_inversion_polarity_harmonic_xxxviii_xlvi-summary | Notes: 18_inversion_polarity_harmonic_xxxviii_xlvi-notes

.. _lemoine-18_inversion_polarity_harmonic_xxxviii_xlvi-en:
.. _lemoine-en-projective-inversive:

Problems XXXVIII–XLVI: Inversion, Polarity, Radical Axis & Harmonic Conjugates
==============================================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 29–33, fols. ``0045–0049``)

.. folio:: 0045
   :page: p. 29

Problems XXXVIII–XLVI reveal the deepest structural discovery of *Géométrographie*: even when both instruments are allowed, pure **compass-only** (:person:`Mascheroni <mascheroni>`) or pure **straightedge-only** (:person:`Pappus <pappus>`, :person:`Steiner <steiner>`) syntheses frequently beat mixed constructions!

**Problem XXXVIII (:term:`Circle Inversion <inversion>` — Inverse Point :math:`A'` of :math:`A` with Respect to :math:`O(R)`).**
1. *When :math:`OA > R/2` (Compass Alone!)*: Sweep :math:`A(AO)` cutting :math:`O(R)` at :math:`B, C`, then sweep :math:`B(R)` and :math:`C(R)` meeting at :math:`O` and :math:`A'` (:ref:`concordance-circle-inversion`):

.. math::

   \mathrm{Op.} : \left(5C_1 + 3C_3\right), \qquad S = 8, \quad E = 5 \quad (0\text{ lines}, 3\text{ circles}).

This exact 3-circle lemma powered :person:`August Adler <adler>`'s 1890 conceptual proof of the :person:`Mohr <mohr>`–:person:`Mascheroni <mascheroni>` theorem (:cite:`adler-1890`)!
2. *General case (:math:`OA < R/2`)*: Draw :math:`OA`, sweep :math:`A(R)` cutting :math:`O(R)` at :math:`B`, sweep :math:`B(R)` cutting :math:`O(R)` at :math:`D, D'`, and draw :math:`DD'` cutting :math:`OA` at :math:`A'`: :math:`4R_1 + 2R_2 + 4C_1 + 2C_3` (:math:`S = 12, E = 8`, 2 lines, 2 circles). A 1-circle general method also exists in :math:`8R_1 + 4R_2 + C_1 + C_3` (:math:`S = 14`).

**Problem XXXIX (:term:`Polar Line <polaire>` of :math:`A` with Respect to Circle :math:`O(R)` — Straightedge Alone!).**
*Method (a)*: Draw two arbitrary secants through :math:`A` cutting the circumference at :math:`B, B'` and :math:`C, C'` (:math:`2R_1 + 2R_2`); intersect :math:`B'C', BC` at :math:`D` and :math:`BC', CB'` at :math:`E`, then join :math:`ED` (:ref:`concordance-polar-of-point`):

.. math::

   \mathrm{Op.} : \left(12R_1 + 7R_2\right), \qquad S = 19, \quad E = 12 \quad (7\text{ lines}, 0\text{ circles}),

identical to :person:`Jakob Steiner <steiner>` § 10 (:cite:`steiner-1833`) and strictly beating classical ruler-and-compass (:math:`S = 25`)!

.. folio:: 0046
   :page: p. 30

*Method (b)* drops a perpendicular from :math:`D` to un-traced :math:`OA` in :math:`8R_1 + 5R_2 + 4C_1 + 2C_3` (also :math:`S = 19, E = 12`). When :math:`OA > R/2`, non-general *Method (c)* yields :math:`4R_1 + 2R_2 + 5C_1 + 3C_3` (:math:`S = 14, E = 9`, correcting Lemoine's earlier 1888 *Mathesis* slip).

**Problem XL — Pole :math:`L` of a Line :math:`XY` with Respect to :math:`O(R)`.**
1° When :math:`XY` cuts :math:`O(R)` at :math:`M, N`: draw tangent at :math:`M` (Problem XXV), sweep :math:`N(R)` cutting :math:`M(R)` at :math:`O'`, and draw :math:`OO'` meeting the tangent at :math:`L`: :math:`4R_1 + 2R_2 + 5C_1 + 4C_3` (:math:`S = 15, E = 9`, 2 lines, 4 circles).

.. folio:: 0047
   :page: p. 31

2° When :math:`XY` does not cut :math:`O(R)` (or distance :math:`OF > R/2`): drop perpendicular :math:`OF` to :math:`XY`, sweep :math:`F(FO)` cutting :math:`O(R)` at :math:`H`, and sweep :math:`H(R)` cutting :math:`OF` at :math:`L`: :math:`2R_1 + R_2 + 7C_1 + 5C_3` (:math:`S = 15, E = 9`, 1 line, 5 circles). Together, 1° and 2° achieve a uniform general cost of :math:`S = 15`!

**Problem XLI (:term:`Radical Axis <linie-der-gleichen-potenzen>` of Two Circles :math:`O(R), O'(R')`).**
Sweep **two completely arbitrary secant circles** :math:`\omega(\rho), \omega'(\rho')` (:math:`2C_3`—zero alignment cost!) each intersecting both given circles, join pairwise common chords to locate two radical centers, and join them (:ref:`concordance-radical-axis`):

.. math::

   \mathrm{Op.} : \left(10R_1 + 5R_2 + 2C_3\right), \qquad S = 17, \quad E = 10 \quad (5\text{ lines}, 2\text{ circles}),

dramatically defeating :person:`Amédée Mannheim <mannheim>`'s common-tangent construction (:math:`S = 58`, pp. 57–58)! (Tangent circles reduce to :math:`S = 10`, intersecting circles to :math:`2R_1 + R_2`, :math:`S = 3`.)

**Problem XLII — Radical Center of Three Circles :math:`R_1, R_2, R_3`.**

.. folio:: 0048
   :page: p. 32

Across all five incidence cases (pp. 31–32), the symbol decreases from :math:`16R_1 + 8R_2 + 2C_3` (:math:`S = 26`, disjoint) and :math:`16R_1 + 8R_2 + C_3` (:math:`S = 25`, mutually tangent) down to :math:`8R_1 + 4R_2 + C_3` (:math:`S = 13`) and :math:`4R_1 + 2R_2` (:math:`S = 6`, pairwise intersecting).

**Problem XLIII — Plot Point :math:`M` from Cartesian Coordinates :math:`(x, y)` on Axes :math:`ox, oy` (Compass Alone!).**
Lay off :math:`OA = x` on :math:`ox`, :math:`OB = y` on :math:`oy`, and intersect :math:`A(y)` with :math:`B(x)` at :math:`M`: :math:`10C_1 + 4C_3` (:math:`S = 14, E = 10`, **0 lines, 4 circles**; or :math:`8C_1 + 4C_3` with two compasses). In footnote (*) on p. 32, Lemoine thanks :person:`Gaston Tarry <tarry>` for two years of correspondence that uncovered numerous simplifications throughout this memoir.

**Problems XLIV & XLV — Centers & Four Axes of Similitude of Two and Three Circles.**

.. folio:: 0049
   :page: p. 33

From Problem XXIX (**FIG. 3**), both centers of similitude :math:`V, V_1` of two circles cost :math:`6R_1 + 3R_2 + 4C_1 + 2C_3` (:math:`S = 15, E = 10`, 3 lines, 2 circles), while the four axes of similitude of three circles drop from :math:`S = 46` to :math:`24R_1 + 12R_2 + 4C_1 + 2C_3` (:math:`S = 42, E = 28`, 12 lines, 2 circles) via parallel diameters through :math:`O''`.

**Problem XLVI (:term:`Harmonic Conjugate <conjugue-harmonique>` :math:`C'` of :math:`C` with Respect to :math:`A, B` — Straightedge Alone!).**
Draw arbitrary ray :math:`CDE` through :math:`C` and two rays :math:`AD, AE` through :math:`A` (:math:`3R_1 + 3R_2`); draw :math:`DB, EB` (:math:`4R_1 + 2R_2`) cutting :math:`AE, AD` at :math:`F, G`; draw :math:`FG` (:math:`2R_1 + R_2`) cutting :math:`AB` at :math:`C'` (:person:`Pappus <pappus>` *Synagoge* Book VII, :cite:`pappus-synagoge`; :person:`Steiner <steiner>` §§ 4–6; :ref:`concordance-harmonic-conjugate`):

.. math::

   \mathrm{Op.} : \left(9R_1 + 6R_2\right), \qquad S = 15, \quad E = 9 \quad (6\text{ lines}, 0\text{ circles}).
