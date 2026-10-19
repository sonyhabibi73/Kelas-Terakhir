"""Generate the two raster assets used by the prologue.

Outputs:
    game/images/bg/rumah.png          1920x1080, morning entryway
    game/images/char/ibu_senyum.png   560x980, transparent mother sprite

The art is intentionally painted in flat, warm shapes so it sits comfortably
next to the rest of the visual-novel assets. Run with:

    python3 tools/generate_prolog_assets.py
"""

from __future__ import annotations

import math
import os
import random

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BG_PATH = os.path.join(ROOT, "game", "images", "bg", "rumah.png")
CHAR_PATH = os.path.join(ROOT, "game", "images", "char", "ibu_senyum.png")


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def qbez(p0, p1, p2, steps=28):
    """Quadratic Bezier points, inclusive."""
    out = []
    for i in range(steps + 1):
        t = i / steps
        u = 1.0 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


def cbez(p0, p1, p2, p3, steps=32):
    """Cubic Bezier points, inclusive."""
    out = []
    for i in range(steps + 1):
        t = i / steps
        u = 1.0 - t
        x = (u**3 * p0[0] + 3 * u * u * t * p1[0]
             + 3 * u * t * t * p2[0] + t**3 * p3[0])
        y = (u**3 * p0[1] + 3 * u * u * t * p1[1]
             + 3 * u * t * t * p2[1] + t**3 * p3[1])
        out.append((x, y))
    return out


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def shade(color, factor):
    return tuple(max(0, min(255, int(round(c * factor)))) for c in color)


# ---------------------------------------------------------------------------
# Background: rumah Rei, pagi
# ---------------------------------------------------------------------------


