"""Lições do nível Avançado: metaética, as fronteiras do círculo, decidir sem certeza, progresso e abertura."""
from licoes_iniciante import SEP, IEP, WP, WE, TESTE, MAPA, VINDING, SINGER_PE
PARFIT = ('Reasons and Persons', 'https://www.google.com/search?tbm=bks&q=Parfit+Reasons+and+Persons')
OWM = ('On What Matters', 'https://www.google.com/search?tbm=bks&q=Parfit+On+What+Matters')

AVANCADO = [
dict(slug='o-que-e-metaetica', grupo='Metaética', titulo='O que é metaética: fatos morais existem?', resumo='Quando digo que a tortura é errada, descrevo um fato, expresso um sentimento ou dou uma ordem? O mapa das respostas.', corpo='''
<p class="abre">A ética normativa pergunta o que é certo. A metaética pergunta o que estamos fazendo quando dizemos que algo é certo: há fatos morais, como há fatos físicos? Eles dependem de nós? Como os conhecemos? As respostas se dividem em três grandes posições.</p>
<h2>As três perguntas</h2>
<table><thead><tr><th>Pergunta</th><th>Nome técnico</th><th>Exemplo</th></tr></thead><tbody>
<tr><td>Juízos morais podem ser verdadeiros ou falsos?</td><td>Semântica: cognitivismo ou não</td><td>“Torturar é errado” é como “a água ferve a 100 graus” ou como “viva o time”?</td></tr>
<tr><td>Se podem, existem fatos que os tornam verdadeiros?</td><td>Ontologia: realismo ou antirrealismo</td><td>Há algo no mundo que faz a tortura ser errada, independentemente de qualquer opinião?</td></tr>
<tr><td>Como conhecemos esses fatos?</td><td>Epistemologia</td><td>Por observação, por intuição racional, por acordo?</td></tr>
</tbody></table>
<h2>O mapa</h2>
<div class="tres">
<div><h3>Realismo moral</h3><p>Existem fatos morais objetivos, independentes do que qualquer pessoa ou cultura pensa. Alguns juízos morais são verdadeiros, e descobrimos quais.</p><p class="pol">Variantes: <a href="teorias/realismo-naturalista.html">naturalista</a> e <a href="teorias/realismo-nao-naturalista.html">não naturalista</a>.</p></div>
<div><h3>Antirrealismo moral</h3><p>Não existem fatos morais objetivos. Ou os juízos são relativos a um referencial, ou são todos falsos, ou não são o tipo de coisa que pode ser verdadeira.</p><p class="pol">Variantes: <a href="teorias/relativismo-metaetico.html">relativismo</a>, <a href="teorias/teoria-do-erro.html">teoria do erro</a>, <a href="teorias/emotivismo.html">emotivismo</a>, <a href="teorias/prescritivismo.html">prescritivismo</a>, <a href="teorias/quase-realismo.html">quase-realismo</a>.</p></div>
<div><h3>Quietismo</h3><p>A pergunta está mal colocada. Perguntar se fatos morais são “independentes da mente” confunde a moral com a física. Aceite a prática moral como ela funciona, sem fundamentos de fora.</p><p class="pol">Veja o <a href="teorias/quietismo-metaetico.html">quietismo</a>.</p></div>
</div>
<h2>Por que isso importa</h2>
<p>Parece abstrato, mas tem efeitos práticos:</p>
<ul>
<li><strong>Se não há fatos morais,</strong> dizer que a escravidão era errada seria expressar uma preferência, e não corrigir um erro. Muitos antirrealistas aceitam isso com ressalvas, e explicam por que ainda vale a pena argumentar.</li>
<li><strong>Se há fatos morais,</strong> podemos estar errados sobre eles, do mesmo jeito que estávamos errados sobre a Terra ser plana. A ética vira uma investigação, com progresso possível.</li>
<li><strong>A conversa muda:</strong> um realista discute como quem busca a verdade; um emotivista, como quem tenta mudar atitudes; um relativista, como quem compara referenciais.</li>
</ul>
<h2>Um teste simples</h2>
<p>Pense na frase: “se todos aprovassem a tortura de crianças por diversão, ela seria aceitável”. Se a sua reação é “não, continuaria errada”, você tem uma intuição realista. Se é “a frase não faz sentido, porque não haveria quem a julgasse”, você se aproxima do antirrealismo ou do quietismo. Nenhuma das reações encerra o debate, mas as duas revelam de onde você parte.</p>
<h2>O que a metaética não decide</h2>
<p>Ela não diz o que fazer. Dois realistas podem ser um utilitarista e um kantiano; dois emotivistas podem discordar sobre tudo. E, como lembra o <a href="https://ethicstest.biblioverse.org/map.html" target="_blank" rel="noopener">Teste de Visão Moral</a>, até o cético tem uma tendência prática. A metaética esclarece o que está em jogo quando discutimos; não substitui a discussão.</p>
<div class="nota"><strong>Para guardar:</strong> a metaética pergunta sobre o estatuto da moral, não sobre o conteúdo. As próximas lições percorrem as respostas, de quem acha que há fatos morais a quem acha que a pergunta não faz sentido.</div>
''', fontes=[('Metaethics (Stanford Encyclopedia)', SEP + 'metaethics/'), ('Metaética (Wikipédia)', WP + 'Meta%C3%A9tica'), ('Metaethics (Internet Encyclopedia of Philosophy)', IEP + 'metaethi/'), MAPA]),

dict(slug='realismo-moral', grupo='Metaética', titulo='Realismo moral: naturalistas e não naturalistas', resumo='Se fatos morais existem, do que são feitos e como os descobrimos? Duas respostas, e os argumentos que as sustentam.', corpo='''
<p class="abre">O realismo moral afirma que alguns juízos morais são verdadeiros, e são verdadeiros por causa de fatos que não dependem de opinião. Que a tortura por diversão é errada seria um fato como o de que a água ferve a 100 graus: podemos ignorá-lo, mas não mudá-lo. Os realistas discordam sobre que tipo de fato é esse.</p>
<h2>Realismo naturalista</h2>
<p>Fatos morais são fatos naturais, redutíveis a propriedades que a ciência pode estudar: bem-estar, sofrimento, florescimento, cooperação. “Isso é errado” significa algo como “isso causa sofrimento sem compensação” ou “isso frustra o florescimento”. Autores: Richard Boyd, David Brink e Nicholas Sturgeon (o “realismo de Cornell”), Peter Railton (naturalismo redutivo) e Philippa Foot (a bondade de um ser humano é como a boa saúde de uma planta: um fato sobre o que o faz funcionar bem). A vantagem é encaixar a moral no mundo que conhecemos. A desvantagem é o <strong>argumento da questão em aberto</strong> de G. E. Moore: para qualquer propriedade natural N, faz sentido perguntar “N é bom?”, o que mostra que “bom” não significa N. Veja o <a href="teorias/realismo-naturalista.html">realismo naturalista</a>.</p>
<h2>Realismo não naturalista</h2>
<p>Fatos morais são de um tipo próprio, irredutível, como os fatos matemáticos: não estão no espaço, não têm causa, e ainda assim há verdades sobre eles. Que dois mais dois são quatro não é um fato físico, e não deixa de ser um fato. Moore, W. D. Ross e, recentemente, Derek Parfit, Thomas Nagel e David Enoch defendem alguma versão. Veja o <a href="teorias/realismo-nao-naturalista.html">realismo não naturalista</a>.</p>
<h2>Como conhecemos: o intuicionismo</h2>
<p>Se fatos morais não são empíricos, como os descobrimos? A resposta não naturalista é a <strong>intuição racional</strong>: certas proposições são autoevidentes a quem as entende bem, como axiomas. “Sofrimento, em si, é ruim” seria uma delas. Não é um sentimento, e sim uma apreensão intelectual, do tipo que temos ao ver que se A é maior que B e B maior que C, então A é maior que C. Críticos perguntam por que intuições morais conflitam tanto entre pessoas; defensores respondem que intuições matemáticas também erraram e foram corrigidas.</p>
<h2>Os argumentos a favor do realismo</h2>
<ul>
<li><strong>A aparência:</strong> a experiência moral se parece com descobrir, não com inventar. Quem muda de ideia sobre a escravidão sente que aprendeu algo, não que trocou de gosto.</li>
<li><strong>O argumento da convergência:</strong> em condições de informação, imparcialidade e reflexão, as pessoas tendem a concordar em muito: dor é ruim, casos iguais pedem tratamento igual. Isso sugere que estão respondendo a algo.</li>
<li><strong>A paridade com a matemática e a lógica:</strong> rejeitar verdades normativas por não serem empíricas exigiria rejeitar também a lógica, que diz o que <em>devemos</em> inferir. Parfit e Enoch exploram isso.</li>
<li><strong>O custo do antirrealismo:</strong> se nada é mesmo errado, o genocídio não é mesmo errado. Muitos acham isso mais implausível do que qualquer problema do realismo.</li>
</ul>
<h2>Os argumentos contra</h2>
<ul>
<li><strong>Estranheza:</strong> J. L. Mackie perguntou que tipo de coisa seria um fato que, só por ser conhecido, nos obriga a agir. Nada no mundo físico funciona assim.</li>
<li><strong>Desacordo:</strong> se há fatos, por que tanta divergência persistente? Realistas respondem que boa parte do desacordo é sobre fatos não morais e sobre quem conta, e que diminui com informação.</li>
<li><strong>Desmascaramento evolutivo:</strong> nossas intuições foram moldadas pela seleção natural para sobreviver, não para rastrear verdades morais. Veja <a href="evolucao-e-moral.html">evolução e moral</a>.</li>
<li><strong>Economia:</strong> dá para explicar toda a prática moral sem supor fatos extras. Por que supô-los?</li>
</ul>
<h2>A convergência de Parfit</h2>
<p>Em <em>On What Matters</em>, Derek Parfit tentou mostrar que kantianos, contratualistas e consequencialistas, bem entendidos, “escalam a mesma montanha por lados diferentes” e chegam a conclusões muito próximas. Se tiver razão, isso é um argumento forte a favor do realismo: teorias independentes convergindo é o que esperaríamos se houvesse algo a descobrir.</p>
<div class="nota"><strong>Para guardar:</strong> o realismo paga um preço metafísico (admitir fatos que não são físicos) para preservar a ideia de que a moral pode estar certa ou errada. Os antirrealistas, na próxima lição, pagam o preço inverso.</div>
''', fontes=[('Moral Realism (Stanford Encyclopedia)', SEP + 'moral-realism/'), ('Moral Non-Naturalism (Stanford Encyclopedia)', SEP + 'moral-non-naturalism/'), ('Moral Naturalism (Stanford Encyclopedia)', SEP + 'naturalism-moral/'), OWM]),

dict(slug='antirrealismo-moral', grupo='Metaética', titulo='Antirrealismo moral: erro, emotivismo e quase-realismo', resumo='Se não há fatos morais, o que fazemos quando dizemos que algo é errado? Quatro respostas, da mais radical à mais conciliadora.', corpo='''
<p class="abre">Os antirrealistas negam que haja fatos morais independentes de nós. Mas discordam sobre o que a linguagem moral faz. Alguns dizem que ela tenta descrever fatos e falha; outros, que ela nunca tentou descrever nada: expressa, prescreve, recomenda.</p>
<h2>Teoria do erro</h2>
<p>J. L. Mackie, em <em>Ética: Inventando o Certo e o Errado</em> (1977), aceitou que a linguagem moral comum pretende descrever fatos objetivos e vinculantes, e concluiu que ela erra: não há tais fatos. Todo juízo moral é, estritamente, falso, como todo juízo sobre bruxas. Dois argumentos: o da <strong>relatividade</strong> (a variação moral entre culturas se explica melhor por modos de vida do que por percepções diferentes de um fato) e o da <strong>estranheza</strong> (fatos que obrigam por si mesmos não se parecem com nada que conhecemos). Mackie não achava que isso liberasse ninguém: a moral é uma invenção útil, e devemos continuar inventando bem. Veja a <a href="teorias/teoria-do-erro.html">teoria do erro</a>.</p>
<h2>Emotivismo</h2>
<p>A. J. Ayer e Charles Stevenson, nos anos 1930 e 1940, disseram que juízos morais não descrevem nada, nem falsamente. Eles <em>expressam</em> atitudes: “matar é errado” equivale a “matar, buuu!”, com a função de influenciar os outros. Não são verdadeiros nem falsos, como um grito não é. A vantagem é explicar por que a moral motiva: ela é emoção expressa. A desvantagem é o <strong>problema de Frege-Geach</strong>: a frase “se matar é errado, mandar matar é errado” não expressa emoção alguma, e ainda assim faz sentido e entra em argumentos válidos. Veja o <a href="teorias/emotivismo.html">emotivismo</a>.</p>
<h2>Prescritivismo</h2>
<p>R. M. Hare refinou a ideia: juízos morais são <em>prescrições</em>, comandos, mas de um tipo especial: universalizáveis. Dizer que algo é errado é prescrever que ninguém o faça, em qualquer situação igual, inclusive eu. Isso dá lógica à moral (prescrições podem ser consistentes ou não) sem supor fatos. E tem uma consequência normativa: levar a sério a universalização, para Hare, leva ao utilitarismo, porque é preciso pesar as preferências de todos como se fossem as próprias. Veja o <a href="teorias/prescritivismo.html">prescritivismo</a>.</p>
<h2>Quase-realismo</h2>
<p>Simon Blackburn aceitou que juízos morais expressam atitudes, e tentou mostrar que, mesmo assim, temos direito a falar como realistas: dizer que a escravidão “era errada mesmo quando todos a aprovavam”, que podemos estar enganados, que há progresso. O truque é que essas frases expressam atitudes de segunda ordem: atitudes sobre as nossas atitudes. Os críticos perguntam se, no fim, o quase-realista acredita ou não que a tortura é errada. Blackburn responde: acredito, e isso é uma atitude. Veja o <a href="teorias/quase-realismo.html">quase-realismo</a>.</p>
<table><thead><tr><th>Posição</th><th>Juízos morais são…</th><th>Podem ser verdadeiros?</th><th>Problema principal</th></tr></thead><tbody>
<tr><td>Teoria do erro</td><td>Tentativas de descrever fatos que não existem</td><td>Não; todos falsos</td><td>Como seguir levando a moral a sério?</td></tr>
<tr><td>Emotivismo</td><td>Expressões de emoção</td><td>Não se aplica</td><td>Não explica argumentos morais (Frege-Geach)</td></tr>
<tr><td>Prescritivismo</td><td>Comandos universalizáveis</td><td>Não se aplica, mas há consistência</td><td>Um fanático consistente passaria no teste</td></tr>
<tr><td>Quase-realismo</td><td>Atitudes, com direito a falar como realista</td><td>“Sim”, em sentido deflacionado</td><td>Parece realismo com outro nome</td></tr>
</tbody></table>
<h2>O que os antirrealistas acertam</h2>
<ul>
<li><strong>A moral motiva:</strong> saber que algo é errado move à ação de um jeito que saber que a água ferve a 100 graus não move. Expressivismo explica isso bem.</li>
<li><strong>A conexão com o desejo:</strong> David Hume já havia notado que a razão sozinha não motiva; precisa de uma paixão. Antirrealistas levam isso a sério.</li>
<li><strong>Economia:</strong> não precisam de fatos estranhos.</li>
</ul>
<h2>O que custam</h2>
<p>Se nada é errado em sentido pleno, a frase “o genocídio seria errado mesmo que todos o aprovassem” precisa de uma reinterpretação. Os antirrealistas sofisticados oferecem uma. Se ela convence, é uma questão que divide a filosofia até hoje. O que quase todos concordam é que a <em>prática</em> moral, argumentar, criticar, mudar de ideia, continua fazendo sentido em qualquer das posições.</p>
''', fontes=[('Moral Anti-Realism (Stanford Encyclopedia)', SEP + 'moral-anti-realism/'), ('Ethics: Inventing Right and Wrong', 'https://www.google.com/search?tbm=bks&q=Mackie+Ethics+Inventing+Right+and+Wrong'), ('Moral Cognitivism vs. Non-Cognitivism (Stanford Encyclopedia)', SEP + 'moral-cognitivism/'), ('Ruling Passions', 'https://www.google.com/search?tbm=bks&q=Blackburn+Ruling+Passions')]),

dict(slug='relativismo-e-quietismo', grupo='Metaética', titulo='Relativismo metaético e quietismo', resumo='A verdade moral depende do referencial, ou a pergunta sobre fatos morais é que está mal feita? Duas saídas, com problemas diferentes.', corpo='''
<p class="abre">O relativismo metaético diz que juízos morais são verdadeiros ou falsos, mas só dentro de um referencial, cultural ou pessoal. O quietismo diz que a pergunta inteira, sobre haver ou não fatos morais “lá fora”, é um erro de gramática filosófica. As duas tentam escapar da disputa entre realistas e antirrealistas.</p>
<h2>Relativismo metaético</h2>
<p>Diferente do <a href="egoismo-relativismo-e-ceticismo.html">relativismo normativo</a> visto no Iniciante (“não julgue outras culturas”), o metaético é uma tese sobre a verdade: “X é errado” é como “X é ilegal”, verdadeiro em relação a um código, sem sentido fora de um. Gilbert Harman defendeu uma versão sofisticada: juízos morais pressupõem um acordo implícito entre quem fala e quem ouve, e só valem dentro dele.</p>
<p>O que o relativismo acerta: a variação moral entre culturas é real, e muitos de nossos juízos dependem de um pano de fundo que não escolhemos. O que custa:</p>
<ul>
<li><strong>Perde o desacordo:</strong> se “a escravidão é errada” é verdadeiro para mim e “é aceitável” é verdadeiro para o escravocrata, não estamos discordando: estamos falando de referenciais diferentes, como quem diz “é tarde” em fusos horários diferentes. Mas a disputa moral parece ser um desacordo real.</li>
<li><strong>Quem define o referencial?</strong> Dentro de qualquer cultura há dissidentes, e quase sempre são as vítimas. O relativismo tende a dar a última palavra a quem manda.</li>
<li><strong>Autorrefutação:</strong> “toda verdade moral é relativa” é uma afirmação que pretende valer para todos. Veja o <a href="teorias/relativismo-metaetico.html">relativismo metaético</a>.</li>
</ul>
<h2>Quietismo</h2>
<p>Inspirado em Ludwig Wittgenstein, o quietista diz que perguntar se fatos morais são “independentes da mente” importa um modelo da física para onde ele não cabe. A prática moral funciona: damos razões, corrigimos erros, convencemos e somos convencidos. Perguntar o que “fundamenta” isso de fora é como perguntar o que fundamenta a matemática fora da matemática: a pergunta não tem para onde ir.</p>
<p>Ronald Dworkin, em <em>Justiça para Porcos-Espinhos</em>, defendeu que a única forma de responder a uma pergunta moral é com um argumento moral: nenhuma descoberta sobre a natureza dos fatos pode mostrar que a tortura é aceitável. Thomas Scanlon e John McDowell têm posições próximas, às vezes chamadas de realismo “relaxado”.</p>
<table><thead><tr><th>Quietismo acerta</th><th>Quietismo custa</th></tr></thead><tbody>
<tr><td>A moral não precisa de aval da física para funcionar</td><td>Parece recusar uma pergunta legítima, em vez de respondê-la</td></tr>
<tr><td>Argumentos morais só se respondem com argumentos morais</td><td>Não explica por que a moral motiva, nem de onde vem o desacordo</td></tr>
<tr><td>Evita a metafísica estranha do realismo e o niilismo da teoria do erro</td><td>Críticos dizem que é realismo sem coragem, ou antirrealismo sem honestidade</td></tr>
</tbody></table>
<h2>O que isso muda na prática</h2>
<p>Pouco, e isso é o ponto dos quietistas. Em qualquer das posições, continua fazendo sentido perguntar se uma prática causa sofrimento, se trata casos iguais igualmente, se resistiria a quem a sofre. A metaética esclarece o que estamos fazendo quando perguntamos; não muda as perguntas. Mas há uma diferença de atitude: quem acha que pode estar errado investiga; quem acha que “é tudo relativo” para de investigar. Veja o <a href="teorias/quietismo-metaetico.html">quietismo metaético</a>.</p>
<div class="nota"><strong>Para guardar:</strong> o relativismo metaético paga com a perda do desacordo real. O quietismo paga com a recusa da pergunta. Se algum dos preços vale a pena, é o que o debate decide.</div>
''', fontes=[('Moral Relativism (Stanford Encyclopedia)', SEP + 'moral-relativism/'), ('Quietism (Wikipédia)', WE + 'Quietism_(philosophy)'), ('Justice for Hedgehogs', 'https://www.google.com/search?tbm=bks&q=Dworkin+Justice+for+Hedgehogs'), MAPA]),

dict(slug='evolucao-e-moral', grupo='Metaética', titulo='Evolução, desmascaramento e moral', resumo='Nossas intuições morais foram moldadas para sobreviver, não para achar a verdade. Isso as desmente? O argumento de Sharon Street e as respostas.', corpo='''
<p class="abre">A seleção natural moldou nossas emoções morais: cuidamos dos filhos, retribuímos favores, punimos trapaceiros, desconfiamos de estranhos. Tudo isso ajudou nossos ancestrais a sobreviver. A pergunta metaética é o que isso diz sobre a confiabilidade dessas intuições para descobrir o que é certo.</p>
<h2>A origem evolutiva da moral</h2>
<table><thead><tr><th>Disposição</th><th>Vantagem evolutiva</th><th>Intuição moral</th></tr></thead><tbody>
<tr><td>Cuidado parental</td><td>Filhos sobrevivem</td><td>Dever especial com os filhos</td></tr>
<tr><td>Reciprocidade</td><td>Cooperação repetida</td><td>Gratidão, justiça, punição de trapaceiros</td></tr>
<tr><td>Favoritismo de grupo</td><td>Coesão contra rivais</td><td>Lealdade, desconfiança do estranho</td></tr>
<tr><td>Nojo</td><td>Evitar contaminação</td><td>Juízos de pureza e impureza</td></tr>
<tr><td>Hierarquia</td><td>Ordem no grupo</td><td>Respeito à autoridade</td></tr>
</tbody></table>
<p>Frans de Waal mostrou raízes dessas disposições em outros primatas: empatia, consolo, senso de justiça. A moral humana é uma elaboração, com linguagem e cultura, de algo mais antigo.</p>
<h2>O dilema darwiniano de Street</h2>
<p>Sharon Street formulou em 2006 um argumento contra o realismo moral. Se há fatos morais independentes de nós, ou nossas intuições foram selecionadas <em>porque</em> rastreiam esses fatos, ou a coincidência entre o que a evolução favoreceu e o que é verdade seria um milagre. Mas a seleção natural não premia crenças verdadeiras: premia crenças que ajudam a sobreviver. Logo, para o realista, nossas intuições não têm por que ser confiáveis, e ele perde o acesso aos fatos que afirma. Para o antirrealista, não há problema: a moral <em>é</em> o conjunto de atitudes que a evolução e a cultura produziram, refinado pela reflexão.</p>
<h2>As respostas realistas</h2>
<ul>
<li><strong>Terceiro fator (Enoch, Wielenberg):</strong> a sobrevivência é, em geral, boa; então o que favorece a sobrevivência tende a coincidir com o que é bom, sem milagre. Street responde que isso já pressupõe um juízo moral.</li>
<li><strong>Desmascarar seletivamente (Singer, de Lazari-Radek):</strong> a evolução explica as intuições <em>parciais</em>: favoritismo de grupo, nojo, prioridade ao próximo. Mas não explica bem a intuição <em>imparcial</em> de que a dor de qualquer um conta igual, que não ajudava ninguém a sobreviver. Logo, essa intuição sobrevive ao desmascaramento, e as parciais não. O resultado é um argumento evolutivo a favor da imparcialidade.</li>
<li><strong>Paridade com a razão:</strong> a lógica e a matemática também evoluíram, e confiamos nelas. Se o desmascaramento derruba a moral, derruba tudo. Realistas acham isso um custo alto demais para o argumento.</li>
</ul>
<h2>O que fica, para todos</h2>
<p>Mesmo sem decidir a metaética, o argumento de Street deixa uma lição prática: intuições que têm uma explicação evolutiva clara e servem ao interesse do grupo merecem desconfiança. É o caso da parcialidade pelo próximo, do nojo e do tribalismo. Intuições que não se explicam por vantagem, como “o sofrimento de qualquer ser é ruim”, merecem mais confiança. Esse filtro move na direção da <a href="imparcialidade.html">imparcialidade</a> e da <a href="expansao-do-circulo-moral.html">expansão do círculo</a>.</p>
<h2>Explicar não é justificar</h2>
<p>Saber que o nojo evoluiu para evitar doença não torna o nojo um guia moral. Saber que a lealdade evoluiu para a guerra não a justifica. A evolução explica de onde vieram nossas reações; a ética pergunta se devemos segui-las. Confundir as duas é a <a href="fatos-e-valores.html">falácia naturalista</a> em versão darwiniana.</p>
<div class="nota"><strong>Para guardar:</strong> a mente moral veio pronta para um mundo de pequenas tribos. O trabalho da ética é descobrir que partes dessa herança merecem ser mantidas, e isso a evolução não pode responder por nós.</div>
''', fontes=[('A Darwinian Dilemma for Realist Theories of Value (2006)', 'https://doi.org/10.1007/s11098-005-1726-6'), ('Evolutionary Debunking Arguments (Wikipédia)', WE + 'Evolutionary_debunking_argument'), ('The Point of View of the Universe', 'https://www.google.com/search?tbm=bks&q=Lazari-Radek+Singer+The+Point+of+View+of+the+Universe'), ('Morality and Evolutionary Biology (Stanford Encyclopedia)', SEP + 'morality-biology/')]),

dict(slug='gradualismo', grupo='As fronteiras do círculo', titulo='Gradualismo: a inteligência muda o peso do sofrimento?', resumo='Uma dor igual conta igual em um humano e em um frango? O gradualista diz que capacidades cognitivas alteram o peso. O argumento dos casos marginais responde.', corpo='''
<p class="abre">Quem aceita que seres sencientes contam ainda precisa responder: contam igual? O gradualismo diz que o peso de um interesse depende de capacidades como inteligência, autoconsciência e planejamento. O não gradualismo diz que uma dor de mesma intensidade conta igual, seja de quem for.</p>
<h2>Duas perguntas que se confundem</h2>
<p>É preciso separar:</p>
<ol class="roteiro">
<li><strong>Capacidades mudam o que está em jogo?</strong> Sim, e ninguém discute. Um humano que morre perde planos, relações e um futuro antecipado; um peixe perde menos disso. Matar os dois não é igual, porque o <em>dano</em> não é igual.</li>
<li><strong>Capacidades mudam o peso de um dano igual?</strong> Esta é a pergunta do gradualismo. Se um humano e um porco sentem uma dor física de mesma intensidade e duração, a dor do humano conta mais?</li>
</ol>
<p>Muitos que se dizem gradualistas só aceitam a primeira. O gradualismo propriamente dito responde sim à segunda.</p>
<h2>O argumento gradualista</h2>
<p>Seres com mais capacidades têm vidas mais ricas, e seu sofrimento se liga a mais coisas: memória, antecipação, sentido. Um humano sofre também por saber que sofre. Além disso, dizem alguns, a complexidade da mente é em si fonte de valor, e o que acontece a uma mente complexa importa mais.</p>
<h2>O argumento dos casos marginais</h2>
<p>Se o peso de um interesse depende de inteligência, então humanos com menos capacidades (bebês, pessoas com deficiência cognitiva grave, pessoas em estágio avançado de demência) teriam interesses de menor peso do que os de um adulto típico. Quase ninguém aceita isso. E muitos animais adultos têm capacidades iguais ou superiores às de um bebê humano. Logo, ou aceitamos que esses humanos contam menos, ou abandonamos a inteligência como critério de peso. Veja <a href="dilemas/casos-marginais.html">o dilema</a>.</p>
<p>As respostas gradualistas: (a) o potencial do bebê conta, mas isso não cobre quem não tem potencial; (b) laços e pertença à espécie contam, mas isso é o <a href="especismo.html">especismo</a> que o argumento questiona; (c) aceitar a conclusão, como Peter Singer faz em parte, o que a maioria rejeita.</p>
<h2>Uma distinção útil</h2>
<table><thead><tr><th>Posição</th><th>Dor igual conta igual?</th><th>Morte é igualmente ruim?</th></tr></thead><tbody>
<tr><td>Não gradualista estrito</td><td>Sim</td><td>Não necessariamente: depende do que se perde</td></tr>
<tr><td>Gradualista moderado</td><td>Quase; a inteligência pode agravar ou aliviar a dor</td><td>Não</td></tr>
<tr><td>Gradualista forte</td><td>Não; mentes complexas pesam mais</td><td>Não</td></tr>
<tr><td>Antropocentrista</td><td>Só humanos contam de forma plena</td><td>Só a morte humana importa diretamente</td></tr>
</tbody></table>
<h2>O que a ciência acrescenta</h2>
<p>A intensidade da dor não parece acompanhar a inteligência. Um animal sem a capacidade de entender que a dor vai passar pode sofrer <em>mais</em> em uma situação em que um humano se consola com o futuro. Alguns pesquisadores argumentam que a dor pode ser a experiência central de mentes simples, sem distrações cognitivas. Isso vira o gradualismo ao contrário em alguns casos.</p>
<h2>Por que isso importa</h2>
<p>Se a dor conta igual, a criação industrial de animais é um dos maiores problemas morais existentes, por escala e intensidade. Se conta menos por grau de inteligência, o problema é menor, mas não desaparece, porque as capacidades dos animais criados são bem maiores do que se supõe. Em qualquer dos casos, a resposta “não contam” fica sem defesa. Veja <a href="etica-animal-na-pratica.html">ética animal na prática</a>.</p>
<div class="nota"><strong>Para guardar:</strong> capacidades mudam o que alguém perde, e por isso mudam o dano. A pergunta difícil é se mudam o peso de um dano igual, e o argumento dos casos marginais torna o sim muito caro.</div>
''', fontes=[('Argument from marginal cases (Wikipédia)', WE + 'Argument_from_marginal_cases'), ('The Moral Status of Animals (Stanford Encyclopedia)', SEP + 'moral-animal/'), MAPA, SINGER_PE]),

dict(slug='geracoes-futuras', grupo='As fronteiras do círculo', titulo='Gerações futuras: quem ainda não nasceu conta igual?', resumo='Temporalismo contra atemporalismo: o sofrimento daqui a cem anos vale menos do que o de hoje? Parfit, o desconto e os riscos de longo prazo.', corpo='''
<p class="abre">Pessoas que vão existir daqui a cem anos não votam, não protestam e não aparecem em pesquisas. Mas sofrerão ou se beneficiarão do que decidimos hoje sobre clima, dívidas, tecnologia e instituições. A pergunta é se os interesses delas contam tanto quanto os de quem existe agora.</p>
<h2>Temporalismo e atemporalismo</h2>
<div class="passos"><div><span>T</span><h3>Temporalista</h3><p>O presente pesa mais. O futuro é incerto, distante e, para alguns, menos real. Aplica-se uma taxa de desconto ao bem-estar futuro.</p></div><div><span>A</span><h3>Atemporalista</h3><p>Um sofrimento é igualmente ruim em qualquer data. A distância no tempo, como a distância no espaço, não é uma razão moral. Descontar o futuro é um viés.</p></div></div>
<h2>O argumento contra descontar</h2>
<p>Derek Parfit distinguiu duas razões para dar menos peso ao futuro. A <strong>incerteza</strong> é legítima: se não sabemos se o dano acontecerá, pesamos pela probabilidade. Mas o <strong>desconto puro</strong>, dar menos valor a um sofrimento certo só porque é mais tarde, não tem defesa: ninguém acha que uma dor de dente na próxima semana doerá menos do que uma amanhã. Henry Sidgwick já dizia que o tempo em que alguém existe não muda o valor do que lhe acontece. Economistas usam taxas de desconto por razões práticas (crescimento, incerteza), mas quando o desconto é puro, filósofos de quase todas as correntes o rejeitam.</p>
<h2>O problema da não identidade</h2>
<p>Parfit notou uma dificuldade. Nossas políticas de hoje determinam <em>quem</em> vai existir: outra política, outros pais se encontrariam, outras pessoas nasceriam. Então quem nasce em um mundo arruinado não pode dizer que foi prejudicado, porque sem a política ruim não existiria. Isso parece absurdo (a política foi ruim de qualquer jeito), e mostra que o dano a gerações futuras não pode ser pensado só em termos de prejudicar indivíduos específicos. Veja <a href="etica-populacional.html">ética populacional</a>.</p>
<h2>Longo prazo e riscos</h2>
<p>Se o futuro conta, o número de pessoas que podem vir a existir é imenso, e isso dá peso enorme a evitar catástrofes irreversíveis: guerra nuclear, pandemias projetadas, inteligência artificial fora de controle, colapso climático. Essa é a ideia do <strong>longoprazismo</strong>, de autores como Toby Ord e William MacAskill. As críticas:</p>
<ul>
<li><strong>Fanatismo:</strong> números imensos multiplicados por probabilidades minúsculas podem justificar qualquer coisa hoje. Defensores respondem com limites à agregação e foco em riscos concretos.</li>
<li><strong>Pessoas possíveis:</strong> temos dever de <em>criar</em> pessoas felizes, ou só de não prejudicar quem vai existir? A visão focada no sofrimento diz que o dever é evitar que o futuro seja ruim, não garantir que seja populoso.</li>
<li><strong>Negligenciar o presente:</strong> há sofrimento concreto agora, e ele é certo. Muitos defendem que a prioridade ao sofrimento atual e ao futuro não são rivais: ambas pedem evitar os piores desfechos.</li>
</ul>
<h2>Uma convergência</h2>
<p>Teorias diferentes concordam em uma coisa: há riscos cujo custo seria tão grande e irreversível, para tantos, que evitá-los é prioridade em quase qualquer visão. Um atemporalista focado no sofrimento, um utilitarista clássico e um deontologista preocupado com deveres às próximas gerações chegam ao mesmo lugar: não deixar um mundo arruinado para quem não teve voz.</p>
<div class="nota"><strong>Para guardar:</strong> a distância no tempo é como a distância no espaço: muda o que sabemos, não o que vale. Veja o <a href="https://ethicstest.biblioverse.org/map.html" target="_blank" rel="noopener">mapa do Teste</a>, em que o temporalismo é uma das perguntas sobre o círculo moral.</div>
''', fontes=[PARFIT, ('Intergenerational Justice (Stanford Encyclopedia)', SEP + 'justice-intergenerational/'), ('The Precipice', 'https://www.google.com/search?tbm=bks&q=Toby+Ord+The+Precipice'), ('Longtermism (Wikipédia)', WE + 'Longtermism')]),

dict(slug='mentes-artificiais', grupo='As fronteiras do círculo', titulo='Mentes artificiais: o substrato importa?', resumo='Se uma máquina vier a sentir, ela conta? O carbonismo diz que só mentes biológicas importam. O que está em jogo e por que a dúvida pede cuidado.', corpo='''
<p class="abre">Hoje não há evidência de que algum sistema artificial sinta algo. Mas a pergunta já importa: se um dia houver, o que diremos? Dar peso a uma mente só por ela ser feita de carbono e não de silício seria mais um eixo de tribalismo, ou há uma diferença relevante?</p>
<h2>Carbonismo</h2>
<p>É o nome dado à posição de que só seres biológicos podem ter interesses que contam, mesmo que um sistema artificial venha a ter experiências. O <a href="https://ethicstest.biblioverse.org/map.html" target="_blank" rel="noopener">Teste de Visão Moral</a> registra essa posição quando alguém inclui animais sencientes no círculo mas exclui mentes artificiais sencientes. A pergunta de coerência é a de sempre: <strong>se o critério é poder sentir, por que o material em que se sente mudaria o peso?</strong></p>
<h2>Os argumentos para incluir</h2>
<ul>
<li><strong>Consistência:</strong> rejeitamos raça, sexo e espécie como critérios porque não mudam a capacidade de sofrer. O substrato parece ser mais um desses traços.</li>
<li><strong>O princípio da precaução:</strong> não temos certeza sobre senciência em polvos ou insetos, e ainda assim concordamos em ter cautela. O mesmo vale aqui.</li>
<li><strong>Escala:</strong> se mentes artificiais sencientes puderem ser criadas em grande número, o sofrimento potencial seria enorme. Alguns autores consideram isso um dos maiores riscos do futuro.</li>
</ul>
<h2>Os argumentos para a dúvida</h2>
<ul>
<li><strong>Não sabemos o que produz experiência:</strong> talvez a consciência exija processos biológicos específicos. Se for assim, nenhuma máquina sentirá, e a questão não se coloca. Mas isso é uma hipótese empírica, não uma razão moral para excluir quem sentir.</li>
<li><strong>Risco de falsos positivos:</strong> sistemas de linguagem produzem textos que parecem expressar sentimentos sem que haja evidência de sentimento. Atribuir senciência cedo demais pode distorcer decisões e distrair de quem já sofre.</li>
<li><strong>O problema do acesso:</strong> inferimos senciência em animais por semelhança conosco (nervos, comportamento, evolução compartilhada). Com máquinas, essas pistas falham, e precisaríamos de outras.</li>
</ul>
<h2>Uma posição razoável</h2>
<table><thead><tr><th>Pergunta</th><th>Resposta prudente</th></tr></thead><tbody>
<tr><td>Sistemas atuais sentem?</td><td>Não há evidência disso. Trate como hipótese fraca.</td></tr>
<tr><td>Se um sistema sentir, conta?</td><td>Sim, pelo mesmo critério que faz um porco contar.</td></tr>
<tr><td>O que fazer agora?</td><td>Pesquisar critérios de senciência, evitar criar sistemas que possam sofrer sem saber, e não zombar da pergunta.</td></tr>
<tr><td>Isso tira foco dos animais?</td><td>Não deveria: o critério é o mesmo, e os animais já estão aqui, sofrendo em escala.</td></tr>
</tbody></table>
<h2>O que isso ensina sobre o círculo</h2>
<p>A questão das mentes artificiais é um teste de coerência para a posição que já tomamos. Quem diz “só humanos contam” tem uma resposta fácil (não). Quem diz “quem sente conta” precisa dizer sim, condicionado à senciência, ou explicar o que o carbono tem de especial. Para o <a href="circulo-moral.html">círculo moral</a>, a lição é a mesma de sempre: a fronteira precisa de uma razão, e “é diferente de mim” não é uma.</p>
<div class="nota"><strong>Para guardar:</strong> a pergunta não é se devemos incluir as máquinas de hoje. É se o nosso critério de inclusão depende de algo que importa (sentir) ou de algo que não importa (de que é feito quem sente).</div>
''', fontes=[('The Moral Consideration of Artificial Entities: A Literature Review', 'https://link.springer.com/article/10.1007/s11948-021-00331-8'), ('Ethics of Artificial Intelligence and Robotics (Stanford Encyclopedia)', SEP + 'ethics-ai/'), ('Sentience Institute: artificial sentience', 'https://www.sentienceinstitute.org/'), MAPA]),

dict(slug='vida-e-ecossistemas', grupo='As fronteiras do círculo', titulo='Vida e ecossistemas: biocentrismo e ecocentrismo', resumo='Uma árvore ou um rio contam por si mesmos? As éticas ambientais ampliam o círculo além da senciência, e entram em tensão com ela.', corpo='''
<p class="abre">A ética ambiental pergunta se seres vivos sem senciência, como plantas, e sistemas naturais, como florestas e rios, têm valor por si mesmos, e não só pelo que fazem por quem sente. Duas posições respondem sim, com argumentos e problemas diferentes.</p>
<h2>Biocentrismo</h2>
<p>Toda vida tem valor inerente. Albert Schweitzer falou de “reverência pela vida”; Paul Taylor, em <em>Respeito pela Natureza</em> (1986), argumentou que todo organismo tem um bem próprio (crescer, se reproduzir, manter-se), e que ter um bem próprio basta para merecer consideração. Humanos não seriam superiores: apenas uma espécie entre outras. Veja o <a href="teorias/biocentrismo.html">biocentrismo</a>.</p>
<p>A dificuldade: o que uma bactéria ou uma planta tem a perder? Ela pode ser danificada, mas não <em>sente</em> o dano. Se a consideração moral exige um ponto de vista, alguém para quem as coisas vão bem ou mal, seres sem senciência não o têm. E dar peso igual a tudo o que vive leva a conclusões estranhas: matar uma planta e matar um porco seriam equivalentes.</p>
<h2>Ecocentrismo</h2>
<p>O que tem valor são os sistemas: ecossistemas, espécies, a biosfera. Aldo Leopold, em <em>A Ética da Terra</em> (1949), formulou: algo é certo quando tende a preservar a integridade, a estabilidade e a beleza da comunidade biótica. J. Baird Callicott desenvolveu a posição, e a ecologia profunda de Arne Naess a radicalizou. Veja o <a href="teorias/ecocentrismo.html">ecocentrismo</a>.</p>
<p>A dificuldade: um ecossistema não sente nada. Os animais que vivem nele, sim. Quando o ecocentrismo manda sacrificar indivíduos pela “saúde do sistema” (abater animais introduzidos, deixar que a predação siga seu curso), ele dá prioridade a algo que não sofre sobre quem sofre. Tom Regan chamou isso de “fascismo ambiental”. Além disso, “integridade” e “estabilidade” não são estados naturais: ecossistemas mudam o tempo todo, e escolher um estado como o certo é uma decisão humana.</p>
<h2>O último homem</h2>
<p>Richard Routley propôs: o último humano vivo destrói, antes de morrer, toda a vida restante. Ninguém será afetado. Ele fez algo errado? Se a resposta é sim, algo na natureza tem valor independente de nós. Mas repare: no cenário, há animais sencientes sendo mortos. Um sencientista também diz que foi errado. Para separar as posições, é preciso imaginar a destruição só de plantas e rochas, e aí a intuição fica muito menos clara. Veja <a href="dilemas/ultimo-homem.html">o dilema</a>.</p>
<h2>A tensão com a senciência</h2>
<table><thead><tr><th>Caso</th><th>Ecocentrismo</th><th>Sencientismo</th></tr></thead><tbody>
<tr><td>Animais selvagens sofrendo por fome ou doença</td><td>Parte do sistema; não interferir</td><td>Sofrimento conta; ajudar se possível sem causar mais dano</td></tr>
<tr><td>Espécie invasora que ameaça um bioma</td><td>Erradicar</td><td>Buscar métodos que não causem sofrimento; o bioma só vale pelos seres que sentem</td></tr>
<tr><td>Floresta sem animais sencientes</td><td>Tem valor em si</td><td>Tem valor pelo que faz por quem sente, inclusive no futuro</td></tr>
<tr><td>Criação industrial de animais</td><td>Ruim pelo impacto ambiental</td><td>Ruim pelo sofrimento, antes de qualquer impacto</td></tr>
</tbody></table>
<p>O <a href="https://ethicstest.biblioverse.org/map.html" target="_blank" rel="noopener">Teste de Visão Moral</a> emite um aviso de tensão quando alguém inclui ecossistemas sem incluir nenhum ser senciente: deu consideração ao todo, e nenhuma a quem sofre dentro dele.</p>
<h2>Um meio-termo possível</h2>
<p>Muita gente combina as posições: seres sencientes contam por si; ecossistemas contam de forma derivada, porque abrigam quem sente, hoje e no futuro, e porque sua destruição é irreversível. Isso preserva quase tudo o que o ambientalismo pede, sem colocar o sistema acima de quem sofre nele. O que não dá é ignorar a tensão: proteger “a natureza” e proteger os animais nem sempre coincidem.</p>
<div class="nota"><strong>Para guardar:</strong> cuidar do planeta é cuidar de quem vive nele. Quando o todo e os indivíduos entram em conflito, vale lembrar quem sente a diferença.</div>
''', fontes=[('Environmental Ethics (Stanford Encyclopedia)', SEP + 'ethics-environmental/'), ('A Sand County Almanac (Wikipédia)', WE + 'A_Sand_County_Almanac'), ('Respect for Nature', 'https://www.google.com/search?tbm=bks&q=Paul+Taylor+Respect+for+Nature'), ('Animal Ethics: respeito pelos animais e ambientalismo', 'https://www.animal-ethics.org/perguntas-frequentes-sobre-as-diferencas-entre-respeito-pelos-animais-e-ambientalismo/')]),

dict(slug='etica-populacional', grupo='As fronteiras do círculo', titulo='Ética populacional e a conclusão repugnante', resumo='Quantas pessoas devem existir? Criar alguém feliz é um dever? Parfit mostrou que toda resposta leva a algum paradoxo.', corpo='''
<p class="abre">A ética populacional compara mundos com números diferentes de pessoas. Parece acadêmico, mas decide questões reais: políticas de natalidade, o peso das gerações futuras, se extinção é o pior resultado possível. Derek Parfit mostrou que todas as respostas simples levam a conclusões que ninguém aceita.</p>
<h2>A conclusão repugnante</h2>
<p>Compare o mundo A, com 10 bilhões de pessoas vivendo muito bem, e o mundo Z, com trilhões de pessoas cujas vidas são apenas um pouco melhores do que nada. Se o que importa é a soma total de bem-estar, Z é melhor, porque a soma é maior. Parfit chamou isso de conclusão repugnante, e passou décadas buscando uma teoria que a evitasse sem cair em outra conclusão igualmente ruim. Não achou. Veja <a href="dilemas/conclusao-repugnante.html">o dilema</a>.</p>
<h2>As saídas e seus custos</h2>
<table><thead><tr><th>Saída</th><th>Como evita</th><th>Novo problema</th></tr></thead><tbody>
<tr><td>Utilitarismo médio</td><td>Z tem média baixa</td><td>Um mundo com uma só pessoa extasiada seria melhor do que bilhões felizes; e adicionar alguém feliz, mas abaixo da média, pioraria o mundo</td></tr>
<tr><td>Visão da pessoa afetada</td><td>Só quem existe conta; criar não é dever</td><td>Não consegue dizer que é errado criar uma vida de puro sofrimento, nem explicar por que a extinção importa</td></tr>
<tr><td>Nível crítico</td><td>Vidas abaixo de um nível contam negativo</td><td>Vidas boas, mas abaixo do nível, ficam com valor negativo (“conclusão sádica”)</td></tr>
<tr><td>Limites à agregação</td><td>Muito bem-estar pequeno não supera pouco bem-estar grande</td><td>Viola a transitividade: A melhor que B, B melhor que C, C melhor que A</td></tr>
<tr><td>Prioridade ao sofrimento</td><td>Z tem muito sofrimento disperso; A, pouco</td><td>Precisa explicar por que criar vidas felizes não tem valor positivo comparável</td></tr>
</tbody></table>
<h2>A assimetria</h2>
<p>Quase todos aceitam duas intuições que não se encaixam fácil: é errado criar uma pessoa que só sofrerá; não é obrigatório criar uma pessoa que só será feliz. Jan Narveson resumiu: fazemos pessoas felizes, não fazemos pessoas <em>para</em> que haja felicidade. Essa assimetria é central para as éticas focadas no sofrimento, e difícil de acomodar no utilitarismo clássico, que trata criar felicidade e evitar sofrimento como simétricos. Veja <a href="o-peso-do-sofrimento.html">o peso do sofrimento</a>.</p>
<h2>O problema da não identidade</h2>
<p>Políticas de hoje determinam quem existirá. Uma política ruim produz um mundo pior, mas as pessoas que nele nascem não existiriam sem ela, e por isso não podem dizer que foram prejudicadas em comparação com a alternativa. Isso mostra que o mal de arruinar o futuro não pode ser descrito só como dano a indivíduos específicos. Precisamos de uma noção de “mundo pior” que não dependa de comparar as mesmas pessoas, e é isso que a ética populacional tenta construir.</p>
<h2>Por que isso importa</h2>
<ul>
<li><strong>Extinção:</strong> é o pior resultado possível, porque impede trilhões de vidas futuras? Ou é neutro, porque ninguém sofre a ausência? A resposta depende da posição.</li>
<li><strong>Procriação:</strong> há dever de ter filhos? Há dever de não ter, em um mundo com muito sofrimento? Autores como David Benatar defendem o antinatalismo; a maioria rejeita, mas a assimetria lhes dá um ponto de partida.</li>
<li><strong>Animais:</strong> criar bilhões de animais para vidas curtas e ruins é tornar o mundo pior em quase qualquer teoria populacional, porque adiciona sofrimento líquido.</li>
</ul>
<div class="nota"><strong>Para guardar:</strong> Parfit chamou a teoria que resolveria isso de “Teoria X”, e morreu sem encontrá-la. Gustaf Arrhenius e outros provaram, com teoremas de impossibilidade, que nenhuma teoria satisfaz todas as condições que achamos óbvias. Alguma intuição vai ter de ser abandonada; a discussão é sobre qual.</div>
''', fontes=[PARFIT, ('The Repugnant Conclusion (Stanford Encyclopedia)', SEP + 'repugnant-conclusion/'), ('Population Ethics (Utilitarianism.net)', 'https://utilitarianism.net/population-ethics/'), ('Better Never to Have Been', 'https://www.google.com/search?tbm=bks&q=Benatar+Better+Never+to+Have+Been')]),

dict(slug='incerteza-moral', grupo='Decidir sem certeza', titulo='Incerteza moral: agir sem saber qual teoria é a certa', resumo='Você não tem certeza se o utilitarismo ou a deontologia está certa. E agora? Parlamento moral, cobertura de riscos e o que as teorias concordam.', corpo='''
<p class="abre">Depois de todo o curso, uma coisa ficou clara: ninguém tem certeza sobre qual teoria ética é a correta. Pessoas inteligentes discordam há séculos. A pergunta prática é como agir bem sem ter resolvido isso. A resposta tem nome: ética sob incerteza moral.</p>
<h2>Dois tipos de incerteza</h2>
<p>A incerteza <strong>empírica</strong> é sobre fatos: esse remédio funciona? esse animal sente dor? Lidamos com ela por probabilidades. A incerteza <strong>moral</strong> é sobre valores: o sofrimento pesa mais do que o prazer? direitos cedem em catástrofes? Para ela, não há consenso sobre o que fazer, mas há propostas.</p>
<h2>Minha teoria favorita</h2>
<p>A resposta mais comum é agir pela teoria em que você mais acredita, ignorando as outras. O problema: se você tem 60% de confiança em uma teoria que diz que um ato é levemente bom e 40% em outra que diz que ele é uma catástrofe, agir só pela primeira ignora um risco enorme. Fazemos o oposto com incerteza empírica: não dirigimos a 200 km/h porque “provavelmente” nada acontecerá.</p>
<h2>Maximizar a escolha esperada</h2>
<p>William MacAskill, Toby Ord e Krister Bykvist propõem tratar teorias como hipóteses com probabilidades, e escolher a ação com o melhor resultado esperado, somando o que cada teoria diria, ponderado pela confiança. A dificuldade é comparar o que teorias diferentes dizem: quanto “errado” deontológico equivale a quanto “bem-estar perdido” utilitarista? Há propostas de normalização, nenhuma consensual.</p>
<h2>O parlamento moral</h2>
<p>Nick Bostrom sugeriu imaginar um parlamento em que cada teoria tem assentos proporcionais à sua credibilidade, e negocia. Teorias que se importam muito com um caso (a deontologia, diante de uma violação grave) conseguem barrá-lo, mesmo em minoria, em troca de ceder em casos que lhes importam menos. A imagem captura algo que a soma não captura: evitar que uma teoria minoritária seja pisoteada em tudo.</p>
<h2>Cobertura de riscos</h2>
<p>Com dinheiro, diversificamos para não perder tudo. Com teorias, podemos fazer o mesmo: preferir ações que são boas ou aceitáveis em muitas teorias, e evitar as que são catastróficas em alguma, mesmo que ótimas em outra. Isso tem uma consequência prática forte:</p>
<table><thead><tr><th>Ação</th><th>Utilitarismo</th><th>Deontologia</th><th>Virtudes</th><th>Sob incerteza</th></tr></thead><tbody>
<tr><td>Matar um para salvar cinco</td><td>Certo</td><td>Grave violação</td><td>Horror</td><td>Evitar: catástrofe em duas teorias</td></tr>
<tr><td>Doar parte da renda a quem precisa</td><td>Obrigatório</td><td>Louvável</td><td>Generoso</td><td>Fazer: bom em todas</td></tr>
<tr><td>Reduzir sofrimento de animais criados</td><td>Obrigatório</td><td>Devido, se são sujeitos de uma vida</td><td>Compassivo</td><td>Fazer: bom em todas, e a dúvida sobre senciência pede cautela</td></tr>
<tr><td>Mentir para proteger um inocente</td><td>Certo</td><td>Discutível; muitos aceitam</td><td>Honesto e prudente</td><td>Fazer, com cuidado</td></tr>
</tbody></table>
<h2>Incerteza sobre quem conta</h2>
<p>A incerteza moral mais consequente é sobre o círculo. Se há 30% de chance de que camarões sintam dor, e matamos trilhões por ano, o valor esperado do sofrimento é enorme mesmo com a dúvida. Jonathan Birch propõe tratar a senciência como uma questão de precaução: diante de evidência razoável, agir como se fosse verdade. Veja <a href="senciencia.html">senciência</a>.</p>
<h2>O que fazer, em resumo</h2>
<ol class="roteiro">
<li>Não exija certeza para agir: ela não vem.</li>
<li>Prefira ações robustas, boas em muitas teorias.</li>
<li>Evite as que são catastróficas em alguma teoria plausível, mesmo que ótimas em outra.</li>
<li>Dê peso à dúvida sobre quem sente: errar por incluir custa menos do que errar por excluir.</li>
<li>Continue aprendendo: a incerteza diminui com informação e reflexão. Veja <a href="abertura-moral.html">abertura moral</a>.</li>
</ol>
''', fontes=[('Moral Uncertainty', 'https://www.moraluncertainty.com/'), ('The Edge of Sentience', 'https://www.google.com/search?tbm=bks&q=Jonathan+Birch+The+Edge+of+Sentience'), ('Moral Uncertainty – Towards a Solution? (2009)', 'https://www.overcomingbias.com/p/moral-uncertainty-towards-a-solutionhtml')]),

dict(slug='quanto-a-moral-pode-exigir', grupo='Decidir sem certeza', titulo='Quanto a moral pode exigir de você?', resumo='Se cada real pode salvar alguém, por que não doar quase tudo? A objeção da exigência excessiva, os santos morais e o que é razoável pedir.', corpo='''
<p class="abre">Leve a sério a ideia de que o sofrimento de qualquer pessoa conta igual, e surge uma conclusão desconfortável: a maior parte do que gastamos em conforto poderia salvar vidas. Até onde a moral pode ir antes de pedir demais?</p>
<h2>O argumento de Singer</h2>
<p>Em <em>Fome, Riqueza e Moralidade</em> (1972), Peter Singer propôs: se podemos evitar algo muito ruim sem sacrificar nada de importância moral comparável, devemos fazê-lo. Com a <a href="dilemas/crianca-no-lago.html">criança no lago</a>, mostrou que já aceitamos isso quando a vítima está perto. Como distância e número de outros que poderiam ajudar não parecem diferenças relevantes, a conclusão é que devemos doar até o ponto em que doar mais nos custaria algo tão importante quanto o que a doação salva. Quase ninguém faz isso.</p>
<h2>A objeção da exigência excessiva</h2>
<p>Críticos dizem que uma teoria que proíbe quase todo projeto pessoal (uma viagem, um presente, um hobby) não pode estar certa, porque nenhuma pessoa real pode viver assim. Susan Wolf, em <em>Santos Morais</em> (1982), argumentou que uma pessoa inteiramente dedicada ao bem seria, a seu modo, empobrecida: sem arte, sem humor, sem relações que não fossem instrumentais. E ninguém quer que seus filhos sejam assim. Bernard Williams acrescentou que a moral que exige abandonar o que dá sentido à vida esqueceu para que a vida serve.</p>
<h2>As respostas</h2>
<table><thead><tr><th>Resposta</th><th>O que diz</th><th>Problema</th></tr></thead><tbody>
<tr><td>Aceitar a exigência</td><td>A teoria está certa; nós é que somos complacentes</td><td>Pode desencorajar em vez de motivar</td></tr>
<tr><td>Obrigatório e supererrogatório</td><td>Há um mínimo devido; acima dele é louvável, não obrigatório</td><td>Onde fica o mínimo, e por quê?</td></tr>
<tr><td>Prerrogativa do agente</td><td>Samuel Scheffler: temos direito a dar algum peso extra aos próprios projetos</td><td>Quanto peso? E vale para quem está morrendo?</td></tr>
<tr><td>Dever justo</td><td>Liam Murphy: cada um deve a sua parte do que seria preciso se todos fizessem a sua</td><td>Quem sofre não é ajudado pela parte que os outros não fizeram</td></tr>
<tr><td>Consequencialismo sobre exigências</td><td>Uma regra moderada gera mais bem no total, porque é seguida</td><td>Pode ser verdade, mas parece conveniente demais</td></tr>
</tbody></table>
<h2>Uma posição prática</h2>
<p>Singer mesmo adotou, em livros posteriores, um padrão realista: doar uma porcentagem crescente da renda, começando por algo como 1% e subindo com a riqueza, e comparar o que se faz com o que se poderia fazer sem ilusões. O movimento do altruísmo eficaz propôs o compromisso de 10%. Não é o que a teoria pura pede, mas é muito mais do que a média, e salva vidas. A diferença entre o ideal e o nada não precisa ser preenchida com culpa; pode ser preenchida com uma meta.</p>
<h2>O que isso diz sobre as teorias</h2>
<ul>
<li><strong>Consequencialismo:</strong> enfrenta a objeção de frente; suas melhores versões distinguem o que é certo do que vale a pena cobrar.</li>
<li><strong>Deontologia:</strong> tem deveres positivos limitados; Kant falava em dever imperfeito de beneficência, com latitude. Isso alivia a exigência, mas pode permitir pouco demais.</li>
<li><strong>Virtudes:</strong> a pessoa generosa dá muito, mas também cultiva amizades, arte e descanso. A exigência é vivida, não calculada.</li>
<li><strong>Cuidado:</strong> começa pelos próximos, mas não termina neles: a vulnerabilidade distante também chama.</li>
</ul>
<div class="nota"><strong>Para guardar:</strong> talvez a moral exija mais do que fazemos. Isso não é razão para rejeitá-la, nem para se paralisar. É razão para fazer mais, aos poucos, e com honestidade sobre a distância que falta.</div>
''', fontes=[('Famine, Affluence, and Morality (Wikipédia)', WE + 'Famine,_Affluence,_and_Morality'), ('Moral Saints (1982)', 'https://doi.org/10.2307/2026228'), ('The Life You Can Save', 'https://www.thelifeyoucansave.org/'), ('Demandingness objection (Wikipédia)', WE + 'Demandingness_objection')]),

dict(slug='da-etica-a-politica', grupo='Decidir sem certeza', titulo='Da ética à política: valores primeiro, evidências depois', resumo='Toda decisão política carrega uma resposta ética, mesmo sem dizê-la. Como levar o que você aprendeu aqui para o debate público.', corpo='''
<p class="abre">A ética pergunta o que é certo. A política decide o que fazer em conjunto, com poder e recursos limitados. Toda decisão política já responde a perguntas éticas, quase sempre sem admitir: quem conta, quanto conta, o que pode ser sacrificado. Quem pula essa etapa não fica sem ética; fica com uma ética que nunca examinou.</p>
<h2>O ideal dos dois passos</h2>
<p>Magnus Vinding, em <em>Reasoned Politics</em>, propõe separar o debate político em dois passos. No primeiro, <strong>normativo</strong>, esclarecer e defender os valores: reduzir sofrimento? proteger direitos? dar prioridade a quem está pior? No segundo, <strong>empírico</strong>, investigar com evidências quais políticas realizam esses valores. A maior parte das brigas públicas mistura os dois, e por isso não avança: um lado discute valores, o outro discute efeitos, e cada um acha que o outro é desonesto. Veja <a href="fatos-e-valores.html">fatos e valores</a>.</p>
<h2>As perguntas éticas escondidas em cada política</h2>
<table><thead><tr><th>Política</th><th>Pergunta ética escondida</th><th>Teorias em jogo</th></tr></thead><tbody>
<tr><td>Imposto progressivo</td><td>Um real vale o mesmo para quem tem muito e para quem tem pouco?</td><td>Prioritarismo contra libertarismo</td></tr>
<tr><td>Saúde universal</td><td>Há um mínimo devido a todos, independentemente do mérito?</td><td>Suficientismo, direitos positivos</td></tr>
<tr><td>Pena de morte</td><td>O Estado pode tirar uma vida? Punição é merecimento ou prevenção?</td><td>Retributivismo contra consequencialismo</td></tr>
<tr><td>Subsídio à pecuária</td><td>O sofrimento de quem é criado conta na decisão?</td><td>Antropocentrismo contra sencientismo</td></tr>
<tr><td>Imigração</td><td>O lugar de nascimento é uma razão moral para menos direitos?</td><td>Nacionalismo contra imparcialidade</td></tr>
<tr><td>Dívida pública e clima</td><td>Quem ainda não nasceu conta?</td><td>Temporalismo contra atemporalismo</td></tr>
</tbody></table>
<h2>O que a ética leva para a política</h2>
<ul>
<li><strong>Explicitar valores:</strong> antes de discutir uma medida, dizer o que ela tenta realizar. Isso mostra se o desacordo é de valor ou de fato.</li>
<li><strong>Testar com imparcialidade:</strong> eu aceitaria essa regra sem saber em que lugar estaria? Nas mãos do governo adversário? Veja <a href="imparcialidade.html">imparcialidade</a>.</li>
<li><strong>Contar todos os afetados:</strong> inclusive quem não vota: crianças, estrangeiros, animais, gerações futuras. Uma política que ignora quem sofre com ela não é neutra, é parcial.</li>
<li><strong>Comparar com as alternativas reais:</strong> não basta uma política ser boa; precisa ser melhor do que as opções disponíveis, inclusive a de não fazer nada.</li>
<li><strong>Humildade:</strong> valores também podem estar errados. A história política é cheia de certezas morais que hoje envergonham.</li>
</ul>
<h2>Ética não é partido</h2>
<p>Nenhuma teoria ética pertence a um lado. Consequencialistas defendem o livre mercado e a redistribuição, conforme o que as evidências mostrem. Deontologistas defendem direitos civis e direitos de propriedade. A ética das virtudes inspira conservadores e progressistas. O que a ética faz é obrigar cada lado a dizer o que valoriza e a aceitar que seja testado. Quem usa a ética só para justificar o que seu grupo já defendia inverteu a ordem: a ética vem antes.</p>
<h2>Continue no Política Para Iniciantes</h2>
<p>Este curso para aqui, na porta da política. O <a href="https://politicaparainiciantes.biblioverse.org/" target="_blank" rel="noopener">Política Para Iniciantes</a> continua do outro lado: como funciona o sistema, o que cada vertente defende, os grandes debates com os dois lados e o que os dados indicam, e os vieses que torcem o julgamento político. Ele parte das mesmas premissas deste site: valores e fatos devem ser separados, todos os que podem sofrer devem ser considerados, e a ética vem antes da política.</p>
<div class="cta"><a class="btn" href="https://politicaparainiciantes.biblioverse.org/" target="_blank" rel="noopener">Ir para o Política Para Iniciantes</a></div>
''', fontes=[VINDING, ('Política Para Iniciantes', 'https://politicaparainiciantes.biblioverse.org/'), ('Political Philosophy (Internet Encyclopedia of Philosophy)', IEP + 'polphil/'), SINGER_PE]),

dict(slug='progresso-moral', grupo='Progresso e abertura', titulo='Progresso moral: existe, e como saber?', resumo='Abolição, voto feminino, fim da tortura pública. Isso é progresso ou só mudança de costume? Critérios para distinguir, e por que nada é garantido.', corpo='''
<p class="abre">Escravidão legal, mulheres sem voto e tortura como espetáculo público já foram normais. Hoje, a maioria considera tudo isso errado. Isso é progresso, no sentido de ter chegado mais perto da verdade moral? Ou só mudança, como a moda? A resposta depende da metaética, mas há critérios que servem em quase qualquer posição.</p>
<h2>O problema</h2>
<p>Se julgamos o passado pelos nossos valores, é claro que parecemos melhores: estamos usando a régua que nos favorece. Um escravocrata do século XVIII também achava que vivia o ponto alto da civilização. Para falar em progresso sem circularidade, precisamos de um critério que não seja só “o que achamos hoje”.</p>
<h2>Critérios que servem</h2>
<ol class="roteiro">
<li><strong>Coerência:</strong> a mudança corrigiu uma contradição? “Todos nascem iguais” mais escravidão era uma contradição. Resolvê-la é progresso por qualquer régua que aceite a lógica.</li>
<li><strong>Informação:</strong> a mudança veio de saber mais sobre quem é afetado? Descobrir que mulheres raciocinam tão bem quanto homens, que animais sentem dor, que a homossexualidade não é doença, mudou juízos sem mudar valores básicos.</li>
<li><strong>Imparcialidade:</strong> a nova regra seria aceita por quem está dos dois lados dela? A velha, não?</li>
<li><strong>Menos sofrimento:</strong> há menos dor e morte evitáveis? É um critério que quase toda teoria aceita como relevante, mesmo que não como único.</li>
<li><strong>Melhores razões:</strong> a mudança se apoiou em argumentos que sobrevivem ao exame, ou em força e preconceito?</li>
</ol>
<p>Allen Buchanan e Russell Powell, em <em>A Evolução do Progresso Moral</em> (2018), propõem pensar o progresso em tipos específicos (inclusão de novos grupos, melhor compreensão de conceitos morais, redução de crenças falsas que sustentavam práticas) em vez de uma única linha ascendente. Isso permite reconhecer progresso aqui e regresso ali, sem uma narrativa triunfal.</p>
<h2>A principal forma: incluir quem ficava de fora</h2>
<p>Quase todo progresso moral reconhecido foi uma <a href="expansao-do-circulo-moral.html">expansão do círculo</a>: descobrir que uma diferença tratada como relevante não era. Isso dá uma direção: a pergunta “quem ainda está de fora por uma diferença irrelevante?” é um bom detector de onde o próximo progresso pode estar.</p>
<h2>Nada é garantido</h2>
<ul>
<li><strong>O círculo encolhe:</strong> a Alemanha de Weimar se tornou o nazismo em poucos anos. Ruanda em 1994 e a Bósnia nos anos 1990 mostram que grupos incluídos podem ser expulsos do círculo com rapidez.</li>
<li><strong>Progresso de fachada:</strong> leis mudam sem que a prática mude. A escravidão foi abolida e cerca de 50 milhões de pessoas vivem em formas modernas dela, segundo a OIT.</li>
<li><strong>Pontos cegos imensos:</strong> condenamos a crueldade e mantemos bilhões de animais em condições que, descritas sem a palavra “comida”, chamaríamos de tortura. Progresso convive com cegueira.</li>
<li><strong>Falso progresso:</strong> regimes do século XX mataram milhões em nome do “homem novo”, e o colonialismo se chamou “civilizar”. Nem tudo que se anuncia como avanço é.</li>
</ul>
<h2>Humildade com o passado e com o presente</h2>
<p>Se nossos avós erraram em coisas que lhes pareciam óbvias, é quase certo que nós também. A pergunta útil não é “como eles puderam?”, e sim “o que estamos fazendo que o futuro verá assim?”. Candidatos frequentes: o tratamento dos animais, a indiferença à pobreza extrema, o descaso com as gerações futuras. Nenhum deles exige valores novos. Exige aplicar os que já temos a quem ainda não aplicamos.</p>
<div class="nota"><strong>Para guardar:</strong> progresso moral não é uma linha que sobe sozinha. É o trabalho de corrigir incoerências, aprender quem sofre e incluir quem ficou de fora, refeito a cada geração.</div>
''', fontes=[('The Evolution of Moral Progress', 'https://www.google.com/search?tbm=bks&q=Buchanan+Powell+The+Evolution+of+Moral+Progress'), ('Moral progress (Wikipédia)', WE + 'Moral_progress'), ('OIT: 50 milhões em escravidão moderna', 'https://www.ilo.org/resource/news/50-million-people-worldwide-modern-slavery-0'), ('The Expanding Circle', 'https://www.google.com/search?tbm=bks&q=Peter+Singer+The+Expanding+Circle')]),

dict(slug='abertura-moral', grupo='Progresso e abertura', titulo='Abertura moral: como revisar o que você acredita', resumo='Diante de um argumento forte contra a sua posição, você reavalia ou resiste? A disposição de mudar é o que separa quem evolui de quem só se defende.', corpo='''
<p class="abre">A última parte do <a href="https://ethicstest.biblioverse.org/" target="_blank" rel="noopener">Teste de Visão Moral</a> não pergunta quais crenças você tem, e sim como as sustenta: o que acontece quando um bom argumento vai contra o que você pensa. Essa disposição, entre flexibilidade e firmeza, decide se as suas visões melhoram com o tempo ou só endurecem.</p>
<h2>Três perfis</h2>
<div class="tres">
<div><h3>Alta abertura</h3><p>Questiona crenças arraigadas diante de bons contra-argumentos. Risco: mudar por qualquer vento, sem critério.</p></div>
<div><h3>Abertura moderada</h3><p>Flexível, mas exige evidência excepcionalmente forte para rever o que já pensa. Risco: a exigência virar desculpa.</p></div>
<div><h3>Baixa abertura</h3><p>Forte confiança em intuições e convenções estabelecidas. Força: estabilidade. Risco: nunca corrigir um erro.</p></div>
</div>
<h2>Por que é difícil mudar</h2>
<ul>
<li><strong>Identidade:</strong> crenças morais viram parte de quem somos e do grupo a que pertencemos. Abandonar uma parece traição.</li>
<li><strong>Raciocínio motivado:</strong> buscamos razões para a conclusão que já queremos, e as encontramos. Veja <a href="vieses-morais.html">vieses morais</a>.</li>
<li><strong>Custo prático:</strong> mudar de ideia sobre animais, doação ou política muda hábitos. É mais fácil ajustar a crença ao hábito do que o contrário.</li>
<li><strong>Dissonância:</strong> quanto mais investimos em uma posição, mais custa admitir que estava errada.</li>
</ul>
<h2>Como revisar bem</h2>
<ol class="roteiro">
<li><strong>Separe a crença da identidade:</strong> você não é a sua opinião sobre o utilitarismo. Pode trocá-la e continuar sendo você.</li>
<li><strong>Diga o que o faria mudar:</strong> antes de discutir, escreva que evidência ou caso o faria rever a posição. Se não há nada, não é uma crença, é uma lealdade.</li>
<li><strong>Procure o melhor adversário:</strong> leia quem discorda de você no seu melhor, não no pior. Se a posição sobreviver, está mais forte; se não, você aprendeu.</li>
<li><strong>Calibre:</strong> atribua graus de confiança, não certezas. “Acho 70% provável que” permite ajustar; “tenho certeza” só permite capitular ou negar.</li>
<li><strong>Note a origem da intuição:</strong> ela vem de informação e reflexão, ou de nojo, grupo e hábito? Veja <a href="evolucao-e-moral.html">evolução e moral</a>.</li>
<li><strong>Celebre a mudança:</strong> ter mudado de ideia é sinal de que você pensa, não de que era burro. Quem nunca mudou é que deveria se preocupar.</li>
</ol>
<h2>Abertura não é relativismo</h2>
<p>Estar aberto a argumentos não é achar que todas as posições valem o mesmo. É o oposto: é porque algumas são melhores que vale a pena procurar. O relativista não precisa de abertura, porque não há nada a descobrir. O realista e o quase-realista precisam, porque podem estar errados. Veja <a href="egoismo-relativismo-e-ceticismo.html">relativismo</a>.</p>
<h2>Firmeza também é virtude</h2>
<p>Há coisas sobre as quais a abertura excessiva é vício: alguém que “considera os dois lados” sobre torturar crianças não é aberto, é perdido. A abertura madura distingue entre questões em aberto (quanto pesa o sofrimento diante do prazer? direitos cedem em catástrofes?) e questões em que o peso da razão já se acumulou. Mudar de ideia sobre as primeiras é inteligência; sobre as segundas, exige muito mais do que um argumento esperto.</p>
<h2>O curso termina, a pergunta não</h2>
<p>Você percorreu as teorias normativas, o círculo moral, a metaética e as fronteiras do debate atual. Nenhuma lição deu a resposta final, porque ela não existe pronta. O que existe é um método: separar fatos de valores, exigir coerência, testar com imparcialidade, contar todos os afetados, agir sob incerteza e manter-se aberto. Se este site conseguiu alguma coisa, foi tornar essas ferramentas suas.</p>
<div class="cta"><a class="btn" href="https://ethicstest.biblioverse.org/" target="_blank" rel="noopener">Faça o Teste de Visão Moral</a><a class="btn alt" href="teorias.html">Reveja as teorias</a></div>
''', fontes=[TESTE, ('Intellectual humility (Wikipédia)', WE + 'Intellectual_humility'), ('Mudar de ideia (Política Para Iniciantes)', 'https://politicaparainiciantes.biblioverse.org/mudar-de-ideia.html'), ('Changing Our Minds (Stanford Encyclopedia: Belief revision)', SEP + 'logic-belief-revision/')]),
]
