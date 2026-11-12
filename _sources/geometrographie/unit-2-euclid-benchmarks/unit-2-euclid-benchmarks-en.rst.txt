:layout: book

.. _geometrographie-unit-2-en:

Unit II: Fundamental Speculative vs. *Géométrographique* Constructions (Euclid Book I Benchmarks)
=================================================================================================

.. rubric:: Émile Lemoine — *Géométrographie, ou Art des constructions géométriques* (English Translation, Problems XI–XXIV, pp. 6–14)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _lemoine-en-copy-angle-triangles:

.. folio:: Problèmes XI–XVI
   :page: 6

§ 1. Copying an Angle (XI) and Constructing Triangles (XII–XVI)
---------------------------------------------------------------

In Book I of :person:`Euclid <euclid>`'s *Elements* (:cite:`euclid-heath`; see :external+euclid:doc:`index` and :external+elements:doc:`index`), Proposition I.23 constructs at a given point on a straight line an angle equal to a given rectilinear angle by first joining two arbitrary points across the arms of the given angle and then invoking Proposition I.22 (triangle from three segments). Executed literally on the drawing sheet, that speculative reduction draws an unnecessary auxiliary straight line across the given angle (:math:`4R_1 + 2R_2 + 8C_1 + C_2 + 4C_3`, :math:`S = 19, E = 13`).

**Problem XI (Euclid I.23 — Equal Angle at a Given Point).** Given angle :math:`O` and a point :math:`A` marked on a traced line :math:`AB`, open the compass to an *arbitrary* radius, sweep an arc centered at :math:`O` (:math:`C_1 + C_3`) cutting the arms of angle :math:`O` at :math:`M, N`, and with the **same** unaltered radius sweep an arc centered at :math:`A` (:math:`C_1 + C_3`) cutting :math:`AB` at :math:`M'`. Span chord :math:`MN` with the compass (:math:`2C_1`), transfer it to center :math:`M'` (:math:`C_1 + C_3`) cutting the second arc at :math:`N'`, and join :math:`AN'` (:math:`2R_1 + R_2`):

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 5C_1 + 3C_3\right), \qquad S = 11, \quad E = 7 \quad (1\text{ line}, 3\text{ circles}).

If the vertex on :math:`AB` may be taken at an indeterminate point of the line, one :math:`C_1` becomes :math:`C_2` (:math:`2R_1 + R_2 + 4C_1 + C_2 + 3C_3`, still :math:`S = 11, E = 7`).

**Problem XVI (Euclid I.22 — Triangle from Three Given Sides :math:`a, b, c`).** Instead of placing two points first and aligning a ruler across them (:math:`2R_1 + R_2`), draw an arbitrary carrier line directly (:math:`R_2`), lay off :math:`BC = a` from an indeterminate point :math:`B` (:math:`2C_1 + C_2 + C_3`), sweep :math:`B(c)` (:math:`3C_1 + C_3`) and :math:`C(b)` (:math:`3C_1 + C_3`) meeting at :math:`A`, and join :math:`AB, AC` (:math:`4R_1 + 2R_2`):

.. math::

   \mathrm{Op.} : \left(4R_1 + 3R_2 + 8C_1 + C_2 + 3C_3\right), \qquad S = 19, \quad E = 13 \quad (3\text{ lines}, 3\text{ circles}),

saving three operations over textbook execution (:math:`S = 22`).

.. _lemoine-en-parallel-tarry:

.. folio:: Problème XVII
   :page: 8

§ 2. Parallel Through an External Point (XVII): Classical :math:`S = 11` vs. Gaston Tarry's :math:`S = 9`
---------------------------------------------------------------------------------------------------------

**Problem XVII (Euclid I.31).** *Through a given point* :g:`A` *outside a traced straight line* :g:`BC` *, to draw a straight line parallel to* :g:`BC`.

