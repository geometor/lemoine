"""Generate the 9 standalone theme-adaptive .euclid-graphic SVG plates for GEOMETOR Lemoine.

Every plate computes its geometric loci via exact SymPy algebra over Q or radical
extensions before emitting theme-adaptive .euclid-graphic SVG markup into
``docsrc/_static/figures/``. Zero Python scripts are embedded in the treatise RST.
"""

from __future__ import annotations

import html
import math
from dataclasses import dataclass, field
from pathlib import Path

import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "docsrc" / "_static" / "figures"

Pt = tuple[sp.Expr, sp.Expr]


def fxy(p: Pt) -> tuple[float, float]:
    """Evaluate an exact SymPy 2D point to floating-point SVG coordinates."""
    return (float(sp.N(p[0], 20)), float(sp.N(p[1], 20)))


@dataclass
class EuclidGraphicBuilder:
    """Emit standalone `.euclid-graphic` SVGs honoring the Scriptorium Codex contract."""

    graphic_id: str
    proposition: str
    width: int
    height: int
    elements: list[str] = field(default_factory=list)
    graphics: list[str] = field(default_factory=list)
    highlights: list[str] = field(default_factory=list)
    points: list[str] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)

    def add_polygon(
        self, pts: list[Pt], ref: str, cls: str = "geom-polygon"
    ) -> None:
        coords = " ".join(f"{fxy(p)[0]:.2f},{fxy(p)[1]:.2f}" for p in pts)
        self.elements.append(
            f'    <polygon points="{coords}" class="{cls}" data-ref="{html.escape(ref, quote=True)}" />'
        )

    def add_segment(
        self,
        p1: Pt,
        p2: Pt,
        ref: str | None = None,
        cls: str = "geom-line",
        ticks: int = 0,
    ) -> None:
        x1, y1 = fxy(p1)
        x2, y2 = fxy(p2)
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        attrs = [
            f'd="M {x1:.2f} {y1:.2f} L {mx:.2f} {my:.2f} L {x2:.2f} {y2:.2f}"',
            'fill="none"',
            f'class="{cls}"',
        ]
        if ticks in (1, 2, 3):
            attrs.append(f'marker-mid="url(#geom-tick-{ticks})"')
        if ref:
            attrs.append(f'data-ref="{html.escape(ref, quote=True)}"')
            self.elements.append(f"    <path {' '.join(attrs)} />")
        else:
            self.graphics.append(f"    <path {' '.join(attrs)} />")

    def add_circle(
        self, center: Pt, radius: sp.Expr | float, ref: str | None = None, cls: str = "geom-circle"
    ) -> None:
        cx, cy = fxy(center)
        r = float(sp.N(radius, 20))
        ref_attr = f' data-ref="{html.escape(ref, quote=True)}"' if ref else ""
        target = self.elements if ref else self.graphics
        target.append(
            f'    <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="none" class="{cls}"{ref_attr} />'
        )

    def add_arc(
        self,
        center: Pt,
        radius: sp.Expr | float,
        deg_start: float,
        deg_end: float,
        ref: str | None = None,
        cls: str = "geom-arc",
    ) -> None:
        cx, cy = fxy(center)
        r = float(sp.N(radius, 20))
        a1 = math.radians(deg_start)
        a2 = math.radians(deg_end)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        delta = (deg_end - deg_start) % 360.0
        large = 1 if delta > 180.0 else 0
        ref_attr = f' data-ref="{html.escape(ref, quote=True)}"' if ref else ""
        target = self.elements if ref else self.graphics
        target.append(
            f'    <path d="M {x1:.2f} {y1:.2f} A {r:.2f} {r:.2f} 0 {large} 1 {x2:.2f} {y2:.2f}" '
            f'fill="none" class="{cls}"{ref_attr} />'
        )

    def add_right_angle(
        self, vertex: Pt, u_dir: tuple[float, float], v_dir: tuple[float, float], size: float = 9.5
    ) -> None:
        vx, vy = fxy(vertex)
        ux, uy = u_dir
        wx, wy = v_dir
        un = math.hypot(ux, uy) or 1.0
        wn = math.hypot(wx, wy) or 1.0
        ux, uy = ux / un * size, uy / un * size
        wx, wy = wx / wn * size, wy / wn * size
        p1x, p1y = vx + ux, vy + uy
        p2x, p2y = vx + ux + wx, vy + uy + wy
        p3x, p3y = vx + wx, vy + wy
        self.highlights.append(
            f'    <path d="M {p1x:.2f} {p1y:.2f} L {p2x:.2f} {p2y:.2f} L {p3x:.2f} {p3y:.2f}" '
            f'fill="none" class="geom-ang-arc" />'
        )

    def add_point(
        self, pt: Pt, ref: str, cls: str = "geom-point", r: float = 3.3
    ) -> None:
        px, py = fxy(pt)
        self.points.append(
            f'    <circle cx="{px:.2f}" cy="{py:.2f}" r="{r:.2f}" class="{cls}" '
            f'data-ref="{html.escape(ref, quote=True)}" />'
        )

    def add_label(
        self,
        pt: Pt,
        text: str,
        dx: float = 0.0,
        dy: float = -8.0,
        ref: str | None = None,
        cls: str = "geom-label",
        anchor: str = "middle",
    ) -> None:
        px, py = fxy(pt)
        ref_attr = f' data-ref="{html.escape(ref, quote=True)}"' if ref else ""
        self.labels.append(
            f'    <text x="{px + dx:.2f}" y="{py + dy:.2f}" text-anchor="{anchor}" '
            f'class="{cls}"{ref_attr}>{html.escape(text)}</text>'
        )

    def add_caption(self, x: float, y: float, text: str, anchor: str = "middle") -> None:
        self.labels.append(
            f'    <text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" class="geom-label-sm">{html.escape(text)}</text>'
        )

    def render(self) -> str:
        return "\n".join(
            [
                (
                    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
                    f'width="{self.width}" height="{self.height}" class="euclid-graphic" '
                    f'data-graphic-id="{self.graphic_id}" data-proposition="{self.proposition}">'
                ),
                "  <defs>",
                '    <marker id="geom-tick-1" viewBox="-2 -6 4 12" markerWidth="4" markerHeight="12" orient="auto">',
                '      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="var(--geom-fg)" stroke-width="1.4" />',
                "    </marker>",
                '    <marker id="geom-tick-2" viewBox="-4 -6 8 12" markerWidth="8" markerHeight="12" orient="auto">',
                '      <line x1="-1.8" y1="-4.5" x2="-1.8" y2="4.5" stroke="var(--geom-fg)" stroke-width="1.4" />',
                '      <line x1="1.8" y1="-4.5" x2="1.8" y2="4.5" stroke="var(--geom-fg)" stroke-width="1.4" />',
                "    </marker>",
                '    <marker id="geom-tick-3" viewBox="-6 -6 12 12" markerWidth="12" markerHeight="12" orient="auto">',
                '      <line x1="-3.4" y1="-4.5" x2="-3.4" y2="4.5" stroke="var(--geom-fg)" stroke-width="1.4" />',
                '      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="var(--geom-fg)" stroke-width="1.4" />',
                '      <line x1="3.4" y1="-4.5" x2="3.4" y2="4.5" stroke="var(--geom-fg)" stroke-width="1.4" />',
                "    </marker>",
                "  </defs>",
                "  <style>",
                "    :root {",
                "      --geom-fg: #18181b;",
                "      --geom-bg: #ffffff;",
                "      --geom-point-stroke: #ffffff;",
                "      --geom-poly-fill: #000000;",
                "      --geom-accent: #c88a1e;",
                "      --geom-assert: #16a34a;",
                "    }",
                "    .euclid-graphic {",
                "      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;",
                "      font-style: normal;",
                "      font-weight: 700;",
                "      background-color: var(--geom-bg);",
                "    }",
                "    .geom-line { stroke: var(--geom-fg); stroke-width: 1.8; stroke-linecap: round; fill: none; }",
                "    .geom-bold { stroke: var(--geom-fg); stroke-width: 2.3; stroke-linecap: round; fill: none; }",
                "    .geom-dashed { stroke: var(--geom-fg); stroke-width: 1.35; stroke-dasharray: 5, 3.5; stroke-linecap: round; fill: none; opacity: 0.78; }",
                "    .geom-accent-line { stroke: var(--geom-accent); stroke-width: 2.15; stroke-linecap: round; fill: none; }",
                "    .geom-assert-line { stroke: var(--geom-assert); stroke-width: 2.25; stroke-linecap: round; fill: none; }",
                "    .geom-circle { stroke: var(--geom-fg); stroke-width: 1.55; fill: none; }",
                "    .geom-arc { stroke: var(--geom-accent); stroke-width: 1.75; stroke-dasharray: 4.5, 3; stroke-linecap: round; fill: none; }",
                "    .geom-ang-arc { stroke: var(--geom-assert); stroke-width: 1.7; stroke-linecap: round; fill: none; }",
                "    .geom-polygon { fill: var(--geom-poly-fill); fill-opacity: 0.05; stroke: none; }",
                "    .geom-polygon-accent { fill: var(--geom-accent); fill-opacity: 0.12; stroke: none; }",
                "    .geom-point { fill: var(--geom-fg); stroke: var(--geom-point-stroke); stroke-width: 1.15; }",
                "    .geom-point-accent { fill: var(--geom-accent); stroke: var(--geom-point-stroke); stroke-width: 1.15; }",
                "    .geom-point-assert { fill: var(--geom-assert); stroke: var(--geom-point-stroke); stroke-width: 1.25; }",
                "    .geom-label { font-size: 13px; font-weight: 700; fill: var(--geom-fg); user-select: none; }",
                "    .geom-label-sm { font-size: 10.2px; font-weight: 700; fill: var(--geom-fg); opacity: 0.88; user-select: none; }",
                "    .is-active { stroke-width: 3.1 !important; filter: drop-shadow(0 0 3px var(--geom-accent)); }",
                "    @media (prefers-color-scheme: dark) {",
                "      :root {",
                "        --geom-fg: #d6cfc5;",
                "        --geom-bg: #1e1e20;",
                "        --geom-point-stroke: #1e1e20;",
                "        --geom-poly-fill: #d6cfc5;",
                "        --geom-accent: #e8b85a;",
                "        --geom-assert: #5ec27e;",
                "      }",
                "    }",
                "  </style>",
                '  <g id="elements">',
                *self.elements,
                "  </g>",
                '  <g id="graphics">',
                *self.graphics,
                "  </g>",
                '  <g id="highlights" style="pointer-events: none;">',
                *self.highlights,
                "  </g>",
                '  <g id="points">',
                *self.points,
                "  </g>",
                '  <g id="labels">',
                *self.labels,
                "  </g>",
                "</svg>",
                "",
            ]
        )


