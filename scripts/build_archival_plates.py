"""Extract Lemoine's 11 original 1892/1893 archival plates and generate exact SymPy-calibrated SVGs.

Each original printed diagram (FIG. 1 - FIG. 11) from the 300-DPI scans under
``resources/geometrographie/folios/`` is paired inside its atomic leaf directory with:

1. ``<NNNN>.g1.png`` — contrast-normalized archival bitmap crop preserving original craftsmanship.
2. ``<NNNN>.g1.svg`` — calibrated 5-layer theme-adaptive ``.euclid-graphic`` SVG vectorization
   computed with exact SymPy symbolic algebra matching the orientation and labels of the 1893 plate.
"""

from __future__ import annotations

import html
import math
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import sympy as sp
from PIL import Image, ImageOps

REPO_ROOT = Path(__file__).resolve().parents[1]
FOLIOS_DIR = REPO_ROOT / "resources" / "geometrographie" / "folios"
CODEX_DIR = REPO_ROOT / "docsrc" / "geometrographie"

Pt = tuple[sp.Expr, sp.Expr]

# Target leaf directory for each of Lemoine's 11 printed figures (FIG. 1 - FIG. 11)
PLATE_SPECS: tuple[tuple[str, str, tuple[int, int, int, int]], ...] = (
    ("0031", "part_03_circles_and_tangency/11_incircle_xxvii", (855, 735, 1515, 1455)),
    ("0032", "part_03_circles_and_tangency/12_capable_segment_xxviii", (195, 865, 1000, 1515)),
    ("0034", "part_03_circles_and_tangency/13_common_tangents_xxix", (225, 600, 1475, 1215)),
    ("0037", "part_03_circles_and_tangency/15_fourth_and_third_proportionals_xxxiii_xxxiv", (710, 1455, 1480, 1995)),
    ("0038", "part_03_circles_and_tangency/15_fourth_and_third_proportionals_xxxiii_xxxiv", (180, 310, 725, 795)),
    ("0042", "part_03_circles_and_tangency/16_mean_proportional_xxxv", (185, 1165, 795, 1775)),
    ("0043", "part_03_circles_and_tangency/16_mean_proportional_xxxv", (880, 370, 1495, 925)),
    ("0044", "part_03_circles_and_tangency/17_golden_section_and_inaccessible_xxxvi_xxxvii", (190, 340, 875, 1015)),
    ("0050", "part_03_circles_and_tangency/19_square_and_ellipse_axes_xlvii_xlviii", (150, 585, 820, 1125)),
    ("0054", "part_04_triangle_and_reflections/20_principles_and_rational_division", (215, 1135, 995, 1630)),
    ("0056", "part_04_triangle_and_reflections/21_normal_coordinates_xlix", (415, 915, 1295, 1690)),
)


def fxy(p: Pt | tuple[float, float]) -> tuple[float, float]:
    """Convert an exact SymPy or numeric 2D point to float SVG coordinates."""
    return (float(sp.N(p[0], 20)), float(sp.N(p[1], 20)))


def dist(p1: Pt, p2: Pt) -> sp.Expr:
    """Exact Euclidean distance between two SymPy points."""
    return sp.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def add_vec(p: Pt, dx: sp.Expr, dy: sp.Expr) -> Pt:
    """Translate a point by exact vector (dx, dy)."""
    return (sp.simplify(p[0] + dx), sp.simplify(p[1] + dy))


def ray_point(origin: Pt, through: Pt, length: sp.Expr) -> Pt:
    """Point at exact distance ``length`` from ``origin`` along ray ``origin -> through``."""
    d = dist(origin, through)
    ux = (through[0] - origin[0]) / d
    uy = (through[1] - origin[1]) / d
    return (sp.simplify(origin[0] + length * ux), sp.simplify(origin[1] + length * uy))


