#!/usr/bin/env python3
"""Build-time generator for the news-image-20261119 entry.

Draws the front page (1024x1024) and saves it as entry.png beside this
file. This is NOT the entrypoint: the site's runner has no Pillow, so
main.py is a stdlib-only copier that delivers the committed entry.png
byte for byte. Run this only where Pillow is installed, to regenerate
the picture. The two panel illustrations (Vice City, tanker) are
build-workspace files; ART_DIR points at them.

Full-day edition for Thursday 19 November 2026: GTA VI's launch day
closes with an estimated $2.36bn in sales (Sensor Tower); the World
Court finds Myanmar committed genocide against the Rohingya; Trump, Xi
and Putin end their Shenzhen summit with a peace declaration; five
tankers hit mines in the Strait of Hormuz in two days; NASA confirms
Voyager 1 at one light-day; a Van Gogh sells for a record $190.4M.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 231)
INK = (20, 24, 29)
RED = (200, 16, 46)
GREY = (88, 94, 102)
BODY = (52, 58, 64)
WHITE = (255, 255, 255)
GOLD = (212, 160, 32)
ART_DIR = "/home/hatch/workspace/makefun/news-image-20261119/work"
HERE = os.path.dirname(os.path.abspath(__file__))

F_BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"
F_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
F_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

def tw(d, s, f):
    return d.textlength(s, font=f)

def center(d, cx, y, s, f, fill):
    d.text((cx - tw(d, s, f) / 2, y), s, font=f, fill=fill)

def wrap(d, s, f, max_w):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(d, t, f) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur:
        lines.append(cur)
    return lines

def paste_cover(canvas, im, box):
    x0, y0, x1, y1 = box
    tw_, th_ = x1 - x0, y1 - y0
    iw, ih = im.size
    sc = max(tw_ / iw, th_ / ih)
    nw, nh = int(iw * sc + 0.5), int(ih * sc + 0.5)
    r = im.resize((nw, nh), Image.LANCZOS)
    ox, oy = (nw - tw_) // 2, (nh - th_) // 2
    canvas.paste(r.crop((ox, oy, ox + tw_, oy + th_)), (x0, y0))

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
center(d, W // 2, 14, "T H E   W O R L D   I N   O N E   P I C T U R E", F(F_BOLD, 21), GREY)
center(d, W // 2, 40, "THURSDAY 19 NOVEMBER 2026", F(F_BLACK, 57), INK)
d.rectangle([28, 106, 996, 112], fill=INK)
d.rectangle([28, 116, 996, 118], fill=INK)

# ---------- lead: GTA VI ----------
vice = Image.open(ART_DIR + "/media-generation-panel-vice-city-0-dc0eb8fd-ee83-40b0-964a-c3bb29fb68ce.png").convert("RGB")
paste_cover(img, vice, (28, 128, 996, 438))
d.rectangle([28, 128, 996, 438], outline=INK, width=2)
d.rectangle([28, 448, 172, 474], fill=RED)
d.text((39, 452), "THE BIG STORY", font=F(F_BOLD, 18), fill=WHITE)
d.text((28, 480), "GTA VI EARNS $2.36BN IN A DAY", font=F(F_BLACK, 46), fill=INK)
sub = "Sensor Tower counts 24.6 million copies sold in 24 hours \u2014 the biggest entertainment launch in history, nearly triple GTA V's first day."
for i, line in enumerate(wrap(d, sub, F(F_REG, 21), 968)):
    d.text((28, 536 + i * 27), line, font=F(F_REG, 21), fill=BODY)
d.rectangle([28, 598, 996, 601], fill=INK)

# ---------- middle row ----------
tanker = Image.open(ART_DIR + "/media-generation-panel-tanker-0-9ad66c44-70e5-449d-ba15-0ac3c661afc2.png").convert("RGB")
paste_cover(img, tanker, (28, 612, 502, 716))
d.rectangle([28, 612, 502, 716], outline=INK, width=2)
for i, line in enumerate(wrap(d, "OIL TANKERS ABLAZE IN THE STRAIT OF HORMUZ", F(F_BLACK, 26), 474)):
    d.text((28, 724 + i * 31), line, font=F(F_BLACK, 26), fill=INK)
cap = "Five tankers hit mines in two days; US jets strike a missile site on Qeshm Island."
for i, line in enumerate(wrap(d, cap, F(F_REG, 19), 474)):
    d.text((28, 790 + i * 24), line, font=F(F_REG, 19), fill=BODY)

# summit panel art (drawn): Chinese rooftops + CN / US / RU flags
sx0, sy0, sx1, sy1 = 522, 612, 996, 716
for i in range(sy1 - sy0):
    t = i / (sy1 - sy0)
    d.line([(sx0, sy0 + i), (sx1, sy0 + i)], fill=(int(38 + 60 * t), int(30 + 26 * t), int(52 + 8 * t)))
def roof(cx, base, w_, h_, col):
    d.polygon([(cx - w_ // 2, base), (cx + w_ // 2, base), (cx + w_ // 4, base - h_), (cx - w_ // 4, base - h_)], fill=col)
    d.rectangle([cx - w_ // 4, base - h_, cx + w_ // 4, base - h_ + 5], fill=col)
SIL = (22, 18, 32)
def pagoda(cx, base, w_):
    tiers = [(1.0, 0), (0.78, 15), (0.56, 29), (0.36, 42)]
    for frac, lift in tiers:
        tw_ = int(w_ * frac)
        yb = base - lift
        d.rectangle([cx - tw_ // 2, yb - 7, cx + tw_ // 2, yb], fill=SIL)
        d.line([(cx - tw_ // 2, yb - 7), (cx + tw_ // 2, yb - 7)], fill=GOLD, width=2)
        if lift:
            d.rectangle([cx - int(tw_ * 0.36), yb, cx + int(tw_ * 0.36), yb + 8], fill=SIL)
    d.rectangle([cx - int(w_ * 0.30), base - 8, cx + int(w_ * 0.30), base], fill=SIL)
for cx, w_ in [(592, 140), (700, 180), (822, 160), (946, 140)]:
    pagoda(cx, sy1, w_)
def flag(x, y, kind):
    fw, fh = 56, 36
    if kind == "CN":
        d.rectangle([x, y, x + fw, y + fh], fill=(222, 41, 16))
        d.polygon([(x + 10, y + 6), (x + 12.5, y + 12), (x + 19, y + 12), (x + 14, y + 16), (x + 16, y + 22), (x + 10, y + 18), (x + 4, y + 22), (x + 6, y + 16), (x, y + 12), (x + 7.5, y + 12)], fill=(255, 222, 0))
        for dx, dy in [(24, 4), (27, 11), (27, 19), (24, 26)]:
            d.ellipse([x + dx, y + dy, x + dx + 4, y + dy + 4], fill=(255, 222, 0))
    elif kind == "US":
        for i in range(7):
            col = (178, 34, 52) if i % 2 == 0 else (255, 255, 255)
            d.rectangle([x, y + i * fh // 7, x + fw, y + (i + 1) * fh // 7], fill=col)
        d.rectangle([x, y, x + 24, y + 19], fill=(60, 59, 110))
        for r in range(3):
            for c in range(4):
                d.ellipse([x + 3 + c * 6, y + 3 + r * 6, x + 5 + c * 6, y + 5 + r * 6], fill=WHITE)
    else:
        d.rectangle([x, y, x + fw, y + 12], fill=WHITE)
        d.rectangle([x, y + 12, x + fw, y + 24], fill=(0, 57, 166))
        d.rectangle([x, y + 24, x + fw, y + fh], fill=(213, 43, 30))
for px, kind in [(600, "CN"), (731, "US"), (862, "RU")]:
    d.line([(px, sy0 + 14), (px, sy1 - 20)], fill=(230, 228, 220), width=3)
    flag(px + 3, sy0 + 14, kind)
d.rectangle([sx0, sy0, sx1, sy1], outline=INK, width=2)
for i, line in enumerate(wrap(d, "TRUMP, XI, PUTIN SIGN PEACE DECLARATION", F(F_BLACK, 26), 474)):
    d.text((522, 724 + i * 31), line, font=F(F_BLACK, 26), fill=INK)
cap2 = "Ends in Shenzhen with a four-point peace declaration; no deal on Ukraine."
for i, line in enumerate(wrap(d, cap2, F(F_REG, 19), 474)):
    d.text((522, 790 + i * 24), line, font=F(F_REG, 19), fill=BODY)
d.rectangle([28, 848, 996, 851], fill=INK)

# ---------- bottom row: three text cards ----------
# (band set 6px higher than the morning edition so caption text
#  clears the footer ticker instead of grazing it)
cards = [
    ("THE HAGUE", "MYANMAR GUILTY OF GENOCIDE",
     "First genocide verdict ever against a state; reparations ordered."),
    ("DEEP SPACE", "VOYAGER 1 REACHES ONE LIGHT-DAY",
     "NASA confirms the milestone: its signals now take a full day."),
    ("ART MARKET", "VAN GOGH SELLS FOR RECORD $190.4M",
     "The 'Blossoming Chestnut Trees' canvas: fourth-priciest ever sold."),
]
for i, (kick, head, cap_) in enumerate(cards):
    x = 28 + i * 330
    d.rectangle([x, 854, x + 309, 859], fill=RED)
    d.text((x, 866), kick, font=F(F_BOLD, 15), fill=RED)
    for j, line in enumerate(wrap(d, head, F(F_BLACK, 21), 309)):
        d.text((x, 884 + j * 24), line, font=F(F_BLACK, 21), fill=INK)
    for j, line in enumerate(wrap(d, cap_, F(F_REG, 16), 309)):
        d.text((x, 932 + j * 19), line, font=F(F_REG, 16), fill=BODY)

# ---------- footer ticker ----------
d.rectangle([0, 974, 1024, 1024], fill=INK)
tick = "Christmas Island's red crabs begin their march to the sea  \u00b7  EU proposes a \u20ac45bn loan for Ukraine  \u00b7  Hegseth signs a defence pact in Venezuela  \u00b7  France jails three women for joining ISIS"
total = "ALSO TODAY:  " + tick
lines = wrap(d, total, F(F_REG, 16), 968)
for i, line in enumerate(lines[:2]):
    center(d, W // 2, 980 + i * 19, line, F(F_REG, 16), (235, 232, 222))

out = os.path.join(HERE, "entry.png")
img.save(out, optimize=True)
print("saved", out, img.size, os.path.getsize(out), "bytes")