def build_elementary_operations() -> str:
    """1. Five elementary operations R1, R2, C1, C2, C3 and circle O(AB)."""
    g = EuclidGraphicBuilder("fig_elementary_operations", "Op.I-VIII", 620, 230)

    A = (sp.Integer(65), sp.Integer(145))
    B = (sp.Integer(235), sp.Integer(81))
    L_left = (sp.Integer(32), sp.Integer(145) - sp.Rational(64, 170) * (32 - 65))
    L_right = (sp.Integer(272), sp.Integer(145) - sp.Rational(64, 170) * (272 - 65))

    g.add_segment(L_left, L_right, ref="AB", cls="geom-assert-line")
    g.add_segment(A, B, ref="AB", cls="geom-bold", ticks=1)
    g.add_point(A, "A", "geom-point-accent", 3.8)
    g.add_point(B, "B", "geom-point-accent", 3.8)
    g.add_label(A, "A (R₁)", dx=-4, dy=20, ref="A")
    g.add_label(B, "B (R₁)", dx=6, dy=-10, ref="B")
    g.add_caption(152, 26, "Ruler Join AB : 2R₁ + R₂  (S = 3, E = 2)")
    g.add_caption(152, 206, "R₁: align on point · R₂: trace straight line")

    g.add_segment((sp.Integer(302), sp.Integer(18)), (sp.Integer(302), sp.Integer(212)), cls="geom-dashed")

    O_pt = (sp.Integer(456), sp.Integer(114))
    R_len = sp.Integer(62)
    D_left = (sp.Integer(336), sp.Integer(148))
    D_right = (sp.Integer(582), sp.Integer(148))
    dx = sp.sqrt(sp.Integer(62) ** 2 - sp.Integer(34) ** 2)
    M = (sp.Integer(456) - dx, sp.Integer(148))
    N = (sp.Integer(456) + dx, sp.Integer(148))
    P_rad = (sp.Integer(456) + R_len * sp.Rational(3, 5), sp.Integer(114) - R_len * sp.Rational(4, 5))

    g.add_segment(D_left, D_right, ref="MN", cls="geom-line")
    g.add_circle(O_pt, R_len, ref="O(AB)", cls="geom-accent-line")
    g.add_segment(O_pt, P_rad, ref="OR", cls="geom-dashed", ticks=1)
    g.add_point(O_pt, "O", "geom-point-accent", 3.8)
    g.add_point(P_rad, "R", "geom-point")
    g.add_point(M, "M", "geom-point-assert", 3.5)
    g.add_point(N, "N", "geom-point-assert", 3.5)
    g.add_label(O_pt, "O (C₁)", dx=-20, dy=-6, ref="O")
    g.add_label(P_rad, "O(AB)", dx=22, dy=-5, ref="O(AB)")
    g.add_label(M, "M (C₂)", dx=-8, dy=18, ref="M")
    g.add_label(N, "N", dx=8, dy=18, ref="N")
    g.add_caption(460, 26, "Circle O(AB) & Segment Transfer : 2C₁ + C₂ + C₃  (S = 4)")
    g.add_caption(460, 206, "C₁: set on point · C₂: set on locus · C₃: trace circle")
    return g.render()


