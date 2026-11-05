"""Lições do nível Iniciante. O corpo é HTML; as fontes são pares (rótulo, url), só com o título da obra."""
SEP = 'https://plato.stanford.edu/entries/'
IEP = 'https://iep.utm.edu/'
WP = 'https://pt.wikipedia.org/wiki/'
WE = 'https://en.wikipedia.org/wiki/'
TESTE = ('Teste de Visão Moral', 'https://ethicstest.biblioverse.org/')
MAPA = ('Mapa do Teste de Visão Moral', 'https://ethicstest.biblioverse.org/map.html')
VINDING = ('Reasoned Politics (2022)', 'https://magnusvinding.com/wp-content/uploads/2022/03/reasoned-politics.pdf')
SINGER_PE = ('Ética Prática', 'https://www.google.com/search?tbm=bks&q=Peter+Singer+%C3%89tica+Pr%C3%A1tica')
RACHELS = ('Os Elementos da Filosofia Moral', 'https://www.google.com/search?tbm=bks&q=Rachels+Os+Elementos+da+Filosofia+Moral')

INICIANTE = [
dict(slug='o-que-e-etica', grupo='O básico', titulo='O que é ética?', resumo='Ética é a área da filosofia que analisa a moral, também chamada de filosofia moral: o estudo de como devemos agir e tratar os outros.', corpo='''
<p class="abre">Ética é a área da filosofia dedicada à análise da moral, e por isso também é chamada de filosofia moral. É a reflexão sobre como devemos viver e agir: o que é certo e errado, o que devemos aos outros, quem merece nossa consideração e por quê.</p>
<p>Todo mundo já tem uma ética, mesmo sem nunca ter lido um filósofo. Quando você acha injusto que alguém fure a fila, quando se sente culpado por uma mentira ou quando se indigna com um caso de crueldade, você está fazendo juízos morais. O estudo da ética não inventa esses juízos. Ele os organiza, os testa e pergunta se eles se sustentam.</p>
<h2>Três perguntas que a ética faz</h2>
<div class="tres">
<div><h3>Como devo agir?</h3><p>É a pergunta da <strong>ética normativa</strong>: que critério separa uma ação certa de uma errada? Resultado, regra, caráter?</p><p class="pol">Veja o <a href="mapa-das-teorias.html">mapa das teorias</a>.</p></div>
<div><h3>Quem conta?</h3><p>É a pergunta do <strong>círculo moral</strong>: quem merece consideração direta, e com que peso? Só eu, meu grupo, todos os humanos, todos os que sentem?</p><p class="pol">Veja o <a href="circulo-moral.html">círculo moral</a>.</p></div>
<div><h3>O que é um juízo moral?</h3><p>É a pergunta da <strong>metaética</strong>: quando digo que a tortura é errada, estou descrevendo um fato, expressando um sentimento ou dando uma ordem?</p><p class="pol">Fica para o nível <a href="avancado.html">Avançado</a>.</p></div>
</div>
<h2>Descrever e prescrever</h2>
<p>Uma antropóloga pode descrever o que uma sociedade considera certo. Isso é <strong>ética descritiva</strong>: um retrato de costumes, que pode mudar de um lugar para outro. A filosofia moral faz outra coisa: pergunta o que <em>deveria</em> ser considerado certo, e com que razões. É a <strong>ética normativa</strong>. Confundir as duas é um erro comum: saber que uma prática é aceita em algum lugar não diz se ela é boa.</p>
<table><thead><tr><th>Pergunta</th><th>Tipo</th><th>Quem responde</th></tr></thead><tbody>
<tr><td>O que os romanos achavam da escravidão?</td><td>Descritiva</td><td>Historiadores</td></tr>
<tr><td>A escravidão era errada?</td><td>Normativa</td><td>Qualquer pessoa que argumente</td></tr>
<tr><td>O que a maioria pensa sobre comer carne?</td><td>Descritiva</td><td>Pesquisas de opinião</td></tr>
<tr><td>Devemos comer carne?</td><td>Normativa</td><td>Argumentos e evidências sobre os afetados</td></tr>
</tbody></table>
<h2>Ética não é opinião, nem só gosto</h2>
<p>“Cada um tem a sua ética” soa humilde, mas raramente é levado a sério por quem diz. Ninguém aceita que torturar uma criança por diversão seja só uma questão de gosto, como preferir chocolate a baunilha. Juízos morais pedem razões. Quando alguém diz que algo é errado, pode ser perguntado “por quê?”, e a resposta pode ser boa ou ruim. É isso que torna a ética um assunto que se estuda, e não só se sente.</p>
<p>Isso não significa que exista uma resposta fácil para tudo. Significa que algumas respostas são melhores do que outras: mais coerentes, mais informadas sobre quem é afetado, menos dependentes de quem está falando. Este curso ensina a reconhecer essas diferenças.</p>
<h2>Por que estudar isso</h2>
<ul>
<li><strong>Para decidir melhor:</strong> dilemas reais, do trabalho à família, ficam mais claros quando se sabe o que está em jogo.</li>
<li><strong>Para não ser levado:</strong> quem nunca examinou os próprios valores fica mais fácil de manipular, inclusive na política.</li>
<li><strong>Para entender quem discorda:</strong> muitas brigas são entre pessoas que usam critérios diferentes sem saber.</li>
<li><strong>Para corrigir pontos cegos:</strong> cada época achou normal algo que depois foi visto como erro grave. A nossa provavelmente não é exceção.</li>
</ul>
<h2>As outras dimensões</h2>
<p>As três perguntas acima são as da teoria. Uma visão moral completa tem mais duas dimensões: a <strong>capacidade de agir</strong> (que conhecimento e que poder a pessoa tem para realizar o que considera certo) e a <strong>abertura</strong> (como ela revisa o que acredita diante de bons argumentos). Saber o certo e não poder, ou não querer mudar de ideia, são falhas tão comuns quanto não saber. A seção de <a href="criterios.html">critérios éticos</a> apresenta as cinco dimensões juntas.</p>
<div class="nota"><strong>Para guardar:</strong> ética é a pergunta “como devo agir, e por quê?”, feita com seriedade e aberta a razões. O resto do curso são tentativas de respondê-la.</div>
''', fontes=[('Ethics (Internet Encyclopedia of Philosophy)', IEP + 'ethics/'), ('Ética (Wikipédia)', WP + '%C3%89tica'), RACHELS, TESTE]),

dict(slug='etica-moral-lei-e-religiao', grupo='O básico', titulo='Ética, moral, lei e religião: não são a mesma coisa', resumo='Legal não quer dizer certo, e proibido não quer dizer errado. Entenda o que cada palavra faz e por que separá-las evita confusão.', corpo='''
<p class="abre">Quatro coisas costumam ser misturadas: o que a lei permite, o que a religião manda, o que os costumes aprovam e o que é certo. Elas se influenciam, mas não são a mesma coisa.</p>
<h2>Ética e moral</h2>
<p>No uso comum, as duas palavras são quase sinônimas. Em filosofia, muitos reservam <strong>moral</strong> para o conjunto de valores e normas que uma pessoa ou grupo segue, e <strong>ética</strong> para a área da filosofia que analisa esses valores, também chamada de filosofia moral. Neste curso, usamos as duas de forma solta, como a maioria dos autores faz hoje. O que importa é a diferença entre <em>ter</em> valores e <em>examiná-los</em>.</p>
<h2>Lei não é moral</h2>
<p>A lei é um conjunto de regras com força do Estado. Ela tenta refletir a moral de uma sociedade, mas falha de dois jeitos:</p>
<table><thead><tr><th>Caso</th><th>Legal?</th><th>Moralmente certo?</th></tr></thead><tbody>
<tr><td>Escravidão no Brasil até 1888</td><td>Sim</td><td>Não</td></tr>
<tr><td>Esconder judeus do regime nazista</td><td>Não</td><td>Sim</td></tr>
<tr><td>Mentir para um amigo sobre algo importante</td><td>Sim</td><td>Em geral, não</td></tr>
<tr><td>Deixar de ajudar alguém que se afoga, podendo</td><td>Depende do país</td><td>Não</td></tr>
</tbody></table>
<p>“É legal, então pode” e “é crime, então é errado” são atalhos que falham o tempo todo. Leis são feitas por pessoas, com interesses e pontos cegos, e precisam ser julgadas pela ética, e não o contrário. Foi assim que a escravidão, a censura e a discriminação legal caíram: alguém disse que a lei estava errada.</p>
<h2>Religião e moral</h2>
<p>Muitas pessoas aprendem seus valores em uma tradição religiosa, e as grandes religiões carregam reflexões morais profundas. Mas há duas razões para não reduzir a ética à religião:</p>
<ul>
<li><strong>Pessoas sem religião também têm moral</strong>, e pessoas de religiões diferentes concordam em muito: não matar, não roubar, cuidar dos vulneráveis. Isso sugere que a moral tem bases que não dependem de uma crença específica.</li>
<li><strong>O dilema de Eutífron:</strong> Platão perguntou se algo é bom porque Deus manda, ou se Deus manda porque é bom. Se for a primeira opção, a bondade seria arbitrária. Se for a segunda, há um padrão de bondade que podemos examinar com a razão. O nível Intermediário discute isso em <a href="etica-e-religiao.html">ética e religião</a>.</li>
</ul>
<p>Nada disso é um argumento contra a religião. É um argumento para que crentes e não crentes possam discutir ética com razões que ambos entendam.</p>
<h2>Costume não é moral</h2>
<p>“Sempre foi assim” descreve, não justifica. Duelos, pés enfaixados, casamentos infantis e castigos públicos já foram costumes respeitáveis. Kwame Anthony Appiah mostra em <em>O Código de Honra</em> que esses costumes caíram quando passaram a ser vistos como vergonhosos. O costume muda; a pergunta sobre se ele era certo continua sendo outra pergunta.</p>
<h2>Etiqueta não é moral</h2>
<p>Comer com a mão ou falar alto no cinema são questões de convenção. Elas podem incomodar, mas ninguém é prejudicado de forma séria. A moral trata do que afeta o bem-estar, os direitos e a dignidade de alguém. Boa parte das confusões morais vem de tratar convenção como moral, ou moral como convenção.</p>
<div class="nota"><strong>Teste rápido:</strong> diante de uma regra, pergunte “quem é prejudicado se ela for quebrada?”. Se a resposta for “ninguém, só é feio”, provavelmente é etiqueta. Se alguém sofre ou perde algo, é moral.</div>
''', fontes=[('Euthyphro (Wikipédia)', WE + 'Euthyphro'), ('The Honor Code', 'https://www.google.com/search?tbm=bks&q=Appiah+The+Honor+Code'), ('The Nature of Law (Stanford Encyclopedia)', SEP + 'lawphil-nature/'), RACHELS]),

dict(slug='fatos-e-valores', grupo='O básico', titulo='Fatos e valores: a diferença que organiza tudo', resumo='Do que “é” não se tira sozinho o que “deve ser”. Separar as duas perguntas resolve metade das discussões.', corpo='''
<p class="abre">Uma afirmação de fato descreve o mundo e pode ser checada. Uma afirmação de valor diz como o mundo deveria ser e pede argumentos. Misturar as duas é a fonte mais comum de confusão moral.</p>
<h2>A guilhotina de Hume</h2>
<p>David Hume observou, no século XVIII, que não se pode concluir o que <em>deve ser</em> só a partir do que <em>é</em>. “Os animais comem uns aos outros” é um fato. “Logo, podemos comê-los” é um salto: falta uma premissa de valor, como “o que acontece na natureza é bom”, que precisa ser defendida por si mesma. Esse salto ganhou o nome de <strong>falácia naturalista</strong>, em sentido amplo.</p>
<table><thead><tr><th>Fato</th><th>Salto</th><th>Premissa que faltou</th></tr></thead><tbody>
<tr><td>A maioria faz isso</td><td>Logo, é certo</td><td>“O que a maioria faz é certo” (é?)</td></tr>
<tr><td>Sempre foi assim</td><td>Logo, deve continuar</td><td>“Tradição é razão suficiente” (é?)</td></tr>
<tr><td>É natural</td><td>Logo, é bom</td><td>“Natural é bom” (doenças também são naturais)</td></tr>
<tr><td>Sinto nojo disso</td><td>Logo, é errado</td><td>“Minha repulsa é um guia confiável” (nem sempre foi)</td></tr>
</tbody></table>
<h2>Como separar na prática</h2>
<p>Em qualquer discussão, duas perguntas estão misturadas: <em>o que queremos?</em> e <em>o que funciona?</em> Magnus Vinding chama isso de ideal dos dois passos. Primeiro, esclarecer os valores. Depois, com os valores claros, investigar com evidências o que os realiza.</p>
<div class="passos"><div><span>1</span><h3>Passo normativo</h3><p>O que importa aqui? Reduzir sofrimento? Respeitar um direito? Ser justo com quem está pior?</p></div><div><span>2</span><h3>Passo empírico</h3><p>Dado o que importa, qual ação ou regra tem mais chance de realizar isso? Aqui entram dados, estudos e experiência.</p></div></div>
<p>Um exemplo: duas pessoas discutem se a pena de prisão deve ser mais longa. Pode ser que as duas queiram a mesma coisa, menos crimes, e discordem sobre o efeito das penas. Isso é uma disputa de fatos, que pesquisas ajudam a resolver. Ou pode ser que uma valorize a punição como merecimento e a outra só o resultado. Isso é uma disputa de valores, e nenhum dado sozinho a encerra.</p>
<h2>Valores também se discutem</h2>
<p>Separar fatos de valores não quer dizer que valores sejam só gosto. Eles podem ser examinados por coerência (“você aceita a mesma regra quando ela é contra você?”), por implicações (“o que a sua regra manda no caso extremo?”) e por informação (“você sabia quem é afetado?”). Muita gente muda de valor ao conhecer melhor os fatos, e isso é um sinal de que fatos e valores conversam, mesmo sem um derivar do outro.</p>
<h2>Fatos podem mudar a conclusão sem mudar o valor</h2>
<p>Se o valor é “não causar sofrimento desnecessário” e a ciência mostra que peixes sentem dor, a conclusão sobre como tratá-los muda, sem que o valor tenha mudado. Por isso, boa parte do progresso moral vem de descobrir fatos: sobre quem sofre, sobre o que funciona, sobre as consequências reais de uma prática. Veja a <a href="expansao-do-circulo-moral.html">expansão do círculo moral</a>.</p>
<div class="nota"><strong>Para guardar:</strong> antes de discutir, pergunte “discordamos sobre o que queremos ou sobre o que acontece?”. A primeira pede argumentos morais; a segunda pede evidências. Treine na ferramenta <a href="ferramentas/fato-ou-valor.html">Fato ou valor?</a>.</div>
''', fontes=[('Is–ought problem (Wikipédia)', WE + 'Is%E2%80%93ought_problem'), ('Hume’s Moral Philosophy (Stanford Encyclopedia)', SEP + 'hume-moral/'), VINDING]),

dict(slug='argumentos-morais', grupo='O básico', titulo='Como funciona um argumento moral', resumo='Premissas, conclusão e coerência. Um argumento moral se avalia como qualquer outro, e os erros mais comuns têm nome.', corpo='''
<p class="abre">Um argumento moral junta ao menos uma premissa de fato e uma de valor, e tira delas uma conclusão sobre o que fazer. Se as premissas são verdadeiras e a lógica é válida, a conclusão precisa ser aceita, mesmo que incomode.</p>
<h2>A forma básica</h2>
<ol class="roteiro">
<li><strong>Premissa de valor:</strong> é errado causar sofrimento intenso a alguém sem necessidade.</li>
<li><strong>Premissa de fato:</strong> esta prática causa sofrimento intenso sem necessidade.</li>
<li><strong>Conclusão:</strong> esta prática é errada.</li>
</ol>
<p>Para discordar da conclusão, é preciso atacar uma das premissas: ou o sofrimento não é tão intenso, ou há necessidade, ou a regra do passo 1 tem exceções. Dizer “não gosto da conclusão” não é um contra-argumento. Esse é o ganho de escrever o argumento em passos: a discordância fica localizada.</p>
<h2>Coerência: a ferramenta mais poderosa</h2>
<p>A maior parte do avanço em ética não veio de descobrir valores novos, e sim de notar incoerências nos valores antigos. Quem defendia “todos os homens nascem iguais” e mantinha escravizados estava em contradição, e a contradição acabou cedendo. O teste é simples: <strong>casos iguais devem ser tratados igualmente, a menos que haja uma diferença relevante</strong>. Se você julga dois casos de forma diferente, precisa dizer qual diferença justifica isso, e por que ela importa.</p>
<table><thead><tr><th>Juízo A</th><th>Juízo B</th><th>Pergunta de coerência</th></tr></thead><tbody>
<tr><td>Bater em um cão por diversão é errado</td><td>Confinar um porco a vida inteira para comer mais barato é aceitável</td><td>Que diferença entre cão e porco justifica isso?</td></tr>
<tr><td>Corrupção do adversário é inaceitável</td><td>Corrupção do meu lado é “jogo político”</td><td>O ato mudou, ou só o autor?</td></tr>
<tr><td>Devo salvar uma criança que se afoga à minha frente</td><td>Não preciso doar para salvar uma criança distante</td><td>A distância muda o valor da vida?</td></tr>
</tbody></table>
<h2>Intuições: dado ou veredito?</h2>
<p>Intuições morais, aquela reação imediata de “isso é errado”, são o ponto de partida de quase toda discussão. Elas são dados importantes: uma teoria que diz que torturar inocentes por diversão é bom tem algo errado. Mas intuições também já aprovaram a escravidão e a queima de bruxas. O método da filosofia é ir e voltar: usar intuições para testar princípios, e princípios para corrigir intuições, até chegar a um conjunto coerente. John Rawls chamou isso de <strong>equilíbrio reflexivo</strong>.</p>
<h2>Erros comuns</h2>
<ul>
<li><strong>Apelo à natureza:</strong> “é natural, logo é bom”. Veja <a href="fatos-e-valores.html">fatos e valores</a>.</li>
<li><strong>Apelo à maioria ou à tradição:</strong> popularidade e antiguidade não são razões morais.</li>
<li><strong>Ad hominem:</strong> atacar quem argumenta em vez do argumento. Um hipócrita pode ter razão.</li>
<li><strong>Falso dilema:</strong> “ou aceita tudo, ou é contra tudo”. Quase sempre há posições intermediárias.</li>
<li><strong>Bola de neve sem evidência:</strong> “se permitirmos X, logo virá Y”. Às vezes é verdade, mas precisa ser mostrado.</li>
<li><strong>Confundir explicar com justificar:</strong> saber por que alguém fez algo não diz se foi certo.</li>
<li><strong>Relativismo de conveniência:</strong> “quem sou eu para julgar?” só quando a conclusão incomoda.</li>
</ul>
<h2>Um bom argumento aceita ser testado</h2>
<p>Quem argumenta de boa-fé diz o que o faria mudar de ideia. Se nenhuma evidência e nenhum caso contrário podem abalar uma posição, ela deixou de ser um argumento e virou uma identidade. Veja <a href="como-discutir-etica.html">como discutir ética</a> e, para falácias em detalhe, o <a href="https://guiadeargumentacao.biblioverse.org/" target="_blank" rel="noopener">Guia de Argumentação</a>.</p>
''', fontes=[('Reflective Equilibrium (Stanford Encyclopedia)', SEP + 'reflective-equilibrium/'), ('Moral Reasoning (Stanford Encyclopedia)', SEP + 'reasoning-moral/'), RACHELS]),

dict(slug='mapa-das-teorias', grupo='As grandes famílias', titulo='Resultado, regra ou caráter? O mapa das teorias', resumo='As teorias da ética normativa se dividem pelo que colocam no centro: as consequências, os deveres ou quem você é. Nenhuma ignora o resto.', corpo='''
<p class="abre">A ética normativa pergunta o que torna uma ação certa ou errada. As respostas se organizam em famílias, e cada família se define pelo que coloca no <strong>ponto focal</strong>: o que mais deve pesar quando se decide.</p>
<p>Um aviso antes do mapa: dizer que o consequencialismo foca nos resultados não quer dizer que ele ignore regras, nem que a deontologia ignore resultados. Todas as teorias sérias olham para tudo. A diferença está no que vem primeiro quando os critérios entram em conflito.</p>
<div class="tres">
<div><h3>Consequencialismo</h3><p><strong>O que mais deve importar é o resultado.</strong> Uma ação é certa quando produz o melhor estado de coisas para os afetados.</p><p class="pol">Pergunta típica: “quem fica melhor, quem fica pior, e quanto?”</p></div>
<div><h3>Deontologia</h3><p><strong>O que mais deve importar são regras e deveres.</strong> Algumas coisas não se fazem, e alguns direitos não se violam, mesmo que o resultado fosse bom.</p><p class="pol">Pergunta típica: “isso respeita cada pessoa como um fim, e não como um meio?”</p></div>
<div><h3>Éticas do caráter</h3><p><strong>O que mais deve importar é quem você é.</strong> Agir bem é agir como uma pessoa virtuosa e cuidadosa agiria.</p><p class="pol">Pergunta típica: “que tipo de pessoa esta escolha me torna?”</p></div>
</div>
<h2>As outras respostas</h2>
<table><thead><tr><th>Família</th><th>Ponto focal</th><th>Em uma frase</th></tr></thead><tbody>
<tr><td><a href="teorias/contratualismo-rawlsiano.html">Contratualismo</a></td><td>O acordo que pessoas razoáveis fariam</td><td>Certo é o que ninguém poderia rejeitar razoavelmente</td></tr>
<tr><td><a href="teorias/egoismo-etico.html">Egoísmo ético</a></td><td>O próprio interesse</td><td>Cada um deve cuidar de si; o resto segue disso</td></tr>
<tr><td><a href="teorias/relativismo-cultural.html">Relativismo</a></td><td>A cultura ou a pessoa</td><td>Certo e errado dependem de quem julga</td></tr>
<tr><td><a href="teorias/ceticismo-normativo.html">Ceticismo</a></td><td>Nenhum</td><td>Talvez não haja padrão algum para descobrir</td></tr>
</tbody></table>
<h2>Um caso para ver a diferença</h2>
<p>Você promete visitar um amigo doente. No caminho, encontra um desconhecido ferido, e ajudá-lo faria você faltar à visita.</p>
<ul>
<li><strong>Consequencialista:</strong> compara os resultados. O ferido provavelmente ganha mais com a ajuda do que o amigo perde com a falta. Ajuda.</li>
<li><strong>Deontologista:</strong> reconhece o dever de ajudar e o dever de cumprir a promessa. Em geral, o dever de socorro vence, mas a promessa não deixa de contar: deve explicar-se ao amigo e compensar.</li>
<li><strong>Ética das virtudes:</strong> pergunta o que uma pessoa compassiva e confiável faria. Ajudaria o ferido, e cuidaria depois do amigo, sem transformar nenhum dos dois em número.</li>
</ul>
<p>Repare que, neste caso, as três chegam ao mesmo lugar por caminhos diferentes. É o que acontece na maior parte da vida. As teorias se separam nos casos de conflito, e é para eles que os <a href="dilemas.html">dilemas clássicos</a> existem.</p>
<h2>Dentro de cada família, muitas variantes</h2>
<p>Dizer “sou consequencialista” ainda não diz como somar o bem de várias pessoas, nem quanto pesa o sofrimento diante do prazer. Dizer “sou deontologista” não diz se as regras são absolutas ou cedem em catástrofes. O <a href="teorias.html">catálogo de teorias</a> detalha essas variantes, e o <a href="https://ethicstest.biblioverse.org/" target="_blank" rel="noopener">Teste de Visão Moral</a> ajuda a descobrir onde você está.</p>
<div class="nota"><strong>Para guardar:</strong> as famílias se distinguem pelo que pesa mais, não pelo que ignoram. Quase ninguém segue uma teoria só, e isso não é defeito: é o que a vida real pede.</div>
<div class="cta"><a class="btn" href="teorias.html">Ver todas as teorias</a><a class="btn alt" href="https://ethicstest.biblioverse.org/" target="_blank" rel="noopener">Fazer o Teste de Visão Moral</a></div>
''', fontes=[MAPA, ('Normative Ethics (Internet Encyclopedia of Philosophy)', IEP + 'ethics/#H3'), ('Ética normativa (Wikipédia)', WP + '%C3%89tica_normativa'), VINDING]),

dict(slug='consequencialismo', grupo='As grandes famílias', titulo='Consequencialismo: quando o resultado pesa mais', resumo='Uma ação é certa quando produz o melhor resultado para todos os afetados. Simples de dizer, difícil de aplicar, e muito influente.', corpo='''
<p class="abre">Para o consequencialismo, o que mais deve importar em uma ação são as suas consequências: o quanto ela melhora ou piora a vida de todos os afetados. A versão mais conhecida é o utilitarismo.</p>
<h2>A ideia em três passos</h2>
<ol class="roteiro">
<li><strong>Só o bem-estar conta no fim:</strong> regras, intenções e tradições importam na medida em que afetam como as vidas correm.</li>
<li><strong>Todos contam igualmente:</strong> a dor de um desconhecido vale tanto quanto a do seu vizinho. Jeremy Bentham resumiu: cada um conta por um, e ninguém por mais de um.</li>
<li><strong>Escolha a melhor opção disponível:</strong> não a perfeita, e sim a que, entre as alternativas reais, produz mais bem e menos mal.</li>
</ol>
<h2>O que torna a ideia atraente</h2>
<ul>
<li><strong>É imparcial por construção:</strong> não há lugar para privilegiar a própria tribo, raça ou espécie. Foi por isso que Bentham, já em 1789, incluiu os animais: a pergunta não é se raciocinam, e sim se podem sofrer.</li>
<li><strong>Olha para quem é afetado:</strong> em vez de perguntar se uma regra foi violada, pergunta se alguém foi prejudicado.</li>
<li><strong>Admite exceções com razão:</strong> mentir é quase sempre ruim porque quase sempre causa dano. Quando salva uma vida, a conta muda.</li>
<li><strong>Puxou reformas:</strong> utilitaristas estiveram entre os primeiros a defender o fim da escravidão, o voto feminino, a descriminalização da homossexualidade e a proteção dos animais.</li>
</ul>
<h2>As decisões dentro da família</h2>
<p>Dizer “o resultado pesa mais” ainda deixa perguntas abertas. Cada resposta gera uma variante, e o <a href="teorias.html">catálogo</a> detalha todas:</p>
<table><thead><tr><th>Pergunta</th><th>Respostas</th></tr></thead><tbody>
<tr><td>Avaliar cada ato ou seguir regras que em geral dão bons resultados?</td><td><a href="teorias/consequencialismo-de-ato.html">De ato</a>, <a href="teorias/consequencialismo-de-regras.html">de regras</a>, ou dois níveis</td></tr>
<tr><td>Como juntar o bem de várias pessoas?</td><td>Somar tudo (<a href="teorias/utilitarismo-classico.html">utilitarismo clássico</a>), dar peso extra a quem está pior (<a href="teorias/prioritarismo.html">prioritarismo</a>), garantir um mínimo (<a href="teorias/suficientismo.html">suficientismo</a>), olhar só o pior caso (<a href="teorias/maximin.html">maximin</a>), ou a igualdade (<a href="teorias/igualitarismo.html">igualitarismo</a>)</td></tr>
<tr><td>Sofrimento e prazer pesam igual?</td><td>Simétrico, <a href="teorias/prioridade-ao-sofrimento.html">prioridade ao sofrimento</a>, ou <a href="teorias/utilitarismo-negativo.html">negativo</a></td></tr>
<tr><td>O que é bem-estar?</td><td>Prazer e ausência de dor, satisfação de preferências, ou uma lista de bens</td></tr>
</tbody></table>
<h2>As objeções mais fortes</h2>
<ul>
<li><strong>Pode sacrificar inocentes:</strong> se matar um salva cinco, a conta parece aprovar. Quase todo consequencialista responde com regras, incerteza e efeitos de longo prazo, mas a objeção segue viva. Veja o <a href="dilemas/transplante.html">dilema do transplante</a>.</li>
<li><strong>Exige demais:</strong> se cada real pode salvar alguém, por que não doar quase tudo? Veja <a href="quanto-a-moral-pode-exigir.html">quanto a moral pode exigir</a>.</li>
<li><strong>Ninguém sabe o futuro:</strong> as consequências são incertas. A resposta é agir pelo resultado esperado, com o melhor conhecimento disponível.</li>
<li><strong>Ignora a separação entre pessoas:</strong> John Rawls objetou que somar o bem de todos trata a sociedade como se fosse uma pessoa só.</li>
</ul>
<div class="nota"><strong>Cuidado com a caricatura:</strong> “o fim justifica os meios” não é o lema do consequencialismo. Os meios têm consequências, inclusive as de longo prazo, e um consequencialista honesto as inclui todas na conta. Veja o <a href="utilitarismo-classico.html">utilitarismo clássico</a> no nível Intermediário.</div>
''', fontes=[('Consequentialism (Stanford Encyclopedia)', SEP + 'consequentialism/'), ('Utilitarianism.net', 'https://utilitarianism.net/'), ('Uma Introdução aos Princípios da Moral e da Legislação (1789)', WP + 'Jeremy_Bentham'), MAPA]),

dict(slug='deontologia', grupo='As grandes famílias', titulo='Deontologia: quando deveres e direitos pesam mais', resumo='Algumas coisas não se fazem, mesmo com bons resultados. A deontologia explica por que cada pessoa é um fim, e não um meio.', corpo='''
<p class="abre">Para a deontologia, o que mais deve importar em uma ação são os deveres que ela cumpre ou viola e os direitos que ela respeita ou atropela. O nome vem do grego <em>déon</em>, dever.</p>
<h2>A ideia central</h2>
<p>Há coisas que não se fazem com uma pessoa, não importa o ganho: torturá-la, escravizá-la, usá-la como instrumento sem o seu consentimento. Esses limites valem porque cada pessoa tem um valor que não se soma nem se troca. Immanuel Kant formulou isso como tratar a humanidade sempre como <strong>fim</strong>, nunca apenas como <strong>meio</strong>.</p>
<p>Disso saem dois tipos de regra:</p>
<div class="passos"><div><span>✕</span><h3>Restrições</h3><p>O que não se pode fazer, nem por bons motivos: matar inocentes, mentir, quebrar promessas, trair confiança.</p></div><div><span>✓</span><h3>Deveres positivos</h3><p>O que se deve fazer: socorrer, cumprir o prometido, cuidar de quem depende de você, dizer a verdade.</p></div></div>
<h2>O que torna a ideia atraente</h2>
<ul>
<li><strong>Protege o indivíduo contra a maioria:</strong> ninguém pode ser sacrificado porque a conta fecha. É a base dos direitos humanos e das constituições.</li>
<li><strong>Dá previsibilidade:</strong> você sabe o que esperar de uma pessoa de princípios. Promessas valem porque não dependem do humor do dia.</li>
<li><strong>Reconhece a separação entre pessoas:</strong> a dor de um não é compensada pelo prazer de outro, porque são vidas diferentes.</li>
<li><strong>Combina com nossas intuições mais fortes:</strong> quase todo mundo sente que empurrar alguém do alto para parar um bonde é diferente de desviar o bonde, mesmo que o número de mortos seja igual.</li>
</ul>
<h2>As decisões dentro da família</h2>
<table><thead><tr><th>Pergunta</th><th>Respostas</th></tr></thead><tbody>
<tr><td>De onde vêm as regras?</td><td>Da razão (<a href="teorias/deontologia-kantiana.html">Kant</a>), de direitos básicos (<a href="teorias/deontologia-de-direitos.html">direitos como trunfos</a>), de Deus (<a href="teorias/teoria-do-mandamento-divino.html">mandamento divino</a>), de vários deveres sem hierarquia fixa (<a href="teorias/deontologia-pluralista.html">Ross</a>)</td></tr>
<tr><td>As regras cedem em catástrofes?</td><td>Nunca (<a href="teorias/deontologia-absolutista.html">absolutista</a>) ou só acima de um limiar (<a href="teorias/deontologia-de-limiar.html">de limiar</a>)</td></tr>
<tr><td>Importa se o dano foi pretendido ou só previsto?</td><td>Sim, para a <a href="teorias/doutrina-do-duplo-efeito.html">doutrina do duplo efeito</a></td></tr>
</tbody></table>
<h2>As objeções mais fortes</h2>
<ul>
<li><strong>Regras entram em conflito:</strong> e aí? Kant achava que mentir é sempre errado, mesmo para um assassino que pergunta onde está sua vítima. Poucos aceitam isso hoje. Veja <a href="dilemas/mentir-ao-assassino.html">o dilema</a>.</li>
<li><strong>Pode produzir catástrofes:</strong> se nenhuma regra cede, uma cidade inteira pode morrer para que uma mentira não seja dita. A deontologia de limiar nasceu dessa objeção.</li>
<li><strong>Por que a regra?</strong> Se mentir é errado porque prejudica, então o que importa no fim é o prejuízo, e estamos de volta às consequências. Deontologistas respondem que o erro está em desrespeitar, não só em prejudicar.</li>
<li><strong>Quem tem direitos?</strong> Se só seres racionais contam, bebês e animais ficariam fora. Muitos deontologistas hoje, como Tom Regan e Christine Korsgaard, estendem a ideia a quem tem uma vida que importa para si.</li>
</ul>
<div class="nota"><strong>Cuidado com a caricatura:</strong> deontologia não é “seguir regras cegamente”. É a ideia de que algumas coisas se devem às pessoas por serem pessoas, antes de qualquer conta. Veja <a href="kant-e-o-imperativo-categorico.html">Kant</a> no nível Intermediário.</div>
''', fontes=[('Deontological Ethics (Stanford Encyclopedia)', SEP + 'ethics-deontological/'), ('Deontologia (Wikipédia)', WP + 'Deontologia'), ('Fundamentação da Metafísica dos Costumes', WP + 'Fundamenta%C3%A7%C3%A3o_da_Metaf%C3%ADsica_dos_Costumes'), MAPA]),

dict(slug='etica-do-carater', grupo='As grandes famílias', titulo='Virtudes e cuidado: quando quem você é pesa mais', resumo='Em vez de perguntar “o que devo fazer?”, pergunte “que pessoa devo ser?”. As éticas do caráter colocam o foco em traços e relações.', corpo='''
<p class="abre">As éticas do caráter deslocam a pergunta. Em vez de avaliar cada ato pelo resultado ou pela regra, perguntam que traços uma boa pessoa cultiva e o que ela faria nesta situação. As duas correntes principais são a ética das virtudes e a ética do cuidado.</p>
<h2>Ética das virtudes</h2>
<p>Aristóteles defendeu que o objetivo da vida é a <em>eudaimonia</em>, uma vida realizada e florescente, e que ela se alcança pelo exercício das virtudes: coragem, justiça, generosidade, temperança, honestidade, compaixão. Uma virtude é um traço estável, e não um ato isolado: a pessoa corajosa age com coragem de forma confiável, no momento certo e na medida certa.</p>
<p>O ponto focal é o <strong>agente</strong>. Uma ação é certa quando é o que uma pessoa virtuosa faria naquelas circunstâncias. Isso não ignora consequências nem regras: a pessoa prudente pensa nos resultados, e a pessoa justa respeita direitos. Mas a prioridade está em formar o caráter, porque regras não antecipam todas as situações e cálculos não dizem quem você se torna.</p>
<table><thead><tr><th>Virtude</th><th>A falta</th><th>O excesso</th></tr></thead><tbody>
<tr><td>Coragem</td><td>Covardia</td><td>Temeridade</td></tr>
<tr><td>Generosidade</td><td>Avareza</td><td>Esbanjamento</td></tr>
<tr><td>Confiança em si</td><td>Humildade excessiva</td><td>Arrogância</td></tr>
<tr><td>Honestidade</td><td>Dissimulação</td><td>Franqueza cruel</td></tr>
</tbody></table>
<p>A tabela ilustra o “meio-termo” aristotélico: a virtude fica entre dois vícios. Não é mediocridade, e sim acerto.</p>
<h2>Ética do cuidado</h2>
<p>Nascida nos anos 1980 com Carol Gilligan e Nel Noddings, a ética do cuidado observa que as teorias tradicionais partem de indivíduos independentes que negociam regras. Mas a vida moral começa em relações de dependência: bebês, doentes, idosos, todos nós em algum momento. O ponto focal é a <strong>relação</strong>: atenção às necessidades concretas de quem depende de você, e a disposição de responder a elas.</p>
<p>O cuidado não é só sentimento. Envolve perceber, responder com competência e verificar se a resposta funcionou. E ele se estende: cuidar dos próximos não exclui ampliar a atenção para quem está longe e para outros animais, que também são vulneráveis.</p>
<h2>O que torna essas éticas atraentes</h2>
<ul>
<li><strong>São realistas sobre as pessoas:</strong> ninguém decide cada ato com uma planilha. Agimos pelo que somos.</li>
<li><strong>Dão lugar às emoções:</strong> compaixão e indignação não são ruído, e sim parte de perceber bem.</li>
<li><strong>Valorizam o concreto:</strong> este doente, esta promessa, esta amizade, e não só “a soma do bem”.</li>
<li><strong>Explicam a educação moral:</strong> aprendemos a ser bons por exemplo e prática, não por teoremas.</li>
</ul>
<h2>As objeções</h2>
<ul>
<li><strong>Não diz o que fazer:</strong> “faça o que a pessoa virtuosa faria” ajuda pouco em um dilema novo. Rosalind Hursthouse responde que as virtudes geram regras práticas (“aja com honestidade”, “não aja com crueldade”), e que a vagueza é da vida, não da teoria.</li>
<li><strong>Virtudes variam entre culturas:</strong> a coragem do guerreiro não é a do enfermeiro. Defensores dizem que o núcleo (justiça, compaixão, honestidade) é bem estável.</li>
<li><strong>O cuidado pode ser parcial:</strong> cuidar dos “meus” pode virar desculpa para ignorar os outros. Virginia Held e outras autoras defendem um cuidado que se expande, e não um cuidado só para dentro.</li>
</ul>
<div class="nota"><strong>Para guardar:</strong> o foco em quem você é não nega resultados nem regras. Ele lembra que, no fim, são pessoas que agem, e que formar boas pessoas é tão importante quanto achar as regras certas. Veja <a href="aristoteles-e-as-virtudes.html">Aristóteles</a> e a <a href="etica-do-cuidado.html">ética do cuidado</a> no Intermediário.</div>
''', fontes=[('Virtue Ethics (Stanford Encyclopedia)', SEP + 'ethics-virtue/'), ('Care Ethics (Internet Encyclopedia of Philosophy)', IEP + 'care-ethics/'), ('Ética a Nicômaco', WP + '%C3%89tica_a_Nic%C3%B4maco'), MAPA]),

dict(slug='egoismo-relativismo-e-ceticismo', grupo='As grandes famílias', titulo='Egoísmo, relativismo e ceticismo: há um padrão?', resumo='Três posições que desafiam a ideia de uma moral comum: cada um por si, cada cultura com a sua, ou nenhuma resposta. Vale entender o que dizem e onde falham.', corpo='''
<p class="abre">Nem toda teoria aceita que exista um critério moral válido para todos. O egoísmo ético coloca o próprio interesse no centro; o relativismo diz que certo e errado dependem de quem julga; o ceticismo duvida que haja resposta. Elas são mais populares em conversas do que em filosofia, e por boas razões.</p>
<h2>Egoísmo ético</h2>
<p>O egoísmo <em>psicológico</em> é uma tese de fato: as pessoas sempre agem por interesse próprio. O egoísmo <em>ético</em> é uma tese de valor: cada pessoa <strong>deve</strong> agir pelo próprio interesse. São coisas diferentes, e a primeira é provavelmente falsa: pessoas se sacrificam por estranhos, e dizer que “no fundo” fizeram isso por prazer esvazia a palavra interesse.</p>
<p>O egoísmo ético tem um argumento sério: cada um conhece melhor as próprias necessidades, e um mundo em que todos cuidam de si pode funcionar bem. Mas enfrenta problemas:</p>
<ul>
<li><strong>Não resolve conflitos:</strong> se o meu interesse e o seu colidem, a teoria manda cada um vencer o outro. Não é uma moral, é a ausência de uma.</li>
<li><strong>É arbitrário:</strong> por que a minha dor conta e a sua não, se são iguais? A única diferença é que uma é minha. Isso é tão arbitrário quanto dizer que só a dor dos ruivos conta.</li>
<li><strong>Quase ninguém o defende em público:</strong> o egoísta que convence os outros a serem altruístas vive melhor. Uma teoria que não pode ser recomendada tem algo errado.</li>
</ul>
<h2>Relativismo moral</h2>
<p>O relativismo <em>descritivo</em> observa que sociedades diferem sobre o que é certo. É verdade, embora menos do que parece: proibições de matar, roubar e trair aparecem em todas, e as diferenças costumam estar nos fatos (“o que acontece depois da morte?”) e no círculo de quem conta. O relativismo <em>normativo</em> vai além: diz que cada cultura, ou cada pessoa, tem a sua verdade moral, e que não cabe julgar de fora.</p>
<table><thead><tr><th>O que o relativismo acerta</th><th>Onde falha</th></tr></thead><tbody>
<tr><td>Humildade: nossa cultura também tem pontos cegos</td><td>Impede dizer que a escravidão era errada, e não só “diferente”</td></tr>
<tr><td>Muita coisa é mesmo convenção, como vestir-se ou comer</td><td>Trata o sofrimento de uma vítima como “cultura” de quem a oprime</td></tr>
<tr><td>Julgar de fora já serviu para dominar</td><td>Não permite progresso: se cada época está certa por definição, nada melhora</td></tr>
<tr><td>Tolerância é um valor importante</td><td>Mas é um valor que o relativista quer que valha para todos, o que o contradiz</td></tr>
</tbody></table>
<p>A pergunta que derruba o relativismo cultural é simples: quem fala pela cultura? Dentro de qualquer sociedade há quem discorda, e quase sempre é quem sofre com a prática. Veja <a href="relativismo-e-quietismo.html">relativismo e quietismo</a> no nível Avançado.</p>
<h2>Ceticismo normativo</h2>
<p>O cético diz que talvez não haja fato nenhum sobre o que é certo, e que juízos morais só expressam atitudes. É uma posição séria em metaética, discutida no Avançado. Mas ela não dispensa ninguém de agir: o cético também decide se mente, se ajuda, se come carne. Por isso o <a href="https://ethicstest.biblioverse.org/map.html" target="_blank" rel="noopener">Teste de Visão Moral</a> pergunta ao cético qual é a sua <em>tendência prática</em>. Mesmo quem duvida da teoria tem uma prática, e ela pode ser mais ou menos coerente.</p>
<h2>Por que estudar posições que a maioria rejeita</h2>
<p>Porque elas aparecem disfarçadas. “Quem sou eu para julgar?” costuma ser relativismo usado só quando a conclusão incomoda. “Todo mundo pensa em si” costuma ser egoísmo psicológico usado para desculpar o egoísmo ético. Reconhecer a posição ajuda a responder a ela.</p>
''', fontes=[('Egoism (Stanford Encyclopedia)', SEP + 'egoism/'), ('Moral Relativism (Stanford Encyclopedia)', SEP + 'moral-relativism/'), ('Moral Skepticism (Stanford Encyclopedia)', SEP + 'skepticism-moral/'), RACHELS]),

dict(slug='circulo-moral', grupo='Quem conta', titulo='O círculo moral: quem conta e por quê', resumo='Toda ética precisa dizer quem merece consideração direta. A resposta depende do critério: senciência, razão, laços ou espécie.', corpo='''
<p class="abre">O círculo moral é o conjunto de seres cujos interesses contam por si mesmos, e não só pelo efeito sobre outros. Toda teoria ética precisa traçar essa fronteira, e a escolha do critério muda tudo o que vem depois.</p>
<h2>Consideração direta e indireta</h2>
<p>Quase todo mundo acha errado chutar um cão. Mas há duas razões possíveis. Uma é indireta: isso embrutece quem chuta, ou incomoda o dono. Outra é direta: o cão sofre, e o sofrimento dele conta. Kant deu a primeira resposta; Bentham, a segunda. Quem está <em>dentro</em> do círculo recebe consideração direta. Quem está fora só conta quando afeta alguém de dentro.</p>
<h2>Os critérios possíveis</h2>
<table><thead><tr><th>Critério</th><th>Quem entra</th><th>Problema</th></tr></thead><tbody>
<tr><td>Ser eu</td><td>Só eu</td><td>Arbitrário: por que a minha dor e não a sua?</td></tr>
<tr><td>Laços</td><td>Minha família, meu grupo</td><td>Permite indiferença ao estranho que sofre igual</td></tr>
<tr><td>Espécie</td><td>Todos os humanos</td><td>Por que a espécie, e não a cor ou o sexo? O que ela muda?</td></tr>
<tr><td>Racionalidade</td><td>Quem raciocina</td><td>Exclui bebês e pessoas com deficiência grave, e inclui máquinas que raciocinem</td></tr>
<tr><td>Senciência</td><td>Quem pode sentir dor e prazer</td><td>Pede saber quem sente, o que a ciência ainda estuda</td></tr>
<tr><td>Vida</td><td>Todo ser vivo</td><td>O que uma bactéria tem a perder?</td></tr>
<tr><td>Ecossistemas</td><td>Rios, florestas, biomas</td><td>Um ecossistema não sente nada; os animais nele, sim</td></tr>
</tbody></table>
<h2>A pergunta que organiza o debate</h2>
<p>Para incluir ou excluir alguém, é preciso apontar uma <strong>diferença relevante</strong>. A cor da pele não muda a capacidade de sofrer, e por isso não serviu como razão para excluir. O sexo não muda a capacidade de decidir, e por isso não serviu. A pergunta de hoje é: a espécie muda algo relevante? Um porco não faz matemática, mas também um bebê não faz, e o bebê está dentro. Se o que importa é poder sofrer, a fronteira passa pela senciência, e não pela espécie.</p>
<p>Esse é o argumento de Peter Singer em <em>Libertação Animal</em>, retomando Bentham: a pergunta não é “podem raciocinar?”, mas “podem sofrer?”. Quem rejeita a conclusão precisa dizer qual é a diferença relevante. Veja <a href="especismo.html">especismo</a>.</p>
<h2>Três perguntas extras</h2>
<p>Decidir que seres sencientes contam ainda deixa perguntas, que o <a href="https://ethicstest.biblioverse.org/map.html" target="_blank" rel="noopener">Teste de Visão Moral</a> separa:</p>
<ul>
<li><strong>Gradualismo:</strong> a inteligência muda o peso do sofrimento? Uma dor igual conta igual em um humano e em um frango? Veja <a href="gradualismo.html">gradualismo</a>.</li>
<li><strong>Tempo:</strong> quem vai existir daqui a cem anos conta tanto quanto quem existe hoje? Veja <a href="geracoes-futuras.html">gerações futuras</a>.</li>
<li><strong>Substrato:</strong> se uma máquina vier a sentir, ela conta? Ou só mentes biológicas? Veja <a href="mentes-artificiais.html">mentes artificiais</a>.</li>
</ul>
<h2>Posições com nome</h2>
<p><a href="teorias/antropocentrismo.html">Antropocentrismo</a> (só humanos), <a href="teorias/sencientismo.html">sencientismo</a> (quem sente), <a href="teorias/biocentrismo.html">biocentrismo</a> (toda vida) e <a href="teorias/ecocentrismo.html">ecocentrismo</a> (os sistemas naturais) são as principais. Elas podem se combinar: dá para achar que seres sencientes contam por si e que florestas contam também. O que não dá é fugir da pergunta: quem conta, e o que justifica a fronteira exatamente ali?</p>
<p>A seção de <a href="criterios.html">critérios éticos</a> compara as seis delimitações lado a lado: quem tem valor direto em cada uma, a razão alegada, o que cada uma deixa passar e onde é forte ou fraca.</p>
<div class="cta"><a class="btn" href="ferramentas/meu-circulo-moral.html">Monte o seu círculo moral</a></div>
''', fontes=[('Moral Status (Stanford Encyclopedia)', SEP + 'grounds-moral-status/'), ('Libertação Animal', WP + 'Liberta%C3%A7%C3%A3o_Animal'), ('The Expanding Circle', 'https://www.google.com/search?tbm=bks&q=Peter+Singer+The+Expanding+Circle'), MAPA]),

dict(slug='expansao-do-circulo-moral', grupo='Quem conta', titulo='A expansão do círculo moral na história', resumo='Escravizados, mulheres, estrangeiros e outros grupos já ficaram fora de quem “conta”. O círculo cresceu, e talvez não tenha terminado.', corpo='''
<p class="abre">Durante a maior parte da história, a maioria das pessoas achou normal que alguns humanos não contassem: escravizados, mulheres, estrangeiros, pessoas de outra religião. O círculo de quem merece consideração se ampliou aos poucos. Peter Singer chamou esse movimento de <strong>expansão do círculo moral</strong>.</p>
<h2>Uma linha do tempo resumida</h2>
<table><thead><tr><th>Quem ficava de fora</th><th>A razão alegada</th><th>O que mudou</th></tr></thead><tbody>
<tr><td>Escravizados</td><td>Origem, cor, “natureza inferior”</td><td>Abolição no Brasil em 1888, última das Américas</td></tr>
<tr><td>Mulheres</td><td>Sexo, “emoção demais, razão de menos”</td><td>Voto feminino no Brasil em 1932</td></tr>
<tr><td>Pessoas de outra religião</td><td>“Infiéis”</td><td>Liberdade religiosa como direito</td></tr>
<tr><td>Pessoas LGBT</td><td>“Antinatural”, “doença”</td><td>Despatologização; união reconhecida no Brasil em 2011</td></tr>
<tr><td>Crianças</td><td>“Propriedade dos pais”</td><td>Direitos da criança; fim do castigo físico legal em muitos países</td></tr>
<tr><td>Estrangeiros</td><td>Lugar de nascimento</td><td>Direitos humanos universais, em teoria; na prática, ainda em disputa</td></tr>
<tr><td>Animais</td><td>Espécie</td><td>Leis contra crueldade; reconhecimento da senciência em várias legislações. Em disputa</td></tr>
</tbody></table>
<h2>O motor da expansão</h2>
<p>O que empurra o círculo para fora não é só sentimento. É um argumento de <a href="imparcialidade.html">coerência</a>: tratar casos iguais de forma igual, a menos que haja uma diferença relevante. Cada exclusão se apoiava em uma diferença, e a diferença se mostrou irrelevante para o que estava em jogo. A cor da pele não muda a capacidade de sofrer; o sexo não muda a capacidade de decidir. Quase todo avanço moral foi descobrir que uma diferença tratada como importante não era.</p>
<p>Houve outros motores: convivência (conhecer “o outro” desfaz estereótipos), ativismo (quase toda conquista teve quem pagasse caro por ela), ciência (saber quem sente e o que sente) e prosperidade (com menos medo, é mais fácil incluir).</p>
<h2>Isso é progresso ou só mudança?</h2>
<p>Se cada época só julga pelos próprios valores, “progresso” seria o nome que damos à nossa opinião. Mas há um teste melhor: a mudança corrigiu uma incoerência? Defender a liberdade e manter escravizados era contradição. Dizer que a dor importa e ignorar a dor das mulheres era contradição. Por isso dá para falar em progresso, e não só em moda. Veja <a href="progresso-moral.html">progresso moral</a> no Avançado.</p>
<h2>O círculo não cresce sozinho</h2>
<p>Ele também encolhe. A Alemanha de Weimar virou o nazismo em poucos anos, e grupos antes incluídos foram expulsos do círculo. Genocídios começam quando um grupo é descrito como menos humano. Por isso, a expansão não é uma lei da história, e sim um trabalho que cada geração faz ou desfaz.</p>
<h2>Quem está na fronteira hoje</h2>
<ul>
<li><strong>Animais:</strong> bilhões vivem e morrem em criação industrial. Ver <a href="etica-animal-na-pratica.html">ética animal na prática</a>.</li>
<li><strong>Gerações futuras:</strong> quem ainda não nasceu não vota, e sofre as consequências do que decidimos. Ver <a href="geracoes-futuras.html">gerações futuras</a>.</li>
<li><strong>Pessoas distantes:</strong> a distância ainda pesa mais do que deveria. Ver <a href="dilemas/crianca-no-lago.html">a criança no lago</a>.</li>
<li><strong>Mentes artificiais:</strong> se vierem a sentir, a pergunta se coloca. Ver <a href="mentes-artificiais.html">mentes artificiais</a>.</li>
</ul>
<div class="nota"><strong>Uma pergunta honesta:</strong> é provável que o futuro nos julgue por algo que hoje achamos normal. O que você acha que será?</div>
''', fontes=[('The Expanding Circle', 'https://www.google.com/search?tbm=bks&q=Peter+Singer+The+Expanding+Circle'), ('Moral circle expansion (Wikipédia)', WE + 'Moral_circle_expansion'), ('Moral progress (Wikipédia)', WE + 'Moral_progress'), ('Sentience Institute', 'https://www.sentienceinstitute.org/')]),

dict(slug='imparcialidade', grupo='Quem conta', titulo='Imparcialidade: a regra de ouro, o véu e a universalidade', resumo='Três testes para saber se você defende um princípio ou só o seu lado. Eles não dão a resposta final, mas eliminam as respostas ruins.', corpo='''
<p class="abre">Quase todo mundo acha a própria visão justa. A imparcialidade é o conjunto de testes para descobrir se ela é mesmo, ou se só favorece você e os seus. A ideia é antiga e aparece em quase todas as tradições.</p>
<h2>A regra de ouro</h2>
<p>“Trate os outros como gostaria de ser tratado.” Aparece no confucionismo, no judaísmo, no cristianismo, no islamismo, no hinduísmo e no budismo, com variações. Na forma negativa: não faça aos outros o que não quer para si. Na positiva: faça aos outros o que quer para si.</p>
<p>O limite: nem todos querem as mesmas coisas. Por isso, uma versão melhor pergunta o que <em>aquela pessoa</em> tem razão para querer, e não só o que você quereria no lugar dela.</p>
<h2>O véu da ignorância</h2>
<p>John Rawls propôs imaginar que escolhemos as regras da sociedade sem saber quem seremos nela: rico ou pobre, saudável ou doente, da maioria ou da minoria. O véu retira da conta tudo o que só favorece você. Quem sabe que é rico pode achar a desigualdade natural; sem saber, tende a querer proteções para quem estiver pior.</p>
<p>Mark Rowlands estendeu o véu: e se você também não soubesse a sua espécie? Se poderia nascer frango em uma granja industrial, que regras aceitaria para a criação de animais? Veja o <a href="teorias/contratualismo-estendido.html">contratualismo estendido</a>.</p>
<h2>A universalidade</h2>
<p>Kant perguntou se você poderia querer que a regra da sua ação valesse para todos. R. M. Hare e Peter Singer defendem que julgar moralmente é, por definição, sair do próprio ponto de vista. Uma regra que só funciona quando você está do lado vencedor não é uma regra moral, é uma vantagem disfarçada.</p>
<table><thead><tr><th>Falha de universalidade</th><th>O teste</th></tr></thead><tbody>
<tr><td>“Mentir é errado”, mas as minhas mentiras são “necessárias”</td><td>Eu aceitaria a mesma desculpa de outra pessoa?</td></tr>
<tr><td>“Quem sofre importa”, só se for do meu grupo</td><td>O que justifica a diferença, além de ser do meu grupo?</td></tr>
<tr><td>“Liberdade de expressão”, só para quem concorda</td><td>Eu defenderia esse direito para quem me critica?</td></tr>
<tr><td>“Crueldade é inaceitável”, exceto a que está no meu prato</td><td>O que muda quando a vítima é de outra espécie?</td></tr>
</tbody></table>
<h2>Por que a imparcialidade empurra o círculo</h2>
<p>Os três testes dizem a mesma coisa de formas diferentes: <strong>casos iguais pedem tratamento igual, a menos que haja uma diferença relevante</strong>. É esse princípio que explica a <a href="expansao-do-circulo-moral.html">expansão do círculo moral</a>. Cada vez que uma diferença tratada como importante (cor, sexo, origem) se mostrou irrelevante para o que estava em jogo, a exclusão caiu. A pergunta aberta é quais diferenças ainda tratamos como relevantes sem que sejam.</p>
<h2>Os limites dos testes</h2>
<ul>
<li><strong>Não eliminam os valores:</strong> duas pessoas podem passar pelo véu e escolher diferente, conforme o quanto temem o risco.</li>
<li><strong>Deveres especiais existem:</strong> cuidar mais dos próprios filhos não viola a imparcialidade, desde que não se trate os outros como se não contassem.</li>
<li><strong>Passar no teste não prova que está certo:</strong> os testes eliminam visões ruins com mais facilidade do que confirmam as boas.</li>
<li><strong>Viés continua:</strong> dá para usar o teste só para confirmar o que já se pensava. Veja <a href="vieses-morais.html">vieses morais</a>.</li>
</ul>
<div class="nota"><strong>Para guardar:</strong> uma boa visão moral não é a que faz você se sentir certo. É a que continua de pé quando você troca de lugar com quem ela afeta. Treine na ferramenta <a href="ferramentas/teste-de-troca.html">Teste de troca</a>.</div>
''', fontes=[('Regra de ouro (Wikipédia)', WP + 'Regra_de_ouro'), ('Original Position (Stanford Encyclopedia)', SEP + 'original-position/'), ('Impartiality (Stanford Encyclopedia)', SEP + 'impartiality/'), ('Animals Like Us', 'https://www.google.com/search?tbm=bks&q=Mark+Rowlands+Animals+Like+Us')]),

dict(slug='dilemas-do-cotidiano', grupo='Para o dia a dia', titulo='Dilemas do cotidiano: mentiras, promessas e consumo', resumo='A ética não vive só nos bondes. Ela aparece quando você mente para poupar alguém, quebra uma promessa ou escolhe o que comprar.', corpo='''
<p class="abre">Dilemas de filósofo têm bondes e vilões. Os nossos têm colegas, parentes, carrinhos de compras e notificações de doação. As mesmas ferramentas servem para os dois.</p>
<h2>Mentiras</h2>
<p>“Adorei o presente.” “Já estou chegando.” A maior parte das mentiras do dia a dia é pequena e feita para poupar alguém ou a si mesmo. O que cada família diz:</p>
<ul>
<li><strong>Consequências:</strong> a mentira branca pode ser inofensiva ou até boa, mas cada uma gasta um pouco da confiança geral. A questão é o padrão, não o caso.</li>
<li><strong>Deveres:</strong> mentir trata o outro como alguém que não merece a verdade. Kant era absoluto; a maioria aceita exceções quando a verdade seria crueldade sem propósito.</li>
<li><strong>Caráter:</strong> uma pessoa honesta não é a que despeja verdades, e sim a que encontra o jeito verdadeiro e gentil de falar.</li>
</ul>
<h2>Promessas</h2>
<p>Prometer é criar uma expectativa em alguém que vai agir com base nela. Quebrar uma promessa porque apareceu algo mais interessante é diferente de quebrá-la por uma emergência. O teste de <a href="imparcialidade.html">universalidade</a> ajuda: se todos quebrassem promessas pelo mesmo motivo que você, prometer ainda significaria algo?</p>
<h2>O que você compra</h2>
<p>Cada compra é um voto silencioso sobre como as coisas são produzidas: quem trabalhou, em que condições, que animais foram usados, que dano ambiental ficou para trás. Dois cuidados:</p>
<ul>
<li><strong>Não exija pureza:</strong> ninguém consome sem causar algum dano. A pergunta útil é “entre as opções reais, qual causa menos?”.</li>
<li><strong>Olhe o tamanho do efeito:</strong> a escolha de alimentos tem impacto muito maior do que a de embalagens. Em termos de sofrimento causado, a diferença entre comer ou não produtos de animais criados industrialmente é a maior decisão de consumo que a maioria de nós toma. Veja o <a href="https://ethicalfood.biblioverse.org/pt/" target="_blank" rel="noopener">Guia de Alimentos Éticos</a>.</li>
</ul>
<h2>Doar</h2>
<p>Peter Singer propôs um caso: você vê uma criança se afogando em um lago raso; salvá-la estraga seus sapatos. Ninguém hesita. Então por que hesitamos em doar o valor dos sapatos para salvar uma criança distante? A distância e o fato de haver outros que poderiam ajudar não parecem diferenças moralmente relevantes. O caso é discutido em <a href="dilemas/crianca-no-lago.html">a criança no lago</a>. Mesmo quem não aceita a conclusão radical costuma concordar que doar algo, para organizações que comprovam resultados, é mais do que uma gentileza.</p>
<h2>No trabalho</h2>
<table><thead><tr><th>Situação</th><th>Pergunta útil</th></tr></thead><tbody>
<tr><td>Vi um colega errar e ninguém notou</td><td>Quem é prejudicado pelo erro? A lealdade a ele vale mais do que isso?</td></tr>
<tr><td>Meu chefe pede para omitir algo de um cliente</td><td>Eu aceitaria ser o cliente nesta situação?</td></tr>
<tr><td>Posso levar o crédito por algo que fizemos juntos</td><td>Que pessoa isso me torna, se virar hábito?</td></tr>
<tr><td>Uma regra da empresa é absurda</td><td>Quebrá-la prejudica alguém, ou só é inconveniente?</td></tr>
</tbody></table>
<h2>Um roteiro simples</h2>
<ol class="roteiro">
<li>Quem é afetado, inclusive quem não está na sala?</li>
<li>Qual é o dano e o benefício de cada opção, incluindo a de não fazer nada?</li>
<li>Alguma opção usa alguém como meio, ou quebra uma confiança?</li>
<li>Eu aceitaria essa decisão se estivesse do outro lado?</li>
<li>Que pessoa eu me torno repetindo essa escolha?</li>
</ol>
<p>As cinco perguntas vêm das três famílias de teorias. Elas não dão a resposta sozinhas, mas quase sempre mostram qual opção não passa.</p>
''', fontes=[('Lying (Stanford Encyclopedia)', SEP + 'lying-definition/'), ('Promises (Stanford Encyclopedia)', SEP + 'promises/'), ('Famine, Affluence, and Morality (Wikipédia)', WE + 'Famine,_Affluence,_and_Morality'), SINGER_PE]),

dict(slug='como-discutir-etica', grupo='Para o dia a dia', titulo='Como discutir ética sem brigar', resumo='Separe fato de valor, explique o outro lado de um jeito que ele aceitaria e diga o que o faria mudar de ideia. O resto é tom.', corpo='''
<p class="abre">Discussões morais viram briga porque misturam três coisas: desacordo sobre fatos, desacordo sobre valores e defesa da própria identidade. Separar as três não garante acordo, mas quase sempre melhora a conversa.</p>
<h2>Antes de começar</h2>
<ul>
<li><strong>Localize o desacordo:</strong> “discordamos sobre o que acontece ou sobre o que importa?”. Veja <a href="fatos-e-valores.html">fatos e valores</a>.</li>
<li><strong>Lembre que o outro também acha que é bom:</strong> quase ninguém defende o mal. Jonathan Haidt mostra que pessoas com valores diferentes pesam fundamentos morais de forma diferente, e os dois lados têm pontos cegos. Veja <a href="psicologia-moral.html">psicologia moral</a>.</li>
<li><strong>Escolha o objetivo:</strong> vencer, convencer ou entender? Só os dois últimos valem o tempo.</li>
</ul>
<h2>Durante</h2>
<table><thead><tr><th>Em vez de</th><th>Tente</th></tr></thead><tbody>
<tr><td>“Isso é absurdo”</td><td>“O que te leva a pensar isso?”</td></tr>
<tr><td>Atacar a versão mais fraca do argumento</td><td>Reconstruir a versão mais forte, e responder a ela</td></tr>
<tr><td>“Você só pensa assim porque é X”</td><td>Responder ao argumento, não à biografia</td></tr>
<tr><td>Empilhar exemplos</td><td>Um caso bem escolhido, e perguntar o que o outro diria dele</td></tr>
<tr><td>“Isso é relativo”</td><td>“Que diferença entre os dois casos justifica tratá-los diferente?”</td></tr>
</tbody></table>
<h2>O teste da explicação justa</h2>
<p>Você consegue explicar a posição do outro de um jeito que ele diria “é isso mesmo”? Se não consegue, ainda não entendeu o que está refutando. O exercício costuma revelar que a diferença é menor do que parecia, ou que está em um lugar diferente do esperado.</p>
<h2>Diga o que o faria mudar</h2>
<p>Quem argumenta de boa-fé sabe responder: “que fato ou que caso me faria rever isso?”. Se a resposta é “nada”, a posição virou identidade, e a conversa não é mais sobre ética. Pergunte o mesmo ao outro, com gentileza. Mudar de ideia diante de um bom argumento não é fraqueza: é a única forma de melhorar. Veja <a href="abertura-moral.html">abertura moral</a>.</p>
<h2>Quando o desacordo é de valor mesmo</h2>
<p>Às vezes, depois de limpar os fatos, sobra um desacordo real: uma pessoa dá mais peso à liberdade, outra à proteção. Ainda assim há o que fazer:</p>
<ol class="roteiro">
<li><strong>Coerência:</strong> o valor é aplicado a todos os casos, ou só aos convenientes?</li>
<li><strong>Casos extremos:</strong> o que o valor manda no pior cenário? A pessoa aceita?</li>
<li><strong>Quem paga:</strong> quem sofre com a posição, e essa pessoa teve voz?</li>
<li><strong>Troca de lugar:</strong> a pessoa manteria a posição do outro lado? Veja a <a href="imparcialidade.html">imparcialidade</a>.</li>
</ol>
<h2>O que não funciona</h2>
<p>Humilhar, rotular e vencer no grito confirmam a identidade do outro e o afastam da sua posição. Pesquisas sobre mudança de opinião mostram que respeito e escuta abrem portas que argumento nenhum abre sozinho. Fale primeiro com a pessoa, depois com a ideia.</p>
<div class="nota"><strong>Para guardar:</strong> uma boa discussão moral termina com alguém dizendo “não tinha pensado nisso”. Pode ser você.</div>
''', fontes=[('A Mente Moralista', WE + 'The_Righteous_Mind'), ('Steelmanning (Wikipédia)', WE + 'Straw_man#Steelmanning'), ('Guia de Argumentação', 'https://guiadeargumentacao.biblioverse.org/'), VINDING]),
]
