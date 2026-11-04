"""Lições do nível Intermediário, parte 1: as teorias por dentro."""
from licoes_iniciante import SEP, IEP, WP, WE, TESTE, MAPA, VINDING, SINGER_PE, RACHELS
UTIL = ('Utilitarianism.net', 'https://utilitarianism.net/')
PARFIT = ('Reasons and Persons', 'https://www.google.com/search?tbm=bks&q=Parfit+Reasons+and+Persons')

INTERMEDIARIO = [
dict(slug='utilitarismo-classico', grupo='Consequencialismo por dentro', titulo='Bentham, Mill e o utilitarismo clássico', resumo='A maior felicidade para o maior número: de onde veio a ideia, o que ela quer dizer de fato e as duas formas de aplicá-la.', corpo='''
<p class="abre">O utilitarismo é a forma mais conhecida de consequencialismo. Diz que a ação certa é a que produz a maior soma de bem-estar, contando igualmente o bem-estar de cada afetado. Nasceu com Jeremy Bentham, foi refinado por John Stuart Mill e Henry Sidgwick, e continua sendo a teoria mais discutida da ética.</p>
<h2>Bentham: a aritmética da felicidade</h2>
<p>Em 1789, Bentham propôs um critério único para julgar leis e ações: o quanto aumentam o prazer e reduzem a dor de todos os afetados. Foi radical para a época. Ele defendeu a descriminalização da homossexualidade, o voto feminino, o fim da escravidão e a proteção legal dos animais, com uma frase que ainda organiza o debate: a pergunta não é se podem raciocinar ou falar, e sim se podem sofrer.</p>
<p>Bentham chegou a propor um “cálculo felicífico”, com intensidade, duração, certeza e extensão do prazer. Ninguém o usa ao pé da letra, mas a ideia de olhar para quem é afetado, e quanto, ficou.</p>
<h2>Mill: qualidade e liberdade</h2>
<p>Mill, em <em>Utilitarismo</em> (1861), respondeu à acusação de que a teoria era “uma filosofia de porcos”. Para ele, há prazeres superiores e inferiores, e quem conhece os dois prefere os superiores: é melhor ser um Sócrates insatisfeito do que um tolo satisfeito. Em <em>Sobre a Liberdade</em>, defendeu que a liberdade individual, protegida por regras firmes, é o que mais promove a felicidade a longo prazo. O utilitarismo de Mill é, por isso, muito mais parecido com uma defesa de direitos do que a caricatura sugere.</p>
<h2>Ato ou regra?</h2>
<table><thead><tr><th>Versão</th><th>Como decide</th><th>Vantagem</th><th>Problema</th></tr></thead><tbody>
<tr><td><a href="teorias/consequencialismo-de-ato.html">De ato</a></td><td>Caso a caso: qual ação, agora, produz mais bem?</td><td>Flexível, sem regras cegas</td><td>Imprevisível; convida a exceções convenientes</td></tr>
<tr><td><a href="teorias/consequencialismo-de-regras.html">De regras</a></td><td>Siga as regras que, aceitas por todos, produzem mais bem</td><td>Previsível; protege a confiança</td><td>Pode mandar seguir a regra quando quebrá-la seria melhor</td></tr>
<tr><td>Dois níveis</td><td>Regras no dia a dia, cálculo direto só em casos extremos ou novos</td><td>Junta as duas vantagens</td><td>Quem decide quando o caso é extremo?</td></tr>
</tbody></table>
<p>R. M. Hare defendeu a versão de dois níveis: pensamos como “prolas”, seguindo regras boas, e só como “arcanjos”, calculando tudo, quando as regras falham. É como a maioria dos utilitaristas pensa hoje.</p>
<h2>O que conta como bem-estar</h2>
<ul>
<li><strong>Hedonismo:</strong> prazer e ausência de dor, como em Bentham.</li>
<li><strong>Preferências:</strong> o que as pessoas de fato querem para si, como em Singer por boa parte da carreira.</li>
<li><strong>Lista objetiva:</strong> saúde, conhecimento, amizade, autonomia, mesmo que a pessoa não os deseje.</li>
</ul>
<p>Essa escolha muda conclusões práticas. Para um hedonista, uma vida feliz dentro da <a href="dilemas/maquina-de-experiencias.html">máquina de experiências</a> de Nozick é tão boa quanto uma vida real. Para quem valoriza preferências ou uma lista de bens, não.</p>
<h2>Por que a teoria continua viva</h2>
<p>Porque faz a pergunta que nenhuma outra pode ignorar: <em>quem fica melhor, quem fica pior, e quanto?</em> Mesmo quem rejeita o utilitarismo como teoria completa usa seu raciocínio em saúde pública, políticas sociais e ajuda humanitária. Os problemas, discutidos em <a href="objecoes-ao-consequencialismo.html">objeções ao consequencialismo</a>, são sobre o que falta, não sobre o que ele vê.</p>
''', fontes=[UTIL, ('Utilitarismo (Wikipédia)', WP + 'Utilitarismo'), ('The History of Utilitarianism (Stanford Encyclopedia)', SEP + 'utilitarianism-history/'), ('Utilitarianism (1861)', 'https://www.gutenberg.org/ebooks/11224')]),

dict(slug='somar-priorizar-ou-garantir', grupo='Consequencialismo por dentro', titulo='Somar, priorizar ou garantir o mínimo?', resumo='Dizer que o resultado importa não diz como juntar o bem de várias pessoas. Utilitarismo, prioritarismo, maximin, igualitarismo e suficientismo dão respostas diferentes.', corpo='''
<p class="abre">Imagine que você pode distribuir recursos entre pessoas. Todas as teorias desta lição concordam que o bem-estar delas importa. Discordam sobre como juntar o bem-estar de muitos em um só julgamento. Essa é a questão da <strong>agregação</strong>.</p>
<h2>Um exemplo para comparar</h2>
<p>Duas políticas. A primeira dá 10 pontos de bem-estar a quem já tem 90, e nada a quem tem 10. A segunda dá 6 pontos a quem tem 10 e nada a quem tem 90. A primeira produz mais bem-estar total; a segunda, mais igualdade. Qual é melhor?</p>
<table><thead><tr><th>Teoria</th><th>Regra</th><th>Neste exemplo</th><th>Crítica comum</th></tr></thead><tbody>
<tr><td><a href="teorias/utilitarismo-classico.html">Utilitarismo clássico</a></td><td>A maior soma total</td><td>Primeira (10 &gt; 6)</td><td>Indiferente a quem recebe; pode sacrificar os que estão pior</td></tr>
<tr><td><a href="teorias/prioritarismo.html">Prioritarismo</a></td><td>Soma, mas um ganho vale mais para quem está pior</td><td>Segunda, provavelmente</td><td>Quanto a mais, exatamente?</td></tr>
<tr><td><a href="teorias/maximin.html">Maximin</a></td><td>Só importa o nível de quem está pior</td><td>Segunda, sempre</td><td>Trocaria um ganho enorme de milhões por um ganho mínimo do pior</td></tr>
<tr><td><a href="teorias/igualitarismo.html">Igualitarismo</a></td><td>O que importa é a igualdade da distribuição</td><td>Segunda</td><td>Nivelar por baixo também iguala</td></tr>
<tr><td><a href="teorias/suficientismo.html">Suficientismo</a></td><td>Garantir um mínimo a todos; acima dele, tanto faz</td><td>Segunda, se 10 está abaixo do mínimo</td><td>Onde fica a linha, e por que acima dela nada importa?</td></tr>
<tr><td><a href="teorias/utilitarismo-medio.html">Utilitarismo médio</a></td><td>A maior média por pessoa</td><td>Primeira</td><td>Aprova reduzir a população para subir a média</td></tr>
</tbody></table>
<h2>Por que o utilitarismo puro incomoda</h2>
<p>Somar sem olhar quem recebe trata o bem-estar como se fosse um só, em um só corpo. John Rawls chamou isso de não levar a sério a <strong>separação entre as pessoas</strong>. Uma sociedade não é um indivíduo grande: o prazer de um não compensa a dor de outro, porque são vidas diferentes. Essa objeção levou muitos consequencialistas ao prioritarismo.</p>
<h2>Por que o prioritarismo atrai</h2>
<p>Derek Parfit o formulou assim: o bem-estar importa mais quanto pior está a pessoa. Isso dá razão para ajudar primeiro quem tem menos, sem o problema do igualitarismo (nivelar por baixo não ajuda ninguém) nem o do maximin (ignorar todos exceto o pior). A dificuldade é escolher o peso extra: a teoria é uma família de curvas, não uma regra só.</p>
<h2>A objeção do nivelamento por baixo</h2>
<p>Se a igualdade tem valor em si, um mundo em que todos estão igualmente mal seria, nesse aspecto, melhor do que um em que alguns estão bem. Quase ninguém aceita isso. Por isso a maioria dos igualitaristas diz que a igualdade importa junto com o bem-estar, nunca sozinha, ou migra para o prioritarismo.</p>
<h2>O que isso muda na prática</h2>
<ul>
<li><strong>Saúde pública:</strong> salvar quem tem menos anos de vida pela frente ou quem está em pior situação?</li>
<li><strong>Impostos:</strong> um real tirado de quem tem muito pesa menos do que um real dado a quem tem pouco. É prioritarismo aplicado.</li>
<li><strong>Ajuda internacional:</strong> o mesmo valor salva muito mais vidas onde a pobreza é extrema. Veja <a href="dilemas/crianca-no-lago.html">a criança no lago</a>.</li>
<li><strong>Animais:</strong> se o que está pior é um frango em uma granja industrial, prioritarismo e maximin apontam para ele.</li>
</ul>
<div class="nota"><strong>Para guardar:</strong> quase ninguém defende a soma pura nem a igualdade pura. O debate real é sobre quanto peso dar a quem está pior, e é aí que as políticas públicas se decidem.</div>
''', fontes=[('Prioritarianism (Stanford Encyclopedia)', SEP + 'prioritarianism/'), ('Egalitarianism (Stanford Encyclopedia)', SEP + 'egalitarianism/'), ('Equality or Priority?', 'https://www.google.com/search?tbm=bks&q=Parfit+Equality+or+Priority'), MAPA]),

dict(slug='o-peso-do-sofrimento', grupo='Consequencialismo por dentro', titulo='O peso do sofrimento diante do prazer', resumo='Um dia bom compensa um dia de agonia? Para alguns, sim, ponto a ponto. Para outros, o sofrimento extremo pesa mais, ou pesa só ele.', corpo='''
<p class="abre">O utilitarismo clássico trata prazer e sofrimento como a mesma moeda com sinais trocados: dez unidades de dor são canceladas por dez de prazer. Muitos filósofos acham isso errado. A questão de quanto o sofrimento pesa diante do prazer divide o consequencialismo em enfoques.</p>
<h2>Os quatro enfoques</h2>
<table><thead><tr><th>Enfoque</th><th>O que diz</th><th>Um exemplo</th></tr></thead><tbody>
<tr><td>Simétrico</td><td>Sofrimento e prazer entram com o mesmo peso</td><td>Vale criar um ser que terá 50 de dor e 51 de prazer</td></tr>
<tr><td><a href="teorias/prioridade-ao-sofrimento.html">Prioridade ao sofrimento</a></td><td>Reduzir sofrimento pesa mais, mas muito prazer ainda compensa</td><td>Só vale criar esse ser se o prazer superar a dor por boa margem</td></tr>
<tr><td><a href="teorias/utilitarismo-negativo.html">Negativo (prioridade absoluta)</a></td><td>Nenhuma quantidade de prazer compensa sofrimento extremo; fora dos extremos, o prazer conta normalmente</td><td>Nenhum paraíso para muitos justifica uma tortura para um</td></tr>
<tr><td><a href="teorias/etica-focada-no-sofrimento.html">Exclusivamente negativo</a></td><td>O prazer nunca tem valor positivo; só reduzir sofrimento conta</td><td>Um mundo sem ninguém não é pior do que um mundo feliz</td></tr>
</tbody></table>
<h2>Por que dar prioridade ao sofrimento</h2>
<ul>
<li><strong>Assimetria da experiência:</strong> a pior dor imaginável parece pior do que o melhor prazer imaginável é bom. Poucos trocariam uma hora de tortura por qualquer quantidade de prazer depois.</li>
<li><strong>Urgência moral:</strong> quem sofre pede ajuda; quem está bem não pede mais prazer. A dor cria uma razão de agir que o prazer não cria da mesma forma.</li>
<li><strong>A assimetria da criação:</strong> parece errado criar alguém que só sofrerá, mas não parece obrigatório criar alguém que só será feliz. Isso sugere que evitar dor pesa mais do que gerar prazer.</li>
<li><strong>Autores:</strong> Karl Popper defendeu que a formulação utilitarista deveria ser “minimizar o sofrimento”, e não “maximizar a felicidade”. Hoje, Magnus Vinding, Brian Tomasik e outros desenvolvem éticas focadas no sofrimento.</li>
</ul>
<h2>As objeções</h2>
<ul>
<li><strong>O argumento do botão:</strong> se só o sofrimento importa, um utilitarista negativo deveria apertar um botão que elimine toda a vida sem dor. Defensores respondem que há incerteza enorme, que isso destruiria o que já valorizamos, e que versões moderadas (prioridade, não exclusividade) não têm essa implicação.</li>
<li><strong>Prazeres valem algo:</strong> a maioria de nós acha que uma vida feliz é boa, e não só não ruim. O enfoque exclusivamente negativo precisa explicar essa intuição.</li>
<li><strong>Onde fica o “extremo”?</strong> A prioridade absoluta a sofrimento extremo exige uma linha. Defensores dizem que a linha é vaga, mas a diferença entre um incômodo e uma agonia é clara o bastante.</li>
</ul>
<h2>Por que isso importa na prática</h2>
<p>O enfoque muda prioridades. Se o sofrimento extremo pesa mais, a atenção vai para onde ele se concentra: dor sem tratamento, tortura, criação industrial de animais, guerras. Projetos de “mais felicidade” para quem já está bem perdem urgência. É uma das razões pelas quais a ética animal ocupa tanto espaço nas éticas focadas no sofrimento: há bilhões de seres em condições de sofrimento intenso, e evitar isso não exige teoria sofisticada, só a decisão de contar quem sofre.</p>
<div class="nota"><strong>Para pensar:</strong> você aceitaria um dia de dor intensa em troca de uma semana de alegria intensa? E um mês? A sua resposta diz qual é o seu enfoque.</div>
''', fontes=[('Negative utilitarianism (Wikipédia)', WE + 'Negative_utilitarianism'), ('Suffering-focused ethics (Wikipédia)', WE + 'Suffering-focused_ethics'), ('Suffering-Focused Ethics: Defense and Implications', 'https://magnusvinding.com/2020/05/31/suffering-focused-ethics-defense-and-implications/'), ('Center for Reducing Suffering', 'https://centerforreducingsuffering.org/')]),

dict(slug='objecoes-ao-consequencialismo', grupo='Consequencialismo por dentro', titulo='As objeções ao consequencialismo, e as respostas', resumo='Exige demais, aprova sacrifícios, não respeita direitos, não dá para calcular. Cada objeção tem uma resposta, e nem todas convencem.', corpo='''
<p class="abre">Nenhuma teoria ética recebeu tantas críticas quanto o consequencialismo, em parte porque é a mais explícita sobre o que defende. Esta lição apresenta as objeções mais fortes e o que os defensores respondem. Você decide quem vence.</p>
<h2>1. Aprova sacrificar inocentes</h2>
<p><strong>A objeção:</strong> um cirurgião pode matar um paciente saudável e usar seus órgãos para salvar cinco. A soma aprova. Veja <a href="dilemas/transplante.html">o dilema do transplante</a>.</p>
<p><strong>A resposta:</strong> em um mundo real, isso destruiria a confiança na medicina, com consequências muito piores. Um consequencialista de regras ou de dois níveis proíbe a prática. <em>Mas:</em> e se ninguém jamais soubesse? A objeção volta, e muitos acham que a resposta correta é “ainda assim é errado”, o que o consequencialismo de ato não consegue dizer.</p>
<h2>2. Exige demais</h2>
<p><strong>A objeção:</strong> se cada real doado pode salvar alguém, você deveria doar até ficar quase tão pobre quanto quem ajuda. Nenhuma vida normal passa nesse teste.</p>
<p><strong>A resposta:</strong> alguns aceitam a exigência e dizem que a culpa é da nossa complacência, não da teoria. Outros distinguem o que é <em>obrigatório</em> do que é <em>ideal</em>, ou dizem que uma exigência tão alta geraria menos bem no total, porque ninguém a seguiria. Veja <a href="quanto-a-moral-pode-exigir.html">quanto a moral pode exigir</a>.</p>
<h2>3. Não dá para calcular</h2>
<p><strong>A objeção:</strong> ninguém conhece todas as consequências de um ato, a longo prazo e para todos.</p>
<p><strong>A resposta:</strong> a teoria diz o que torna um ato certo, não como decidir na hora. Na prática, agimos pelo resultado <em>esperado</em>, com regras boas e humildade. Toda teoria enfrenta incerteza: o deontologista também precisa saber se está mesmo mentindo, e para quem.</p>
<h2>4. Ignora a separação entre pessoas</h2>
<p><strong>A objeção:</strong> somar o bem de todos trata a sociedade como um único organismo. Mas o prazer de um não compensa a dor de outro: são vidas diferentes.</p>
<p><strong>A resposta:</strong> o prioritarismo e as éticas focadas no sofrimento incorporam a objeção, dando peso extra a quem está pior e recusando compensações entre pessoas no caso de sofrimento extremo. Veja <a href="somar-priorizar-ou-garantir.html">como agregar</a>.</p>
<h2>5. O monstro utilitário e a conclusão repugnante</h2>
<p>Dois casos de Nozick e Parfit: um ser que ganha mais prazer do que todos perdem justifica que todos sejam sacrificados a ele; e um mundo imenso de vidas quase sem valor supera um mundo pequeno de vidas excelentes. Veja <a href="dilemas/monstro-utilitario.html">o monstro</a> e <a href="dilemas/conclusao-repugnante.html">a conclusão repugnante</a>. As respostas passam por limites à agregação e por prioridade ao sofrimento, e nenhuma é consensual.</p>
<h2>6. Destrói a integridade</h2>
<p>Bernard Williams objetou que o consequencialismo exige que você trate os próprios projetos e compromissos como uma fonte de bem entre outras. Veja <a href="dilemas/jim-e-os-indigenas.html">Jim e os indígenas</a>. A resposta usual é que relações e projetos geram bem, e uma teoria sensata os protege, mas Williams insistia que isso os protege pelo motivo errado.</p>
<h2>7. Não respeita direitos</h2>
<p>Se direitos só valem enquanto produzem bons resultados, não são direitos: são políticas. Mill respondeu que direitos protegidos com firmeza são justamente o que produz mais bem a longo prazo. Deontologistas acham a resposta boa demais para ser verdade: ela chega à conclusão certa pela razão errada.</p>
<h2>O que fica</h2>
<p>As objeções mostram o que a teoria pura deixa de fora: a separação entre pessoas, o valor de relações e a sensação de que algumas coisas simplesmente não se fazem. Os consequencialistas responderam incorporando boa parte disso. O que não conseguem abandonar, e com razão, é a pergunta central: <em>quem fica melhor e quem fica pior?</em> Qualquer teoria que a ignore também tem um problema.</p>
''', fontes=[('Consequentialism (Stanford Encyclopedia)', SEP + 'consequentialism/'), ('Arguments against utilitarianism (Utilitarianism.net)', 'https://utilitarianism.net/objections-to-utilitarianism/'), ('Utilitarianism: For and Against', 'https://www.google.com/search?tbm=bks&q=Smart+Williams+Utilitarianism+For+and+Against'), PARFIT]),

dict(slug='kant-e-o-imperativo-categorico', grupo='Deontologia por dentro', titulo='Kant e o imperativo categórico', resumo='Aja só segundo uma regra que você poderia querer universal, e trate cada pessoa como fim. As duas fórmulas de Kant, explicadas sem jargão.', corpo='''
<p class="abre">Immanuel Kant construiu a deontologia mais influente da história. Para ele, a moral não vem de Deus nem das consequências, e sim da razão: há regras que qualquer ser racional precisa aceitar, só por ser racional. Ele chamou a regra fundamental de <strong>imperativo categórico</strong>.</p>
<h2>Hipotético e categórico</h2>
<p>Um imperativo hipotético diz “se quer X, faça Y”: se quer passar na prova, estude. Ele depende de um desejo. Um imperativo categórico vale sem condição: não minta, ponto, mesmo que mentir lhe convenha. Para Kant, só o segundo tipo é moral, porque a moral não pode depender do que cada um quer.</p>
<h2>Primeira fórmula: a universalidade</h2>
<p>“Aja só segundo uma máxima que você possa querer que se torne lei universal.” O teste: pegue a regra pessoal por trás do seu ato (“posso quebrar promessas quando me convém”) e imagine todos seguindo-a. Se a prática se destrói, a regra é proibida: se todos quebrassem promessas quando conviesse, ninguém acreditaria em promessas, e prometer deixaria de existir. A mentira, o roubo e a fraude falham no teste pelo mesmo motivo: só funcionam se forem exceção.</p>
<h2>Segunda fórmula: a humanidade como fim</h2>
<p>“Trate a humanidade, na sua pessoa e na de qualquer outro, sempre como fim, nunca apenas como meio.” Usar alguém como meio é normal: o motorista de ônibus é meio para você chegar. O erro é usar <em>apenas</em> como meio, sem que a pessoa possa consentir: enganar, coagir, manipular. Esta fórmula é a origem filosófica da ideia de dignidade humana que aparece nas constituições.</p>
<h2>O que torna Kant forte</h2>
<ul>
<li><strong>Explica por que a mentira ofende:</strong> ela trata o outro como alguém que não merece decidir com a verdade.</li>
<li><strong>Protege cada pessoa da maioria:</strong> ninguém pode ser sacrificado “pelo bem geral”.</li>
<li><strong>Dá base à igualdade:</strong> a dignidade não depende de talento, riqueza ou utilidade.</li>
<li><strong>A boa vontade:</strong> para Kant, a única coisa boa sem restrição é querer fazer o certo por ser certo. Resultados dependem de sorte; a intenção, não.</li>
</ul>
<h2>Os problemas</h2>
<ul>
<li><strong>Rigidez:</strong> Kant disse que não se deve mentir nem para um assassino que pergunta onde está sua vítima. Quase ninguém aceita. Veja <a href="dilemas/mentir-ao-assassino.html">o dilema</a>.</li>
<li><strong>Conflitos de deveres:</strong> o que fazer quando cumprir um dever viola outro? Kant deu pouca orientação.</li>
<li><strong>A máxima certa:</strong> o teste de universalização depende de como se descreve o ato. “Mentir” falha; “mentir para salvar uma vida” talvez passe. Escolher a descrição vira o jogo.</li>
<li><strong>Quem é fim?</strong> Só seres racionais, para Kant. Animais contam apenas indiretamente: a crueldade com eles embrutece quem a pratica. Christine Korsgaard, kantiana, discorda: a capacidade de ter uma vida que importa para si basta para ser fim, e os animais a têm.</li>
</ul>
<h2>Kant hoje</h2>
<p>Poucos são kantianos puros, mas a segunda fórmula está em toda parte: no consentimento informado da medicina, na proibição de tortura, na crítica a manipulações digitais que tratam usuários como meios. Mesmo consequencialistas usam a linguagem da dignidade. É a prova de que a pergunta de Kant, “isso respeita cada pessoa?”, não dá para ser ignorada.</p>
''', fontes=[('Kant’s Moral Philosophy (Stanford Encyclopedia)', SEP + 'kant-moral/'), ('Imperativo categórico (Wikipédia)', WP + 'Imperativo_categ%C3%B3rico'), ('Fundamentação da Metafísica dos Costumes', WP + 'Fundamenta%C3%A7%C3%A3o_da_Metaf%C3%ADsica_dos_Costumes'), ('Fellow Creatures: Our Obligations to the Other Animals', 'https://www.google.com/search?tbm=bks&q=Korsgaard+Fellow+Creatures')]),

dict(slug='direitos-e-limiares', grupo='Deontologia por dentro', titulo='Direitos como trunfos e a deontologia de limiar', resumo='Direitos vencem cálculos de utilidade, como trunfos no baralho. Mas vencem sempre, ou cedem diante de uma catástrofe?', corpo='''
<p class="abre">Dizer que alguém tem um direito é dizer que certas coisas não podem ser feitas a essa pessoa, mesmo que fossem úteis para outras. Ronald Dworkin chamou os direitos de <strong>trunfos</strong>: cartas que vencem o cálculo de utilidade. A pergunta que divide os deontologistas é se eles vencem sempre.</p>
<h2>Direitos como trunfos</h2>
<p>Se a liberdade de expressão de uma pessoa só valesse enquanto fosse útil à maioria, não seria um direito, seria uma concessão. Para Dworkin, o ponto de um direito é proteger o indivíduo justamente quando a maioria quer passar por cima dele. Robert Nozick foi além: direitos são <strong>restrições laterais</strong>, limites ao que qualquer um pode fazer em busca de qualquer meta, inclusive da meta de proteger direitos.</p>
<table><thead><tr><th>Tipo de direito</th><th>O que impõe aos outros</th><th>Exemplo</th></tr></thead><tbody>
<tr><td>Negativo</td><td>Não interferir</td><td>Não ser torturado, não ser censurado</td></tr>
<tr><td>Positivo</td><td>Fornecer algo</td><td>Educação, saúde, socorro</td></tr>
<tr><td>De liberdade</td><td>Deixar fazer</td><td>Culto, associação, expressão</td></tr>
<tr><td>De reivindicação</td><td>Alguém tem o dever correspondente</td><td>Receber o que foi contratado</td></tr>
</tbody></table>
<p>Libertários como Nozick aceitam só os negativos. A tradição dos direitos humanos inclui os positivos. Essa é uma das linhas que separa esquerda e direita, e ela nasce aqui, na teoria dos direitos.</p>
<h2>Absolutismo: nunca</h2>
<p>A <a href="teorias/deontologia-absolutista.html">deontologia absolutista</a> diz que certas restrições nunca podem ser violadas: não torturar, não matar inocentes, não escravizar. Nem para salvar mil vidas. O lema é <em>fiat justitia, ruat caelum</em>: faça-se justiça, ainda que o céu caia. Elizabeth Anscombe defendeu que quem considera, nem que seja por um instante, executar um inocente para salvar outros já mostrou uma mente corrompida.</p>
<h2>Limiar: quase nunca</h2>
<p>A <a href="teorias/deontologia-de-limiar.html">deontologia de limiar</a> responde: as restrições valem com força enorme, mas cedem quando as consequências ultrapassam um limiar catastrófico. Torturar para evitar um constrangimento, jamais; torturar um terrorista para impedir a explosão de uma cidade, talvez. Michael Moore e outros defendem essa posição como a que melhor descreve nossas intuições.</p>
<h2>O problema de cada uma</h2>
<ul>
<li><strong>Absolutismo:</strong> parece fanatismo quando o custo é imenso. Permitir que milhões morram para não violar um direito é difícil de defender diante dessas pessoas.</li>
<li><strong>Limiar:</strong> onde fica a linha, e por quê? Se mil vidas justificam a violação, 999 não? Larry Alexander mostrou que qualquer limiar fixo gera paradoxos. Defensores respondem que a vagueza é da moral, não da teoria, e que vagueza não é arbitrariedade.</li>
<li><strong>As duas:</strong> por que a restrição? Se é errado matar um para salvar cinco, mas não para salvar um milhão, parece que no fundo o número conta. A deontologia de limiar pode ser consequencialismo com freio de mão.</li>
</ul>
<h2>Quem tem direitos?</h2>
<p>Para Nozick e Kant, seres racionais. Mas bebês e pessoas com deficiência cognitiva grave não raciocinam no sentido exigido, e têm direitos. Tom Regan propôs que o critério é ser <strong>sujeito de uma vida</strong>: ter experiências, preferências, um bem-estar que importa para si. Pelo critério, muitos animais são portadores de direitos, inclusive o de não ser usado como recurso. Veja <a href="especismo.html">especismo</a>.</p>
<div class="nota"><strong>Para guardar:</strong> a diferença entre uma política e um direito é o que acontece quando ele é inconveniente. Se cede fácil, era política. A questão é se deve ceder nunca ou só diante da catástrofe.</div>
''', fontes=[('Rights (Stanford Encyclopedia)', SEP + 'rights/'), ('Threshold deontology (Wikipédia)', WE + 'Deontology#Threshold_deontology'), ('Taking Rights Seriously', 'https://www.google.com/search?tbm=bks&q=Dworkin+Taking+Rights+Seriously'), ('The Case for Animal Rights', 'https://www.google.com/search?tbm=bks&q=Regan+The+Case+for+Animal+Rights')]),

dict(slug='intencao-e-previsao', grupo='Deontologia por dentro', titulo='Intenção e previsão: o duplo efeito e os deveres prima facie', resumo='Importa se o dano foi pretendido ou só previsto? E o que fazer quando dois deveres colidem? Duas ferramentas da deontologia moderada.', corpo='''
<p class="abre">Duas ideias refinam a deontologia e a aproximam de como as pessoas de fato julgam: a diferença entre causar um dano de propósito e causá-lo como efeito colateral, e a existência de vários deveres que precisam ser pesados caso a caso.</p>
<h2>A doutrina do duplo efeito</h2>
<p>Formulada por Tomás de Aquino para discutir a legítima defesa, a <a href="teorias/doutrina-do-duplo-efeito.html">doutrina</a> diz que um ato com um efeito bom e um efeito ruim pode ser permitido se:</p>
<ol class="roteiro">
<li>O ato em si não é errado.</li>
<li>O efeito ruim é previsto, mas não pretendido, nem como fim nem como meio.</li>
<li>O efeito bom não é produzido pelo efeito ruim.</li>
<li>O bem é proporcional ao mal causado.</li>
</ol>
<table><thead><tr><th>Caso</th><th>Dano</th><th>Veredito usual</th></tr></thead><tbody>
<tr><td>Bombardear uma fábrica de armas, prevendo mortes de civis vizinhos</td><td>Previsto</td><td>Pode ser permitido, se proporcional</td></tr>
<tr><td>Bombardear civis para quebrar o moral do inimigo</td><td>Pretendido como meio</td><td>Proibido</td></tr>
<tr><td>Dar morfina a um doente terminal, prevendo que acelere a morte</td><td>Previsto</td><td>Permitido</td></tr>
<tr><td>Dar uma dose letal para acabar com o sofrimento</td><td>Pretendido</td><td>Proibido pela doutrina; permitido por muitos consequencialistas</td></tr>
<tr><td>Desviar o bonde para o trilho com uma pessoa</td><td>Previsto</td><td>Permitido</td></tr>
<tr><td>Empurrar alguém da passarela para parar o bonde</td><td>Pretendido como meio</td><td>Proibido</td></tr>
</tbody></table>
<p>A doutrina explica por que a maioria desvia o bonde mas não empurra o homem da passarela, mesmo com o mesmo número de mortos. Veja <a href="o-dilema-do-bonde.html">o dilema do bonde</a>.</p>
<h2>As críticas</h2>
<ul>
<li><strong>A vítima não vê diferença:</strong> quem morre como efeito colateral morre do mesmo jeito. Por que a intenção de quem age muda o que é devido a quem sofre?</li>
<li><strong>Dá para redescrever a intenção:</strong> “não pretendi matá-lo, só pretendi que seu corpo parasse o bonde”. A doutrina precisa de um critério para separar intenção genuína de truque verbal, e ele é difícil.</li>
<li><strong>Serve para lavar as mãos:</strong> na guerra, “dano colateral” virou um jeito de aceitar mortes que seriam inaceitáveis se pretendidas. O critério da proporcionalidade tenta conter isso, mas é elástico.</li>
</ul>
<h2>Os deveres prima facie de Ross</h2>
<p>W. D. Ross observou, em 1930, que temos vários deveres, nenhum absoluto: fidelidade (cumprir promessas), reparação, gratidão, justiça, beneficência, autoaperfeiçoamento e não causar dano. Cada um vale <em>prima facie</em>, à primeira vista. Quando colidem, é preciso julgar qual pesa mais naquele caso, sem fórmula. Essa é a <a href="teorias/deontologia-pluralista.html">deontologia pluralista</a>.</p>
<p>A força de Ross é descrever como pensamos: sentimos que prometer cria um dever, e que salvar uma vida pode anulá-lo, sem que a promessa deixe de contar. A fraqueza é não dizer como pesar. Ross respondeu que a moral é assim: juízo, não cálculo. Para muitos, isso é honestidade; para críticos, é desistir de teorizar.</p>
<div class="nota"><strong>Para guardar:</strong> a diferença entre pretender e prever e a ideia de deveres que se pesam são o que torna a deontologia aplicável fora dos livros. Elas também mostram onde ela precisa de juízo, e não só de regras.</div>
''', fontes=[('Doctrine of Double Effect (Stanford Encyclopedia)', SEP + 'double-effect/'), ('W. D. Ross (Stanford Encyclopedia)', SEP + 'william-david-ross/'), ('The Right and the Good', 'https://www.google.com/search?tbm=bks&q=Ross+The+Right+and+the+Good')]),

dict(slug='etica-e-religiao', grupo='Deontologia por dentro', titulo='Ética e religião: o dilema de Eutífron', resumo='Algo é bom porque Deus manda, ou Deus manda porque é bom? A pergunta de Platão ainda organiza o debate entre crentes e não crentes.', corpo='''
<p class="abre">Para boa parte da humanidade, a moral vem da religião. A filosofia não nega a importância das tradições religiosas, mas faz uma pergunta que crentes e não crentes precisam enfrentar: a relação entre o que Deus manda e o que é bom.</p>
<h2>A pergunta de Platão</h2>
<p>No diálogo <em>Eutífron</em>, Sócrates pergunta: o que é piedoso é piedoso porque os deuses o amam, ou os deuses o amam porque é piedoso? Traduzindo para o monoteísmo:</p>
<div class="passos"><div><span>A</span><h3>Bom porque Deus manda</h3><p>A vontade divina define o bem. Se Deus mandasse torturar crianças, seria bom. A moral parece arbitrária.</p></div><div><span>B</span><h3>Deus manda porque é bom</h3><p>Há um padrão de bondade que Deus reconhece. Então o padrão existe independentemente, e podemos estudá-lo com a razão.</p></div></div>
<p>A opção A é a <a href="teorias/teoria-do-mandamento-divino.html">teoria do mandamento divino</a> tradicional. A opção B leva a uma moral acessível a todos, crentes ou não. Nenhuma das duas é confortável para quem quer que a moral dependa inteiramente de Deus.</p>
<h2>A resposta modificada</h2>
<p>Teólogos e filósofos como Robert Adams propuseram uma terceira via: Deus manda o bom porque a sua própria natureza é boa. O bem não é arbitrário (não é o que Deus poderia mandar à toa) nem externo a Deus (é a natureza dele). A objeção comum: como sabemos que a natureza de Deus é boa, sem já ter um conceito de bondade para julgar? A discussão segue aberta há séculos.</p>
<h2>O que a religião oferece à ética</h2>
<ul>
<li><strong>Tradição de reflexão:</strong> Tomás de Aquino, Maimônides, Al-Ghazali e tantos outros pensaram a moral com rigor.</li>
<li><strong>Comunidade e prática:</strong> a moral se aprende vivendo, e as religiões organizam esse aprendizado.</li>
<li><strong>Motivação:</strong> para muitos, a fé sustenta a ação boa quando a razão sozinha não bastaria.</li>
<li><strong>A regra de ouro:</strong> aparece em quase todas as tradições, o que sugere um núcleo moral comum.</li>
</ul>
<h2>O que a ética oferece à religião</h2>
<ul>
<li><strong>Critério para interpretar:</strong> todo texto sagrado tem passagens que os próprios fiéis não seguem ao pé da letra. A escolha do que seguir usa um juízo moral anterior.</li>
<li><strong>Linguagem comum:</strong> em sociedades plurais, argumentos que só valem para quem compartilha a fé não convencem os demais. A razão moral permite conversar.</li>
<li><strong>Proteção contra o abuso:</strong> “Deus quer” já justificou guerras, escravidão e perseguições. Um padrão de bondade examinável é um freio.</li>
</ul>
<h2>Pessoas sem religião têm moral?</h2>
<p>Os dados dizem que sim: taxas de crime, confiança e cooperação não são piores em sociedades menos religiosas, e indivíduos não religiosos relatam os mesmos juízos básicos sobre dano e justiça. Isso é compatível com a opção B: o padrão moral é acessível a todos. O que varia é a motivação e a comunidade, não o conteúdo central.</p>
<div class="nota"><strong>Para guardar:</strong> a pergunta de Eutífron não é um ataque à fé. É um convite para que crentes e não crentes discutam o bem com razões que os dois lados possam avaliar.</div>
''', fontes=[('Eutífron (Wikipédia)', WP + 'Eut%C3%ADfron'), ('Religion and Morality (Stanford Encyclopedia)', SEP + 'religion-morality/'), ('Divine Command Theory (Internet Encyclopedia of Philosophy)', IEP + 'divine-command-theory/')]),

dict(slug='aristoteles-e-as-virtudes', grupo='Caráter, cuidado e contrato', titulo='Aristóteles, a vida boa e as virtudes', resumo='Eudaimonia, o meio-termo e a sabedoria prática: por que a ética das virtudes voltou ao centro do debate depois de dois mil anos.', corpo='''
<p class="abre">A <em>Ética a Nicômaco</em> de Aristóteles é o texto fundador da ética das virtudes. Ela pergunta o que é uma vida boa para um ser humano, e responde que é uma vida de atividade virtuosa, guiada pela razão prática.</p>
<h2>Eudaimonia</h2>
<p>A palavra costuma ser traduzida por felicidade, mas significa algo mais próximo de <em>florescimento</em>: uma vida realizada, vivida bem como um todo. Não é um estado de prazer, e sim uma atividade. Para Aristóteles, todo ser tem uma função, e o florescimento humano está em exercer bem o que nos é próprio: a razão, em pensamento e em ação.</p>
<h2>Virtude como hábito</h2>
<p>Ninguém nasce virtuoso. Tornamo-nos justos praticando a justiça, corajosos praticando a coragem. A virtude é uma disposição estável, adquirida pelo hábito, de sentir e agir corretamente. Isso tem uma consequência prática: a educação moral é treino, exemplo e repetição, muito mais do que teoria.</p>
<h2>O meio-termo</h2>
<p>Cada virtude é um acerto entre dois vícios, um por falta e outro por excesso. A coragem fica entre a covardia e a temeridade; a generosidade, entre a avareza e o desperdício. O meio-termo não é uma média aritmética nem mediocridade: é agir na medida certa, na hora certa, pelo motivo certo, em relação às pessoas certas. Isso exige julgamento, e nenhuma regra o substitui.</p>
<h2>Phronesis, a sabedoria prática</h2>
<p>É a virtude que coordena as outras: a capacidade de perceber o que a situação pede e de encontrar o meio-termo em cada caso. Para Aristóteles, uma pessoa de boa vontade sem phronesis pode fazer o mal com boas intenções. Isso explica por que a ética das virtudes desconfia de regras fixas: a vida é mais variada do que qualquer lista.</p>
<h2>A volta das virtudes</h2>
<p>Depois de séculos de domínio de Kant e do utilitarismo, a ética das virtudes voltou em 1958, com um artigo de Elizabeth Anscombe. Ela argumentou que conceitos como “obrigação” haviam perdido o sentido fora de um quadro religioso, e que a ética deveria voltar a falar de caráter e de florescimento. Seguiram-a Philippa Foot, Alasdair MacIntyre (<em>Depois da Virtude</em>, 1981), Rosalind Hursthouse e Martha Nussbaum.</p>
<table><thead><tr><th>Autor</th><th>Contribuição</th></tr></thead><tbody>
<tr><td><a href="filosofos/anscombe.html">Anscombe</a></td><td>Reabriu o debate; criou o termo “consequencialismo” como crítica</td></tr>
<tr><td><a href="filosofos/foot.html">Foot</a></td><td>Virtudes como o que faz um ser humano bom, assim como raízes fazem uma árvore boa</td></tr>
<tr><td><a href="filosofos/macintyre.html">MacIntyre</a></td><td>Virtudes vivem em tradições e comunidades; a modernidade as perdeu</td></tr>
<tr><td><a href="filosofos/hursthouse.html">Hursthouse</a></td><td>A ética das virtudes dá orientação para a ação, pelas “regras-v”</td></tr>
<tr><td><a href="filosofos/nussbaum.html">Nussbaum</a></td><td>Lista de capacidades para uma vida digna, inspirada em Aristóteles</td></tr>
</tbody></table>
<h2>Os limites de Aristóteles</h2>
<p>Ele aceitou a escravidão e a inferioridade das mulheres como naturais. Isso mostra o risco de uma ética baseada em “o que é próprio do ser humano”: quem define o que é próprio pode excluir quem quiser. Os aristotélicos de hoje respondem que a teoria é melhor do que o seu autor, e que o florescimento, bem entendido, vale para todos os que podem florescer, humanos ou não. Nussbaum estendeu sua lista de capacidades aos animais.</p>
<div class="nota"><strong>Para guardar:</strong> a pergunta de Aristóteles, “que tipo de pessoa estou me tornando?”, acompanha cada escolha. Ela não substitui as outras perguntas, mas nenhuma teoria conseguiu dispensá-la.</div>
''', fontes=[('Aristotle’s Ethics (Stanford Encyclopedia)', SEP + 'aristotle-ethics/'), ('Ética a Nicômaco', WP + '%C3%89tica_a_Nic%C3%B4maco'), ('Modern Moral Philosophy (1958)', WE + 'Modern_Moral_Philosophy'), ('Depois da Virtude', 'https://www.google.com/search?tbm=bks&q=MacIntyre+Depois+da+Virtude')]),

dict(slug='etica-do-cuidado', grupo='Caráter, cuidado e contrato', titulo='A ética do cuidado', resumo='Gilligan, Noddings e Held: a moral começa em relações de dependência, não entre estranhos que negociam. O que isso muda e o que não muda.', corpo='''
<p class="abre">A ética do cuidado nasceu de uma observação: as grandes teorias partem de indivíduos adultos, independentes e iguais, que negociam regras. Mas ninguém começa assim. Começamos dependentes, e passamos boa parte da vida cuidando ou sendo cuidados. Uma ética que ignora isso deixa de fora a maior parte da experiência moral.</p>
<h2>A origem: Gilligan contra Kohlberg</h2>
<p>Nos anos 1970, Lawrence Kohlberg propôs estágios de desenvolvimento moral, com o raciocínio por princípios abstratos no topo. Meninas e mulheres pontuavam menos. Carol Gilligan, sua colaboradora, ouviu as mesmas entrevistas e concluiu em <em>Uma Voz Diferente</em> (1982) que elas não raciocinavam pior: raciocinavam de outro modo, atentas a relações, contexto e às necessidades concretas de cada envolvido. Kohlberg havia medido uma “voz” e chamado a outra de imatura.</p>
<p>Gilligan não disse que mulheres são cuidadosas e homens justos por natureza. Disse que há duas orientações morais, a da justiça e a do cuidado, e que as duas são necessárias.</p>
<h2>O que é cuidar</h2>
<p>Nel Noddings descreveu o cuidado como uma relação: quem cuida se volta para o outro, percebe suas necessidades e responde; quem é cuidado reconhece a resposta. Joan Tronto listou fases: perceber a necessidade, assumir a responsabilidade, prestar o cuidado com competência e verificar se funcionou. O cuidado não é sentimento vago. É atenção mais ação mais verificação.</p>
<h2>O que a ética do cuidado critica</h2>
<table><thead><tr><th>Teorias tradicionais</th><th>Ética do cuidado</th></tr></thead><tbody>
<tr><td>Partem de indivíduos independentes</td><td>Parte de pessoas em relações de dependência</td></tr>
<tr><td>Valorizam imparcialidade e distância</td><td>Valoriza atenção ao particular e proximidade</td></tr>
<tr><td>Veem a emoção como obstáculo</td><td>Vê a emoção como forma de perceber</td></tr>
<tr><td>Buscam princípios universais</td><td>Busca respostas adequadas a cada relação</td></tr>
<tr><td>Trabalho de cuidado é invisível</td><td>Trabalho de cuidado é o centro da vida moral</td></tr>
</tbody></table>
<h2>As objeções</h2>
<ul>
<li><strong>Parcialidade:</strong> cuidar dos “meus” pode justificar ignorar os de fora. Virginia Held e outras respondem que o cuidado deve se expandir: começa perto, mas não termina ali.</li>
<li><strong>Reforça estereótipos:</strong> associar cuidado a mulheres pode naturalizar a divisão que oprime. Muitas autoras insistem que o cuidado é humano, não feminino, e que o problema é sua desvalorização.</li>
<li><strong>Falta critério:</strong> como saber se o cuidado é bom? Noddings respondeu que o cuidado bom é o que a pessoa cuidada reconhece como tal, mas isso não resolve casos em que quem é cuidado não pode responder.</li>
<li><strong>Precisa de justiça:</strong> relações de cuidado podem ser exploradoras. A maioria das autoras hoje defende cuidado <em>e</em> justiça, não um no lugar do outro.</li>
</ul>
<h2>Cuidado e animais</h2>
<p>Josephine Donovan e Carol Adams argumentam que a ética do cuidado tem uma vantagem na questão animal: em vez de debater se animais têm direitos, pergunta o que eles precisam e como respondemos. A atenção à vulnerabilidade concreta, central ao cuidado, aponta diretamente para quem está mais vulnerável, e bilhões de animais estão.</p>
<div class="nota"><strong>Para guardar:</strong> a ética do cuidado lembra que, antes de qualquer princípio, alguém nos alimentou e nos protegeu. Uma teoria que não dá conta disso não dá conta de nós.</div>
''', fontes=[('Feminist Ethics (Stanford Encyclopedia)', SEP + 'feminism-ethics/'), ('Care Ethics (Internet Encyclopedia of Philosophy)', IEP + 'care-ethics/'), ('Uma Voz Diferente', 'https://www.google.com/search?tbm=bks&q=Gilligan+In+a+Different+Voice'), ('The Feminist Care Tradition in Animal Ethics', 'https://www.google.com/search?tbm=bks&q=Donovan+Adams+Feminist+Care+Tradition+in+Animal+Ethics')]),

dict(slug='contratualismo', grupo='Caráter, cuidado e contrato', titulo='Contratualismo: a moral como acordo', resumo='Certo é o que pessoas razoáveis aceitariam, de Hobbes a Scanlon. E o que acontece quando o véu da ignorância esconde também a espécie.', corpo='''
<p class="abre">O contratualismo diz que os princípios morais são aqueles que as pessoas aceitariam em um acordo justo. A ideia tem versões muito diferentes, conforme quem senta à mesa, o que sabe e o que busca.</p>
<h2>Hobbes: paz entre interessados</h2>
<p>Em <em>Leviatã</em> (1651), Thomas Hobbes imaginou a vida sem regras: uma guerra de todos contra todos, em que a vida é “solitária, pobre, sórdida, brutal e curta”. Pessoas racionais e interessadas em si aceitariam regras para ter segurança mútua. A moral, nessa versão, é um pacto de não agressão entre quem pode se ameaçar. O problema: quem não pode ameaçar ninguém (bebês, pessoas com deficiência grave, animais) fica fora do contrato, e a teoria não tem como protegê-los, a não ser indiretamente. Veja o <a href="teorias/contratualismo-hobbesiano.html">contratualismo hobbesiano</a>.</p>
<h2>Rawls: justiça sob o véu</h2>
<p>John Rawls, em <em>Uma Teoria da Justiça</em> (1971), mudou a mesa. As partes escolhem os princípios da sociedade por trás de um <strong>véu da ignorância</strong>: não sabem sua classe, talento, religião, sexo ou saúde. Sem saber quem serão, escolheriam liberdades iguais para todos e permitiriam desigualdades só se beneficiassem quem está pior. O véu força a imparcialidade: ninguém escolhe regras que o beneficiem, porque não sabe quem é. Veja o <a href="teorias/contratualismo-rawlsiano.html">contratualismo rawlsiano</a>.</p>
<h2>Scanlon: o que ninguém pode rejeitar</h2>
<p>T. M. Scanlon, em <em>O Que Devemos Uns aos Outros</em> (1998), propôs que um ato é errado quando é proibido por princípios que ninguém poderia razoavelmente rejeitar. A diferença para o utilitarismo: as objeções são de cada pessoa, não da soma. Um princípio que impõe um custo imenso a alguém pode ser rejeitado por ela, mesmo que beneficie milhões um pouco. Isso reconstrói a separação entre pessoas dentro do contrato. Veja o <a href="teorias/contratualismo-escanloniano.html">contratualismo escanloniano</a>.</p>
<table><thead><tr><th>Versão</th><th>Quem contrata</th><th>Com que motivação</th><th>Quem fica fora</th></tr></thead><tbody>
<tr><td>Hobbes</td><td>Quem pode ameaçar e ser ameaçado</td><td>Interesse próprio</td><td>Os que não podem ameaçar</td></tr>
<tr><td>Rawls</td><td>Pessoas livres e iguais sob o véu</td><td>Justiça e interesse</td><td>Quem não é “pessoa moral”, inclusive animais</td></tr>
<tr><td>Scanlon</td><td>Quem pode ser razoável</td><td>Justificar-se aos outros</td><td>Quem não pode exigir justificativas</td></tr>
<tr><td>Rowlands</td><td>Qualquer um, sem saber a própria espécie</td><td>Imparcialidade</td><td>Ninguém que possa ter interesses</td></tr>
</tbody></table>
<h2>O problema de quem fica fora</h2>
<p>A objeção mais forte ao contratualismo é que ele parece deixar fora do círculo quem não pode contratar. Rawls admitiu que sua teoria não tratava dos animais, e que isso era uma lacuna. Mark Rowlands respondeu de dentro da teoria: se o véu esconde traços que não merecemos (talento, classe, sexo), e a espécie também não é merecida, o véu deveria escondê-la. Sem saber se nasceria humano ou porco, que regras você aceitaria para a criação de animais? É o <a href="teorias/contratualismo-estendido.html">contratualismo estendido</a>.</p>
<h2>O que torna o contratualismo atraente</h2>
<ul>
<li><strong>Explica a autoridade da moral:</strong> as regras valem porque você as aceitaria, não porque alguém as impôs.</li>
<li><strong>Leva a sério cada pessoa:</strong> em Scanlon, uma objeção individual pode derrubar um princípio.</li>
<li><strong>Produz o teste mais usado da ética:</strong> o véu de Rawls é a ferramenta de <a href="imparcialidade.html">imparcialidade</a> mais conhecida do mundo.</li>
</ul>
<div class="nota"><strong>Para guardar:</strong> o contratualismo é tão bom quanto a mesa que monta. A pergunta decisiva é quem está sentado nela, e o que foi escondido sob o véu.</div>
''', fontes=[('Contractualism (Stanford Encyclopedia)', SEP + 'contractualism/'), ('Contemporary Approaches to the Social Contract (Stanford Encyclopedia)', SEP + 'contractarianism-contemporary/'), ('Uma Teoria da Justiça', WP + 'Uma_Teoria_da_Justi%C3%A7a'), ('Animal Rights: Moral Theory and Practice', 'https://www.google.com/search?tbm=bks&q=Rowlands+Animal+Rights+Moral+Theory+and+Practice')]),
]
