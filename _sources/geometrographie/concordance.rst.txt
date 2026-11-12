:layout: book

.. _concordance:

Dual Minimal-Instrument Concordance
===================================

.. rubric:: *Géométrographie* (1902) · *Euclid's Elements* · *Mascheroni Compass-Only* (1797) · *Poncelet–Steiner Fixed-Circle* (1833)

This concordance synthesizes :person:`Émile Lemoine <lemoine>`'s quantitative
:term:`Géométrographie <geometrographie>` (:cite:`lemoine-1902`) with
:person:`Euclid <euclid>`'s axiomatic canon (:cite:`euclid-heath`),
:person:`Lorenzo Mascheroni <mascheroni>`'s compass-only constructions
(:cite:`mascheroni-1797`, :cite:`fazzari-1901`), and :person:`Jakob Steiner <steiner>`'s
straightedge-only constructions with a single fixed circle and its center (:cite:`steiner-1833`).
Every operation vector satisfies Lemoine's exact identities:

.. math::

   \mathrm{Op.} : (l_1 R_1 + l_2 R_2 + m_1 C_1 + m_2 C_2 + m_3 C_3), \qquad
   S = l_1 + l_2 + m_1 + m_2 + m_3, \qquad
   E = l_1 + m_1 + m_2.

Master Operation-Count Summary
------------------------------