def build_perpendicular_bisector() -> str:
    """2. Problem XVIII: Perpendicular bisector & midpoint M in 2R1 + R2 + 2C1 + 2C3 (S = 7, E = 4)."""
    g = EuclidGraphicBuilder("fig_perpendicular_bisector", "XVIII", 520, 265)

    A = (sp.Integer(175), sp.Integer(138))
    B = (sp.Integer(345), sp.Integer(138))
    M = (sp.Integer(260), sp.Integer(138))
    R = sp.Integer(115)
    dy = sp.sqrt(R**2 - sp.Integer(85) ** 2)
    P = (sp.Integer(260), sp.Integer(138) - dy)
    Q = (sp.Integer(260), sp.Integer(138) + dy)

    g.add_arc(A, R, -62, 62, ref="A(R)", cls="geom-arc")
    g.add_arc(B, R, 118, 242, ref="B(R)", cls="geom-arc")
    g.add_segment((sp.Integer(115), sp.Integer(138)), (sp.Integer(405), sp.Integer(138)), cls="geom-dashed")
    g.add_segment(A, M, ref="AM", cls="geom-bold", ticks=1)
    g.add_segment(M, B, ref="MB", cls="geom-bold", ticks=1)
    g.add_segment(
        (sp.Integer(260), sp.Integer(34)),
        (sp.Integer(260), sp.Integer(242)),
        ref="PQ",
        cls="geom-assert-line",
    )
    g.add_right_angle(M, (1, 0), (0, -1), 9.5)

    g.add_point(A, "A", "geom-point")
    g.add_point(B, "B", "geom-point")
    g.add_point(P, "P", "geom-point-accent")
    g.add_point(Q, "Q", "geom-point-accent")
    g.add_point(M, "M", "geom-point-assert", 3.8)

    g.add_label(A, "A", dx=-12, dy=18, ref="A")
    g.add_label(B, "B", dx=12, dy=18, ref="B")
    g.add_label(P, "P", dx=14, dy=-4, ref="P")
    g.add_label(Q, "Q", dx=14, dy=14, ref="Q")
    g.add_label(M, "M", dx=-12, dy=-8, ref="M")
    g.add_caption(260, 20, "Problem XVIII (Euclid I.10) — 2R₁ + R₂ + 2C₁ + 2C₃  (S = 7, E = 4 vs. S = 8)")
    return g.render()


