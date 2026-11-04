"""Ilustrações geométricas do site: círculos concêntricos (o círculo moral que se expande), feitos só de círculos e retângulos com gradiente."""
DEFS = '''<defs>
<linearGradient id="gC" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f5b35b"/><stop offset="1" stop-color="#e4615f"/></linearGradient>
<linearGradient id="gV" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e3d26a"/><stop offset="1" stop-color="#2fa08a"/></linearGradient>
<linearGradient id="gA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#86c5e8"/><stop offset="1" stop-color="#6a63d9"/></linearGradient>
<linearGradient id="gL" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6c9a6"/><stop offset="1" stop-color="#e9868c"/></linearGradient>
</defs>'''
def q(x, y, r, c, f):
    """Quarto de círculo com o centro em (x, y). c: ne, no, se, so."""
    a, b = {'ne': (1, -1), 'no': (-1, -1), 'se': (1, 1), 'so': (-1, 1)}[c]
    return f'<path d="M{x} {y}L{x + a * r} {y}A{r} {r} 0 0 {1 if a * b > 0 else 0} {x} {y + b * r}Z" fill="url(#{f})"/>'
def r(x, y, w, h, f, rx=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="url(#{f})"/>'
def c(x, y, s, f):
    return f'<circle cx="{x}" cy="{y}" r="{s}" fill="url(#{f})"/>'
def anel(x, y, s, w, f, op=1):
    return f'<circle cx="{x}" cy="{y}" r="{s}" fill="none" stroke="url(#{f})" stroke-width="{w}" opacity="{op}"/>'
def meio(x, y, s, f, cima=True):
    d = 1 if cima else 0
    return f'<path d="M{x - s} {y}A{s} {s} 0 0 {d} {x + s} {y}Z" fill="url(#{f})"/>'
def hero():
    # o círculo moral: anéis que se expandem a partir de um ponto (eu, os próximos, todos os humanos, todos os que sentem)
    # mesma caixa (620x365) e mesma plataforma da ilustração do Política Para Iniciantes, para o herói ter a mesma altura
    p = [DEFS]
    p += [anel(320, 190, 150, 20, 'gA', .35), anel(320, 190, 110, 20, 'gV', .55), anel(320, 190, 70, 20, 'gC', .8), c(320, 190, 34, 'gC')]
    p += [c(320, 118, 8, 'gC'), c(382, 150, 8, 'gV'), c(428, 206, 8, 'gV'), c(320, 300, 8, 'gA'), c(192, 216, 8, 'gA'), c(230, 108, 8, 'gA')]
    p += [r(20, 340, 600, 24, 'gA', 4), r(70, 364, 500, 16, 'gL', 3)]
    return f'<svg class="arte" viewBox="10 25 620 365" role="img" aria-label="Ilustração geométrica de círculos concêntricos, o círculo moral que se expande">{"".join(p)}</svg>'

ICONES = {
 'circulo': lambda: anel(32, 32, 26, 6, 'gA', .5) + anel(32, 32, 16, 6, 'gV') + c(32, 32, 7, 'gC'),
 'balanca': lambda: r(29, 8, 6, 46, 'gA', 2) + r(10, 16, 44, 5, 'gA', 2) + meio(17, 36, 11, 'gC', cima=False) + meio(47, 32, 11, 'gV', cima=False) + r(20, 52, 24, 5, 'gL', 2),
 'bonde': lambda: r(10, 16, 44, 28, 'gC', 6) + r(16, 22, 12, 10, 'gL', 2) + r(36, 22, 12, 10, 'gL', 2) + c(20, 50, 6, 'gA') + c(44, 50, 6, 'gA') + r(6, 57, 52, 3, 'gV', 1),
 'valor': lambda: r(8, 26, 48, 6, 'gA', 2) + r(29, 12, 6, 42, 'gA', 2) + meio(16, 34, 11, 'gC', cima=False) + meio(48, 34, 11, 'gV', cima=False),
 'compara': lambda: r(8, 14, 21, 40, 'gC', 4) + r(35, 8, 21, 46, 'gV', 4),
 'arvore': lambda: c(32, 13, 8, 'gA') + c(14, 48, 8, 'gC') + c(50, 48, 8, 'gV') + r(30, 20, 4, 16, 'gA') + r(14, 34, 36, 4, 'gA') + r(12, 36, 4, 6, 'gC') + r(48, 36, 4, 6, 'gV'),
 'troca': lambda: q(30, 30, 22, 'no', 'gC') + q(34, 34, 22, 'se', 'gA'),
 'ficha': lambda: r(12, 6, 40, 52, 'gL', 5) + r(19, 18, 26, 4, 'gA') + r(19, 28, 26, 4, 'gA') + r(19, 38, 16, 4, 'gA'),
 'pessoa': lambda: c(32, 17, 10, 'gC') + q(32, 54, 24, 'no', 'gA') + q(32, 54, 24, 'ne', 'gV'),
 'livro': lambda: r(9, 10, 21, 44, 'gC', 3) + r(34, 10, 21, 44, 'gV', 3),
 'pata': lambda: c(20, 20, 6, 'gC') + c(32, 14, 6, 'gC') + c(44, 20, 6, 'gC') + meio(32, 50, 17, 'gV', cima=True) + r(15, 50, 34, 6, 'gV', 3),
 'lampada': lambda: c(32, 26, 18, 'gV') + r(24, 42, 16, 8, 'gA', 2) + r(26, 52, 12, 5, 'gA', 2),
 'ponto': lambda: c(32, 32, 24, 'gA') + c(32, 32, 14, 'gL') + c(32, 32, 6, 'gC'),
 'rede': lambda: ''.join(c(14 + 12 * (i % 4), 16 + 12 * (i // 4), 5, ['gC', 'gA', 'gV'][i % 3]) for i in range(12)),
}
def icone(n):
    return f'<svg class="ico" viewBox="0 0 64 64" aria-hidden="true">{DEFS.replace("gC", "gC" + n).replace("gV", "gV" + n).replace("gA", "gA" + n).replace("gL", "gL" + n)}{ICONES[n]().replace("#gC", "#gC" + n).replace("#gV", "#gV" + n).replace("#gA", "#gA" + n).replace("#gL", "#gL" + n)}</svg>'
LOGO = '<svg viewBox="0 0 40 40" width="34" height="34" aria-hidden="true"><defs><linearGradient id="lgA" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#e4615f"/><stop offset="1" stop-color="#f5b35b"/></linearGradient><linearGradient id="lgB" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#2fa08a"/><stop offset="1" stop-color="#e3d26a"/></linearGradient><linearGradient id="lgC" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#6a63d9"/><stop offset="1" stop-color="#86c5e8"/></linearGradient></defs><circle cx="20" cy="20" r="17" fill="none" stroke="url(#lgC)" stroke-width="4"/><circle cx="20" cy="20" r="10" fill="none" stroke="url(#lgB)" stroke-width="4"/><circle cx="20" cy="20" r="4" fill="url(#lgA)"/></svg>'