.. list-table:: Classical vs. *Géométrographique* Simplicity & Exactitude
   :header-rows: 1
   :widths: 10 28 12 20 20 10

   * - Prob.
     - Benchmark Construction
     - Euclid / ETC
     - Classical Symbol (:math:`S, E`)
     - Lemoine Symbol (:math:`S, E`)
     - :math:`\Delta S`
   * - ``III``
     - :ref:`Straight Line Joining Two Given Points <concordance-line-two-points>`
     - I.Post.1
     - :math:`2R_1 + R_2` (:math:`S=3, E=2`)
     - :math:`2R_1 + R_2` (:math:`S=3, E=2`)
     - ``0``
   * - ``VIII``
     - :ref:`Laying Off a Given Segment Along a Traced Line <concordance-transfer-segment>`
     - I.2, I.3
     - :math:`4R_1 + 2R_2 + 5C_1 + 5C_3` (:math:`S=16, E=9`)
     - :math:`2C_1 + C_2 + C_3` (:math:`S=4, E=3`)
     - ``+12``
   * - ``XI``
     - :ref:`Constructing at a Given Point an Angle Equal to a Given Angle <concordance-copy-angle>`
     - I.23
     - :math:`4R_1 + 2R_2 + 8C_1 + C_2 + 4C_3` (:math:`S=19, E=13`)
     - :math:`2R_1 + R_2 + 5C_1 + 3C_3` (:math:`S=11, E=7`)
     - ``+8``
   * - ``XVI``
     - :ref:`Triangle from Three Given Sides <concordance-triangle-sss>`
     - I.22
     - :math:`6R_1 + 3R_2 + 9C_1 + C_2 + 3C_3` (:math:`S=22, E=16`)
     - :math:`4R_1 + 3R_2 + 8C_1 + C_2 + 3C_3` (:math:`S=19, E=13`)
     - ``+3``
   * - ``XVII``
     - :ref:`Parallel Through an External Point to a Given Line <concordance-parallel-external>`
     - I.31
     - :math:`2R_1 + R_2 + 5C_1 + 3C_3` (:math:`S=11, E=7`)
     - :math:`2R_1 + R_2 + 3C_1 + 3C_3` (:math:`S=9, E=5`)
     - ``+2``
   * - ``XVIII``
     - :ref:`Perpendicular Bisector and Midpoint of a Segment <concordance-perpendicular-bisector>`
     - I.10
     - :math:`2R_1 + R_2 + 3C_1 + 2C_3` (:math:`S=8, E=5`)
     - :math:`2R_1 + R_2 + 2C_1 + 2C_3` (:math:`S=7, E=4`)
     - ``+1``
   * - ``XVIII bis``
     - :ref:`Symmetric Reflection of a Point Across a Traced Line <concordance-point-reflection>`
     - I.12 (cor.)
     - :math:`4R_1 + 2R_2 + 5C_1 + C_2 + 3C_3` (:math:`S=15, E=10`)
     - :math:`2C_1 + 2C_2 + 2C_3` (:math:`S=6, E=4`)
     - ``+9``
   * - ``XX.1``
     - :ref:`Perpendicular to a Traced Line from an External Point <concordance-perpendicular-external>`
     - I.12
     - :math:`2R_1 + R_2 + 3C_1 + C_2 + 3C_3` (:math:`S=10, E=6`)
     - :math:`2R_1 + R_2 + 3C_1 + C_2 + 2C_3` (:math:`S=9, E=6`)
     - ``+1``
   * - ``XX.2``
     - :ref:`Perpendicular Erected at a Given Point on a Traced Line <concordance-perpendicular-on-line>`
     - I.11, III.31
     - :math:`2R_1 + R_2 + 3C_1 + 3C_3` (:math:`S=9, E=5`)
     - :math:`4R_1 + 2R_2 + C_1 + C_3` (:math:`S=8, E=5`)
     - ``+1``
   * - ``XXII``
     - :ref:`Bisecting a Given Rectilinear Angle <concordance-angle-bisector>`
     - I.9
     - :math:`2R_1 + R_2 + 4C_1 + 3C_3` (:math:`S=10, E=6`)
     - :math:`2R_1 + R_2 + 3C_1 + 3C_3` (:math:`S=9, E=5`)
     - ``+1``
   * - ``XXI``
     - :ref:`Circumcircle and Circumcenter X(3) Through Three Given Points <concordance-circumcircle>`
     - IV.5 · X(3) Circumcenter
     - :math:`4R_1 + 2R_2 + 6C_1 + 5C_3` (:math:`S=17, E=10`)
     - :math:`4R_1 + 2R_2 + 5C_1 + 4C_3` (:math:`S=15, E=9`)
     - ``+2``
   * - ``XXVI``
     - :ref:`Tangents to a Given Circle from an External Point <concordance-external-tangents>`
     - III.17
     - :math:`8R_1 + 4R_2 + 4C_1 + 3C_3` (:math:`S=19, E=12`)
     - :math:`5R_1 + 3R_2 + 6C_1 + 4C_3` (:math:`S=18, E=11`)
     - ``+1``
   * - ``XXVII``
     - :ref:`Incircle and Incenter X(1) of a Given Triangle <concordance-incircle-x1>`
     - IV.4 · X(1) Incenter
     - :math:`6R_1 + 3R_2 + 11C_1 + 10C_3` (:math:`S=30, E=17`)
     - :math:`4R_1 + 2R_2 + 11C_1 + 6C_3` (:math:`S=23, E=15`)
     - ``+7``
   * - ``XXXIII``
     - :ref:`Fourth Proportional to Three Given Segments <concordance-fourth-proportional>`
     - VI.12
     - :math:`4R_1 + 3R_2 + 11C_1 + C_2 + 6C_3` (:math:`S=25, E=16`)
     - :math:`2R_1 + 2R_2 + 11C_1 + C_2 + 6C_3` (:math:`S=22, E=14`)
     - ``+3``
   * - ``XXXV``
     - :ref:`Mean Proportional (Geometric Mean) of Two Segments <concordance-mean-proportional>`
     - II.14, VI.13
     - :math:`4R_1 + 3R_2 + 10C_1 + C_2 + 6C_3` (:math:`S=24, E=15`)
     - :math:`2R_1 + 2R_2 + 6C_1 + C_2 + 3C_3` (:math:`S=14, E=9`)
     - ``+10``
   * - ``XXXVI``
     - :ref:`Division in Extreme and Mean Ratio (Golden Section phi) <concordance-golden-section>`
     - II.11, VI.30
     - :math:`6R_1 + 3R_2 + 9C_1 + 7C_3` (:math:`S=25, E=15`)
     - :math:`2R_1 + R_2 + 9C_1 + 6C_3` (:math:`S=18, E=11`)
     - ``+7``
   * - ``XXXVIII``
     - :ref:`Inverse of a Given Point with Respect to a Given Circle <concordance-circle-inversion>`
     - III.36, VI.8
     - :math:`4R_1 + 2R_2 + 4C_1 + 2C_3` (:math:`S=12, E=8`)
     - :math:`5C_1 + 3C_3` (:math:`S=8, E=5`)
     - ``+4``
   * - ``XXXIX``
     - :ref:`Polar Line of a Given Point with Respect to a Traced Circle <concordance-polar-of-point>`
     - III.17, III.36
     - :math:`10R_1 + 5R_2 + 6C_1 + 4C_3` (:math:`S=25, E=16`)
     - :math:`12R_1 + 7R_2` (:math:`S=19, E=12`)
     - ``+6``
   * - ``XLI``
     - :ref:`Radical Axis of Two Non-Intersecting Traced Circles <concordance-radical-axis>`
     - III.35, III.36
     - :math:`18R_1 + 9R_2 + 19C_1 + 12C_3` (:math:`S=58, E=37`)
     - :math:`10R_1 + 5R_2 + 2C_3` (:math:`S=17, E=10`)
     - ``+41``
   * - ``XLVI``
     - :ref:`Harmonic Conjugate of a Point with Respect to a Segment <concordance-harmonic-conjugate>`
     - VI.3 (harmonic angle bisector)
     - :math:`10R_1 + 6R_2 + 4C_1 + 2C_3` (:math:`S=22, E=14`)
     - :math:`9R_1 + 6R_2` (:math:`S=15, E=9`)
     - ``+7``
   * - ``L``
     - :ref:`Centroid G = X(2) of a Given Triangle <concordance-centroid-x2>`
     - I.10, I.34 · X(2) Centroid
     - :math:`8R_1 + 4R_2 + 3C_1 + 3C_3` (:math:`S=18, E=11`)
     - :math:`6R_1 + 3R_2 + 6C_1 + 2C_3` (:math:`S=17, E=12`)
     - ``+1``
   * - ``LI``
     - :ref:`Lemoine Symmedian Point K = X(6) of a Given Triangle <concordance-lemoine-point-x6>`
     - VI.4, III.21–22 · X(6) Symmedian / Lemoine Point
     - :math:`14R_1 + 7R_2 + 21C_1 + 12C_3` (:math:`S=54, E=35`)
     - :math:`4R_1 + 2R_2 + 13C_1 + 8C_3` (:math:`S=27, E=17`)
     - ``+27``
   * - ``LIV–LV``
     - :ref:`First and Second Brocard Points omega and omega' of a Triangle <concordance-brocard-points>`
     - III.21, III.32 · Bicentric Brocard pair (Ω, Ω')
     - :math:`22R_1 + 11R_2 + 24C_1 + 17C_3` (:math:`S=74, E=46`)
     - :math:`12R_1 + 6R_2 + 12C_1 + 8C_3` (:math:`S=38, E=24`)
     - ``+36``
   * - ``LXI``
     - :ref:`Nagel Point X(8) of a Given Triangle <concordance-nagel-point-x8>`
     - IV.4 (excircle touchpoints) · X(8) Nagel Point
     - :math:`6R_1 + 3R_2 + 15C_1 + 10C_3` (:math:`S=34, E=21`)
     - :math:`4R_1 + 2R_2 + 7C_1 + 3C_3` (:math:`S=16, E=11`)
     - ``+18``
   * - ``Masch. §§ 66, 112``
     - :ref:`Mascheroni Compass-Only Midpoint & Intersection of Two Lines <concordance-mascheroni-midpoint-line-intersection>`
     - I.Post.3, I.10
     - :math:`2R_1 + R_2 + 2C_1 + 2C_3` (:math:`S=7, E=4`)
     - :math:`10C_1 + 7C_3` (:math:`S=17, E=10`)
     - ``-10``
   * - ``Steiner § 18 Aufg. 1–8``
     - :ref:`Poncelet–Steiner Straightedge-Only Parallel & Virtual Circle Intersections <concordance-steiner-parallel-circle-meet>`
     - I.Post.1–2, I.31
     - :math:`2R_1 + R_2 + 3C_1 + 3C_3` (:math:`S=9, E=5`)
     - :math:`11R_1 + 6R_2` (:math:`S=17, E=11`)
     - ``-8``

Unit I: Historical Genesis, Methodological Criteria & The Five Elementary Operations
------------------------------------------------------------------------------------

 Companion codex unit: :doc:`Unit I: Historical Genesis, Methodological Criteria & The Five Elementary Operations <unit-1-operations/unit-1-operations-en>`.

.. _concordance-line-two-points:

III — Straight Line Joining Two Given Points
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Tracer la droite joignant deux points donnés A et B*

**Lemoine Folio**: pp. 4 | **Euclid**: I.Post.1 | **Elements DAG**: G.1 (Postulate 1) | **Projective**: Projective incidence join AB

- **Classical / Speculative Construction**: :math:`2R_1 + R_2` — Simplicity :math:`S = 3`, Exactitude :math:`E = 2` (1 lines, 0 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2R_1 + R_2` — Simplicity :math:`S = 3`, Exactitude :math:`E = 2` (1 lines, 0 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro VIII, § 113; Libro VII, §§ 110–112 (pp. 60–63)*): A straight line cannot be continuously traced without a straightedge; Mascheroni represents line AB implicitly by its point-pair (A, B) and constructs collinear multiples (§ 64) or intersections (§ 112) by compass arcs alone.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Einleitung § 1; Drittes Kapitel § 18, II ([68], p. 50)*): Primitive straightedge operation (2R_1 + R_2): joining two given points with the ruler is immediately permitted without consulting the fixed circle M.
- **Critical Note**: Establishes the fundamental ruler cost 2R_1 + R_2 (S = 3, E = 2) against which all straightedge alignments are measured.

.. _concordance-transfer-segment:

VIII — Laying Off a Given Segment Along a Traced Line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Porter sur une droite tracée une longueur donnée AB*

**Lemoine Folio**: pp. 4–5 | **Euclid**: I.2, I.3 | **Elements DAG**: G.3, G.4 (I.2, I.3) | **Projective**: Metric gauge / Hilbert § 36 Streckenübertrager

- **Classical / Speculative Construction**: :math:`4R_1 + 2R_2 + 5C_1 + 5C_3` — Simplicity :math:`S = 16`, Exactitude :math:`E = 9` (2 lines, 5 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2C_1 + C_2 + C_3` — Simplicity :math:`S = 4`, Exactitude :math:`E = 3` (0 lines, 1 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro I, §§ 10–11 (pp. 12–13); Libro IV, §§ 72–74 (pp. 40–42)*): Modern divider-compass transfer (3C_1 + C_3 from a given origin M, or 5-circle reflection/parallelogram when transferring onto an un-drawn line defined by two points).
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Sechste Aufgabe ([76]–[78], pp. 56–57)*): Pure straightedge transfer of segment M_1 a_1 to a given origin M_2 by constructing the centers of similitude A_1, I_1 of the fixed circle M and the virtual circle (M_2, M_1 a_1).
- **Critical Note**: Euclid I.2–I.3 avoids assuming a divider compass that retains its opening when lifted (S = 16); Lemoine's modern compass takes AB in 2C_1 and lays it off in C_2 + C_3 (or C_1 + C_3 from a fixed point, S = 4, E = 3).

Unit II: Fundamental Speculative vs. Géométrographique Constructions (Euclid Book I Benchmarks)
-----------------------------------------------------------------------------------------------

 Companion codex unit: :doc:`Unit II: Fundamental Speculative vs. Géométrographique Constructions (Euclid Book I Benchmarks) <unit-2-euclid-benchmarks/unit-2-euclid-benchmarks-en>`.

.. _concordance-copy-angle:

XI — Constructing at a Given Point an Angle Equal to a Given Angle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire en un point donné d'une droite un angle égal à un angle donné*

**Lemoine Folio**: pp. 6 | **Euclid**: I.23 | **Elements DAG**: G.24 (I.23)

- **Classical / Speculative Construction**: :math:`4R_1 + 2R_2 + 8C_1 + C_2 + 4C_3` — Simplicity :math:`S = 19`, Exactitude :math:`E = 13` (2 lines, 4 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2R_1 + R_2 + 5C_1 + 3C_3` — Simplicity :math:`S = 11`, Exactitude :math:`E = 7` (1 lines, 3 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro VIII, § 114 (pp. 63–64, Fig. 51)*): Given angle ABC by three points and target ray ba, constructs fourth proportionals (§ 93) or equal-radius chord transfer (5C_1 + 3C_3 when radii AB = ab are chosen equal) to locate c.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Vierte Aufgabe ([75], p. 55, Fig. 21)*): Draws diameters ab, cd of the fixed circle M parallel to the sides of angle AmC and ef parallel to EF, transfers the central angle via parallel chords ce and ag, and draws pq parallel to diameter gMh.
- **Critical Note**: Euclid's reduction of I.23 to I.22 joins a speculative auxiliary chord across the given angle; equal-radius arc transfer cuts S from 19 to 11.

.. _concordance-triangle-sss:

XVI — Triangle from Three Given Sides
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire un triangle connaissant les trois côtés a, b, c*

**Lemoine Folio**: pp. 7–8 | **Euclid**: I.22 | **Elements DAG**: G.23 (I.22)

- **Classical / Speculative Construction**: :math:`6R_1 + 3R_2 + 9C_1 + C_2 + 3C_3` — Simplicity :math:`S = 22`, Exactitude :math:`E = 16` (3 lines, 3 circles).
- **Lemoine Géométrographique Synthesis**: :math:`4R_1 + 3R_2 + 8C_1 + C_2 + 3C_3` — Simplicity :math:`S = 19`, Exactitude :math:`E = 13` (3 lines, 3 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro I, § 11 (pp. 12–13); Libro VIII, § 115 (p. 64)*): Once base endpoints B, C are separated by a, two compass arcs of radii b and c (6C_1 + 2C_3) determine the third vertex A directly without tracing the three side lines.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Sechste & Achte Aufgabe ([76]–[85], pp. 56–62)*): Transfers lengths a, b, c via Sixth Problem and intersects the two virtual circles (B, c) and (C, b) via their radical axis (Eighth Problem) using straightedge alone.
- **Critical Note**: Drawing the initial carrier line as an arbitrary line R_2 (rather than joining two pre-placed points) saves 2R_1 + C_1 over textbook execution.

.. _concordance-parallel-external:

XVII — Parallel Through an External Point to a Given Line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Par un point donné A hors d'une droite BC, mener une parallèle à BC*

**Lemoine Folio**: pp. 8–9 | **Euclid**: I.31 | **Elements DAG**: G.32 (I.31) | **Projective**: Harmonic point at infinity

- **Classical / Speculative Construction**: :math:`2R_1 + R_2 + 5C_1 + 3C_3` — Simplicity :math:`S = 11`, Exactitude :math:`E = 7` (1 lines, 3 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2R_1 + R_2 + 3C_1 + 3C_3` — Simplicity :math:`S = 9`, Exactitude :math:`E = 5` (1 lines, 3 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro IV, § 80 (p. 43, Fig. 29)*): Opposite-side parallelogram: with A, B on the given line and external point C, draw B(CA) and C(BA) meeting at D (5C_1 + 2C_3, S = 7, E = 5 for point D alone!).
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Erste Aufgabe ([68]–[71], pp. 50–52, Fig. 19)*): Pure straightedge parallel via a diameter aMb of the fixed circle (providing midpoint M of ab) and complete-quadrangle harmonic construction (11R_1 + 6R_2 when line passes through M).
- **Critical Note**: Gaston Tarry discovered two S = 9 constructions: 1° two equal-radius circles passing through A (2R_1 + R_2 + 4C_1 + 2C_3, E = 6, 2 circles), and 2° single-aperture rhombus (2R_1 + R_2 + 3C_1 + 3C_3, E = 5, 3 circles).

.. _concordance-perpendicular-bisector:

XVIII — Perpendicular Bisector and Midpoint of a Segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Tracer la perpendiculaire au milieu de AB, ou trouver le milieu de AB*

**Lemoine Folio**: pp. 9–10 | **Euclid**: I.10 | **Elements DAG**: G.11 (I.10) | **Projective**: Harmonic conjugate of point at infinity

- **Classical / Speculative Construction**: :math:`2R_1 + R_2 + 3C_1 + 2C_3` — Simplicity :math:`S = 8`, Exactitude :math:`E = 5` (1 lines, 2 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2R_1 + R_2 + 2C_1 + 2C_3` — Simplicity :math:`S = 7`, Exactitude :math:`E = 4` (1 lines, 2 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro III, § 66 Sol. I–V (pp. 32–33, Figs. 14–17); Libro IV, § 79 (p. 43)*): Bisecting AB without a drawn line takes 7 circles in Sol. V (10C_1 + 7C_3, S = 17): double AB to E via 4 unit-radius arcs, draw E(EB) cutting B(BA) at P, p, then P(PB) and p(PB) meet at midpoint M.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Zweite & Dritte Aufgabe ([71]–[75], pp. 52–55)*): Draws a line parallel to AB (First Problem) to bisect AB harmonically via a complete quadrangle (Second Problem, b), then erects the perpendicular via Third Problem.
- **Critical Note**: Keeping an arbitrary compass opening > AB/2 avoids setting the compass on B to measure AB, saving 1 C_1 (S = 7 vs. Euclid's equilateral-triangle S = 8).

.. _concordance-point-reflection:

XVIII bis — Symmetric Reflection of a Point Across a Traced Line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire le symétrique A' d'un point A par rapport à une droite tracée BC*

**Lemoine Folio**: pp. 10 | **Euclid**: I.12 (cor.) | **Elements DAG**: G.13 (reflection lemma) | **Projective**: Orthogonal involution

- **Classical / Speculative Construction**: :math:`4R_1 + 2R_2 + 5C_1 + C_2 + 3C_3` — Simplicity :math:`S = 15`, Exactitude :math:`E = 10` (2 lines, 3 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2C_1 + 2C_2 + 2C_3` — Simplicity :math:`S = 6`, Exactitude :math:`E = 4` (0 lines, 2 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro I, § 14 (p. 14); Libro IV, § 78 (p. 43, Fig. 28)*): Identical two-circle compass-only reflection! When B and C are given points on the mirror line, B(BA) and C(CA) intersect at A' in 4C_1 + 2C_3 (or 3C_1 + 3C_3 if radii share opening), S = 6.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Dritte & Sechste Aufgabe ([71]–[78], pp. 52–57)*): Drops the perpendicular from A to BC meeting BC at foot M (Third Problem), then doubles AM harmonically to A' via a parallel line (Second Problem).
- **Critical Note**: Crucial géométrographique primitive: Lemoine uses compass-only reflection (0 lines, 2 circles, S = 6) inside his symmedian X(6) and tangent constructions.

.. _concordance-perpendicular-external:

XX.1 — Perpendicular to a Traced Line from an External Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Mener par un point extérieur A la perpendiculaire à une droite tracée BC*

**Lemoine Folio**: pp. 11 | **Euclid**: I.12 | **Elements DAG**: G.13 (I.12)

- **Classical / Speculative Construction**: :math:`2R_1 + R_2 + 3C_1 + C_2 + 3C_3` — Simplicity :math:`S = 10`, Exactitude :math:`E = 6` (1 lines, 3 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2R_1 + R_2 + 3C_1 + C_2 + 2C_3` — Simplicity :math:`S = 9`, Exactitude :math:`E = 6` (1 lines, 2 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro IV, § 78 (p. 43, Fig. 28)*): Reflects D across AB to E in 2 arcs B(BD), A(AD) (determining the perpendicular line DE in S = 6!), and if foot M is required, bisects DE by § 66.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Dritte Aufgabe A & B ([71]–[75], pp. 52–55, Fig. 20)*): When BC is a diameter ab of the fixed circle, joins Pa, Pb meeting the circle at c, d; lines ad and bc meet at orthocenter p_1, and Pp_1 is perpendicular to ab (10R_1 + 5R_2, S = 15!).
- **Critical Note**: Instead of drawing a circle centered at A cutting BC twice and then bisecting the chord (3 circles, S = 10), Lemoine reflects A across two centres on BC (2 circles, S = 9).

.. _concordance-perpendicular-on-line:

XX.2 — Perpendicular Erected at a Given Point on a Traced Line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Élever en un point donné A d'une droite BC la perpendiculaire à BC*

**Lemoine Folio**: pp. 11–12 | **Euclid**: I.11, III.31 | **Elements DAG**: G.12 (I.11), G.105 (III.31)

- **Classical / Speculative Construction**: :math:`2R_1 + R_2 + 3C_1 + 3C_3` — Simplicity :math:`S = 9`, Exactitude :math:`E = 5` (1 lines, 3 circles).
- **Lemoine Géométrographique Synthesis**: :math:`4R_1 + 2R_2 + C_1 + C_3` — Simplicity :math:`S = 8`, Exactitude :math:`E = 5` (2 lines, 1 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro IV, §§ 76–77 (pp. 42–43, Figs. 26–27)*): 3-circle Thales semicircle (§ 77): with arbitrary radius r, draw A(r) and B(r) meeting at C, then trace semicircle C(r) stepping two chords from B to D; AD is perpendicular to AB (3C_1 + 5C_3 or 4C_1 + 3C_3 + stepping).
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Dritte Aufgabe A ([71]–[72], pp. 52–53)*): Constructs orthogonal chords in the fixed circle via diameters (Euclid III.31) and draws the parallel through A on BC.
- **Critical Note**: Thales single-circle construction: place compass at an arbitrary point O off BC, draw O(OA) (C_1 + C_3) cutting BC again at B, draw diameter BO cutting O(OA) at D (2R_1 + R_2), and join AD (2R_1 + R_2) — only 1 circle and S = 8!

.. _concordance-angle-bisector:

XXII — Bisecting a Given Rectilinear Angle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Diviser un angle donné BAC en deux parties égales*

**Lemoine Folio**: pp. 13 | **Euclid**: I.9 | **Elements DAG**: G.10 (I.9)

- **Classical / Speculative Construction**: :math:`2R_1 + R_2 + 4C_1 + 3C_3` — Simplicity :math:`S = 10`, Exactitude :math:`E = 6` (1 lines, 3 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2R_1 + R_2 + 3C_1 + 3C_3` — Simplicity :math:`S = 9`, Exactitude :math:`E = 5` (1 lines, 3 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro II, § 60 (p. 29); Libro VIII, § 118 (p. 65)*): Bisects the subtended arc BD of circle A(AB) via Mascheroni's arc-bisection parallelogram (§ 60) using compass arcs alone.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Fünfte Aufgabe, Fall a ([75]–[76], pp. 55–56, Fig. 21)*): Draws diameters ab, cd of fixed circle M parallel to sides mA, mC so central angle aMc = AmC; the line through vertex m parallel to chord ad (or cb) bisects angle AmC!
- **Critical Note**: Retaining the same sufficient radius R for the initial arc at A and the two intersecting arcs from B and D avoids resetting the compass, reducing S from 10 to 9.

Unit III: Circles, Tangency, Golden Section, Projective Polarity & Modern Triangle Centers
------------------------------------------------------------------------------------------

 Companion codex unit: :doc:`Unit III: Circles, Tangency, Golden Section, Projective Polarity & Modern Triangle Centers <unit-3-circles-tangency-golden/unit-3-circles-tangency-golden-en>`.

.. _concordance-circumcircle:

XXI — Circumcircle and Circumcenter X(3) Through Three Given Points
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Circonscrire un cercle à un triangle donné ABC, ou faire passer un cercle par A, B, C*

**Lemoine Folio**: pp. 12–13 | **Euclid**: IV.5 | **Elements DAG**: G.117 (IV.5) | **ETC**: X(3) Circumcenter

- **Classical / Speculative Construction**: :math:`4R_1 + 2R_2 + 6C_1 + 5C_3` — Simplicity :math:`S = 17`, Exactitude :math:`E = 10` (2 lines, 5 circles).
- **Lemoine Géométrographique Synthesis**: :math:`4R_1 + 2R_2 + 5C_1 + 4C_3` — Simplicity :math:`S = 15`, Exactitude :math:`E = 9` (2 lines, 4 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro X, §§ 143–144 (pp. 82–84, Fig. 71)*): Paired with Napoleon's Problem (§ 143, center of a drawn circle in 6 arcs): § 144 finds circumcenter O of three non-collinear points M, A, B by compass inversion/third-proportional arcs alone.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Zweite & Dritte Aufgabe ([71]–[75], pp. 52–55)*): Constructs the perpendicular bisectors of AB and AC by straightedge via fixed circle M; their intersection is X(3) (while the circle itself remains represented by center O and radius OA).
- **Critical Note**: Sharing circle B(R) across both perpendicular bisectors AB and BC cuts the circle count from 5 to 4 (3 mediatrix circles + circumcircle O(OA), S = 15).

.. _concordance-external-tangents:

XXVI — Tangents to a Given Circle from an External Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Mener d'un point extérieur A les tangentes à un cercle donné O*

**Lemoine Folio**: pp. 15–16 | **Euclid**: III.17 | **Elements DAG**: G.91 (III.17) | **Projective**: Pole-polar contact chord

- **Classical / Speculative Construction**: :math:`8R_1 + 4R_2 + 4C_1 + 3C_3` — Simplicity :math:`S = 19`, Exactitude :math:`E = 12` (4 lines, 3 circles).
- **Lemoine Géométrographique Synthesis**: :math:`5R_1 + 3R_2 + 6C_1 + 4C_3` — Simplicity :math:`S = 18`, Exactitude :math:`E = 11` (3 lines, 4 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro XI, § 161 (pp. 92–93)*): Finds midpoint M of OA (§ 66) or uses concentric radius 2R arc and circle A(OA) to determine contact points T, T' on O(R) by compass alone.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Erstes Kapitel, § 10 ([26]–[30], pp. 20–23)*): Pure straightedge construction! Draw two arbitrary secants from A cutting the drawn circle O, construct the polar of A via the complete inscribed quadrangle (Lemoine XXXIX, 12R_1 + 7R_2), and join A to its two intersections T, T' with circle O.
- **Critical Note**: Highlights instrument duality: when circle O is already drawn, Steiner's projective polar method needs ZERO circles (16R_1 + 9R_2 for both tangents), whereas Lemoine optimizes the metric ruler-and-compass construction to S = 18.

.. _concordance-incircle-x1:

XXVII — Incircle and Incenter X(1) of a Given Triangle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Inscrire un cercle dans un triangle donné ABC*

**Lemoine Folio**: pp. 16–18 | **Euclid**: IV.4 | **Elements DAG**: G.116 (IV.4) | **ETC**: X(1) Incenter

- **Classical / Speculative Construction**: :math:`6R_1 + 3R_2 + 11C_1 + 10C_3` — Simplicity :math:`S = 30`, Exactitude :math:`E = 17` (3 lines, 10 circles).
- **Lemoine Géométrographique Synthesis**: :math:`4R_1 + 2R_2 + 11C_1 + 6C_3` — Simplicity :math:`S = 23`, Exactitude :math:`E = 15` (2 lines, 6 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro X, § 149 (p. 85)*): Determines incenter X(1) and inradius by compass-only angle bisections (§ 118) and line intersection (§ 112) + reflection (§ 78).
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Dritte & Fünfte Aufgabe ([71]–[76], pp. 52–56)*): Bisects angles B and C via parallel diameters of fixed circle M (Fifth Problem) to meet at incenter I = X(1), then drops perpendicular from I to BC (Third Problem) to obtain touchpoint D.
- **Critical Note**: One of Lemoine's signature triumphs: eliminates 4 circles and 1 line (S: 30 -> 23) by reusing a single compass radius across vertices and measuring the perpendicular distance from I to BC without tracing the altitude line!

.. _concordance-fourth-proportional:

XXXIII — Fourth Proportional to Three Given Segments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire la quatrième proportionnelle x = bc/a à trois longueurs a, b, c*

**Lemoine Folio**: pp. 24–25 | **Euclid**: VI.12 | **Elements DAG**: G.167 (VI.12) | **Projective**: Thales intercept / Hilbert § 15 segment product

- **Classical / Speculative Construction**: :math:`4R_1 + 3R_2 + 11C_1 + C_2 + 6C_3` — Simplicity :math:`S = 25`, Exactitude :math:`E = 16` (3 lines, 6 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2R_1 + 2R_2 + 11C_1 + C_2 + 6C_3` — Simplicity :math:`S = 22`, Exactitude :math:`E = 14` (2 lines, 6 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro V, §§ 93–95 (pp. 48–49)*): Remarkably compact concentric-circle construction! Draw concentric circles O(a) and O(b); place chord BC = c in O(a), then step equal arcs BD = CE on O(b) from B and C to read chord DE = bc/a directly in 4 circles!
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Erste & Sechste Aufgabe ([68]–[78], pp. 50–57)*): Transfers segments onto two intersecting rays from O (Sixth Problem) and draws the Thales parallel via fixed circle M (First Problem).
- **Critical Note**: Fazzari's 1901 Palermo preface (p. xi) singles out Mascheroni's concentric-circle fourth proportional (§ 93, S = 14 when a <= 2c!) as simpler even than standard ruler-and-compass Thales constructions.

.. _concordance-mean-proportional:

XXXV — Mean Proportional (Geometric Mean) of Two Segments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire la moyenne proportionnelle entre deux longueurs données a et b*

**Lemoine Folio**: pp. 26–27 | **Euclid**: II.14, VI.13 | **Elements DAG**: G.63 (II.14), G.168 (VI.13) | **Projective**: Pappus Book III three-means configuration

- **Classical / Speculative Construction**: :math:`4R_1 + 3R_2 + 10C_1 + C_2 + 6C_3` — Simplicity :math:`S = 24`, Exactitude :math:`E = 15` (3 lines, 6 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2R_1 + 2R_2 + 6C_1 + C_2 + 3C_3` — Simplicity :math:`S = 14`, Exactitude :math:`E = 9` (2 lines, 3 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro VI, §§ 99–103 (pp. 51–54)*): Extracts sqrt(ab) by compass arcs alone using power-of-a-point / semicircle chord relations without drawing the diameter line.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Dritte & Siebente Aufgabe ([71]–[82], pp. 52–60)*): Intersects the altitude at the junction of a and b with the virtual semicircle on diameter a + b via Seventh Problem (line-circle intersection with fixed circle M).
- **Critical Note**: The Lemoine–Gouzy construction cuts S by 42% (24 -> 14), halving the circle count from 6 to 3.

.. _concordance-golden-section:

XXXVI — Division in Extreme and Mean Ratio (Golden Section phi)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Diviser une droite donnée AB en moyenne et extrême raison*

**Lemoine Folio**: pp. 27–28 | **Euclid**: II.11, VI.30 | **Elements DAG**: G.60 (II.11), G.185 (VI.30) | **Projective**: Q(phi) harmonic/golden range

- **Classical / Speculative Construction**: :math:`6R_1 + 3R_2 + 9C_1 + 7C_3` — Simplicity :math:`S = 25`, Exactitude :math:`E = 15` (3 lines, 7 circles).
- **Lemoine Géométrographique Synthesis**: :math:`2R_1 + R_2 + 9C_1 + 6C_3` — Simplicity :math:`S = 18`, Exactitude :math:`E = 11` (1 lines, 6 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro II, §§ 38–42 (pp. 22–24); Libro IX, § 128 (p. 70)*): Mascheroni's 5-circle regular decagon/pentagon division: stepping three hexagon chords B, C, D of radius r = AB around O(r) gives AC = BD = r*sqrt(3); intersecting A(AC) and D(BD) at E gives OE = r*sqrt(2), whence the decagon chord AB/phi and extreme-and-mean section (§ 128) follow by compass alone.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Dritte, Sechste & Siebente Aufgabe ([71]–[82], pp. 52–60)*): Erects perpendicular BC = AB/2 at B by straightedge (Second & Third Problems) and intersects line AC with virtual circle C(CB) via Seventh Problem, then transfers segment to AB via Sixth Problem.
- **Critical Note**: Lemoine traces ONLY ONE straight line (the perpendicular at B obtained simultaneously with the midpoint arc) instead of three lines in classical II.11/VI.30, cutting S from 25 to 18.

.. _concordance-circle-inversion:

XXXVIII — Inverse of a Given Point with Respect to a Given Circle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire l'inverse A' d'un point A par rapport à un cercle O(R)*

**Lemoine Folio**: pp. 29–30 | **Euclid**: III.36, VI.8 | **Elements DAG**: G.110 (III.36) | **Projective**: Inversive duality

- **Classical / Speculative Construction**: :math:`4R_1 + 2R_2 + 4C_1 + 2C_3` — Simplicity :math:`S = 12`, Exactitude :math:`E = 8` (2 lines, 2 circles).
- **Lemoine Géométrographique Synthesis**: :math:`5C_1 + 3C_3` — Simplicity :math:`S = 8`, Exactitude :math:`E = 5` (0 lines, 3 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro V, § 86 (p. 46, Fig. 35); August Adler (1890) inversion proof of Mohr–Mascheroni*): Identical 3-circle compass-only inversion (when OA > R/2): draw A(AO) cutting O(R) at M, N; then M(MO) and N(NO) intersect at A' with OA * OA' = R^2! (When OA <= R/2, double OA k times first.)
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Erstes Kapitel, § 10 ([26]–[30], pp. 20–23)*): Pure straightedge inversion! Construct the polar p of A with respect to the fixed circle O via an inscribed quadrangle, join OA, and intersect OA with p at A'.
- **Critical Note**: August Adler (1890) proved the entire Mohr–Mascheroni theorem at a stroke by observing that Lemoine's 5C_1 + 3C_3 inversion maps lines and circles into circles and lines using the compass alone.

.. _concordance-polar-of-point:

XXXIX — Polar Line of a Given Point with Respect to a Traced Circle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire la polaire d'un point donné A par rapport à un cercle tracé O*

**Lemoine Folio**: pp. 30–31 | **Euclid**: III.17, III.36 | **Elements DAG**: G.91 (III.17) | **Projective**: Pappus Book VII harmonic polarity

- **Classical / Speculative Construction**: :math:`10R_1 + 5R_2 + 6C_1 + 4C_3` — Simplicity :math:`S = 25`, Exactitude :math:`E = 16` (5 lines, 4 circles).
- **Lemoine Géométrographique Synthesis**: :math:`12R_1 + 7R_2` — Simplicity :math:`S = 19`, Exactitude :math:`E = 12` (7 lines, 0 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro V, § 86; Libro IV, § 77 (pp. 42–46)*): Constructs the inverse A' of A in circle O (5C_1 + 3C_3) and a second point on the perpendicular to OA at A' (§ 77).
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Erstes Kapitel, § 10, III–IV ([27]–[29], pp. 21–22)*): Exact same pure-straightedge inscribed quadrangle construction (12R_1 + 7R_2, S = 19, 0 circles), which works whether A lies outside or inside the circle and without needing the center O!
- **Critical Note**: Demonstrates that even inside standard ruler-and-compass Géométrographie, pure projective straightedge synthesis beats metric compass-and-ruler constructions (S = 19 vs. S = 25).

