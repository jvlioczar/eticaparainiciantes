"""Gera todas as páginas do site. Uso: python tools/build.py"""
import json, os, re, sys, unicodedata
from html import escape as e
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from licoes_iniciante import INICIANTE
from licoes_intermediario import INTERMEDIARIO
from licoes_intermediario_b import INTERMEDIARIO_B
from licoes_avancado import AVANCADO
from extras import TEMAS, META, ORDEM_GRUPOS
from reforco import REFORCO
from teorias import T_ as TEO, FAMILIAS, FOCO_FAM
from dilemas import DILEMAS, TEMAS_D
from filosofos import F as FIL, CORRENTES
from glossario import GLOSSARIO, GRUPOS_G
from biblioteca import LIVROS, SECOES_L, SITES, GRUPOS_S, NAC, INT
from ferramentas import FERR, TEORIAS_OPS, FRASES_TEORIA, FRASES_FV, TROCA, BONDE
from licoes_novas import NOVAS_INICIANTE, NOVAS_INTERMEDIARIO, NOVAS_AVANCADO, META_NOVAS, REFORCO_NOVAS, POSICAO
from licoes_novas2 import NOVAS2_INICIANTE, NOVAS2_INTERMEDIARIO, NOVAS2_AVANCADO, META_NOVAS2, REFORCO_NOVAS2, POSICAO2
from licoes_novas3 import NOVAS3_INICIANTE, NOVAS3_INTERMEDIARIO, NOVAS3_AVANCADO, META_NOVAS3, REFORCO_NOVAS3, POSICAO3
from licoes_novas5 import NOVAS5_INICIANTE, NOVAS5_INTERMEDIARIO, NOVAS5_AVANCADO, META_NOVAS5, REFORCO_NOVAS5, POSICAO5
from teorias_novas2 import T_NOVAS2
from filosofos_novos3 import F_NOVOS3
from debates11 import DEBATES11
from debates12 import DEBATES12
from licoes_novas4 import NOVAS4_INICIANTE, NOVAS4_INTERMEDIARIO, NOVAS4_AVANCADO, META_NOVAS4, REFORCO_NOVAS4, POSICAO4
from teorias_novas import T_NOVAS
from filosofos_novos2 import F_NOVOS2, CORRENTES_NOVAS
from dilemas2 import DILEMAS2, TEMAS_D2
from debates5 import DEBATES5, TEMAS_DB5
from debates6 import DEBATES6
from debates7 import DEBATES7
from debates8 import DEBATES8
from debates9 import DEBATES9
from debates10 import DEBATES10, TEMAS_DB10
from didatica_1 import D1
from didatica_2 import D2
from didatica_3 import D3
from trilhas import TRILHAS, CASOS_FIO, RESPOSTAS_FIO
from fecho import F as FECHO
from licoes_novas6 import NOVAS6_INTERMEDIARIO, META_NOVAS6, REFORCO_NOVAS6, POSICAO6, DID6, FECHO6
from licoes_novas7 import NOVAS7_INTERMEDIARIO, NOVAS7_AVANCADO, META_NOVAS7, REFORCO_NOVAS7, POSICAO7, DID7, FECHO7
FECHO.update(FECHO7)
FECHO.update(FECHO6)
DID = {**D1, **D2, **D3}
DID.update(DID6); DID.update(DID7)
from ferramentas2 import FERR2, VEU, QUEM_OPS, QUEM, ER_CASOS, ER_PRINCIPIOS, ER_PARES
from filosofos_novos import F_NOVOS, MUDA_CORRENTE
from debates import DEBATES, ROT_PESO, TEMAS_DB
from criterios_dados import DELIM, FRONTEIRAS, GRAUS, DIMENSOES, FONTES_CRIT
from debates2 import DEBATES2, TEMAS_DB2
from debates3 import DEBATES3, TEMAS_DB3
from debates4 import DEBATES4
DEBATES.extend(DEBATES2); DEBATES.extend(DEBATES3); DEBATES.extend(DEBATES4); DEBATES.extend(DEBATES5); DEBATES.extend(DEBATES6); DEBATES.extend(DEBATES7); DEBATES.extend(DEBATES8); DEBATES.extend(DEBATES9); DEBATES.extend(DEBATES10); DEBATES.extend(DEBATES11); DEBATES.extend(DEBATES12); TEMAS_DB.extend(TEMAS_DB5); TEMAS_DB.extend(TEMAS_DB10); DILEMAS.extend(DILEMAS2); TEMAS_D.extend(TEMAS_D2); FERR.extend(FERR2); TEMAS_DB.extend(TEMAS_DB2); TEMAS_DB.extend(TEMAS_DB3)
assert len({d['s'] for d in DEBATES}) == len(DEBATES)
import arte

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://eticaparainiciantes.biblioverse.org'
NOME = 'Ética Para Iniciantes'
EXT = 'target="_blank" rel="noopener"'
ATUALIZADO = '2026-11-05'
INTERMEDIARIO.extend(INTERMEDIARIO_B)
# ética animal passa para o Avançado (pedido de 2026-11-03); as lições novas entram depois da lição indicada em POSICAO
AVANCADO.extend([l for l in INTERMEDIARIO if l['grupo'] == 'Ética animal']); INTERMEDIARIO[:] = [l for l in INTERMEDIARIO if l['grupo'] != 'Ética animal']
META.update(META_NOVAS); REFORCO.update(REFORCO_NOVAS)
def _apos(ls, slug, nova): ls.insert(next(i for i, l in enumerate(ls) if l['slug'] == slug) + 1, nova)
for _ls, _novas in ((INICIANTE, NOVAS_INICIANTE), (INTERMEDIARIO, NOVAS_INTERMEDIARIO), (AVANCADO, NOVAS_AVANCADO)):
    for _l in _novas: _apos(_ls, POSICAO[_l['slug']], _l)
META.update(META_NOVAS2); REFORCO.update(REFORCO_NOVAS2)
for _ls, _novas in ((INICIANTE, NOVAS2_INICIANTE), (INTERMEDIARIO, NOVAS2_INTERMEDIARIO), (AVANCADO, NOVAS2_AVANCADO)):
    for _l in _novas: _apos(_ls, POSICAO2[_l['slug']], _l)
META.update(META_NOVAS3); REFORCO.update(REFORCO_NOVAS3); META.update(META_NOVAS4); REFORCO.update(REFORCO_NOVAS4)
for _ls, _novas in ((INICIANTE, NOVAS3_INICIANTE), (INTERMEDIARIO, NOVAS3_INTERMEDIARIO), (AVANCADO, NOVAS3_AVANCADO)):
    for _l in _novas: _apos(_ls, POSICAO3[_l['slug']], _l)
for _ls, _novas in ((INICIANTE, NOVAS4_INICIANTE), (INTERMEDIARIO, NOVAS4_INTERMEDIARIO), (AVANCADO, NOVAS4_AVANCADO)):
    for _l in _novas: _apos(_ls, POSICAO4[_l['slug']], _l)
TEO.extend(T_NOVAS); TEO.extend(T_NOVAS2); assert all(t['f'] in FAMILIAS for t in TEO)
META.update(META_NOVAS5); REFORCO.update(REFORCO_NOVAS5)
META.update(META_NOVAS6); REFORCO.update(REFORCO_NOVAS6)
META.update(META_NOVAS7); REFORCO.update(REFORCO_NOVAS7)
for _ls, _novas in ((INICIANTE, NOVAS5_INICIANTE), (INTERMEDIARIO, NOVAS5_INTERMEDIARIO), (AVANCADO, NOVAS5_AVANCADO)):
    for _l in _novas: _apos(_ls, POSICAO5[_l['slug']], _l)
for _l in NOVAS6_INTERMEDIARIO: _apos(INTERMEDIARIO, POSICAO6[_l['slug']], _l)
for _l in NOVAS7_INTERMEDIARIO: _apos(INTERMEDIARIO, POSICAO7[_l['slug']], _l)
for _l in NOVAS7_AVANCADO: _apos(AVANCADO, POSICAO7[_l['slug']], _l)
FIL.extend(F_NOVOS); FIL.extend(F_NOVOS2); FIL.extend(F_NOVOS3); CORRENTES.extend(CORRENTES_NOVAS)
for _f in FIL: _f['corrente'] = MUDA_CORRENTE.get(_f['slug'], _f['corrente'])
assert all(_f['corrente'] in CORRENTES for _f in FIL), [_f['slug'] for _f in FIL if _f['corrente'] not in CORRENTES]
assert len({_f['slug'] for _f in FIL}) == len(FIL)

# ordem dos grupos em cada nível (ordenação estável mantém a sequência dentro do grupo)
for _n, _ls in (('iniciante', INICIANTE), ('intermediario', INTERMEDIARIO), ('avancado', AVANCADO)):
    _o = ORDEM_GRUPOS[_n]; assert all(_l['grupo'] in _o for _l in _ls), [_l['slug'] for _l in _ls if _l['grupo'] not in _o]
    _ls.sort(key=lambda l: _o.index(l['grupo']))
NIVEIS = [('iniciante', 'Iniciante', INICIANTE, 'Ética para iniciantes', 'O que é ética, as grandes famílias de teorias, quem conta e como discutir sem brigar.', 'v'),
          ('intermediario', 'Intermediário', INTERMEDIARIO, 'Ética intermediária', 'As teorias por dentro, a mente moral, a pobreza global e os dilemas clássicos.', ''),
          ('avancado', 'Avançado', AVANCADO, 'Ética avançada', 'Metaética, ética animal, as fronteiras do círculo moral e decidir sem certeza.', 'a')]
for slug, rot, ls, _, _, _ in NIVEIS:
    for i, l in enumerate(ls):
        assert l['slug'] in META, l['slug']; assert l['slug'] in REFORCO, l['slug']
        l.update(nivel=slug, nivel_rot=rot, i=i, temas=META[l['slug']][0], quiz=META[l['slug']][1])
        assert all(t in TEMAS for t in l['temas']), l['slug']
TODAS = INICIANTE + INTERMEDIARIO + AVANCADO
assert len({l['slug'] for l in TODAS}) == len(TODAS)
assert set(META) == {l['slug'] for l in TODAS}, set(META) ^ {l['slug'] for l in TODAS}
for l in TODAS:
    x = REFORCO[l['slug']]
    blocos = f'<div class="ajuda"><section class="analogia"><h3>Uma analogia</h3><p>{e(x["analogia"])}</p></section><section class="crianca"><h3>Explicando para uma criança</h3><p>{e(x["crianca"])}</p></section></div>'
    fim = l['corpo'].index('</p>') + 4
    l['corpo'] = l['corpo'][:fim] + blocos + l['corpo'][fim:]
TEO_S = {t['s']: t for t in TEO}; FIL_S = {f['slug']: f for f in FIL}; DIL_S = {d['s']: d for d in DILEMAS}
for t in TEO:
    for f in t['fil']: assert f in FIL_S, (t['s'], f)
for f in FIL:
    for t in f['teorias']: assert t in TEO_S, (f['slug'], t)
for d in DILEMAS:
    for t in d['teorias']: assert t[0] in TEO_S, (d['s'], t[0])
for v in BONDE:
    for t in v['teorias']: assert t[0] in TEO_S, (v['n'], t[0])

PAGINAS = []
SECOES = {'teorias': ('teorias.html', 'Teorias éticas', 'O que mais pesa para cada teoria, pontos fortes, objeções e referências.'), 'debates': ('debates.html', 'Debates', 'As perspectivas, por que é complexo e onde a razão pesa.'), 'dilemas': ('dilemas.html', 'Dilemas clássicos', 'O caso, a pergunta e o que cada teoria tende a dizer.'), 'filosofos': ('filosofos.html', 'Filósofos morais', 'Quem foi, o que defendeu e o que dizem os críticos.'), 'ferramentas': ('ferramentas.html', 'Ferramentas', 'Ferramenta interativa e gratuita, sem cadastro.')}
PAIS_NIVEL = {'iniciante.html': 'Iniciante', 'intermediario.html': 'Intermediário', 'avancado.html': 'Avançado'}
HUB_DE = {'teorias.html': 'Teorias éticas', 'criterios.html': 'Critérios éticos', 'metaetica.html': 'Metaética', 'debates.html': 'Debates'}
HUBS = {'catalogo.html', 'iniciante.html', 'intermediario.html', 'avancado.html', 'teorias.html', 'criterios.html', 'metaetica.html', 'debates.html', 'dilemas.html', 'filosofos.html', 'ferramentas.html', 'biblioteca.html', 'sites.html', 'glossario.html'}

def desc_seo(path, desc):
    d = re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', desc)).strip()
    if d and d[-1] not in '.!?…': d += '.'
    if len(d) < 70:
        sec = SECOES.get(path.split('/')[0]) if '/' in path else None
        d += ' ' + (sec[2] if sec else 'Explicação simples e com fontes, sem escolher time.')
    if len(d) > 160: d = d[:157].rsplit(' ', 1)[0].rstrip(' ,;:') + '…'
    return d

def dados(path, title, desc, url, atual, home):
    org = {'@type': 'Organization', 'name': 'BiblioVerse', 'url': 'https://biblioverse.org'}
    site = {'@type': 'WebSite', '@id': SITE + '/#site', 'name': NOME, 'url': SITE + '/', 'inLanguage': 'pt-BR', 'publisher': org}
    if home: return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': [site]}, ensure_ascii=False) + '</script>'
    pasta = path.split('/')[0] if '/' in path else ''
    pai = (atual, HUB_DE[atual]) if atual in HUB_DE else (SECOES[pasta][0], SECOES[pasta][1]) if pasta in SECOES else ((atual, PAIS_NIVEL[atual]) if atual in PAIS_NIVEL else None)
    trilha = [('Início', SITE + '/')] + ([(pai[1], f'{SITE}/{pai[0]}')] if pai else []) + [(title, url)]
    migalhas = {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(trilha)]}
    base = {'name': title, 'description': desc, 'url': url, 'inLanguage': 'pt-BR', 'isPartOf': {'@id': SITE + '/#site'}, 'dateModified': ATUALIZADO, 'image': SITE + '/assets/share.png'}
    if atual in PAIS_NIVEL or pasta in ('teorias', 'dilemas', 'debates'):
        pagina = {'@type': 'Article', 'headline': title[:110], 'datePublished': ATUALIZADO, 'author': {'@type': 'Organization', 'name': NOME, 'url': SITE + '/sobre.html'}, 'publisher': org, 'mainEntityOfPage': url, **base}
    elif pasta == 'filosofos':
        pagina = {'@type': 'WebPage', 'about': {'@type': 'Person', 'name': title}, **base}
    elif pasta == 'ferramentas':
        pagina = {'@type': 'WebApplication', 'applicationCategory': 'EducationalApplication', 'operatingSystem': 'Web', 'isAccessibleForFree': True, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'BRL'}, **base}
    elif path in HUBS:
        pagina = {'@type': 'CollectionPage', **base}
    else:
        pagina = {'@type': 'WebPage', **base}
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': [site, pagina, migalhas]}, ensure_ascii=False).replace('</', '<\\/') + '</script>'

