"""Lições acrescentadas em novembro de 2026: igualdade humana, fazer e deixar acontecer, pobreza, animais selvagens, animais e política, riscos S e X.
Cada lista traz as lições; META_NOVAS e REFORCO_NOVAS, os temas, testes e reforços. POSICAO diz depois de qual lição cada uma entra."""
from licoes_iniciante import SEP, IEP, WP, WE, TESTE, MAPA, VINDING, SINGER_PE
ZOOPOLIS = ('Zoopolis: A Political Theory of Animal Rights', 'https://willkymlicka.ca/publications/books/animals')

POSICAO = {'catastrofes-morais': 'progresso-moral', 'fraqueza-de-vontade': 'vieses-morais', 'igualdade-humana': 'imparcialidade', 'fazer-e-deixar-acontecer': 'objecoes-ao-consequencialismo', 'pobreza-e-etica-global': 'tribalismo-moral', 'sofrimento-dos-animais-selvagens': 'etica-animal-na-pratica', 'animais-e-a-politica': 'sofrimento-dos-animais-selvagens', 'riscos-s-e-riscos-x': 'incerteza-moral'}

NOVAS_INICIANTE = [
dict(slug='igualdade-humana', grupo='Quem conta', titulo='Igualdade humana: em que ela se baseia?', resumo='As pessoas não são iguais em força, talento ou inteligência. Então o que quer dizer que são iguais, e por que isso importa?', corpo='''
<p class="abre">“Todos os seres humanos nascem livres e iguais em dignidade e direitos”, diz a Declaração Universal de 1948. Mas ninguém acha que as pessoas são iguais em altura, memória, talento ou força de vontade. A igualdade humana precisa querer dizer outra coisa, e descobrir o quê é uma das perguntas centrais da ética.</p>
<h2>Igualdade de fato e igualdade de consideração</h2>
<p>A tentação é fundar a igualdade em um fato: “todos têm a mesma capacidade de raciocinar”, por exemplo. O problema é que isso é falso. As capacidades variam, e muito. Se a igualdade dependesse de um fato assim, bastaria mostrar que um grupo tem menos de alguma capacidade para justificar tratá-lo pior, e foi exatamente esse o raciocínio do racismo e do sexismo “científicos”.</p>
<p>Por isso, Peter Singer argumenta que a igualdade não é uma descrição, e sim um <strong>princípio moral</strong>: os interesses de cada pessoa devem receber a mesma consideração, não importa o que ela é capaz de fazer. A dor de quem tem um QI baixo conta tanto quanto a de um gênio, porque dor é dor. É a <strong>igual consideração de interesses</strong>, que você já viu na <a href="imparcialidade.html">imparcialidade</a>.</p>
<table><thead><tr><th>Versão</th><th>O que diz</th><th>Problema</th></tr></thead><tbody>
<tr><td>Igualdade de fato</td><td>Todos têm as mesmas capacidades</td><td>É falsa, e deixa a igualdade refém de medições</td></tr>
<tr><td>Igualdade de consideração</td><td>Os interesses de todos pesam igual</td><td>Precisa dizer o que é um interesse, e quem os tem</td></tr>
<tr><td>Igualdade de tratamento</td><td>Todos devem ser tratados do mesmo jeito</td><td>Dar o mesmo a quem precisa de coisas diferentes é injusto</td></tr>
<tr><td>Igualdade de oportunidades</td><td>Todos devem partir do mesmo lugar</td><td>Ninguém parte do mesmo lugar: família, saúde e sorte variam</td></tr>
</tbody></table>
<h2>Consideração igual não é tratamento igual</h2>
<p>Dar consideração igual a interesses iguais pode exigir tratamentos muito diferentes. Uma criança e um adulto não devem ter o mesmo direito de dirigir, porque seus interesses e capacidades nessa questão são diferentes. Mas o interesse dos dois em não sofrer é o mesmo, e deve pesar o mesmo. A igualdade proíbe dar menos peso a alguém por um traço irrelevante, não exige ignorar as diferenças relevantes.</p>
<h2>O que John Rawls acrescentou</h2>
<p>Rawls propôs que a base da igualdade é uma <strong>propriedade de alcance</strong>: assim como todos os pontos dentro de um círculo estão igualmente “dentro”, mesmo que uns estejam mais perto do centro, todos os que têm um mínimo de capacidade moral estão igualmente dentro do círculo da justiça. Não importa quanto além do mínimo cada um vai. A ideia é elegante, mas deixa uma pergunta: e quem não atinge o mínimo? Bebês e pessoas com deficiência cognitiva grave contam, e Rawls precisou de ajustes para incluí-los.</p>
<h2>Por que a igualdade foi uma conquista</h2>
<p>Durante quase toda a história, a desigualdade entre humanos foi considerada natural: senhores e escravizados, homens e mulheres, nobres e plebeus. Aristóteles achava que alguns nasciam para servir. A igualdade humana não foi descoberta como um fato; foi conquistada como um princípio, contra argumentos que pareciam científicos na época. Veja a <a href="expansao-do-circulo-moral.html">expansão do círculo moral</a>.</p>
<h2>As objeções</h2>
<ul>
<li><strong>“Mas as pessoas são diferentes.”</strong> Sim. A igualdade moral não nega as diferenças; nega que elas justifiquem contar os interesses de alguém como menores.</li>
<li><strong>“Igualdade mata o mérito.”</strong> Consideração igual é compatível com recompensar o esforço. O que ela proíbe é deixar alguém fora da conta por nascimento, cor, sexo ou deficiência.</li>
<li><strong>“Se a base é a consideração de interesses, por que parar nos humanos?”</strong> Esta é a objeção mais interessante, e é a de Singer: se a igualdade não se baseia em capacidades, a espécie também não serve de fronteira. Quem tem interesses tem direito a que eles contem. Veja o <a href="circulo-moral.html">círculo moral</a>.</li>
</ul>
<div class="nota"><strong>Para guardar:</strong> a igualdade humana não é a afirmação de que somos todos iguais. É a decisão de que ninguém conta menos por aquilo que não escolheu.</div>
''', fontes=[('Declaração Universal dos Direitos Humanos', 'https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos'), ('Equality (Stanford Encyclopedia)', SEP + 'equality/'), ('Libertação Animal', WP + 'Liberta%C3%A7%C3%A3o_Animal'), ('Uma Teoria da Justiça', WP + 'Uma_Teoria_da_Justi%C3%A7a')]),
]