def make_background():
    W, H = 1920, 1080
    S = 2
    Ws, Hs = W * S, H * S

    # -- wall gradient + morning glow -------------------------------------
    yy = np.linspace(0.0, 1.0, Hs)[:, None, None]
    top = np.array([247, 236, 219], dtype=np.float64)
    bottom = np.array([226, 204, 178], dtype=np.float64)
    arr = top * (1.0 - yy) + bottom * yy

    xx = np.arange(Ws)[None, :, None]
    gy = np.arange(Hs)[:, None, None]
    dist = np.sqrt(((xx - 1570 * S) / (760 * S)) ** 2
                   + ((gy - 390 * S) / (520 * S)) ** 2)
    glow = np.clip(1.0 - dist, 0.0, 1.0) ** 2
    arr = arr + glow * np.array([34, 20, 4], dtype=np.float64)

    # a faint cool wash on the left, so the window side feels warmer
    dist2 = np.sqrt(((xx - 300 * S) / (900 * S)) ** 2
                    + ((gy - 500 * S) / (700 * S)) ** 2)
    cool = np.clip(1.0 - dist2, 0.0, 1.0) ** 2
    arr = arr + cool * np.array([-4, -2, 6], dtype=np.float64)

    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")
    d = ImageDraw.Draw(img)

    def P(x, y):
        return (int(round(x * S)), int(round(y * S)))

    def poly(points, fill, outline=None, width=0):
        pts = [P(x, y) for x, y in points]
        d.polygon(pts, fill=fill)
        if outline and width:
            d.line(pts + [pts[0]], fill=outline, width=max(1, int(width * S)),
                   joint="curve")

    def rect(x0, y0, x1, y1, fill, outline=None, width=0):
        d.rectangle([P(x0, y0), P(x1, y1)], fill=fill, outline=outline,
                    width=max(0, int(width * S)))

    def ell(x0, y0, x1, y1, fill, outline=None, width=0):
        d.ellipse([P(x0, y0), P(x1, y1)], fill=fill, outline=outline,
                  width=max(0, int(width * S)))

    def line(points, fill, width=1):
        d.line([P(x, y) for x, y in points], fill=fill,
               width=max(1, int(width * S)), joint="curve")

    # -- floor -------------------------------------------------------------
    rect(0, 700, W, H, (183, 130, 88))
    vpx, vpy = 1050, 615

    # Perspective planks radiate from the corridor vanishing point.
    plank_colors = [(190, 137, 94), (178, 125, 84), (198, 145, 100),
                    (172, 119, 80), (186, 132, 89)]
    for i, x in enumerate(range(-600, W + 700, 118)):
        col = plank_colors[i % len(plank_colors)]
        poly([(vpx, vpy), (x, H), (x + 118, H)], col)
        line([(vpx, vpy), (x, H)], (142, 95, 61), 1)

    # Transverse floor joints.
    joints = Image.new("RGBA", (Ws, Hs), (0, 0, 0, 0))
    jd = ImageDraw.Draw(joints)
    for t in (0.16, 0.32, 0.50, 0.70, 0.90):
        y = 700 + (H - 700) * (t ** 1.55)
        jd.line([P(0, y), P(W, y)], fill=(118, 77, 49, 75),
                width=max(1, int(1.2 * S)))
    img = Image.alpha_composite(img.convert("RGBA"), joints).convert("RGB")
    d = ImageDraw.Draw(img)

    # soft window light on the floor
    floor_light = Image.new("RGBA", (Ws, Hs), (0, 0, 0, 0))
    fd = ImageDraw.Draw(floor_light)
    fd.polygon([P(1210, 690), P(1800, 690), P(1520, 1080), P(900, 1080)],
               fill=(255, 226, 166, 42))
    floor_light = floor_light.filter(ImageFilter.GaussianBlur(18 * S))
    img = Image.alpha_composite(img.convert("RGBA"), floor_light).convert("RGB")
    d = ImageDraw.Draw(img)

    # -- skirting board / lower wall --------------------------------------
    rect(0, 640, W, 705, (221, 204, 181))
    rect(0, 640, W, 648, (205, 184, 158))
    rect(0, 700, W, 710, (188, 164, 137))
    for x in range(90, W, 190):
        line([(x, 650), (x, 699)], (211, 192, 166), 1)

    # -- front door (left) -------------------------------------------------
    rect(38, 78, 486, 728, (111, 76, 54))
    rect(55, 96, 468, 712, (137, 94, 65))
    rect(82, 122, 440, 692, (151, 105, 73))

    # inset panels
    rect(108, 148, 414, 354, (168, 119, 84), (110, 72, 50), 2)
    rect(122, 162, 400, 340, (206, 221, 211), (110, 72, 50), 2)
    # frosted glass reflection
    poly([(132, 330), (250, 172), (285, 172), (167, 330)],
         (232, 242, 231))
    poly([(302, 330), (388, 195), (400, 214), (326, 330)],
         (222, 235, 224))
    rect(108, 386, 414, 662, (158, 110, 78), (110, 72, 50), 2)
    rect(128, 406, 394, 642, (145, 98, 69), (109, 71, 49), 2)
    line([(150, 430), (372, 430)], (178, 125, 90), 3)

    # handle and lock
    ell(396, 500, 424, 528, (211, 170, 93), (104, 68, 43), 2)
    ell(405, 509, 415, 519, (241, 209, 141))
    ell(397, 538, 407, 548, (109, 71, 45))

    # door step / genkan
    poly([(24, 724), (500, 724), (530, 790), (0, 790)], (164, 122, 88))
    poly([(44, 724), (480, 724), (500, 755), (24, 755)], (198, 160, 120))
    line([(44, 756), (500, 756)], (131, 91, 64), 2)

    # -- shoe cabinet and Rei's bag ---------------------------------------
    rect(520, 612, 730, 842, (142, 96, 66), (99, 64, 43), 3)
    rect(534, 626, 716, 700, (160, 111, 78), (105, 69, 46), 2)
    rect(534, 712, 716, 786, (154, 106, 74), (105, 69, 46), 2)
    rect(534, 798, 716, 828, (135, 90, 62), (105, 69, 46), 2)
    for cx in (590, 660):
        ell(cx - 5, 654, cx + 5, 664, (207, 174, 115))
        ell(cx - 5, 740, cx + 5, 750, (207, 174, 115))
        ell(cx - 5, 810, cx + 5, 820, (207, 174, 115))
    # a small tray with keys
    poly([(610, 620), (700, 620), (694, 634), (616, 634)], (112, 79, 55))
    line([(648, 617), (648, 607)], (205, 176, 116), 3)
    ell(641, 600, 655, 612, (190, 158, 101))

    # bag on the floor beside the cabinet
    poly([(744, 790), (812, 790), (824, 900), (730, 900)],
         (120, 79, 55), (76, 48, 34), 3)
    poly([(752, 790), (804, 790), (812, 844), (744, 844)],
         (139, 94, 65), (76, 48, 34), 2)
    line([(750, 800), (770, 890), (786, 890), (768, 800)], (88, 56, 39), 3)
    line([(806, 800), (788, 890), (776, 890), (792, 800)], (88, 56, 39), 3)

    # -- central console + wall details -----------------------------------
    rect(790, 670, 1088, 702, (141, 96, 67), (94, 60, 41), 3)
    rect(806, 702, 830, 848, (120, 80, 55), (90, 58, 39), 2)
    rect(1048, 702, 1072, 848, (120, 80, 55), (90, 58, 39), 2)
    rect(824, 770, 1054, 790, (132, 89, 61), (90, 58, 39), 2)

    # vase with spring flowers
    poly([(900, 610), (940, 610), (950, 670), (890, 670)],
         (116, 139, 120), (72, 91, 77), 3)
    line([(918, 610), (900, 548)], (93, 119, 88), 3)
    line([(922, 610), (940, 538)], (93, 119, 88), 3)
    line([(916, 610), (916, 540)], (93, 119, 88), 3)
    for fx, fy, fr in ((900, 548, 14), (940, 538, 15), (916, 540, 12),
                       (884, 564, 10), (956, 560, 10)):
        ell(fx - fr, fy - fr, fx + fr, fy + fr, (214, 137, 108),
            (154, 79, 64), 2)
        ell(fx - 3, fy - 3, fx + 3, fy + 3, (239, 188, 116))
    ell(974, 650, 1004, 668, (219, 198, 170), (142, 108, 80), 2)

    # framed family photo
    rect(856, 342, 1024, 522, (126, 84, 58), (87, 55, 38), 3)
    rect(872, 358, 1008, 506, (217, 202, 177))
    poly([(890, 484), (918, 430), (946, 484)], (157, 177, 153))
    poly([(922, 484), (962, 408), (1000, 484)], (181, 198, 174))
    ell(916, 400, 938, 422, (218, 177, 144))
    ell(974, 414, 992, 432, (218, 177, 144))
    rect(936, 514, 944, 530, (110, 76, 53))

    # wall clock
    ell(1002, 156, 1130, 284, (242, 232, 214), (121, 86, 62), 3)
    ell(1010, 164, 1122, 276, (250, 242, 228), (184, 158, 127), 2)
    for ang in range(0, 360, 30):
        rad = math.radians(ang)
        x0 = 1066 + math.cos(rad) * 43
        y0 = 220 + math.sin(rad) * 43
        x1 = 1066 + math.cos(rad) * 50
        y1 = 220 + math.sin(rad) * 50
        line([(x0, y0), (x1, y1)], (116, 82, 58), 2)
    line([(1066, 220), (1066, 188)], (79, 53, 37), 4)
    line([(1066, 220), (1092, 232)], (79, 53, 37), 3)
    ell(1061, 215, 1071, 225, (108, 73, 51))

    # -- window (right) ----------------------------------------------------
    rect(1178, 92, 1824, 664, (244, 233, 216))
    rect(1198, 112, 1804, 644, (206, 185, 157))
    rect(1212, 126, 1790, 630, (29, 38, 44))

    # sky patch
    sky_w, sky_h = 578, 504
    sy = np.linspace(0.0, 1.0, sky_h)[:, None, None]
    sky_top = np.array([171, 211, 227], dtype=np.float64)
    sky_bot = np.array([255, 224, 177], dtype=np.float64)
    sky_arr = sky_top * (1.0 - sy) + sky_bot * sy
    sky = Image.fromarray(np.clip(sky_arr, 0, 255).astype(np.uint8), "RGB")
    sky = sky.resize((sky_w * S, sky_h * S), Image.LANCZOS)
    img.paste(sky, P(1212, 126))
    d = ImageDraw.Draw(img)

    # skyline / trees
    poly([(1212, 520), (1280, 480), (1330, 500), (1390, 455),
          (1460, 490), (1540, 462), (1620, 500), (1700, 470),
          (1790, 505), (1790, 630), (1212, 630)], (172, 190, 166))
    poly([(1212, 555), (1300, 520), (1360, 545), (1440, 512),
          (1510, 540), (1600, 518), (1680, 548), (1790, 530),
          (1790, 630), (1212, 630)], (137, 160, 140))
    for tx, ty, tr in ((1260, 522, 34), (1440, 500, 40), (1640, 516, 36),
                       (1740, 500, 30)):
        ell(tx - tr, ty - tr, tx + tr, ty + tr, (104, 137, 103))
        ell(tx - tr // 2, ty - tr, tx + tr // 2, ty + tr // 2,
            (125, 158, 116))

    # sun glow + clouds
    sun_glow = Image.new("RGBA", (Ws, Hs), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sun_glow)
    sd.ellipse([P(1490, 150), P(1690, 350)], fill=(255, 230, 165, 120))
    sun_glow = sun_glow.filter(ImageFilter.GaussianBlur(36 * S))
    img = Image.alpha_composite(img.convert("RGBA"), sun_glow).convert("RGB")
    d = ImageDraw.Draw(img)
    ell(1560, 220, 1640, 300, (255, 242, 204))
    for cx, cy, rx, ry in ((1330, 240, 75, 24), (1400, 226, 54, 20),
                           (1690, 330, 80, 22), (1750, 310, 50, 18)):
        ell(cx - rx, cy - ry, cx + rx, cy + ry, (255, 247, 225))

    # window mullions and glass reflection
    rect(1488, 126, 1510, 630, (238, 224, 202))
    rect(1212, 366, 1790, 388, (238, 224, 202))
    line([(1212, 126), (1790, 630)], (255, 255, 255), 2)
    glass = Image.new("RGBA", (Ws, Hs), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glass)
    gd.polygon([P(1250, 610), P(1478, 140), P(1570, 140), P(1340, 610)],
               fill=(255, 255, 255, 26))
    img = Image.alpha_composite(img.convert("RGBA"), glass).convert("RGB")
    d = ImageDraw.Draw(img)

    # curtain rod and curtains
    rect(1088, 82, 1908, 94, (94, 64, 45))
    ell(1080, 74, 1100, 102, (120, 83, 57))
    ell(1896, 74, 1916, 102, (120, 83, 57))

    def curtain(x0, x1, flip=1):
        w = x1 - x0
        edge = []
        for i in range(15):
            y = 100 + i * 40
            xx = x0 + (w * 0.12 if i % 2 else 0)
            edge.append((xx, y))
        edge += [(x1, 700), (x0, 700)]
        poly(edge, (241, 229, 209), (201, 179, 151), 2)
        for k in range(1, 4):
            fx = x0 + w * k / 4
            line([(fx, 110), (fx + 8 * flip, 690)], (216, 197, 173), 2)

    curtain(1112, 1212, 1)
    curtain(1790, 1892, -1)

    # sill + small plant
    rect(1168, 632, 1834, 676, (231, 216, 194))
    rect(1168, 676, 1834, 686, (193, 168, 137))
    poly([(1748, 600), (1792, 600), (1802, 640), (1738, 640)],
         (188, 132, 93), (130, 84, 58), 2)
    for lx, ly, lw, lh in ((1752, 548, 8, 60), (1770, 530, 7, 78),
                           (1784, 552, 7, 56)):
        ell(lx - lw, ly, lx + lw, ly + lh, (109, 139, 96))
    ell(1746, 544, 1764, 562, (109, 139, 96))
    ell(1780, 528, 1798, 546, (128, 157, 107))

    # -- tall plant between console and window ----------------------------
    poly([(1118, 742), (1178, 742), (1190, 842), (1106, 842)],
         (166, 119, 84), (105, 70, 48), 3)
    rect(1110, 720, 1186, 746, (184, 136, 96), (105, 70, 48), 2)
    for lx, ly, rx, ry in ((1130, 620, 20, 56), (1156, 586, 18, 70),
                           (1178, 622, 16, 52), (1110, 646, 16, 42)):
        ell(lx - rx, ly - ry, lx + rx, ly + ry, (92, 126, 86))
    line([(1148, 720), (1148, 620)], (75, 104, 72), 3)
    line([(1148, 700), (1114, 652)], (75, 104, 72), 2)
    line([(1148, 680), (1180, 640)], (75, 104, 72), 2)

    # -- slippers / small details -----------------------------------------
    poly([(740, 890), (802, 890), (810, 914), (730, 914)],
         (197, 178, 155), (135, 111, 90), 2)
    poly([(812, 890), (874, 890), (882, 914), (802, 914)],
         (188, 169, 146), (135, 111, 90), 2)

    # -- light beams + atmosphere -----------------------------------------
    beams = Image.new("RGBA", (Ws, Hs), (0, 0, 0, 0))
    bd = ImageDraw.Draw(beams)
    bd.polygon([P(1212, 630), P(1430, 630), P(1120, 1080), P(650, 1080)],
               fill=(255, 232, 177, 30))
    bd.polygon([P(1470, 630), P(1790, 630), P(1680, 1080), P(1180, 1080)],
               fill=(255, 228, 170, 22))
    beams = beams.filter(ImageFilter.GaussianBlur(22 * S))
    img = Image.alpha_composite(img.convert("RGBA"), beams).convert("RGB")
    d = ImageDraw.Draw(img)

    # dust motes in the light
    rng = random.Random(11)
    motes = Image.new("RGBA", (Ws, Hs), (0, 0, 0, 0))
    md = ImageDraw.Draw(motes)
    for _ in range(70):
        x = rng.uniform(900, 1750)
        y = rng.uniform(220, 960)
        r = rng.uniform(1.0, 3.4)
        a = int(rng.uniform(18, 70))
        md.ellipse([P(x - r, y - r), P(x + r, y + r)],
                   fill=(255, 242, 205, a))
    img = Image.alpha_composite(img.convert("RGBA"), motes).convert("RGB")

    # -- vignette and grain ------------------------------------------------
    arr = np.asarray(img).astype(np.float64)
    yy = np.linspace(-1.0, 1.0, Hs)[:, None, None]
    xx = np.linspace(-1.0, 1.0, Ws)[None, :, None]
    vig = np.clip(1.0 - 0.23 * (xx**2 + yy**2), 0.72, 1.0)
    arr = arr * vig

    noise_rng = np.random.default_rng(7)
    noise = noise_rng.normal(0.0, 2.0, (Hs, Ws, 1))
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    img = Image.fromarray(arr, "RGB").resize((W, H), Image.LANCZOS)

    os.makedirs(os.path.dirname(BG_PATH), exist_ok=True)
    img.save(BG_PATH, optimize=True)
    print("wrote", BG_PATH, img.size)


