:layout: book

.. _geometrographie-unit-3-en:

Unit III: Circles, Tangency, Golden Section, Projective Polarity & Modern Triangle Centers
==========================================================================================

.. rubric:: Émile Lemoine — *Géométrographie, ou Art des constructions géométriques* (English Translation, Problems XXI & XXV–LXIII, pp. 12–51)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _lemoine-en-circles-tangents-incircle:

.. folio:: Problèmes XXI, XXV–XXVII
   :page: 15

§ 1. Circumcircle (XXI), Circle Tangents (XXV–XXVI), and Incircle :math:`X(1)` (XXVII)
--------------------------------------------------------------------------------------

**Problem XXI (Euclid IV.5 — Circumcircle and Circumcenter :math:`X(3)`, :math:`S = 15`).** Given three non-collinear points :math:`A, B, C`, open the compass to one arbitrary radius :math:`R` greater than half of :math:`AB` and :math:`BC`. Sweep :math:`B(R)` once (:math:`C_1 + C_3`), then :math:`A(R)` (:math:`C_1 + C_3`) and :math:`C(R)` (:math:`C_1 + C_3`). Reusing :math:`B(R)` across both perpendicular bisectors cuts the auxiliary circle count from four to three; drawing the two mediatrices (:math:`4R_1 + 2R_2`) locates the circumcenter :math:`O = X(3)`, and sweeping :math:`O(A)` (:math:`2C_1 + C_3`) completes the circumcircle in :math:`4R_1 + 2R_2 + 5C_1 + 4C_3` (:math:`S = 15, E = 9`, 2 lines, 4 circles vs. classical :math:`S = 17`).

**Problems XXV & XXVI (Euclid III.16 Por. & III.17 — Tangents to a Circle).**

* **Tangent at a Point :math:`A` on Traced Circle :math:`O` (XXV)**: Place one leg at :math:`A` (:math:`C_1`), pivot around an arbitrary exterior point :math:`P` to draw :math:`P(PA)` (:math:`C_3`) cutting circle :math:`O` again at :math:`B`, draw diameter :math:`BPC` (:math:`2R_1 + R_2`)—when :math:`P` is chosen on ray :math:`OA` or via Thales semicircle on :math:`OA`—yielding :math:`4R_1 + 2R_2 + C_1 + C_3` (:math:`S = 8`, **1 circle**).
* **Tangents from an External Point :g:`A` to Circle :g:`O(R)` (XXVI)**: Classical *Elements* III.17 uses concentric circles (:math:`8R_1 + 4R_2 + 4C_1 + 3C_3, S = 19`). Lemoine reduces the cost to :math:`S = 18` via two distinct syntheses—either :math:`5R_1 + 3R_2 + 7C_1 + 3C_3` (:math:`E = 12`, 3 circles) or bisecting :g:`OA` at :g:`M` to sweep :g:`M(MO)` cutting :g:`O(R)` at :g:`T`, :g:`T'` and joining :g:`AT`, :g:`AT'` (:math:`5R_1 + 3R_2 + 6C_1 + 4C_3, S = 18, E = 11`).

.. picture:: /_static/figures/fig_circle_tangents.svg

**Problem XXVII (Euclid IV.4 — Incircle and Incenter :math:`I = X(1)`, :math:`S = 23` vs. :math:`S = 30`).** Textbook execution bisects two angles of :g:`ABC` (6 circles, 2 lines), drops a full perpendicular line from incenter :g:`I` to :g:`BC` (3 circles, 1 line), and finally draws the incircle (1 circle): **3 lines and 10 circles** (:math:`6R_1 + 3R_2 + 11C_1 + 10C_3, S = 30, E = 17`). :person:`Lemoine <lemoine>` cuts **seven operations and four circles** by: (1) sharing one compass radius across vertices :g:`B` and :g:`C` to draw bisectors :g:`BI` and :g:`CI` meeting at :g:`I` (:math:`X(1)` in :external+etc:doc:`index`), and (2) determining the perpendicular touch-radius :g:`ID` to :g:`BC` via symmetric compass arcs *without tracing the third straight line* before sweeping :g:`I(ID)`:

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 11C_1 + 6C_3\right), \qquad S = 23, \quad E = 15 \quad (2\text{ lines}, 6\text{ circles}).

.. picture:: /_static/figures/fig_incircle_lemoine.svg

.. _lemoine-en-proportions-golden:

.. folio:: Problèmes XXXIII–XXXVI
   :page: 24

§ 2. Proportions (XXXIII–XXXV) & Division in Extreme and Mean Ratio :math:`\phi` (XXXVI)
----------------------------------------------------------------------------------------