def titulos_ok(corpo):
    """Título da analogia não é seção, e páginas de cards não saltam de h1 para h3."""
    corpo = re.sub(r'(<section class="(?:analogia|crianca)">)<h3>(.*?)</h3>', r'\1<p class="ti">\2</p>', corpo)
    m = re.search(r'</h1>.*?<h([2-6])[\s>]', corpo, re.S)
    fim = corpo.find('</section>', corpo.find('</h1>'))
    if m and m.group(1) == '3' and fim > 0:
        fim += len('</section>')
        return corpo[:fim] + '<h2 class="so-leitor">Nesta página</h2>' + corpo[fim:]
    return corpo

def page(path, title, desc, corpo, atual='', home=False):
    PAGINAS.append(path)
    erro = path == '404.html'
    desc = desc_seo(path, desc)
    corpo = titulos_ok(corpo)
    pre = '../' * path.count('/')
    url = SITE + '/' + ('' if path == 'index.html' else path)
    full = title if home else f'{title} | {NOME}'
    if len(full) > 60: full = title
    artigo = atual in PAIS_NIVEL or path.split('/')[0] in ('teorias', 'dilemas', 'debates')
    pre_tag = '<base href="/"/>\n' if erro else ''
    indexa = '<meta name="robots" content="noindex"/>\n' if erro else f'<link rel="canonical" href="{url}"/>\n' + dados(path, title, desc, url, atual, home) + '\n'
    l = lambda u, t: f'<a href="{pre}{u}">{e(t)}</a>'
    def grupo(nome, itens, cls=''):
        ativo = any(u == atual for u, _ in itens)
        links = ''.join(f'<a href="{pre}{u}"{" aria-current=page" if u == atual else ""}>{e(t)}</a>' for u, t in itens)
        gid = 'm-' + re.sub(r'[^a-z]', '', unicodedata.normalize('NFD', nome.lower()))
        return f'<div class="drop{" ativo" if ativo else ""}"><button type="button" aria-expanded="false" aria-controls="{gid}">{e(nome)} ▾</button><div class="mega{" " + cls if cls else ""}" id="{gid}" hidden>{links}</div></div>'
    menu = grupo('Aprender', [('comece-aqui.html', 'Comece aqui'), ('trilhas.html', 'Trilhas por tema')] + [(f'{s}.html', r) for s, r, *_ in NIVEIS] + [('catalogo.html', 'Todas as lições'), ('minha-posicao.html', 'Minha posição')])
    menu += grupo('Ideias', [('teorias.html', 'Teorias éticas'), ('criterios.html', 'Critérios éticos'), ('metaetica.html', 'Metaética'), ('dilemas.html', 'Dilemas clássicos'), ('debates.html', 'Debates'), ('filosofos.html', 'Filósofos morais'), ('glossario.html', 'Glossário')])
    menu += grupo('Ferramentas', [(f'ferramentas/{a}.html', b) for a, b, _, _ in FERR] + [('ferramentas.html', 'Todas as ferramentas')])
    menu += grupo('Biblioteca', [('biblioteca.html', 'Livros'), ('sites.html', 'Sites sobre ética')])
    menu += f'<a href="{pre}sobre.html"{" aria-current=page" if atual == "sobre.html" else ""}>Sobre</a>'
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
{pre_tag}<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}"/>
{indexa}<meta property="og:type" content="{'article' if artigo else 'website'}"/>
<meta property="og:site_name" content="{NOME}"/>
<meta property="og:title" content="{e(full)}"/>
<meta property="og:description" content="{e(desc)}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:locale" content="pt_BR"/>
<meta property="og:image" content="{SITE}/assets/share.png"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:alt" content="{NOME}"/>
{f'<meta property="article:modified_time" content="{ATUALIZADO}"/>' if artigo else ''}
<meta name="twitter:card" content="summary_large_image"/>
<meta name="theme-color" content="#1f5a4c"/>
<link rel="icon" href="{pre}favicon.ico" sizes="32x32"/>
<link rel="icon" href="{pre}assets/icon.svg" type="image/svg+xml"/>
<link rel="apple-touch-icon" href="{pre}assets/icon-180.png"/>
<link rel="manifest" href="{pre}manifest.webmanifest"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Fraunces:ital,opsz,wght,SOFT@0,9..144,400,100;0,9..144,600,100;0,9..144,700,100;1,9..144,500,100&display=swap"/>
<link rel="stylesheet" href="{pre}assets/style.min.css?v={VERSAO}"/>
<script src="https://biblioverse.org/superbar.js" async></script>
</head>
<body data-base="{pre}">
<nav id="bvbar" class="bvbar" data-current="eticaparainiciantes" data-offset="none" aria-label="BiblioVerse" style="position:relative;height:44px;background:linear-gradient(90deg,#4f7cff,#7a5cff)"><a href="https://biblioverse.org" style="color:#fff;line-height:44px;padding:0 14px;font-weight:700;text-decoration:none">BiblioVerse</a></nav>
<a class="skip" href="#main">Pular para o conteúdo</a>
<header class="topo"><div class="wrap topo-in">
<a class="marca" href="{pre}index.html">{arte.LOGO}<span>Ética<br/>Para Iniciantes</span></a>
<nav class="menu" aria-label="Principal">{menu}</nav>
<a class="btn cta-topo" href="{pre}comece-aqui.html">Comece aqui</a>
<button class="bbusca" type="button" aria-label="Buscar no site">🔍<span> Buscar</span> <kbd>Ctrl K</kbd></button>
<button class="hamb" type="button" aria-label="Abrir menu" aria-expanded="false">☰</button>
</div></header>
<div id="busca" hidden><div class="bcx" role="dialog" aria-label="Buscar no site"><input id="q" type="search" placeholder="Busque um tema, teoria ou filósofo" aria-label="Buscar no site" autocomplete="off"/><div class="res" id="res"></div></div></div>
<main id="main">{corpo}</main>
<footer class="rodape"><div class="wrap rodape-in">
<div><strong>{NOME}</strong><p>Explicações objetivas e simples sobre ética, do básico ao avançado. Com fontes e aberto a correções.</p><p>Parte da <a href="https://biblioverse.org">BiblioVerse</a>.</p><p class="copy">© {ATUALIZADO[:4]} BiblioVerse. Atualizado em {ATUALIZADO[8:10]}/{ATUALIZADO[5:7]}/{ATUALIZADO[:4]}.</p></div>
<div><p class="ti">Aprender</p><ul><li>{l('comece-aqui.html', 'Comece aqui')}</li><li>{l('iniciante.html', 'Iniciante')}</li><li>{l('intermediario.html', 'Intermediário')}</li><li>{l('avancado.html', 'Avançado')}</li><li>{l('trilhas.html', 'Trilhas por tema')}</li><li>{l('catalogo.html', 'Todas as lições')}</li><li>{l('minha-posicao.html', 'Minha posição')}</li></ul></div>
<div><p class="ti">Ideias</p><ul><li>{l('teorias.html', 'Teorias éticas')}</li><li>{l('criterios.html', 'Critérios éticos')}</li><li>{l('metaetica.html', 'Metaética')}</li><li>{l('dilemas.html', 'Dilemas clássicos')}</li><li>{l('debates.html', 'Debates')}</li><li>{l('filosofos.html', 'Filósofos morais')}</li><li>{l('glossario.html', 'Glossário')}</li><li><a href="https://ethicstest.biblioverse.org/" {EXT}>Teste de Visão Moral</a></li></ul></div>
<div><p class="ti">Mais</p><ul><li>{l('ferramentas.html', 'Ferramentas')}</li><li>{l('biblioteca.html', 'Biblioteca')}</li><li>{l('sites.html', 'Sites sobre ética')}</li><li><a href="https://politicaparainiciantes.biblioverse.org/" {EXT}>Política Para Iniciantes</a></li><li>{l('sobre.html', 'Sobre')}</li><li>{l('privacidade.html', 'Política de privacidade')}</li></ul></div>
</div></footer>
<noscript><p class="nojs">A leitura funciona sem JavaScript. A busca, os menus suspensos, os testes e as ferramentas interativas precisam dele; o rodapé tem links para todas as seções.</p></noscript>
<script src="{pre}assets/app.min.js?v={VERSAO}" defer></script>
</body></html>
'''
    html = html.replace('href="index.html"', 'href="./"').replace('href="../index.html"', 'href="../"')
    full_path = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    open(full_path, 'w', encoding='utf-8', newline='\n').write(html)

def cabeca(kicker, titulo, lede='', meta=''):
    return f'<section class="cabeca"><div class="wrap"><p class="trilha">{kicker}</p><h1>{e(titulo)}</h1>' + (f'<p class="lede">{lede}</p>' if lede else '') + meta + '</div></section>'
def fontes(ls):
    return '<aside class="fontes"><h2>Fontes e leituras</h2><ul>' + ''.join(f'<li><a href="{e(u)}" {EXT}>{e(t)}</a></li>' for t, u in ls) + '</ul></aside>'
def tabelas(h): return h.replace('<table>', '<div class="tabela"><table>').replace('</table>', '</table></div>')
def tempo_leitura(h): return max(2, round(len(re.sub('<[^>]+>', ' ', h).split()) / 190))
def cartao_licao(l, pre=''):
    tg = ''.join(f'<span class="tag">{e(TEMAS[t])}</span>' for t in l['temas'])
    return f'<a class="cartao" data-licao="{l["slug"]}" data-temas="{" ".join(l["temas"])}" data-nivel="{l["nivel"]}" href="{pre}{l["slug"]}.html"><span class="linha-cartao"><span class="tipo {l["nivel"]}">{e(l["nivel_rot"])}</span></span><h3>{e(l["titulo"])}</h3><p>{e(l["resumo"])}</p><span class="tags" style="margin-top:auto;padding-top:6px">{tg}</span></a>'
def cartao_ferr(a, b, c, n, pre=''): return f'<a class="cartao" data-temas="ferramenta" data-nivel="ferr" href="{pre}ferramentas/{a}.html">{arte.icone(n)}<h3>{e(b)}</h3><p>{e(c)}</p></a>'
def relacionados(l):
    alvos = [x for x in TODAS if x['slug'] != l['slug'] and set(x['temas']) & set(l['temas'])]
    alvos.sort(key=lambda x: (x['nivel'] != l['nivel'], -len(set(x['temas']) & set(l['temas']))))
    return f'<section class="relac"><div class="wrap"><h2>Continue</h2><div class="grade">{"".join(cartao_licao(x) for x in alvos[:3])}</div></div></section>'
def bloco_quiz(q, rot='Teste rápido'):
    return f'<div class="quiz" data-quiz="{e(json.dumps(q, ensure_ascii=False))}"><p class="k">{e(rot)}</p><div class="alvo"></div></div>'
COR_FAM = {f: i for i, f in enumerate(FAMILIAS)}
FAM_TEO = FAMILIAS[:4]; FAM_CRI = FAMILIAS[4:6]; FAM_MET = FAMILIAS[6:]
HUB_FAM = {**{f: 'teorias.html' for f in FAM_TEO}, **{f: 'criterios.html' for f in FAM_CRI}, **{f: 'metaetica.html' for f in FAM_MET}}
COR_COR = {c: i for i, c in enumerate(CORRENTES)}
def cartao_t(t, pre=''): return f'<a class="cartao item" data-f="{e(t["f"])}" href="{pre}{t["s"]}.html"><span class="tipo fam f{COR_FAM[t["f"]]}">{e(t["f"])}</span><h3>{e(t["n"])}</h3><p>{e(t["r"])}</p></a>'
def cartao_d(d, pre=''): return f'<a class="cartao item" data-t="{e(d["t"])}" href="{pre}{d["s"]}.html"><span class="tipo ferr">{e(d["t"])}</span><h3>{e(d["n"])}</h3><p>{e(d["r"])}</p></a>'
def cartao_f(f, pre=''): return f'<a class="cartao item" data-c="{e(f["corrente"])}" href="{pre}{f["slug"]}.html"><span class="linha-cartao"><span class="tipo fam f{COR_COR[f["corrente"]]}">{e(f["corrente"])}</span><span class="tipo">{e(f["anos"])}</span></span><h3>{e(f["nome"])}</h3><p>{e(f["quem"])}</p></a>'
def tlink(s, pre='', cls=''): return f'<a href="{pre}teorias/{s}.html" class="{cls}">{e(TEO_S[s]["n"])}</a>'

# ---------- início ----------
def inicio():
    niv = ''.join(f'<div><h2><span class="grad {g}">{e(r)}</span></h2><p>{e(d)}</p><a class="btn {g}" href="{s}.html">Começar</a><small>{len(ls)} lições</small></div>' for s, r, ls, _, d, g in NIVEIS)
    temas = ''.join(f'<a href="catalogo.html?tema={k}">{e(v)}</a>' for k, v in TEMAS.items())
    secoes = ''.join(f'<a class="cartao" href="{u}">{arte.icone(i)}<h3>{e(t)}</h3><p>{e(d)}</p></a>' for u, i, t, d in [
        ('catalogo.html', 'ficha', 'Aprenda', f'{len(TODAS)} lições em três níveis, com busca por tema.'),
        ('trilhas.html', 'rede', 'Trilhas por tema', f'{len(TRILHAS)} caminhos curtos: duas horas, ética animal, discutir, mente moral, política, metaética e futuro.'),
        ('minha-posicao.html', 'ponto', 'Minha posição', 'Monte sua visão moral em cinco escolhas e veja o que ela implica.'),
        ('teorias.html', 'arvore', 'Teorias éticas', f'{sum(1 for t in TEO if t["f"] in FAM_TEO)} teorias normativas: o que pesa mais para cada uma, forças e objeções.'),
        ('criterios.html', 'circulo', 'Critérios éticos', f'{sum(1 for t in TEO if t["f"] in FAM_CRI)} posições sobre quem conta, e sobre egoísmo, relativismo e ceticismo.'),
        ('metaetica.html', 'lampada', 'Metaética', f'{sum(1 for t in TEO if t["f"] in FAM_MET)} posições sobre o que é um juízo moral.'),
        ('debates.html', 'valor', 'Debates', f'{len(DEBATES)} debates: as perspectivas e onde a razão pesa.'),
        ('dilemas.html', 'bonde', 'Dilemas clássicos', f'{len(DILEMAS)} experimentos mentais e o que cada teoria diz sobre eles.'),
        ('filosofos.html', 'pessoa', 'Filósofos morais', f'{len(FIL)} pensadores, de Platão a Singer: ideias, obras e críticas.'),
        ('ferramentas.html', 'compara', 'Ferramentas', f'{len(FERR)} jogos e simuladores para aprender fazendo.'),
        ('glossario.html', 'livro', 'Glossário', f'{len(GLOSSARIO)} termos explicados em uma frase.'),
        ('biblioteca.html', 'livro', 'Biblioteca', f'{len(LIVROS)} livros por nível e {len(SITES)} sites para ir além.'),
        ('https://ethicstest.biblioverse.org/', 'circulo', 'Teste de Visão Moral', 'Descubra sua teoria, seu círculo moral e sua metaética.'),
    ])
    corpo = f'''<section class="capa"><div class="wrap capa-in"><div><h1>Entenda a <span class="grifo">ética</span>, do <span class="grifo v">básico</span> ao <span class="grifo a">avançado</span>, e decida por conta própria.</h1><p class="lede">Explicações objetivas e simples, com fontes, em três níveis. Das grandes teorias ao círculo moral, da metaética à ética animal.</p><div class="cta"><a class="btn" href="comece-aqui.html">Comece aqui</a><a class="btn alt" href="teorias.html">Mapa das teorias</a></div></div>{arte.hero()}</div></section>
