:layout: book
:canonical_id: Prob. XLIX
:order: 2
:folio: 0056

.. _lemoine-21_normal_coordinates_xlix-en:

Problem XLIX: Constructing a Point from Normal Coordinates
==========================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 40–42, fols. ``0056–0058``)

.. folio:: 0056
   :page: p. 40

The new geometry of the triangle makes even more evident how indispensable it is to occupy oneself systematically with *the art of constructions*, for everything relating to it, in the matter of constructions, reduces in the last analysis to the construction of *remarkable* points—that is, those whose *normal* [*]_ coordinates, expressed as functions of the elements of the triangle, exhibit cyclic symmetry.

Now, every property found for a point gives a construction of that point more or less simple, more or less direct; it is therefore necessary to classify these constructions, to present *the simplest* for determining each remarkable point studied in this geometry, and to know the principal constructions among
the others less simple, yet which may frequently become the simplest in such or such overall drawings.

.. container:: lemoine-plate-pair

   .. picture:: 0056.g1.png
      :alt: Archival 1893 engraving FIG. 11 of Problem XLIX showing homothetic triangle A2B2C2 locating M from normal coordinates
      :caption: FIG. 11 archival scan (Paris 1893, fol. 0056, p. 40): Homothetic triangle A₂B₂C₂ and center M from trilinear coordinates (l : m : n).

   .. picture:: 0056.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 11 (Problem XLIX normal coordinates l, m, n)
      :caption: FIG. 11 vectorization: Exact SymPy calibration of perpendiculars A'O, B'O, C'γ₁, homothetic triangle A₂B₂C₂, and rays AM, BM meeting at M (S = 54).

The first problem to solve in the geometry of the triangle where the various coordinates employed must be translated for graphical solutions into normal coordinates is the following:

**XLIX.** — *Place a point* :g:`M` *whose proportional normal coordinates* :math:`l, m, n` *with respect to the reference triangle* :g:`ABC` *are known.*

I suppose that :math:`l, m, n` are straight lines
(otherwise one would first have to determine straight lines proportional to these quantities, of which we give an example further on).

*a)* I draw (*fig. 11*) three perpendiculars, one to each side, by

.. folio:: 0057
   :page: p. 41

describing from the vertices three circles of the same sufficient but arbitrary radius.
The intersections of these circles two by two give the three perpendicular bisectors; it is obvious that the radii of the three circles need not be equal in order to draw perpendiculars that are not the perpendicular bisectors, but it is more convenient :math:`\mathrm{op.} : (6R_1 + 3R_2 + 3C_1 + 3C_3)`.

On each side of the triangle, :g:`BC` for example, I take the foot :g:`A'` of the perpendicular drawn to that side and I determine the vertex :g:`A₁` opposite to :g:`A'` of a square :math:`A' a A_1 \alpha_1` of side :math:`l` whose sides would be directed along :g:`A'B` and the perpendicular to :g:`A'B` drawn at :g:`A'`.
I draw :math:`A_1 \alpha_1`; I have thus performed :math:`\mathrm{op.} : 3\left[2R_1 + R_2 + 5C_1 + 3C_3\right]`. The three lines :math:`A_1 \alpha_1, B_1 \beta_1, C_1 \gamma_1` determine a triangle :math:`A_2 B_2 C_2` homothetic to :g:`ABC`; the center of homothety, which I obtain by :math:`\mathrm{op.} : (4R_1 + 2R_2)`, is the sought point :g:`M`.

Symbol of the total operation:

.. math::

   \mathrm{op.} : \left(16R_1 + 8R_2 + 18C_1 + 12C_3\right); \quad \text{simplicity } 54; \quad \text{exactitude } 34; \quad 8\text{ lines}, 12\text{ circles}.

We treated the *same* question (*Bulletin de la Soc. math.*, 1888, p. 163), relying upon the *same geometric principle* (namely, that the point :g:`M` belongs to the locus of points whose ratio of distances to :g:`BC` and to :g:`CA` is :math:`\frac{l}{m}`, etc.);

We found for the symbol:

.. math::

   \mathrm{op.} : \left(34R_1 + 17R_2 + 13C_1 + 7C_3\right); \quad \text{simplicity } 71; \quad \text{exactitude } 47; \quad 17\text{ lines}, 7\text{ circles}.

This construction is less simple than the preceding one; moreover, in the cited article, we had not even turned it to the best possible account.

I would point out in this connection that it does not enter our mind that we are fixing here the fundamental symbols of *the art of geometric*
*construction*, as if we were giving the *definitively* simplest constructions, for:

1° Another geometer may find a better graphical interpretation of the solution we have adopted;

2° He may devise another solution leading to a better result; let us even say that constructions can never be *theoretically* fixed, since there is
no *criterion* for recognizing whether a solution is the simplest possible and whether it is executed graphically as well as possible; but *practically* the thing will soon be done once geometers have turned their attention to so clear and so sharply defined a subject;
it will suffice to record each improvement, and one will rapidly obtain the effectively definitive results.

*b) The normal coordinates* :math:`l, m, n` *are absolute normal coordinates and two of them are known,* :math:`l` *and* :math:`m` *for example:*

1° I take :math:`l` :math:`\mathrm{op.} : (2C_1)`.

I describe :g:`C(l)` and draw the two perpendiculars at :g:`C` to :g:`CA` and

.. folio:: 0058
   :page: p. 42

to :g:`CB` :math:`\mathrm{op.} : (4R_1 + 2R_2 + 5C_1 + 5C_3)`.

I take :math:`m` which I lay off in the proper direction as :math:`C\mu` on the perpendicular to :g:`CA`; this transfer need not be done for :math:`l`, which is placed on the circle :g:`C(l)` :math:`\mathrm{op.} : (3C_1 + C_3)`.

Through the endpoints thus obtained of :math:`l` and :math:`m`, I draw perpendiculars to the straight lines joining these endpoints to :g:`C` (XX 2° *b*)
:math:`\mathrm{op.} : (8R_1 + 4R_2 + 2C_1 + 2C_3)`. They intersect at the sought point.

.. math::

   \mathrm{Op.} : \left(12R_1 + 6R_2 + 12C_1 + 8C_3\right); \quad \text{simplicity } 38; \quad \text{exactitude } 24; \quad 6\text{ lines}, 8\text{ circles}.

2° I draw a circle passing through :g:`C` by means of which I draw the two perpendiculars to :g:`CB` and to :g:`CA` erected at :g:`C` (XX 2° *b*, saving :math:`C_1 + C_3` since a single circle suffices) :math:`\mathrm{op.} \left(8R_1 + 4R_2 + C_1 + C_3\right)`.
On these perpendiculars, I lay off in the proper direction the coordinates :math:`l` and :math:`m` :math:`\mathrm{op.} : (6C_1 + 2C_3)`, and, as in the preceding construction, I draw through the endpoints thus obtained perpendiculars to the straight lines joining these endpoints to :g:`C` :math:`\mathrm{op.} : (8R_1 + 4R_2 + 2C_1 + 2C_3)`.

.. math::

   \mathrm{Op.} : \left(16R_1 + 8R_2 + 9C_1 + 5C_3\right); \quad \text{simplicity } 38; \quad \text{exactitude } 25; \quad 8\text{ lines}, 5\text{ circles}.

Every remarkable point can evidently be constructed when one has the expression of its normal coordinates, but this construction is *always* much more complicated than others deduced from the properties of the point. We shall give a few examples of this.

.. [*] I say *normal* to the exclusion of *barycentric*, because the latter are coordinates very useful for geometric speculation, but ill suited to *direct construction*, which immediately uses only straight lines and circles and not weights or areas.
