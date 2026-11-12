:layout: book

.. _geometrographie-unit-4-summary:

Unit IV Summary: The Three Restricted-Instrument Regimes
========================================================

.. rubric:: Comparative Architecture of Ruler+Compass, Set-Square, Mascheroni, and Poncelet–Steiner

1. Instrument Regimes & Allowed Operation Subspaces
---------------------------------------------------

.. list-table:: Constructibility & Operation Subspaces Across Classical and Minimal Instruments
   :header-rows: 1
   :widths: 22 24 26 28

   * - Regime
     - Primary Source
     - Operation Symbol
     - Algebraic Field & Invariance
   * - **Canonical Ruler + Compass**
     - :cite:`lemoine-1892`, :cite:`lemoine-1902`
     - :math:`l_1 R_1 + l_2 R_2 + m_1 C_1 + m_2 C_2 + m_3 C_3`
     - Full Euclidean quadratic tower (:math:`\sqrt{x^2 \pm y^2}`)
   * - **Ruler + Équerre (Set-Square)**
     - :cite:`lemoine-1888`, :cite:`lemoine-1902`
     - :math:`R_1, R_2 + E_1, E_2` (sliding right angle)
     - Affine + orthogonal projections (pythagorean field when segment transfer added)
   * - **Mascheroni Compass Alone**
     - :cite:`mohr-1672`, :cite:`mascheroni-1797`
     - :math:`m_1 C_1 + m_2 C_2 + m_3 C_3` (:math:`l_1 = l_2 = 0`)
     - Full Euclidean quadratic tower (lines implicit as point-pairs :math:`(A, B)`)
   * - **Poncelet–Steiner Straightedge + Fixed Circle :math:`M`**
     - :cite:`poncelet-1822`, :cite:`steiner-1833`
     - :math:`l_1 R_1 + l_2 R_2` (:math:`m_1 = m_2 = m_3 = 0`)
     - Full Euclidean quadratic tower (circles implicit as center + radius endpoint)
   * - **Hilbert Straightedge + Eichmaß (Unit Gauge)**
     - :cite:`hilbert-1899` (§§ 36–39)
     - :math:`R_1, R_2` + unit-segment transferrer
     - Strictly *pythagorean* subfield (:math:`\sqrt{1 + \omega^2}`, smaller than Euclidean!)

2. Steiner's Eight Fundamental Problems (*Drittes Kapitel*, § 18, ``[68]``–``[85]``)
------------------------------------------------------------------------------------

1. **Erste Aufgabe** (``[68]``–``[71]``): Parallel through external point to a diameter (:math:`11R_1 + 6R_2, S = 17`) or general line.
2. **Zweite Aufgabe** (``[71]``): Harmonic bisection and rational multiplication/:math:`n`-section of a segment.
3. **Dritte Aufgabe** (``[71]``–``[75]``): Perpendicular to a line (orthocenter on fixed-circle diameter: :math:`10R_1 + 5R_2, S = 15`).
4. **Vierte Aufgabe** (``[75]``): Copying a given angle to a given vertex and ray via parallel diameters of :math:`M`.
5. **Fünfte Aufgabe** (``[75]``–``[76]``): Bisecting a given angle via parallel diameters and subtended chord.
6. **Sechste Aufgabe** (``[76]``–``[78]``): Transferring a given segment to a given point along a given ray via centers of similitude :math:`A, I`.
7. **Siebente Aufgabe** (``[78]``–``[82]``): Intersecting a given line with an un-drawn circle :math:`(M_1, r_1)` via homothetic secant on fixed circle :math:`M`.
8. **Achte Aufgabe** (``[82]``–``[85]``): Intersecting two un-drawn circles :math:`(M_1, r_1)` and :math:`(M_2, r_2)` via their radical axis (*Linie der gleichen Potenzen*) reduced to Problem 7.
