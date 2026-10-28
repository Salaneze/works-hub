"""Превью карточек хаба: 720x450 jpg.

Сайты — первый экран живой страницы. Боты — экран телефона на подложке в цвет работы:
вертикальный скрин, обрезанный в 16:10, читается как обрывок.
"""
import sys

from PIL import Image, ImageDraw, ImageFilter

SHOTS = sys.argv[1]
PF = "C:/dev/fl-portfolio/"
OUT = "C:/dev/web/works-hub/img/"
W, H = 720, 450


def site(src, name):
    im = Image.open(src).convert("RGB")
    im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS).crop((0, 0, W, H))
    im.save(OUT + name + ".jpg", quality=82, optimize=True, progressive=True)


def phone(src, name, bg, top=0, box=None):
    im = Image.open(src).convert("RGB")
    if box:
        im = im.crop(box)
    ph = im.resize((300, round(im.height * 300 / im.width)), Image.LANCZOS).crop((0, top, 300, top + 520))
    card = Image.new("RGB", (W, H), bg)
    mask = Image.new("L", ph.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *ph.size), 28, fill=255)
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).rounded_rectangle((210, 70, 510, 590), 28, fill=90)
    card.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(22)))
    card.paste(ph, (210, 52), mask)
    card.save(OUT + name + ".jpg", quality=82, optimize=True, progressive=True)


site(f"{SHOTS}/britva.png", "site-britva")
site(f"{SHOTS}/pitline.png", "site-pitline")
site(f"{SHOTS}/beauty.png", "site-beauty")
# 1_watch_demo_catalog — уже макет с телефоном, берём только экран
phone(PF + "1_watch_demo_catalog.png", "bot-shop", (58, 46, 24), box=(300, 104, 896, 1396))
phone(PF + "6_britva_app_light_services.png", "bot-britva", (201, 163, 91))
print("ok")