def line_intersect(p1: Pt, p2: Pt, p3: Pt, p4: Pt) -> Pt:
    """Exact intersection of lines p1-p2 and p3-p4."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    return (sp.simplify(px), sp.simplify(py))


def circle_circle_intersect(c1: Pt, r1: sp.Expr, c2: Pt, r2: sp.Expr) -> tuple[Pt, Pt]:
    """Exact intersections of circles (c1, r1) and (c2, r2)."""
    x1, y1 = fxy(c1)
    x2, y2 = fxy(c2)
    rv1 = float(sp.N(r1, 20))
    rv2 = float(sp.N(r2, 20))
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy)
    a = (rv1 * rv1 - rv2 * rv2 + d * d) / (2.0 * d)
    h = math.sqrt(max(0.0, rv1 * rv1 - a * a))
    xm = x1 + a * dx / d
    ym = y1 + a * dy / d
    rx = -dy * (h / d)
    ry = dx * (h / d)
    return (
        (sp.nsimplify(xm + rx, tolerance=1e-9), sp.nsimplify(ym + ry, tolerance=1e-9)),
        (sp.nsimplify(xm - rx, tolerance=1e-9), sp.nsimplify(ym - ry, tolerance=1e-9)),
    )


def circle_circle_exact(c1: Pt, r1: sp.Expr, c2: Pt, r2: sp.Expr) -> tuple[Pt, Pt]:
    """Exact symbolic circle-circle intersections over Q/radicals."""
    d = dist(c1, c2)
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = sp.sqrt(sp.simplify(r1**2 - a**2))
    dx = (c2[0] - c1[0]) / d
    dy = (c2[1] - c1[1]) / d
    xm = c1[0] + a * dx
    ym = c1[1] + a * dy
    p_plus = (sp.simplify(xm - h * dy), sp.simplify(ym + h * dx))
    p_minus = (sp.simplify(xm + h * dy), sp.simplify(ym - h * dx))
    return p_plus, p_minus


def deg_of(center: Pt, pt: Pt) -> float:
    """SVG angle in degrees from ``center`` to ``pt`` (y-down)."""
    cx, cy = fxy(center)
    px, py = fxy(pt)
    return math.degrees(math.atan2(py - cy, px - cx))


def extend_seg(p1: Pt, p2: Pt, pad1: float = 0.0, pad2: float = 0.0) -> tuple[Pt, Pt]:
    """Extend segment p1->p2 backward by pad1 and forward by pad2 in SVG units."""
    x1, y1 = fxy(p1)
    x2, y2 = fxy(p2)
    d = math.hypot(x2 - x1, y2 - y1) or 1.0
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    return (
        (sp.Float(x1 - pad1 * ux), sp.Float(y1 - pad1 * uy)),
        (sp.Float(x2 + pad2 * ux), sp.Float(y2 + pad2 * uy)),
    )


_PRES_ATTRS: dict[str, str] = {
    "geom-line": 'stroke="#18181b" stroke-width="1.7" stroke-linecap="round"',
    "geom-bold": 'stroke="#18181b" stroke-width="2.25" stroke-linecap="round"',
    "geom-dashed": 'stroke="#18181b" stroke-width="1.3" stroke-dasharray="5,3.5" stroke-linecap="round" opacity="0.78"',
    "geom-accent-line": 'stroke="#c88a1e" stroke-width="2.05" stroke-linecap="round"',
    "geom-assert-line": 'stroke="#16a34a" stroke-width="2.25" stroke-linecap="round"',
    "geom-circle": 'stroke="#18181b" stroke-width="1.7"',
    "geom-arc": 'stroke="#c88a1e" stroke-width="1.45" stroke-dasharray="4.5,3" stroke-linecap="round" opacity="0.88"',
    "geom-ang-arc": 'stroke="#16a34a" stroke-width="1.6" stroke-linecap="round"',
    "geom-polygon": 'fill="#18181b" fill-opacity="0.045" stroke="none"',
    "geom-point": 'fill="#18181b" stroke="#ffffff" stroke-width="1.1"',
    "geom-point-accent": 'fill="#c88a1e" stroke="#ffffff" stroke-width="1.1"',
    "geom-point-assert": 'fill="#16a34a" stroke="#ffffff" stroke-width="1.2"',
}


@dataclass
class ArchivalPlateSVG:
    """Calibrated 5-layer interactive `.euclid-graphic` SVG builder for archival plates."""

    folio: str
    graphic: str
    title: str
    width: int
    height: int
    elements: list[str] = field(default_factory=list)
    graphics: list[str] = field(default_factory=list)
    highlights: list[str] = field(default_factory=list)
    points: list[str] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)

    def add_polygon(self, pts: list[Pt], ref: str, cls: str = "geom-polygon") -> None:
        coords = " ".join(f"{fxy(p)[0]:.2f},{fxy(p)[1]:.2f}" for p in pts)
        pres = _PRES_ATTRS.get(cls, "")
        self.elements.append(
            f'    <polygon points="{coords}" {pres} class="{cls}" data-ref="{html.escape(ref, quote=True)}" />'
        )

    def add_segment(
        self,
        p1: Pt | tuple[float, float],
        p2: Pt | tuple[float, float],
        ref: str | None = None,
        cls: str = "geom-line",
        ticks: int = 0,
    ) -> None:
        x1, y1 = fxy(p1)
        x2, y2 = fxy(p2)
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        pres = _PRES_ATTRS.get(cls, "")
        attrs = [
            f'd="M {x1:.2f} {y1:.2f} L {mx:.2f} {my:.2f} L {x2:.2f} {y2:.2f}"',
            'fill="none"',
            pres,
            f'class="{cls}"',
        ]
        if ticks in (1, 2, 3):
            attrs.append(f'marker-mid="url(#geom-tick-{ticks})"')
        if ref:
            attrs.append(f'data-ref="{html.escape(ref, quote=True)}"')
            self.elements.append(f"    <path {' '.join(a for a in attrs if a)} />")
        else:
            self.graphics.append(f"    <path {' '.join(a for a in attrs if a)} />")

    def add_circle(
        self,
        center: Pt | tuple[float, float],
        radius: sp.Expr | float,
        ref: str | None = None,
        cls: str = "geom-circle",
    ) -> None:
        cx, cy = fxy(center)
        r = float(sp.N(radius, 20))
        pres = _PRES_ATTRS.get(cls, "")
        ref_attr = f' data-ref="{html.escape(ref, quote=True)}"' if ref else ""
        target = self.elements if ref else self.graphics
        target.append(
            f'    <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="none" {pres} class="{cls}"{ref_attr} />'
        )

    def add_arc(
        self,
        center: Pt | tuple[float, float],
        radius: sp.Expr | float,
        deg_start: float,
        deg_end: float,
        ref: str | None = None,
        cls: str = "geom-arc",
    ) -> None:
        """Draw clockwise arc from deg_start to deg_end in SVG y-down coords."""
        cx, cy = fxy(center)
        r = float(sp.N(radius, 20))
        a1 = math.radians(deg_start)
        a2 = math.radians(deg_end)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        delta = (deg_end - deg_start) % 360.0
        large = 1 if delta > 180.0 else 0
        pres = _PRES_ATTRS.get(cls, "")
        ref_attr = f' data-ref="{html.escape(ref, quote=True)}"' if ref else ""
        target = self.elements if ref else self.graphics
        target.append(
            f'    <path d="M {x1:.2f} {y1:.2f} A {r:.2f} {r:.2f} 0 {large} 1 {x2:.2f} {y2:.2f}" '
            f'fill="none" {pres} class="{cls}"{ref_attr} />'
        )

    def add_tick_arc(
        self,
        center: Pt | tuple[float, float],
        pt: Pt | tuple[float, float],
        span_deg: float = 18.0,
        ref: str | None = None,
        cls: str = "geom-arc",
    ) -> None:
        """Draw a short compass-strike arc centered at ``center`` passing through ``pt``."""
        cx, cy = fxy(center)
        px, py = fxy(pt)
        r = math.hypot(px - cx, py - cy)
        ang = math.degrees(math.atan2(py - cy, px - cx))
        self.add_arc(center, r, ang - span_deg / 2.0, ang + span_deg / 2.0, ref=ref, cls=cls)

    def add_highlight_arc(
        self,
        center: Pt | tuple[float, float],
        radius: float,
        deg_start: float,
        deg_end: float,
    ) -> None:
        cx, cy = fxy(center)
        a1, a2 = math.radians(deg_start), math.radians(deg_end)
        x1, y1 = cx + radius * math.cos(a1), cy + radius * math.sin(a1)
        x2, y2 = cx + radius * math.cos(a2), cy + radius * math.sin(a2)
        delta = (deg_end - deg_start) % 360.0
        large = 1 if delta > 180.0 else 0
        pres = _PRES_ATTRS["geom-ang-arc"]
        self.highlights.append(
            f'    <path d="M {x1:.2f} {y1:.2f} A {radius:.2f} {radius:.2f} 0 {large} 1 {x2:.2f} {y2:.2f}" '
            f'fill="none" {pres} class="geom-ang-arc" />'
        )

    def add_right_angle(
        self,
        vertex: Pt | tuple[float, float],
        u_pt: Pt | tuple[float, float],
        v_pt: Pt | tuple[float, float],
        size: float = 9.0,
    ) -> None:
        vx, vy = fxy(vertex)
        ux, uy = fxy(u_pt)[0] - vx, fxy(u_pt)[1] - vy
        wx, wy = fxy(v_pt)[0] - vx, fxy(v_pt)[1] - vy
        un = math.hypot(ux, uy) or 1.0
        wn = math.hypot(wx, wy) or 1.0
        ux, uy = ux / un * size, uy / un * size
        wx, wy = wx / wn * size, wy / wn * size
        p1x, p1y = vx + ux, vy + uy
        p2x, p2y = vx + ux + wx, vy + uy + wy
        p3x, p3y = vx + wx, vy + wy
        pres = _PRES_ATTRS["geom-ang-arc"]
        self.highlights.append(
            f'    <path d="M {p1x:.2f} {p1y:.2f} L {p2x:.2f} {p2y:.2f} L {p3x:.2f} {p3y:.2f}" '
            f'fill="none" {pres} class="geom-ang-arc" />'
        )

    def add_point(
        self,
        pt: Pt | tuple[float, float],
        ref: str,
        label: str | None = None,
        dx: float = 0.0,
        dy: float = -13.0,
        cls: str = "geom-point",
        radius: float = 3.2,
    ) -> None:
        x, y = fxy(pt)
        esc_ref = html.escape(ref, quote=True)
        pres = _PRES_ATTRS.get(cls, "")
        self.points.append(
            f'    <circle cx="{x:.2f}" cy="{y:.2f}" r="{radius:.2f}" {pres} class="{cls}" data-ref="{esc_ref}" />'
        )
        if label is not None:
            self.labels.append(
                f'    <text x="{x + dx:.2f}" y="{y + dy:.2f}" text-anchor="middle" '
                f'dominant-baseline="central" font-size="13.5" font-weight="700" font-style="italic" '
                f'fill="#18181b" class="geom-label" data-ref="{esc_ref}">{html.escape(label)}</text>'
            )

    def add_caption(self, text: str, x: float | None = None, y: float | None = None) -> None:
        cx = self.width / 2.0 if x is None else x
        cy = self.height - 16.0 if y is None else y
        self.labels.append(
            f'    <text x="{cx:.2f}" y="{cy:.2f}" text-anchor="middle" '
            f'dominant-baseline="central" font-size="10.5" font-weight="700" '
            f'fill="#18181b" opacity="0.85" class="geom-caption">{html.escape(text)}</text>'
        )

    def render(self) -> str:
        gid = f"{self.folio}.{self.graphic}"
        parts: list[str] = [
            (
                f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
                f'width="{self.width}" height="{self.height}" class="euclid-graphic" '
                f'data-graphic-id="{gid}" data-folio="{self.folio}" data-graphic="{self.graphic}" '
                f'role="img" aria-label="{html.escape(self.title, quote=True)}">'
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
            "      font-family: 'Fira Sans Condensed', 'Fira Sans', Georgia, sans-serif;",
            "      background-color: var(--geom-bg);",
            "    }",
            "    .geom-line { stroke: #18181b; stroke: var(--geom-fg, #18181b); stroke-width: 1.7; stroke-linecap: round; fill: none; }",
            "    .geom-bold { stroke: #18181b; stroke: var(--geom-fg, #18181b); stroke-width: 2.25; stroke-linecap: round; fill: none; }",
            "    .geom-dashed { stroke: #18181b; stroke: var(--geom-fg, #18181b); stroke-width: 1.3; stroke-dasharray: 5, 3.5; stroke-linecap: round; fill: none; opacity: 0.78; }",
            "    .geom-accent-line { stroke: #c88a1e; stroke: var(--geom-accent, #c88a1e); stroke-width: 2.05; stroke-linecap: round; fill: none; }",
            "    .geom-assert-line { stroke: #16a34a; stroke: var(--geom-assert, #16a34a); stroke-width: 2.25; stroke-linecap: round; fill: none; }",
            "    .geom-circle { stroke: #18181b; stroke: var(--geom-fg, #18181b); stroke-width: 1.7; fill: none; }",
            "    .geom-arc { stroke: #c88a1e; stroke: var(--geom-accent, #c88a1e); stroke-width: 1.45; stroke-dasharray: 4.5, 3; stroke-linecap: round; fill: none; opacity: 0.88; }",
            "    .geom-ang-arc { stroke: #16a34a; stroke: var(--geom-assert, #16a34a); stroke-width: 1.6; stroke-linecap: round; fill: none; }",
            "    .geom-polygon { fill: #18181b; fill: var(--geom-poly-fill, #18181b); fill-opacity: 0.045; stroke: none; }",
            "    .geom-point { fill: #18181b; fill: var(--geom-fg, #18181b); stroke: #ffffff; stroke: var(--geom-point-stroke, #ffffff); stroke-width: 1.1; }",
            "    .geom-point-accent { fill: #c88a1e; fill: var(--geom-accent, #c88a1e); stroke: #ffffff; stroke: var(--geom-point-stroke, #ffffff); stroke-width: 1.1; }",
            "    .geom-point-assert { fill: #16a34a; fill: var(--geom-assert, #16a34a); stroke: #ffffff; stroke: var(--geom-point-stroke, #ffffff); stroke-width: 1.2; }",
            "    .geom-label { font-size: 13.5px; font-weight: 700; font-style: italic; fill: #18181b; fill: var(--geom-fg, #18181b); user-select: none; }",
            "    .geom-caption { font-size: 10.5px; font-weight: 700; fill: #18181b; fill: var(--geom-fg, #18181b); opacity: 0.85; user-select: none; letter-spacing: 0.02em; }",
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
        return "\n".join(parts)


def build_0031_fig01() -> str:
    """FIG. 1 (fol. 0031, p. 15) — Problem XXVII: Incircle of triangle ABC."""
    g = ArchivalPlateSVG("0031", "g1", "FIG. 1 — Problem XXVII: Incircle of triangle ABC", 520, 560)
    # Exact triangle matching 1893 orientation (C bottom-left, B bottom-right, A upper-center)
    C: Pt = (sp.Integer(72), sp.Integer(476))
    B: Pt = (sp.Integer(378), sp.Integer(476))
    A: Pt = (sp.Integer(274), sp.Integer(274))

    a = dist(B, C)
    b = dist(C, A)
    c = dist(A, B)
    s = (a + b + c) / 2

    # Ray BA extended past A: AD = AC = b, BE = BC = a
    D = ray_point(A, add_vec(A, A[0] - B[0], A[1] - B[1]), b)
    E = ray_point(B, A, a)
    r_de = dist(D, E)  # = b + c - a = 2(s - a)

    # Circle A(DE) cuts AB at R' and AC at Q'
    Rp = ray_point(A, B, r_de)
    Qp = ray_point(A, C, r_de)
    R = ray_point(A, B, s - a)
    Q = ray_point(A, C, s - a)
    P = ray_point(B, C, s - b)

    # Exact incenter O = (aA + bB + cC) / (a + b + c)
    perim = a + b + c
    O: Pt = (
        sp.simplify((a * A[0] + b * B[0] + c * C[0]) / perim),
        sp.simplify((a * A[1] + b * B[1] + c * C[1]) / perim),
    )
    inradius = dist(O, P)

    # Intersections of A(DE) with R'(DE) and Q'(DE)
    r1, r2 = circle_circle_intersect(A, r_de, Rp, r_de)
    q1, q2 = circle_circle_intersect(A, r_de, Qp, r_de)

    g.add_polygon([A, B, C], "ABC")
    g.add_segment(B, D, "BD", cls="geom-line")
    g.add_segment(A, B, "AB", cls="geom-bold")
    g.add_segment(B, C, "BC", cls="geom-bold")
    g.add_segment(C, A, "CA", cls="geom-bold")

    # Construction arcs matching Lemoine's exact strokes
    g.add_tick_arc(A, D, span_deg=18.0, ref="A(AC)")
    g.add_tick_arc(B, E, span_deg=16.0, ref="B(BC)")
    ang_r_min = min(deg_of(A, r1) % 360.0, deg_of(A, r2) % 360.0)
    ang_q_max = max(deg_of(A, q1) % 360.0, deg_of(A, q2) % 360.0)
    g.add_arc(A, r_de, ang_r_min - 14.0, ang_q_max + 14.0, ref="A(DE)")
    g.add_tick_arc(Rp, r1, span_deg=24.0)
    g.add_tick_arc(Rp, r2, span_deg=24.0)
    g.add_tick_arc(Qp, q1, span_deg=24.0)
    g.add_tick_arc(Qp, q2, span_deg=24.0)

    # Perpendicular bisectors through O (R-locus and Q-locus)
    rr1, rr2 = extend_seg(r1, r2, 16, 16)
    qq1, qq2 = extend_seg(q1, q2, 16, 16)
    g.add_segment(rr1, rr2, "OR", cls="geom-dashed")
    g.add_segment(qq1, qq2, "OQ", cls="geom-dashed")

    # Incircle O(OR)
    g.add_circle(O, inradius, "O(OR)", cls="geom-assert-line")
    g.add_right_angle(P, O, C, size=8.0)

    g.add_point(D, "D", "D", dx=-12, dy=-12)
    g.add_point(E, "E", "E", dx=13, dy=-6)
    g.add_point(A, "A", "A", dx=14, dy=-4)
    g.add_point(B, "B", "B", dx=14, dy=4)
    g.add_point(C, "C", "C", dx=-15, dy=4)
    g.add_point(P, "P", "P", dx=0, dy=15, cls="geom-point-accent")
    g.add_point(Q, "Q", "Q", dx=-14, dy=-8, cls="geom-point-accent")
    g.add_point(Qp, "Q'", "Q'", dx=-15, dy=-6)
    g.add_point(R, "R", "R", dx=14, dy=-6, cls="geom-point-accent")
    g.add_point(Rp, "R'", "R'", dx=15, dy=-8)
    g.add_point(O, "O", "O", dx=1, dy=-14, cls="geom-point-assert", radius=3.5)

    g.add_caption("FIG. 1 — Problem XXVII : Incircle of △ABC  (4R₁ + 2R₂ + 11C₁ + 6C₃, S = 23)")
    return g.render()


def build_0032_fig02() -> str:
    """FIG. 2 (fol. 0032, p. 16) — Problem XXVIII: Segment capable of angle DCE on AB."""
    g = ArchivalPlateSVG("0032", "g1", "FIG. 2 — Problem XXVIII: Segment capable of a given angle", 600, 480)

    # Left panel: horizontal chord AB
    A: Pt = (sp.Integer(82), sp.Integer(254))
    B: Pt = (sp.Integer(248), sp.Integer(254))
    ab = dist(A, B)  # 166

    # Angle alpha = 42 deg (matches 1893 engraving geometry)
    alpha = math.radians(42.0)
    # P (above) and Q (below) are intersections of A(AB) and B(AB)
    P, Q = circle_circle_exact(A, ab, B, ab)
    if fxy(P)[1] > fxy(Q)[1]:
        P, Q = Q, P

    # D on A(AB) at angle 2*alpha = 84 deg above AB (just left of P which is at 60 deg)
    ang_d = -2.0 * alpha
    D: Pt = (
        sp.Float(fxy(A)[0] + float(ab) * math.cos(ang_d)),
        sp.Float(fxy(A)[1] + float(ab) * math.sin(ang_d)),
    )
    # O is intersection of BD and PQ
    O = line_intersect(B, D, P, Q)
    r_cap = dist(O, A)

    # Right panel: angle DCE = alpha, arc C(AB) cutting CD at D_r, CE at E_r, doubled to F_r
    Cr: Pt = (sp.Integer(372), sp.Integer(254))
    Er: Pt = (sp.Float(372.0 + float(ab)), sp.Integer(254))
    Dr: Pt = (
        sp.Float(372.0 + float(ab) * math.cos(-alpha)),
        sp.Float(254.0 + float(ab) * math.sin(-alpha)),
    )
    Fr: Pt = (
        sp.Float(372.0 + float(ab) * math.cos(alpha)),
        sp.Float(254.0 + float(ab) * math.sin(alpha)),
    )
    # Extended rays for right panel
    _, cd_end = extend_seg(Cr, Dr, 0, 56)
    _, ce_end = extend_seg(Cr, Er, 0, 42)

    # Left panel drawing
    g.add_segment(A, B, "AB", cls="geom-bold")
    p_top, q_bot = extend_seg(P, Q, 42, 26)
    g.add_segment(p_top, q_bot, "PQ", cls="geom-dashed")
    b_ext, d_ext = extend_seg(B, D, 0, 16)
    g.add_segment(b_ext, d_ext, "BD", cls="geom-dashed")

    # Construction arcs on left panel
    g.add_arc(A, ab, math.degrees(ang_d) - 14, -46, ref="A(AB)")
    g.add_tick_arc(A, Q, span_deg=24.0)
    g.add_tick_arc(B, P, span_deg=20.0)
    g.add_tick_arc(B, Q, span_deg=24.0)
    g.add_tick_arc(B, D, span_deg=18.0)

    # Capable circular segment O(OA) from A clockwise over the top to B
    g.add_arc(O, r_cap, deg_of(O, A), deg_of(O, B), ref="O(OA)", cls="geom-assert-line")

    # Right panel drawing
    g.add_segment(Cr, cd_end, "CD", cls="geom-bold")
    g.add_segment(Cr, ce_end, "CE", cls="geom-bold")
    g.add_arc(Cr, ab, -52, 52, ref="C(AB)")
    g.add_tick_arc(Er, Fr, span_deg=26.0)
    g.add_highlight_arc(Cr, 34.0, -42.0, 0.0)

    # Points & labels
    g.add_point(A, "A", "A", dx=-12, dy=13)
    g.add_point(B, "B", "B", dx=12, dy=13)
    g.add_point(P, "P", "P", dx=13, dy=-10)
    g.add_point(Q, "Q", "Q", dx=-11, dy=14)
    g.add_point(D, "D", "D", dx=-10, dy=-13, cls="geom-point-accent")
    g.add_point(O, "O", "O", dx=12, dy=-5, cls="geom-point-assert", radius=3.5)

    g.add_point(Cr, "C", "C", dx=-14, dy=0)
    g.add_point(Dr, "D_ang", "D", dx=0, dy=-15, cls="geom-point-accent")
    g.add_point(Er, "E", "E", dx=13, dy=-12)
    g.add_point(Fr, "F", "F", dx=1, dy=16, cls="geom-point-accent")

    g.add_caption("FIG. 2 — Problem XXVIII : Segment capable of ∠DCE on AB  (4R₁ + 2R₂ + 11C₁ + 6C₃, S = 23)")
    return g.render()


def build_0034_fig03() -> str:
    """FIG. 3 (fol. 0034, p. 18) — Problem XXIX (2nd method): Centers of similitude V, V1."""
    g = ArchivalPlateSVG("0034", "g1", "FIG. 3 — Problem XXIX: Homothety centers V and V1 of circles O and O'", 680, 340)

    cy = sp.Integer(160)
    O: Pt = (sp.Integer(170), cy)
    R = sp.Integer(118)
    Op: Pt = (sp.Integer(392), cy)
    r = sp.Integer(62)

    A1: Pt = (O[0] - R, cy)
    A: Pt = (O[0] + R, cy)
    Ap: Pt = (Op[0] - r, cy)
    Ap1: Pt = (Op[0] + r, cy)

    # Exact 60-degree points: A(AO) cuts O at alpha (+60 above OA), A1(A1O) cuts at alpha1 (-120)
    s3 = sp.sqrt(3)
    alpha: Pt = (O[0] + R / 2, cy - R * s3 / 2)
    alpha1: Pt = (O[0] - R / 2, cy + R * s3 / 2)
    alphap: Pt = (Op[0] + r / 2, cy - r * s3 / 2)

    # Centers of similitude V (external) and V1 (internal)
    V = line_intersect(alpha, alphap, O, Op)
    V1 = line_intersect(alpha1, alphap, O, Op)

    # Circles
    g.add_circle(O, R, "O", cls="geom-bold")
    g.add_circle(Op, r, "O'", cls="geom-bold")

    # Line of centers & homothety transversals
    l_start, l_end = extend_seg(A1, V, 18, 12)
    g.add_segment(l_start, l_end, "OO'", cls="geom-dashed")
    g.add_segment(alpha, V, "αV", cls="geom-accent-line")
    g.add_segment(alpha1, alphap, "α₁α'", cls="geom-accent-line")

    # Compass strike arcs locating alpha, alpha1, alpha'
    g.add_tick_arc(A, alpha, span_deg=24.0, ref="A(AO)")
    g.add_tick_arc(A1, alpha1, span_deg=24.0, ref="A₁(A₁O)")
    g.add_tick_arc(Ap1, alphap, span_deg=30.0, ref="A'₁(A'₁O')")

    # Points & labels matching 1893 scan
    g.add_point(A1, "A₁", "A₁", dx=-14, dy=15)
    g.add_point(O, "O", "O", dx=0, dy=15)
    g.add_point(A, "A", "A", dx=-12, dy=15)
    g.add_point(V1, "V₁", "V₁", dx=0, dy=16, cls="geom-point-assert", radius=3.5)
    g.add_point(Ap, "A'", "A'", dx=12, dy=15)
    g.add_point(Op, "O'", "O'", dx=0, dy=15)
    g.add_point(Ap1, "A'₁", "A'₁", dx=14, dy=15)
    g.add_point(V, "V", "V", dx=2, dy=16, cls="geom-point-assert", radius=3.5)
    g.add_point(alpha, "α", "α", dx=2, dy=-14, cls="geom-point-accent")
    g.add_point(alpha1, "α₁", "α₁", dx=-4, dy=16, cls="geom-point-accent")
    g.add_point(alphap, "α'", "α'", dx=4, dy=-15, cls="geom-point-accent")

    g.add_caption("FIG. 3 — Problem XXIX (2nd Method) : Centers of Similitude V, V₁ of Circles O and O'")
    return g.render()


def build_0037_fig04() -> str:
    """FIG. 4 (fol. 0037, p. 21) — Problem XXXIII(b): Fourth proportional via power of a point."""
    g = ArchivalPlateSVG("0037", "g1", "FIG. 4 — Problem XXXIII(b): Fourth proportional X = NP / M", 600, 420)

    # Left panel: R external to AB (RA = N, RB = P, RC = M, RD = X = NP/M)
    R1: Pt = (sp.Integer(198), sp.Integer(66))
    A1: Pt = (sp.Integer(206), sp.Integer(132))
    B1: Pt = (sp.Integer(224), sp.Integer(322))
    # Circle center O1 passing through A1, B1 (choose O1 to the right of midpoint)
    # Wait: in 1893 scan, C and D are to the LEFT of RAB, so circle passes through A1, B1 curving left!
    # Center O1 at (185, 226) -> check distances to A1, B1
    mid1 = ((A1[0] + B1[0]) / 2, (A1[1] + B1[1]) / 2)
    # Perpendicular direction to A1B1
    dx1, dy1 = B1[0] - A1[0], B1[1] - A1[1]
    O1: Pt = (sp.simplify(mid1[0] - dy1 * sp.Rational(1, 7)), sp.simplify(mid1[1] + dx1 * sp.Rational(1, 7)))
    rad1 = dist(O1, A1)
    # Secant direction from R1 down-left at ~128 deg (in SVG y-down: dx < 0, dy > 0)
    ang_sec = math.radians(126.0)
    ux, uy = math.cos(ang_sec), math.sin(ang_sec)
    # Solve |R1 + t u - O1|^2 = rad1^2
    rx, ry = fxy(R1)[0] - fxy(O1)[0], fxy(R1)[1] - fxy(O1)[1]
    b_q = 2.0 * (rx * ux + ry * uy)
    c_q = rx * rx + ry * ry - float(sp.N(rad1, 20)) ** 2
    disc = math.sqrt(b_q * b_q - 4.0 * c_q)
    t_c = (-b_q - disc) / 2.0
    t_d = (-b_q + disc) / 2.0
    C1: Pt = (sp.Float(fxy(R1)[0] + t_c * ux), sp.Float(fxy(R1)[1] + t_c * uy))
    D1: Pt = (sp.Float(fxy(R1)[0] + t_d * ux), sp.Float(fxy(R1)[1] + t_d * uy))

    r1_top, b1_bot = extend_seg(R1, B1, 24, 24)
    _, d1_end = extend_seg(R1, D1, 0, 48)
    g.add_segment(r1_top, b1_bot, "RAB", cls="geom-dashed")
    g.add_segment(R1, d1_end, "RCD", cls="geom-accent-line")
    g.add_arc(O1, rad1, deg_of(O1, C1) - 18, deg_of(O1, A1) + 18, ref="cAB_1")
    g.add_tick_arc(O1, B1, span_deg=24.0)
    g.add_tick_arc(O1, D1, span_deg=34.0)
    g.add_tick_arc(R1, C1, span_deg=38.0, ref="R(M)_1")

    g.add_point(R1, "R", "R", dx=14, dy=-4)
    g.add_point(A1, "A", "A", dx=14, dy=-6)
    g.add_point(B1, "B", "B", dx=13, dy=6)
    g.add_point(C1, "C", "C", dx=-6, dy=-16, cls="geom-point-accent")
    g.add_point(D1, "D", "D", dx=-15, dy=-4, cls="geom-point-assert", radius=3.5)

    # Right panel: R internal between B (top) and A (bottom)
    B2: Pt = (sp.Integer(436), sp.Integer(66))
    R2: Pt = (sp.Integer(434), sp.Integer(126))
    A2: Pt = (sp.Integer(429), sp.Integer(322))
    O2: Pt = (sp.Integer(432), sp.Integer(194))
    rad2 = dist(O2, B2)
    # Secant through R2 tilted -19 deg (going up-right to C2, down-left to D2)
    ang2 = math.radians(-19.0)
    ux2, uy2 = math.cos(ang2), math.sin(ang2)
    rx2, ry2 = fxy(R2)[0] - fxy(O2)[0], fxy(R2)[1] - fxy(O2)[1]
    b2_q = 2.0 * (rx2 * ux2 + ry2 * uy2)
    c2_q = rx2 * rx2 + ry2 * ry2 - float(sp.N(rad2, 20)) ** 2
    disc2 = math.sqrt(b2_q * b2_q - 4.0 * c2_q)
    tc2 = (-b2_q + disc2) / 2.0
    td2 = (-b2_q - disc2) / 2.0
    C2: Pt = (sp.Float(fxy(R2)[0] + tc2 * ux2), sp.Float(fxy(R2)[1] + tc2 * uy2))
    D2: Pt = (sp.Float(fxy(R2)[0] + td2 * ux2), sp.Float(fxy(R2)[1] + td2 * uy2))

    b2_top, a2_bot = extend_seg(B2, A2, 24, 24)
    d2_ext, c2_ext = extend_seg(D2, C2, 34, 30)
    g.add_segment(b2_top, a2_bot, "BRA", cls="geom-dashed")
    g.add_segment(d2_ext, c2_ext, "DRC", cls="geom-accent-line")
    g.add_arc(O2, rad2, deg_of(O2, B2) - 18, deg_of(O2, C2) + 22, ref="cAB_2")
    g.add_tick_arc(O2, A2, span_deg=32.0)
    g.add_tick_arc(O2, D2, span_deg=36.0)
    g.add_tick_arc(R2, C2, span_deg=34.0, ref="R(M)_2")

    g.add_point(B2, "B_int", "B", dx=14, dy=-8)
    g.add_point(R2, "R_int", "R", dx=13, dy=12)
    g.add_point(A2, "A_int", "A", dx=-14, dy=10)
    g.add_point(C2, "C_int", "C", dx=10, dy=-15, cls="geom-point-accent")
    g.add_point(D2, "D_int", "D", dx=-14, dy=-10, cls="geom-point-assert", radius=3.5)

    g.add_caption("FIG. 4 — Problem XXXIII(b) : Fourth Proportional X = NP/M  (2R₁ + 2R₂ + 11C₁ + C₂ + 6C₃, S = 22)")
    return g.render()


def build_0038_fig05() -> str:
    """FIG. 5 (fol. 0038, p. 22) — Problem XXXIII(c): Fourth proportional via inscribed chords."""
    g = ArchivalPlateSVG("0038", "g1", "FIG. 5 — Problem XXXIII(c): Fourth proportional via circle chords", 500, 420)

    O: Pt = (sp.Integer(250), sp.Integer(220))
    rad = sp.Integer(170)

    def on_c(deg: float) -> Pt:
        a = math.radians(deg)
        return (sp.Float(250.0 + 170.0 * math.cos(a)), sp.Float(220.0 + 170.0 * math.sin(a)))

    # R at top, A mid-left, B mid-right (same y -> horizontal AB), C lower-right, E lower-left (arc AE = arc BC)
    R = on_c(-88.0)
    A = on_c(195.0)
    B = on_c(-15.0)
    C = on_c(28.0)   # arc BC = 43 deg
    E = on_c(152.0)  # arc AE = 195 - 152 = 43 deg -> exact AE = BC!
    H = line_intersect(R, E, A, B)

    g.add_segment(A, B, "AB", cls="geom-dashed")
    g.add_segment(R, E, "RE", cls="geom-accent-line")
    g.add_segment(R, H, "RH", cls="geom-assert-line")

    # Main circle arcs matching 1893 engraving
    g.add_arc(O, rad, -108, -70, ref="cO_R")
    g.add_arc(O, rad, 138, 212, ref="cO_AE")
    g.add_arc(O, rad, -30, 44, ref="cO_BC")

    # Compass strike arcs from R and A
    g.add_tick_arc(R, A, span_deg=24.0, ref="R(N)")
    g.add_tick_arc(R, B, span_deg=22.0, ref="R(P)")
    g.add_tick_arc(R, C, span_deg=22.0, ref="R(M)")
    g.add_tick_arc(A, E, span_deg=32.0, ref="A(BC)")

    g.add_point(R, "R", "R", dx=2, dy=-15)
    g.add_point(A, "A", "A", dx=-16, dy=0)
    g.add_point(B, "B", "B", dx=16, dy=0)
    g.add_point(C, "C", "C", dx=15, dy=8)
    g.add_point(E, "E", "E", dx=-14, dy=12)
    g.add_point(H, "H", "H", dx=-11, dy=-13, cls="geom-point-assert", radius=3.6)

    g.add_caption("FIG. 5 — Prob. XXXIII(c) : Inscribed-Chord Fourth Proportional RH = NP/M (S = 23)")
    return g.render()


def build_0042_fig06() -> str:
    """FIG. 6 (fol. 0042, p. 26) — Problem XXXV(d): Mean proportional AB = sqrt(MN)."""
    g = ArchivalPlateSVG("0042", "g1", "FIG. 6 — Problem XXXV(d): Mean proportional AB = sqrt(MN)", 520, 480)

    O: Pt = (sp.Integer(248), sp.Integer(204))
    rad = sp.Integer(198)
    # Horizontal chord CB below O at y = 296
    dy_cb = sp.Integer(92)
    dx_cb = sp.sqrt(rad**2 - dy_cb**2)
    C: Pt = (sp.simplify(O[0] - dx_cb), O[1] + dy_cb)
    B: Pt = (sp.simplify(O[0] + dx_cb), O[1] + dy_cb)

    # K on BC with BK = N (about 0.42 * BC)
    M_len = dist(B, C)
    N_len = M_len * sp.Rational(42, 100)
    K = ray_point(B, C, N_len)

    # Reflection K' of K across line OB -> line KK' is strictly perpendicular to OB!
    # Intersections of B(BK) and O(OK) are K and K'
    r_ok = dist(O, K)
    p_a, p_b = circle_circle_intersect(O, r_ok, B, N_len)
    Kp = p_a if float(sp.N(dist(p_a, K), 10)) > 1.0 else p_b

    # Intersect line KK' with circle O(OB) -> point A (upper-right)
    kx, ky = fxy(K)
    kpx, kpy = fxy(Kp)
    d_kk = math.hypot(kpx - kx, kpy - ky)
    ux, uy = (kpx - kx) / d_kk, (kpy - ky) / d_kk
    ox, oy = fxy(O)
    rx, ry = kx - ox, ky - oy
    bq = 2.0 * (rx * ux + ry * uy)
    cq = rx * rx + ry * ry - float(rad) ** 2
    t_pos = (-bq + math.sqrt(bq * bq - 4.0 * cq)) / 2.0
    A: Pt = (sp.Float(kx + t_pos * ux), sp.Float(ky + t_pos * uy))

    # Draw circle arc O(OB) from upper-right past B, bottom, to C
    g.add_arc(O, rad, deg_of(O, A) - 18, deg_of(O, C) + 22, ref="O(OB)")
    g.add_segment(C, B, "CB", cls="geom-dashed")
    k_ext, a_ext = extend_seg(K, A, 16, 20)
    g.add_segment(k_ext, a_ext, "KA", cls="geom-accent-line")
    g.add_segment(A, B, "AB", cls="geom-assert-line")

    # Construction arcs B(N) (short upper-left arc from K to K') and O(OK) (crossing at K')
    g.add_arc(B, N_len, deg_of(B, K) - 18, deg_of(B, Kp) + 18, ref="B(N)")
    g.add_tick_arc(O, Kp, span_deg=32.0, ref="O(OK)")

    g.add_point(O, "O", "O", dx=-12, dy=-12)
    g.add_point(C, "C", "C", dx=-15, dy=2)
    g.add_point(B, "B", "B", dx=15, dy=4)
    g.add_point(K, "K", "K", dx=-10, dy=15, cls="geom-point-accent")
    g.add_point(A, "A", "A", dx=15, dy=2, cls="geom-point-assert", radius=3.6)

    g.add_caption("FIG. 6 — Prob. XXXV(d) : Mean Proportional AB = √(MN) (S = 18)")
    return g.render()


def build_0043_fig07() -> str:
    """FIG. 7 (fol. 0043, p. 27) — Problem XXXV(e): Léon Colette's 1892 mean proportional."""
    g = ArchivalPlateSVG("0043", "g1", "FIG. 7 — Problem XXXV(e): Léon Colette's mean proportional", 540, 460)

    O: Pt = (sp.Integer(270), sp.Integer(232))
    rad = sp.Integer(168)
    A: Pt = (O[0], O[1] - rad)  # top of circle

    M_len = sp.Integer(296)  # chord AB = AC = M
    N_len = sp.Integer(204)  # chord AF = AG = N (< M)

    # Intersections of A(M) with O(OA) -> B (left), C (right)
    b1, b2 = circle_circle_intersect(O, rad, A, M_len)
    B, C = (b1, b2) if fxy(b1)[0] < fxy(b2)[0] else (b2, b1)

    # Intersections of A(N) with O(OA) -> F (left), G (right)
    f1, f2 = circle_circle_intersect(O, rad, A, N_len)
    F, G = (f1, f2) if fxy(f1)[0] < fxy(f2)[0] else (f2, f1)

    # D on AB at distance N from A; E on AC at distance N from A
    D = ray_point(A, B, N_len)
    E = ray_point(A, C, N_len)

    # Horizontal line DE cuts O(OA) at M (left) and N (right)
    dy_de = fxy(D)[1] - fxy(O)[1]
    dx_mn = math.sqrt(float(rad) ** 2 - dy_de * dy_de)
    M: Pt = (sp.Float(fxy(O)[0] - dx_mn), D[1])
    N: Pt = (sp.Float(fxy(O)[0] + dx_mn), D[1])

    # Circle O(OA) arcs matching 1893 engraving
    g.add_tick_arc(O, A, span_deg=26.0, ref="O(OA)")
    g.add_arc(O, rad, deg_of(O, B) - 14, deg_of(O, F) + 18)
    g.add_arc(O, rad, deg_of(O, G) - 18, deg_of(O, C) + 14)

    # Arcs A(M) at B, C and A(N) from F through D, and E through G
    g.add_tick_arc(A, B, span_deg=26.0, ref="A(M)")
    g.add_tick_arc(A, C, span_deg=26.0)
    g.add_arc(A, N_len, deg_of(A, D) - 10, deg_of(A, F) + 12, ref="A(N)")
    g.add_arc(A, N_len, deg_of(A, G) - 12, deg_of(A, E) + 10)

    # Lines AB, AC, and horizontal line M-D-E-N
    _, b_ext = extend_seg(A, B, 0, 22)
    _, c_ext = extend_seg(A, C, 0, 22)
    m_ext, n_ext = extend_seg(M, N, 20, 20)
    g.add_segment(A, b_ext, "AB", cls="geom-dashed")
    g.add_segment(A, c_ext, "AC", cls="geom-dashed")
    g.add_segment(m_ext, n_ext, "DE", cls="geom-accent-line")
    g.add_segment(A, M, "AM", cls="geom-assert-line")

    g.add_point(A, "A", "A", dx=0, dy=-15)
    g.add_point(O, "O", "O", dx=-6, dy=-14)
    g.add_point(F, "F", "F", dx=15, dy=-4)
    g.add_point(G, "G", "G", dx=-15, dy=-4)
    g.add_point(D, "D", "D", dx=-14, dy=12, cls="geom-point-accent")
    g.add_point(E, "E", "E", dx=14, dy=12, cls="geom-point-accent")
    g.add_point(M, "M", "M", dx=-16, dy=-10, cls="geom-point-assert", radius=3.5)
    g.add_point(N, "N", "N", dx=16, dy=-10, cls="geom-point-assert", radius=3.5)
    g.add_point(B, "B", "B", dx=-16, dy=6)
    g.add_point(C, "C", "C", dx=16, dy=6)

    g.add_caption("FIG. 7 — Problem XXXV(e) : Léon Colette's Mean Proportional AM = √(MN)  (S = 18)")
    return g.render()


