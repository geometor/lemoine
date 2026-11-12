:layout: book

.. _geometrographie-unit-4-en:

Unit IV: Restricted & Alternative Instruments — *Équerre*, Mascheroni Compass-Only & Poncelet–Steiner Fixed-Circle
==================================================================================================================

.. rubric:: Émile Lemoine (*Scientia* No. 18, 1902, pp. 55–88) · Lorenzo Mascheroni (1797) · Jakob Steiner (1833)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _lemoine-en-equerre:

.. folio:: L'Équerre
   :page: 55

§ 1. *Géométrographie de l'équerre* (Draftsman's Set-Square)
------------------------------------------------------------

Already in his Oran communication of 30 March 1888 (:cite:`lemoine-1888`, p. 9; recalled on p. 55 of :cite:`lemoine-1892` and expanded in *Scientia* No. 18, :cite:`lemoine-1902`), :person:`Émile Lemoine <lemoine>` observed that practical geometers and engineers continually replace multi-circle parallel and perpendicular constructions with the :term:`équerre <equerre>` (draftsman's right-angled set-square) sliding against a straightedge. Extending *Géométrographie* to the set-square introduces dedicated alignment and sliding primitives:

* Placing one edge of the *équerre* along a traced line (or against the guiding ruler) and sliding the ruler-guided set-square until an edge passes through a given point :math:`A` reduces **Problem XVII (Parallel through :math:`A` to :math:`BC`)** and **Problem XX (Perpendicular through :math:`A` to :math:`BC`)** from nine ruler-and-compass operations (and 2–3 circles) to a pure linear translation without a single compass arc!
* Conversely, because the *équerre* introduces sliding contact between two rigid edges, Lemoine carefully separates its operational ledger from pure Euclidean ruler-and-compass symbols so that constructions are compared only within identical instrument postulates.

.. _lemoine-en-mascheroni:

.. folio:: Géométrographie Mascheronienne
   :page: 66

§ 2. *Géométrographie Mascheronienne*: Compass Alone (*La Geometria del Compasso*, 1797)
----------------------------------------------------------------------------------------

When the straightedge is banished altogether (:math:`l_1 = l_2 = 0`), every construction reduces to a pure compass symbol:

.. math::

   \mathrm{Op.}_{\text{Masch.}} : \left(m_1 C_1 + m_2 C_2 + m_3 C_3\right), \qquad S = m_1 + m_2 + m_3, \quad E = m_1 + m_2, \quad N_{\text{lines}} = 0.

Unknown to eighteenth-century Europe, :person:`Georg Mohr <mohr>` had proved compass-only Euclidean completeness in *Euclides Danicus* (:cite:`mohr-1672`). Independently in Pavia in 1797, :person:`Lorenzo Mascheroni <mascheroni>` published *La Geometria del Compasso* (:cite:`mascheroni-1797`; French translation by :person:`Antoine-Michel Carette <carette>`, :cite:`carette-1798`), dedicated to :person:`Napoléon Bonaparte <bonaparte>`. Because no continuous straight line can be drawn without a ruler, Mascheroni represents every straight line implicitly by **two distinct points** :math:`(A, B)` and proves across twelve books that every point constructible with ruler and compass is constructible by intersecting circular arcs alone:

1. **Collinear Doubling & Multiplication (Libro III, § 64)**: Stepping three chords of radius :math:`AB` around semicircle :math:`B(BA)` from :math:`A` produces :math:`E` collinear with :math:`A, B` such that :math:`AE = 2\,AB` in :math:`5C_1 + 4C_3` (:math:`S = 9`, 4 circles).
2. **Bisecting an Un-Drawn Segment (Libro III, § 66, Sol. V)**: Having doubled :math:`AB` to :math:`E`, sweep :math:`E(EB)` cutting :math:`B(BA)` at :math:`P, p`; then :math:`P(PB)` and :math:`p(PB)` intersect at the exact midpoint :math:`M` of :math:`AB` in **7 circles**: :math:`10C_1 + 7C_3` (:math:`S = 17, E = 10`).
3. **Reflection, Perpendicular & Parallel Point (Libro IV, §§ 76–80)**: Reflecting :math:`A` across :math:`(B, C)` takes :math:`4C_1 + 2C_3` (:math:`S = 6`); constructing :math:`D` so :math:`(C, D) \parallel (A, B)` via :g:`B(AC)` and :g:`C(AB)` takes :math:`5C_1 + 2C_3` (:math:`S = 7, E = 5`).
4. **Concentric Fourth Proportional (Libro V, § 93)**: Highlighted by :person:`Gaetano Fazzari <fazzari>` (:cite:`fazzari-1901`, p. xi) as *simpler in Lemoine's Géométrographie than standard ruler-and-compass Thales constructions*: draw concentric circles :math:`O(a)` and :math:`O(b)`, place chord :math:`BC = c` in :math:`O(a)`, and step equal arcs :math:`BD = CE` onto :math:`O(b)`; then chord :math:`DE = bc/a` in just 4 circles (:math:`S = 14` when :math:`c \le 2a`)!
5. **Circle Inversion & Compass Completeness (Libro V, § 86; Libro VII, §§ 110–112)**: Intersecting a circle with a point-pair line (§§ 110–111, by reflecting the center across :math:`AB`) and intersecting two point-pair lines :math:`AB \cap CD` (§ 112, via symmetric reflections :math:`c, d` and fourth proportional) complete Euclidean geometry. In 1890, :person:`August Adler <adler>` (:cite:`adler-1890`) unified all of Libro VII into a single conceptual stroke: Lemoine's Problem XXXVIII (:math:`5C_1 + 3C_3` compass-only inversion) maps lines not through :math:`O` into circles through :math:`O`, reducing line–line and line–circle intersections directly to circle–circle intersections!

.. picture:: /_static/figures/fig_mascheroni_steiner_duality.svg

.. _lemoine-en-steiner:

.. folio:: Géométrographie Steinerienne
   :page: 74

§ 3. *Géométrographie Steinerienne*: Straightedge Alone with One Fixed Circle (*Die geometrischen Constructionen*, 1833)
------------------------------------------------------------------------------------------------------------------------

At the opposite pole, banishing the compass (:math:`m_1 = m_2 = m_3 = 0`) leaves pure straightedge operations:

.. math::

   \mathrm{Op.}_{\text{Steiner}} : \left(l_1 R_1 + l_2 R_2\right), \qquad S = l_1 + l_2, \quad E = l_1, \quad N_{\text{circles}} = 0.

By projective invariance, a straightedge alone *cannot* bisect a segment, draw a parallel, or solve quadratic metric equations—because non-affine projective collineations preserve straight lines while moving the line at infinity and the circular points. In 1822 :person:`Jean-Victor Poncelet <poncelet>` (:cite:`poncelet-1822`) announced, and in 1833 :person:`Jakob Steiner <steiner>` (:cite:`steiner-1833`) constructively proved across **eight fundamental problems** (*Drittes Kapitel*, § 18, ``[68]``–``[85]``), that **one single permanently drawn circle** :g:`Omega` **together with its given center** :math:`M` (:term:`fester Hülfskreis <fester-huelfskreis>`) restores the entire power of the compass:

1. **Erste Aufgabe (Parallel Line, ``[68]``–``[71]``)**: Any line through center :math:`M` cuts :g:`Omega` in a diameter :g:`ab` bisected at :math:`M`. Joining :math:`a, M, b` to an auxiliary vertex :math:`S` and completing the quadrangle through :math:`P` constructs the parallel :g:`PQ_par` in :math:`11R_1 + 6R_2` (:math:`S = 17, E = 11`, 6 lines, 0 circles); for an arbitrary line not through :math:`M`, two secant chords through :math:`M` first supply a parallel diameter.
2. **Zweite Aufgabe (Segment Multiplication & Harmonic Bisection, ``[71]``)**: Once a parallel line is drawn, complete-quadrangle diagonals bisect or multiply any segment :math:`AB` by straightedge alone.
3. **Dritte Aufgabe (Perpendicular Line, ``[71]``–``[75]``)**: Inscribed angles on diameter :math:`ab` supply right-angle chords in :g:`Omega` (orthocenter construction in :math:`10R_1 + 5R_2, S = 15`), transferred to any point by Problem 1.
4. **Vierte & Fünfte Aufgabe (Copying & Bisecting Angles, ``[75]``–``[76]``)**: Drawing diameters of :g:`Omega` parallel to the arms of any angle transports the angle to center :math:`M`, where parallel chords copy it (Problem 4) and the parallel to chord :math:`ad` bisects it (Problem 5)!
5. **Sechste Aufgabe (Segment Transfer, ``[76]``–``[78]``)**: Given a segment :math:`M_1 a_1` (defining a *virtual* un-drawn circle centered at :math:`M_1`), parallel radii in :g:`Omega` and :math:`M_1` determine their :term:`external and internal centers of similitude <aehnlichkeitspunkte>` :math:`A, I`, transferring length :math:`M_1 a_1` to any new origin :math:`M_2` in any direction!
6. **Siebente & Achte Aufgabe (Intersecting a Line with a Virtual Circle & Two Virtual Circles, ``[78]``–``[85]``)**: Homothetic projection through a center of similitude maps any secant line of un-drawn circle :math:`(M_1, r_1)` onto a secant of the **drawn** fixed circle :g:`Omega` (Problem 7); finally, constructing the :term:`radical axis (Linie der gleichen Potenzen) <linie-der-gleichen-potenzen>` of two un-drawn circles :math:`(M_1, r_1)` and :math:`(M_2, r_2)` via auxiliary homothetic chords reduces circle–circle intersection to Problem 7 (Problem 8)!

**Why Center :math:`M` Cannot Be Omitted**: If circle :g:`Omega` is given *without* its center :math:`M`, any hyperbolic projective transformation (Möbius/Klein automorphic collineation of the disk interior) maps :g:`Omega` onto itself and straight lines onto straight lines, yet moves the Euclidean center :math:`M` to another interior point—proving that :math:`M` itself cannot be found by straightedge alone from a single circle!