def build_perpendicular_external() -> str:
    """3. Problem XX: External perpendicular (S = 9) & Thales 1-circle perpendicular at A (S = 8)."""
    g = EuclidGraphicBuilder("fig_perpendicular_external", "XX", 620, 255)

    B1 = (sp.Integer(72), sp.Integer(138))
    C1 = (sp.Integer(212), sp.Integer(138))
    A1 = (sp.Integer(154), sp.Integer(68))
    Ap1 = (sp.Integer(154), sp.Integer(208))
    H1 = (sp.Integer(154), sp.Integer(138))
    rB = sp.sqrt((A1[0] - B1[0]) ** 2 + (A1[1] - B1[1]) ** 2)
    rC = sp.sqrt((A1[0] - C1[0]) ** 2 + (A1[1] - C1[1]) ** 2)

    g.add_segment((sp.Integer(35), sp.Integer(138)), (sp.Integer(265), sp.Integer(138)), ref="BC", cls="geom-bold")
    g.add_arc(B1, rB, -50, 50, cls="geom-arc")
    g.add_arc(C1, rC, 122, 238, cls="geom-arc")
    g.add_segment((sp.Integer(154), sp.Integer(48)), (sp.Integer(154), sp.Integer(226)), ref="AA'", cls="geom-assert-line")
    g.add_right_angle(H1, (1, 0), (0, -1), 8.5)

    for pt, nm, cl, dx, dy in (
        (A1, "A", "geom-point-accent", 12, -5),
        (Ap1, "A'", "geom-point-accent", 14, 13),
        (B1, "B", "geom-point", -8, 17),
        (C1, "C", "geom-point", 10, 17),
        (H1, "H", "geom-point-assert", -11, -7),
    ):
        g.add_point(pt, nm, cl)
        g.add_label(pt, nm, dx=dx, dy=dy, ref=nm)
    g.add_caption(150, 24, "XX.1 Off Line (I.12): 2 Circles, S = 9")

    g.add_segment((sp.Integer(298), sp.Integer(20)), (sp.Integer(298), sp.Integer(235)), cls="geom-dashed")

    A2 = (sp.Integer(398), sp.Integer(186))
    O2 = (sp.Integer(458), sp.Integer(141))
    R2 = sp.Integer(75)
    B2 = (sp.Integer(518), sp.Integer(186))
    D2 = (sp.Integer(398), sp.Integer(96))

    g.add_segment((sp.Integer(332), sp.Integer(186)), (sp.Integer(576), sp.Integer(186)), cls="geom-bold")
    g.add_circle(O2, R2, ref="O(OA)", cls="geom-arc")
    g.add_segment(B2, D2, ref="BD", cls="geom-line")
    g.add_segment((sp.Integer(398), sp.Integer(54)), (sp.Integer(398), sp.Integer(212)), ref="AD", cls="geom-assert-line")
    g.add_right_angle(A2, (1, 0), (0, -1), 9.0)

    for pt, nm, cl, dx, dy in (
        (A2, "A", "geom-point-assert", -11, 18),
        (O2, "O", "geom-point-accent", 12, -5),
        (B2, "B", "geom-point", 10, 18),
        (D2, "D", "geom-point-assert", -13, -4),
    ):
        g.add_point(pt, nm, cl)
        g.add_label(pt, nm, dx=dx, dy=dy, ref=nm)
    g.add_caption(458, 24, "XX.2 On Line (Thales): 1 Circle, 4R₁ + 2R₂ + C₁ + C₃ (S = 8)")
    return g.render()


