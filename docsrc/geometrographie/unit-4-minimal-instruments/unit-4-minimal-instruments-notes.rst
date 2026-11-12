:layout: book

.. _geometrographie-unit-4-notes:

Unit IV Commentary & Notes: Mohr–Mascheroni, Poncelet–Steiner & Hilbert's Field Hierarchy
=========================================================================================

.. rubric:: Historical Lineage, Projective Obstructions & Algebraic Constructibility

1. From Mohr (1672) and Mascheroni (1797) to Bonaparte and Fazzari (1901)
-------------------------------------------------------------------------

As :person:`Gaetano Fazzari <fazzari>` documents in the historical preface to his 1901 Palermo edition of *La Geometria del Compasso* (:cite:`fazzari-1901`, pp. v–xiii), :person:`Lorenzo Mascheroni <mascheroni>` met :person:`Napoléon Bonaparte <bonaparte>` in northern Italy in 1797 and dedicated the Pavia *editio princeps* (:cite:`mascheroni-1797`) to him in Italian hendecasyllabic verse. Returning to Paris, Bonaparte famously astonished Laplace and Lagrange at the Institut National by presenting Mascheroni's compass-only quadrisection of the circle (Libro II, § 34: stepping three hexagon chords :math:`B, C, D` of radius :math:`r` so :math:`AC = BD = r\sqrt{3}`, intersecting :math:`A(AC)` and :math:`D(BD)` at :math:`E` so :math:`OE = r\sqrt{2}`, and cutting the circle from :math:`A` with radius :math:`OE` in just **4 auxiliary arcs**), provoking Laplace's celebrated remark: *"Nous attendions tout de vous, général, excepté des leçons de géométrie."*

Only in 1928 did Danish mathematician Johannes Hjelmslev examine a student-submitted 1672 Amsterdam booklet by :person:`Georg Mohr <mohr>`, *Euclides Danicus* (:cite:`mohr-1672`), discovering that Mohr had solved the entire compass-only program 125 years before Mascheroni! Even more remarkably, :person:`August Adler <adler>` (:cite:`adler-1890`) showed that circular inversion (:math:`5C_1 + 3C_3`, Lemoine Problem XXXVIII) provides a single uniform functor translating every straightedge step into compass arcs.

2. Poncelet–Steiner vs. Hilbert Chapter VII: Euclidean vs. Pythagorean Fields
-----------------------------------------------------------------------------

Comparing :person:`Steiner <steiner>`'s 1833 fixed-circle constructions (:cite:`steiner-1833`) with :person:`David Hilbert <hilbert>`'s 1899 *Grundlagen der Geometrie* Chapter VII (:cite:`hilbert-1899`, §§ 36–39; published in ``geometor/hilbert``) clarifies the exact algebraic role of a **traced circle locus**:

* In **Hilbert §§ 36–39**, the geometer possesses a straightedge and an *Eichmaß* (segment-transferrer capable of laying off a fixed unit length :math:`1` along any ray, equivalent to Lemoine's *équerre* + unit gauge without a drawn circle). Hilbert proves that this instrument constructs a point if and only if its coordinates lie in the **pythagorean closure** :math:`\Omega_{\text{pyth}}` (closed under :math:`\sqrt{1 + \omega^2}`, sums of squares). Crucially, :math:`\sqrt{1 + \sqrt{2}} \notin \Omega_{\text{pyth}}`: **not** every circle–line intersection can be executed!
* In **Poncelet–Steiner (1822 / 1833)**, replacing the movable unit gauge by **one single drawn circle** :math:`\Omega` with its center :math:`M` upgrades constructibility from the pythagorean field :math:`\Omega_{\text{pyth}}` to the **full Euclidean quadratic closure** :math:`\mathbb{E}` (closed under :math:`\sqrt{\alpha}` for *every* positive :math:`\alpha > 0`), because Steiner's Seventh Problem projects arbitrary secants homothethically onto the actual continuous circumference :math:`\Omega`!

3. Why *Géométrographie* Bridges Synthetic Duality and Algorithmic Cost
-----------------------------------------------------------------------

Viewed through Lemoine's operation vectors:

* **Mascheroni** trades :math:`(l_1, l_2) \to (0, 0)` at the price of simulating collinear incidences via inversion/fourth-proportional circles (e.g., midpoint :math:`S = 7 \to 17`); yet on metric/inversive problems (point reflection :math:`S = 6`, parallel point :math:`S = 7`, circle inversion :math:`S = 8`, fourth proportional :math:`S = 14`), Mascheroni **ties or beats** standard ruler-and-compass textbooks!
* **Steiner** trades :math:`(m_1, m_2, m_3) \to (0, 0, 0)` once fixed circle :math:`M` is given; on metric transfers (Sixth–Eighth Problems) homothetic simulation increases :math:`S`, yet on projective/harmonic problems (polar :math:`12R_1 + 7R_2, S = 19`; harmonic conjugate :math:`9R_1 + 6R_2, S = 15`; tangents to a drawn circle :math:`16R_1 + 9R_2, S = 25`), Steiner's pure straightedge **beats** compass-assisted constructions!