# ---------------------------------------------------------------------------
# Mother sprite
# ---------------------------------------------------------------------------


def make_mother():
    W, H = 560, 980
    S = 4
    img = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    OUT = (75, 49, 41, 255)
    SKIN = (242, 207, 179, 255)
    SKIN_SH = (224, 178, 151, 255)
    SKIN_HI = (251, 223, 199, 255)
    HAIR = (74, 52, 45, 255)
    HAIR_HI = (119, 82, 64, 255)
    HAIR_SH = (54, 37, 33, 255)
    BLOUSE = (246, 237, 223, 255)
    BLOUSE_SH = (224, 210, 191, 255)
    APRON = (137, 158, 128, 255)
    APRON_SH = (111, 132, 105, 255)
    APRON_HI = (160, 179, 148, 255)
    SKIRT = (93, 75, 70, 255)
    SKIRT_SH = (75, 59, 56, 255)
    EYE = (85, 55, 39, 255)
    IRIS = (151, 99, 61, 255)
    LIP = (172, 108, 92, 255)
    SHOE = (121, 83, 64, 255)
    SHOE_SH = (91, 61, 47, 255)

    def P(x, y):
        return (int(round(x * S)), int(round(y * S)))

    def poly(points, fill, outline=None, width=0):
        pts = [P(x, y) for x, y in points]
        d.polygon(pts, fill=fill)
        if outline and width:
            d.line(pts + [pts[0]], fill=outline, width=max(1, int(width * S)),
                   joint="curve")

    def ell(x0, y0, x1, y1, fill, outline=None, width=0):
        d.ellipse([P(x0, y0), P(x1, y1)], fill=fill, outline=outline,
                  width=max(0, int(width * S)))

    def line(points, fill, width=1):
        d.line([P(x, y) for x, y in points], fill=fill,
               width=max(1, int(width * S)), joint="curve")

    def rrect(x0, y0, x1, y1, r, fill, outline=None, width=0):
        d.rounded_rectangle([P(x0, y0), P(x1, y1)], radius=int(r * S),
                            fill=fill, outline=outline,
                            width=max(0, int(width * S)))

    # floor shadow ---------------------------------------------------------
    shadow = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.ellipse([P(128, 914), P(432, 970)], fill=(60, 40, 30, 70))
    shadow = shadow.filter(ImageFilter.GaussianBlur(12 * S))
    img = Image.alpha_composite(img, shadow)
    d = ImageDraw.Draw(img)

    # back hair ------------------------------------------------------------
    ell(176, 66, 384, 320, HAIR)
    poly([(182, 246), (214, 380), (206, 470), (164, 446), (158, 300)],
         HAIR_SH)
    poly([(352, 248), (386, 390), (400, 470), (356, 450), (338, 316)],
         HAIR)
    # low bun
    ell(338, 104, 412, 182, HAIR, OUT, 2.4)
    ell(350, 116, 402, 168, HAIR_HI)
    poly([(344, 138), (402, 158), (396, 176), (340, 156)], (142, 72, 63))

    # neck ----------------------------------------------------------------
    rrect(250, 280, 310, 350, 18, SKIN)
    poly([(250, 292), (310, 292), (304, 320), (256, 320)], SKIN_SH)

    # skirt ---------------------------------------------------------------
    poly([(206, 592), (354, 592), (396, 906), (162, 906)],
         SKIRT, OUT, 2.6)
    poly([(220, 610), (250, 610), (240, 896), (186, 896)], SKIRT_SH)
    poly([(310, 610), (338, 610), (370, 896), (322, 896)], SKIRT_SH)
    line([(280, 608), (280, 900)], (80, 64, 60), 1.4)
    line([(250, 620), (238, 890)], (112, 91, 84), 1.2)
    line([(318, 620), (334, 890)], (112, 91, 84), 1.2)

    # torso / blouse ------------------------------------------------------
    torso = [(190, 330), (220, 314), (340, 314), (372, 332),
             (382, 520), (366, 626), (196, 626), (176, 526)]
    poly(torso, BLOUSE, OUT, 2.6)
    # soft side shadows
    poly([(190, 340), (212, 330), (198, 610), (180, 520)], BLOUSE_SH)
    poly([(352, 330), (372, 340), (380, 520), (362, 608)], BLOUSE_SH)
    # collar
    poly([(250, 306), (280, 352), (310, 306), (300, 298),
          (280, 330), (260, 298)], (255, 250, 240), OUT, 2)
    line([(280, 352), (280, 410)], (216, 202, 184), 1.4)
    for by in (390, 430, 470):
        ell(276, by, 284, by + 8, (221, 205, 185))

    # apron bib -----------------------------------------------------------
    poly([(226, 380), (334, 380), (342, 608), (218, 608)],
         APRON, OUT, 2.4)
    poly([(226, 380), (254, 380), (246, 600), (218, 600)], APRON_SH)
    poly([(306, 380), (334, 380), (342, 600), (316, 600)], APRON_HI)
    # straps
    line([(233, 382), (211, 330)], APRON_SH, 7)
    line([(233, 382), (211, 330)], OUT, 1.5)
    line([(327, 382), (351, 330)], APRON_SH, 7)
    line([(327, 382), (351, 330)], OUT, 1.5)
    # waistband
    rrect(210, 588, 350, 612, 8, APRON_SH, OUT, 1.8)
    # apron skirt
    poly([(210, 604), (350, 604), (382, 892), (176, 892)],
         APRON, OUT, 2.4)
    poly([(210, 604), (240, 604), (214, 884), (180, 884)], APRON_SH)
    poly([(322, 604), (350, 604), (378, 884), (344, 884)], APRON_HI)
    # pocket
    rrect(238, 690, 322, 770, 8, APRON_SH, OUT, 1.8)
    line([(238, 714), (322, 714)], (94, 115, 90), 1.6)
    # folded handkerchief in pocket
    poly([(260, 684), (294, 680), (302, 706), (254, 710)],
         (220, 158, 112), OUT, 1.6)
    line([(262, 692), (292, 690)], (244, 190, 145), 2)

    # arms ----------------------------------------------------------------
    # left sleeve
    poly([(192, 342), (228, 350), (212, 508), (172, 496)],
         BLOUSE, OUT, 2.4)
    poly([(192, 342), (208, 348), (190, 496), (172, 490)], BLOUSE_SH)
    # left forearm
    poly([(174, 494), (212, 506), (242, 606), (210, 618)],
         SKIN, OUT, 2.4)
    poly([(174, 494), (190, 500), (220, 604), (210, 610)], SKIN_HI)
    ell(228, 604, 270, 642, SKIN, OUT, 2.2)
    # right sleeve
    poly([(352, 342), (388, 350), (408, 496), (368, 508)],
         BLOUSE, OUT, 2.4)
    poly([(372, 348), (388, 352), (404, 492), (388, 500)], BLOUSE_SH)
    # right forearm
    poly([(366, 506), (406, 494), (350, 618), (318, 606)],
         SKIN, OUT, 2.4)
    poly([(388, 500), (406, 494), (338, 610), (326, 606)], SKIN_HI)
    ell(292, 604, 334, 642, SKIN, OUT, 2.2)

    # clasped hands / fingers
    ell(242, 616, 300, 660, SKIN, OUT, 2.2)
    line([(250, 626), (272, 630), (292, 624)], (198, 145, 124), 2.2)
    line([(252, 638), (274, 642), (290, 636)], (198, 145, 124), 2)
    line([(254, 648), (274, 652), (286, 647)], (198, 145, 124), 1.8)

    # head ----------------------------------------------------------------
    # ears
    ell(190, 174, 218, 224, SKIN, OUT, 2)
    ell(342, 174, 370, 224, SKIN, OUT, 2)
    ell(198, 190, 210, 208, SKIN_SH)
    ell(350, 190, 362, 208, SKIN_SH)
    # pearl earrings
    ell(198, 220, 208, 230, (242, 228, 195), OUT, 1.2)
    ell(352, 220, 362, 230, (242, 228, 195), OUT, 1.2)

    # face
    ell(202, 92, 358, 300, SKIN, OUT, 2.4)
    # cheek shading
    poly([(212, 210), (238, 246), (222, 286), (206, 250)], SKIN_SH)
    poly([(348, 210), (322, 246), (338, 286), (354, 250)], SKIN_SH)

    # hair cap / bangs
    hair_cap = ([(196, 178)]
                + qbez((196, 178), (204, 88), (280, 70), 22)
                + qbez((280, 70), (356, 88), (364, 178), 22)
                + [(354, 180), (334, 162), (320, 184), (300, 158),
                   (280, 186), (260, 158), (240, 184), (220, 162),
                   (206, 180)])
    poly(hair_cap, HAIR, OUT, 2.2)
    # side locks
    poly([(194, 162), (220, 158), (224, 264), (208, 300),
          (188, 260)], HAIR, OUT, 2)
    poly([(340, 158), (364, 166), (370, 262), (354, 302),
          (336, 262)], HAIR, OUT, 2)
    # bun highlight and hair strands
    line([(214, 120), (240, 100), (270, 94)], HAIR_HI, 2)
    line([(300, 100), (330, 122), (344, 150)], HAIR_HI, 2)
    line([(210, 170), (220, 244)], HAIR_SH, 1.4)
    line([(350, 172), (340, 248)], HAIR_SH, 1.4)

    # eyebrows
    line([(232, 184), (250, 178), (266, 183)], (90, 59, 43), 2.4)
    line([(294, 183), (310, 178), (328, 184)], (90, 59, 43), 2.4)

    # eyes
    for cx in (246, 314):
        # white
        ell(cx - 19, 196, cx + 19, 232, (255, 252, 246), OUT, 1.6)
        # iris
        ell(cx - 11, 201, cx + 11, 229, IRIS)
        ell(cx - 8, 205, cx + 8, 225, EYE)
        # pupil + highlight
        ell(cx - 4, 211, cx + 4, 221, (39, 27, 23))
        ell(cx - 7, 204, cx - 1, 210, (255, 250, 238))
        ell(cx + 3, 218, cx + 6, 221, (255, 250, 238))
        # lashes / upper lid
        line([(cx - 18, 198), (cx - 9, 192), (cx + 10, 193),
              (cx + 18, 199)], (70, 45, 35), 2.2)
    # nose
    line([(277, 234), (282, 242), (276, 245)], (198, 145, 124), 1.6)
    # mouth
    line([(264, 260), (280, 268), (296, 260)], LIP, 2.4)
    line([(278, 268), (282, 268)], (147, 87, 76), 1.2)
    # blush
    blush = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    bd = ImageDraw.Draw(blush)
    bd.ellipse([P(216, 228), P(252, 252)], fill=(232, 142, 132, 55))
    bd.ellipse([P(308, 228), P(344, 252)], fill=(232, 142, 132, 55))
    blush = blush.filter(ImageFilter.GaussianBlur(5 * S))
    img = Image.alpha_composite(img, blush)
    d = ImageDraw.Draw(img)

    # slippers ------------------------------------------------------------
    poly([(218, 900), (286, 900), (296, 936), (206, 936)],
         SHOE, OUT, 2)
    poly([(274, 900), (342, 900), (352, 936), (264, 936)],
         SHOE_SH, OUT, 2)
    line([(220, 914), (286, 914)], (166, 123, 96), 2)
    line([(278, 914), (344, 914)], (149, 108, 84), 2)

    # final rim light on the window-facing side
    rim = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    rd = ImageDraw.Draw(rim)
    rd.line([P(352, 150), P(368, 240), P(360, 300)],
            fill=(255, 231, 194, 90), width=int(2.2 * S))
    rd.line([P(372, 340), P(382, 500), P(360, 610)],
            fill=(255, 231, 194, 55), width=int(2.0 * S))
    rim = rim.filter(ImageFilter.GaussianBlur(1.2 * S))
    img = Image.alpha_composite(img, rim)

    img = img.resize((W, H), Image.LANCZOS)
    os.makedirs(os.path.dirname(CHAR_PATH), exist_ok=True)
    img.save(CHAR_PATH, optimize=True)
    print("wrote", CHAR_PATH, img.size)


if __name__ == "__main__":
    make_background()
    make_mother()