<section class="noite"><div class="wrap niveis">{niv}</div></section>
<section class="secao areia"><div class="wrap"><div class="sec-cab"><h2>Explore o site</h2><p>Escolha por onde quer ir.</p></div><div class="grade">{secoes}</div></div></section>
<section class="secao"><div class="wrap numeros"><div><b class="grad">{len(TODAS)}</b><span>lições em três níveis</span></div><div><b class="grad v">{len(TEO)}</b><span>teorias e posições</span></div><div><b class="grad a">{len(DILEMAS) + len(DEBATES)}</b><span>dilemas e debates</span></div><div><b class="grad">{len(FIL)}</b><span>filósofos e pensadores</span></div></div></section>
<section class="secao areia"><div class="wrap capa-in" style="padding-block:0"><div><h2>Resultado, regra ou caráter?</h2><p style="font-size:1.1rem">As teorias éticas se distinguem pelo que colocam no centro, não pelo que ignoram. Veja o ponto focal de cada uma, as variantes e as objeções.</p><a class="btn" href="teorias.html">Explorar as teorias</a></div><div class="temas">{"".join(f'<a href="teorias/{s}.html">{e(TEO_S[s]["n"])}</a>' for s in ['utilitarismo-classico', 'deontologia-kantiana', 'etica-das-virtudes', 'etica-do-cuidado', 'contratualismo-rawlsiano', 'sencientismo'])}</div></div></section>
<section class="secao"><div class="wrap"><div class="sec-cab"><h2>O que você quer entender?</h2></div><div class="temas">{temas}</div></div></section>'''
    page('index.html', 'Ética Para Iniciantes: do básico ao avançado', 'Guia de ética em três níveis: teorias normativas, círculo moral, metaética, ética animal, dilemas e filósofos, com fontes.', corpo, home=True)

def comece():
    _p1 = ['o-que-e-etica', 'fatos-e-valores', 'mapa-das-teorias', 'consequencialismo', 'deontologia', 'etica-do-carater', 'circulo-moral', 'imparcialidade']
    p1 = sorted((l for l in INICIANTE if l['slug'] in _p1), key=lambda l: _p1.index(l['slug']))
    corpo = cabeca('Comece aqui', 'Novo em ética? Comece por aqui', 'Um caminho curto para ter o básico em cerca de uma hora. Depois, siga pelo tema que mais te interessar.')
    corpo += f'''<div class="wrap secao"><h2>1. Entenda o básico</h2><p>Oito lições curtas, nesta ordem: o que é ética, fatos e valores, as três grandes famílias de teorias e quem conta.</p><div class="grade">{"".join(cartao_licao(l) for l in p1)}</div>
<h2 style="margin-top:2.4rem">2. Descubra o que você pensa</h2><div class="grade"><a class="cartao" href="https://ethicstest.biblioverse.org/" {EXT}>{arte.icone("circulo")}<h3 class="ext">Teste de Visão Moral</h3><p>Sua teoria normativa, seu círculo moral, sua metaética e sua abertura.</p></a>{cartao_ferr(*FERR[3])}{cartao_ferr(*FERR[0])}</div>
<h2 style="margin-top:2.4rem">3. Teste as teorias nos dilemas</h2><div class="grade">{cartao_ferr(*FERR[2])}<a class="cartao" href="dilemas.html">{arte.icone("bonde")}<h3>Dilemas clássicos</h3><p>{len(DILEMAS)} casos e o que cada teoria diz.</p></a>{cartao_ferr(*FERR[4])}</div>
<h2 style="margin-top:2.4rem">4. Vá mais fundo</h2><div class="grade"><a class="cartao" href="teorias.html">{arte.icone("arvore")}<h3>Todas as teorias</h3><p>{len(TEO)} teorias e posições, com forças e objeções.</p></a><a class="cartao" href="filosofos.html">{arte.icone("pessoa")}<h3>Filósofos morais</h3><p>{len(FIL)} pensadores, com ideias e críticas.</p></a><a class="cartao" href="biblioteca.html">{arte.icone("livro")}<h3>Biblioteca</h3><p>Livros por nível e sites para continuar.</p></a></div></div>'''
    page('comece-aqui.html', 'Comece aqui', 'Um caminho curto para entender o básico de ética em cerca de uma hora.', corpo, atual='comece-aqui.html')

def catalogo():
    bt = lambda k, v, t: f'<button type="button" data-k="{k}" data-v="{v}" aria-pressed="false">{e(t)}</button>'
    filt = '<div class="filtros" role="group" aria-label="Nível">' + bt('nivel', '', 'Todos os níveis') + ''.join(bt('nivel', s, r) for s, r, *_ in NIVEIS) + bt('nivel', 'ferr', 'Ferramentas') + '</div><div class="filtros" role="group" aria-label="Tema">' + bt('tema', '', 'Todos os temas') + ''.join(bt('tema', k, v) for k, v in TEMAS.items()) + '</div>'
    itens = ''.join(cartao_licao(l) for l in TODAS) + ''.join(cartao_ferr(*f) for f in FERR)
    corpo = cabeca('Lições', 'Todas as lições', 'Filtre por nível ou por tema.') + f'<div class="wrap secao"><input class="fq" id="fq" type="search" placeholder="Filtrar por palavra" aria-label="Filtrar"/>{filt}<p class="contagem" id="contagem" role="status"></p><div class="grade" id="catalogo">{itens}</div></div>'
    page('catalogo.html', 'Todas as lições', 'Todas as lições e ferramentas de ética, com filtros por nível e tema.', corpo, atual='catalogo.html')

# ---------- níveis e lições ----------

# ---------- camada didática ----------
GL_STOP = {'Ética', 'Moral', 'Agregação', 'Universalidade', 'Consideração direta e indireta', 'Ética aplicada', 'Ética normativa', 'Ética descritiva', 'Fato e valor', 'Dever prima facie'}
GL_TERMS = sorted(((re.sub(r'\s*\(.*?\)', '', t).strip(), d) for _, t, d, _ in GLOSSARIO if len(t) >= 6 and t not in GL_STOP), key=lambda x: -len(x[0]))
GL_SKIP = {'a', 'h1', 'h2', 'h3', 'h4', 'summary', 'th', 'button', 'script', 'style', 'code'}
def glossa(h, titulo, maximo=6):
    partes = re.split(r'(<[^>]+>)', h); pilha = 0; usados = set(); n = 0; tl = titulo.lower()
    for i, p in enumerate(partes):
        if not p: continue
        if p.startswith('<'):
            m = re.match(r'</?([a-zA-Z0-9]+)', p); nome = m.group(1).lower() if m else ''
            if nome in GL_SKIP and not p.endswith('/>'): pilha = max(0, pilha - 1) if p.startswith('</') else pilha + 1
            continue
        if pilha or n >= maximo: continue
        off = 0; novo = ''
        for termo, d in GL_TERMS:
            if n >= maximo: break
            if termo in usados or termo.lower() in tl: continue
            m = re.search(r'(?<![\w-])' + re.escape(termo) + r'(?![\w-])', p[off:], flags=re.I)
            if not m: continue
            s, f = m.start() + off, m.end() + off
            novo += p[off:s] + f'<span class="gl" tabindex="0" data-def="{e(d)}">{p[s:f]}</span>'; off = f; usados.add(termo); n += 1
        partes[i] = novo + p[off:]
    return ''.join(partes)
def lista_mais(rotulo, links, pre='', n=6):
    if not links: return ''
    saida = f'<div class="lista-mais"><strong>{rotulo}:</strong> ' + ', '.join(links[:n])
    if len(links) > n: saida += f' <details class="mais"><summary>e mais {len(links) - n}</summary><span>' + ', '.join(links[n:]) + '</span></details>'
    return saida + '.</div>'
def bloco_didatico(l):
    d = DID[l['slug']]
    pre = ', '.join(f'<a href="{p}.html">{e(next(x["titulo"] for x in TODAS if x["slug"] == p))}</a>' for p in d['pre'])
    pre = f'<p class="pre">Ajuda ter lido: {pre}.</p>' if pre else ''
    obj = '<div class="objetivos"><p class="k">Ao fim desta lição, você vai conseguir</p><ul>' + ''.join(f'<li>{e(o)}</li>' for o in d['obj']) + '</ul>' + pre + '</div>'
    caso = f'<div class="caso-abre"><p class="k">Antes de ler: o que você faria?</p><p>{e(d["caso"][0])}</p><p class="q">{e(d["caso"][1])}</p><details><summary>Ver o que a lição responde</summary><p>{e(d["caso"][2])}</p></details></div>'
    return obj + caso
def erro_pratica(l):
    d = DID[l['slug']]
    out = f'<div class="nota erro-comum"><strong>Erro comum:</strong> <em>{e(d["erro"][0])}</em> {e(d["erro"][1])}</div>'
    if d['ferr']:
        f = next(x for x in FERR if x[0] == d['ferr'])
        out += f'<div class="nota"><strong>Pratique:</strong> <a href="ferramentas/{f[0]}.html">{e(f[1])}</a>. {e(f[2])}</div>'
    return out
def quizzes(l):
    d = DID[l['slug']]
    return bloco_quiz(l['quiz'], 'Teste rápido · 1 de 3') + bloco_quiz(d['quiz'][0], 'Aplique · 2 de 3') + bloco_quiz(d['quiz'][1], 'Confira · 3 de 3')
def casos_fio(nivel):
    cab = '<tr><th>Família</th>' + ''.join(f'<th>{e(n)}</th>' for _, n, _ in CASOS_FIO) + '</tr>'
    linhas = ''.join(f'<tr><th>{e(f)}</th><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td></tr>' for f, a, b, c in RESPOSTAS_FIO[nivel])
    desc = ''.join(f'<li><strong>{e(n)}.</strong> {e(d)}</li>' for _, n, d in CASOS_FIO)
    return f'<section class="casos-fio"><h2 class="grupo">Os três casos do curso</h2><p>Três casos atravessam os três níveis. A cada nível, veja como cada família responde a eles, com mais detalhe do que no nível anterior.</p><ul class="casos-lista">{desc}</ul><div class="tabela"><table class="compara"><thead>{cab}</thead><tbody>{linhas}</tbody></table></div></section>'
def trilhas():
    secs = ''
    for t in TRILHAS:
        ls = [next(l for l in TODAS if l['slug'] == s) for s in t['licoes']]
        prog = f'<div class="barra-prog" id="pg-{t["s"]}" data-prog="{",".join(t["licoes"])}" style="max-width:420px"><i></i></div><small data-prog-t="pg-{t["s"]}"></small>'
        cards = ''.join(f'<div class="trilha-item"><span class="trilha-n">{i + 1}</span>{cartao_licao(l)}</div>' for i, l in enumerate(ls))
        secs += f'<section class="trilha-sec" id="{t["s"]}"><h2 class="grupo">{e(t["n"])} <small>{e(t["tempo"])} · {len(ls)} lições</small></h2><p>{e(t["d"])}</p>{prog}<div class="grade trilha-grade">{cards}</div></section>'
    corpo = cabeca('Aprender', 'Trilhas de estudo', 'Sete caminhos curtos por tema. Cada um tem entre 8 e 10 lições, na ordem em que valem ser lidas, e guarda seu progresso.')
    corpo += f'<div class="wrap secao" style="padding-top:18px"><div class="nota" style="margin-top:0"><strong>Como usar:</strong> escolha a trilha que responde à sua pergunta de agora e siga a ordem. As trilhas se cruzam; uma lição lida conta em todas. Para o curso completo, siga os três níveis: <a href="iniciante.html">Iniciante</a>, <a href="intermediario.html">Intermediário</a> e <a href="avancado.html">Avançado</a>.</div>{secs}</div>'
    page('trilhas.html', 'Trilhas de estudo', 'Sete trilhas curtas de ética por tema: duas horas, ética animal, discutir, mente moral, política, metaética e futuro.', corpo, atual='trilhas.html')
def teste_nivel(slug, rot, ls):
    itens = []
    for l in ls:
        d = DID[l['slug']]
        for q in [l['quiz']] + d['quiz']:
            itens.append([q[0], q[1], q[2], q[3] + f' (Lição: {l["titulo"]}.)'])
    dados = json.dumps(dict(itens=itens, n=10), ensure_ascii=False).replace('</', '<\\/')
    corpo = cabeca(f'<a href="{slug}.html">{e(rot)}</a>', f'Teste do nível {rot}', f'Dez perguntas sorteadas entre as {len(itens)} do nível. Cada resposta diz em que lição rever o assunto. Refaça quantas vezes quiser: as perguntas mudam.')
    corpo += f'<div class="wrap estreito secao"><div id="jogo" class="quiz" style="margin-top:0"><div class="placar"><span></span><span></span></div><div class="barra-prog"><i></i></div><div class="alvo" style="margin-top:14px"></div><button class="btn prox-q" type="button" style="margin-top:12px" hidden>Próxima</button></div><script type="application/json" id="dados-teste">{dados}</script><p class="legenda">Acertou 8 ou mais? Você está pronto para o próximo nível. Menos que isso: veja as lições indicadas e tente de novo.</p><p><a class="btn alt" href="{slug}.html">Voltar ao nível {e(rot)}</a></p></div>'
    page(f'teste-{slug}.html', f'Teste do nível {rot}', f'Dez perguntas sorteadas sobre as lições do nível {rot} de ética, com a lição a rever em cada resposta.', corpo, atual=f'{slug}.html')
def minha_posicao():
    teo = [dict(s=t['s'], n=t['n'], f=t['f'], foco=t['foco']) for t in TEO]
    deb = {}
    for d in DEBATES:
        for s, _, _ in d['teorias']:
            deb.setdefault(s, [])
            if len(deb[s]) < 4: deb[s].append([d['s'], d['n']])
    dados = json.dumps(dict(teo=teo, fam=dict(teo=FAM_TEO, cri=FAM_CRI, met=FAM_MET), deb=deb), ensure_ascii=False).replace('</', '<\\/')
    campo = lambda i, rot: f'<label class="campo">{rot}<select id="{i}"></select></label>'
    corpo = cabeca('Aprender', 'Minha posição', 'Monte a sua visão moral em cinco escolhas e veja o que ela implica, com os debates que a testam. Fica salvo no seu navegador.')
    corpo += f'''<div class="wrap estreito secao"><div id="minha-posicao" class="quiz" style="margin-top:0"><div class="grade" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">{campo('mp-teoria', 'Como agir: a teoria normativa')}{campo('mp-circulo', 'Quem conta: o círculo moral')}{campo('mp-padrao', 'Há um padrão comum?')}{campo('mp-meta', 'O que é um juízo moral')}{campo('mp-abertura', 'Diante de um bom argumento contrário, eu…')}</div><div id="mp-saida" style="margin-top:18px"></div></div><script type="application/json" id="dados-mp">{dados}</script><div class="nota"><strong>Compare:</strong> o <a href="https://ethicstest.biblioverse.org/" {EXT}>Teste de Visão Moral</a> mede as mesmas cinco dimensões a partir das suas respostas a casos, não do que você declara. Faça os dois e veja se batem; a diferença é onde vale pensar.</div></div>'''
    page('minha-posicao.html', 'Minha posição', 'Monte sua visão moral em cinco escolhas (teoria, círculo, padrão, metaética, abertura) e veja o que ela implica.', corpo, atual='minha-posicao.html')


