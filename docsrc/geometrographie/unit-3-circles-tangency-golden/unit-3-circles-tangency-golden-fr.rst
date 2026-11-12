:layout: book

.. _geometrographie-unit-3-fr:

Unité III : Cercles, tangentes, section d'or, géométrie projective et géométrie moderne du triangle
===================================================================================================

.. rubric:: Émile Lemoine — *Géométrographie, ou Art des constructions géométriques* (Texte français, Problèmes XXI et XXV–LXIII, pp. 12–51)

.. contents:: Dans cette unité
   :local:
   :depth: 2
   :backlinks: none

.. _lemoine-fr-circles-tangents-incircle:

.. folio:: Problèmes XXI, XXV–XXVII
   :page: 15

§ 1. Cercle circonscrit (XXI), tangentes au cercle (XXV–XXVI) et cercle inscrit :math:`X(1)` (XXVII)
----------------------------------------------------------------------------------------------------

**Problème XXI (Euclide IV.5 — Cercle circonscrit et centre :math:`X(3)`).** En décrivant d'abord :math:`B(R)` d'un rayon arbitraire suffisant (:math:`C_1 + C_3`), puis :math:`A(R)` et :math:`C(R)` (:math:`2C_1 + 2C_3`), un même cercle auxiliaire sert aux deux médiatrices (:math:`4R_1 + 2R_2`), d'où le centre :math:`O = X(3)` et le cercle :math:`O(A)` (:math:`2C_1 + C_3`) :

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 5C_1 + 4C_3\right), \qquad S = 15, \quad E = 9 \quad (2\text{ droites}, 4\text{ cercles}).