.. _concordance-radical-axis:

XLI — Radical Axis of Two Non-Intersecting Traced Circles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire l'axe radical de deux cercles tracés non sécants*

**Lemoine Folio**: pp. 31–32, 57–58 | **Euclid**: III.35, III.36 | **Elements DAG**: G.109, G.110 (III.35–36) | **Projective**: Coaxal pencil of circles

- **Classical / Speculative Construction**: :math:`18R_1 + 9R_2 + 19C_1 + 12C_3` — Simplicity :math:`S = 58`, Exactitude :math:`E = 37` (9 lines, 12 circles).
- **Lemoine Géométrographique Synthesis**: :math:`10R_1 + 5R_2 + 2C_3` — Simplicity :math:`S = 17`, Exactitude :math:`E = 10` (5 lines, 2 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro VI–VII, §§ 103, 112 (pp. 54, 61–62)*): Divides line of centers OO' at M where OM^2 - O'M^2 = R^2 - R'^2 via compass-only fourth proportional and erects a perpendicular point (§ 77).
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Zweites Kapitel, §§ 15–17 ([61]–[67], pp. 45–50); Achte Aufgabe ([82]–[85], pp. 60–62)*): Steiner coins the term 'Linie der gleichen Potenzen' and constructs the radical axis of two arbitrary circles by straightedge alone via their centers of similitude with the fixed circle M!
- **Critical Note**: In his famous reply to Amédée Mannheim (pp. 57–58), Lemoine contrasts Mannheim's midpoint-of-common-tangents construction (S = 58!) against two arbitrary secant circles C_3 + C_3 yielding radical center and axis in S = 17.