def fecho(l):
    f = FECHO[l['slug']]
    return f'<section class="fecho"><h2>Para guardar</h2><ul>{"".join(f"<li>{e(g)}</li>" for g in f["guardar"])}</ul><div class="pensar"><p class="k">Para pensar</p><p>{e(f["pensar"])}</p></div></section>'
def revisao(slug, rot, ls):
    grupos = {}
    for l in ls: grupos.setdefault(l['grupo'], []).append(l)
    cont = f'<div class="nota placar" id="placar-rev" data-total="{len(ls)}" role="status">Responda às perguntas para ver seu placar. Cada uma pede que você aplique a lição a um caso: se errar, o link leva de volta a ela.</div>'
    for gr, its in grupos.items():
        cont += f'<h2 class="grupo">{e(gr)}</h2>'
        for l in its: cont += f'<div class="rev-item"><h3><a href="{l["slug"]}.html">Lição {l["i"] + 1}: {e(l["titulo"])}</a></h3>{bloco_quiz(DID[l["slug"]]["quiz"][0], "Aplique")}</div>'
    ordem = [n[0] for n in NIVEIS]
    if slug != ordem[-1]:
        seg = NIVEIS[ordem.index(slug) + 1]
        cont += f'<div class="fim-nivel"><p class="ti">Pronto para o próximo nível?</p><p>Continue com {len(seg[2])} lições do nível {e(seg[1])}.</p><a class="btn {seg[5]}" href="{seg[0]}.html">Ir para o curso {e(seg[1])} →</a></div>'
    else:
        cont += f'<div class="fim-nivel"><p class="ti">Você concluiu o curso</p><p>Monte a sua posição e siga pelos debates e pelas teorias.</p><a class="btn a" href="minha-posicao.html">Minha posição</a> <a class="btn alt" href="debates.html">Debates</a></div>'
    page(f'revisao-{slug}.html', f'Revisão do nível {rot}', f'{len(ls)} perguntas de aplicação, uma por lição do nível {rot}, com placar e link de volta para cada lição.', cabeca(f'<a href="{slug}.html">{e(rot)}</a> / Revisão', f'Revisão do nível {rot}', f'Uma pergunta de aplicação por lição. Responda, veja o placar e volte às lições em que errou.') + f'<div class="wrap secao revisao-pag">{cont}</div>', atual=f'{slug}.html')

def nivel(slug, rot, ls, titulo, desc, g):
    grupos = {}
    for l in ls: grupos.setdefault(l['grupo'], []).append(l)
    cont = ''
    for gr, its in grupos.items():
        cont += f'<h2 class="grupo">{e(gr)}</h2><div class="grade">{"".join(cartao_licao(l) for l in its)}</div>'
    if slug == 'iniciante': cont += f'<h2 class="grupo">Experimente</h2><div class="grade">{cartao_ferr(*FERR[1])}{cartao_ferr(*FERR[0])}<a class="cartao" href="https://ethicstest.biblioverse.org/" {EXT}>{arte.icone("circulo")}<h3 class="ext">Teste de Visão Moral</h3><p>Descubra de onde você parte.</p></a></div>'
    if slug == 'intermediario': cont += f'<h2 class="grupo">Experimente</h2><div class="grade">{cartao_ferr(*FERR[2])}{cartao_ferr(*FERR[4])}<a class="cartao" href="dilemas.html">{arte.icone("bonde")}<h3>Todos os dilemas</h3><p>{len(DILEMAS)} casos clássicos.</p></a></div>'
    if slug == 'avancado': cont += f'<h2 class="grupo">Experimente</h2><div class="grade">{cartao_ferr(*FERR[3])}<a class="cartao" href="teorias.html">{arte.icone("arvore")}<h3>Compare teorias</h3><p>Três teorias lado a lado.</p></a><a class="cartao" href="https://politicaparainiciantes.biblioverse.org/" {EXT}>{arte.icone("rede")}<h3 class="ext">Política Para Iniciantes</h3><p>A continuação, do lado da política.</p></a></div>'
    tot = sum(tempo_leitura(l['corpo']) for l in ls); h = round(tot / 60)
    dur = f'cerca de {h} hora{"s" if h > 1 else ""} de leitura' if h >= 1 else f'cerca de {tot} minutos de leitura'
    como = f'<div class="como-estudar"><h2>Como estudar este nível</h2><p>{len(ls)} lições em {len(grupos)} blocos, {dur}, em sessões de 10 a 15 minutos.</p><ol><li><strong>Siga a ordem dos blocos.</strong> Cada lição começa dizendo o que você vai aprender e o que ajuda ter lido antes.</li><li><strong>Responda ao caso de abertura antes de ler:</strong> prever e depois conferir é o que mais fixa.</li><li><strong>Não pule o fim da lição:</strong> os pontos para guardar, a pergunta para pensar, o erro comum e os três testes.</li><li><strong>Marque como lida</strong> para acompanhar o progresso e receber lições para revisar.</li><li><strong>Feche com a <a href="revisao-{slug}.html">revisão do nível</a></strong> (uma pergunta por lição, com placar) e o <a href="teste-{slug}.html">teste do nível</a> (dez sorteadas). Para estudar por tema, use as <a href="trilhas.html">trilhas</a>.</li></ol></div>'
    cont = como + f'<div class="nivel-acoes"><a class="btn alt" href="revisao-{slug}.html">Revisão: {len(ls)} perguntas</a> <a class="btn alt" href="teste-{slug}.html">Teste do nível: 10 sorteadas</a> <a class="btn alt" href="trilhas.html">Trilhas por tema</a></div><section class="revisao" hidden><h2 class="grupo">Revise o que leu há mais tempo</h2><p>A memória precisa de revisão espaçada. Estas são as lições deste nível que você marcou como lidas há mais tempo.</p><div class="grade" id="rev-grade"></div></section>' + cont + casos_fio(slug)
    prog = f'<div class="barra-prog" id="pg-{slug}" data-prog="{",".join(l["slug"] for l in ls)}" style="max-width:420px;background:#ffffff33"><i></i></div><small data-prog-t="pg-{slug}" style="color:#fff"></small>'
    page(f'{slug}.html', titulo, desc, cabeca(f'Nível {rot}', titulo, e(desc), meta=f'<div style="margin-top:1.1rem">{prog}</div>') + f'<div class="wrap secao" style="padding-top:18px">{cont}</div>', atual=f'{slug}.html')

def indice(l, ls):
    i = l['i']; n = len(ls)
    def seta(alvo, rel, sim, rot):
        if alvo: return f'<a class="indice-seta" rel="{rel}" href="{alvo["slug"]}.html" aria-label="{rot}: {e(alvo["titulo"])}" title="{rot}: {e(alvo["titulo"])}">{sim}</a>'
        return f'<span class="indice-seta off" aria-hidden="true">{sim}</span>'
    pontos = ''
    for j, x in enumerate(ls):
        rot = f'Lição {j + 1}: {e(x["titulo"])}'
        atual = ' aria-current="page"' if j == i else ''
        pontos += f'<li><a href="{x["slug"]}.html" data-ponto="{x["slug"]}" title="{rot}" aria-label="{rot}"{atual}></a></li>'
    return f'<nav class="indice {l["nivel"]}" aria-label="Lições do nível {e(l["nivel_rot"])}"><div class="wrap"><p class="indice-pos"><a href="{l["nivel"]}.html">{e(l["nivel_rot"])}</a> · Lição {i + 1} de {n}</p><div class="indice-nav">{seta(ls[i - 1] if i else None, "prev", "←", "Lição anterior")}<ol>{pontos}</ol>{seta(ls[i + 1] if i + 1 < n else None, "next", "→", "Próxima lição")}</div></div></nav>'

# dilemas e teorias ligados a cada lição, para o bloco "Veja também"
LICAO_LIGA = {
 'mapa-das-teorias': (['utilitarismo-classico', 'deontologia-kantiana', 'etica-das-virtudes'], ['bonde-desvio']), 'consequencialismo': (['consequencialismo-de-ato', 'utilitarismo-classico', 'prioritarismo'], ['transplante', 'crianca-no-lago']),
 'deontologia': (['deontologia-kantiana', 'deontologia-de-direitos', 'deontologia-de-limiar'], ['mentir-ao-assassino', 'bonde-passarela']), 'etica-do-carater': (['etica-das-virtudes', 'etica-do-cuidado', 'estoicismo'], ['anel-de-giges', 'jim-e-os-indigenas']),
 'egoismo-relativismo-e-ceticismo': (['egoismo-etico', 'relativismo-cultural', 'subjetivismo', 'ceticismo-normativo'], ['anel-de-giges']), 'circulo-moral': (['antropocentrismo', 'sencientismo', 'biocentrismo', 'ecocentrismo'], ['casos-marginais', 'ultimo-homem']),
 'imparcialidade': (['contratualismo-rawlsiano', 'contratualismo-estendido', 'prescritivismo'], ['veu-da-ignorancia']), 'expansao-do-circulo-moral': (['sencientismo'], ['casos-marginais']), 'dilemas-do-cotidiano': ([], ['crianca-no-lago']),
 'utilitarismo-classico': (['utilitarismo-classico', 'consequencialismo-de-ato', 'consequencialismo-de-regras', 'utilitarismo-de-preferencias'], ['maquina-de-experiencias', 'omelas']), 'somar-priorizar-ou-garantir': (['prioritarismo', 'maximin', 'igualitarismo', 'suficientismo', 'utilitarismo-medio'], ['monstro-utilitario']),
 'o-peso-do-sofrimento': (['prioridade-ao-sofrimento', 'utilitarismo-negativo', 'etica-focada-no-sofrimento'], ['omelas']), 'objecoes-ao-consequencialismo': (['utilitarismo-classico', 'prioritarismo'], ['transplante', 'monstro-utilitario', 'conclusao-repugnante', 'jim-e-os-indigenas']),
 'kant-e-o-imperativo-categorico': (['deontologia-kantiana'], ['mentir-ao-assassino', 'bonde-passarela']), 'direitos-e-limiares': (['deontologia-de-direitos', 'deontologia-absolutista', 'deontologia-de-limiar'], ['transplante']), 'intencao-e-previsao': (['doutrina-do-duplo-efeito', 'deontologia-pluralista'], ['bonde-desvio', 'bonde-passarela']),
 'etica-e-religiao': (['teoria-do-mandamento-divino'], []), 'aristoteles-e-as-virtudes': (['etica-das-virtudes', 'estoicismo'], ['anel-de-giges']), 'etica-do-cuidado': (['etica-do-cuidado'], ['dilema-de-heinz']), 'contratualismo': (['contratualismo-hobbesiano', 'contratualismo-rawlsiano', 'contratualismo-escanloniano', 'contratualismo-estendido'], ['veu-da-ignorancia']),
 'psicologia-moral': ([], ['bonde-passarela']), 'vieses-morais': ([], ['crianca-no-lago']), 'tribalismo-moral': (['egoismo-etico', 'antropocentrismo'], ['crianca-no-lago']), 'senciencia': (['sencientismo'], ['casos-marginais']), 'especismo': (['sencientismo', 'antropocentrismo', 'deontologia-de-direitos'], ['casos-marginais', 'veu-da-ignorancia']),
 'etica-animal-na-pratica': (['sencientismo', 'etica-das-virtudes'], ['casos-marginais']), 'o-dilema-do-bonde': (['doutrina-do-duplo-efeito', 'consequencialismo-de-ato', 'deontologia-kantiana'], ['bonde-desvio', 'bonde-passarela', 'transplante']), 'experimentos-mentais': ([], ['maquina-de-experiencias', 'crianca-no-lago', 'violinista', 'anel-de-giges', 'omelas', 'ultimo-homem', 'jim-e-os-indigenas']),
 'o-que-e-metaetica': (['realismo-naturalista', 'teoria-do-erro', 'emotivismo', 'quietismo-metaetico'], []), 'realismo-moral': (['realismo-naturalista', 'realismo-nao-naturalista', 'construtivismo'], []), 'antirrealismo-moral': (['teoria-do-erro', 'emotivismo', 'prescritivismo', 'quase-realismo'], []),
 'relativismo-e-quietismo': (['relativismo-metaetico', 'quietismo-metaetico', 'relativismo-cultural'], []), 'evolucao-e-moral': (['realismo-nao-naturalista', 'quase-realismo'], []), 'gradualismo': (['gradualismo', 'sencientismo'], ['casos-marginais']), 'geracoes-futuras': (['temporalismo'], ['conclusao-repugnante']),
 'mentes-artificiais': (['carbonismo', 'sencientismo'], []), 'vida-e-ecossistemas': (['biocentrismo', 'ecocentrismo', 'sencientismo'], ['ultimo-homem']), 'etica-populacional': (['utilitarismo-medio', 'prioridade-ao-sofrimento'], ['conclusao-repugnante']), 'incerteza-moral': ([], ['transplante']),
 'quanto-a-moral-pode-exigir': (['utilitarismo-classico'], ['crianca-no-lago', 'barco-salva-vidas']),
 'igualdade-humana': (['sencientismo', 'contratualismo-rawlsiano'], ['casos-marginais']), 'fraqueza-de-vontade': (['etica-das-virtudes', 'sencientismo'], ['anel-de-giges', 'crianca-no-lago']), 'fazer-e-deixar-acontecer': (['consequencialismo-de-ato', 'deontologia-de-direitos'], ['bonde-desvio', 'crianca-no-lago']), 'pobreza-e-etica-global': (['utilitarismo-classico', 'prioritarismo', 'deontologia-de-direitos'], ['crianca-no-lago', 'barco-salva-vidas']),
 'sofrimento-dos-animais-selvagens': (['sencientismo', 'ecocentrismo'], ['ultimo-homem']), 'animais-e-a-politica': (['sencientismo', 'contratualismo-estendido'], ['veu-da-ignorancia']), 'riscos-s-e-riscos-x': (['utilitarismo-negativo', 'temporalismo'], ['conclusao-repugnante']), 'catastrofes-morais': (['sencientismo', 'antropocentrismo'], ['casos-marginais', 'omelas']),
 'eticas-religiosas': (['teoria-do-mandamento-divino', 'etica-das-virtudes', 'etica-budista', 'confucionismo'], []), 'historia-da-etica': (['etica-das-virtudes', 'utilitarismo-classico', 'deontologia-kantiana', 'moismo'], []), 'parcialidade-e-deveres-especiais': (['confucionismo', 'contratualismo-rawlsiano', 'etica-do-cuidado'], ['crianca-no-lago']), 'teorias-do-bem-estar': (['utilitarismo-classico', 'utilitarismo-de-preferencias'], ['maquina-de-experiencias']), 'emocoes-morais': (['etica-das-virtudes', 'emotivismo'], ['anel-de-giges']), 'situacionismo-e-experimentos': (['etica-das-virtudes'], ['dilema-do-prisioneiro']), 'livre-arbitrio-e-responsabilidade': (['existencialismo', 'deontologia-kantiana'], ['casos-de-frankfurt', 'gauguin']), 'epistemologia-moral': (['intuicionismo-moral', 'ficcionalismo-moral', 'teoria-do-erro'], []), 'pluralismo-de-valores': (['deontologia-pluralista', 'etica-das-virtudes'], ['escolha-de-sofia']),
 'perguntas-frequentes': (['relativismo-cultural', 'egoismo-etico', 'sencientismo'], ['anel-de-giges']), 'educacao-moral': (['etica-das-virtudes', 'confucionismo', 'pragmatismo'], ['dilema-de-heinz']), 'bioetica': (['deontologia-pluralista', 'deontologia-kantiana', 'utilitarismo-classico'], ['transplante', 'violinista']), 'deficiencia-e-etica': (['etica-do-cuidado', 'sencientismo', 'contratualismo-rawlsiano'], ['casos-marginais']), 'etica-climatica': (['ecocentrismo', 'sencientismo', 'utilitarismo-classico'], ['tragedia-dos-comuns', 'torturadores-inofensivos']), 'etica-da-tecnologia': (['deontologia-kantiana', 'sencientismo', 'carbonismo'], ['torturadores-inofensivos']), 'etica-da-crenca': (['intuicionismo-moral', 'objetivismo-moral'], []), 'etica-feminista': (['etica-do-cuidado', 'contratualismo-rawlsiano', 'sencientismo'], ['veu-da-ignorancia']), 'sentido-da-vida': (['etica-das-virtudes', 'existencialismo', 'epicurismo', 'estoicismo'], ['maquina-de-experiencias']), 'exploracao': (['contratualismo-escanloniano', 'deontologia-kantiana', 'utilitarismo-classico'], ['barco-salva-vidas']), 'responsabilidade-coletiva': (['consequencialismo-de-ato', 'deontologia-kantiana', 'sencientismo'], ['torturadores-inofensivos', 'tragedia-dos-comuns']), 'identidade-pessoal-e-etica': (['egoismo-etico', 'utilitarismo-classico', 'etica-budista'], ['conclusao-repugnante']), 'motivacao-moral': (['sentimentalismo-moral', 'emotivismo', 'realismo-nao-naturalista', 'deontologia-kantiana'], ['anel-de-giges']), 'moralidade-sem-religiao': (['teoria-do-mandamento-divino', 'subjetivismo', 'etica-budista', 'sentimentalismo-moral', 'realismo-naturalista'], ['anel-de-giges']), 'punicao-e-justica': (['deontologia-kantiana', 'utilitarismo-classico', 'consequencialismo-de-regras', 'deontologia-de-direitos'], ['casos-de-frankfurt', 'transplante']), 'etica-da-inteligencia-artificial': (['deontologia-kantiana', 'consequencialismo-de-regras', 'contratualismo-escanloniano', 'sencientismo', 'carbonismo'], ['torturadores-inofensivos']), 'problema-do-alinhamento': (['contratualismo-escanloniano', 'utilitarismo-classico', 'deontologia-kantiana', 'etica-focada-no-sofrimento', 'deontologia-pluralista'], ['veu-da-ignorancia', 'conclusao-repugnante']), 'um-cenario-melhor-ou-o-melhor': (['consequencialismo-de-ato', 'utilitarismo-classico'], ['crianca-no-lago']), 'economia-politica-e-etica': (['deontologia-de-direitos', 'prioritarismo', 'igualitarismo'], ['veu-da-ignorancia']), 'teoria-da-decisao-e-etica': (['utilitarismo-classico', 'maximin'], ['transplante']), 'probabilidade-e-etica': (['sencientismo'], []), 'da-etica-a-politica': (['prioritarismo', 'suficientismo'], []), 'progresso-moral': (['sencientismo'], []), 'abertura-moral': ([], []),
}
def liga_licao(l):
    ts, ds = LICAO_LIGA.get(l['slug'], ([], []))
    for t in ts: assert t in TEO_S, (l['slug'], t)
    for d in ds: assert d in DIL_S, (l['slug'], d)
    out = ''
    if ts: out += '<div class="nota"><strong>Teorias desta lição:</strong> ' + ', '.join(tlink(t) for t in ts) + '.</div>'
    if ds: out += '<div class="nota"><strong>Dilemas para testar:</strong> ' + ', '.join(f'<a href="dilemas/{d}.html">{e(DIL_S[d]["n"])}</a>' for d in ds) + '.</div>'
    dbs = [d for d in DEBATES if l['slug'] in d['licoes']]
    if dbs: out += '<div class="nota"><strong>Nos debates:</strong> ' + ', '.join(f'<a href="debates/{d["s"]}.html">{e(d["n"])}</a>' for d in dbs) + '.</div>'
    return out