def build_parallel_comparison() -> str:
    """4. Problem XVII: Classical alternate-angle parallel (S = 11) vs. Tarry's rhombus parallel (S = 9)."""
    g = EuclidGraphicBuilder("fig_parallel_comparison", "XVII", 650, 250)

    P_l = (sp.Integer(92), sp.Integer(186))
    A_l = (sp.Integer(142), sp.Integer(90))
    R_c = sp.sqrt((A_l[0] - P_l[0]) ** 2 + (A_l[1] - P_l[1]) ** 2)
    Q_l = (sp.Integer(92) + R_c, sp.Integer(186))
    D_l = (A_l[0] + R_c, sp.Integer(90))

    g.add_segment((sp.Integer(34), sp.Integer(186)), (sp.Integer(288), sp.Integer(186)), cls="geom-bold")
    g.add_segment(P_l, A_l, cls="geom-dashed")
    g.add_arc(P_l, R_c, -68, 12, cls="geom-arc")
    g.add_arc(A_l, R_c, -12, 125, cls="geom-arc")
    g.add_arc(Q_l, R_c, -125, -52, cls="geom-arc")
    g.add_segment((sp.Integer(48), sp.Integer(90)), (sp.Integer(288), sp.Integer(90)), cls="geom-assert-line")

    for pt, nm, cl, dx, dy in (
        (A_l, "A", "geom-point-accent", -10, -8),
        (P_l, "P", "geom-point", -8, 17),
        (Q_l, "Q", "geom-point", 6, 17),
        (D_l, "D", "geom-point-assert", 8, -8),
    ):
        g.add_point(pt, nm, cl)
        g.add_label(pt, nm, dx=dx, dy=dy)
    g.add_caption(162, 24, "Classical Euclid I.31 : 2R₁ + R₂ + 5C₁ + 3C₃ (S = 11)")

    g.add_segment((sp.Integer(322), sp.Integer(20)), (sp.Integer(322), sp.Integer(232)), cls="geom-dashed")

    R_t = sp.Integer(96)
    dy_t = sp.sqrt(R_t**2 - sp.Integer(42) ** 2)
    P_r = (sp.Integer(392), sp.Integer(186))
    Q_r = (sp.Integer(392) + R_t, sp.Integer(186))
    A_r = (sp.Integer(434), sp.Integer(186) - dy_t)
    D_r = (sp.Integer(434) + R_t, sp.Integer(186) - dy_t)

    g.add_polygon([P_r, Q_r, D_r, A_r], "APQD", "geom-polygon-accent")
    g.add_segment((sp.Integer(350), sp.Integer(186)), (sp.Integer(612), sp.Integer(186)), ref="BC", cls="geom-bold")
    g.add_segment(P_r, A_r, cls="geom-dashed", ticks=1)
    g.add_segment(P_r, Q_r, cls="geom-bold", ticks=1)
    g.add_segment(Q_r, D_r, cls="geom-dashed", ticks=1)
    g.add_arc(P_r, R_t, -75, 10, cls="geom-arc")
    g.add_arc(A_r, R_t, -20, 20, cls="geom-arc")
    g.add_arc(Q_r, R_t, -82, -45, cls="geom-arc")
    g.add_segment((sp.Integer(356), A_r[1]), (sp.Integer(612), A_r[1]), ref="AD", cls="geom-assert-line")

    for pt, nm, cl, dx, dy in (
        (A_r, "A", "geom-point-accent", -10, -8),
        (P_r, "P", "geom-point", -8, 17),
        (Q_r, "Q", "geom-point", 6, 17),
        (D_r, "D", "geom-point-assert", 10, -8),
    ):
        g.add_point(pt, nm, cl)
        g.add_label(pt, nm, dx=dx, dy=dy, ref=nm)
    g.add_caption(485, 24, "Tarry Rhombus : 2R₁ + R₂ + 3C₁ + 3C₃ (S = 9, E = 5)")
    return g.render()


def build_circle_tangents() -> str:
    """5. Problem XXVI & XXXIX: External tangents to circle O (S = 18) & straightedge polar TT'."""
    g = EuclidGraphicBuilder("fig_circle_tangents", "XXVI", 580, 260)

    A = (sp.Integer(115), sp.Integer(136))
    O_pt = (sp.Integer(375), sp.Integer(136))
    R = sp.Integer(78)
    M = (sp.Integer(245), sp.Integer(136))
    OA = sp.Integer(260)
    x_T = sp.Integer(375) - sp.Rational(R**2, OA)
    y_off = R * sp.sqrt(1 - sp.Rational(R**2, OA**2))
    T = (x_T, sp.Integer(136) - y_off)
    Tp = (x_T, sp.Integer(136) + y_off)

    g.add_circle(O_pt, R, ref="O(R)", cls="geom-bold")
    g.add_circle(M, OA / 2, ref="M(MO)", cls="geom-arc")
    g.add_segment(A, O_pt, ref="OA", cls="geom-dashed")
    g.add_segment(O_pt, T, cls="geom-dashed")
    g.add_segment(O_pt, Tp, cls="geom-dashed")
    T_ext = (A[0] + sp.Rational(6, 5) * (T[0] - A[0]), A[1] + sp.Rational(6, 5) * (T[1] - A[1]))
    Tp_ext = (A[0] + sp.Rational(6, 5) * (Tp[0] - A[0]), A[1] + sp.Rational(6, 5) * (Tp[1] - A[1]))
    g.add_segment(A, T_ext, ref="AT", cls="geom-assert-line")
    g.add_segment(A, Tp_ext, ref="AT'", cls="geom-assert-line")
    g.add_segment(
        (x_T, sp.Integer(38)),
        (x_T, sp.Integer(234)),
        ref="TT'",
        cls="geom-accent-line",
    )

    for pt, nm, cl, dx, dy in (
        (A, "A", "geom-point-accent", -13, 5),
        (M, "M", "geom-point", 0, 17),
        (O_pt, "O", "geom-point", 12, 5),
        (T, "T", "geom-point-assert", 12, -9),
        (Tp, "T'", "geom-point-assert", 14, 17),
    ):
        g.add_point(pt, nm, cl)
        g.add_label(pt, nm, dx=dx, dy=dy, ref=nm)
    g.add_caption(290, 22, "Problems XXVI & XXXIX — Tangents (S = 18) & Straightedge Polar TT' (12R₁ + 7R₂)")
    return g.render()