.. _concordance-harmonic-conjugate:

XLVI — Harmonic Conjugate of a Point with Respect to a Segment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire le conjugué harmonique D d'un point C par rapport à A et B*

**Lemoine Folio**: pp. 34–35 | **Euclid**: VI.3 (harmonic angle bisector) | **Elements DAG**: G.158 (VI.3) | **Projective**: Pappus Book VII Prop. 131 complete quadrilateral

- **Classical / Speculative Construction**: :math:`10R_1 + 6R_2 + 4C_1 + 2C_3` — Simplicity :math:`S = 22`, Exactitude :math:`E = 14` (6 lines, 2 circles).
- **Lemoine Géométrographique Synthesis**: :math:`9R_1 + 6R_2` — Simplicity :math:`S = 15`, Exactitude :math:`E = 9` (6 lines, 0 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro V, §§ 93, 96 (pp. 48–49)*): Computes BD from AD : BD = AC : BC via proportional segment division (§ 96) with compass arcs alone.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Erstes Kapitel, §§ 4–6 ([10]–[16], pp. 9–13)*): Identical pure-straightedge complete quadrilateral construction (9R_1 + 6R_2, S = 15, 0 circles) — didn't even require the fixed circle M!
- **Critical Note**: Projective invariant cross-ratio (A, B; C, D) = -1 constructed with zero compass operations; choosing the first auxiliary ray as R_1 + R_2 through A saves 3R_1 over naive alignment.

