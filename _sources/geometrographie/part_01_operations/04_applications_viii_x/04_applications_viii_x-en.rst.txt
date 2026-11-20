:layout: book
:canonical_id: Apps. VIII–X
:order: 4
:folio: 0022
:tracks: English: 04_applications_viii_x-en | French: 04_applications_viii_x-fr | Summary: 04_applications_viii_x-summary | Notes: 04_applications_viii_x-notes

.. _lemoine-04_applications_viii_x-en:

Applications VIII–X: Segment Transfer & Equidistant Points
==========================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, p. 6, fols. ``0022``)

.. folio:: 0022
   :page: p. 6

On page 6, Lemoine completes the ten fundamental operations with segment transfer (including :math:`n`-fold stepping), the arbitrary circle through two points, and the equidistant point primitive:

**Application VIII — Lay Off a Given Length :math:`AB` on a Traced Line.**

* From an *indeterminate* point of the traced line: capture :math:`AB` (:math:`2C_1`), set one leg on the line (:math:`C_2`), and mark the endpoint by an arc (:math:`C_3`):

.. math::

   \mathrm{Op.} : \left(2C_1 + C_2 + C_3\right), \qquad S = 4, \quad E = 3 \quad (0\text{ lines}, 1\text{ circle}).

* From a *determined* point :math:`M` on the traced line: capture :math:`AB` (:math:`2C_1`), set the pivot at :math:`M` (:math:`C_1`), and sweep :math:`M(AB)` (:math:`C_3`): :math:`3C_1 + C_3` (:math:`S = 4, E = 3`).
* **Remark on :math:`n`-fold Stepping**: To step a length :math:`AB` :math:`n` consecutive times along a traced line *without marking intermediate arcs* (merely pivoting the divider compass along the line) costs :math:`(n + 2)C_1 + C_2` (or :math:`(n + 2)C_1` from a fixed origin); if each intermediate division is marked with a small arc, the symbol becomes :math:`(n + 1)C_1 + C_2 + nC_3`. Here Lemoine contrasts the modern divider compass (:math:`S = 4`) directly against :person:`Euclid <euclid>`'s collapsing-compass transfer in *Elements* I.2–I.3 (:math:`S = 16`, :ref:`concordance-transfer-segment`).

**Application IX — Trace an Arbitrary Circle Passing Through Two Given Points :math:`A` and :math:`B`.**

To locate an arbitrary center equidistant from :math:`A` and :math:`B` without drawing the perpendicular bisector, sweep two equal-radius arcs :math:`A(R)` and :math:`B(R)` (:math:`2C_1 + 2C_3`) meeting at :math:`O`, then sweep :math:`O(R)` (:math:`C_1 + C_3`) with the **same unaltered aperture** :math:`R`:

.. math::

   \mathrm{Op.} : \left(3C_1 + 3C_3\right), \qquad S = 6, \quad E = 3 \quad (0\text{ lines}, 3\text{ circles}).

**Application X — Place a Point :math:`C` Equidistant from Two Given Points :math:`A` and :math:`B`.**

Sweep two equal-radius arcs :math:`A(R)` and :math:`B(R)` with arbitrary sufficient radius :math:`R > AB/2`; either intersection is :math:`C`:

.. math::

   \mathrm{Op.} : \left(2C_1 + 2C_3\right), \qquad S = 4, \quad E = 2 \quad (0\text{ lines}, 2\text{ circles}).

If :math:`C` must lie at a *prescribed* distance :math:`l` from both :math:`A` and :math:`B`, capturing :math:`l` adds :math:`2C_1`, yielding :math:`4C_1 + 2C_3` (:math:`S = 6, E = 4`).