def build_0044_fig08() -> str:
    """FIG. 8 (fol. 0044, p. 28) — Problem XXXVI(c): Lemoine's 1-line Golden Section of AB."""
    g = ArchivalPlateSVG("0044", "g1", "FIG. 8 — Problem XXXVI(c): Lemoine's 1-line Golden Section of AB", 560, 520)

    # Exact algebraic construction over Q(sqrt(3), sqrt(5))!
    scale = sp.Integer(190)
    ax, ay = sp.Integer(188), sp.Integer(254)
    A: Pt = (ax, ay)
    B: Pt = (ax + scale, ay)
    s3 = sp.sqrt(3)
    s5 = sp.sqrt(5)

    # C' (above) and C (below) from A(AB) ∩ B(AB)
    Cp: Pt = (ax + scale / 2, ay - scale * s3 / 2)
    C: Pt = (ax + scale / 2, ay + scale * s3 / 2)

    # D = C'(AB) ∩ B(AB) -> exact tangent direction AD to C(AB) at A!
    D: Pt = (ax + scale * sp.Rational(3, 2), ay - scale * s3 / 2)
    # E = AD ∩ A(AB) -> exact point at 30 deg above AB
    E: Pt = (ax + scale * s3 / 2, ay - scale / 2)
    # Circle C(CE) of radius scale*sqrt(2) cuts ray BA at M -> AM = scale / phi!
    r_ce = scale * sp.sqrt(2)
    am_len = scale * (s5 - 1) / 2
    M: Pt = (sp.simplify(ax - am_len), ay)
    # Circle A(AM) cuts segment AB at golden point P!
    P: Pt = (sp.simplify(ax + am_len), ay)

    # Base line M — A — P — B and the SINGLE traced straight line AD!
    g.add_segment(M, B, "MB", cls="geom-line")
    g.add_segment(A, B, "AB", cls="geom-bold")
    g.add_segment(A, P, "AP", cls="geom-assert-line")
    g.add_segment(A, D, "AD", cls="geom-accent-line")

    # Six exact construction circles/arcs matching 1893 scan
    # 1. A(AB): passes through B, E, C' and below at C
    g.add_arc(A, scale, -108, 18, ref="A(AB)")
    g.add_tick_arc(A, C, span_deg=32.0)
    # 2. B(AB): passes through A, C', D and below at C
    g.add_arc(B, scale, 168, 322, ref="B(AB)")
    g.add_tick_arc(B, C, span_deg=32.0)
    # 3. C(AB): upper arc passing through A and B
    g.add_arc(C, scale, deg_of(C, A) - 24, deg_of(C, B) + 24, ref="C(AB)")
    # 4. C'(AB): arc through A, B, and D
    g.add_arc(Cp, scale, deg_of(Cp, D) - 18, deg_of(Cp, A) + 14, ref="C'(AB)")
    # 5. C(CE): arc sweeping from E over to M
    g.add_arc(C, r_ce, deg_of(C, M) - 10, deg_of(C, E) + 18, ref="C(CE)")
    # 6. A(AM): arc from M and cutting AB at P
    g.add_tick_arc(A, M, span_deg=32.0, ref="A(AM)")
    g.add_arc(A, am_len, -52, 14)

    g.add_point(M, "M", "M", dx=-15, dy=2, cls="geom-point-accent")
    g.add_point(A, "A", "A", dx=-13, dy=-12)
    g.add_point(P, "P", "P", dx=11, dy=-13, cls="geom-point-assert", radius=3.7)
    g.add_point(B, "B", "B", dx=15, dy=2)
    g.add_point(Cp, "C'", "C'", dx=2, dy=-15)
    g.add_point(C, "C", "C", dx=0, dy=16)
    g.add_point(D, "D", "D", dx=14, dy=-6, cls="geom-point-accent")
    g.add_point(E, "E", "E", dx=4, dy=-15, cls="geom-point-accent")

    g.add_caption("FIG. 8 — Problem XXXVI(c) : Golden Section AP = AB/φ  (2R₁ + R₂ + 9C₁ + 6C₃, S = 18)")
    return g.render()