.. _concordance-centroid-x2:

L — Centroid G = X(2) of a Given Triangle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire le centre de gravité G d'un triangle donné ABC*

**Lemoine Folio**: pp. 42–43 | **Euclid**: I.10, I.34 | **Elements DAG**: G.11 (I.10), G.35 (I.34) | **ETC**: X(2) Centroid | **Projective**: Pappus centroidal median concurrency

- **Classical / Speculative Construction**: :math:`8R_1 + 4R_2 + 3C_1 + 3C_3` — Simplicity :math:`S = 18`, Exactitude :math:`E = 11` (4 lines, 3 circles).
- **Lemoine Géométrographique Synthesis**: :math:`6R_1 + 3R_2 + 6C_1 + 2C_3` — Simplicity :math:`S = 17`, Exactitude :math:`E = 12` (3 lines, 2 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro X, § 150 (p. 85); Libro III, § 68 (p. 36)*): Finds midpoint M_a of BC (§ 66) and trisects median AM_a at G via compass-only trisection (§ 68).
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Erste & Zweite Aufgabe ([68]–[71], pp. 50–52)*): Draws parallels to two sides via fixed circle M to bisect them harmonically, then intersects two medians by straightedge.
- **Critical Note**: Lemoine forms parallelogram ABDC with only 2 circles B(AC) and C(AB) so AD bisects BC without drawing BC's perpendicular bisector, cutting S from 18 to 17 (2 circles instead of 3).

