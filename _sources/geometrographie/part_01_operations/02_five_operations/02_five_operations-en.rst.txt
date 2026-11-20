:layout: book
:canonical_id: Exposition
:order: 2
:folio: 0019
:tracks: English: 02_five_operations-en | French: 02_five_operations-fr | Summary: 02_five_operations-summary | Notes: 02_five_operations-notes

.. _lemoine-02_five_operations-en:
.. _lemoine-en-five-operations:

The Five Elementary Operations & Coefficients S and E
=====================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 3–5, fols. ``0019–0021``)

.. folio:: 0019
   :page: p. 3

Every plane construction executed with ungraduated straightedge and compass decomposes exhaustively into **five—and only five—irreducible elementary operations**:

* :term:`R₁ <r1>` — **Bring the edge of the straightedge into coincidence with one determined point** (:math:`\mathrm{op.} : R_1`). Aligning the ruler simultaneously through *two* determined points :g:`A` and :g:`B` requires two point coincidences and therefore always counts as :math:`2R_1`.
* :term:`R₂ <r2>` — **Draw the straight line along the aligned edge of the straightedge** (:math:`\mathrm{op.} : R_2`).
* :term:`C₁ <c1>` — **Place one point of the compass upon one determined point** (:math:`\mathrm{op.} : C_1`). Spanning the distance :g:`AB` between two placed points :g:`A` and :g:`B` sets both compass legs on determined points and counts as :math:`2C_1`. If one leg then remains pivoted at :g:`A` or :g:`B` to trace an arc immediately, no additional :math:`C_1` is incurred; lifting the compass to place its pivot at a third determined center :g:`O` adds one :math:`C_1` (for :math:`3C_1` in all).
* :term:`C₂ <c2>` — **Place one point of the compass at an indeterminate point of a line (straight or circular) already traced** (:math:`\mathrm{op.} : C_2`). Setting a compass leg at an arbitrary point of the blank plane off all traced loci requires no alignment and counts as :math:`0`.
* :term:`C₃ <c3>` — **Trace the circle or required circular arc** (:math:`\mathrm{op.} : C_3`), whether a brief intersecting arc or the complete circumference is drawn.

.. picture:: /_static/figures/fig_elementary_operations.svg
   :alt: Diagram of Lemoine's five elementary ruler-and-compass operations R1, R2, C1, C2, C3
   :caption: Lemoine's five elementary operations: straightedge alignment and trace (2R₁ + R₂, S = 3) alongside circle notation O(AB) and locus-constrained transfer (2C₁ + C₂ + C₃, S = 4).

In the left panel above, aligning the ruler edge across :g:`A` and :g:`B` costs :math:`2R_1` and drawing line :g:`AB` adds :math:`R_2`, giving :math:`2R_1 + R_2` (:math:`S = 3, E = 2`). In the right panel, :term:`Lemoine's compact circle notation <cercle-o-ab>` denotes by :g:`O(AB)` the circle centered at :g:`O` whose radius equals segment :g:`AB`, while marking a length along a traced line from an indeterminate locus point :g:`M` costs :math:`2C_1 + C_2 + C_3` (:math:`S = 4, E = 3`).

.. _lemoine-en-symbol-coefficients:

.. folio:: 0020
   :page: p. 4

The Operation Symbol & Invariants :math:`S` and :math:`E`
---------------------------------------------------------

If executing a complete construction requires :math:`l_1` occurrences of :math:`R_1`, :math:`l_2` of :math:`R_2`, :math:`m_1` of :math:`C_1`, :math:`m_2` of :math:`C_2`, and :math:`m_3` of :math:`C_3`, Lemoine summarizes the entire graphical procedure by a single algebraic **operation symbol**:

.. math::

   \mathrm{Op.} : \left(l_1 R_1 + l_2 R_2 + m_1 C_1 + m_2 C_2 + m_3 C_3\right).

Four fundamental invariants are read directly from this vector:

.. math::

   \begin{aligned}
   \text{Coefficient of Simplicity:} \quad S &= l_1 + l_2 + m_1 + m_2 + m_3, \\
   \text{Coefficient of Exactitude:} \quad E &= l_1 + m_1 + m_2, \\
   \text{Number of Traced Straight Lines:} \quad N_{\text{lines}} &= l_2, \\
   \text{Number of Traced Circles:} \quad N_{\text{circles}} &= m_3.
   \end{aligned}

.. folio:: 0021
   :page: p. 5

The :term:`coefficient of simplicity <simplicite>` :math:`S` counts the total number of elementary acts, while the :term:`coefficient of exactitude <exactitude>` :math:`E` counts solely the *preparatory coincidences* (:math:`R_1, C_1, C_2`) prior to drawing (:math:`R_2, C_3`). Because every point coincidence entails a small observational inaccuracy, a **smaller** integer :math:`E` denotes fewer opportunities for drafting error and therefore greater precision.

Lemoine also notes on pp. 4–5 (and again on pp. 55–56) why he streamlined his preliminary 1888 Oran eight-symbol system (:math:`\rho_1, \rho_2, \rho_3, \gamma_1, \gamma'_1, \gamma''_1, \gamma_2, \gamma'_2` of :cite:`lemoine-1888`) down to :math:`(R_1, R_2, C_1, C_2, C_3)`: distinguishing sliding vs. pivoting movements added subjective ambiguity without changing comparative rankings, whereas the five-symbol calculus yields an objective invariant verified identically by every geometer.