**Problème XXVI (Euclide III.17 — Tangentes menées d'un point extérieur :g:`A` à un cercle :g:`O(R)`).** La construction d':person:`Euclide <euclid>` demande :math:`8R_1 + 4R_2 + 4C_1 + 3C_3` (:math:`S = 19`). :person:`Lemoine <lemoine>` abaisse la simplicité à :math:`S = 18`, soit par :math:`5R_1 + 3R_2 + 7C_1 + 3C_3`, soit par le cercle :g:`M(MO)` de diamètre :g:`OA` coupant :g:`O(R)` en :g:`T` et :g:`T'` le long de la polaire :g:`TT'`, d'où les tangentes :g:`AT` et :g:`AT'` (:math:`5R_1 + 3R_2 + 6C_1 + 4C_3`, :math:`S = 18, E = 11`).

.. picture:: /_static/figures/fig_circle_tangents.svg

**Problème XXVII (Euclide IV.4 — Cercle inscrit et centre :g:`I` :math:`= X(1)`).** La construction classique trace deux bissectrices et abaisse la perpendiculaire complète de :g:`I` sur :g:`BC`, soit :math:`6R_1 + 3R_2 + 11C_1 + 10C_3` (:math:`S = 30, E = 17`, 3 droites, 10 cercles). En conservant la même ouverture aux sommets :g:`B`, :g:`C` pour mener :g:`BI` et :g:`CI` et en déterminant le rayon de contact :g:`ID` sans tracer de troisième droite avant de décrire :g:`I(ID)`, Lemoine économise sept opérations et quatre cercles :

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 11C_1 + 6C_3\right), \qquad S = 23, \quad E = 15 \quad (2\text{ droites}, 6\text{ cercles}).

.. picture:: /_static/figures/fig_incircle_lemoine.svg

.. _lemoine-fr-proportions-golden:

.. folio:: Problèmes XXXIII–XXXVI
   :page: 24

§ 2. Lignes proportionnelles (XXXIII–XXXV) et division en moyenne et extrême raison (XXXVI)
-------------------------------------------------------------------------------------------

* **Quatrième et troisième proportionnelles (XXXIII–XXXIV)** : :math:`x = bc/a` en :math:`2R_1 + 2R_2 + 11C_1 + C_2 + 6C_3` (:math:`S = 22`) ; :math:`x = b^2/a` en :math:`4R_1 + 2R_2 + 5C_1 + C_2 + 3C_3` (:math:`S = 15`).
* **Moyenne proportionnelle :math:`\sqrt{ab}` (XXXV — construction de Lemoine et :person:`Gouzy <gouzy>`)** : :math:`\mathrm{Op.} : (2R_1 + 2R_2 + 6C_1 + C_2 + 3C_3)`, :math:`S = 14, E = 9` (2 droites, 3 cercles, contre :math:`S = 24`, 6 cercles dans le tracé classique).

**Problème XXXVI (Euclide II.11 / VI.30 — :term:`Moyenne et extrême raison <moyenne-et-extreme-raison>` :math:`\phi`).** Au lieu des trois droites classiques (:math:`S = 25`), Lemoine ne trace **qu'une seule ligne droite** : la médiatrice :g:`MC` de :g:`AB` (:math:`2R_1 + R_2`), qui fournit simultanément le milieu :g:`M` (:math:`MB = AB/2`) et la perpendiculaire sur laquelle le cercle :math:`M(AB)` marque :g:`C` (:math:`MC = AB`). Sans tracer l'hypoténuse :g:`BC` (:math:`= \frac{\sqrt{5}}{2} AB`), le cercle :math:`B(C)` marque sur la droite prolongée le point :g:`E` tel que :math:`ME = AB/\phi`, et l'arc :g:`A(ME)` donne le point d'or :g:`X` (:g:`AX` :math:`= AB/\phi`) :

.. math::

   \mathrm{Op.} : \left(2R_1 + R_2 + 9C_1 + 6C_3\right), \qquad S = 18, \quad E = 11 \quad (1\text{ droite}, 6\text{ cercles}).

.. picture:: /_static/figures/fig_golden_section_lemoine.svg

.. _lemoine-fr-projective-inversive:

.. folio:: Problèmes XXXVIII–XLVII
   :page: 29

§ 3. Inversion au compas seul (XXXVIII), polaire à la règle seule (XXXIX), axe radical (XLI) et conjugué harmonique (XLVI)
--------------------------------------------------------------------------------------------------------------------------

* **Problème XXXVIII (:term:`Inversion <inversion>` — compas seul lorsque :math:`OA > R/2`)** : Tracer :math:`A(O)` coupant :math:`O(R)` en :math:`M, N`, puis :math:`M(O)` et :math:`N(O)` se recoupant en :math:`A'` : :math:`\mathrm{Op.} : (5C_1 + 3C_3)`, :math:`S = 8, E = 5` (**0 droite, 3 cercles**).
* **Problème XXXIX (:term:`Polaire d'un point <polaire>` — règle seule)** : Par le quadrilatère complet inscrit dans le cercle tracé :math:`O`, :math:`\mathrm{Op.} : (12R_1 + 7R_2)`, :math:`S = 19, E = 12` (**7 droites, 0 cercle**).
* **Problème XLI (:term:`Axe radical <linie-der-gleichen-potenzen>` de deux cercles non sécants)** : Deux cercles auxiliaires quelconques (:math:`2C_3`) coupant les deux cercles donnés fournissent deux centres radicaux par simples droites concourantes : :math:`\mathrm{Op.} : (10R_1 + 5R_2 + 2C_3)`, :math:`S = 17, E = 10` — alors que la construction classique par les tangentes communes défendue par :person:`Amédée Mannheim <mannheim>` (pp. 57–58) exigeait :math:`18R_1 + 9R_2 + 19C_1 + 12C_3` (:math:`S = 58`) !
* **Problème XLVI (:term:`Conjugué harmonique <conjugue-harmonique>` — règle seule)** : Par le quadrilatère complet de :person:`Pappus <pappus>`, :math:`\mathrm{Op.} : (9R_1 + 6R_2)`, :math:`S = 15, E = 9` (**6 droites, 0 cercle**).
* **Problème XLVII (Carré sur :math:`AB`, construction d':person:`Eugène Catalan <catalan>`)** : :math:`\mathrm{Op.} : (6R_1 + 3R_2 + 6C_1 + 4C_3)`, :math:`S = 19, E = 12`.

.. _lemoine-fr-triangle-centers:

.. folio:: Problèmes L–LXIII
   :page: 42

§ 4. Géométrie du triangle : point de Lemoine :math:`X(6)`, points de Brocard et centres remarquables
-----------------------------------------------------------------------------------------------------

* **Problème L — Centre de gravité :g:`G` :math:`= X(2)`** : :math:`\mathrm{Op.} : (6R_1 + 3R_2 + 6C_1 + 2C_3)`, :math:`S = 17, E = 12` (3 droites, 2 cercles).
* **Problème LI — :term:`Point de Lemoine <point-de-lemoine>` :g:`K` :math:`= X(6)`** (:cite:`lemoine-1873`) : Tandis que la construction générale par coordonnées normales (XLIX) demande :math:`S = 54`, la bissection directe d'une :term:`antiparallèle <antiparallele>` :g:`PaQa` à :g:`BC` permet de ne tracer que les deux symédianes :g:`AK` et :g:`BK` :

.. math::

   \mathrm{Op.} : \left(4R_1 + 2R_2 + 13C_1 + 8C_3\right), \qquad S = 27, \quad E = 17 \quad (2\text{ droites}, 8\text{ cercles}).

.. picture:: /_static/figures/fig_lemoine_symmedian_x6.svg

* **Problèmes LII–LV — :term:`Droite de Lemoine <droite-de-lemoine>` (:math:`S = 19`), couple :math:`(G, K)` (:math:`S = 32`) et :term:`points de Brocard <points-de-brocard>` :math:`\omega, \omega'`** : Un point de Brocard en :math:`8R_1 + 4R_2 + 10C_1 + 6C_3` (:math:`S = 28`) ; les deux points simultanément en :math:`12R_1 + 6R_2 + 12C_1 + 8C_3` (:math:`S = 38`, contre :math:`S = 74` dans la lettre d':person:`Henri Brocard <brocard>`, pp. 58–59).
* **Problèmes LVI–LXIII** : Point de :person:`Steiner <steiner>` :math:`X(99)` (:math:`S = 24`), point de :person:`Tarry <tarry>` :math:`X(98)` (:math:`S = 28`), point de :person:`Gergonne <gergonne>` :math:`X(7)` (:math:`S = 27`), centre de :person:`Spieker <spieker>` :math:`X(10)` (:math:`S = 29`), point de :person:`Nagel <nagel>` :math:`X(8)` (:math:`4R_1 + 2R_2 + 7C_1 + 3C_3, S = 16`), point :math:`\Phi` de :person:`Neuberg <neuberg>` (:math:`S = 37`) et point :math:`W` (:math:`S = 62` au lieu de :math:`148`).