.. _concordance-lemoine-point-x6:

LI — Lemoine Symmedian Point K = X(6) of a Given Triangle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire le point de Lemoine K d'un triangle donné ABC*

**Lemoine Folio**: pp. 43–45 | **Euclid**: VI.4, III.21–22 | **Elements DAG**: G.159 (VI.4) | **ETC**: X(6) Symmedian / Lemoine Point | **Projective**: Harmonic pole of Lemoine line / Gergonne-symmedian duality

- **Classical / Speculative Construction**: :math:`14R_1 + 7R_2 + 21C_1 + 12C_3` — Simplicity :math:`S = 54`, Exactitude :math:`E = 35` (7 lines, 12 circles).
- **Lemoine Géométrographique Synthesis**: :math:`4R_1 + 2R_2 + 13C_1 + 8C_3` — Simplicity :math:`S = 27`, Exactitude :math:`E = 17` (2 lines, 8 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro IV, § 78; Libro VII, § 112 (pp. 43, 61–62)*): Lemoine's antiparallel-reflection construction is already nearly compass-pure (8 circles, only 2 symmedian lines)! Intersecting those two symmedian point-pairs via Mascheroni § 112 yields X(6) by compass alone.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Erstes Kapitel, § 10; Drittes Kapitel, § 18 ([26]–[30], [68]–[75])*): Once circumcircle (ABC) is drawn, X(6) is constructed by PURE STRAIGHTEDGE without a single compass operation: construct the tangents at A, B, C via polars and join each vertex to the pole of its opposite side!
- **Critical Note**: Lemoine discovered X(6) in 1873 (AFAS Lyon, 'Sur quelques propriétés d'un point remarquable du triangle'). In Problem LI he halves the trilinear-coordinate cost (S: 54 -> 27) by reflecting antiparallel midpoints using only 2 traced lines!

.. _concordance-brocard-points:

LIV–LV — First and Second Brocard Points omega and omega' of a Triangle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire les points de Brocard ω et ω' d'un triangle donné ABC*

**Lemoine Folio**: pp. 46–48, 58–59 | **Euclid**: III.21, III.32 | **Elements DAG**: G.95 (III.21), G.106 (III.32) | **ETC**: Bicentric Brocard pair (Ω, Ω') | **Projective**: Harmonic/isogonal Brocard circle on diameter OK

- **Classical / Speculative Construction**: :math:`22R_1 + 11R_2 + 24C_1 + 17C_3` — Simplicity :math:`S = 74`, Exactitude :math:`E = 46` (11 lines, 17 circles).
- **Lemoine Géométrographique Synthesis**: :math:`12R_1 + 6R_2 + 12C_1 + 8C_3` — Simplicity :math:`S = 38`, Exactitude :math:`E = 24` (6 lines, 8 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro VII, §§ 110–112; Libro X, § 144 (pp. 60–63, 83–84)*): Constructs the centers of the adjoint tangent circles by compass-only perpendiculars and circumcenter arcs, locating ω and ω' as second intersections of the adjoint circles.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Erste, Dritte & Achte Aufgabe ([68]–[85], pp. 50–62)*): Constructs parallels and perpendiculars at A, B, C via fixed circle M to locate the adjoint circle centers, then intersects the virtual adjoint circles via their radical axes (Eighth Problem).
- **Critical Note**: In his reply to Henri Brocard (pp. 58–59), Lemoine dissects Brocard's own classical three-adjoint-circle trace (S = 74) and cuts the simultaneous cost nearly in half (S = 38; single Brocard point LIV takes 8R_1 + 4R_2 + 10C_1 + 6C_3, S = 28).

.. _concordance-nagel-point-x8:

LXI — Nagel Point X(8) of a Given Triangle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Construire le point de Nagel X(8) d'un triangle donné ABC*

**Lemoine Folio**: pp. 50 | **Euclid**: IV.4 (excircle touchpoints) | **Elements DAG**: G.116 (IV.4) | **ETC**: X(8) Nagel Point | **Projective**: Isotomic/cevian concurrency

- **Classical / Speculative Construction**: :math:`6R_1 + 3R_2 + 15C_1 + 10C_3` — Simplicity :math:`S = 34`, Exactitude :math:`E = 21` (3 lines, 10 circles).
- **Lemoine Géométrographique Synthesis**: :math:`4R_1 + 2R_2 + 7C_1 + 3C_3` — Simplicity :math:`S = 16`, Exactitude :math:`E = 11` (2 lines, 3 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro I, §§ 10–11; Libro VII, § 112 (pp. 12–13, 61–62)*): Transfers side lengths along the extended sides by three compass arcs to mark two excircle touchpoints T_b, T_c, then intersects cevians AT_b and BT_c by § 112.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Sechste Aufgabe ([76]–[78], pp. 56–57)*): Transfers side lengths along the triangle's sides via centers of similitude with fixed circle M to locate T_b, T_c, then joins AT_b and BT_c by straightedge.
- **Critical Note**: Instead of constructing two excircles via exterior angle bisectors (S = 34), Lemoine lays off semiperimeter differences directly with 3 circles and joins two Nagel cevians in S = 16!

Unit IV: Restricted & Alternative Instruments — Équerre, Mascheroni Compass-Only & Poncelet–Steiner Fixed-Circle
----------------------------------------------------------------------------------------------------------------

 Companion codex unit: :doc:`Unit IV: Restricted & Alternative Instruments — Équerre, Mascheroni Compass-Only & Poncelet–Steiner Fixed-Circle <unit-4-minimal-instruments/unit-4-minimal-instruments-en>`.

.. _concordance-mascheroni-midpoint-line-intersection:

Masch. §§ 66, 112 — Mascheroni Compass-Only Midpoint & Intersection of Two Lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Géométrographie Mascheronienne : milieu de AB et intersection de deux droites au compas seul*

**Lemoine Folio**: pp. Scientia 1902; Mascheroni pp. 33, 61–63 | **Euclid**: I.Post.3, I.10 | **Elements DAG**: G.2 (Postulate 3), G.11 (I.10) | **Projective**: Mohr–Mascheroni / Adler inversive completeness

- **Classical / Speculative Construction**: :math:`2R_1 + R_2 + 2C_1 + 2C_3` — Simplicity :math:`S = 7`, Exactitude :math:`E = 4` (1 lines, 2 circles).
- **Lemoine Géométrographique Synthesis**: :math:`10C_1 + 7C_3` — Simplicity :math:`S = 17`, Exactitude :math:`E = 10` (0 lines, 7 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro III, § 66 Sol. V (p. 33, Fig. 14); Libro VII, §§ 110–112 (pp. 60–63, Figs. 46–50)*): Proves compass-only completeness: line-circle intersection (§§ 110–111) and line-line intersection (§ 112, via symmetric points c, d across AB, parallelogram CDd-delta, and fourth proportional c-delta : CD = Cc : CS) reduce all Euclidean constructions to C_1, C_2, C_3.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Einleitung § 2 ([2]–[4], pp. 4–5)*): Steiner opens his 1833 treatise by contrasting Mascheroni's exclusion of the straightedge with the dual projective program of excluding the compass altogether.
- **Critical Note**: In Géométrographie Mascheronienne (r1 = r2 = 0), bisecting an un-drawn segment AB takes 10C_1 + 7C_3 (S = 17, 7 circles), whereas reflecting a point takes 4C_1 + 2C_3 (S = 6) and constructing a parallel point takes 5C_1 + 2C_3 (S = 7).