def build_0050_fig09() -> str:
    """FIG. 9 (fol. 0050, p. 34) — Problem XLVII: Catalan's 1847 square vertices C, D on AB."""
    g = ArchivalPlateSVG("0050", "g1", "FIG. 9 — Problem XLVII: Catalan's 1847 construction of square vertices C, D", 540, 460)

    # Rotate unit square slightly clockwise (-8 deg) to match the exact 1893 engraving tilt
    theta = math.radians(8.0)  # y-down: +8 deg puts B slightly lower than A
    scale = 235.0
    ax, ay = 94.0, 344.0

    def local(u: float, v: float) -> Pt:
        # u along AB, v upward perpendicular to AB
        x = ax + scale * (u * math.cos(theta) + v * math.sin(theta))
        y = ay + scale * (u * math.sin(theta) - v * math.cos(theta))
        return (sp.Float(x), sp.Float(y))

    s3 = math.sqrt(3.0)
    A = local(0.0, 0.0)
    B = local(1.0, 0.0)
    K = local(0.5, s3 / 2.0)
    G = local(1.5, s3 / 2.0)
    I = local(s3 / 2.0, 0.5)
    C = local(1.0, 1.0)
    D = local(0.0, 1.0)
    r_ki = scale * math.sqrt(2.0 - s3)

    # Highlight the square ABCD subtly
    g.add_polygon([A, B, C, D], "ABCD")

    # 1. A(AB): big arc from B through I, K to D
    g.add_arc(A, scale, deg_of(A, D) - 10, deg_of(A, B) + 10, ref="A(AB)")
    # 2. B(AB): arc from A (tick), K, C to G
    g.add_tick_arc(B, A, span_deg=24.0, ref="B(AB)")
    g.add_arc(B, scale, deg_of(B, K) - 12, deg_of(B, G) + 14)
    # 3. K(AB): arc from A (tick), B to G
    g.add_tick_arc(K, A, span_deg=22.0, ref="K(AB)")
    g.add_arc(K, scale, deg_of(K, G) - 14, deg_of(K, B) + 14)
    # 4. Single straight line AG passing through I
    _, g_ext = extend_seg(A, G, 0, 22)
    g.add_segment(A, g_ext, "AG", cls="geom-accent-line")
    # 5. K(KI): arc passing through I, C, and cutting A(AB) at D
    g.add_arc(K, r_ki, deg_of(K, C) - 18, deg_of(K, I) + 18, ref="K(KI)", cls="geom-assert-line")
    g.add_tick_arc(K, D, span_deg=34.0, cls="geom-assert-line")

    # Subtle dotted square outline showing verified right-angle square ABCD
    g.add_segment(A, B, "AB", cls="geom-dashed")
    g.add_segment(B, C, "BC", cls="geom-dashed")
    g.add_segment(C, D, "CD", cls="geom-dashed")
    g.add_segment(D, A, "DA", cls="geom-dashed")

    g.add_point(A, "A", "A", dx=-14, dy=8)
    g.add_point(B, "B", "B", dx=12, dy=12)
    g.add_point(K, "K", "K", dx=2, dy=-15, cls="geom-point-accent")
    g.add_point(G, "G", "G", dx=15, dy=2, cls="geom-point-accent")
    g.add_point(I, "I", "I", dx=13, dy=8, cls="geom-point-accent")
    g.add_point(C, "C", "C", dx=12, dy=-13, cls="geom-point-assert", radius=3.7)
    g.add_point(D, "D", "D", dx=-12, dy=-12, cls="geom-point-assert", radius=3.7)

    g.add_caption("FIG. 9 — Problem XLVII : Catalan's Square Vertices C, D  (2R₁ + R₂ + 6C₁ + 4C₃, S = 13)")
    return g.render()