def licao(l, ls):
    i = l['i']; ant = ls[i - 1] if i else None; prox = ls[i + 1] if i + 1 < len(ls) else None
    pager = '<nav class="pager" aria-label="Lições">'
    if ant: pager += f'<a href="{ant["slug"]}.html"><small>← Anterior</small>{e(ant["titulo"])}</a>'
    if prox: pager += f'<a class="prox" href="{prox["slug"]}.html"><small>Próxima →</small>{e(prox["titulo"])}</a>'
    pager += '</nav>'
    ordem = [n[0] for n in NIVEIS]
    if not prox and l['nivel'] != ordem[-1]:
        seg = NIVEIS[ordem.index(l['nivel']) + 1]
        pager += f'<div class="fim-nivel"><p class="ti">Você chegou ao fim do nível {e(l["nivel_rot"])}</p><p>Faça o teste do nível e continue com {len(seg[2])} lições do nível {e(seg[1])}.</p><a class="btn alt" href="revisao-{l["nivel"]}.html">Revisão do nível</a> <a class="btn alt" href="teste-{l["nivel"]}.html">Teste do nível</a> <a class="btn {seg[5]}" href="{seg[0]}.html">Ir para o curso {e(seg[1])} →</a></div>'
    if not prox and l['nivel'] == ordem[-1]:
        pager += f'<div class="fim-nivel"><p class="ti">Você chegou ao fim do curso</p><p>Faça o teste do nível, monte a sua posição e continue do lado da política.</p><a class="btn alt" href="revisao-avancado.html">Revisão do nível</a> <a class="btn alt" href="teste-avancado.html">Teste do nível</a> <a class="btn a" href="minha-posicao.html">Minha posição</a> <a class="btn" href="https://politicaparainiciantes.biblioverse.org/" {EXT}>Política Para Iniciantes →</a></div>'
    min_ = tempo_leitura(l['corpo'])
    tg = ''.join(f'<a class="tag" href="catalogo.html?tema={t}">{e(TEMAS[t])}</a>' for t in l['temas'])
    meta = f'<div class="meta"><span class="tipo {l["nivel"]}">{e(l["nivel_rot"])}</span>{tg}<span>{min_} min de leitura</span></div>'
    topo = cabeca(f'<a href="{l["nivel"]}.html">{e(l["nivel_rot"])}</a> / {e(l["grupo"])}', l['titulo'], e(l['resumo']), meta=meta)
    pre_ = DID[l['slug']]['pre']
    antes = ('<dt>Antes</dt><dd>' + ', '.join(f'<a href="{s}.html">{e(next(x["titulo"] for x in TODAS if x["slug"] == s))}</a>' for s in pre_) + '</dd>') if pre_ else ''
    lado = f'''<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Nível</dt><dd>{e(l["nivel_rot"])}</dd><dt>Tempo</dt><dd>{min_} minutos</dd><dt>Temas</dt><dd>{e(", ".join(TEMAS[t] for t in l["temas"]))}</dd>{antes}</dl></div><div class="caixa toc-caixa"><h2>Nesta lição</h2><ul class="toc"></ul></div><button class="marcar" type="button" data-id="{l["slug"]}">Marcar como lida</button></aside>'''
    ct = l['corpo']; k = ct.index('</section></div>', ct.index('class="ajuda"')) + len('</section></div>')
    ct = glossa(ct[:k] + bloco_didatico(l) + ct[k:], l['titulo'])
    ct = re.sub(r'<div class="nota"><strong>Para guardar:</strong>.*?</div>', '', ct, count=1, flags=re.S)
    corpo = indice(l, ls) + topo + f'<div class="wrap layout"><article class="leitura">{tabelas(ct)}{fecho(l)}{erro_pratica(l)}{liga_licao(l)}{quizzes(l)}{fontes(l["fontes"])}{pager}</article>{lado}</div>' + relacionados(l)
    page(f'{l["slug"]}.html', l['titulo'], l['resumo'], corpo, atual=f'{l["nivel"]}.html')

# ---------- teorias, critérios e metaética ----------
def hub_teorias(kicker, titulo, lede, nota, fams, comparador=False):
    arvore = ''
    for f in fams:
        its = [t for t in TEO if t['f'] == f]
        arvore += f'<section class="familia"><h3><span class="tipo fam f{COR_FAM[f]}">{e(f)}</span> <small>{e(FOCO_FAM[f])}</small></h3><div class="fio">' + ''.join(f'<a href="teorias/{t["s"]}.html">{e(t["n"])}</a>' for t in its) + '</div></section>'
    bots = '<button type="button" data-k="f" data-v="" aria-pressed="true">Todas</button>' + ''.join(f'<button type="button" data-k="f" data-v="{e(f)}" aria-pressed="false">{e(f)}</button>' for f in fams)
    gr = ''.join(f'<section class="grupo-l"><h2 class="grupo">{e(f)} <small>{e(FOCO_FAM[f])}</small></h2><div class="grade">' + ''.join(cartao_t(t, 'teorias/') for t in TEO if t['f'] == f) + '</div></section>' for f in fams)
    comp = ''
    if comparador:
        dados_t = json.dumps([dict(s=t['s'], n=t['n'], f=t['f'], foco=t['foco'], i=t['i'], bonde=t['bonde'], forte=t['forte'], contra=t['contra'], p=t['p']) for t in TEO], ensure_ascii=False).replace('</', '<\\/')
        comp = f'<h2 style="margin:2.2rem 0 .8rem">Compare</h2><div class="grade" style="grid-template-columns:repeat(auto-fit,minmax(170px,1fr));margin-bottom:14px"><label class="campo">Teoria 1<select id="ta"></select></label><label class="campo">Teoria 2<select id="tb"></select></label><label class="campo">Teoria 3<select id="tc"></select></label></div><div class="tabela"><table class="compara" id="tcomp"></table></div><script type="application/json" id="dados-teo">{dados_t}</script>'
    n = sum(1 for t in TEO if t['f'] in fams)
    corpo = cabeca(kicker, titulo, lede.format(n=n))
    corpo += f'<div class="wrap secao"><div class="nota" style="margin-top:0">{nota}</div><div class="sec-cab"><h2>O mapa</h2><p>Clique em uma posição para abrir.</p></div>{arvore}{comp}<h2 style="margin:2.2rem 0 .8rem">Todas</h2><input class="fq" id="fq" type="search" placeholder="Filtrar por nome ou ideia" aria-label="Filtrar"/><div class="filtros" role="group" aria-label="Família">{bots}</div><p class="contagem" id="contagem" role="status"></p><div id="lista">{gr}</div></div>'
    return corpo
