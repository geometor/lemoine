:layout: book
:canonical_id: Principes
:order: 1
:folio: 0052
:tracks: English: 20_principles_and_rational_division-en | French: 20_principles_and_rational_division-fr | Summary: 20_principles_and_rational_division-summary | Notes: 20_principles_and_rational_division-notes

.. _lemoine-20_principles_and_rational_division-en:

Five Guiding Principles & Simultaneous 1/10 and 1/15 Division
=============================================================

.. rubric:: Émile Lemoine — *La Géométrographie* (English Translation, pp. 36–39, fols. ``0052–0055``)

.. folio:: 0052
   :page: p. 36

We said above that the art of geometric constructions, or *Geometrography*, rested upon *principles* of the most extreme simplicity; the digression concerning the constructions of Messrs. :person:`Chasles <chasles>` and :person:`Mannheim <mannheim>` caused us to defer the statement of these principles; here they are:

1° *In each construction, trace no useless line—that is to say, employ, when one can, either the traced lines of the given figure or those already traced in the course of the construction.*

COROLLARY: trace, whenever possible, all circles of a given compass opening once their centers are placed, even though the drawing of these
circles only appears later in the logical development of the solution; one must therefore, as we have already said, make a preliminary study of the question by a kind of reasoned sketch of the construction.

.. folio:: 0053
   :page: p. 37

2° *Choose among the solutions of the same problem those whose total system of constructions leads to the simplest symbol.*

3° *Examine, in every problem, all particular cases of data that may arise and then simplify the general symbol for those particular cases.*

This discussion in somewhat complex problems, such as, for example, the problem of *Apollonius* (circles tangent to three given circles), is
very delicate, and it is the best exercise in sagacity and discussion that one can propose to students.

4° *In searching for the* GENERAL *symbol of a construction, employ only general constructions, unless one proves that a particular solution always applies to the problem under examination.*

Thus, for example, if in a general construction one has to draw polars of points with respect to circles, one must adopt for the general symbol of drawing these polars either *a* or *b* of construction XXXIX, and not *c*, which is simpler, but applies only when the distance from the pole
to the center is greater than half the radius; unless, quite evidently, one proves that this circumstance always occurs in the general problem one is studying.

5° *For a construction carried out with particular data, take advantage of all particular constructions simpler than the general constructions that can apply in the case where one stands.*

There is evidently a general study of procedures to be made in order to arrive at simple constructions; nothing has yet been done from this point of view; we shall merely give an example here to make our thought clearly understood.

Let us examine the two problems: *To take a straight line* :math:`n`
*times greater or a straight line* :math:`n` *times smaller than a given straight line* :g:`BC`; :math:`n` *being supposed an integer.*

Constructions XXX and XXXI are rather complicated and *above all* give rise to a great probability of error when :math:`n` is somewhat considerable; there is
reason therefore to seek whether one cannot find another mode of constructions deriving from the properties of certain figures or from the values of the number :math:`n` and yielding a better practical result.

Suppose, for example, that we have to draw a straight line that is :math:`\frac{1}{10}` of :g:`BC` and, at the same time,
a straight line that is :math:`\frac{1}{15}` of :g:`BC`. By construction XXXI I construct :math:`B_1 C_1` which is :math:`\frac{1}{5}` of :g:`BC` :math:`\mathrm{op.} : (2R_1 + 2R_2 + 11C_1 + 13C_3)`, and to have :math:`\frac{1}{15}` of :g:`BC`, I have only to divide :math:`B_1 C_1` at point :g:`N'` between :math:`B_1` and :math:`C_1`

.. folio:: 0054
   :page: p. 38

so that
:math:`\frac{N'C_1}{B_1 N} = \frac{1}{2}`; :math:`N'C_1` will be :math:`\frac{BC}{15}`. I can, in order to divide :math:`B_1 C_1` in the ratio of 1 to 2, employ the following procedure, simpler than the general procedure given for dividing a given straight line in a given ratio. Through :math:`B_1` I draw any straight line :math:`B_1 A'` and on :math:`B_1 A'` I mark any point :g:`M'` by taking :math:`B_1 M' = M'A'`
:math:`\mathrm{op.} : (R_1 + R_2 + C_1 + C_2 + C_3)`; I take the symmetric :g:`A''` of :g:`A'` with respect to :math:`C_1` and draw :math:`A'' M'` cutting :math:`B_1 C_1` at :g:`N'` :math:`\mathrm{op.} : (4R_1 + 3R_2 + 2C_1 + C_3)`.

In all: :math:`\mathrm{op.} : (5R_1 + 3R_2 + 3C_1 + C_2 + 2C_3)` to divide :math:`B_1 C_1` at :g:`N'` in the ratio of 2 to 1. I shall thus have obtained :math:`\frac{1}{10}` and :math:`\frac{1}{15}` of :g:`BC` by the symbol:

.. math::

   \mathrm{Op.} : \left(7R_1 + 5R_2 + 14C_1 + C_2 + 15C_3\right); \quad \text{simplicity } 42; \quad \text{exactitude } 22; \quad 5\text{ lines}, 15\text{ circles}.

.. container:: lemoine-plate-pair

   .. picture:: 0054.g1.png
      :alt: Archival 1893 engraving FIG. 10 showing Lemoine's equilateral-triangle 1/10 and 1/15 division of BC
      :caption: FIG. 10 archival scan (Paris 1893, fol. 0054, p. 38): Simultaneous 1/15 (KG) and 1/10 (KE) division of BC.

   .. picture:: 0054.g1.svg
      :alt: Calibrated interactive vectorization of FIG. 10 (exact Menelaus rational division of equilateral triangle)
      :caption: FIG. 10 vectorization: Exact SymPy calibration verifying KG = (1/15)BC, KE = (1/10)BC, LH = (1/14)BC, and MC' = (1/3)BC (S = 35).

