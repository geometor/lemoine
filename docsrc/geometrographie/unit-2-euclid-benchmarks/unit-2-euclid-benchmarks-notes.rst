:layout: book

.. _geometrographie-unit-2-notes:

Unit II Commentary & Notes: Euclid, Mascheroni, and Steiner on Book I Primitives
================================================================================

.. rubric:: Minimal-Instrument Counterparts & Deductive Order vs. Constructive Economy

1. Why Euclid Could Not Use Thales's Circle (:math:`S = 8`) in Proposition I.11
-------------------------------------------------------------------------------

In Problem XX.2, :person:`Lemoine <lemoine>` erects the perpendicular at :math:`A \in BC` in a single circle (:math:`4R_1 + 2R_2 + C_1 + C_3, S = 8`) via Thales's semicircle theorem (:person:`Euclid <euclid>`, *Elements* III.31). Why did Euclid instead use three circles (:math:`S = 9` or :math:`10`) in Proposition I.11?

Because **Euclid III.31 depends deductively on the parallel postulate (I.29, I.32: angle sum of a triangle equals two right angles)!** In *absolute* (neutral) geometry—the first twenty-eight propositions of Book I, valid identically in Euclidean and Bolyai–Lobachevsky hyperbolic planes—the angle inscribed in a semicircle is strictly less than a right angle in hyperbolic space! Euclid's three-circle equilateral construction in I.11 holds in absolute geometry without the parallel postulate, whereas Lemoine's :math:`S = 8` Thales construction exploits Euclidean flatness to save two circles and one operation.

2. Dual Minimal-Instrument Comparison on the Parallel (XVII) and Perpendicular (XX)
-----------------------------------------------------------------------------------

Comparing Lemoine's Book I benchmarks with :person:`Mascheroni <mascheroni>` (:cite:`mascheroni-1797`) and :person:`Steiner <steiner>` (:cite:`steiner-1833`) reveals an extraordinary structural symmetry (see :ref:`concordance-parallel-external` and :ref:`concordance-perpendicular-external`):

* **Parallel Through an External Point**:
  * **Lemoine / Tarry Rhombus (Ruler + Compass)**: :math:`2R_1 + R_2 + 3C_1 + 3C_3` (:math:`S = 9, E = 5`).
  * **Mascheroni Libro IV, § 80 (Compass Alone)**: Given :math:`A, B` on the line and external point :math:`C`, sweep :math:`B(AC)` (:math:`3C_1 + C_3`) and :math:`C(AB)` (:math:`2C_1 + C_3` if :math:`AB` was spanned first) meeting at :math:`D`. Point :math:`D` completes parallelogram :math:`ABCD` so pair :math:`(C, D)` represents the parallel in :math:`5C_1 + 2C_3` (:math:`S = 7, E = 5`, **zero lines**!). Notice that Tarry's rhombus (:math:`S = 9`) is simply Mascheroni's parallelogram specialized to equal sides :math:`R` plus the final straightedge join :math:`2R_1 + R_2`!
  * **Steiner § 18, Erste Aufgabe (Straightedge + Fixed Circle :math:`M`)**: When the given line passes through the center :math:`M` of the fixed circle, cutting it at diameter endpoints :math:`a, b`, M is the known midpoint of :math:`ab`. A complete quadrangle over :math:`a, M, b` constructs the harmonic conjugate of the point at infinity—hence the parallel through :math:`P`—in :math:`11R_1 + 6R_2` (:math:`S = 17, E = 11`, **zero circles**).

* **Perpendicular From an External Point**:
  * **Lemoine XX.1 (Ruler + Compass)**: :math:`2R_1 + R_2 + 3C_1 + C_2 + 2C_3` (:math:`S = 9`, 1 line, 2 circles).
  * **Mascheroni Libro IV, § 78 (Compass Alone)**: Reflect :math:`A` across :math:`B, C` to :math:`A'` in :math:`4C_1 + 2C_3` (:math:`S = 6`, 0 lines, 2 circles), determining the perpendicular line implicitly as :math:`(A, A')`!
  * **Steiner § 18, Dritte Aufgabe (Straightedge + Fixed Circle :math:`M`)**: Join external :math:`P` to diameter endpoints :math:`a, b` cutting the fixed circle again at :math:`c, d`; by Thales's theorem :math:`ad \perp Pb` and :math:`bc \perp Pa`, so :math:`H = ad \cap bc` is the orthocenter of :math:`\triangle Pab`, and line :math:`PH` is perpendicular to :math:`ab` in :math:`10R_1 + 5R_2` (:math:`S = 15`, 5 lines, 0 circles)!