def build_0054_fig10() -> str:
    """FIG. 10 (fol. 0054, p. 38) — Principes: Simultaneous 1/10 and 1/15 division of BC."""
    g = ArchivalPlateSVG("0054", "g1", "FIG. 10 — Simultaneous 1/10 and 1/15 division via equilateral triangle", 640, 410)

    # Exact equilateral triangle AB'C' of side s = 260, extended to D with C'D = s
    s = sp.Integer(260)
    h = s * sp.sqrt(3) / 2
    bx, by = sp.Integer(62), sp.Integer(334)

    Bp: Pt = (bx, by)
    Cp: Pt = (bx + s, by)
    D: Pt = (bx + 2 * s, by)
    A: Pt = (bx + s / 2, by - h)

    E: Pt = ((A[0] + Bp[0]) / 2, (A[1] + Bp[1]) / 2)
    H: Pt = ((A[0] + Cp[0]) / 2, (A[1] + Cp[1]) / 2)

    F = line_intersect(E, D, A, Cp)
    G = line_intersect(H, D, A, Bp)
    I = line_intersect(E, H, G, F)
    M = line_intersect(G, F, Bp, D)
    K = line_intersect(D, I, A, Bp)
    L = line_intersect(D, I, A, Cp)

    g.add_polygon([A, Bp, Cp], "AB'C'")
    # Main equilateral triangle + base extension
    g.add_segment(Bp, D, "B'D", cls="geom-bold")
    g.add_segment(A, Bp, "AB'", cls="geom-bold")
    g.add_segment(A, Cp, "AC'", cls="geom-bold")
    # Midline EH and transversals ED, HD, GFM, DIK
    g.add_segment(E, H, "EH", cls="geom-line")
    g.add_segment(E, D, "ED", cls="geom-line")
    g.add_segment(G, D, "GD", cls="geom-line")
    g.add_segment(G, M, "GM", cls="geom-accent-line")
    g.add_segment(K, D, "KD", cls="geom-assert-line")
    # Emphasize target segments KG = 1/15 BC and KE = 1/10 BC
    g.add_segment(G, K, "KG", cls="geom-assert-line")
    g.add_segment(K, E, "KE", cls="geom-accent-line")

    g.add_point(A, "A", "A", dx=0, dy=-15)
    g.add_point(Bp, "B'", "B'", dx=-15, dy=10)
    g.add_point(Cp, "C'", "C'", dx=2, dy=15)
    g.add_point(M, "M", "M", dx=0, dy=15, cls="geom-point-accent")
    g.add_point(D, "D", "D", dx=4, dy=15)
    g.add_point(G, "G", "G", dx=-16, dy=-4, cls="geom-point-assert")
    g.add_point(K, "K", "K", dx=-16, dy=-2, cls="geom-point-assert", radius=3.5)
    g.add_point(E, "E", "E", dx=-16, dy=2, cls="geom-point-accent")
    g.add_point(H, "H", "H", dx=12, dy=-10)
    g.add_point(I, "I", "I", dx=-6, dy=14, cls="geom-point-accent")
    g.add_point(L, "L", "L", dx=15, dy=1, cls="geom-point-assert")
    g.add_point(F, "F", "F", dx=-10, dy=14)

    g.add_caption("FIG. 10 — Simultaneous 1/15 & 1/10 Division : KG = (1/15)BC, KE = (1/10)BC  (S = 35)")
    return g.render()


