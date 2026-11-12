:layout: book

.. _geometrographie-unit-2-fr:

Unité II : Constructions fondamentales d'Euclide — Tracé spéculatif et tracé géométrographique
==============================================================================================

.. rubric:: Émile Lemoine — *Géométrographie, ou Art des constructions géométriques* (Texte français, Problèmes XI–XXIV, pp. 6–14)

.. contents:: Dans cette unité
   :local:
   :depth: 2
   :backlinks: none

.. _lemoine-fr-copy-angle-triangles:

.. folio:: Problèmes XI–XVI
   :page: 6

§ 1. Report d'un angle (XI) et construction des triangles (XII–XVI)
-------------------------------------------------------------------

**Problème XI (Euclide I.23).** *Sur une droite tracée, construire en un point donné* :math:`A` *un angle égal à un angle donné* :math:`O`.
La réduction spéculative d':person:`Euclide <euclid>` (:cite:`euclid-heath`) joint deux points sur les côtés de l'angle :math:`O` pour ramener le problème à la construction d'un triangle (I.22), ce qui exige :math:`4R_1 + 2R_2 + 8C_1 + C_2 + 4C_3` (:math:`S = 19, E = 13`). En traçant de :math:`O` puis de :math:`A` deux arcs d'un même rayon arbitraire (:math:`2C_1 + 2C_3`), en prenant la corde interceptée (:math:`2C_1`), en la reportant (:math:`C_1 + C_3`) et en joignant :math:`A` au point obtenu (:math:`2R_1 + R_2`), on obtient :

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 5C_1 + 3C_3\right), \qquad S = 11, \quad E = 7 \quad (1\text{ droite}, 3\text{ cercles}).

**Problème XVI (Euclide I.22).** *Construire un triangle connaissant les trois côtés* :math:`a, b, c`.
En traçant d'abord une droite indéfinie quelconque (:math:`R_2`) au lieu de joindre deux points placés d'avance, on porte :math:`BC = a` (:math:`2C_1 + C_2 + C_3`), puis :math:`B(c)` et :math:`C(b)` (:math:`6C_1 + 2C_3`) se coupant en :math:`A`, et l'on trace :math:`AB` et :math:`AC` (:math:`4R_1 + 2R_2`) :

.. math::

   \mathrm{Op.} : \left(4R_1 + 3R_2 + 8C_1 + C_2 + 3C_3\right), \qquad S = 19, \quad E = 13 \quad (3\text{ droites}, 3\text{ cercles}).

.. _lemoine-fr-parallel-tarry:

.. folio:: Problème XVII
   :page: 8

§ 2. Parallèle par un point extérieur (XVII) : les deux constructions de Gaston Tarry (:math:`S = 9`)
-----------------------------------------------------------------------------------------------------

**Problème XVII (Euclide I.31).** *Par un point donné* :g:`A` *hors d'une droite tracée* :g:`BC` *, mener une parallèle à* :g:`BC`.

* **Construction classique par l'angle alterne-interne** : :math:`\mathrm{Op.} : (2R_1 + R_2 + 5C_1 + 3C_3)` ; :math:`S = 11, E = 7` ; 1 droite, 3 cercles.
* **Première construction géométrographique de Gaston Tarry** (:person:`Gaston Tarry <tarry>`) : D'un centre arbitraire, tracer un cercle passant par :g:`A` (:math:`C_1 + C_3`) coupant :g:`BC` en deux points, et reporter l'arc avec le même rayon : :math:`\mathrm{Op.} : (2R_1 + R_2 + 4C_1 + 2C_3)` ; :math:`S = 9, E = 6` ; **1 droite, 2 cercles**.
* **Deuxième construction géométrographique de Gaston Tarry (par le losange d'ouverture unique)** : Avec un rayon arbitraire suffisant :math:`R`, tracer de :g:`A` un arc (:math:`C_1 + C_3`) coupant :g:`BC` en :g:`P` ; du même rayon :math:`R`, tracer :math:`P(R)` (:math:`C_1 + C_3`) coupant :g:`BC` en :g:`Q`, puis :math:`Q(R)` (:math:`C_1 + C_3`) coupant le premier arc :math:`A(R)` en :g:`D`. Le quadrilatère :g:`APQD` est un losange et la droite :g:`AD` (:math:`2R_1 + R_2`) est parallèle à :g:`BC` :

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 3C_1 + 3C_3\right), \qquad S = 9, \quad E = 5 \quad (1\text{ droite}, 3\text{ cercles}).

