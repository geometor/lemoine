:layout: book
:canonical_id: Exposition
:order: 2
:folio: 0019
:tracks: English: 02_five_operations-en | French: 02_five_operations-fr | Summary: 02_five_operations-summary | Notes: 02_five_operations-notes

.. _lemoine-02_five_operations-fr:
.. _lemoine-fr-five-operations:

Exposition de la théorie de la simplicité et de l'exactitude
============================================================

.. folio:: 0019
   :page: p. 3

Une construction exécutée avec la règle et le compas ne comporte que les opérations élémentaires suivantes :

* :term:`R₁ <r1>` — Mettre le bord de la règle en coïncidence avec un point :math:`\mathrm{op.} : (R_1)`.
* :term:`R₂ <r2>` — Tracer la ligne droite :math:`\mathrm{op.} : (R_2)`.
* :term:`C₁ <c1>` — Mettre une pointe du compas en un point déterminé :math:`\mathrm{op.} : (C_1)`.
* :term:`C₂ <c2>` — Mettre une pointe du compas en un point indéterminé d'une ligne :math:`\mathrm{op.} : (C_2)`.
* :term:`C₃ <c3>` — Tracer la circonférence :math:`\mathrm{op.} : (C_3)`.

(Op. : est l'abrégé du mot opération.)

.. picture:: /_static/figures/fig_elementary_operations.svg
   :alt: Schéma des cinq opérations élémentaires R1, R2, C1, C2, C3 de la Géométrographie
   :caption: Les cinq opérations élémentaires de Lemoine : alignement et tracé à la règle (2R₁ + R₂, S = 3), notation abrégée O(AB) et report sur droite tracée (2C₁ + C₂ + C₃, S = 4).

Nous ne tenons pas compte de la longueur *tracée* des lignes.

Si l'on trace, par exemple, un petit arc
ou le cercle entier, c'est toujours :math:`C_3` ; toujours :math:`R_2` pour une portion quelconque de droite tracée.

.. _lemoine-fr-symbol-coefficients:

Toute construction est donc finalement représentée par :

.. math::

   \mathrm{Op.} : \left(l_1 R_1 + l_2 R_2 + m_1 C_1 + m_2 C_2 + m_3 C_3\right).

Nous appelons *coefficient de simplicité*, ou plus brièvement *Simplicité de la construction*, le nombre
:math:`l_1 + l_2 + m_1 + m_2 + m_3`, et *coefficient d'exactitude*, ou plus brièvement *Exactitude de la construction*, le nombre
:math:`l_1 + m_1 + m_2`, parce que l'on voit facilement que, en réalité, l'exactitude dépend des opérations préparatoires
:math:`l_1, m_1, m_2` et non des opérations de tracé ; :math:`l_2` est le nombre de droites tracées, :math:`m_3` le nombre des cercles [*]_ .

Pour abréger l'écriture, au lieu d'écrire : la circonférence qui a :g:`O` pour centre, et la longueur :g:`AB`
ou la longueur :math:`R` pour rayon, nous écrirons : :g:`O(AB)` ou :math:`O(R)`.

Nous ferons ici une remarque importante
qui s'applique toutes les fois que la notion générale de *nombre* intervient dans un problème de *Géométrographie* ;
c'est que la question sort alors du domaine de la *Géométrographie* pure et qu'il s'y mêle de l'arithmologie,
comme on le verra dans la suite de ce travail. Ainsi : *Diviser une droite dans le rapport*
*de deux longueurs données* est un problème de *Géométrographie* pure, et : *Diviser une droite dans le rapport*
*de deux nombres* :math:`m` *et* :math:`n` *donnés* n'est point du tout dans le même cas ;
il n'y a même pas de méthode *générale* purement graphique pour faire le plus simplement possible cette

.. folio:: 0020
   :page: p. 4

division ; il faut étudier chaque cas particulier en ayant égard à la question qui a fourni ces nombres.
En pratique, on la ramène au cas des longueurs en prenant sur une règle divisée des longueurs proportionnelles aux nombres donnés,
et l'on doit faire le plus souvent ainsi, mais en sachant bien que l'on sort de la *Géométrographie* pure
qui n'autorise l'usage que de la règle et du compas. Pour ramener la question à la *Géométrographie* pure,
il faudrait porter sur une ligne :math:`m + n` fois une longueur quelconque, etc., et cela éloignerait trop
de la construction que l'on fait pratiquement. Encore, si porter :math:`m + n` fois une longueur sur une droite
de façon à marquer les divisions :math:`m` et :math:`m + n` est facile, quoique long et peu pratique,
il n'est nullement commode, peut-être pas possible, d'indiquer le moyen de marquer ces divisions *le plus simplement possible*
par une méthode générale. La question revient au problème : *Étant donnée une longueur, trouver une droite* :math:`m` *fois plus longue.*
Porter la longueur :math:`m` fois à la suite d'elle-même sur une droite est une solution, mais non la plus simple.
En étudiant le problème, on est conduit à une question d'arithmologie tout à fait analogue à la suivante, qui semble fort difficile :
*Combien faut-il effectuer de multiplications, au moins, pour calculer* :math:`A^m`, *le nombre* :math:`A` *étant donné ?*

La question de la multiplication de la droite par un nombre aurait, du reste, à la rigueur, exigé un nouveau symbole
pour représenter l'opération, qui consiste à fixer sur une ligne donnée la pointe d'un compas, lorsque l'autre pointe est fixée ;
mais, à cause de la nature mixte des problèmes où l'on en ferait usage et surtout parce que l'on s'éloignerait trop
de ce que l'on fait pratiquement, nous ne nous sommes pas arrêté à cette considération.

Il est un point qui mérite aussi quelques mots d'explications, lesquelles répondront à une objection
que je m'étais faite à l'origine et qui doit venir à l'esprit de ceux qui examinent notre méthode.
Est-il légitime de supposer identiques les opérations :math:`C_1, C_2, C_3, R_1, R_2`, pour composer
le coefficient de simplicité et le coefficient d'exactitude ? Non, évidemment, s'il s'agissait dans la *Géométrographie*
d'une mesure absolue. Mais ce n'est nullement le cas, et j'assimile ces opérations parce qu'elles sont élémentaires,
c'est-à-dire indécomposables en d'autres plus simples, et que, spéculativement, elles ne sont ni *plus simples*
ni *moins simples* les unes que les autres. On peut ne pas faire cette assimilation du reste,
en se contentant du symbole complet. Le mot de *mesure* ne peut pas être exact avec le sens habituel
de ce mot qui s'applique à la comparaison d'une grandeur avec *une* unité de même nature ;
une construction n'est pas une grandeur et elle s'exécute au moyen d'opérations élémentaires irréductibles entre elles.
Si j'emploie l'expression *mesure*, c'est que je trouve qu'elle s'applique mieux au but poursuivi que le mot général de comparaison.

.. folio:: 0021
   :page: p. 5

La rigueur absolue conduirait, dans beaucoup de cas, à rejeter toute comparaison de simplicité relative de deux constructions.
En effet, comment apprécier si la construction :math:`5C_3` est plus ou moins simple que :math:`50R_2`,
puisque les unités :math:`C_3` et :math:`R_2` sont par essence de nature différente ; mais, en réfléchissant
et aussi en pratiquant un peu la *Géométrographie*, on reconnaîtra que les assimilations sont admissibles
dans l'ordre d'exactitude des tracés eux-mêmes ; en effet, nous traçons des lignes et la ligne
n'a pas de dimensions, nous plaçons des points et le point ne peut être marqué.

En somme, notre méthode donne *un critérium* spéculatif qui a des applications pratiques, et avant elle il n'en existait pas.
Ce que nous faisons n'est pas une *mesure*, c'est une comparaison avec cinq unités distinctes : :math:`R_1, R_2, C_1, C_2, C_3`,
et l'on ne peut dire *d'une façon absolue* que la construction A est plus simple que la construction B,
que lorsque les coefficients de toutes les unités sont respectivement plus petits dans A que dans B, cas très fréquent.

.. [*] Nous n'avons pas été sans voir que la *simplicité* et l'*exactitude* d'une opération varient dans le même sens
   que l'inverse des nombres que nous nommons : coefficient de simplicité et coefficient d'exactitude ;
   mais comme il n'y a aucune confusion possible et que ce ne sont *que des noms*, nous avons préféré
   des dénominations rappelant le but à atteindre à celles de *coefficient de complication* et de *coefficient d'inexactitude* plus logiques certainement.
