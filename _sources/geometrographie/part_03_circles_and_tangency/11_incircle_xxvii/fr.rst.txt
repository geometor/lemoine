:type: fr
:layout: book
:canonical_id: Prob. XXVII
:order: 1
:folio: 0031

.. _lemoine-11_incircle_xxvii-fr:
.. _geometrographie-part-03-fr:
.. _geometrographie-unit-3-fr:
.. _lemoine-fr-circles-tangents-incircle:

Problème XXVII : Inscrire un cercle dans un triangle donné ABC
==============================================================

.. folio:: 0031
   :page: p. 15

**XXVII.** — *Inscrire un cercle dans un triangle donné ABC.*

Qu'il s'agisse d'un cercle inscrit ou d'un cercle ex-inscrit, la méthode classique par les bissectrices des angles du triangle
conduit au symbole :

:math:`\mathrm{Op.} : (6R_1 + 3R_2 + 11C_1 + 10C_3)` ; simplicité 30 ; exactitude 17 ; 3 droites, 10 cercles.

Si l'on voulait tracer les trois autres cercles tangents, on aurait en plus à ajouter : :math:`\mathrm{op.} : (12R_1 + 6R_2 + 16C_1 + 13C_3)`.
En tout, par conséquent :

:math:`\mathrm{Op.} : (18R_1 + 9R_2 + 27C_1 + 23C_3)` ; simplicité 77 ; exactitude 45 ; 18 droites, 23 cercles.

Voici une solution plus simple, mais qui ne se présenterait certes point à l'esprit si l'on ne dirigeait point l'attention
vers la recherche systématique de la simplicité de la construction (*fig. 1*).

.. container:: lemoine-plate-pair

   .. picture:: 0031.g1.png
      :alt: Gravure originale FIG. 1 (1893, fol. 0031) du Problème XXVII : cercle inscrit d'un triangle ABC
      :caption: FIG. 1 — Fac-similé d'archives (Paris 1893, fol. 0031, p. 15) : construction géométrographique du cercle inscrit.

   .. picture:: 0031.g1.svg
      :alt: Vectorisation interactive calibrée de la FIG. 1 (Problème XXVII, cercle inscrit du triangle ABC)
      :caption: FIG. 1 — Vectorisation calibrée : demi-périmètre DE = 2(s − a), médiatrices OR, OQ et cercle inscrit O(OR) (S = 23).

J'appelle :g:`P`, :g:`Q`, :g:`R` les points de contact du cercle inscrit sur :g:`BC`, :g:`CA`, :g:`AB` et :g:`O` le centre de ce cercle.

Sur :g:`BA`, dans le sens :g:`BA`, je prends :math:`AD = AC` ; sur :g:`BA`, dans le sens :g:`BA`, je prends :math:`BE = BC` — :math:`\mathrm{op.} : (4C_1 + 2C_3)`.

Je décris :g:`A(DE)` qui coupe :g:`AB` en :g:`R'` (:g:`R'` est dans le sens :g:`AB`), et :g:`AC` en :g:`Q'` (:g:`Q'` est dans le sens :g:`AC`) — :math:`\mathrm{op.} : (3C_1 + C_3)` ;
il est évident que :math:`AR = AQ = \frac{b + c - a}{2}` et que, par suite, :g:`R` et :g:`Q` sont les milieux de :math:`AR'` et de :math:`AQ'` ; :g:`O` est donc le centre du cercle circonscrit au triangle :math:`AQ'R'`.

Je trace :math:`R'(DE)` qui coupe :g:`A(DE)` en deux points ; en joignant ces points, j'ai un lieu de :g:`O` — :math:`\mathrm{op.} : (2R_1 + R_2 + C_1 + C_3)`.

Je trace :math:`Q'(DE)` qui coupe :g:`A(DE)` en deux points ; en joignant ces points, j'ai un autre lieu de :g:`O` — :math:`\mathrm{op.} : (2R_1 + R_2 + C_1 + C_3)`.

Je décris :g:`O(OR)` qui est le cercle cherché — :math:`\mathrm{op.} : (2C_1 + C_3)`.

:math:`\mathrm{Op.} : (4R_1 + 2R_2 + 11C_1 + 6C_3)` ; simplicité 23 ; exactitude 15 ; 2 droites, 6 cercles.

En appliquant la *transformation continue* (voir *A. F.*, Congrès de Marseille, 1891), on arrive immédiatement à la construction qu'il faudrait faire
pour tracer un cercle ex-inscrit ; elle a le même symbole que celle du tracé du cercle inscrit.

.. folio:: 0032
   :page: p. 16

Si l'on veut tracer les quatre cercles tangents, il vaut mieux commencer par les trois cercles ex-inscrits et finir par le cercle inscrit en joignant :math:`AO_a`, :math:`BO_b`, etc.

On a :

:math:`\mathrm{Op.} : (18R_1 + 9R_2 + 26C_1 + 13C_3)` ; simplicité 66 ; exactitude 44 ; 9 droites, 13 cercles.

.. picture:: /_static/figures/fig_incircle_lemoine.svg
   :alt: Schéma explicatif comparant la construction de Lemoine (S = 23) à la méthode classique (S = 30)
   :caption: Schéma comparatif complémentaire : centre inscrit X(1) et économie de 4 cercles par rapport au tracé classique (S = 30 → 23).