NOVAS_INTERMEDIARIO = [
dict(slug='fazer-e-deixar-acontecer', grupo='Consequencialismo por dentro', titulo='Fazer e deixar acontecer: o viés de omissão', resumo='Causar um dano parece pior do que deixar que ele aconteça. Às vezes é. Mas o cérebro usa essa diferença para desculpar muito do que deixamos de fazer.', corpo='''
<p class="abre">Empurrar alguém na água é pior do que não salvar quem está se afogando? A maioria diz que sim. A diferença entre <strong>fazer</strong> e <strong>deixar acontecer</strong> está no centro de muitos debates éticos, e também no centro de um viés que nos faz tolerar danos enormes, desde que não os tenhamos causado com as próprias mãos.</p>
<h2>O caso de Rachels</h2>
<p>James Rachels, em 1975, propôs dois casos. Smith herdará uma fortuna se o primo de seis anos morrer; ele afoga a criança na banheira e faz parecer acidente. Jones tem o mesmo plano, mas, ao entrar no banheiro, vê o primo escorregar e bater a cabeça; ele só fica olhando, pronto para empurrá-lo de volta se for preciso, e a criança morre sozinha. Smith matou; Jones deixou morrer. Alguém acha Jones melhor do que Smith? Rachels concluiu que a diferença entre matar e deixar morrer, por si só, não tem peso moral: o que importa são a intenção, o motivo e o resultado.</p>
<h2>Onde a diferença parece real</h2>
<p>Deontologistas respondem que os casos de Rachels são iguais porque tudo o mais é igual. Em geral, não é. Quem faz o dano é a causa dele; quem deixa acontecer só não interferiu. Warren Quinn e Philippa Foot defenderam que temos direitos <em>negativos</em> (a não ser prejudicado) mais fortes do que direitos <em>positivos</em> (a ser ajudado), e que isso explica a diferença: matar viola um direito negativo; deixar morrer, no máximo, deixa de cumprir um dever positivo. Sem essa distinção, argumentam, estaríamos obrigados a salvar todos o tempo todo, e a vida seria impossível.</p>
<table><thead><tr><th>Posição</th><th>Fazer e deixar acontecer</th><th>Consequência</th></tr></thead><tbody>
<tr><td>Consequencialismo</td><td>Não há diferença em si; o que conta é o resultado e o que estava ao alcance</td><td>Deixar de ajudar quando se pode é tão sério quanto prejudicar</td></tr>
<tr><td>Deontologia</td><td>Há diferença: causar dano viola um direito; não ajudar não viola</td><td>Deveres de ajuda são reais, mas mais fracos e com latitude</td></tr>
<tr><td>Ética das virtudes</td><td>Depende do que a omissão revela: indiferença, covardia ou prudência</td><td>A pessoa boa não se esconde atrás de “eu não fiz nada”</td></tr>
</tbody></table>
<h2>O viés de omissão</h2>
<p>Independentemente de a distinção ser válida, a psicologia mostra que a usamos além da conta. Ilana Ritov e Jonathan Baron, em 1990, perguntaram a pais se vacinariam os filhos contra uma doença que mata 10 em 10 mil crianças, sabendo que a vacina mata 5 em 10 mil. Muitos recusaram: preferiam o risco maior, desde que viesse da doença, e não de uma ação deles. É o <strong>viés de omissão</strong>: julgar ações danosas como piores do que omissões igualmente danosas, mesmo quando o resultado é pior.</p>
<p>O viés tem explicações. A ação é mais visível, mais atribuível e mais fácil de culpar. Omissões se diluem entre todos os que poderiam ter agido. E a evolução nos preparou para evitar a culpa, não para minimizar o dano.</p>
<h2>Onde ele custa caro</h2>
<ul>
<li><strong>Doar:</strong> não doar para salvar uma vida parece neutro; tirar a vida parece crime. O resultado para quem morre é o mesmo. Veja <a href="dilemas/crianca-no-lago.html">a criança no lago</a>.</li>
<li><strong>Políticas públicas:</strong> reguladores atrasam remédios por medo dos efeitos colaterais de aprovar, enquanto as mortes por não aprovar não aparecem em lugar nenhum.</li>
<li><strong>Animais selvagens:</strong> “a natureza é assim” trata o sofrimento que não causamos como se não contasse. Veja <a href="sofrimento-dos-animais-selvagens.html">animais selvagens</a>.</li>
<li><strong>Clima e futuro:</strong> os danos de não agir não têm autor, e por isso parecem menos graves do que são.</li>
<li><strong>Medicina:</strong> deixar morrer é aceito; ajudar a morrer é proibido, mesmo quando o paciente pede e o resultado é o mesmo. É a origem do debate sobre eutanásia passiva e ativa.</li>
</ul>
<h2>Como usar a distinção com honestidade</h2>
<ol class="roteiro">
<li>Pergunte o que estava ao seu alcance. Omissão só é neutra quando não havia nada a fazer.</li>
<li>Compare os resultados. Se a omissão produz mais dano, “não fiz nada” não é defesa.</li>
<li>Reserve a diferença para onde ela faz sentido: proteger direitos contra interferência, e não desculpar indiferença.</li>
<li>Desconfie quando a distinção sempre favorece a sua comodidade.</li>
</ol>
<div class="nota"><strong>Para guardar:</strong> pode haver uma diferença moral entre fazer e deixar acontecer. O que não há é uma licença para que tudo o que não causamos deixe de contar.</div>
''', fontes=[('Doing vs. Allowing Harm (Stanford Encyclopedia)', SEP + 'doing-allowing/'), ('James Rachels (Wikipédia)', WE + 'James_Rachels'), ('Omission bias (Wikipédia)', WE + 'Omission_bias'), ('Reluctance to vaccinate: omission bias and ambiguity (1990)', 'https://doi.org/10.1002/bdm.3960030404')]),

dict(slug='fraqueza-de-vontade', grupo='Mente e moral', titulo='Fraqueza de vontade: saber o que é certo e não fazer', resumo='Especialistas em ética animal que comem animais provam que argumentos não mudam ninguém? Não. Entre a crença e o ato há mais coisas do que parece.', corpo='''
<p class="abre">Quase todo mundo já concluiu que algo é errado e continuou fazendo. Os gregos chamaram isso de <em>acrasia</em>, agir contra o próprio melhor juízo. O caso é tão comum que virou argumento: se nem quem estuda ética muda de comportamento, para que servem os argumentos? Esta lição mostra por que essa conclusão é apressada.</p>
<h2>O problema antigo</h2>
<p>Sócrates achava que ninguém faz o mal sabendo que é mal: quem erra, erra por ignorância. Aristóteles discordou, e descreveu o acrático: a pessoa sabe o que é certo, em algum sentido, mas no momento da ação o desejo vence, e o conhecimento fica “como o de quem dorme ou está bêbado”. Para ele, a fraqueza de vontade é diferente do vício: o vicioso acha que está certo; o acrático sabe que está errado e se arrepende.</p>
<p>A filosofia moderna transformou isso em uma pergunta sobre <strong>motivação moral</strong>: acreditar que algo é errado já motiva, por si, a não fazê-lo? Os <em>internalistas</em> dizem que sim, ao menos um pouco: quem diz que algo é errado e não sente nenhuma inclinação a evitá-lo não entendeu o que disse. Os <em>externalistas</em> dizem que a crença e a motivação são coisas separadas, e que é preciso um desejo a mais. A fraqueza de vontade é o campo de teste das duas posições.</p>
<h2>O caso dos especialistas que comem animais</h2>
<p>Eric Schwitzgebel e Joshua Rust compararam professores de ética com outros professores. Os de ética eram mais propensos a dizer que comer carne de mamíferos é moralmente ruim, mas não comiam menos carne do que os colegas. O dado é usado assim: “se nem os especialistas mudam, a crença moral não move ninguém; o que move são imagens, histórias, choques, não argumentos”.</p>
<p>Luciano Carlos Cunha, em um texto de 2024, mostra que o caso admite ao menos cinco leituras, e só uma delas apoia a conclusão:</p>
<table><thead><tr><th>O que pode estar acontecendo</th><th>O que isso mostra sobre crença e ação</th></tr></thead><tbody>
<tr><td>A pessoa não acha mesmo que comer animais é errado</td><td>Ela faz o que acredita. A crença está movendo o comportamento, só que na outra direção</td></tr>
<tr><td>Acha errado, mas pouco errado, como chegar atrasado</td><td>O grau da crença explica o grau do esforço. Também confirma que a crença move</td></tr>
<tr><td>Diz que acha muito errado, mas não é sincera</td><td>O relato é que não corresponde à crença; a crença real segue movendo</td></tr>
<tr><td>Acha muito errado e tem vontade fraca: a motivação compete com hábito, prazer, pressão social e afeto</td><td>A crença motiva, mas não sozinha. Perde para motivações contrárias</td></tr>
<tr><td>Acha muito errado, não há motivações contrárias, e mesmo assim decide não agir</td><td>O caso raro. Mostra que a crença não <em>determina</em> o ato; não mostra que não motiva</td></tr>
</tbody></table>
<p>Em nenhuma das cinco leituras a crença deixa de influenciar. O que o caso dos especialistas mostra é que crenças morais não são o único fator, e que podem perder. Isso ninguém discutia.</p>
<h2>O que compete com a crença</h2>
<ul>
<li><strong>Hábito:</strong> o que fazemos há décadas exige pouco esforço; mudar exige muito, todos os dias.</li>
<li><strong>Prazer e afeto:</strong> comida se liga a família, festa e memória, e não só a nutrição.</li>
<li><strong>Pressão social:</strong> ser o diferente à mesa tem custo, e o cérebro o sente como ameaça.</li>
<li><strong>Dissonância:</strong> quando o ato não muda, a crença tende a se ajustar a ele, e a pessoa passa a “achar menos errado”. Veja <a href="vieses-morais.html">vieses morais</a>.</li>
<li><strong>Distância:</strong> a vítima está longe e não tem rosto; o prato está aqui. Veja <a href="fazer-e-deixar-acontecer.html">fazer e deixar acontecer</a>.</li>
<li><strong>Desconto do futuro:</strong> o custo da mudança é agora; o benefício, para outro, e depois.</li>
</ul>
<h2>Argumentos ainda são o melhor que temos</h2>
<p>A conclusão de que “só o choque funciona” leva a abandonar a persuasão racional por imagens e apelos emocionais. Mas, como nota Cunha, a persuasão não racional tem os mesmos limites: a pessoa pode ignorar a imagem, dizer que se comoveu e não agir, ou agir por uma semana. E tem um limite a mais: não explica por que a prática está errada, e por isso não dá à pessoa razões para sustentar a mudança quando o choque passar. A persuasão racional, com toda a sua fraqueza, é a única que deixa algo que a pessoa pode usar depois. Veja <a href="como-discutir-etica.html">como discutir ética</a>.</p>
<p>Há também um limite que nenhuma técnica supera: ninguém decide pelo outro. O melhor argumento do mundo, aceito, ainda deixa a decisão com quem ouviu. Isso não é um defeito dos argumentos; é o que significa ser um agente.</p>
<h2>O que ajuda a vontade</h2>
<p>Se a crença compete com outros fatores, agir bem é em parte um problema de engenharia pessoal, e a psicologia tem algo a dizer:</p>
<ol class="roteiro">
<li><strong>Intenções concretas:</strong> “vou fazer X quando acontecer Y” funciona melhor do que “vou tentar”.</li>
<li><strong>Mudar o ambiente:</strong> é mais fácil não comprar do que não comer o que está na geladeira.</li>
<li><strong>Começar por onde o custo é menor e o efeito é maior:</strong> trocas parciais sustentadas valem mais do que uma mudança total abandonada em um mês. Veja <a href="etica-animal-na-pratica.html">ética animal na prática</a>.</li>
<li><strong>Compromisso público e companhia:</strong> a pressão social que atrapalha também pode ajudar, se for na direção certa.</li>
<li><strong>Tratar a recaída como dado, não como veredito:</strong> o acrático de Aristóteles se arrepende, e é isso que o distingue do vicioso. O arrependimento é o sinal de que a crença continua lá.</li>
</ol>
<h2>Fraqueza de vontade não é hipocrisia</h2>
<p>O hipócrita finge uma crença que não tem para parecer melhor. O acrático tem a crença e falha em segui-la. Confundir os dois é uma arma comum nos debates: “você diz que é errado e faz, logo não acredita”. Não segue. A inconsistência entre crença e ato é desconfortável, e é justamente esse desconforto que, com o tempo, costuma mover o ato na direção da crença, ou a crença na direção do ato. A escolha de qual dos dois vai ceder é o que está em jogo.</p>
<div class="nota"><strong>Para guardar:</strong> saber o que é certo e não fazer não prova que saber é inútil. Prova que saber é o começo, e que o resto é vontade, hábito e ambiente, coisas que também se trabalham.</div>
''', fontes=[('Crenças morais, motivação para agir e o caso de especialistas em ética animal que consomem animais', 'https://senciencia.org/2024/07/08/crencas-morais-motivacao-para-agir-e-o-caso-de-especialistas-em-etica-animal-que-consomem-animais/'), ('The Moral Behavior of Ethics Professors (2014)', 'https://doi.org/10.1080/09515089.2012.727135'), ('Weakness of Will (Stanford Encyclopedia)', SEP + 'weakness-will/'), ('Moral Motivation (Stanford Encyclopedia)', SEP + 'moral-motivation/'), ('Ética a Nicômaco, livro VII', WP + '%C3%89tica_a_Nic%C3%B4maco')]),

dict(slug='pobreza-e-etica-global', grupo='Ética aplicada', titulo='Pobreza extrema e ética global', resumo='Centenas de milhões vivem com menos do que o mínimo. O que isso exige de quem tem mais, e o que de fato funciona para ajudar?', corpo='''
<p class="abre">Cerca de 700 milhões de pessoas vivem em pobreza extrema, abaixo da linha de cerca de dois dólares por dia, segundo o Banco Mundial. Milhões de crianças morrem por ano de causas evitáveis com remédios baratos. A ética global pergunta o que isso exige de quem vive com muito mais, e por que a resposta costuma ser tão menor do que a pergunta.</p>
<h2>O argumento de Singer</h2>
<p>Peter Singer formulou em 1972 o argumento que organiza o debate: se podemos evitar algo muito ruim sem sacrificar nada de importância moral comparável, devemos fazê-lo. A pobreza extrema é muito ruim. Doar parte da renda a organizações eficazes a evita, ao custo de bens que não são comparáveis a uma vida. Logo, devemos doar. A <a href="dilemas/crianca-no-lago.html">criança no lago</a> mostra que já aceitamos a premissa quando a vítima está perto.</p>
<h2>O argumento de Pogge</h2>
<p>Thomas Pogge chegou a uma conclusão parecida por um caminho deontológico. Para ele, a pobreza global não é só um mal que deixamos de aliviar: é um dano que ajudamos a <em>causar</em>, por meio de regras de comércio, dívida e recursos que favorecem países ricos e sustentam regimes corruptos. Se é assim, não se trata de caridade, e sim de reparação, um dever negativo de não prejudicar, mais forte do que qualquer dever positivo de ajudar. Veja <a href="fazer-e-deixar-acontecer.html">fazer e deixar acontecer</a>.</p>
<h2>O que dizem as teorias</h2>
<table><thead><tr><th>Teoria</th><th>O que exige</th><th>Limite reconhecido</th></tr></thead><tbody>
<tr><td>Utilitarismo</td><td>Doar até que o custo para você se iguale ao benefício para o outro</td><td>Exige demais; versões práticas propõem uma porcentagem</td></tr>
<tr><td>Prioritarismo</td><td>Prioridade máxima a quem está pior, e os mais pobres do mundo estão pior</td><td>Quanto peso a mais, exatamente</td></tr>
<tr><td>Kant</td><td>Dever imperfeito de beneficência: ajudar é devido, com latitude sobre quanto e a quem</td><td>A latitude pode virar desculpa</td></tr>
<tr><td>Direitos (Pogge)</td><td>Parar de prejudicar e reparar o dano causado</td><td>Depende de mostrar a causa</td></tr>
<tr><td>Ética do cuidado</td><td>Atenção à vulnerabilidade, que não termina na fronteira</td><td>O cuidado distante é mais difícil de sustentar</td></tr>
<tr><td>Libertarismo</td><td>Nenhum dever forçado; ajudar é louvável, não obrigatório</td><td>Não explica por que o lago e a distância seriam diferentes</td></tr>
</tbody></table>
<h2>As objeções</h2>
<ul>
<li><strong>“A ajuda não funciona.”</strong> Parte dela não funcionou: ajuda entre governos foi desperdiçada ou desviada. Mas intervenções específicas, como redes contra a malária, vermífugos e transferências diretas de dinheiro, têm efeito medido em estudos controlados. Avaliadores como o GiveWell estimam que algumas salvam uma vida por alguns milhares de dólares.</li>
<li><strong>“Cria dependência.”</strong> Transferências diretas de dinheiro, estudadas em vários países, aumentaram consumo, investimento e trabalho, não a dependência. O argumento vale contra formas ruins de ajuda, não contra a ajuda.</li>
<li><strong>“Primeiro os pobres daqui.”</strong> Há pobreza no Brasil, e ela conta. Mas o mesmo valor alivia muito mais sofrimento onde a pobreza é extrema, e o lugar de nascimento não é uma razão moral para que uma vida valha menos. Veja <a href="tribalismo-moral.html">tribalismo moral</a>.</li>
<li><strong>“Exige demais.”</strong> A objeção mais séria, discutida em <a href="quanto-a-moral-pode-exigir.html">quanto a moral pode exigir</a>. A resposta prática é uma meta realista e crescente, não a culpa.</li>
<li><strong>“É dever do Estado, não meu.”</strong> Também é dever do Estado. Mas quem morre enquanto o Estado não age não é ajudado por essa divisão de tarefas.</li>
</ul>
<h2>Pobreza e outros círculos</h2>
<p>A ética da pobreza tem a mesma estrutura dos outros temas do curso: alguém sofre, nós podemos reduzir o sofrimento, e uma diferença (a distância, a fronteira) é tratada como relevante sem ser. As mesmas organizações que avaliam a ajuda humana começaram a avaliar a defesa animal pelo mesmo critério: quanto sofrimento cada real evita. Veja <a href="etica-animal-na-pratica.html">ética animal na prática</a>.</p>
<h2>O que uma pessoa pode fazer</h2>
<ol class="roteiro">
<li><strong>Doar com evidência:</strong> escolher organizações avaliadas por resultado, não por emoção.</li>
<li><strong>Doar uma porcentagem:</strong> o compromisso de 10% do altruísmo eficaz, ou menos, mas regular.</li>
<li><strong>Apoiar regras melhores:</strong> comércio, patentes de remédios, paraísos fiscais e dívida afetam mais pessoas do que qualquer doação.</li>
<li><strong>Não se paralisar:</strong> a diferença entre o ideal e o nada é imensa, e cada passo salva alguém.</li>
</ol>
<div class="nota"><strong>Para guardar:</strong> a pergunta não é se você pode salvar o mundo. É se há alguém que você poderia salvar e não salva, e que razão você tem para isso.</div>
''', fontes=[('Famine, Affluence, and Morality (Wikipédia)', WE + 'Famine,_Affluence,_and_Morality'), ('World Poverty and Human Rights', 'https://www.google.com/search?tbm=bks&q=Pogge+World+Poverty+and+Human+Rights'), ('Banco Mundial: pobreza', 'https://www.worldbank.org/en/topic/poverty/overview'), ('GiveWell', 'https://www.givewell.org/'), ('The Life You Can Save', 'https://www.thelifeyoucansave.org/')]),
]