* **Classical Alternate-Angle Method** (:math:`S = 11, E = 7`): Sweep an arc from an arbitrary center on :g:`BC` through :g:`A`? Even without drawing the transversal line, the traditional equal-angle construction takes center :math:`P` on :g:`BC`, sweeps :math:`P(PA)`, sweeps :math:`A(AP)` cutting :g:`BC` at :math:`Q`? In standard practice it costs :math:`2R_1 + R_2 + 5C_1 + 3C_3` (:math:`S = 11, E = 7`, 1 line, 3 circles).
* **Gaston Tarry's First Géométrographique Construction (Two Equal Circles, :math:`S = 9, E = 6`)**: Communicated to :person:`Lemoine <lemoine>` by :person:`Gaston Tarry <tarry>`, choose an arbitrary point in the plane, sweep a circle passing through :g:`A` (:math:`C_1 + C_3`—setting one leg on :g:`A` and the pivot arbitrarily!) that cuts :g:`BC` in :math:`M` and :math:`N`. Keeping the **same radius**, span chord :math:`AM`? Even simpler: shift the circle along :g:`BC` by placing one leg at :math:`N`? Specifically, Tarry's two-circle method uses :math:`2R_1 + R_2 + 4C_1 + 2C_3` (:math:`S = 9, E = 6`, **1 line, 2 circles**).
* **Gaston Tarry's Second Géométrographique Construction (Single-Aperture Rhombus, :math:`S = 9, E = 5`)**: Open the compass to any sufficient radius :math:`R`. Set one leg on :g:`A` (:math:`C_1`) and place the pivot on :g:`BC` by sweeping an arc from :g:`A` (:math:`C_3`) cutting :g:`BC` at :g:`P`. Keeping the **same aperture** :math:`R`, center at :g:`P` (:math:`C_1 + C_3`) to cut :g:`BC` at :g:`Q`, and center at :g:`Q` (:math:`C_1 + C_3`) to cut the first arc :math:`A(R)` at :g:`D`. Because :math:`PA = PQ = QD = DA = R`, quadrilateral :g:`APQD` is a rhombus; joining :g:`AD` (:math:`2R_1 + R_2`) gives the parallel:

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 3C_1 + 3C_3\right), \qquad S = 9, \quad E = 5 \quad (1\text{ line}, 3\text{ circles}).

.. picture:: /_static/figures/fig_parallel_comparison.svg

Notice the remarkable trade-off illuminated by *Géométrographie*: Tarry's first method draws one fewer circle (:math:`2` vs. :math:`3`) at :math:`E = 6`, whereas Tarry's rhombus method achieves the superior exactitude :math:`E = 5` at the identical simplicity :math:`S = 9`!

.. _lemoine-en-bisector-reflection:

.. folio:: Problèmes XVIII–XIX
   :page: 9

§ 3. Perpendicular Bisector, Midpoint (XVIII), and Compass-Only Reflection (XVIII *bis*)
----------------------------------------------------------------------------------------

**Problem XVIII (Euclid I.10 — Perpendicular Bisector and Midpoint).** To trace the perpendicular bisector :g:`PQ` of two given points :g:`A` and :g:`B` (or bisect segment :g:`AB` at :g:`M`), :person:`Euclid <euclid>` sets the compass specifically to radius :math:`AB` (:math:`2C_1 + C_3` at :g:`A`, then :math:`C_1 + C_3` at :g:`B`), costing :math:`S = 8, E = 5`. :person:`Lemoine <lemoine>` observes that any *arbitrary* shared aperture :math:`R > AB/2` suffices: sweep :g:`A(R)` (:math:`C_1 + C_3`) and :g:`B(R)` (:math:`C_1 + C_3`) meeting at :g:`P` and :g:`Q`, and draw :g:`PQ` (:math:`2R_1 + R_2`) bisecting :g:`AB` into :g:`AM` and :g:`MB`:

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 2C_1 + 2C_3\right), \qquad S = 7, \quad E = 4 \quad (1\text{ line}, 2\text{ circles}).

.. picture:: /_static/figures/fig_perpendicular_bisector.svg

