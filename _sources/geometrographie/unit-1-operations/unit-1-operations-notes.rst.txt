:layout: book

.. _geometrographie-unit-1-notes:

Unit I Commentary & Notes: Epistemology of Constructive Complexity
==================================================================

.. rubric:: Scholarly Apparatus, Cross-Corpus Concordance & Algorithmic Interpretation

1. Problems vs. Theorems: Proclus, Hoenen, and Lemoine
------------------------------------------------------

In his *Commentary on Book I of Euclid's Elements* (:cite:`proclus-in-euclidem`), :person:`Proclus <proclus>` records the ancient controversy between the schools of Speusippus (who held that all geometric propositions are timeless contemplative *theorems*) and Menaechmus (who held that all geometric propositions are constructive *problems* bringing figures into genesis within spatial imagination, *phantasia*). In *De Noetica Geometriae* (:cite:`hoenen-1954`; see :external+hoenen:doc:`index`), Peter Hoenen S.J. analyzes how *materia intelligibilis* bridges ideal geometric essence and imaginative construction.

:person:`Émile Lemoine <lemoine>` discovers an overlooked third dimension of this classical distinction (pp. 60–65): Greek geometers drew schematic figures freehand in sand or wax dust, using postulates (*aitemata*) solely as **existential licenses** inside deductive syllogisms. Consequently, Greek synthesis optimized **logical call-depth**—reducing Problem :math:`P_n` to :math:`P_{n-1}`—which behaves exactly like an un-inlined recursive subroutine in computer science: concise source code, heavy runtime instruction count! *Géométrographie* is the historical birth of **concrete computational complexity theory** for geometric algorithms, counting exact primitive instructions rather than asymptotic big-:math:`O` steps.

2. Critical Nuances in Counting :math:`C_1` and :math:`C_2`
-----------------------------------------------------------

Students reading :cite:`lemoine-1902` for the first time should note three subtle rules verified across Lemoine's sixty-three problems:

1. **Circle :math:`O(A)` Costs :math:`2C_1 + C_3`, Whereas Circle :math:`O(BC)` Costs :math:`3C_1 + C_3`**:
   When drawing :math:`O(A)` (Operation VII), one compass leg is set on :math:`O` (:math:`C_1`), the other on :math:`A` (:math:`C_1`), and the circle is swept immediately around :math:`O` (:math:`C_3`)—total :math:`2C_1 + C_3` (:math:`S = 3`). When transferring a detached distance :math:`BC` to center :math:`O`, spanning :math:`BC` costs :math:`2C_1`, lifting and setting the pivot on :math:`O` costs a third :math:`C_1`, and sweeping costs :math:`C_3`—total :math:`3C_1 + C_3` (:math:`S = 4`).
2. **Retaining Compass Aperture Across Ruler Operations**:
   Lemoine explicitly permits keeping a fixed radius in the compass while picking up the straightedge to draw a line. Thus in Problem XVIII (perpendicular bisector), choosing an *arbitrary* sufficient aperture costs :math:`0` to open, :math:`C_1 + C_3` around :math:`A`, and :math:`C_1 + C_3` around :math:`B` (:math:`2C_1 + 2C_3` for both circles, versus :math:`3C_1 + 2C_3` in Euclid I.10 where the aperture is forced to equal :math:`AB`).
3. **Why Arbitrary Plane Points Cost :math:`0`, Locus Points Cost :math:`C_2`, and Intersection Points Cost :math:`C_1`**:
   The cost of placing a point equals the **codimension** of the constraint in :math:`\mathbb{R}^2`:

   * Open 2D plane (codimension :math:`0`): :math:`0` alignment cost;
   * 1D curve—traced line or circle (codimension :math:`1`): :math:`C_2` (or :math:`R_1` for ruler);
   * 0D determined point (codimension :math:`2`): :math:`C_1` (or :math:`R_1` for ruler).

3. Reception in Palermo (1901), Edinburgh (1893), and Vienna (1890–1906)
------------------------------------------------------------------------

Within a decade of Pau (:cite:`lemoine-1892`), *Géométrographie* became an international standard:

* John Sturgeon Mackay introduced the system in Britain in *The Geometrography of Euclid's Problems* (:cite:`mackay-1893`), followed by Lemoine's own Edinburgh memoir (:cite:`lemoine-1895`).
* In Palermo, :person:`Gaetano Fazzari <fazzari>` opened his critical 1901 edition of :person:`Mascheroni <mascheroni>`'s *La Geometria del Compasso* (:cite:`fazzari-1901`, Preface p. xi) by comparing Mascheroni's compass-only fourth proportional against Euclidean ruler-and-compass methods via *"il metodo della Geometrografia del Lemoine"*.
* In Vienna and Prague, :person:`August Adler <adler>` (:cite:`adler-1890`) integrated Lemoine's operation counts directly into his unified treatise on Mascheroni, Steiner, and set-square constructions.