NOVAS_AVANCADO = [
dict(slug='sofrimento-dos-animais-selvagens', grupo='Ética animal', titulo='O sofrimento dos animais selvagens', resumo='A natureza não é um documentário. A maioria dos animais que nasce morre cedo, de fome, doença ou predação. Se o sofrimento conta, conta aqui também.', corpo='''
<p class="abre">Pense em um peixe que põe milhões de ovos. Em uma população estável, em média só dois descendentes chegam à idade adulta. Os outros morrem jovens, de fome, frio, doença, parasitas ou nas mandíbulas de outro animal. Esse é o padrão da maior parte da vida na Terra, e ele coloca uma pergunta que a ética animal evitou por muito tempo.</p>
<h2>A escala</h2>
<p>O número de animais selvagens supera em muito o de animais criados por humanos: estimativas falam em trilhões de vertebrados e um número incomparavelmente maior de invertebrados. A maioria das espécies segue a estratégia de ter muitos filhotes e investir pouco em cada um. O resultado é que, para a maior parte dos animais que nascem, a vida é curta e termina mal. Para os que sobrevivem, fome sazonal, ferimentos sem tratamento, parasitas e doenças são comuns.</p>
<table><thead><tr><th>Causa</th><th>O que acontece</th></tr></thead><tbody>
<tr><td>Mortalidade juvenil</td><td>A maioria dos filhotes morre antes de se reproduzir, em geral de fome ou predação</td></tr>
<tr><td>Doença e parasitas</td><td>Sem tratamento; infecções e parasitas são a norma, não a exceção</td></tr>
<tr><td>Fome e sede</td><td>Secas e invernos matam populações inteiras lentamente</td></tr>
<tr><td>Predação</td><td>Muitas vezes sem morte rápida; animais são comidos vivos</td></tr>
<tr><td>Clima e acidentes</td><td>Incêndios, inundações, frio extremo</td></tr>
</tbody></table>
<h2>Por que o tema foi ignorado</h2>
<ul>
<li><strong>A visão idílica:</strong> documentários mostram o leão caçando, não a gazela morrendo por horas, nem os filhotes de leão que morrem de fome.</li>
<li><strong>“Não fomos nós”:</strong> o <a href="fazer-e-deixar-acontecer.html">viés de omissão</a> faz o sofrimento que não causamos parecer menos nosso problema.</li>
<li><strong>O ecocentrismo:</strong> se o que importa é o ecossistema, o sofrimento dos indivíduos dentro dele é “parte do equilíbrio”. Veja <a href="vida-e-ecossistemas.html">vida e ecossistemas</a>.</li>
<li><strong>O medo de parecer absurdo:</strong> “ajudar animais selvagens” soa como querer impedir leões de caçar. Não é disso que se trata.</li>
</ul>
<h2>O argumento</h2>
<ol class="roteiro">
<li>Se o sofrimento conta, conta pelo que é sentido, não por quem o causou. Uma dor de origem natural não dói menos.</li>
<li>Já aceitamos isso para humanos: ninguém diz que um terremoto “é natural” e por isso não se deve socorrer as vítimas.</li>
<li>Já intervimos na natureza o tempo todo: vacinamos animais selvagens contra a raiva, resgatamos animais de incêndios, alimentamos populações em invernos severos.</li>
<li>Logo, a pergunta não é se devemos intervir, e sim quando a intervenção reduz sofrimento sem causar mais, e como saber.</li>
</ol>
<p>Oscar Horta, Catia Faria e Brian Tomasik estão entre os autores que desenvolveram o tema. Para eles, a defesa dos animais não pode se limitar aos que estão nas nossas mãos: a imparcialidade pede olhar para onde o sofrimento é maior.</p>
<h2>As objeções</h2>
<ul>
<li><strong>“A natureza sabe o que faz.”</strong> A natureza não sabe nada: a seleção natural produz o que se reproduz, não o que vive bem. Apelar a ela é a <a href="fatos-e-valores.html">falácia naturalista</a>.</li>
<li><strong>“Intervir vai piorar.”</strong> Muitas vezes vai, e por isso a maior parte dos defensores pede pesquisa antes de ação em escala, e ações pequenas e reversíveis agora. A incerteza é razão para estudar, não para declarar o problema inexistente.</li>
<li><strong>“Não dá para resolver.”</strong> Também não dá para resolver a pobreza inteira, e nem por isso deixamos de ajudar quem podemos. Vacinação, resgate em desastres e controle de doenças já são possíveis.</li>
<li><strong>“Os animais selvagens vivem bem.”</strong> Alguns sim, sobretudo mamíferos e aves de vida longa. A maioria dos indivíduos que nascem, não. A objeção confunde os animais que vemos com os animais que existem.</li>
</ul>
<h2>O que isso muda</h2>
<p>Se o argumento está certo, o sofrimento dos animais selvagens é, pela escala, um dos maiores problemas morais existentes, e quase ninguém trabalha nele. Isso não exige abandonar o resto: a criação industrial continua sendo o maior sofrimento que <em>causamos</em>, e é por onde a maioria começa. Mas muda a forma de ver a natureza: de cenário intocável a lugar onde há quem sofre, e onde um dia talvez possamos ajudar.</p>
<div class="nota"><strong>Para guardar:</strong> “é a natureza” descreve de onde o sofrimento veio. Não diz que ele não conta.</div>
''', fontes=[('Animal Ethics: a situação dos animais na natureza', 'https://www.animal-ethics.org/a-situacao-dos-animais-na-natureza/'), ('Wild animal suffering (Wikipédia)', WE + 'Wild_animal_suffering'), ('Wild Animal Initiative', 'https://www.wildanimalinitiative.org/'), ('Animal Ethics in the Wild', 'https://www.google.com/search?tbm=bks&q=Catia+Faria+Animal+Ethics+in+the+Wild')]),

dict(slug='animais-e-a-politica', grupo='Ética animal', titulo='Animais e a política: cidadania e constituições', resumo='Se os animais contam, como entram nas instituições? Zoopolis, a democracia senciente de Cochrane e o constitucionalismo baseado na senciência.', corpo='''
<p class="abre">A ética animal passou décadas perguntando o que <em>não</em> se pode fazer com os animais. Uma geração de autores passou a perguntar outra coisa: que lugar eles têm na comunidade política? Quem os representa? O que uma constituição lhes deve?</p>
<h2>Quem sofre e não vota</h2>
<p>Democracias representam quem vota. Animais, crianças pequenas e gerações futuras não votam, e seus interesses entram na política só quando alguém com voto os defende. Bilhões de animais vivem e morrem em sistemas sustentados por leis, subsídios e fiscalização pública. Suas vidas são decididas politicamente, sem que ninguém fale por eles. É o problema que estes autores tentam resolver.</p>
<h2>Donaldson e Kymlicka: Zoopolis</h2>
<p>Em <em>Zoopolis</em> (2011), Sue Donaldson e Will Kymlicka propõem que a relação política com os animais depende da relação que cada grupo tem com a nossa sociedade:</p>
<table><thead><tr><th>Animais</th><th>Exemplos</th><th>Situação proposta</th></tr></thead><tbody>
<tr><td>Domesticados</td><td>Cães, gatos, vacas, galinhas</td><td><strong>Cidadania:</strong> nós os trouxemos para dentro da sociedade; seus interesses devem contar nas decisões, com representação</td></tr>
<tr><td>Que vivem entre nós</td><td>Pombos, ratos urbanos</td><td><strong>Residência:</strong> não são cidadãos plenos, mas têm direito de existir e de não ser tratados como praga</td></tr>
<tr><td>Selvagens</td><td>Animais em seus habitats</td><td><strong>Soberania:</strong> comunidades com direito ao próprio território, sem invasão</td></tr>
</tbody></table>
<p>A proposta inclui direitos positivos (cuidado, saúde, espaço), e não só proteção contra danos. As críticas: animais podem ser cidadãos em algum sentido real? E a soberania dos selvagens não os deixa sem ajuda diante do <a href="sofrimento-dos-animais-selvagens.html">sofrimento na natureza</a>?</p>
<h2>Cochrane: uma democracia senciente</h2>
<p>Alasdair Cochrane, em <em>Sentientist Politics</em> (2018), propõe uma “democracia cosmopolita senciocêntrica”: instituições, do local ao global, que levem em conta os interesses de todos os seres sencientes, com representantes dedicados a quem não pode votar. Diferente de <em>Zoopolis</em>, baseia os direitos nos interesses de cada indivíduo, não em grupos, e distingue: a maioria dos animais tem interesse forte em não sofrer, mas não necessariamente em liberdade no sentido humano.</p>
<h2>Adenitire e Fasel: a Constituição para os animais</h2>
<p>Em <em>Animals and the Constitution</em> (2025), John Adenitire e Raffael Fasel criticam a teoria constitucional por olhar só para humanos. Propõem um constitucionalismo baseado na senciência, que respeite os interesses de todos os seres sencientes governados, e repensam quatro princípios: direitos fundamentais, proporcionalidade, Estado de direito e democracia. Citam casos reais: a votação sobre direitos de primatas na Basileia, em 2022, e propostas de carta de direitos para animais na Finlândia.</p>
<h2>O que já existe</h2>
<ul>
<li>Reconhecimento legal da senciência animal na União Europeia, no Reino Unido, na Nova Zelândia e em outros países.</li>
<li>Proibições de gaiolas, de testes cosméticos em animais e de certas práticas de criação, em vários países.</li>
<li>No Brasil, a Constituição proíbe práticas que submetam animais a crueldade (artigo 225), e o Supremo Tribunal Federal já a aplicou contra a farra do boi e a vaquejada, com idas e vindas.</li>
<li>Partidos pelos animais, com representação parlamentar, na Holanda e em Portugal.</li>
</ul>
<h2>As objeções</h2>
<ul>
<li><strong>“Política é entre humanos.”</strong> Política é sobre quem é afetado pelas decisões coletivas. Animais são.</li>
<li><strong>“Quem fala por eles pode distorcer.”</strong> O mesmo vale para crianças e pessoas incapazes, e resolvemos com tutela e fiscalização, não com exclusão.</li>
<li><strong>“É utópico.”</strong> O voto feminino também foi. E parte já existe.</li>
</ul>
<div class="nota"><strong>Eles discordam entre si</strong> sobre o que os direitos devem ser, sobre liberdade e sobre o mundo selvagem. Partem de uma mesma ideia: uma política justa não termina na fronteira da espécie. É também o ponto de partida do <a href="https://politicaparainiciantes.biblioverse.org/senciocentrismo.html" target="_blank" rel="noopener">Política Para Iniciantes</a>.</div>
''', fontes=[ZOOPOLIS, ('Sentientist Politics: A Theory of Global Inter-Species Justice', 'https://global.oup.com/academic/product/sentientist-politics-9780198789802'), ('Animals and the Constitution: Towards Sentience-Based Constitutionalism', 'https://academic.oup.com/book/59826'), ('Constituição Federal, art. 225', 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm')]),

dict(slug='catastrofes-morais', grupo='Progresso e abertura', titulo='Catástrofes morais: e se estivermos errados agora?', resumo='Guerras e genocídios são catástrofes que reconhecemos. Mas toda sociedade do passado cometeu um mal grave achando que era normal. Qual é o nosso, e o que fazer com a dúvida?', corpo='''
<p class="abre">A Atenas de Sócrates tinha escravizados. A Europa iluminista traficava pessoas. Os Estados Unidos que escreveram “todos os homens são criados iguais” mantiveram a escravidão por mais oitenta anos. Em cada caso, pessoas inteligentes, instruídas e de boa-fé viviam dentro de um mal grave e o achavam normal. O filósofo Evan Williams chamou isso de <strong>catástrofe moral em curso</strong>, e perguntou qual é a chance de estarmos em uma.</p>
<h2>Dois tipos de catástrofe</h2>
<p>Guerras, genocídios, fomes provocadas, limpezas étnicas: são catástrofes morais, e todos as reconhecem como tal. Esta lição não é sobre elas, por uma razão simples: o problema das catástrofes reconhecidas não é descobri-las, e sim impedi-las, e isso é assunto de outras lições, da <a href="riscos-s-e-riscos-x.html">prevenção de riscos</a> à <a href="da-etica-a-politica.html">política</a>. O problema desta lição é outro: o mal que uma sociedade pratica <em>sem o reconhecer como mal</em>, e que por isso ninguém tenta impedir.</p>
<table><thead><tr><th></th><th>Catástrofes reconhecidas</th><th>Catástrofes não reconhecidas</th></tr></thead><tbody>
<tr><td>Exemplos</td><td>Guerras de agressão, genocídios, tortura em massa, fomes provocadas</td><td>A escravidão para quem a praticava; os candidatos de hoje, discutidos abaixo</td></tr>
<tr><td>Como aparecem</td><td>Como tragédia, crime ou emergência</td><td>Como normalidade, costume, economia</td></tr>
<tr><td>Quem as condena</td><td>Quase todos, ao menos em abstrato</td><td>Uma minoria, vista como exagerada ou fanática</td></tr>
<tr><td>O problema</td><td>Impedir, punir, reparar</td><td>Antes de tudo, enxergar</td></tr>
</tbody></table>
<p>A fronteira entre os dois tipos é menos nítida do que parece. A guerra é condenada em abstrato, mas cada guerra concreta é defendida por um dos lados como necessária, justa ou inevitável, e por isso continua acontecendo. Dentro de catástrofes reconhecidas há partes não reconhecidas: os civis do outro lado, os prisioneiros, os animais, o custo deixado às gerações seguintes. E muito do que hoje chamamos de catástrofe reconhecida começou como não reconhecida: o tráfico de pessoas foi comércio respeitável antes de ser crime. O argumento de Williams é sobre essa passagem, e sobre o que ainda não a fez.</p>
<h2>O argumento</h2>
<p>Williams, em um artigo de 2015, dá duas razões para achar provável que a nossa sociedade esteja cometendo um erro moral grave sem perceber:</p>
<ol class="roteiro">
<li><strong>Indução:</strong> até onde a história alcança, toda sociedade cometeu ao menos uma injustiça enorme que seus membros não viam como injustiça. Supor que a nossa é a primeira a não cometer nenhuma exige uma razão especial, e não temos nenhuma.</li>
<li><strong>Disjunção:</strong> há muitas formas independentes de estar errado. Podemos estar errados sobre quem conta (animais, gerações futuras, mentes artificiais), sobre o que devemos a quem está longe, sobre punição, sobre o que fazemos com quem está no fim da vida, sobre riscos que impomos ao futuro. Mesmo que cada erro seja improvável, a chance de ao menos um deles ser real é alta.</li>
</ol>
<p>A conclusão não é que sabemos qual é o erro. É que devemos agir como quem provavelmente está cometendo um, sem saber qual.</p>
<h2>Por que não o vemos</h2>
<p>O mal do passado não parecia mal a quem o praticava. Os mecanismos são os mesmos de sempre:</p>
<table><thead><tr><th>Mecanismo</th><th>Então</th><th>Hoje, possivelmente</th></tr></thead><tbody>
<tr><td>Interesse</td><td>A escravidão sustentava a economia</td><td>Práticas baratas e confortáveis, que ninguém quer encarecer</td></tr>
<tr><td>Normalidade</td><td>“Sempre foi assim”</td><td>O que está no prato, no mercado, na lei</td></tr>
<tr><td>Invisibilidade</td><td>As vítimas estavam longe ou caladas</td><td>Quem sofre não vota, não fala, ou ainda não nasceu</td></tr>
<tr><td>Justificativas prontas</td><td>“Eles não sentem como nós”</td><td>As mesmas frases, aplicadas a outros grupos</td></tr>
<tr><td>Dissonância</td><td>Quem participava precisava acreditar que estava certo</td><td>Idem. Veja <a href="vieses-morais.html">vieses morais</a></td></tr>
</tbody></table>
<p>Um teste útil: as justificativas que usamos hoje para alguma prática são parecidas com as que o passado usou para as suas? Se são, o alarme deveria soar.</p>
<h2>Os candidatos mais citados</h2>
<p>Ninguém sabe qual é a catástrofe, mas alguns candidatos aparecem com frequência, porque reúnem escala, invisibilidade das vítimas e justificativas conhecidas:</p>
<ul>
<li><strong>A criação industrial de animais:</strong> dezenas de bilhões de seres sencientes por ano em condições que, descritas sem a palavra “comida”, chamaríamos de tortura. Veja <a href="etica-animal-na-pratica.html">ética animal na prática</a>.</li>
<li><strong>A pobreza extrema evitável:</strong> milhões de mortes por ano por causas que custam pouco a prevenir, enquanto recursos abundam. Veja <a href="pobreza-e-etica-global.html">pobreza e ética global</a>.</li>
<li><strong>O sofrimento dos animais selvagens:</strong> em escala maior que tudo o mais, e quase ignorado. Veja <a href="sofrimento-dos-animais-selvagens.html">animais selvagens</a>.</li>
<li><strong>As gerações futuras:</strong> riscos irreversíveis impostos a quem não tem voz. Veja <a href="riscos-s-e-riscos-x.html">riscos X e S</a>.</li>
<li><strong>O encarceramento em massa e as condições das prisões:</strong> sofrimento intenso, imposto pelo Estado, a pessoas sem poder.</li>
<li><strong>Mentes artificiais:</strong> se vierem a sentir, podemos estar criando sofrimento sem perceber. Veja <a href="mentes-artificiais.html">mentes artificiais</a>.</li>
</ul>
<p>A lista não é um veredito. É o conjunto de lugares onde a estrutura de uma catástrofe do passado se repete, e por isso merece exame antes dos outros.</p>
<h2>A objeção: “isso é só a sua pauta”</h2>
<p>Um crítico pode dizer que a lista revela as opiniões de quem a escreve, e que outros fariam listas diferentes: o aborto, a eutanásia, a destruição da família, a perda da fé. É verdade que o argumento de Williams não diz <em>qual</em> é o erro, e cada pessoa tende a ver a catástrofe nos outros. Isso não desarma o argumento; mostra como aplicá-lo com honestidade: pergunte onde <em>você</em> tem interesse, conforto e justificativas prontas, e não só onde o outro lado tem. A catástrofe que você não vê, por definição, não está na sua pauta.</p>
<h2>O que fazer com a dúvida</h2>
<p>Se é provável que estejamos errados em algo grave, sem saber em quê, Williams e outros propõem uma resposta em três partes:</p>
<ol class="roteiro">
<li><strong>Investigar:</strong> dedicar esforço real a descobrir onde estamos errados, em vez de defender o que já fazemos. A ética não é um luxo: é a pesquisa sobre o erro que pode estar nos custando mais caro.</li>
<li><strong>Preservar a capacidade de corrigir:</strong> instituições abertas, liberdade de crítica, pluralismo e o hábito de <a href="abertura-moral.html">mudar de ideia</a>. Uma sociedade que não pode ser corrigida mantém suas catástrofes para sempre.</li>
<li><strong>Evitar o irreversível e cobrir-se:</strong> diante da dúvida, preferir ações que seriam aceitáveis em muitas visões morais e evitar as que seriam catastróficas em alguma. Veja <a href="incerteza-moral.html">incerteza moral</a>.</li>
</ol>
<h2>Tobias Baumann: a catástrofe que ainda não aconteceu</h2>
<p>Williams olha para o presente: o mal que praticamos sem ver. Tobias Baumann, cofundador do Center for Reducing Suffering, olha para o futuro. Em <em>Avoiding the Worst: How to Prevent a Moral Catastrophe</em> (2022), ele chama de catástrofe moral um futuro com sofrimento em escala muito maior do que toda a história até aqui, os <strong>riscos S</strong> discutidos em <a href="riscos-s-e-riscos-x.html">riscos X e riscos S</a>, e argumenta que evitar esses piores cenários deveria ser uma prioridade.</p>
<p>Três ideias do livro completam o argumento de Williams:</p>
<ul>
<li><strong>As catástrofes não precisam de vilões.</strong> Baumann distingue riscos <em>incidentais</em>, em que o sofrimento é subproduto de uma atividade que ninguém faz para causar dor, de riscos <em>agenciais</em>, em que alguém o causa de propósito, por conflito, vingança ou sadismo. A criação industrial de animais é o modelo do primeiro tipo: ninguém a criou para fazer sofrer, e ela é provavelmente a maior fonte de sofrimento causado por humanos. Tecnologias novas, como mentes artificiais criadas em massa, podem repetir o padrão em escala muito maior, sem que ninguém decida isso.</li>
<li><strong>Os fatores de risco são conhecidos.</strong> Tecnologia poderosa sem controle, falta de consideração moral por quem sente, e conflito ou concentração de poder. Juntos, eles produziram as catástrofes do passado e podem produzir as do futuro. Isso dá um mapa: reduzir a chance de uma catástrofe é agir sobre esses fatores antes que ela comece.</li>
<li><strong>O que fazer é, em boa parte, o mesmo que esta lição propõe.</strong> Baumann defende a <em>defesa moral</em> (ampliar o círculo de quem conta, para que o sofrimento futuro não seja invisível como o de hoje), <em>política melhor</em> (instituições cooperativas e capazes de corrigir erros, menos conflito) e cautela com <em>tecnologias emergentes</em>, sobretudo a inteligência artificial. Ele também dedica um capítulo aos vieses que nos fazem subestimar o pior: insensibilidade à escala, desconto do futuro, otimismo. Veja <a href="vieses-morais.html">vieses morais</a>.</li>
</ul>
<p>A ligação entre os dois autores é direta. As catástrofes que Williams descreve, as que não vemos, são as que, segundo Baumann, podem crescer até escalas inéditas se nada mudar. Enxergar a de hoje é a melhor proteção contra a de amanhã.</p>
<h2>Como o passado foi corrigido</h2>
<p>As catástrofes anteriores não acabaram porque a época “amadureceu”. Acabaram porque alguém disse que o normal estava errado, em geral com custo pessoal, e porque havia instituições e argumentos capazes de ouvir. Abolicionistas, sufragistas e defensores de direitos civis foram chamados de fanáticos pela maioria razoável do seu tempo. Isso é um aviso em duas direções: quem denuncia uma catástrofe hoje pode ter razão, e também pode estar errado, e só o argumento separa os casos. Veja <a href="progresso-moral.html">progresso moral</a>.</p>
<h2>Uma atitude, não uma culpa</h2>
<p>O argumento não serve para paralisar ninguém com culpa, nem para se sentir superior ao passado. Serve para uma atitude: a de quem sabe que provavelmente está errado em algo importante, procura descobrir em quê, e muda quando encontra. É a diferença entre quem viveu uma catástrofe e a defendeu, e quem viveu a mesma e ajudou a acabar com ela. Os dois achavam que estavam certos. Só um estava disposto a verificar.</p>
<div class="nota"><strong>Para guardar:</strong> a pergunta não é “o que nossos avós fizeram de errado?”. É “o que estamos fazendo que nossos netos vão perguntar como foi possível?”, e o que você faz hoje com a resposta.</div>
''', fontes=[('The Possibility of an Ongoing Moral Catastrophe', 'https://link.springer.com/article/10.1007/s10677-015-9567-7'), ('Avoiding the Worst: How to Prevent a Moral Catastrophe', 'https://centerforreducingsuffering.org/research/avoiding-the-worst/'), ('Moral progress (Wikipédia)', WE + 'Moral_progress'), ('The Expanding Circle', 'https://www.google.com/search?tbm=bks&q=Peter+Singer+The+Expanding+Circle'), ('Moral Uncertainty', 'https://www.moraluncertainty.com/')]),

dict(slug='riscos-s-e-riscos-x', grupo='Decidir sem certeza', titulo='Riscos X e riscos S: o pior que pode acontecer', resumo='Extinção da humanidade e sofrimento em escala astronômica são os dois piores desfechos imagináveis. Como pensar neles sem fanatismo nem indiferença?', corpo='''
<p class="abre">Dois tipos de risco ocupam uma parte crescente da ética do futuro. O <strong>risco existencial</strong> (risco X) é o de a humanidade ser extinta ou perder para sempre seu potencial. O <strong>risco de sofrimento</strong> (risco S) é o de o futuro conter sofrimento em escala muito maior do que toda a história até aqui. Teorias diferentes dão pesos diferentes a cada um, e a diferença revela o que cada uma valoriza.</p>
<h2>Riscos existenciais</h2>
<p>Nick Bostrom definiu o termo em 2002. Toby Ord, em <em>O Precipício</em> (2020), estimou em cerca de um em seis a chance de uma catástrofe existencial neste século, com as maiores parcelas vindas de inteligência artificial fora de controle e de pandemias projetadas, seguidas de guerra nuclear e colapso climático. Os números são palpites informados, e Ord os apresenta assim.</p>
<p>Por que a extinção seria pior do que uma catástrofe que mata 99% das pessoas? Derek Parfit respondeu: porque a diferença entre 99% e 100% não é 1%, e sim todas as gerações que poderiam vir depois. Para quem dá valor a vidas futuras boas, evitar a extinção é a prioridade quase absoluta. Veja <a href="geracoes-futuras.html">gerações futuras</a>.</p>
<h2>Riscos de sofrimento</h2>
<p>Autores ligados ao Center on Long-Term Risk e ao Center for Reducing Suffering, como Brian Tomasik, David Althaus, Lukas Gloor, Magnus Vinding e Tobias Baumann, chamam a atenção para outro desfecho: não a ausência de futuro, mas um futuro cheio de sofrimento. Exemplos: criação de animais em escala ainda maior, espalhada por outros planetas; mentes artificiais sencientes criadas aos bilhões e exploradas; regimes totalitários estáveis com tecnologia de vigilância; conflitos entre potências com armas capazes de causar sofrimento extremo.</p>
<p>Baumann, em <em>Avoiding the Worst</em> (2022), a primeira introdução sistemática ao tema, separa os riscos S em <strong>incidentais</strong> (sofrimento como subproduto de atividades que ninguém faz para causar dor, como a criação industrial hoje), <strong>agenciais</strong> (causado de propósito, por conflito, vingança ou sadismo) e <strong>naturais</strong> (como o sofrimento dos animais selvagens, se se espalhar). Para ele, os riscos mais importantes são os realistas e evitáveis, e os fatores que os alimentam são tecnologia poderosa sem controle, falta de consideração moral por quem sente, e conflito. Veja <a href="catastrofes-morais.html">catástrofes morais</a>.</p>
<p>Para quem dá <a href="o-peso-do-sofrimento.html">prioridade ao sofrimento</a>, um risco S é pior do que a extinção: um universo vazio não sofre; um universo cheio de seres em agonia sofre mais do que qualquer coisa que já existiu. Essa é a divergência central entre as duas agendas.</p>
<table><thead><tr><th></th><th>Risco X</th><th>Risco S</th></tr></thead><tbody>
<tr><td>O pior desfecho</td><td>Nenhum futuro</td><td>Um futuro de sofrimento imenso</td></tr>
<tr><td>Quem mais se preocupa</td><td>Utilitaristas clássicos, longoprazistas</td><td>Éticas focadas no sofrimento</td></tr>
<tr><td>O que torna o futuro valioso</td><td>Vidas boas que podem existir</td><td>Ausência de vidas ruins</td></tr>
<tr><td>Ponto de convergência</td><td colspan="2">Evitar catástrofes irreversíveis; manter instituições capazes de corrigir erros; cautela com tecnologias que concentram poder</td></tr>
</tbody></table>
<h2>Onde as agendas se encontram</h2>
<p>Apesar da divergência, as duas concordam em muito. Uma guerra nuclear é um risco X e um risco S. Uma inteligência artificial com objetivos errados pode extinguir ou pode fazer sofrer. Instituições estáveis, cooperação internacional e cautela com tecnologias irreversíveis servem às duas. Por isso, muitos autores defendem focar no que é robusto: o que reduz os dois riscos ao mesmo tempo.</p>
<h2>As objeções</h2>
<ul>
<li><strong>Fanatismo:</strong> números astronômicos multiplicados por probabilidades minúsculas podem justificar qualquer sacrifício presente. A resposta usual é limitar a agregação, focar em riscos concretos e nunca aceitar causar sofrimento certo hoje por benefícios especulativos. Veja <a href="incerteza-moral.html">incerteza moral</a>.</li>
<li><strong>Negligenciar o presente:</strong> há sofrimento certo agora. Defensores respondem que as duas coisas não competem tanto quanto parece, e que parte dos riscos (pandemias, guerra) já afeta o presente.</li>
<li><strong>Quem decide o futuro:</strong> pensar a longo prazo pode virar desculpa para concentrar poder “pelo bem das gerações futuras”. É um risco real, e uma razão para preferir instituições plurais a planos grandiosos.</li>
<li><strong>Ficção científica:</strong> mentes artificiais e colonização espacial parecem distantes. Mas a criação industrial de animais já é um sofrimento em escala que ninguém previu há dois séculos, e as decisões que moldam tecnologias são tomadas antes que elas existam.</li>
</ul>
<h2>Para que serve pensar nisso</h2>
<p>Não para prever o futuro, e sim para notar que as escolhas de hoje, sobre inteligência artificial, sobre como tratamos quem sente, sobre que instituições construímos, podem se repetir em escala muito maior. A pergunta do círculo moral aparece de novo, no tempo: quem vai sofrer com o que decidimos, e eles têm voz?</p>
<div class="nota"><strong>Para guardar:</strong> o risco X pergunta se haverá futuro. O risco S pergunta como ele será para quem o viver. Uma ética completa precisa das duas perguntas.</div>
''', fontes=[('The Precipice', 'https://www.google.com/search?tbm=bks&q=Toby+Ord+The+Precipice'), ('Reducing Risks of Astronomical Suffering: A Neglected Priority', 'https://longtermrisk.org/reducing-risks-of-astronomical-suffering-a-neglected-priority/'), ('Avoiding the Worst: How to Prevent a Moral Catastrophe', 'https://centerforreducingsuffering.org/research/avoiding-the-worst/'), ('Existential risk (Wikipédia)', WE + 'Global_catastrophic_risk'), ('Center for Reducing Suffering', 'https://centerforreducingsuffering.org/'), VINDING]),
]

META_NOVAS = {
 'igualdade-humana': (['circulo', 'fundamentos'], ('Para Singer, a igualdade humana é…', ['Um fato sobre as capacidades das pessoas', 'Um princípio moral: interesses iguais pesam igual', 'Uma lei do Estado'], 1, 'Se fosse um fato sobre capacidades, bastaria medir para justificar exclusões. Como princípio, ninguém conta menos pelo que não escolheu.')),
 'fazer-e-deixar-acontecer': (['consequencias', 'mente'], ('No estudo de Ritov e Baron, pais recusavam uma vacina que matava 5 em 10 mil para evitar uma doença que matava 10 em 10 mil. Isso é…', ['Prudência', 'Viés de omissão', 'Deontologia de limiar'], 1, 'Preferiram o risco maior desde que viesse de uma omissão, e não de uma ação deles.')),
 'fraqueza-de-vontade': (['mente', 'pratica'], ('Para Aristóteles, o que distingue o acrático do vicioso?', ['O acrático não sabe o que é certo', 'O acrático sabe que errou e se arrepende; o vicioso acha que está certo', 'Nada: são o mesmo'], 1, 'A fraqueza de vontade é agir contra o próprio juízo, não ter um juízo errado.')),
 'pobreza-e-etica-global': (['pratica', 'circulo'], ('Para Thomas Pogge, a pobreza global é sobretudo…', ['Um mal que deixamos de aliviar', 'Um dano que ajudamos a causar, pelas regras globais', 'Responsabilidade só dos países pobres'], 1, 'Por isso, para ele, não é caridade: é reparação, um dever negativo de não prejudicar.')),
 'sofrimento-dos-animais-selvagens': (['animais', 'circulo'], ('Por que a maioria dos animais selvagens que nascem tem vidas curtas e ruins?', ['Por causa dos humanos', 'Porque a maioria das espécies tem muitos filhotes e poucos sobrevivem', 'Porque a natureza é equilibrada'], 1, 'A seleção natural produz o que se reproduz, não o que vive bem.')),
 'animais-e-a-politica': (['animais', 'pratica'], ('Em Zoopolis, animais domesticados teriam…', ['Soberania', 'Residência', 'Cidadania'], 2, 'Nós os trouxemos para dentro da sociedade; seus interesses devem contar nas decisões.')),
 'catastrofes-morais': (['futuro', 'circulo', 'mente'], ('O argumento de Williams conclui que…', ['Sabemos qual é a catástrofe moral de hoje', 'É provável que estejamos cometendo um erro grave sem saber qual', 'A nossa época é a primeira sem erros graves'], 1, 'Toda sociedade do passado cometeu um; supor que a nossa é a exceção exige uma razão que não temos.')),
 'riscos-s-e-riscos-x': (['futuro', 'consequencias'], ('Para uma ética focada no sofrimento, o que é pior do que a extinção?', ['Nada', 'Um futuro cheio de seres em sofrimento extremo', 'Um futuro sem tecnologia'], 1, 'Um universo vazio não sofre; um universo cheio de agonia sofre mais do que tudo o que já existiu.')),
}

REFORCO_NOVAS = {
 'igualdade-humana': dict(
  analogia='Em um hospital, o paciente que chega de helicóptero e o que chega a pé recebem o mesmo exame de prioridade: o que decide é a gravidade, não quem é a pessoa. Um não é “mais paciente” do que o outro. A igualdade humana é isso: a dor de cada um entra na mesma fila, pesada pelo que é, e não por quem a sente.',
  crianca='As crianças da turma são diferentes: uma corre mais, outra desenha melhor, outra sabe mais contas. Mas quando alguém se machuca, a dor de cada uma importa do mesmo jeito. Ser igual não é ser parecido. É contar do mesmo jeito.'),
 'fazer-e-deixar-acontecer': dict(
  analogia='Um salva-vidas que empurra alguém na água é um criminoso. Um que vê alguém se afogar e fica olhando, podendo salvar, também é. Ele não fez “nada”: fez a escolha de não agir, e o afogado não vê diferença. A distinção entre fazer e deixar acontecer vale em alguns casos; no do salva-vidas, não.',
  crianca='Se você derruba o castelo de areia do seu amigo, fez algo ruim. Se vê a onda vindo, pode avisar e não avisa, também fez algo ruim, mesmo sem tocar no castelo. “Eu não fiz nada” às vezes é só outro jeito de fazer.'),
 'fraqueza-de-vontade': dict(
  analogia='Quase todo mundo sabe que deveria dormir mais cedo, e quase todo mundo fica acordado até tarde. Ninguém conclui disso que saber é inútil: conclui que o sono compete com o celular, o hábito e o cansaço. A moral funciona assim. A crença entra na disputa com o resto; não ganha sozinha, mas também não fica de fora.',
  crianca='Você sabe que deveria guardar os brinquedos, e às vezes não guarda. Isso não quer dizer que você não sabe. Quer dizer que a vontade de continuar brincando venceu. Ficar chateado depois mostra que você sabia. O truque é deixar a coisa certa mais fácil de fazer.'),
 'pobreza-e-etica-global': dict(
  analogia='Imagine que no seu prédio um vizinho morre todo mês por falta de um remédio que custa o valor de um jantar fora. Você provavelmente pagaria o remédio. A pobreza extrema é esse prédio, só que o vizinho mora longe e você não vê o rosto dele. A distância muda o que você sente; não muda o que ele perde.',
  crianca='Imagine que, com o dinheiro de um brinquedo, dá para comprar o remédio que salva uma criança que mora longe. Ela não aparece na sua rua, mas existe de verdade, e a vida dela vale tanto quanto a de qualquer amigo seu.'),
 'sofrimento-dos-animais-selvagens': dict(
  analogia='Um terremoto não é culpa de ninguém, e ninguém diz que por isso não se deve socorrer as vítimas. A natureza é um terremoto permanente para a maioria dos animais que nascem. “Não fomos nós” explica de onde o sofrimento veio; não explica por que ele não contaria.',
  crianca='Nos filmes, os bichos da floresta vivem felizes. Na vida real, a maioria dos filhotes não chega a crescer: morre de fome, de doença ou é comida por outro animal. Se a dor de um bicho importa quando ele está na nossa casa, ela também importa quando ele está na floresta.'),
 'animais-e-a-politica': dict(
  analogia='Em um condomínio, as regras são votadas pelos moradores adultos. Mas as crianças e os cães também moram ali, e as regras afetam a vida deles. Alguém precisa falar por quem não vota, ou as decisões sobre eles serão tomadas como se não existissem. A política dos animais é a pergunta sobre quem fala por eles.',
  crianca='Quando a turma vota as regras do recreio, os bichos da escola não votam, mas vivem lá e sentem o que acontece com eles. Alguém precisa lembrar deles na hora de decidir. É isso que alguns filósofos querem fazer com os animais nas leis.'),
 'catastrofes-morais': dict(
  analogia='Um médico que sabe que todo exame de rotina costuma esconder algum problema não sai do consultório dizendo “comigo não”. Ele pede os exames. O argumento das catástrofes morais é esse: se toda época teve um ponto cego grave, o prudente não é supor que somos a exceção, e sim procurar o nosso.',
  crianca='Antigamente, muita gente achava normal coisas que hoje a gente sabe que eram muito erradas, como não deixar algumas pessoas estudar. Eles não eram burros: só não viam. É quase certo que a gente também não vê alguma coisa errada que faz hoje. Por isso vale perguntar “será que isso é certo mesmo?”, principalmente sobre o que todo mundo faz.'),
 'riscos-s-e-riscos-x': dict(
  analogia='Um engenheiro que projeta uma represa pensa em dois desastres: a represa secar e a represa romper e inundar a cidade. São problemas diferentes, com prioridades diferentes, e um bom projeto evita os dois. O risco X é a represa seca: nenhum futuro. O risco S é a inundação: um futuro que afoga quem está nele.',
  crianca='Imagine que a sua turma vai existir por muitos e muitos anos. Dá para pensar em duas coisas ruins: a turma acabar, ou a turma continuar, mas com todo mundo sofrendo. Pensar no futuro é tentar evitar as duas, começando pelo que a gente decide hoje.'),
}
POSICAO_LISTA = {'catastrofes-morais': 'avancado', 'fraqueza-de-vontade': 'intermediario', 'igualdade-humana': 'iniciante', 'fazer-e-deixar-acontecer': 'intermediario', 'pobreza-e-etica-global': 'intermediario', 'sofrimento-dos-animais-selvagens': 'avancado', 'animais-e-a-politica': 'avancado', 'riscos-s-e-riscos-x': 'avancado'}
