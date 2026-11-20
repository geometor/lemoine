:layout: book
:canonical_id: Principes
:order: 1
:folio: 0052
:tracks: English: 20_principles_and_rational_division-en | French: 20_principles_and_rational_division-fr | Summary: 20_principles_and_rational_division-summary | Notes: 20_principles_and_rational_division-notes

.. _lemoine-20_principles_and_rational_division-en:

Five Guiding Principles & Simultaneous 1/10 and 1/15 Division
=============================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 36–39, fols. ``0052–0055``)

.. folio:: 0052
   :page: p. 36

Having audited forty-eight canonical constructions, :person:`Lemoine <lemoine>` distills the art of *Géométrographie* into **Five Guiding Principles** (*Principes*, pp. 36–37):

1. **Exploit every already-traced line, circle, and held compass aperture** across the entire figure before introducing a new line or resetting the compass.

.. folio:: 0053
   :page: p. 37

2. **Choose among competing geometric solutions** the one whose *total* completed construction (not merely its verbal enunciation!) achieves the lowest operation symbol.
3. **Analyze every special case of the given data** (for example, in the Problem of Apollonius—circles tangent to three given circles—a delicate exercise of geometric sagacity for students).
4. **In determining the GENERAL symbol of a problem, use only general subroutines** unless one proves that a special hypothesis always holds (e.g., use Polar XXXIX *a* or *b*, never *c* unless :math:`OA > R/2` is guaranteed).
5. **For a specific numerical or concrete drawing, freely exploit every special shortcut** whose hypotheses hold in the given configuration.

.. folio:: 0054
   :page: p. 38

Simultaneous :math:`\frac{1}{10}` and :math:`\frac{1}{15}` Division of :math:`BC` (FIG. 10)
---------------------------------------------------------------------------------------------

To illustrate Principle 5, Lemoine confronts the problem of dividing a segment :math:`BC` simultaneously into :math:`\frac{1}{10}BC` and :math:`\frac{1}{15}BC` without suffering the cumulative error of stepping 15 tiny ticks via Problem XXXI!

On folio ``0054`` (p. 38, **FIG. 10**), erect equilateral triangle :g:`AB'C'` of side :math:`BC` and extend base :g:`B'D` so :math:`C'D = BC`. Let :g:`E` and :g:`H` be the midpoints of :g:`AB'` and :g:`AC'`. Draw transversals :g:`ED` (cutting :g:`AC'` at :g:`F`), :g:`GD` through :g:`H` (cutting :g:`AB'` at :g:`G`), :g:`GM` through :g:`F` (cutting midline :g:`EH` at :g:`I` and base :g:`B'D` at :g:`M`), and finally :g:`KD` through :g:`I` (cutting :g:`AC'` at :g:`L` and :g:`AB'` at :g:`K`). By Menelaus's theorem and elementary ratios:

.. math::

   \begin{aligned}
   KG &= \frac{1}{15}\,BC, \qquad KE = \frac{1}{10}\,BC, \qquad HF = GE = IH = \frac{1}{6}\,BC, \\
   MC' &= IE = FC' = \frac{1}{3}\,BC, \qquad LA = \frac{4}{7}\,BC, \qquad LC' = \frac{3}{7}\,BC, \qquad LH = \frac{1}{14}\,BC,
   \end{aligned}

yielding **both** :g:`KG` :math:`= \frac{1}{15}BC` and :g:`KE` :math:`= \frac{1}{10}BC`—plus exact thirds, sixths, sevenths, and fourteenths—in a single clean configuration of simplicity :math:`S = 35`!

.. container:: lemoine-plate-pair

   .. picture:: 0054.g1.png
      :alt: Archival 1893 engraving FIG. 10 showing Lemoine's equilateral-triangle 1/10 and 1/15 division of BC
      :caption: FIG. 10 archival scan (Paris 1893, fol. 0054, p. 38): Simultaneous 1/15 (KG) and 1/10 (KE) division of BC.

   .. picture:: 0054.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 10 (exact Menelaus rational division of equilateral triangle)
      :caption: FIG. 10 vectorization: Exact SymPy calibration verifying KG = (1/15)BC, KE = (1/10)BC, LH = (1/14)BC, and MC' = (1/3)BC (S = 35).

.. folio:: 0055
   :page: p. 39

On page 39, Lemoine computes the exact radical lengths simultaneously present in **FIG. 10** (:math:`HG = \frac{\sqrt{7}}{6}BC`, :math:`DH = \frac{\sqrt{7}}{2}BC`, :math:`DF = \frac{\sqrt{13}}{3}BC`, :math:`EF = \frac{\sqrt{13}}{6}BC`, :math:`KL = \frac{2\sqrt{79}}{35}BC`, :math:`GI = IF = \frac{1}{2\sqrt{3}}BC`) and poses an unexpected open problem in Diophantine geometry via Menelaus's theorem: for integer triangle sides :math:`a, b, c`, when does :math:`ayz - bzx - cxy + bcx - cay - abz + abc = 0` admit nonzero integer solutions?
