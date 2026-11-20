:layout: book
:canonical_id: Exposition
:order: 2
:folio: 0019
:tracks: English: 02_five_operations-en | French: 02_five_operations-fr | Summary: 02_five_operations-summary | Notes: 02_five_operations-notes

.. _lemoine-02_five_operations-fr:
.. _lemoine-fr-five-operations:

Exposition : Les cinq opérations élémentaires et les coefficients S et E
========================================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (Texte français de référence, pp. 3–5, fols. ``0019–0021``)

.. folio:: 0019
   :page: p. 3

Toute construction plane exécutée à l'aide de la règle et du compas se ramène intégralement aux **cinq opérations élémentaires** suivantes :

* :term:`R₁ <r1>` — **Mettre le bord de la règle en coïncidence avec un point placé** (:math:`\mathrm{op.} : R_1`). Faire passer le bord de la règle par deux points déterminés :g:`A` et :g:`B` exige deux mises en coïncidence et compte toujours pour :math:`2R_1`.
* :term:`R₂ <r2>` — **Tracer la ligne droite suivant le bord de la règle** (:math:`\mathrm{op.} : R_2`).
* :term:`C₁ <c1>` — **Mettre une pointe du compas en un point déterminé** (:math:`\mathrm{op.} : C_1`). Prendre entre les branches du compas la longueur :g:`AB` de deux points placés compte pour :math:`2C_1`. Si l'on fait aussitôt tourner le compas autour de l'une des pointes restée fixe en :g:`A` ou en :g:`B`, on n'ajoute aucun :math:`C_1` ; si l'on transporte la pointe sèche en un troisième point déterminé :g:`O`, cette pose ajoute :math:`C_1` (soit :math:`3C_1`).
* :term:`C₂ <c2>` — **Mettre une pointe du compas en un point indéterminé d'une ligne (droite ou courbe) déjà tracée** (:math:`\mathrm{op.} : C_2`). Poser une pointe en un point arbitraire du plan hors de toute ligne tracée ne coûte aucune opération (:math:`0`).
* :term:`C₃ <c3>` — **Tracer le cercle (ou l'arc utile de circonférence)** (:math:`\mathrm{op.} : C_3`).

.. picture:: /_static/figures/fig_elementary_operations.svg
   :alt: Schéma des cinq opérations élémentaires R1, R2, C1, C2, C3 de la Géométrographie
   :caption: Les cinq opérations élémentaires de Lemoine : alignement et tracé à la règle (2R₁ + R₂, S = 3), notation abrégée O(AB) et report sur droite tracée (2C₁ + C₂ + C₃, S = 4).

Suivant la :term:`notation abrégée de Lemoine <cercle-o-ab>`, :g:`O(AB)` désigne le cercle de centre :g:`O` et de rayon égal à :g:`AB`, tandis que :math:`O(A)` ou :math:`O(R)` désigne le cercle de centre :g:`O` passant par le point :g:`A` ou de rayon :math:`R`.

.. _lemoine-fr-symbol-coefficients:

.. folio:: 0020
   :page: p. 4

Symbole opératoire, simplicité (:math:`S`) et exactitude (:math:`E`)
---------------------------------------------------------------------

Lorsqu'une construction exige :math:`l_1` fois :math:`R_1`, :math:`l_2` fois :math:`R_2`, :math:`m_1` fois :math:`C_1`, :math:`m_2` fois :math:`C_2` et :math:`m_3` fois :math:`C_3`, son **symbole géométrographique** s'écrit :

.. math::

   \mathrm{Op.} : \left(l_1 R_1 + l_2 R_2 + m_1 C_1 + m_2 C_2 + m_3 C_3\right).

On lit immédiatement quatre nombres caractéristiques :

* Le :term:`coefficient de simplicité <simplicite>` : :math:`S = l_1 + l_2 + m_1 + m_2 + m_3` ;
* Le :term:`coefficient d'exactitude <exactitude>` : :math:`E = l_1 + m_1 + m_2` (somme des opérations préparatoires de mise en coïncidence) ;
* Le **nombre de droites tracées** : :math:`l_2` ;
* Le **nombre de cercles tracés** : :math:`m_3`.

.. folio:: 0021
   :page: p. 5

Chaque mise en coïncidence (:math:`R_1, C_1, C_2`) introduisant une petite erreur de pointé, la construction la plus exacte est celle dont le coefficient :math:`E` est le plus *petit*. Lemoine précise enfin pourquoi il a remplacé sa première notation à huit symboles du Congrès d'Oran (:cite:`lemoine-1888`) par ce système définitif à cinq symboles, rigoureusement objectif et universellement reproductible.
