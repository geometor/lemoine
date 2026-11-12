:layout: book

.. _geometrographie-unit-1-en:

Unit I: Historical Genesis, Methodological Criteria & The Five Elementary Operations
====================================================================================

.. rubric:: Émile Lemoine — *Géométrographie, ou Art des constructions géométriques* (English Translation, pp. 1–5 & 52–65)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _lemoine-en-genesis:

.. folio:: Préliminaires
   :page: 1

§ 1. Aim of *Géométrographie*: Speculative vs. Constructive Simplicity
----------------------------------------------------------------------

From antiquity onward, geometers have sought the simplest demonstration of a theorem, yet almost universally neglected to measure the simplicity of the *execution* of a construction. When :person:`Euclid <euclid>` (:cite:`euclid-heath`) reduces a new problem to a chain of previously established propositions, his criterion of simplicity is purely *speculative* (:term:`construction spéculative <construction-speculative>`): a construction is deemed brief when its verbal enunciation is concise and its deductive proof invokes few words. When one actually takes straightedge and compass in hand upon the drawing sheet, however, a construction that requires three lines of text to state and prove may demand fifty or sixty distinct instrumental operations, whereas another construction requiring a subtler geometric analysis executes in fifteen.

:term:`Géométrographie <geometrographie>`, first announced by :person:`Émile Lemoine <lemoine>` at the Oran Congress of the *Association Française pour l'Avancement des Sciences* on 30 March 1888 (:cite:`lemoine-1888`), developed systematically at the Pau Congress in 1892 (:cite:`lemoine-1892`), and brought to definitive form in *Collection Scientia* No. 18 (:cite:`lemoine-1902`), supplies an exact quantitative calculus for the art of geometric constructions. Its dual aim is:

1. To evaluate with complete numerical precision the **simplicity** and **exactitude** of any proposed construction; and
2. To replace habitual textbook constructions with genuinely *géométrographique* syntheses minimizing elementary operations without sacrificing rigor.

.. _lemoine-en-ideal-postulates:

.. folio:: Hypothèses d'épure
   :page: 2

§ 2. Ideal Sheet & Instrument Hypotheses
----------------------------------------

To isolate the intrinsic algebraic-operational structure of a construction from accidental drafting contingencies, :person:`Lemoine <lemoine>` stipulates three methodological conventions (pp. 2, 52–54):

* **Unlimited Drawing Sheet**: The plane of execution is assumed unbounded; exercises constrained by torn margins or inaccessible intersections belong to special problems of descriptive drafting (*épure*), not to general *Géométrographie*.
* **Ideal Straightedge and Modern Divider Compass**: The straightedge has unlimited length and a single ungraduated straight edge. Unlike the "collapsing compass" often read into :person:`Euclid <euclid>`'s *Elements* I.1–I.3 (see :external+euclid:doc:`index` and :external+elements:doc:`index`), the modern compass retains an aperture once set between two points until deliberately altered—and a geometer may lay down or use the straightedge without forfeiting a previously set compass radius.
* **Well-Conditioned Data**: Given points and circles are assumed in general position so that intersections are well-determined; graphical ill-conditioning (e.g., aligning a ruler across two nearly coincident points) belongs to physical error analysis (:person:`Maurice d'Ocagne <docagne>`, pp. 60–62), whereas *Géométrographie* counts the discrete alignment acts themselves.

.. _lemoine-en-five-operations:

.. folio:: Les cinq opérations
   :page: 3

§ 3. The Five Canonical Elementary Operations
---------------------------------------------

Every ruler-and-compass construction resolves into five—and only five—irreducible elementary acts:

* :term:`R₁ <r1>` — **Place the edge of the straightedge in coincidence with one determined point** (:math:`\mathrm{op.} : R_1`). Bringing the edge of the ruler to pass simultaneously through *two* determined points :g:`A` and :g:`B` requires two point coincidences and therefore counts as :math:`2R_1` (never :math:`R_1`, even if one extremity already lay near the ruler).
* :term:`R₂ <r2>` — **Draw the indefinite straight line along the edge of the straightedge** (:math:`\mathrm{op.} : R_2`).
* :term:`C₁ <c1>` — **Place one point of the compass upon one determined point** (:math:`\mathrm{op.} : C_1`). Taking up in the compass the distance :g:`AB` between two placed points :g:`A` and :g:`B` places both legs on determined points and counts as :math:`2C_1`. If one leg then remains pivoted at :g:`A` or :g:`B` to trace a circle immediately, no third :math:`C_1` is incurred; if the compass is lifted to place a leg upon a third determined center :g:`O`, that placement adds :math:`C_1` (for :math:`3C_1` in all).
* :term:`C₂ <c2>` — **Place one point of the compass at an indeterminate (arbitrary) point of a traced line or circle** (:math:`\mathrm{op.} : C_2`). Placing a compass point at an arbitrary point of the *blank plane* off all traced loci requires no alignment and counts as :math:`0`.
* :term:`C₃ <c3>` — **Trace the circle or circular arc** (:math:`\mathrm{op.} : C_3`), whether a small arc or the entire circumference is drawn.