.. _concordance-steiner-parallel-circle-meet:

Steiner § 18 Aufg. 1–8 — Poncelet–Steiner Straightedge-Only Parallel & Virtual Circle Intersections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Géométrographie Steinerienne : parallèle et intersections de cercles à la règle seule avec un cercle fixe*

**Lemoine Folio**: pp. Scientia 1902; Steiner [68]–[85] (pp. 50–62) | **Euclid**: I.Post.1–2, I.31 | **Elements DAG**: G.1 (Postulate 1), G.32 (I.31) | **Projective**: Poncelet–Steiner Theorem (complete quadrangle + centers of similitude + radical axis)

- **Classical / Speculative Construction**: :math:`2R_1 + R_2 + 3C_1 + 3C_3` — Simplicity :math:`S = 9`, Exactitude :math:`E = 5` (1 lines, 3 circles).
- **Lemoine Géométrographique Synthesis**: :math:`11R_1 + 6R_2` — Simplicity :math:`S = 17`, Exactitude :math:`E = 11` (6 lines, 0 circles).
- **Mascheroni Compass-Only Counterpart** (*Libro VII, §§ 110–112 (pp. 60–63)*): Dual counterpart: where Mascheroni simulates straight lines via pairs of points and fourth-proportional arcs, Steiner simulates un-drawn circles via centers of similitude and radical axes.
- **Poncelet–Steiner Fixed-Circle Counterpart** (*Drittes Kapitel, § 18, Erste bis Achte Aufgabe ([68]–[85], pp. 50–62, Figs. 19–24)*): Proves straightedge-only completeness given ONE fixed circle with center M: parallel to a diameter aMb takes 11R_1 + 6R_2 (S = 17, 6 lines, 0 circles); Seventh & Eighth Problems find line-circle and circle-circle intersections of un-drawn circles via Aehnlichkeitspunkte A, I and the radical axis.
- **Critical Note**: Notice that center M IS indispensable: by Poncelet–Steiner–Hilbert projective invariance, a projective transformation fixing a circle without fixing its center destroys Euclidean parallelism and orthogonality!