def build_0056_fig11() -> str:
    """FIG. 11 (fol. 0056, p. 40) — Problem XLIX: Point M from normal coordinates l, m, n."""
    g = ArchivalPlateSVG("0056", "g1", "FIG. 11 — Problem XLIX: Construction of point M from normal coordinates l, m, n", 600, 510)

    # Reference triangle ABC matching 1893 orientation (C bottom-left, B bottom-right, A upper-center)
    C: Pt = (sp.Integer(54), sp.Integer(414))
    B: Pt = (sp.Integer(376), sp.Integer(414))
    A: Pt = (sp.Integer(288), sp.Integer(156))

    # Auxiliary interior point O where three perpendiculars A'O, B'O, C'O concur
    O: Pt = (sp.Integer(214), sp.Integer(326))

    def foot(p: Pt, u: Pt, v: Pt) -> Pt:
        dx, dy = v[0] - u[0], v[1] - u[1]
        t = ((p[0] - u[0]) * dx + (p[1] - u[1]) * dy) / (dx**2 + dy**2)
        return (sp.simplify(u[0] + t * dx), sp.simplify(u[1] + t * dy))

    Ap = foot(O, B, C)
    Bp = foot(O, C, A)
    Cp = foot(O, A, B)

    # Signed normal offsets: alpha1 inward from A' (+64 up), beta1 inward from B' (+26), gamma1 OUTWARD from C' (-36)
    alpha1 = ray_point(Ap, O, sp.Integer(64))
    beta1 = ray_point(Bp, O, sp.Integer(26))
    gamma1 = ray_point(Cp, add_vec(Cp, Cp[0] - O[0], Cp[1] - O[1]), sp.Integer(38))

    # Parallels to BC (through alpha1), CA (through beta1), AB (through gamma1) form homothetic triangle A2B2C2
    par_bc_2 = add_vec(alpha1, B[0] - C[0], B[1] - C[1])
    par_ca_2 = add_vec(beta1, A[0] - C[0], A[1] - C[1])
    par_ab_2 = add_vec(gamma1, B[0] - A[0], B[1] - A[1])

    C2 = line_intersect(alpha1, par_bc_2, beta1, par_ca_2)
    B2 = line_intersect(alpha1, par_bc_2, gamma1, par_ab_2)
    A2 = line_intersect(beta1, par_ca_2, gamma1, par_ab_2)

    # Center of homothety M = AA2 ∩ BB2 (also lies on CC2!)
    M = line_intersect(A, A2, B, B2)

    # Extra gauge marks matching 1893 engraving: alpha on CB, A1 on C2B2
    alpha_pt: Pt = (sp.Integer(274), C[1])
    A1_pt: Pt = (sp.Integer(274), alpha1[1])

    g.add_polygon([A, B, C], "ABC")
    g.add_segment(A, B, "AB", cls="geom-bold")
    g.add_segment(B, C, "BC", cls="geom-bold")
    g.add_segment(C, A, "CA", cls="geom-bold")

    # Three perpendiculars at A', B', C'
    ap_s, ap_e = extend_seg(Ap, O, 24, 34)
    bp_s, bp_e = extend_seg(Bp, O, 18, 52)
    cp_s, cp_e = extend_seg(O, gamma1, 46, 26)
    g.add_segment(ap_s, ap_e, "A'O", cls="geom-dashed")
    g.add_segment(bp_s, bp_e, "B'O", cls="geom-dashed")
    g.add_segment(cp_s, cp_e, "C'γ₁", cls="geom-dashed")

    # Homothetic triangle A2B2C2 sides (dashed accent)
    c2_l, b2_r = extend_seg(C2, B2, 22, 24)
    c2_d, a2_u = extend_seg(C2, A2, 22, 28)
    a2_t, b2_b = extend_seg(A2, B2, 20, 22)
    g.add_segment(c2_l, b2_r, "C₂B₂", cls="geom-accent-line")
    g.add_segment(c2_d, a2_u, "C₂A₂", cls="geom-accent-line")
    g.add_segment(a2_t, b2_b, "A₂B₂", cls="geom-accent-line")

    # Homothety rays AM and BM converging at M
    a_m1, a_m2 = extend_seg(A, M, 18, 16)
    b_m1, b_m2 = extend_seg(B, M, 20, 18)
    g.add_segment(a_m1, a_m2, "AM", cls="geom-assert-line")
    g.add_segment(b_m1, b_m2, "BM", cls="geom-assert-line")

    g.add_right_angle(Ap, O, B, size=8.0)

    g.add_point(C, "C", "C", dx=-14, dy=6)
    g.add_point(B, "B", "B", dx=12, dy=11)
    g.add_point(A, "A", "A", dx=-12, dy=-12)
    g.add_point(Ap, "A'", "A'", dx=-14, dy=12)
    g.add_point(Bp, "B'", "B'", dx=14, dy=-10)
    g.add_point(Cp, "C'", "C'", dx=8, dy=-14)
    g.add_point(O, "O", "O", dx=10, dy=-12)
    g.add_point(alpha_pt, "α", "α", dx=12, dy=12)
    g.add_point(A1_pt, "A₁", "A₁", dx=13, dy=-10)
    g.add_point(alpha1, "α₁", "α₁", dx=-14, dy=13, cls="geom-point-accent")
    g.add_point(beta1, "β₁", "β₁", dx=-6, dy=15, cls="geom-point-accent")
    g.add_point(gamma1, "γ₁", "γ₁", dx=6, dy=15, cls="geom-point-accent")
    g.add_point(C2, "C₂", "C₂", dx=12, dy=13, cls="geom-point-accent")
    g.add_point(B2, "B₂", "B₂", dx=17, dy=-10, cls="geom-point-accent")
    g.add_point(A2, "A₂", "A₂", dx=-14, dy=-12, cls="geom-point-accent")
    g.add_point(M, "M", "M", dx=15, dy=8, cls="geom-point-assert", radius=3.8)

    g.add_caption("FIG. 11 — Problem XLIX : Point M via Normal Coordinates l, m, n & Homothetic △A₂B₂C₂")
    return g.render()


