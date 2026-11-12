:layout: book

.. _geometrographie-unit-1-summary:

Unit I Summary: The Operational Calculus of *Géométrographie*
=============================================================

.. rubric:: Executive Synthesis of Genesis, Axiomatic Idealizations & Elementary Cost Vectors

1. Historical Stemma (1888 → 1892 → 1902)
-----------------------------------------

* **Oran (30 March 1888)**: :person:`Émile Lemoine <lemoine>` introduces quantitative simplicity measurement (:cite:`lemoine-1888`) using an experimental eight-operator system (:math:`\rho_1..\gamma'_2`) and right-angle set-square (*équerre*) primitives.
* **Pau (September 1892 / Gauthier-Villars 1893)**: Consolidates the five-operator ruler-and-compass canon :math:`(R_1, R_2, C_1, C_2, C_3)`, defines :math:`S` and :math:`E`, and benchmarks Problems I–LXIII (:cite:`lemoine-1892`).
* **Paris, Collection *Scientia* No. 18 (1902)**: Unifies standard *Géométrographie* with *Géométrographie de l'équerre*, :term:`Géométrographie Mascheronienne <geometrographie-mascheronienne>` (:cite:`mascheroni-1797`), and :term:`Géométrographie Steinerienne <geometrographie-steinerienne>` (:cite:`steiner-1833`).

2. The Five-Dimensional Vector Space of Constructions
-----------------------------------------------------

Every construction maps to a non-negative integer vector :math:`\mathbf{v} = (l_1, l_2, m_1, m_2, m_3) \in \mathbb{Z}_{\ge 0}^5`:

.. list-table:: Canonical *Géométrographie* Cost Primitives
   :header-rows: 1
   :widths: 14 22 44 10 10

   * - Symbol
     - Instrument
     - Physical / Incidence Action
     - :math:`\Delta S`
     - :math:`\Delta E`
   * - :term:`R₁ <r1>`
     - Straightedge
     - Make straightedge pass through 1 determined point (:math:`2R_1` for 2 points)
     - :math:`+1`
     - :math:`+1`
   * - :term:`R₂ <r2>`
     - Straightedge
     - Trace straight line along aligned straightedge
     - :math:`+1`
     - :math:`0`
   * - :term:`C₁ <c1>`
     - Compass
     - Set one compass point on a determined point (:math:`2C_1` to span :math:`AB`)
     - :math:`+1`
     - :math:`+1`
   * - :term:`C₂ <c2>`
     - Compass
     - Set one compass point at an indeterminate point of a traced locus
     - :math:`+1`
     - :math:`+1`
   * - :term:`C₃ <c3>`
     - Compass
     - Describe circle or circular arc
     - :math:`+1`
     - :math:`0`

Linear functionals on :math:`\mathbf{v}` yield:

* **Simplicity**: :math:`S(\mathbf{v}) = l_1 + l_2 + m_1 + m_2 + m_3` (total elementary steps).
* **Exactitude**: :math:`E(\mathbf{v}) = l_1 + m_1 + m_2` (total point/locus alignments; smaller :math:`E` = higher precision).
* **Locus Complexity**: :math:`l_2` straight lines and :math:`m_3` circles drawn on the plane.

3. Why Euclid I.2–I.3 Costs :math:`S = 16` vs. Lemoine VIII :math:`S = 4`
-------------------------------------------------------------------------

In :person:`Euclid <euclid>`'s *Elements* I.2–I.3 (:cite:`euclid-heath`; see :ref:`concordance-transfer-segment`), transferring a segment :math:`AB` to a line without assuming a persistent-aperture divider compass requires constructing an equilateral triangle (:math:`I.1`) and two concentric transfer circles: :math:`4R_1 + 2R_2 + 5C_1 + 5C_3` (:math:`S = 16, E = 9`, 2 lines, 5 circles). With a modern divider compass, Lemoine's Operation VIII executes the transfer in :math:`2C_1 + C_2 + C_3` (or :math:`3C_1 + C_3` from a marked origin), i.e., :math:`S = 4, E = 3`, 0 lines, 1 circle—immediately illustrating the chasm between axiomatic minimalism of postulates and operational minimalism of execution.