def criterios_extra():
    for d in DELIM: assert d['t'] in TEO_S, d['t']
    cab = '<tr><th></th>' + ''.join(f'<th><a href="teorias/{d["t"]}.html">{e(d["n"])}</a></th>' for d in DELIM) + '</tr>'
    linhas = ''.join(f'<tr><td>{e(r)}</td>' + ''.join(f'<td>{e(d[k])}</td>' for d in DELIM) + '</tr>' for r, k in [('Quem tem valor direto', 'valor'), ('A razão alegada', 'mot'), ('Movimentos derivados', 'deriv'), ('Parcialidades que deixa passar', 'permite'), ('Fins', 'fins'), ('Pontos fortes', 'forcas'), ('Fraquezas', 'fraquezas')])
    delim = f'<div class="tabela"><table class="compara matriz-d"><thead>{cab}</thead><tbody>{linhas}</tbody></table></div>'
    fr = ''
    for g in sorted(GRAUS):
        its = [x for x in FRONTEIRAS if x[0] == g]
        fr += f'<tr><th colspan="5">Grau {g}: {e(GRAUS[g])}</th></tr>' + ''.join(f'<tr><td><strong>{e(n)}</strong></td><td>{e(c)}</td><td>{e(f)}</td><td>{e(d)}</td><td>{e(o)}</td></tr>' for _, n, c, f, d, o in its)
    front = f'<div class="tabela"><table class="compara"><thead><tr><th>Viés ou sistema parcial</th><th>Critério usado</th><th>Favorece</th><th>Despreza ou prejudica</th><th>A posição imparcial</th></tr></thead><tbody>{fr}</tbody></table></div>'
    dim = '<div class="tabela"><table class="compara"><thead><tr><th>Dimensão</th><th>A pergunta</th><th>As respostas</th></tr></thead><tbody>' + ''.join(f'<tr><td><a href="{u}"><strong>{e(n)}</strong></a></td><td>{e(p)}</td><td>{e(r)}</td></tr>' for n, p, r, u in DIMENSOES) + '</tbody></table></div>'
    return f'''<div class="wrap secao" style="padding-top:0"><div class="sec-cab"><h2>As seis delimitações do círculo</h2><p>Quem tem valor direto, a razão alegada, o que cada delimitação deixa passar e onde é forte ou fraca. As delimitações podem se combinar, e cada pessoa tem graus de cada uma; quando entram em conflito, é preciso decidir qual pesa.</p></div>{delim}<p class="legenda">Quadro editorial do site, a partir das planilhas de delimitações éticas e do critério da relevância: o que importa para contar é poder ser prejudicado ou beneficiado. Biocentristas e ecocentristas contestam esse critério; as páginas de cada posição trazem a defesa deles.</p>
<div class="sec-cab" style="margin-top:2.4rem"><h2>As fronteiras da parcialidade</h2><p>Raça, espécie, nacionalidade, religião, classe, idade, aparência: cada uma já serviu de critério para decidir quem conta. Todas têm a mesma estrutura: um traço irrelevante para o que está em jogo, tomado como relevante. A coluna da direita diz qual é a posição imparcial correspondente, e ela nunca é a hostilidade ao grupo favorecido: é a consideração igual.</p></div>{front}<p class="legenda">Os graus vão do indivíduo à espécie e ao tempo. Cada pessoa pode ter um pouco de várias fronteiras, em intensidades diferentes; sistemas sociais inteiros se organizam em torno delas. A última linha, o inevidencialismo, não é um viés de grupo: é uma falha epistêmica, incluída porque decisões sem evidência prejudicam quem é afetado por elas. Veja a lição sobre <a href="tribalismo-moral.html">tribalismo moral</a>.</p>
<div class="sec-cab" style="margin-top:2.4rem"><h2>As cinco dimensões de uma visão moral</h2><p>Uma visão moral não é só uma teoria. Tem cinco dimensões, e o site cobre cada uma em uma seção.</p></div>{dim}{fontes(FONTES_CRIT)}</div>'''
def teorias():
    page('teorias.html', 'Teorias éticas', 'Consequencialismo, deontologia, virtudes, cuidado e contratualismo: o ponto focal de cada teoria normativa, forças e objeções.', hub_teorias('Ideias', 'Teorias éticas', '{n} teorias normativas, do utilitarismo ao contratualismo: o que mais pesa para cada uma, as variantes, os pontos fortes e as objeções.', f'<strong>Como ler:</strong> cada teoria é apresentada pelo seu <em>ponto focal</em>, o que mais deve pesar quando os critérios entram em conflito. Nenhuma teoria séria ignora resultados, regras ou caráter; a diferença está no que vem primeiro. As posições sobre quem conta estão em <a href="criterios.html">critérios éticos</a>, e as sobre o que é um juízo moral, em <a href="metaetica.html">metaética</a>. O mapa segue a estrutura do <a href="https://ethicstest.biblioverse.org/map.html" {EXT}>Teste de Visão Moral</a>.', FAM_TEO, comparador=True), atual='teorias.html')
    page('criterios.html', 'Critérios éticos', 'Quem conta e com que peso: antropocentrismo, sencientismo, biocentrismo, ecocentrismo, gradualismo; e egoísmo, relativismo e ceticismo.', hub_teorias('Ideias', 'Critérios éticos', '{n} posições sobre os critérios da moral: quem recebe consideração direta, com que peso, e se há um padrão comum a todos.', f'<strong>Como ler:</strong> antes de decidir como agir, toda ética responde a duas perguntas de critério: <em>quem conta</em> (o círculo moral) e <em>se há um padrão válido para todos</em> (contra o egoísmo, o relativismo e o ceticismo). Estas posições se combinam com qualquer <a href="teorias.html">teoria normativa</a>. Veja as lições sobre o <a href="circulo-moral.html">círculo moral</a> e sobre <a href="egoismo-relativismo-e-ceticismo.html">egoísmo, relativismo e ceticismo</a>.', FAM_CRI) + criterios_extra(), atual='criterios.html')
    page('metaetica.html', 'Metaética', 'Realismo, antirrealismo, teoria do erro, emotivismo, prescritivismo, quase-realismo, construtivismo e quietismo: o que é um juízo moral.', hub_teorias('Ideias', 'Metaética', '{n} posições sobre o estatuto da moral: fatos morais existem? São descobertos, construídos ou expressos? Como os conhecemos?', f'<strong>Como ler:</strong> a metaética não diz o que fazer; pergunta o que estamos fazendo quando dizemos que algo é certo. Dois realistas podem ser um utilitarista e um kantiano, e até o cético tem uma tendência prática. Comece pela lição <a href="o-que-e-metaetica.html">o que é metaética</a>.', FAM_MET), atual='metaetica.html')
    for i, t in enumerate(TEO):
        wiki = ('https://pt.wikipedia.org/wiki/' + t['w'][3:]) if t['w'].startswith('pt:') else 'https://en.wikipedia.org/wiki/' + t['w']
        fils = ''.join(f'<a href="../filosofos/{f["slug"]}.html" class="tipo ferr">{e(f["nome"])}</a>' for f in FIL if t['s'] in f['teorias'] or f['slug'] in t['fil'])
        liga = f'<h2>Filósofos ligados</h2><p class="tags">{fils}</p>' if fils else ''
        lics = [l for l in TODAS if t['s'] in LICAO_LIGA.get(l['slug'], ([], []))[0]]
        dils = [d for d in DILEMAS if any(x[0] == t['s'] for x in d['teorias'])]
        dbs = [d for d in DEBATES if any(x[0] == t['s'] for x in d['teorias'])]
        ler = ''
        ler += lista_mais('Lições', [f'<a href="../{l["slug"]}.html">{e(l["titulo"])}</a>' for l in lics])
        ler += lista_mais('Nos dilemas', [f'<a href="../dilemas/{d["s"]}.html">{e(d["n"])}</a>' for d in dils])
        ler += lista_mais('Nos debates', [f'<a href="../debates/{d["s"]}.html">{e(d["n"])}</a>' for d in dbs])
        mesmas = [x for x in TEO if x['f'] == t['f'] and x['s'] != t['s']][:3]
        ant, prox = TEO[i - 1], TEO[(i + 1) % len(TEO)]
        hub = HUB_FAM[t['f']]
        lado = f'<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Família</dt><dd>{e(t["f"])}</dd><dt>O que mais pesa</dt><dd>{e(t["foco"])}</dd></dl></div><div class="caixa toc-caixa"><h2>Nesta página</h2><ul class="toc"></ul></div></aside>'
        corpo = cabeca(f'<a href="../{hub}">{e(HUB_DE[hub])}</a>', t['n'], e(t['r']), meta=f'<div class="meta"><span class="tipo fam f{COR_FAM[t["f"]]}">{e(t["f"])}</span></div>')
        corpo += f'''<div class="wrap layout"><article class="leitura"><div class="nota" style="margin-top:0"><strong>Ponto focal:</strong> {e(t["foco"])} Isso é o que pesa mais para esta posição, não a única coisa que ela considera.</div><h2>A ideia central</h2><p>{t["i"]}</p>
<h2>Referências</h2><p>{e(t["p"])}</p><h2>De onde veio</h2><p>{t["h"]}</p><h2>No dilema do bonde</h2><p>{e(t["bonde"])} <a href="../o-dilema-do-bonde.html">Entenda o dilema</a>.</p>
<h2>Pontos fortes: o que pode estar certo</h2><ul class="lista-forte">{"".join(f"<li>{e(x)}</li>" for x in t["forte"])}</ul><h2>Objeções</h2><ul class="lista-contra">{"".join(f"<li>{e(x)}</li>" for x in t["contra"])}</ul><h2>O que dizem os críticos</h2><p>{e(t["c"])}</p>{liga}{ler}
{fontes([("Wikipédia: " + t["n"], wiki)] + t["fx"])}<nav class="pager" aria-label="Teorias"><a href="{ant["s"]}.html"><small>← Anterior</small>{e(ant["n"])}</a><a class="prox" href="{prox["s"]}.html"><small>Próxima →</small>{e(prox["n"])}</a></nav></article>{lado}</div><section class="relac"><div class="wrap"><h2>Na mesma família</h2><div class="grade">{"".join(cartao_t(x) for x in mesmas)}</div></div></section>'''
        page(f'teorias/{t["s"]}.html', t['n'], t['r'], corpo, atual=hub)

# ---------- debates ----------
def cartao_db(d, pre=''): return f'<a class="cartao item" data-t="{e(d["t"])}" data-p="{d["p"][0]}" href="{pre}{d["s"]}.html"><span class="linha-cartao"><span class="peso {d["p"][0]}">{e(ROT_PESO[d["p"][0]])}</span></span><h3>{e(d["n"])}</h3><p>{e(d["r"])}</p></a>'
def debates_pub():
    bots = '<button type="button" data-k="t" data-v="" aria-pressed="true">Todos</button>' + ''.join(f'<button type="button" data-k="t" data-v="{e(t)}" aria-pressed="false">{e(t)}</button>' for t in TEMAS_DB)
    gr = ''.join(f'<section class="grupo-l"><h2 class="grupo">{e(t)}</h2><div class="grade">' + ''.join(cartao_db(d, 'debates/') for d in DEBATES if d['t'] == t) + '</div></section>' for t in TEMAS_DB)
    leg = ''.join(f'<li><span class="peso {k}">{e(v)}</span></li>' for k, v in ROT_PESO.items())
    botp = '<button type="button" data-k="p" data-v="" aria-pressed="true">Qualquer peso</button>' + ''.join(f'<button type="button" data-k="p" data-v="{k}" aria-pressed="false">{e(v)}</button>' for k, v in ROT_PESO.items())
    corpo = cabeca('Ideias', 'Debates éticos', f'{len(DEBATES)} questões que dividem o público: as perspectivas, o que cada teoria diz, por que é complexo e onde a razão pesa.')
    corpo += f'''<div class="wrap secao"><div class="nota" style="margin-top:0"><strong>Como ler:</strong> quando há posições razoáveis dos dois lados, mostramos as duas. Quando há consenso entre filósofos morais, ou quando um lado é logicamente mais forte, damos a ele mais ênfase, e dizemos por quê. Essa avaliação é do site e pode ser contestada; cada página traz as fontes.</div><ul class="leg-peso">{leg}</ul><input class="fq" id="fq" type="search" placeholder="Filtrar por nome ou tema" aria-label="Filtrar debates"/><div class="filtros" role="group" aria-label="Tema">{bots}</div><div class="filtros" role="group" aria-label="Peso">{botp}</div><p class="contagem" id="contagem" role="status"></p><div id="lista">{gr}</div></div>'''
    page('debates.html', 'Debates éticos', 'Bilionários, eutanásia, aborto, mentira, tortura, imigração, relacionamentos, duplo padrão sexual, luxo e mais: as perspectivas e onde a razão pesa.', corpo, atual='debates.html')
    for i, d in enumerate(DEBATES):
        lado = lambda x: f'<div><h3>{e(x[0])}</h3><ul>' + ''.join(f'<li>{e(p)}</li>' for p in x[1]) + '</ul></div>'
        lados = f'<div class="dois-lados">{"".join(lado(x) for x in d["lados"])}</div>' if len(d['lados']) > 1 else lado(d['lados'][0]).replace('<div>', '<div class="caso">', 1)
        tab = ''.join(f'<tr><th>{tlink(s, "../")}</th><td>{e(x)}</td></tr>' for s, _, x in d['teorias'])
        for s, _, _ in d['teorias']: assert s in TEO_S, (d['s'], s)
        for s in d['licoes']: assert any(l['slug'] == s for l in TODAS), (d['s'], s)
        ler = '<p><strong>Lições relacionadas:</strong> ' + ', '.join(f'<a href="../{s}.html">{e(next(l["titulo"] for l in TODAS if l["slug"] == s))}</a>' for s in d['licoes']) + '.</p>'
        mesmos = [x for x in DEBATES if x['t'] == d['t'] and x['s'] != d['s']][:3]
        ant, prox = DEBATES[i - 1], DEBATES[(i + 1) % len(DEBATES)]
        corpo = cabeca('<a href="../debates.html">Debates</a> / ' + e(d['t']), d['n'], e(d['r']))
        bts = ''.join(f'<button type="button" data-v="{i}" aria-pressed="false">{e(x[0])}</button>' for i, x in enumerate(d['lados'])) + '<button type="button" data-v="ns" aria-pressed="false">Ainda não sei</button>'
        pos1 = f'<div class="posicao" data-deb="{d["s"]}"><p class="k">Antes de ler: para que lado você pende?</p><div class="ops">{bts}</div><p class="fb" role="status"></p></div>' if len(d['lados']) > 1 else ''
        pos2 = f'<div class="posicao depois" data-deb="{d["s"]}"><p class="k">E agora, depois de ler?</p><div class="ops">{bts}</div><p class="fb" role="status"></p></div>' if len(d['lados']) > 1 else ''
        corpo += f'''<div class="wrap estreito leitura secao"><p class="abre">{e(d["v"])}</p>{pos1}<h2>{"As perspectivas" if len(d["lados"]) > 1 else "A posição"}</h2>{lados}<p class="legenda">Posições gerais. Muita gente concorda em parte com cada lado.</p><h2>O que cada teoria tende a dizer</h2><div class="tabela"><table class="compara"><tbody>{tab}</tbody></table></div><h2>Por que é complexo</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in d["c"])}</ul><h2>Onde a razão pesa</h2><div class="nota veredito {d["p"][0]}"><strong>{e(ROT_PESO[d["p"][0]])}</strong><p>{e(d["p"][1])}</p></div><p class="legenda">Avaliação do site, sujeita a críticas. <a href="../abertura-moral.html">Evidências e argumentos novos podem mudá-la.</a></p>{pos2}<h2>Perguntas para pensar</h2><ol class="roteiro"><li>Qual parte é fato, e qual é valor?</li><li>Quem paga o preço de cada opção, e essa pessoa tem voz?</li><li>Eu aceitaria essa regra sem saber em que lugar estaria?</li><li>O que me faria mudar de ideia?</li></ol>{ler}{fontes(d["fx"])}<nav class="pager" aria-label="Debates"><a href="{ant["s"]}.html"><small>← Anterior</small>{e(ant["n"])}</a><a class="prox" href="{prox["s"]}.html"><small>Próximo →</small>{e(prox["n"])}</a></nav></div><section class="relac"><div class="wrap"><h2>No mesmo tema</h2><div class="grade">{"".join(cartao_db(x) for x in mesmos)}</div></div></section>'''
        page(f'debates/{d["s"]}.html', d['n'], d['r'], corpo, atual='debates.html')

# ---------- dilemas ----------
def dilemas_pub():
    bots = '<button type="button" data-k="t" data-v="" aria-pressed="true">Todos</button>' + ''.join(f'<button type="button" data-k="t" data-v="{e(t)}" aria-pressed="false">{e(t)}</button>' for t in TEMAS_D)
    gr = ''.join(f'<section class="grupo-l"><h2 class="grupo">{e(t)}</h2><div class="grade">' + ''.join(cartao_d(d, 'dilemas/') for d in DILEMAS if d['t'] == t) + '</div></section>' for t in TEMAS_D)
    corpo = cabeca('Ideias', 'Dilemas clássicos', f'{len(DILEMAS)} experimentos mentais que moldaram a ética: o caso, a pergunta e o que cada teoria tende a dizer.')
    corpo += f'''<div class="wrap secao"><div class="nota" style="margin-top:0"><strong>Como usar:</strong> aceite as premissas, note a sua primeira reação, pergunte que princípio ela expressa e teste o princípio em outro caso. Veja <a href="experimentos-mentais.html">como usar um experimento mental</a>, ou responda às variantes do bonde na <a href="ferramentas/dilema-do-bonde.html">ferramenta</a>.</div><input class="fq" id="fq" type="search" placeholder="Filtrar por nome ou tema" aria-label="Filtrar dilemas"/><div class="filtros" role="group" aria-label="Tema">{bots}</div><p class="contagem" id="contagem" role="status"></p><div id="lista">{gr}</div></div>'''
    page('dilemas.html', 'Dilemas clássicos', 'O bonde, o transplante, a criança no lago, o violinista, a máquina de experiências e outros: o que cada teoria ética diz.', corpo, atual='dilemas.html')
    for i, d in enumerate(DILEMAS):
        tab = ''.join(f'<tr><th>{tlink(s, "../")}</th><td>{e(x)}</td></tr>' for s, _, x in d['teorias'])
        lics = [l for l in TODAS if d['s'] in LICAO_LIGA.get(l['slug'], ([], []))[1]]
        ler = ('<p><strong>Lições relacionadas:</strong> ' + ', '.join(f'<a href="../{l["slug"]}.html">{e(l["titulo"])}</a>' for l in lics) + '.</p>') if lics else ''
        mesmos = [x for x in DILEMAS if x['t'] == d['t'] and x['s'] != d['s']][:3]
        ant, prox = DILEMAS[i - 1], DILEMAS[(i + 1) % len(DILEMAS)]
        corpo = cabeca('<a href="../dilemas.html">Dilemas</a> / ' + e(d['t']), d['n'], e(d['r']))
        corpo += f'''<div class="wrap estreito leitura secao"><p class="legenda"><strong>Origem:</strong> {e(d["o"])}</p><div class="cena">{e(d["cena"])}</div><p class="abre">{e(d["q"])}</p><h2>O que cada teoria tende a dizer</h2><div class="tabela"><table class="compara"><tbody>{tab}</tbody></table></div><p class="legenda">Tendências, não vereditos: dentro de cada teoria há variantes, e autores da mesma família discordam.</p><h2>O que o caso ensina</h2><p>{e(d["licao"])}</p><h2>Perguntas para pensar</h2><ol class="roteiro"><li>Qual foi a sua primeira reação, e que princípio ela expressa?</li><li>Esse princípio vale em um caso parecido com os papéis trocados?</li><li>O que mudaria a sua resposta?</li></ol>{ler}{fontes(d["fx"])}<nav class="pager" aria-label="Dilemas"><a href="{ant["s"]}.html"><small>← Anterior</small>{e(ant["n"])}</a><a class="prox" href="{prox["s"]}.html"><small>Próximo →</small>{e(prox["n"])}</a></nav></div><section class="relac"><div class="wrap"><h2>No mesmo tema</h2><div class="grade">{"".join(cartao_d(x) for x in mesmos)}</div></div></section>'''
        page(f'dilemas/{d["s"]}.html', d['n'], d['r'], corpo, atual='dilemas.html')

