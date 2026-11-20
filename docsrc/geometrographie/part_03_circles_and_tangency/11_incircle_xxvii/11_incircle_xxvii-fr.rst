:layout: book
:canonical_id: Prob. XXVII
:order: 1
:folio: 0031
:tracks: English: 11_incircle_xxvii-en | French: 11_incircle_xxvii-fr | Summary: 11_incircle_xxvii-summary | Notes: 11_incircle_xxvii-notes

.. _lemoine-11_incircle_xxvii-fr:
.. _geometrographie-part-03-fr:
.. _geometrographie-unit-3-fr:
.. _lemoine-fr-circles-tangents-incircle:

Problème XXVII : Cercle inscrit et cercles exinscrits d'un triangle
===================================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (Texte français de référence, pp. 15–16, fols. ``0031–0032``)

.. folio:: 0031
   :page: p. 15

**Problème XXVII (Euclide IV.4 — Inscrire un cercle dans un triangle donné :g:`ABC`).**
La construction classique trace deux bissectrices et abaisse la perpendiculaire complète du centre :g:`O` sur un côté : :math:`6R_1 + 3R_2 + 11C_1 + 10C_3` (:math:`S = 30, E = 17`, 3 droites, 10 cercles).

Sur la **FIG. 1** (p. 15), :person:`Lemoine <lemoine>` économise **sept opérations et quatre cercles** en construisant directement :math:`DE = b + c - a = 2(s - a)` sur la droite prolongée :g:`BA` :

1. Tracer :g:`A(AC)` coupant :g:`BA` prolongée en :g:`D`, puis :g:`B(BC)` coupant :g:`BA` en :g:`E` (:math:`4C_1 + 2C_3`).
2. Prendre :math:`DE` et tracer :g:`A(DE)` coupant :g:`AB` en :g:`R'` et :g:`AC` en :g:`Q'` (:math:`3C_1 + C_3`), puis avec le même rayon :math:`R'(DE)` et :g:`Q'(DE)` (:math:`2C_1 + 2C_3`).
3. Tracer les médiatrices de :math:`AR'` et :math:`AQ'` (:math:`4R_1 + 2R_2`), qui passent par les points de contact :g:`R` et :g:`Q` et se coupent au centre inscrit :g:`O` (:math:`X(1)`), puis décrire :g:`O(OR)` (:math:`2C_1 + C_3`) tangent en :g:`P`, :g:`Q`, :g:`R` :

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 11C_1 + 6C_3\right), \qquad S = 23, \quad E = 15 \quad (2\text{ droites}, 6\text{ cercles}).

.. container:: lemoine-plate-pair

   .. picture:: 0031.g1.png
      :alt: Gravure originale FIG. 1 (1893, fol. 0031) du Problème XXVII : cercle inscrit d'un triangle ABC
      :caption: FIG. 1 — Fac-similé d'archives (Paris 1893, fol. 0031, p. 15) : construction géométrographique du cercle inscrit.

   .. picture:: 0031.g1.svg
      :alt: Vectorisation interactive calibrée de la FIG. 1 (Problème XXVII, cercle inscrit du triangle ABC)
      :caption: FIG. 1 — Vectorisation calibrée : demi-périmètre DE = 2(s − a), médiatrices OR, OQ et cercle inscrit O(OR) (S = 23).

.. folio:: 0032
   :page: p. 16

À la page 16, Lemoine étend la même économie de cercles au tracé d'un cercle exinscrit ainsi qu'à l'ensemble des quatre cercles tangents aux trois côtés du triangle.

.. picture:: /_static/figures/fig_incircle_lemoine.svg
   :alt: Schéma explicatif comparant la construction de Lemoine (S = 23) à la méthode classique (S = 30)
   :caption: Schéma comparatif complémentaire : centre inscrit X(1) et économie de 4 cercles par rapport au tracé classique (S = 30 → 23).