.. picture:: /_static/figures/fig_parallel_comparison.svg

.. _lemoine-fr-bisector-reflection:

.. folio:: Problèmes XVIII–XIX
   :page: 9

§ 3. Médiatrice et milieu d'un segment (XVIII) ; symétrique d'un point sans règle (XVIII *bis*)
-----------------------------------------------------------------------------------------------

**Problème XVIII (Euclide I.10).** *Tracer la perpendiculaire au milieu de la distance de deux points* :g:`A` *et* :g:`B` *, ou trouver le milieu* :g:`M` *d'une droite tracée* :g:`AB`.
En conservant une ouverture arbitraire commune :math:`R > AB/2` pour décrire :g:`A(R)` (:math:`C_1 + C_3`) et :g:`B(R)` (:math:`C_1 + C_3`) se coupant en :g:`P` et :g:`Q`, puis en traçant :g:`PQ` (:math:`2R_1 + R_2`) qui partage :g:`AB` en :g:`AM` et :g:`MB`, on évite de prendre :math:`AB` au compas :

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 2C_1 + 2C_3\right), \qquad S = 7, \quad E = 4 \quad (1\text{ droite}, 2\text{ cercles}).

.. picture:: /_static/figures/fig_perpendicular_bisector.svg

**Problème XVIII bis.** *Construire le symétrique* :math:`A'` *d'un point donné* :math:`A` *par rapport à une droite tracée* :math:`BC`.
De deux points quelconques pris sur :math:`BC` (:math:`2C_2`), décrire les deux cercles passant par :math:`A` (:math:`2C_1 + 2C_3`) ; leur second point commun est :math:`A'`, obtenu **sans tracer aucune droite** :

.. math::

   \mathrm{Op.} : \left(2C_1 + 2C_2 + 2C_3\right), \qquad S = 6, \quad E = 4 \quad (0\text{ droite}, 2\text{ cercles}).

.. _lemoine-fr-perpendiculars-bisector:

.. folio:: Problèmes XX–XXIV
   :page: 11

§ 4. Perpendiculaires (XX — cercle unique de Thalès :math:`S = 8`) et bissectrice d'un angle (XXII)
---------------------------------------------------------------------------------------------------

**Problème XX (Euclide I.12 et I.11).** *Mener par un point donné* :g:`A` *la perpendiculaire à une droite tracée* :g:`BC`.

1. **Premier cas — :g:`A` est hors de :g:`BC` (Euclide I.12)** : En construisant le symétrique :g:`A'` de :g:`A` par rapport à deux centres :g:`B`, :g:`C` sur la droite et en joignant :g:`AA'`, on obtient :math:`2R_1 + R_2 + 3C_1 + C_2 + 2C_3` (:math:`S = 9, E = 6`, 1 droite, 2 cercles).
2. **Second cas — :g:`A` est situé sur :g:`BC` (Euclide I.11 par le cercle de Thalès)** : Placer une pointe en :g:`A` (:math:`C_1`) et l'autre en un point quelconque :g:`O` pris hors de :g:`BC` (:math:`0`), décrire **l'unique cercle** :g:`O(OA)` (:math:`C_3`) qui recoupe :g:`BC` en :g:`B`, tracer le diamètre :g:`BD` par :g:`B` et :g:`O` (:math:`2R_1 + R_2`), puis joindre :g:`AD` (:math:`2R_1 + R_2`) :

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + C_1 + C_3\right), \qquad S = 8, \quad E = 5 \quad (2\text{ droites}, 1\text{ cercle}).

.. picture:: /_static/figures/fig_perpendicular_external.svg

**Problème XXII (Euclide I.9 — Bissectrice d'un angle).** En gardant la même ouverture suffisante pour l'arc décrit du sommet et pour les deux arcs décrits des points où il coupe les côtés, la bissectrice s'obtient par :math:`\mathrm{Op.} : (2R_1 + R_2 + 3C_1 + 3C_3)`, :math:`S = 9, E = 5` (1 droite, 3 cercles).
