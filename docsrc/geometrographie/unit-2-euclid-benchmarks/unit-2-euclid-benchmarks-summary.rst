:layout: book

.. _geometrographie-unit-2-summary:

Unit II Summary: Euclid Book I Benchmarks Optimized
===================================================

.. rubric:: Comparative Operation Matrix for Problems XI–XXIV

1. Benchmark Table (Euclid Book I vs. Lemoine *Géométrographie*)
----------------------------------------------------------------

.. list-table:: Elementary Book I Problems: Speculative vs. *Géométrographique* Cost
   :header-rows: 1
   :widths: 10 30 12 20 20 8

   * - Prob.
     - Construction
     - Euclid
     - Speculative (:math:`S, E`)
     - Lemoine (:math:`S, E`)
     - Saved
   * - **XI**
     - Copy given angle at given point
     - I.23
     - :math:`4R_1+2R_2+8C_1+C_2+4C_3` (:math:`19, 13`)
     - :math:`2R_1+R_2+5C_1+3C_3` (:math:`11, 7`)
     - :math:`-8`
   * - **XVI**
     - Triangle from three sides :math:`a, b, c`
     - I.22
     - :math:`6R_1+3R_2+9C_1+C_2+3C_3` (:math:`22, 16`)
     - :math:`4R_1+3R_2+8C_1+C_2+3C_3` (:math:`19, 13`)
     - :math:`-3`
   * - **XVII**
     - Parallel through external point :math:`A`
     - I.31
     - :math:`2R_1+R_2+5C_1+3C_3` (:math:`11, 7`)
     - :math:`2R_1+R_2+3C_1+3C_3` (:math:`9, 5`)
     - :math:`-2`
   * - **XVIII**
     - Perpendicular bisector & midpoint
     - I.10
     - :math:`2R_1+R_2+3C_1+2C_3` (:math:`8, 5`)
     - :math:`2R_1+R_2+2C_1+2C_3` (:math:`7, 4`)
     - :math:`-1`
   * - **XVIII bis**
     - Symmetric reflection across line
     - I.12 cor.
     - :math:`4R_1+2R_2+5C_1+C_2+3C_3` (:math:`15, 10`)
     - :math:`2C_1+2C_2+2C_3` (:math:`6, 4`)
     - :math:`-9`
   * - **XIX**
     - Circle on diameter :math:`AB`
     - I.10+Post.3
     - :math:`2R_1+R_2+5C_1+3C_3` (:math:`11, 7`)
     - :math:`2R_1+R_2+4C_1+3C_3` (:math:`10, 6`)
     - :math:`-1`
   * - **XX.1**
     - Perpendicular from external point
     - I.12
     - :math:`2R_1+R_2+3C_1+C_2+3C_3` (:math:`10, 6`)
     - :math:`2R_1+R_2+3C_1+C_2+2C_3` (:math:`9, 6`)
     - :math:`-1`
   * - **XX.2**
     - Perpendicular at point on line
     - I.11 / III.31
     - :math:`2R_1+R_2+3C_1+3C_3` (:math:`9, 5`)
     - :math:`4R_1+2R_2+C_1+C_3` (:math:`8, 5`)
     - :math:`-1`
   * - **XXII**
     - Angle bisector
     - I.9
     - :math:`2R_1+R_2+4C_1+3C_3` (:math:`10, 6`)
     - :math:`2R_1+R_2+3C_1+3C_3` (:math:`9, 5`)
     - :math:`-1`

2. Four Core Optimization Techniques Introduced in Unit II
----------------------------------------------------------

1. **Unconstrained Initial Carrier (:math:`R_2` vs. :math:`2R_1 + R_2`)**: When constructing a figure congruent to given magnitudes (Problem XVI), start from a free line :math:`R_2` rather than placing two points first.
2. **Aperture Persistence Across Operations**: Retain an arbitrary sufficient radius across symmetric steps (Problems XVII, XVIII, XXII), eliminating redundant :math:`C_1` measurements.
3. **Eliminating Un-Needed Auxiliary Lines (Reflection Lemma XVIII *bis*)**: Reflect points across lines by two intersecting circles alone (:math:`0` lines, :math:`S = 6`), turning reflection into a zero-straightedge macro reused throughout Unit III.
4. **Replacing Symmetric Compass Stepping by Thales Diameter Incidence (XX.2)**: Trade three circles and one line (:math:`S = 9`) for **one single circle** and two lines (:math:`4R_1 + 2R_2 + C_1 + C_3, S = 8`).
