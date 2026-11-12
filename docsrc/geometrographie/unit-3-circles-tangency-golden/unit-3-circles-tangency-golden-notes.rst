:layout: book

.. _geometrographie-unit-3-notes:

Unit III Commentary & Notes: Projective Purity, Golden Ratio & Triangle Synthesis
=================================================================================

.. rubric:: Cross-Corpus Commentary Linking Euclid, Pappus, ETC, Mascheroni & Steiner

1. Spontaneous Emergence of Compass-Only and Straightedge-Only Optimality
-------------------------------------------------------------------------

One of the deepest discoveries in Unit III is that **unrestricted** *Géométrographie*—seeking only to minimize :math:`S` when *both* straightedge and compass are freely available—spontaneously selects:

* **Pure compass** (:math:`l_1 = l_2 = 0`) for **circle inversion** (Problem XXXVIII: :math:`5C_1 + 3C_3, S = 8`, identical to :person:`Mascheroni <mascheroni>`'s Libro V, § 86, :cite:`mascheroni-1797`) and **point reflection** (Problem XVIII *bis*: :math:`S = 6`);
* **Pure straightedge** (:math:`m_1 = m_2 = m_3 = 0`) for **circle polarity** (Problem XXXIX: :math:`12R_1 + 7R_2, S = 19`, identical to :person:`Steiner <steiner>`'s § 10, :cite:`steiner-1833`) and **harmonic conjugation** (Problem XLVI: :math:`9R_1 + 6R_2, S = 15`, from :person:`Pappus <pappus>`'s *Synagoge* VII, :cite:`pappus-synagoge`).

This reveals a fundamental duality between **transformation group** and **optimal instrument**: conformal/inversive point maps minimize :math:`S` on the compass, whereas projective/harmonic collineations and correlations minimize :math:`S` on the straightedge!

2. Algebraic Anatomy of Lemoine's 1-Line Golden Section (Problem XXXVI)
-----------------------------------------------------------------------

In :person:`Euclid <euclid>`'s *Elements* II.11 (:cite:`euclid-heath`; see :external+euclid:doc:`index` and :external+elements:doc:`index`), dividing :math:`AB` of length :math:`2a` in extreme and mean ratio constructs a square :math:`ABDC` on :math:`AB`, bisects :math:`AC` at :math:`E`, extends :math:`CA` to :math:`F` with :math:`EF = EB = a\sqrt{5}`, and constructs square :math:`AFGH` cutting :math:`AB` at :math:`H`. Even stripped to its barest textbook form, three straight lines are drawn.

In Lemoine's Problem XXXVI (:math:`2R_1 + R_2 + 9C_1 + 6C_3, S = 18`), only **one straight line**—the perpendicular bisector :math:`x = a` through midpoint :math:`M` of :math:`AB`—is ever traced. Placing :math:`C = (a, 2a)` on that single line via :math:`M(AB)` creates the un-drawn Pythagorean hypotenuse :math:`BC = \sqrt{a^2 + (2a)^2} = a\sqrt{5}` directly between existing points :math:`B = (2a, 0)` and :math:`C = (a, 2a)`. Sweeping :math:`B(C)` onto the carrier line at :math:`E = (2a - a\sqrt{5}, 0)` yields:

.. math::

   ME = a - (2a - a\sqrt{5}) = a(\sqrt{5} - 1) = \frac{2a}{\phi} = \frac{AB}{\phi},

which arc :math:`A(ME)` transfers onto :math:`AB` at :math:`X`. Every quadratic irrational in :math:`\mathbb{Q}(\phi) = \mathbb{Q}(\sqrt{5})` is extracted via compass distance between determined points without tracing hypotenuse :math:`BC`!

3. Mannheim and Brocard's Objections Answered (pp. 57–59)
---------------------------------------------------------

Two celebrated historical exchanges in Lemoine's *Considérations générales* illuminate Unit III:

* **Reply to Amédée Mannheim on the Radical Axis (pp. 57–58)**: :person:`Mannheim <mannheim>` objected that in descriptive geometry lectures one defines the radical axis of two exterior circles by joining the midpoints of two common tangents. Lemoine calmly evaluates Mannheim's construction: two common tangents plus two midpoints cost :math:`18R_1 + 9R_2 + 19C_1 + 12C_3` (:math:`S = 58, E = 37`, 9 lines, 12 circles!), whereas sweeping two arbitrary intersecting circles (:math:`2C_3`) costs :math:`10R_1 + 5R_2 + 2C_3` (:math:`S = 17, E = 10`)—more than a threefold reduction in both effort and alignment error!
* **Reply to Henri Brocard on :math:`\omega, \omega'` (pp. 58–59)**: :person:`Brocard <brocard>` wrote to Lemoine defending the symmetric beauty of intersecting the three adjoint circles tangent to the sides of :math:`\triangle ABC` at its vertices. Lemoine prints the exact accounting: Brocard's symmetric construction costs :math:`22R_1 + 11R_2 + 24C_1 + 17C_3` (:math:`S = 74, E = 46`), whereas Lemoine's Problem LV obtains *both* :math:`\omega` and :math:`\omega'` in :math:`12R_1 + 6R_2 + 12C_1 + 8C_3` (:math:`S = 38, E = 24`), demonstrating once and for all that **symmetric algebraic specification is distinct from optimal constructive synthesis**.