* **Fourth & Third Proportionals (XXXIII–XXXIV, Euclid VI.12 & VI.11)**: Constructing :math:`x = bc/a` drops from :math:`S = 25` to :math:`2R_1 + 2R_2 + 11C_1 + C_2 + 6C_3` (:math:`S = 22, E = 14`), while :math:`x = b^2/a` drops from :math:`S = 22` to :math:`4R_1 + 2R_2 + 5C_1 + C_2 + 3C_3` (:math:`S = 15, E = 10`).
* **Mean Proportional :math:`\sqrt{ab}` (XXXV, Euclid II.14 / VI.13 — Lemoine–Gouzy Construction, :math:`S = 14`)**: Classical semicircle erection on :math:`a + b` requires 3 lines and 6 circles (:math:`S = 24`). With :person:`Auguste Gouzy <gouzy>`, Lemoine constructs :math:`\sqrt{ab}` in **half the circles** (:math:`2R_1 + 2R_2 + 6C_1 + C_2 + 3C_3`, :math:`S = 14, E = 9`, 2 lines, 3 circles).

**Problem XXXVI (Euclid II.11 & VI.30 — Golden Section :math:`\phi`, :math:`S = 18` in One Single Line!).** To divide a given segment :g:`AB` in :term:`extreme and mean ratio <moyenne-et-extreme-raison>` (:math:`AB / AX = AX / XB = \phi = \frac{1+\sqrt{5}}{2}`), classical constructions draw *three* auxiliary straight lines—erecting :math:`BC \perp AB` of length :math:`AB/2`, joining hypotenuse :math:`AC`, and transferring :math:`AC - BC` onto :math:`AB` (:math:`6R_1 + 3R_2 + 9C_1 + 7C_3, S = 25, E = 15`).

Lemoine eliminates **two of the three straight lines**! Sweeping equal-radius arcs from :g:`A` and :g:`B` traces the **single straight line** :g:`MC`—the perpendicular bisector of :g:`AB`, simultaneously giving midpoint :g:`M` (:math:`MB = AB/2`) and the right angle at :g:`M`. Laying off :math:`MC = AB` along that perpendicular produces right triangle :math:`\triangle BMC` with legs :math:`AB/2` and :math:`AB`, so the un-drawn distance :g:`BC` equals :math:`\frac{\sqrt{5}}{2}\,AB`! Sweeping circle :math:`B(C)` cuts the carrier line beyond :g:`A` at :g:`E`, so segment :math:`ME = BC - MB = \frac{\sqrt{5}-1}{2}\,AB = AB/\phi`, and arc :g:`A(ME)` marks the golden point :g:`X` (:g:`AX` :math:`= AB/\phi`):

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 9C_1 + 6C_3\right), \qquad S = 18, \quad E = 11 \quad (1\text{ line}, 6\text{ circles}).

.. picture:: /_static/figures/fig_golden_section_lemoine.svg

.. _lemoine-en-projective-inversive:

.. folio:: Problèmes XXXVIII–XLVII
   :page: 29

§ 3. Inversion (XXXVIII), Polarity (XXXIX), Radical Axis (XLI) & Harmonic Conjugate (XLVI)
------------------------------------------------------------------------------------------

Problems XXXVIII–XLVI reveal that *Géométrographie* naturally discovers **minimal-instrument constructions** whenever compass-only or straightedge-only syntheses beat mixed methods:

* **Problem XXXVIII (:term:`Circle Inversion <inversion>` — Compass Alone, :math:`5C_1 + 3C_3, S = 8`)**: For a point :math:`A` with :math:`OA > R/2`, sweep :math:`A(O)` (:math:`2C_1 + C_3`) cutting :math:`O(R)` at :math:`M, N`; since :math:`MO = NO = R`, sweeping :math:`M(O)` and :math:`N(O)` adds only :math:`3C_1 + 2C_3`. In total, **zero lines and three circles** (:math:`5C_1 + 3C_3, S = 8, E = 5`) locate :math:`A'` with :math:`OA \cdot OA' = R^2`—the exact lemma by which :person:`August Adler <adler>` (:cite:`adler-1890`) proved :person:`Mascheroni <mascheroni>`'s theorem!
* **Problem XXXIX (:term:`Polar of a Point <polaire>` — Straightedge Alone, :math:`12R_1 + 7R_2, S = 19`)**: Drawing two secants through :g:`A` cutting circle :math:`O` in four vertices of an inscribed complete quadrangle and joining diagonal intersections constructs the polar :g:`TT'` in **seven lines and zero circles** (:math:`S = 19, E = 12`, beating metric ruler-and-compass :math:`S = 25`), identically to :person:`Steiner <steiner>`'s § 10 (:cite:`steiner-1833`).
* **Problem XLI (:term:`Radical Axis <linie-der-gleichen-potenzen>` of Two Non-Intersecting Circles — :math:`S = 17` vs. Mannheim's :math:`S = 58`)**: Answering :person:`Amédée Mannheim <mannheim>` (pp. 57–58), Lemoine contrasts Mannheim's common-tangent midpoint construction (:math:`18R_1 + 9R_2 + 19C_1 + 12C_3, S = 58`) with sweeping **two completely arbitrary secant circles** (:math:`2C_3`, :math:`0` alignment cost!) cutting both given circles and joining chord pairs to two radical centers (:math:`10R_1 + 5R_2 + 2C_3, S = 17, E = 10`).
* **Problem XLVI (:term:`Harmonic Conjugate <conjugue-harmonique>` — Straightedge Alone, :math:`9R_1 + 6R_2, S = 15`)**: Following :person:`Pappus <pappus>` (*Synagoge* Book VII, :cite:`pappus-synagoge`), the complete quadrilateral constructs :math:`D` with :math:`(A, B; C, D) = -1` in 6 lines and 0 circles (:math:`9R_1 + 6R_2, S = 15, E = 9`).
* **Problem XLVII (:person:`Eugène Catalan <catalan>`'s Square on :math:`AB`, :math:`S = 19`)**: Constructs vertices :math:`C, D` in :math:`2R_1 + R_2 + 6C_1 + 4C_3` (:math:`S = 13`) and the full square in :math:`6R_1 + 3R_2 + 6C_1 + 4C_3` (:math:`S = 19` vs. classical :math:`S = 21`).

.. _lemoine-en-triangle-centers:

.. folio:: Problèmes L–LXIII
   :page: 42

§ 4. Modern Triangle Geometry: From :math:`X(2)` and Lemoine's :math:`X(6)` to Brocard and Nagel
------------------------------------------------------------------------------------------------

As co-founder of modern triangle geometry (:cite:`lemoine-1873`, :cite:`altshiller-court-1952`; cross-referenced to :person:`Clark Kimberling <kimberling>`'s *ETC* (:cite:`kimberling-etc`) in :external+etc:doc:`index`), :person:`Lemoine <lemoine>` culminates his treatise by benchmarking the remarkable points of triangle :g:`ABC`:

* **Problem L — Centroid :g:`G` :math:`= X(2)` (:math:`S = 17`)**: Sweeping :math:`B(AC)` and :math:`C(AB)` forms parallelogram :math:`ABDC` whose diagonal :math:`AD` bisects :g:`BC` at :math:`M_a` without tracing a mediatrix; intersecting two medians gives :math:`6R_1 + 3R_2 + 6C_1 + 2C_3` (:math:`S = 17`, 2 circles vs. classical 3 circles, :math:`S = 18`).
* **Problem LI — :term:`Lemoine Symmedian Point <point-de-lemoine>` :g:`K` :math:`= X(6)` (:math:`S = 27` vs. :math:`S = 54`)**: Constructing :math:`K = (a : b : c)` via general trilinear coordinates (Problem XLIX) costs :math:`S = 54`. Lemoine halves the cost by constructing an :term:`antiparallel <antiparallele>` :g:`PaQa` to :g:`BC` and bisecting it by symmetric arcs so **only the two symmedian lines** :g:`AK` and :g:`BK` are ever drawn:

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 13C_1 + 8C_3\right), \qquad S = 27, \quad E = 17 \quad (2\text{ lines}, 8\text{ circles}).

.. picture:: /_static/figures/fig_lemoine_symmedian_x6.svg

* **Problems LII–LIII — :term:`Lemoine Line <droite-de-lemoine>` (:math:`S = 19`) & Simultaneous :math:`(G, K)` (:math:`S = 32`)**: Trilinear polar of :math:`X(6)` in :math:`6R_1 + 3R_2 + 6C_1 + 4C_3` (:math:`S = 19`); joint construction of :math:`X(2)` and :math:`X(6)` in :math:`12R_1 + 6R_2 + 9C_1 + 5C_3` (:math:`S = 32`).
* **Problems LIV–LV — :term:`Brocard Points <points-de-brocard>` :math:`\omega, \omega'` (:math:`S = 28` and :math:`S = 38` vs. Brocard's :math:`S = 74`)**: Single Brocard point in :math:`8R_1 + 4R_2 + 10C_1 + 6C_3` (:math:`S = 28`); both :math:`\omega` and :math:`\omega'` simultaneously in :math:`12R_1 + 6R_2 + 12C_1 + 8C_3` (:math:`S = 38`), cutting :person:`Henri Brocard <brocard>`'s own letter construction (:math:`22R_1 + 11R_2 + 24C_1 + 17C_3, S = 74`, pp. 58–59) nearly in half!
* **Problems LVI–LXIII — Steiner :math:`X(99)` (:math:`S = 24`), Tarry :math:`X(98)` (:math:`S = 28`), Gergonne :math:`X(7)` (:math:`S = 27`), Spieker :math:`X(10)` (:math:`S = 29`), Nagel :math:`X(8)` (:math:`S = 16`), Neuberg :math:`\Phi` (:math:`S = 37`), and Point :math:`W` (:math:`S = 148 \to 62`)**: Notably, :person:`Nagel <nagel>`'s point :math:`X(8)` requires only :math:`4R_1 + 2R_2 + 7C_1 + 3C_3` (:math:`S = 16, E = 11`, 2 lines, 3 circles) by direct semiperimeter transfer without constructing excircles!