.. picture:: /_static/figures/fig_elementary_operations.svg

In the left panel above, aligning the straightedge across :g:`A` and :g:`B` costs :math:`2R_1` and tracing the line :g:`AB` adds :math:`R_2`, yielding :math:`2R_1 + R_2` (:math:`S = 3, E = 2`). In the right panel, :term:`Lemoine's circle notation <cercle-o-ab>` writes :g:`O(AB)` for the circle centered at :g:`O` with radius equal to segment :g:`AB`, and cutting a traced line at :g:`M`, :g:`N` from an arbitrary locus point :g:`M` with given aperture costs :math:`2C_1 + C_2 + C_3` (:math:`S = 4, E = 3`).

.. _lemoine-en-symbol-coefficients:

§ 4. Construction Symbol, Simplicity (:math:`S`), and Exactitude (:math:`E`)
----------------------------------------------------------------------------

Any completed construction is summarized by its canonical **operation symbol**:

.. math::

   \mathrm{Op.} : \left(l_1 R_1 + l_2 R_2 + m_1 C_1 + m_2 C_2 + m_3 C_3\right),

from which four fundamental invariants are read off immediately:

.. math::

   \begin{aligned}
   \text{Coefficient of Simplicity:} \quad S &= l_1 + l_2 + m_1 + m_2 + m_3, \\
   \text{Coefficient of Exactitude:} \quad E &= l_1 + m_1 + m_2, \\
   \text{Number of Straight Lines Drawn:} \quad N_{\text{lines}} &= l_2, \\
   \text{Number of Circles Drawn:} \quad N_{\text{circles}} &= m_3.
   \end{aligned}

Here :term:`S (simplicité) <simplicite>` measures total operational labor, while :term:`E (exactitude) <exactitude>` counts the *preparatory coincidences* (:math:`R_1, C_1, C_2`) where the draftsman's eye and hand must align an instrument with an existing point or locus before drawing (:math:`R_2, C_3`). Each preparatory coincidence introduces an observational error; consequently, a **smaller** value of :math:`E` indicates fewer opportunities for alignment error and hence higher graphical precision.

.. _lemoine-en-fundamental-table:

.. folio:: Opérations I–X
   :page: 4

§ 5. Fundamental Operations I–X & Abandonment of the 1888 Notation
------------------------------------------------------------------

Pages 4–5 establish the ten elementary building blocks from which compound problems are assembled:

.. list-table:: Lemoine's Ten Elementary Building Blocks (Problems I–X, pp. 4–5)
   :header-rows: 1
   :widths: 8 44 24 8 8 8

   * - No.
     - Elementary Construction
     - Symbol
     - :math:`S`
     - :math:`E`
     - L / C
   * - **I**
     - Trace an completely arbitrary straight line
     - :math:`R_2`
     - 1
     - 0
     - 1 / 0
   * - **II**
     - Trace a straight line through one given point :math:`A`
     - :math:`R_1 + R_2`
     - 2
     - 1
     - 1 / 0
   * - **III**
     - Trace the straight line joining two given points :math:`A, B`
     - :math:`2R_1 + R_2`
     - 3
     - 2
     - 1 / 0
   * - **IV**
     - Trace an arbitrary circle (arbitrary center and radius)
     - :math:`C_3`
     - 1
     - 0
     - 0 / 1
   * - **V**
     - Trace a circle of arbitrary radius around a given center :math:`O`
     - :math:`C_1 + C_3`
     - 2
     - 1
     - 0 / 1
   * - **VI**
     - Trace a circle of given radius :math:`AB` around an arbitrary point of the plane
     - :math:`2C_1 + C_3`
     - 3
     - 2
     - 0 / 1
   * - **VII**
     - Trace circle :math:`O(A)` centered at given :math:`O` through given :math:`A`
     - :math:`2C_1 + C_3`
     - 3
     - 2
     - 0 / 1
   * - **VIIIa**
     - Lay off given length :math:`AB` on a traced line from an arbitrary point of it
     - :math:`2C_1 + C_2 + C_3`
     - 4
     - 3
     - 0 / 1
   * - **VIIIb**
     - Lay off given length :math:`AB` on a traced line from a determined point :math:`M` on it
     - :math:`3C_1 + C_3`
     - 4
     - 3
     - 0 / 1
   * - **IX–X**
     - Lay off sum or difference :math:`AB \pm CD` on a traced line from an arbitrary point
     - :math:`4C_1 + C_2 + 2C_3`
     - 7
     - 5
     - 0 / 2

In his closing methodological reflections (pp. 55–56), :person:`Lemoine <lemoine>` explains why he abandoned his preliminary eight-symbol Oran notation (:math:`\rho_1, \rho_2, \rho_3, \gamma_1, \gamma'_1, \gamma''_1, \gamma_2, \gamma'_2` of :cite:`lemoine-1888`), which distinguished sliding the ruler from rotating it around a pin and separated taking a radius from setting a pivot: those sub-distinctions introduced subjective ambiguity without altering comparative rankings, whereas :math:`(R_1, R_2, C_1, C_2, C_3)` yields an objective invariant agreed upon independently by every geometer who counts a construction.