# ---------- filósofos ----------
def filosofos():
    bots = '<button type="button" data-k="c" data-v="" aria-pressed="true">Todas</button>' + ''.join(f'<button type="button" data-k="c" data-v="{e(c)}" aria-pressed="false">{e(c)}</button>' for c in CORRENTES)
    gr = ''.join(f'<section class="grupo-l"><h2 class="grupo">{e(c)}</h2><div class="grade">' + ''.join(cartao_f(f, 'filosofos/') for f in FIL if f['corrente'] == c) + '</div></section>' for c in CORRENTES)
    corpo = cabeca('Ideias', 'Filósofos morais', f'{len(FIL)} pensadores, de Pitágoras e Buda a Singer e Baumann: quem foram, o que defenderam, as obras e o que dizem os críticos.')
    corpo += f'''<div class="wrap secao"><div class="nota" style="margin-top:0"><strong>Como ler:</strong> cada perfil é um resumo, não uma biografia. As ideias estão simplificadas, e a seção de críticas mostra onde cada autor é mais contestado. Alguns nomes não são filósofos de formação (psicólogos, juristas, cientistas, mestres religiosos); o perfil diz isso, e eles entram porque suas ideias moldaram o debate ético. Os pontos cegos de grandes filósofos (Aristóteles e a escravidão, Kant e os animais) ensinam tanto quanto os acertos.</div><input class="fq" id="fq" type="search" placeholder="Filtrar por nome ou ideia" aria-label="Filtrar filósofos"/><div class="filtros" role="group" aria-label="Corrente">{bots}</div><p class="contagem" id="contagem" role="status"></p><div id="lista">{gr}</div></div>'''
    page('filosofos.html', 'Filósofos morais', 'Platão, Aristóteles, Kant, Bentham, Mill, Rawls, Singer, Parfit e outros: ideias, obras e críticas de cada filósofo moral.', corpo, atual='filosofos.html')
    for i, f in enumerate(FIL):
        teos = ''.join(f'{tlink(s, "../", "tipo fam f" + str(COR_FAM[TEO_S[s]["f"]]))}' for s in f['teorias'])
        liga = f'<h2>Teorias ligadas</h2><p class="tags">{teos}</p>' if teos else ''
        mesmos = [x for x in FIL if x['corrente'] == f['corrente'] and x['slug'] != f['slug']][:3]
        ant, prox = FIL[i - 1], FIL[(i + 1) % len(FIL)]
        lado = f'<aside class="lado"><div class="caixa"><h2>Em resumo</h2><dl><dt>Viveu</dt><dd>{e(f["anos"])}</dd><dt>Onde</dt><dd>{e(f["pais"])}</dd><dt>Corrente</dt><dd>{e(f["corrente"])}</dd></dl></div><div class="caixa toc-caixa"><h2>Nesta página</h2><ul class="toc"></ul></div></aside>'
        corpo = cabeca('<a href="../filosofos.html">Filósofos morais</a>', f['nome'], e(f['quem']), meta=f'<div class="meta"><span class="tipo fam f{COR_COR[f["corrente"]]}">{e(f["corrente"])}</span><span class="tipo ferr">{e(f["anos"])}</span></div>')
        corpo += f'''<div class="wrap layout"><article class="leitura"><h2>Ideias principais</h2><ul class="lista-forte">{"".join(f"<li>{e(x)}</li>" for x in f["ideias"])}</ul><h2>Obras</h2><ul>{"".join(f"<li><em>{e(x)}</em></li>" for x in f["obras"])}</ul><h2>O que dizem os críticos</h2><p>{e(f["criticas"])}</p>{liga}
{fontes([("Wikipédia: " + f["nome"], "https://en.wikipedia.org/wiki/" + f["w"])] + f["fx"])}<nav class="pager" aria-label="Filósofos"><a href="{ant["slug"]}.html"><small>← Anterior</small>{e(ant["nome"])}</a><a class="prox" href="{prox["slug"]}.html"><small>Próximo →</small>{e(prox["nome"])}</a></nav></article>{lado}</div><section class="relac"><div class="wrap"><h2>Na mesma corrente</h2><div class="grade">{"".join(cartao_f(x) for x in mesmos)}</div></div></section>'''
        page(f'filosofos/{f["slug"]}.html', f['nome'], f['quem'], corpo, atual='filosofos.html')

# ---------- glossário ----------
def glossario():
    gr = ''
    for g in GRUPOS_G:
        gr += f'<h2 class="grupo">{e(g)}</h2><dl class="glossario">' + ''.join(f'<dt>{e(t)}</dt><dd><p>{e(d)}</p>' + (f'<p class="pol"><a href="{u}">Saiba mais</a></p>' if u else '') + '</dd>' for gg, t, d, u in GLOSSARIO if gg == g) + '</dl>'
    corpo = cabeca('Ideias', 'Glossário de ética', f'{len(GLOSSARIO)} termos explicados em uma ou duas frases, com link para a lição que os aprofunda.') + f'<div class="wrap estreito leitura secao">{gr}</div>'
    page('glossario.html', 'Glossário de ética', 'Consequencialismo, deontologia, senciência, especismo, metaética, realismo moral e outros termos explicados em uma frase.', corpo, atual='glossario.html')

# ---------- ferramentas ----------
def ferramentas():
    cards = ''.join(cartao_ferr(*f) for f in FERR)
    page('ferramentas.html', 'Ferramentas', 'Jogos e simuladores para aprender ética fazendo.', cabeca('Ferramentas', 'Aprenda fazendo', 'Sem cadastro. Nada do que você responde sai do seu navegador.') + f'<div class="wrap secao"><div class="grade">{cards}</div></div>', atual='ferramentas.html')
    def fp(a, tit, lede, corpo):
        d = next(x[2] for x in FERR if x[0] == a)
        page(f'ferramentas/{a}.html', tit, d, cabeca('<a href="../ferramentas.html">Ferramentas</a>', tit, lede) + f'<div class="wrap ferr secao" style="padding-top:28px">{corpo}</div>', atual='ferramentas.html')
    JOGO = '<div id="jogo" class="quiz" style="margin-top:0"><div class="placar"><span></span><span></span></div><div class="barra-prog"><i></i></div><div class="alvo" style="margin-top:14px"></div><button class="btn prox-q" type="button" style="margin-top:12px" hidden>Próxima</button></div>'
    dj = lambda d: f'<script type="application/json" id="dados-jogo">{json.dumps(d, ensure_ascii=False).replace("</", "<\\/")}</script>'
    fp('que-teoria-e-essa', 'Que teoria é essa?', 'Doze frases, seis famílias. Reconheça o ponto focal de cada argumento.', JOGO + dj(dict(tipo='opcoes', ops=TEORIAS_OPS, itens=[list(x) for x in FRASES_TEORIA])) + '<p class="legenda">Frases fictícias, escritas para o exercício. Uma mesma pessoa pode usar várias famílias em dias diferentes, e isso é normal.</p><p><a href="../mapa-das-teorias.html">Reveja o mapa das teorias</a>.</p>')
    fp('fato-ou-valor', 'Fato ou valor?', 'Antes de discutir, descubra o que está em jogo: uma questão de evidências ou uma questão moral.', JOGO + dj(dict(tipo='frases', itens=[list(x) for x in FRASES_FV])) + '<p><a href="../fatos-e-valores.html">Entenda a diferença</a>.</p>')
    fp('dilema-do-bonde', 'O bonde, caso a caso', 'Seis variantes. Responda a cada uma e veja o que o seu padrão sugere sobre a sua visão moral.', f'<div id="bonde" class="quiz" style="margin-top:0"><div class="placar"><span></span><span></span></div><div class="cena"></div><div class="ops"></div><div class="saida"></div><button class="btn prox-q" type="button" style="margin-top:12px" hidden>Próximo caso</button></div><script type="application/json" id="dados-bonde">{json.dumps(BONDE, ensure_ascii=False).replace("</", "<\\/")}</script><p class="legenda">As porcentagens são aproximações de vários estudos e variam com a formulação. <a href="../o-dilema-do-bonde.html">Leia a lição sobre o bonde</a>.</p>')
    fp('meu-circulo-moral', 'Monte o seu círculo moral', 'Marque quem recebe consideração direta de você. O nome da posição segue o mapa do Teste de Visão Moral.', '''<div id="circulo" class="quiz" style="margin-top:0"><p class="k">Quem conta por si mesmo?</p>
<label class="chk"><input type="checkbox" value="humanos" checked/> <span><strong>Humanos</strong><br/><small>Todas as pessoas, de qualquer lugar.</small></span></label>
<label class="chk"><input type="checkbox" value="animais"/> <span><strong>Animais sencientes</strong><br/><small>Todos os que podem sentir dor e prazer. Inclui os humanos.</small></span></label>
<label class="chk"><input type="checkbox" value="ia"/> <span><strong>Mentes artificiais sencientes</strong><br/><small>Caso existam: se uma máquina vier a sentir, ela conta?</small></span></label>
<label class="chk"><input type="checkbox" value="vida"/> <span><strong>Vida orgânica sem senciência</strong><br/><small>Plantas, fungos, bactérias.</small></span></label>
<label class="chk"><input type="checkbox" value="eco"/> <span><strong>Ecossistemas</strong><br/><small>Rios, florestas e biomas, por si mesmos.</small></span></label>
<div id="circulo-extra" hidden style="margin-top:14px"><p class="k">Duas perguntas a mais</p><p style="margin:.2rem 0 .4rem;font-weight:600">A inteligência muda o peso de um sofrimento igual?</p><div class="filtros"><label><input type="radio" name="grad" value="nao" checked/> Não: dor igual conta igual</label><label><input type="radio" name="grad" value="sim"/> Sim: mentes mais complexas pesam mais</label></div><p style="margin:.6rem 0 .4rem;font-weight:600">O presente pesa mais do que o futuro?</p><div class="filtros"><label><input type="radio" name="temp" value="nao" checked/> Não: uma dor vale o mesmo em qualquer data</label><label><input type="radio" name="temp" value="sim"/> Sim: quem existe agora pesa mais</label></div></div>
<div id="circulo-anel" class="aneis" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div><div id="circulo-res" class="fb" role="status" style="font-size:1.05rem"></div></div><p class="legenda">Os nomes seguem o <a href="https://ethicstest.biblioverse.org/map.html" target="_blank" rel="noopener">mapa do Teste de Visão Moral</a>. Para a discussão de cada posição, veja o <a href="../circulo-moral.html">círculo moral</a> e as <a href="../teorias.html">teorias</a>.</p>''')
    dv = json.dumps(VEU, ensure_ascii=False).replace('</', '<\\/')
    fp('veu-da-ignorancia', 'Simulador do véu da ignorância', 'Escolha uma sociedade sem saber quem você será nela. Depois, nasça algumas vezes e veja.', f'''<div id="veu" class="quiz" style="margin-top:0"><label class="campo">Sociedade<select id="veu-soc"></select></label><p id="veu-desc" class="fb"></p><div class="tabela"><table><thead><tr><th>Posição</th><th>Chance de nascer</th><th>Bem-estar (0 a 100)</th></tr></thead><tbody id="veu-tab"></tbody></table></div><p class="fb">Bem-estar médio: <strong id="veu-media"></strong> · Pior posição: <strong id="veu-pior"></strong></p><label class="chk"><input type="checkbox" id="veu-esp"/> <span><strong>Esconder também a espécie</strong><br/><small>Como propôs Mark Rowlands: você pode nascer humano ou um dos animais que a sociedade cria. As chances seguem, de longe, a proporção real.</small></span></label><div class="cta"><button class="btn" type="button" id="veu-nascer">Nascer</button><button class="btn alt" type="button" id="veu-zera">Zerar</button></div><p class="q" id="veu-res"></p><p class="fb" id="veu-hist"></p></div><script type="application/json" id="dados-veu">{dv}</script><p class="legenda">Números ilustrativos, escolhidos para o exercício. Pelo valor esperado, a Sociedade A vence; pelo maximin de Rawls, a D. Sem saber quem seria, qual você escolhe? E a escolha muda quando a espécie entra no véu? <a href="../contratualismo.html">Leia sobre o contratualismo</a>.</p>''')
    fp('quem-disse', 'Quem disse?', 'Dezesseis ideias, dezesseis filósofos. Ligue cada tese a quem a defendeu.', JOGO + dj(dict(tipo='opcoes', ops=QUEM_OPS, itens=[list(x) for x in QUEM])) + '<p class="legenda">Frases entre aspas são citações aproximadas; as outras, resumos. <a href="../filosofos.html">Veja os perfis</a>.</p>')
    der = json.dumps(dict(casos=ER_CASOS, principios=ER_PRINCIPIOS, pares=ER_PARES), ensure_ascii=False).replace('</', '<\\/')
    fp('equilibrio-reflexivo', 'Exercício de equilíbrio reflexivo', 'Julgue oito casos. Depois, veja que princípio mais concorda com você, e onde seus juízos se contradizem.', f'<div id="er" class="quiz" style="margin-top:0"><div class="alvo"></div><button class="btn prox-q" type="button" style="margin-top:12px" hidden>Próximo caso</button></div><script type="application/json" id="dados-er">{der}</script><p class="legenda">Não há respostas certas aqui: o exercício mede a coerência entre seus juízos e um princípio. <a href="../argumentos-morais.html">Leia sobre o equilíbrio reflexivo</a>.</p>')
    fp('teste-de-troca', 'Teste de troca', 'O mesmo ato, dois autores. Se o seu veredito muda, descubra qual diferença o justifica.', f'<div id="troca" class="quiz" style="margin-top:0"><div class="cena"></div><div class="ops"></div><p class="fb" role="status"></p><button class="btn prox-q" type="button" style="margin-top:12px" hidden>Próxima situação</button></div><script type="application/json" id="dados-troca">{json.dumps([list(x) for x in TROCA], ensure_ascii=False).replace("</", "<\\/")}</script><p class="legenda">Não há resposta certa para cada frase. O teste mede só a coerência entre os dois vereditos. <a href="../imparcialidade.html">Leia sobre imparcialidade</a> e <a href="../tribalismo-moral.html">tribalismo moral</a>.</p>')