def build_incircle_lemoine() -> str:
    """6. Problem XXVII: Lemoine's S = 23 Incircle & Incenter X(1) on exact Heronian (13,14,15) triangle."""
    g = EuclidGraphicBuilder("fig_incircle_lemoine", "XXVII", 540, 280)

    s_px = sp.Integer(15)
    B = (sp.Integer(155), sp.Integer(232))
    C = (sp.Integer(155) + 14 * s_px, sp.Integer(232))
    A = (sp.Integer(155) + 5 * s_px, sp.Integer(232) - 12 * s_px)
    I_pt = (sp.Integer(155) + 6 * s_px, sp.Integer(232) - 4 * s_px)
    r_in = 4 * s_px
    D = (I_pt[0], sp.Integer(232))
    F = (B[0] + sp.Rational(6, 13) * (A[0] - B[0]), B[1] + sp.Rational(6, 13) * (A[1] - B[1]))
    E = (C[0] + sp.Rational(8, 15) * (A[0] - C[0]), C[1] + sp.Rational(8, 15) * (A[1] - C[1]))

    g.add_polygon([A, B, C], "ABC", "geom-polygon")
    g.add_segment(A, B, ref="AB", cls="geom-bold")
    g.add_segment(B, C, ref="BC", cls="geom-bold")
    g.add_segment(C, A, ref="CA", cls="geom-bold")

    g.add_arc(B, 46, -68, 4, cls="geom-arc")
    g.add_arc(C, 46, 176, 236, cls="geom-arc")

    B_ray = (B[0] + sp.Rational(7, 5) * (I_pt[0] - B[0]), B[1] + sp.Rational(7, 5) * (I_pt[1] - B[1]))
    C_ray = (C[0] + sp.Rational(6, 5) * (I_pt[0] - C[0]), C[1] + sp.Rational(6, 5) * (I_pt[1] - C[1]))
    g.add_segment(B, B_ray, ref="BI", cls="geom-accent-line")
    g.add_segment(C, C_ray, ref="CI", cls="geom-accent-line")

    g.add_segment(I_pt, D, ref="ID", cls="geom-dashed")
    g.add_right_angle(D, (1, 0), (0, -1), 8.5)
    g.add_circle(I_pt, r_in, ref="I(ID)", cls="geom-assert-line")

    for pt, nm, cl, dx, dy in (
        (A, "A", "geom-point", 0, -9),
        (B, "B", "geom-point", -13, 15),
        (C, "C", "geom-point", 13, 15),
        (I_pt, "I = X(1)", "geom-point-assert", 0, -12),
        (D, "D", "geom-point-accent", 0, 17),
        (E, "E", "geom-point", 13, -3),
        (F, "F", "geom-point", -13, -3),
    ):
        g.add_point(pt, nm.split()[0], cl)
        g.add_label(pt, nm, dx=dx, dy=dy, ref=nm.split()[0])
    g.add_caption(270, 22, "Problem XXVII (Euclid IV.4) — Incircle : 4R₁ + 2R₂ + 11C₁ + 6C₃ (S = 23 vs. S = 30)")
    return g.render()


def build_golden_section_lemoine() -> str:
    """7. Problem XXXVI: Golden section phi of AB in 1 line & 6 circles (2R1 + R2 + 9C1 + 6C3, S = 18)."""
    g = EuclidGraphicBuilder("fig_golden_section_lemoine", "XXXVI", 580, 295)

    a = sp.Integer(80)
    A = (sp.Integer(220), sp.Integer(206))
    B = (sp.Integer(380), sp.Integer(206))
    M = (sp.Integer(300), sp.Integer(206))
    C = (sp.Integer(300), sp.Integer(46))
    r_BC = a * sp.sqrt(5)
    E = (sp.Integer(380) - r_BC, sp.Integer(206))
    phi_seg = a * (sp.sqrt(5) - 1)
    X = (A[0] + phi_seg, sp.Integer(206))

    g.add_segment((sp.Integer(65), sp.Integer(206)), (sp.Integer(505), sp.Integer(206)), cls="geom-line")
    g.add_segment(A, B, ref="AB", cls="geom-bold")
    g.add_segment(A, X, ref="AX", cls="geom-assert-line")
    g.add_segment((sp.Integer(300), sp.Integer(32)), (sp.Integer(300), sp.Integer(258)), ref="MC", cls="geom-accent-line")
    g.add_right_angle(M, (1, 0), (0, -1), 9.0)

    g.add_segment(B, C, ref="BC", cls="geom-dashed")
    g.add_arc(A, 2 * a, -66, -44, cls="geom-arc")
    g.add_arc(B, 2 * a, -136, -114, cls="geom-arc")
    g.add_arc(M, 2 * a, -102, -78, cls="geom-arc")
    g.add_arc(B, r_BC, 174, 236, cls="geom-arc")
    g.add_arc(A, phi_seg, -54, 8, ref="A(ME)", cls="geom-assert-line")

    for pt, nm, cl, dx, dy in (
        (E, "E", "geom-point-accent", -10, -9),
        (A, "A", "geom-point", 0, 19),
        (M, "M", "geom-point", -9, 19),
        (X, "X (φ⁻¹)", "geom-point-assert", 20, -10),
        (B, "B", "geom-point", 10, 19),
        (C, "C", "geom-point-accent", 14, 5),
    ):
        g.add_point(pt, nm.split()[0], cl, 3.6 if "X" in nm else 3.3)
        g.add_label(pt, nm, dx=dx, dy=dy, ref=nm.split()[0])
    g.add_caption(290, 20, "Problem XXXVI (Euclid II.11) — Golden Section in 1 Line & 6 Circles (S = 18 vs. S = 25)")
    g.add_caption(290, 280, "MC = AB, MB = AB/2  ⇒  BC = (√5/2)·AB  ⇒  ME = AX = AB / φ")
    return g.render()


