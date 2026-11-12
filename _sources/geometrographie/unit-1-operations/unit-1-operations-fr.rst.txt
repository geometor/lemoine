:layout: book

.. _geometrographie-unit-1-fr:

Unité I : Genèse historique, principes méthodologiques et les cinq opérations élémentaires
==========================================================================================

.. rubric:: Émile Lemoine — *Géométrographie, ou Art des constructions géométriques* (Texte français de référence, 1892 / *Scientia* n° 18, 1902, pp. 1–5 et 52–65)

.. contents:: Dans cette unité
   :local:
   :depth: 2
   :backlinks: none

.. _lemoine-fr-genesis:

.. folio:: Préliminaires
   :page: 1

§ 1. But de la *Géométrographie* : constructions spéculatives et constructions géométrographiques
-------------------------------------------------------------------------------------------------

Depuis :person:`Euclide <euclid>` (:cite:`euclid-heath`), les géomètres ont toujours attaché le plus grand prix à la simplicité dans la démonstration des théorèmes, mais ils n'ont jamais cherché à définir ni à mesurer avec précision la simplicité dans l'exécution effective des constructions géométriques. Les constructions données dans les traités classiques sont presque toutes des :term:`constructions spéculatives <construction-speculative>` : l'auteur ramène le problème proposé à un problème déjà résolu afin d'abréger le discours et la démonstration, sans se préoccuper du nombre réel de droites et de cercles qu'il faudrait tracer si l'on prenait effectivement la règle et le compas sur la feuille de dessin.

La :term:`Géométrographie <geometrographie>`, esquissée par :person:`Émile Lemoine <lemoine>` au Congrès d'Oran de l'*Association Française pour l'Avancement des Sciences* le 30 mars 1888 (:cite:`lemoine-1888`), constituée dans son mémoire fondamental du Congrès de Pau en 1892 (:cite:`lemoine-1892`) et exposée dans sa forme définitive au n° 18 de la collection *Scientia* (:cite:`lemoine-1902`), a pour double objet :

1. D'évaluer d'une manière rigoureuse et numérique la **simplicité** et l'**exactitude** de toute construction géométrique ;
2. De substituer aux constructions spéculatives habituelles des constructions véritablement *géométrographiques*, réduisant au minimum le travail opératoire de l'exécutant.

.. _lemoine-fr-ideal-postulates:

.. folio:: Conventions fondamentales
   :page: 2

§ 2. Conventions sur la feuille et les instruments
--------------------------------------------------

Pour dégager la complexité intrinsèque d'un tracé des accidents matériels d'une épure particulière, :person:`Lemoine <lemoine>` pose les conventions suivantes (pp. 2, 52–54) :

* **Feuille illimitée** : On suppose toujours la feuille de dessin indéfinie dans tous les sens ; les problèmes où les limites de la feuille interdisent certains points de concours appartiennent à une branche spéciale du dessin géométrique et non à la Géométrographie générale.
* **Règle illimitée et compas moderne à ouverture persistante** : La règle permet de tracer d'un seul trait une droite aussi longue qu'il est nécessaire ; le compas conserve son ouverture lorsqu'on le soulève de la feuille, et l'on peut se servir de la règle tout en gardant au compas le rayon précédemment ouvert.
* **Séparation de l'exactitude théorique et des erreurs physiques** : Comme le précise la discussion avec :person:`Amédée Mannheim <mannheim>` (pp. 57–58) et :person:`Maurice d'Ocagne <docagne>` (pp. 60–62), le géomètre grec traçait à main levée sur le sable des figures schématiques destinées au raisonnement ; le dessinateur moderne aligne des instruments réels où chaque mise en coïncidence comporte une incertitude visuelle élémentaire.

.. _lemoine-fr-five-operations:

.. folio:: Les cinq opérations
   :page: 3

§ 3. Les cinq opérations élémentaires de la règle et du compas
--------------------------------------------------------------

Toute construction exécutée avec la règle et le compas se décompose intégralement dans les cinq opérations élémentaires suivantes :

* :term:`R₁ <r1>` — **Mettre le bord de la règle en coïncidence avec un point placé** (:math:`\mathrm{op.} : R_1`). Faire passer le bord de la règle par deux points déterminés :g:`A` et :g:`B` exige deux mises en coïncidence et compte toujours pour :math:`2R_1`.
* :term:`R₂ <r2>` — **Tracer la ligne droite suivant le bord de la règle** (:math:`\mathrm{op.} : R_2`).
* :term:`C₁ <c1>` — **Mettre une pointe du compas en un point déterminé** (:math:`\mathrm{op.} : C_1`). Prendre avec le compas la distance :g:`AB` de deux points placés compte pour :math:`2C_1`. Si l'on fait aussitôt tourner le compas autour de l'une des pointes restée fixe en :g:`A` ou en :g:`B`, on n'ajoute aucun :math:`C_1` ; si l'on transporte au contraire la pointe sèche en un troisième point déterminé :g:`O`, cette pose ajoute :math:`C_1` (soit :math:`3C_1`).
* :term:`C₂ <c2>` — **Mettre une pointe du compas en un point indéterminé d'une ligne (droite ou cercle) déjà tracée** (:math:`\mathrm{op.} : C_2`). Poser une pointe en un point entièrement arbitraire du plan hors de toute ligne tracée ne coûte aucune opération de mise en coïncidence (:math:`0`).
* :term:`C₃ <c3>` — **Tracer le cercle (ou l'arc de cercle utile)** (:math:`\mathrm{op.} : C_3`).

.. picture:: /_static/figures/fig_elementary_operations.svg

Suivant la :term:`notation abrégée de Lemoine <cercle-o-ab>`, :g:`O(AB)` désigne le cercle de centre :g:`O` et de rayon égal à :g:`AB`, tandis que :math:`O(A)` (ou :math:`O(R)`) désigne le cercle de centre :g:`O` passant par le point :g:`A` (ou de rayon donné :math:`R`).

.. _lemoine-fr-symbol-coefficients:

§ 4. Symbole opératoire, coefficient de simplicité (:math:`S`) et coefficient d'exactitude (:math:`E`)
------------------------------------------------------------------------------------------------------

Lorsque l'exécution d'une construction demande :math:`l_1` fois :math:`R_1`, :math:`l_2` fois :math:`R_2`, :math:`m_1` fois :math:`C_1`, :math:`m_2` fois :math:`C_2` et :math:`m_3` fois :math:`C_3`, son **symbole géométrographique** s'écrit :

.. math::

   \mathrm{Op.} : \left(l_1 R_1 + l_2 R_2 + m_1 C_1 + m_2 C_2 + m_3 C_3\right).

On en déduit quatre nombres caractéristiques :

* Le :term:`coefficient de simplicité <simplicite>` : :math:`S = l_1 + l_2 + m_1 + m_2 + m_3` ;
* Le :term:`coefficient d'exactitude <exactitude>` : :math:`E = l_1 + m_1 + m_2` (somme des opérations préparatoires de pointé) ;
* Le **nombre des droites tracées** : :math:`l_2` ;
* Le **nombre des cercles tracés** : :math:`m_3`.

