:layout: book
:canonical_id: Probs. XIX–XX
:order: 4
:folio: 0026
:tracks: English: 08_diameter_perpendiculars_xix_xx-en | French: 08_diameter_perpendiculars_xix_xx-fr | Summary: 08_diameter_perpendiculars_xix_xx-summary | Notes: 08_diameter_perpendiculars_xix_xx-notes

.. _lemoine-08_diameter_perpendiculars_xix_xx-en:
.. _lemoine-en-perpendiculars-bisector:

Problems XIX–XX: Circle Center & Perpendiculars
===============================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 10–12, fols. ``0026–0028``)

.. folio:: 0026
   :page: p. 10

**Problem XIX (Euclid III.1 — Locate the Center of a Traced Circle).**
Pick three arbitrary points :math:`A, B, C` on the circumference (:math:`3C_2`) and sweep three circles of one *shared* sufficient radius :math:`R` (:math:`3C_3`); the two common chords joining the pairwise intersections of :math:`A(R), B(R)` and :math:`B(R), C(R)` (:math:`4R_1 + 2R_2`) meet at the exact center :math:`O`:

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 3C_2 + 3C_3\right), \qquad S = 12, \quad E = 7 \quad (2\text{ lines}, 3\text{ circles}).

**Problem XX (Euclid I.12 & I.11 — Perpendicular Through a Given Point :g:`A` to Traced Line :g:`BC`).**

1. **Case 1 — Point :g:`A` Outside Traced Line :g:`BC` (Euclid I.12)**:
   * *Classical Method (a)*: Sweep a circle centered at :g:`A` cutting :g:`BC` in two points and bisect the intercepted chord (:math:`2R_1 + R_2 + 3C_1 + C_2 + 3C_3`, :math:`S = 10, E = 6`, 1 line, 3 circles—or :math:`2R_1 + R_2 + 3C_1 + 3C_3`, :math:`S = 9, E = 5` if the radius is kept equal).

   .. folio:: 0027
      :page: p. 11

   * *Lemoine Reflection Method (b)*: From an indeterminate point :g:`B` on :g:`BC`, sweep :math:`B(BA)` (:math:`C_1 + C_2 + C_3`) cutting :g:`BC` at :g:`C`. Take :math:`CA` and sweep :math:`C(CA)` (:math:`2C_1 + C_3`) cutting :math:`B(BA)` at the mirror point :g:`A'`, and join :g:`AA'` (:math:`2R_1 + R_2`):

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 3C_1 + C_2 + 2C_3\right), \qquad S = 9, \quad E = 6 \quad (1\text{ line}, 2\text{ circles}).

2. **Case 2 — Point :g:`A` Lying On Traced Line :g:`BC` (Euclid I.11 via Thales's Circle III.31, :math:`S = 8`!)**:
   Classical textbooks treat erecting a perpendicular at an endpoint of a segment as a special trick; Lemoine proves it is strictly *simpler* than the general textbook method (:math:`S = 9` or :math:`10`) and should **always** replace it! Place one compass leg on :g:`A` (:math:`C_1`) and pivot freely at an arbitrary point :g:`O` off :g:`BC` (:math:`0` cost!) to sweep the **single circle** :g:`O(OA)` (:math:`C_3`), cutting :g:`BC` again at :g:`B`. Draw diameter :g:`BD` through :g:`B` and :g:`O` (:math:`2R_1 + R_2`) meeting :g:`O(OA)` at :g:`D`, and join :g:`AD` (:math:`2R_1 + R_2`):

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + C_1 + C_3\right), \qquad S = 8, \quad E = 5 \quad (2\text{ lines}, 1\text{ circle}).

.. picture:: /_static/figures/fig_perpendicular_external.svg
   :alt: Lemoine Problem XX perpendiculars: reflection method (S = 9) and Thales single-circle method (S = 8)
   :caption: Problem XX: External perpendicular via compass reflection AA' (S = 9, 2 circles) and boundary perpendicular AD via Thales's single circle O(OA) (S = 8, 1 circle).

.. folio:: 0028
   :page: p. 12

**Special Corollaries (pp. 11–12).**

* *Arbitrary perpendicular* to traced :math:`AB`: either Thales's circle (:math:`4R_1 + 2R_2 + C_3`, :math:`S = 7, E = 4`, 2 lines, 1 circle) or two arbitrary circles centered on :math:`AB` (:math:`2R_1 + R_2 + 2C_2 + 2C_3`, :math:`S = 7, E = 4`, 1 line, 2 circles).
* *Perpendicular from external :math:`C` to an un-traced line* given by points :math:`A, B`: sweep :math:`A(AC)` and :math:`B(BC)` and join their intersections (:math:`2R_1 + R_2 + 4C_1 + 2C_3`, :math:`S = 9, E = 6`, 1 line, 2 circles).