**Problem XVIII bis (Symmetric Reflection Across a Line — Zero Straight Lines!).** To construct the reflection :math:`A'` of a point :math:`A` across a traced line :math:`BC`, textbooks drop a perpendicular, extend it, and transfer the foot distance (:math:`S = 15`). Lemoine executes reflection **without touching the straightedge**: pick two indeterminate points on :math:`BC` (:math:`2C_2`), set the other leg on :math:`A` (:math:`2C_1`), and sweep two circles (:math:`2C_3`) whose second intersection is :math:`A'`:

.. math::

   \mathrm{Op.} : \left(2C_1 + 2C_2 + 2C_3\right), \qquad S = 6, \quad E = 4 \quad (0\text{ lines}, 2\text{ circles}),

and if two points :math:`B, C` are already marked on the mirror line, :math:`4C_1 + 2C_3` (or :math:`3C_1 + 3C_3`), still :math:`S = 6`—identical to :person:`Mascheroni <mascheroni>`'s compass-only reflection (:cite:`mascheroni-1797`, Libro IV, § 78)!

.. _lemoine-en-perpendiculars-bisector:

.. folio:: Problèmes XX–XXIV
   :page: 11

§ 4. Perpendiculars Off/On a Line (XX — Thales Single-Circle :math:`S = 8`) & Angle Bisection (XXII)
----------------------------------------------------------------------------------------------------

**Problem XX (Euclid I.12 & I.11 — Perpendicular Through :math:`A` to Traced Line :math:`BC`).**

1. **Case 1 — Point :g:`A` Outside :g:`BC` (Euclid I.12, :math:`S = 9`)**: Instead of drawing a circle around :g:`A` cutting :g:`BC` in two points and then bisecting that chord (3 circles, :math:`S = 10`), construct the symmetric image :g:`A'` of :g:`A` using one marked point or one arbitrary point :g:`B` and a second point :g:`C` on :g:`BC`, then join :g:`AA'` (:math:`2R_1 + R_2 + 3C_1 + C_2 + 2C_3`, :math:`S = 9, E = 6`, 1 line, **2 circles**; or :math:`2R_1 + R_2 + 3C_1 + 3C_3`, :math:`S = 9, E = 5` if a point is pre-marked on :g:`BC`).
2. **Case 2 — Point :g:`A` Lying On :g:`BC` (Euclid I.11 via III.31, :math:`S = 8`, One Single Circle!)**: Classical erection steps off equal segments on either side of :g:`A` and bisects them (3 circles, :math:`S = 9` or :math:`10`). By invoking Thales's theorem on the angle in a semicircle, place one compass leg on :g:`A` (:math:`C_1`) and pivot around a completely *arbitrary* plane point :g:`O` off :g:`BC` (:math:`0` cost!) to sweep the **single circle** :g:`O(OA)` (:math:`C_3`), cutting :g:`BC` again at :g:`B`. Draw the diameter :g:`BD` through :g:`B` and :g:`O` (:math:`2R_1 + R_2`) meeting :g:`O(OA)` at :g:`D`, and join :g:`AD` (:math:`2R_1 + R_2`):

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + C_1 + C_3\right), \qquad S = 8, \quad E = 5 \quad (2\text{ lines}, 1\text{ circle}).

.. picture:: /_static/figures/fig_perpendicular_external.svg

**Problem XXII (Euclid I.9 — Angle Bisector, :math:`S = 9`).** Keeping a *single* arbitrary sufficient radius :math:`R` for the initial arc centered at vertex :math:`A` (:math:`C_1 + C_3`, cutting the arms at :math:`B, D`) and for both intersecting arcs centered at :math:`B` and :math:`D` (:math:`2C_1 + 2C_3`), then joining :math:`A` to their intersection (:math:`2R_1 + R_2`), bisects any rectilinear angle in :math:`2R_1 + R_2 + 3C_1 + 3C_3` (:math:`S = 9, E = 5`, 1 line, 3 circles—saving 1 :math:`C_1` over Euclid I.9's equilateral-chord reset :math:`S = 10`).