def build_lemoine_symmedian_x6() -> str:
    """8. Problem LI: Lemoine Symmedian Point K = X(6) via antiparallel reflection (S = 27 vs. S = 54)."""
    g = EuclidGraphicBuilder("fig_lemoine_symmedian_x6", "LI", 580, 290)

    s = sp.Integer(16)
    B = (sp.Integer(165), sp.Integer(240))
    C = (sp.Integer(165) + 14 * s, sp.Integer(240))
    A = (sp.Integer(165) + 5 * s, sp.Integer(240) - 12 * s)

    Ma = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    G = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)

    wA, wB, wC = sp.Integer(196), sp.Integer(225), sp.Integer(169)
    wSum = wA + wB + wC
    K = ((wA * A[0] + wB * B[0] + wC * C[0]) / wSum, (wA * A[1] + wB * B[1] + wC * C[1]) / wSum)

    Pa = (A[0] + sp.Rational(9, 13) * (B[0] - A[0]), A[1] + sp.Rational(9, 13) * (B[1] - A[1]))
    Qa = (A[0] + sp.Rational(39, 75) * (C[0] - A[0]), A[1] + sp.Rational(39, 75) * (C[1] - A[1]))
    Mpa = ((Pa[0] + Qa[0]) / 2, (Pa[1] + Qa[1]) / 2)

    t_a = (sp.Integer(240) - A[1]) / (K[1] - A[1])
    Ka = (A[0] + t_a * (K[0] - A[0]), sp.Integer(240))
    Kb = ((wA * A[0] + wC * C[0]) / (wA + wC), (wA * A[1] + wC * C[1]) / (wA + wC))

    g.add_polygon([A, B, C], "ABC", "geom-polygon")
    g.add_segment(A, B, ref="AB", cls="geom-bold")
    g.add_segment(B, C, ref="BC", cls="geom-bold")
    g.add_segment(C, A, ref="CA", cls="geom-bold")

    g.add_segment(A, Ma, ref="AMa", cls="geom-dashed")
    g.add_segment(Pa, Qa, ref="PaQa", cls="geom-accent-line")
    g.add_segment(A, Ka, ref="AK", cls="geom-assert-line")
    g.add_segment(B, Kb, ref="BK", cls="geom-assert-line")

    for pt, nm, cl, dx, dy in (
        (A, "A", "geom-point", 0, -9),
        (B, "B", "geom-point", -13, 15),
        (C, "C", "geom-point", 13, 15),
        (Pa, "Pₐ", "geom-point-accent", -15, 3),
        (Qa, "Qₐ", "geom-point-accent", 16, -2),
        (Mpa, "M'ₐ", "geom-point-accent", -16, -5),
        (Ma, "Mₐ", "geom-point", 0, 17),
        (G, "G = X(2)", "geom-point", 32, -4),
        (K, "K = X(6)", "geom-point-assert", -33, 13),
    ):
        ref_id = nm.split()[0].replace("ₐ", "a").replace("'", "p")
        g.add_point(pt, ref_id, cl, 3.8 if "X(6)" in nm else 3.2)
        g.add_label(pt, nm, dx=dx, dy=dy, ref=ref_id)
    g.add_caption(290, 22, "Problem LI — Lemoine Symmedian Point K = X(6) : 4R₁ + 2R₂ + 13C₁ + 8C₃ (S = 27)")
    g.add_caption(290, 276, "Antiparallel PₐQₐ bisected by symmedian AK (isogonal to median AMₐ through G = X(2))")
    return g.render()