.. _lemoine-fr-fundamental-table:

.. folio:: Opérations I–X
   :page: 4

§ 5. Opérations fondamentales (I–X) et abandon de la notation d'Oran
--------------------------------------------------------------------

* **I.** Tracer une droite quelconque : :math:`\mathrm{Op.} : (R_2)` ; :math:`S = 1, E = 0` ; 1 droite.
* **II.** Tracer une droite passant par un point donné :math:`A` : :math:`\mathrm{Op.} : (R_1 + R_2)` ; :math:`S = 2, E = 1` ; 1 droite.
* **III.** Tracer la droite joignant deux points donnés :g:`A` et :g:`B` : :math:`\mathrm{Op.} : (2R_1 + R_2)` ; :math:`S = 3, E = 2` ; 1 droite.
* **IV.** Tracer un cercle quelconque : :math:`\mathrm{Op.} : (C_3)` ; :math:`S = 1, E = 0` ; 1 cercle.
* **V.** Tracer un cercle de rayon quelconque autour d'un centre donné :g:`O` : :math:`\mathrm{Op.} : (C_1 + C_3)` ; :math:`S = 2, E = 1` ; 1 cercle.
* **VI.** Tracer d'un centre quelconque un cercle de rayon donné :g:`AB` : :math:`\mathrm{Op.} : (2C_1 + C_3)` ; :math:`S = 3, E = 2` ; 1 cercle.
* **VII.** Tracer le cercle :math:`O(A)` de centre donné :math:`O` passant par un point donné :math:`A` : :math:`\mathrm{Op.} : (2C_1 + C_3)` ; :math:`S = 3, E = 2` ; 1 cercle.
* **VIII.** Porter sur une droite tracée une longueur donnée :g:`AB` : à partir d'un point indéterminé :g:`M` de cette droite, :math:`\mathrm{Op.} : (2C_1 + C_2 + C_3)`, :math:`S = 4, E = 3` ; à partir d'un point déterminé de la droite, :math:`\mathrm{Op.} : (3C_1 + C_3)`, :math:`S = 4, E = 3`.
* **IX–X.** Porter la somme ou la différence de deux longueurs sur une droite tracée : :math:`\mathrm{Op.} : (4C_1 + C_2 + 2C_3)` ; :math:`S = 7, E = 5` ; 2 cercles.

Aux pages 55–56, :person:`Lemoine <lemoine>` rappelle qu'à Oran (:cite:`lemoine-1888`) il avait d'abord distingué huit opérations (:math:`\rho_1, \rho_2, \rho_3, \gamma_1, \gamma'_1, \gamma''_1, \gamma_2, \gamma'_2`) avant de reconnaître que la réduction aux cinq symboles :math:`R_1, R_2, C_1, C_2, C_3` assure une invariabilité absolue du décompte d'un géomètre à l'autre.