# ---------- biblioteca, sites, sobre ----------
def biblioteca():
    n_cls = {'Iniciante': 'iniciante', 'Intermediário': 'intermediario', 'Avançado': 'avancado'}
    cls = lambda n: n_cls.get(n, 'ferr')
    cart = lambda t, a, d, n, u: f'<a class="cartao" href="{e(u)}" {EXT}><span class="tipo {cls(n)}">{e(n)}</span><h3 class="ext" style="margin-top:.3rem">{e(t)}</h3><p><em>{e(a)}</em></p><p>{e(d)}</p></a>'
    NIV_L = SECOES_L
    li = ''.join(f'<h2 class="grupo">{n} <small>({sum(1 for x in LIVROS if x[3] == n)})</small></h2><p>{d}</p><div class="grade">' + ''.join(cart(*x) for x in LIVROS if x[3] == n) + '</div>' for n, d in NIV_L)
    corpo = cabeca('Fontes', 'Biblioteca', f'{len(LIVROS)} livros para entender ética: três níveis de dificuldade e três seções temáticas.') + f'<div class="wrap secao">{li}<p class="legenda">Os links levam a uma busca pelo livro; alguns títulos têm edição gratuita indicada. Procura sites em vez de livros? Veja a <a href="sites.html">biblioteca de sites sobre ética</a>.</p></div>'
    page('biblioteca.html', 'Biblioteca', 'Livros recomendados sobre ética, por nível e por tema: de Rachels e Singer a Parfit, Regan, Ord e Baumann.', corpo, atual='biblioteca.html')

def sites_pub():
    gr = ''
    for g in GRUPOS_S:
        its = [s for s in SITES if s[3] == g]
        gr += f'<section><h2 class="grupo">{e(g)} <small>({len(its)})</small></h2><div class="grade">' + ''.join(f'<a class="cartao" href="{e(u)}" {EXT}><span class="tipo {"iniciante" if amb == NAC else "ferr"}">{e(amb)}</span><h3 class="ext" style="margin-top:.3rem">{e(n)}</h3><p>{e(dd)}</p></a>' for n, u, dd, _, amb in its) + '</div></section>'
    corpo = cabeca('Fontes', 'Biblioteca de sites sobre ética', 'Enciclopédias, organizações, testes e ferramentas para continuar por conta própria.')
    corpo += f'<div class="wrap secao"><div class="nota alerta" style="margin-top:0">Nenhum site é neutro. Enciclopédias revisadas por pares são o ponto de partida mais seguro; organizações têm causa declarada, o que não as torna erradas, mas pede leitura atenta.</div>{gr}<p class="legenda">Veja também a <a href="biblioteca.html">biblioteca de livros</a>.</p></div>'
    page('sites.html', 'Biblioteca de sites sobre ética', 'Enciclopédias de filosofia, organizações de ética animal e altruísmo eficaz, testes e ferramentas, em português e inglês.', corpo, atual='sites.html')

def privacidade():
    corpo = cabeca('Sobre', 'Política de privacidade', 'Em resumo: não há cadastro, não usamos cookies próprios nem ferramentas de análise de visitas.') + '''<div class="wrap estreito leitura secao"><p class="abre">Esta página explica quais dados podem ser tratados quando você usa o Ética Para Iniciantes, em linha com a Lei Geral de Proteção de Dados (LGPD, Lei 13.709/2018).</p>
<p><em>Última atualização: 3 de novembro de 2026.</em></p>
<h2>O que não fazemos</h2><ul><li>Não pedimos cadastro, login ou pagamento.</li><li>Não há formulário que envie seus dados para nós.</li><li>Não usamos cookies próprios, publicidade ou ferramentas de análise de visitas.</li><li>Não vendemos nem compartilhamos dados pessoais.</li></ul>
<h2>O que fica no seu navegador</h2><p>O recurso “Marcar como lida” usa o armazenamento local (<em>localStorage</em>) do seu aparelho para guardar a lista de lições que você marcou. Essa informação não é enviada para nós. As respostas às ferramentas e aos testes rápidos não são guardadas em lugar nenhum.</p>
<p>Para apagar, limpe os dados deste site nas configurações do navegador. Em aparelhos compartilhados, outras pessoas podem ver essas marcações.</p>
<h2>Serviços de terceiros</h2><p>Como em qualquer site, seu navegador envia dados técnicos, como endereço IP e tipo de navegador, aos serviços que entregam as páginas e arquivos:</p>
<div class="tabela"><table><thead><tr><th>Serviço</th><th>Para quê</th></tr></thead><tbody><tr><td>Hospedagem do site</td><td>Entregar as páginas. O provedor pode manter registros técnicos de acesso</td></tr><tr><td><a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google Fonts</a></td><td>Carregar as fontes do site</td></tr><tr><td><a href="https://biblioverse.org">BiblioVerse</a></td><td>Carregar a barra superior com as bibliotecas da BiblioVerse</td></tr></tbody></table></div>
<h2>Links externos</h2><p>Indicamos fontes, livros e testes em outros sites, como o Teste de Visão Moral. Ao acessá-los, valem as regras de privacidade de cada um.</p>
<h2>Crianças e adolescentes</h2><p>O site é educativo e não pede dados pessoais a pessoas de nenhuma idade.</p>
<h2>Seus direitos</h2><p>A LGPD garante direitos como acesso, correção e eliminação de dados pessoais. Como não mantemos cadastro nem guardamos o que você faz aqui, em geral não temos dados que permitam identificar você. O que está no seu aparelho fica sob seu controle.</p>
<h2>Mudanças</h2><p>Se o funcionamento do site mudar, por exemplo com novas ferramentas ou serviços, esta página será atualizada, com nova data.</p></div>'''
    page('privacidade.html', 'Política de privacidade', 'Quais dados podem ser tratados ao usar o Ética Para Iniciantes, e o que fica só no seu navegador.', corpo)

def sobre():
    corpo = cabeca('Sobre', 'Sobre este projeto') + f'''<div class="wrap estreito leitura secao"><p class="abre">Um guia para quem quer entender ética sem precisar escolher uma teoria antes.</p>
<h2>Posição editorial</h2><p>O site não defende uma teoria como a única certa, mas reconhece que a neutralidade total não existe. Partimos de algumas posições: valores e fatos devem ser separados; a imparcialidade é o melhor teste de uma visão moral; todos os que podem sofrer devem ter seus interesses considerados; e as teorias se distinguem pelo que colocam no centro, não pelo que ignoram. Quando um tema está em aberto, apresentamos os lados e dizemos onde o peso da razão parece estar, com a ressalva de que isso pode ser contestado.</p>
<h2>Como apresentamos as teorias</h2><p>Cada teoria aparece pelo seu <em>ponto focal</em>: o que mais deve pesar para ela. Dizer que o consequencialismo foca nos resultados não quer dizer que ignore regras, nem que a deontologia ignore resultados. Evitamos caricaturas, e cada página traz os pontos fortes antes das objeções.</p>
<h2>Como apuramos</h2><p>Usamos a Stanford Encyclopedia of Philosophy, a Internet Encyclopedia of Philosophy, a Wikipédia e as obras originais, indicadas ao fim de cada página. A estrutura das teorias e do círculo moral segue o <a href="https://ethicstest.biblioverse.org/map.html" {EXT}>mapa do Teste de Visão Moral</a>. Números sobre animais vêm da FAO e de estimativas acadêmicas citadas. Ao ver um erro, mande a correção com a fonte.</p>
<h2>Seus dados</h2><p>Não há cadastro. Lições lidas ficam só no seu navegador. Veja a <a href="privacidade.html">política de privacidade</a>.</p>
<h2>Parte da BiblioVerse</h2><p>Este site faz parte da <a href="https://biblioverse.org">BiblioVerse</a>, ao lado do <a href="https://politicaparainiciantes.biblioverse.org/" {EXT}>Política Para Iniciantes</a>, do <a href="https://ethicstest.biblioverse.org/" {EXT}>Teste de Visão Moral</a>, do <a href="https://guiadeargumentacao.biblioverse.org/" {EXT}>Guia de Argumentação</a> e do <a href="https://ethicalfood.biblioverse.org/pt/" {EXT}>Guia de Alimentos Éticos</a>.</p></div>'''
    page('sobre.html', 'Sobre', 'Posição editorial e método do Ética Para Iniciantes: como as teorias são apresentadas e de onde vêm as fontes.', corpo, atual='sobre.html')

def arquivos():
    w = lambda n, t: open(os.path.join(ROOT, n), 'w', encoding='utf-8', newline='\n').write(t)
    w('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{SITE}/{"" if u == "index.html" else u}</loc><lastmod>{ATUALIZADO}</lastmod></url>\n' for u in sorted(set(PAGINAS) - {'404.html'})) + '</urlset>\n')
    w('llms.txt', f'# {NOME}\n\n> Guia gratuito de ética em português, em três níveis, com fontes: teorias normativas, círculo moral, metaética, ética animal, dilemas clássicos e filósofos.\n\n## Principais seções\n\n- [Comece aqui]({SITE}/comece-aqui.html)\n- [Catálogo de lições]({SITE}/catalogo.html)\n- [Trilhas por tema]({SITE}/trilhas.html)\n- [Minha posição]({SITE}/minha-posicao.html)\n- [Teorias éticas]({SITE}/teorias.html)\n- [Critérios éticos]({SITE}/criterios.html)\n- [Metaética]({SITE}/metaetica.html)\n- [Dilemas clássicos]({SITE}/dilemas.html)\n- [Debates éticos]({SITE}/debates.html)\n- [Filósofos morais]({SITE}/filosofos.html)\n- [Glossário]({SITE}/glossario.html)\n- [Ferramentas]({SITE}/ferramentas.html)\n- [Biblioteca]({SITE}/biblioteca.html)\n- [Sites sobre ética]({SITE}/sites.html)\n- [Sobre e método]({SITE}/sobre.html)\n')
    w('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    w('CNAME', 'eticaparainiciantes.biblioverse.org\n')
    w('.nojekyll', '')
    w('.gitignore', '__pycache__/\n')
    w('manifest.webmanifest', json.dumps(dict(name=NOME, short_name='Ética', start_url='/', display='standalone', background_color='#f9f8f4', theme_color='#1f5a4c', icons=[dict(src='assets/icon.svg', sizes='any', type='image/svg+xml'), dict(src='assets/icon-192.png', sizes='192x192', type='image/png'), dict(src='assets/icon-512.png', sizes='512x512', type='image/png')]), ensure_ascii=False))
    w('assets/icon.svg', arte.LOGO.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"'))
    busca = [dict(t=l['titulo'], d=l['nivel_rot'] + ' · ' + l['resumo'], u=l['slug'] + '.html') for l in TODAS] + [dict(t=t['n'], d='Teoria · ' + t['r'], u=f'teorias/{t["s"]}.html') for t in TEO] + [dict(t=d['n'], d='Dilema · ' + d['r'], u=f'dilemas/{d["s"]}.html') for d in DILEMAS] + [dict(t=d['n'], d='Debate · ' + d['r'], u=f'debates/{d["s"]}.html') for d in DEBATES] + [dict(t='Trilhas por tema', d='Sete caminhos curtos de estudo', u='trilhas.html'), dict(t='Minha posição', d='Monte sua visão moral em cinco escolhas', u='minha-posicao.html'), dict(t='Critérios éticos', d='Quem conta, e se há um padrão comum', u='criterios.html'), dict(t='Metaética', d='O que é um juízo moral', u='metaetica.html'), dict(t='Debates éticos', d='As perspectivas e onde a razão pesa', u='debates.html')] + [dict(t=f['nome'], d=f'{f["anos"]} · {f["quem"]}', u=f'filosofos/{f["slug"]}.html') for f in FIL] + [dict(t=f[1], d='Ferramenta · ' + f[2], u=f'ferramentas/{f[0]}.html') for f in FERR] + [dict(t=t, d='Glossário · ' + d[:90], u='glossario.html') for _, t, d, _ in GLOSSARIO] + [dict(t='Teorias éticas', d='O mapa das teorias e o comparador', u='teorias.html'), dict(t='Dilemas clássicos', d='Experimentos mentais e o que cada teoria diz', u='dilemas.html'), dict(t='Filósofos morais', d='De Platão a Singer', u='filosofos.html'), dict(t='Biblioteca', d='Livros por nível', u='biblioteca.html'), dict(t='Sites sobre ética', d='Enciclopédias, organizações e ferramentas', u='sites.html')]
    w('assets/busca.json', json.dumps(busca, ensure_ascii=False))
    page('404.html', 'Página não encontrada', 'Esta página não existe.', cabeca('Erro 404', 'Página não encontrada', 'Volte para o <a href="/" style="color:#fff">início</a> ou use a busca.'))

os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
def minifica():
    import hashlib
    try:
        import rcssmin, rjsmin
        cm, jm = rcssmin.cssmin, rjsmin.jsmin
    except ImportError:
        cm = jm = lambda s: s
    css = open(os.path.join(ROOT, 'assets', 'style.css'), encoding='utf-8').read(); js = open(os.path.join(ROOT, 'assets', 'app.js'), encoding='utf-8').read()
    open(os.path.join(ROOT, 'assets', 'style.min.css'), 'w', encoding='utf-8', newline='\n').write(cm(css))
    open(os.path.join(ROOT, 'assets', 'app.min.js'), 'w', encoding='utf-8', newline='\n').write(jm(js))
    return hashlib.sha1((css + js).encode()).hexdigest()[:8]
VERSAO = minifica()
inicio(); comece(); catalogo(); trilhas(); minha_posicao()
for s, r, ls, t, d, g in NIVEIS:
    nivel(s, r, ls, t, d, g); teste_nivel(s, r, ls); revisao(s, r, ls)
    for l in ls: licao(l, ls)
teorias(); dilemas_pub(); debates_pub(); filosofos(); glossario(); ferramentas(); biblioteca(); sites_pub(); sobre(); privacidade(); arquivos()
print(f'{len(TODAS)} lições, {len(TEO)} teorias, {len(DILEMAS)} dilemas, {len(DEBATES)} debates, {len(FIL)} filósofos, {len(FERR)} ferramentas, {len(PAGINAS)} páginas.')