def build_mascheroni_steiner_duality() -> str:
    """9. Unit 4: Mascheroni compass-only parallel point vs. Poncelet-Steiner fixed-circle ruler parallel."""
    g = EuclidGraphicBuilder("fig_mascheroni_steiner_duality", "Unit-IV", 650, 265)

    A_m = (sp.Integer(66), sp.Integer(194))
    B_m = (sp.Integer(192), sp.Integer(194))
    C_m = (sp.Integer(104), sp.Integer(96))
    D_m = (C_m[0] + (B_m[0] - A_m[0]), C_m[1])
    r_AC = sp.sqrt((C_m[0] - A_m[0]) ** 2 + (C_m[1] - A_m[1]) ** 2)
    r_AB = B_m[0] - A_m[0]

    g.add_arc(B_m, r_AC, -112, -32, ref="B(AC)", cls="geom-arc")
    g.add_arc(C_m, r_AB, -28, 36, ref="C(AB)", cls="geom-assert-line")
    g.add_segment(A_m, B_m, cls="geom-dashed", ticks=1)
    g.add_segment(C_m, D_m, cls="geom-dashed", ticks=1)

    for pt, nm, cl, dx, dy in (
        (A_m, "A", "geom-point", -10, 16),
        (B_m, "B", "geom-point", 10, 16),
        (C_m, "C", "geom-point-accent", -12, -6),
        (D_m, "D", "geom-point-assert", 13, -6),
    ):
        g.add_point(pt, nm, cl, 3.6)
        g.add_label(pt, nm, dx=dx, dy=dy)
    g.add_caption(158, 22, "Mascheroni (1797) — Compass Alone")
    g.add_caption(158, 248, "5C₁ + 2C₃ (S = 7, 0 lines): (C, D) ∥ (A, B)")

    g.add_segment((sp.Integer(312), sp.Integer(18)), (sp.Integer(312), sp.Integer(250)), cls="geom-dashed")

    M_s = (sp.Integer(476), sp.Integer(182))
    R_s = sp.Integer(46)
    a_pt = (M_s[0] - R_s, M_s[1])
    b_pt = (M_s[0] + R_s, M_s[1])
    V = (sp.Integer(484), sp.Integer(38))
    P_s = (a_pt[0] + sp.Rational(13, 20) * (V[0] - a_pt[0]), a_pt[1] + sp.Rational(13, 20) * (V[1] - a_pt[1]))
    Q_s = (b_pt[0] + sp.Rational(13, 20) * (V[0] - b_pt[0]), b_pt[1] + sp.Rational(13, 20) * (V[1] - b_pt[1]))

    x_sym, y_sym = sp.symbols("x y")
    eq1 = sp.Eq((y_sym - P_s[1]) * (b_pt[0] - P_s[0]), (x_sym - P_s[0]) * (b_pt[1] - P_s[1]))
    eq2 = sp.Eq((y_sym - V[1]) * (M_s[0] - V[0]), (x_sym - V[0]) * (M_s[1] - V[1]))
    sol = sp.solve([eq1, eq2], (x_sym, y_sym))
    Kq = (sol[x_sym], sol[y_sym])

    g.add_circle(M_s, R_s, ref="Omega", cls="geom-accent-line")
    g.add_segment((sp.Integer(352), M_s[1]), (sp.Integer(608), M_s[1]), ref="ab", cls="geom-bold")
    g.add_segment(a_pt, V, cls="geom-line")
    g.add_segment(b_pt, V, cls="geom-line")
    g.add_segment(M_s, V, cls="geom-dashed")
    g.add_segment(P_s, b_pt, cls="geom-line")
    g.add_segment(a_pt, Q_s, cls="geom-line")
    g.add_segment((sp.Integer(358), P_s[1]), (sp.Integer(602), Q_s[1]), ref="PQ_par", cls="geom-assert-line")

    for pt, nm, cl, dx, dy in (
        (M_s, "M", "geom-point-accent", 5, 17),
        (a_pt, "a", "geom-point", -11, 15),
        (b_pt, "b", "geom-point", 11, 15),
        (V, "S", "geom-point", 12, 2),
        (P_s, "P", "geom-point-accent", -13, -5),
        (Q_s, "P'", "geom-point-assert", 14, -5),
        (Kq, "K", "geom-point", 12, -2),
    ):
        g.add_point(pt, nm, cl, 3.3)
        g.add_label(pt, nm, dx=dx, dy=dy)
    g.add_caption(480, 22, "Poncelet–Steiner (1833) — Straightedge + Fixed Circle M")
    g.add_caption(480, 248, "11R₁ + 6R₂ (S = 17, 0 circles): PP' ∥ diameter aMb")
    return g.render()


def main() -> None:
    """Build all 9 standalone .euclid-graphic SVG plates."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    figures = {
        "fig_elementary_operations.svg": build_elementary_operations(),
        "fig_perpendicular_bisector.svg": build_perpendicular_bisector(),
        "fig_perpendicular_external.svg": build_perpendicular_external(),
        "fig_parallel_comparison.svg": build_parallel_comparison(),
        "fig_circle_tangents.svg": build_circle_tangents(),
        "fig_incircle_lemoine.svg": build_incircle_lemoine(),
        "fig_golden_section_lemoine.svg": build_golden_section_lemoine(),
        "fig_lemoine_symmedian_x6.svg": build_lemoine_symmedian_x6(),
        "fig_mascheroni_steiner_duality.svg": build_mascheroni_steiner_duality(),
    }
    for name, content in figures.items():
        target = OUT_DIR / name
        target.write_text(content, encoding="utf-8")
        print(f"Wrote {target.relative_to(REPO_ROOT)} ({len(content)} bytes)")


if __name__ == "__main__":
    main()