SVG_BUILDERS = {
    "0031": build_0031_fig01,
    "0032": build_0032_fig02,
    "0034": build_0034_fig03,
    "0037": build_0037_fig04,
    "0038": build_0038_fig05,
    "0042": build_0042_fig06,
    "0043": build_0043_fig07,
    "0044": build_0044_fig08,
    "0050": build_0050_fig09,
    "0054": build_0054_fig10,
    "0056": build_0056_fig11,
}


def normalize_archival_crop(img: Image.Image) -> Image.Image:
    """Contrast-normalize a 300-DPI scan crop while preserving crisp 1893 ink lines."""
    gray = img.convert("L")
    arr = np.asarray(gray, dtype=np.float32)
    lo = float(np.percentile(arr, 0.5))
    hi = float(np.percentile(arr, 92.0))
    if hi <= lo + 10.0:
        lo, hi = 0.0, 255.0
    norm = np.clip((arr - lo) * (255.0 / (hi - lo)), 0.0, 255.0)
    norm = np.where(norm > 238.0, 255.0, norm)
    cleaned = Image.fromarray(norm.astype(np.uint8), mode="L")
    return ImageOps.expand(cleaned, border=24, fill=255)


def main() -> int:
    """Extract all 11 archival bitmaps and build all 11 paired `.euclid-graphic` SVGs."""
    for folio, rel_leaf, bbox in PLATE_SPECS:
        leaf_dir = CODEX_DIR / rel_leaf
        leaf_dir.mkdir(parents=True, exist_ok=True)

        src_scan = FOLIOS_DIR / f"{folio}.png"
        with Image.open(src_scan) as im:
            cleaned = normalize_archival_crop(im.crop(bbox))
        png_out = leaf_dir / f"{folio}.g1.png"
        cleaned.save(png_out, format="PNG", optimize=True, compress_level=9)

        svg_out = leaf_dir / f"{folio}.g1.svg"
        svg_text = SVG_BUILDERS[folio]()
        svg_out.write_text(svg_text, encoding="utf-8")
        print(f"Paired {rel_leaf}/{folio}.g1.png ({cleaned.size}) + {folio}.g1.svg ({len(svg_text)} B)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