OTHER METHOD. — I take :g:`BC` between the legs of the compass and, :g:`A` being any point, I trace :g:`A(BC)` (*fig. 10*); then from any point :g:`C'` of :g:`A(BC)`, I trace :g:`C'(BC)` cutting :g:`A(BC)` at :g:`B'`, and I trace :g:`B'C'` cutting :g:`C'(BC)` at :g:`D`, then :g:`AC'`, :g:`AB'`, :math:`\mathrm{op.} : (6R_1 + 3R_2 + 2C_1 + C_2 + 2C_3)`.

I place the midpoint :g:`H` of :g:`AC'` and the midpoint :g:`E` of :g:`AB'` :math:`\mathrm{op.} : (2R_1 + R_2 + 2C_1 + C_3)` by using circles :g:`A(BC)`, :g:`C'(BC)` to obtain :g:`H`, and describing :g:`A(AH)` to obtain :g:`E`; I draw :g:`ED` cutting :g:`AC'` at :g:`F`; :g:`HD` cutting :g:`B'` at :g:`G`; :g:`ED`, :g:`GF` meeting at :g:`I`; :g:`DI` cutting :g:`AB'` at :g:`K`, :g:`AC'` at :g:`L` :math:`\mathrm{op.} : (10R_1 + 5R_2)`; we have :math:`KG = \frac{1}{15}\,BC`, :math:`KE = \frac{1}{10}\,BC`.

In all:

.. math::

   \mathrm{op.} : \left(18R_1 + 9R_2 + 4C_1 + C_2 + 3C_3\right); \quad \text{simplicity } 35; \quad \text{exactitude } 23; \quad 9\text{ lines}, 3\text{ circles}.

Let :g:`M` be the point where :g:`GF` cuts :g:`B'C'`.

It is evident that this figure yields many other divisions of :g:`BC`, for example:

.. math::

   \begin{aligned}
   HF = GE = IH &= \frac{1}{6}\,BC; \qquad MC' = IE = FC' = \frac{1}{3}\,BC; \\
   LA = \frac{4}{7}\,BC; \qquad LC' &= \frac{3}{7}\,BC; \qquad LH = \frac{1}{14}\,BC; \qquad MB' = \frac{4}{3}\,BC; \qquad FG = \frac{BC}{\sqrt{3}};
   \end{aligned}

.. folio:: 0055
   :page: p. 39

.. math::

   \begin{aligned}
   HG &= \frac{\sqrt{7}}{6}\,BC; \qquad DH = \frac{\sqrt{7}}{2}\,BC; \qquad DF = \frac{\sqrt{13}}{3}\,BC; \qquad EF = \frac{\sqrt{13}}{6}\,BC; \\
   DE &= \frac{\sqrt{13}}{2}\,BC; \qquad KL = \frac{2\sqrt{79}}{35}\,BC; \qquad GI = IF = \frac{1}{2\sqrt{3}}\,BC,\text{ etc., etc.}
   \end{aligned}

One sees that if, instead of taking :math:`C'D = BC`, one took :math:`C'D = m \cdot BC` (:math:`m` being an integer or fraction), one would have for all the lines, whose lengths we have just given for the particular case :math:`m = 1`, very varied different lengths which one may use
to construct lengths of the forms:

.. math::

   l \cdot BC, \qquad \frac{1}{l} \cdot BC, \qquad \frac{m}{n} \cdot BC, \qquad \frac{\sqrt{l}}{m} \cdot BC, \qquad \frac{m\sqrt{l}}{n} \cdot BC,

:math:`l, m, n` being integers.

This is a study to be made for each case and one not without certain difficulties. The study could be made for the more general case where triangle :g:`AB'C'` is no longer equilateral.
I construct a triangle :g:`AB'C'` whose sides :g:`B'C'`, :g:`C'A`, :g:`B'A` are :math:`l \cdot BC`, :math:`m \cdot BC`, :math:`n \cdot BC`; I take :g:`D` on :g:`B'C'` such that :math:`C'D' = d \cdot BC`; I take on :g:`B'A`, :math:`B'E = p \cdot BC` and on :g:`C'A`, :math:`C'H = q \cdot BC`, and I draw the same straight lines as before with the same notations and compute the lengths :g:`HF`, :g:`FC'`, etc., etc.;
it seems to me that one can always choose, and indeed in infinitely many ways, the integers :math:`l, m, n, d, p, q` so as to obtain, among the lengths :g:`HF`, :g:`FC'`, etc., all expressions of the forms:

.. math::

   \frac{\alpha}{\beta} \cdot BC, \qquad \frac{\alpha}{\beta} \sqrt{\frac{\gamma}{\delta}} \cdot BC,

:math:`\alpha, \beta, \gamma, \delta` being integers.

To this question of indeterminate analysis, somewhat unforeseen in connection with our subject and which I believe very difficult and highly interesting in itself though I cannot study it in detail, are attached a host of others such as the following: *Among the numbers* :math:`l, m, n, d, p, q`; *how many can be chosen arbitrarily*
*so that the others may be determined so that one of the quantities* :g:`HF`, :g:`FC'`, *etc., has a given value, or again: Given a triangle* :g:`AB'C'` *whose sides are integers, can one always find a transversal* :g:`DEF` *that divides the sides of the triangle into integer segments, or under what conditions is the problem possible?*
By the theorem of *Menelaus*, this last question reduces immediately to the following: :math:`a, b, c` being integers, does the equation :math:`ayz - bzx - cxy + bcx - cay - abz + abc = 0` *always have for* :math:`x, y, z` *integer solutions, positive or negative, none of which is zero?*
