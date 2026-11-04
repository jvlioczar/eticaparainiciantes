"""Gera os PNG do site (ícones e imagem de compartilhamento) com Pillow. Uso: python tools/icones.py. Não faz parte do build."""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, 'assets')
PAPEL, NOITE = (249, 248, 244), (31, 90, 76)
def grad(w, h, c1, c2, horizontal=True):
    im = Image.new('RGB', (w, h))
    d = ImageDraw.Draw(im)
    n = w if horizontal else h
    for i in range(n):
        t = i / max(1, n - 1); c = tuple(round(c1[k] + (c2[k] - c1[k]) * t) for k in range(3))
        if horizontal: d.line([(i, 0), (i, h)], fill=c)
        else: d.line([(0, i), (w, i)], fill=c)
    return im
def anel(im, cx, cy, r, w, c1, c2, s=4):
    """Anel com gradiente, desenhado em alta resolução e reduzido (antialiasing)."""
    W, H = im.size
    g = grad(W * s, H * s, c1, c2)
    m = Image.new('L', (W * s, H * s), 0)
    d = ImageDraw.Draw(m)
    d.ellipse([(cx - r) * s, (cy - r) * s, (cx + r) * s, (cy + r) * s], fill=255)
    if w < r: d.ellipse([(cx - r + w) * s, (cy - r + w) * s, (cx + r - w) * s, (cy + r - w) * s], fill=0)
    m = m.resize((W, H), Image.LANCZOS); g = g.resize((W, H), Image.LANCZOS)
    im.paste(g, (0, 0), m)
def logo(im, cx, cy, R):
    anel(im, cx, cy, R, R * .2, (134, 197, 232), (106, 99, 217))
    anel(im, cx, cy, R * .6, R * .2, (227, 210, 106), (47, 160, 138))
    anel(im, cx, cy, R * .24, R * .24, (245, 179, 91), (228, 97, 95))
def icone(n, fundo):
    im = Image.new('RGB', (n, n), fundo)
    logo(im, n / 2, n / 2, n * .42)
    return im
for n in (192, 512): icone(n, NOITE).save(os.path.join(A, f'icon-{n}.png'), optimize=True)
icone(180, NOITE).save(os.path.join(A, 'icon-180.png'), optimize=True)
# imagem de compartilhamento 1200x630
im = Image.new('RGB', (1200, 630), NOITE)
d = ImageDraw.Draw(im)
logo(im, 960, 315, 190)
def fonte(nomes, tam):
    for n in nomes:
        p = os.path.join('C:/Windows/Fonts', n)
        if os.path.exists(p): return ImageFont.truetype(p, tam)
    return ImageFont.load_default()
f1 = fonte(['georgiab.ttf', 'georgia.ttf', 'times.ttf'], 86); f2 = fonte(['segoeui.ttf', 'arial.ttf'], 32); f3 = fonte(['segoeuib.ttf', 'arialbd.ttf'], 24)
d.text((80, 170), 'Ética', font=f1, fill=(255, 255, 255)); d.text((80, 270), 'Para Iniciantes', font=f1, fill=(255, 255, 255))
d.text((80, 400), 'Teorias, círculo moral, metaética e dilemas,', font=f2, fill=(201, 222, 214)); d.text((80, 442), 'do básico ao avançado, com fontes.', font=f2, fill=(201, 222, 214))
d.text((80, 540), 'eticaparainiciantes.biblioverse.org  ·  BiblioVerse', font=f3, fill=(227, 210, 106))
im.save(os.path.join(A, 'share.png'), optimize=True)
print('ok')
