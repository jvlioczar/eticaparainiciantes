"""Lições acrescentadas em novembro de 2026 (terceira leva, parte 1): livre-arbítrio, bem-estar, pluralismo de valores, parcialidade, emoções morais,
epistemologia moral, situacionismo e história da ética."""
from licoes_iniciante import SEP, IEP, WP, WE, TESTE, MAPA, VINDING, SINGER_PE

POSICAO3 = {'historia-da-etica': 'argumentos-morais', 'parcialidade-e-deveres-especiais': 'igualdade-humana', 'teorias-do-bem-estar': 'utilitarismo-classico', 'emocoes-morais': 'psicologia-moral', 'situacionismo-e-experimentos': 'emocoes-morais', 'livre-arbitrio-e-responsabilidade': 'fraqueza-de-vontade', 'epistemologia-moral': 'evolucao-e-moral', 'pluralismo-de-valores': 'probabilidade-e-etica'}

NOVAS3_INICIANTE = [
dict(slug='historia-da-etica', grupo='O básico', titulo='Uma breve história da ética', resumo='De Confúcio e Sócrates a Parfit e Singer: as perguntas mudaram menos do que as respostas. Um mapa do tempo para situar cada lição.', corpo='''
<p class="abre">A ética como reflexão organizada tem cerca de 2.500 anos, e começou em vários lugares ao mesmo tempo: na Grécia, na Índia e na China, entre os séculos VI e IV a.C. Esta lição é um mapa do tempo, para que você saiba onde cada teoria e cada filósofo do site se encaixam.</p>
<h2>Antiguidade: como viver bem</h2>
<table><thead><tr><th>Quando</th><th>Quem</th><th>A pergunta e a resposta</th></tr></thead><tbody>
<tr><td>Século VI a.C.</td><td><a href="filosofos/confucio.html">Confúcio</a>, Laozi</td><td>Como viver em harmonia? Pela benevolência, pelo ritual e pelo exemplo (Confúcio); pelo não forçar (Laozi).</td></tr>
<tr><td>Século V a.C.</td><td><a href="filosofos/sidarta-gautama.html">Buda</a>, Mahavira</td><td>Como cessar o sofrimento? Pelo caminho ético e pela compaixão com todos os seres (budismo); pela não violência radical (jainismo).</td></tr>
<tr><td>Século V a.C.</td><td><a href="filosofos/mozi.html">Mozi</a></td><td>O cuidado deve ser imparcial: amar todos igualmente, e julgar práticas pelos benefícios. O primeiro consequencialista.</td></tr>
<tr><td>Século V a.C.</td><td>Sócrates, <a href="filosofos/platao.html">Platão</a></td><td>O que é a justiça, e vale por si? Sim: a alma justa vive em ordem. Conhecer o bem é condição de fazê-lo.</td></tr>
<tr><td>Século IV a.C.</td><td><a href="filosofos/aristoteles.html">Aristóteles</a></td><td>O que é uma vida boa? O florescimento pela virtude, aprendida pelo hábito e guiada pela sabedoria prática.</td></tr>
<tr><td>Séculos IV a III a.C.</td><td><a href="filosofos/epicuro.html">Epicuro</a>, Zenão</td><td>O prazer tranquilo e a amizade (epicurismo); a virtude como único bem e a aceitação do que não depende de nós (estoicismo).</td></tr>
</tbody></table>
<p>O traço comum da ética antiga: a pergunta central é <em>que vida vale a pena viver</em>, e a resposta passa pelo caráter. Regras e consequências aparecem, mas não são o centro.</p>
<h2>Idade Média: a moral e Deus</h2>
<p>Com o cristianismo, o judaísmo rabínico e o islã, a ética passa a dialogar com a revelação. Agostinho (século V) liga a moral à vontade e ao amor a Deus. Maimônides e Al-Ghazali (séculos XI e XII) tentam conciliar Aristóteles com a lei religiosa. <a href="filosofos/tomas-de-aquino.html">Tomás de Aquino</a> (século XIII) faz a síntese: a razão pode conhecer o bem pela lei natural, e a revelação a completa. O <a href="etica-e-religiao.html">dilema de Eutífron</a> atravessa o período.</p>
<h2>Modernidade: a moral sem Deus como premissa</h2>
<table><thead><tr><th>Quando</th><th>Quem</th><th>A ideia</th></tr></thead><tbody>
<tr><td>1651</td><td><a href="filosofos/hobbes.html">Hobbes</a></td><td>A moral como pacto entre interessados em paz: o contrato social.</td></tr>
<tr><td>1739–1751</td><td><a href="filosofos/hume.html">Hume</a></td><td>A razão não motiva; a moral vem do sentimento e da simpatia. Do “é” não se tira o “deve”.</td></tr>
<tr><td>1759</td><td><a href="filosofos/adam-smith.html">Adam Smith</a></td><td>O espectador imparcial: julgamos bem quando imaginamos como um observador justo nos veria.</td></tr>
<tr><td>1785</td><td><a href="filosofos/kant.html">Kant</a></td><td>A moral vem da razão: o imperativo categórico e a pessoa como fim em si.</td></tr>
<tr><td>1789</td><td><a href="filosofos/bentham.html">Bentham</a></td><td>O utilitarismo: a maior felicidade para o maior número, contando quem pode sofrer, inclusive os animais.</td></tr>
<tr><td>1841</td><td><a href="filosofos/schopenhauer.html">Schopenhauer</a></td><td>A compaixão como base da moral, estendida aos animais.</td></tr>
<tr><td>1861–1874</td><td><a href="filosofos/mill.html">Mill</a>, <a href="filosofos/sidgwick.html">Sidgwick</a></td><td>O utilitarismo refinado: liberdade, prazeres superiores, o ponto de vista do universo.</td></tr>
<tr><td>1887</td><td><a href="filosofos/nietzsche.html">Nietzsche</a></td><td>A genealogia da moral: os valores têm história e interesses; é preciso criar valores.</td></tr>
</tbody></table>
<h2>Século XX: o que é um juízo moral?</h2>
<p>A primeira metade do século foi da <strong>metaética</strong>: <a href="filosofos/moore.html">Moore</a> (1903) perguntou o que “bom” significa; <a href="filosofos/ayer.html">Ayer</a> (1936) respondeu que juízos morais são expressões de emoção; <a href="filosofos/hare.html">Hare</a> (1952) que são prescrições universalizáveis; <a href="filosofos/mackie.html">Mackie</a> (1977) que são todos falsos. O existencialismo de <a href="filosofos/sartre.html">Sartre</a> e <a href="filosofos/beauvoir.html">Beauvoir</a> colocou a liberdade e a responsabilidade no centro, e <a href="filosofos/arendt.html">Arendt</a>, depois do Holocausto, perguntou como pessoas comuns participam do mal.</p>
<p>A segunda metade reabriu a ética normativa: <a href="filosofos/anscombe.html">Anscombe</a> (1958) trouxe de volta as virtudes; <a href="filosofos/rawls.html">Rawls</a> (1971) relançou o contrato social com o véu da ignorância; <a href="filosofos/nozick.html">Nozick</a> (1974) respondeu com os direitos; <a href="filosofos/singer.html">Singer</a> (1975) estendeu a igualdade aos animais; <a href="filosofos/gilligan.html">Gilligan</a> (1982) fundou a ética do cuidado; <a href="filosofos/parfit.html">Parfit</a> (1984) abriu a ética populacional; <a href="filosofos/habermas.html">Habermas</a> formulou a ética do discurso; <a href="filosofos/scanlon.html">Scanlon</a> (1998) o contratualismo da justificabilidade.</p>
<h2>Século XXI: fronteiras</h2>
<p>As perguntas abertas de hoje são sobre as <a href="circulo-moral.html">fronteiras do círculo</a>: animais selvagens, gerações futuras, mentes artificiais; sobre como agir sob <a href="incerteza-moral.html">incerteza</a> sobre a própria teoria; sobre o que a <a href="psicologia-moral.html">psicologia</a> e a evolução dizem da confiabilidade das nossas intuições; e sobre os <a href="riscos-s-e-riscos-x.html">riscos de longo prazo</a>. <a href="filosofos/korsgaard.html">Korsgaard</a>, <a href="filosofos/nussbaum.html">Nussbaum</a>, <a href="filosofos/horta.html">Horta</a>, <a href="filosofos/ord.html">Ord</a> e <a href="filosofos/baumann.html">Baumann</a> estão entre os nomes dessa geração.</p>
<h2>O que mudou e o que não mudou</h2>
<ul>
<li><strong>Mudou o centro:</strong> da vida boa (Antiguidade) para a lei divina (Idade Média), para a regra e o resultado (Modernidade), para o significado do juízo (século XX), para quem conta (hoje).</li>
<li><strong>Mudou o círculo:</strong> de cidadãos livres (Aristóteles aceitava a escravidão) para todos os humanos, e agora para além deles. Mozi, Buda e Mahavira estavam, nisso, à frente do Ocidente.</li>
<li><strong>Não mudou a pergunta:</strong> como devo agir, e por quê? Nem o método: argumentos, casos e coerência.</li>
</ul>
<div class="nota"><strong>Para guardar:</strong> quase toda ideia “nova” em ética tem um ancestral antigo. Saber a história ajuda a não reinventar a roda, e a ver que o progresso foi real: ninguém hoje defende a escravidão com Aristóteles.</div>
''', fontes=[('History of ethics (Wikipédia)', WE + 'History_of_ethics'), ('História da ética (Wikipédia)', WP + '%C3%89tica#Hist%C3%B3ria'), ('A Short History of Ethics', 'https://www.google.com/search?tbm=bks&q=MacIntyre+A+Short+History+of+Ethics'), ('Chinese Ethics (Stanford Encyclopedia)', SEP + 'ethics-chinese/')]),

dict(slug='parcialidade-e-deveres-especiais', grupo='Quem conta', titulo='Parcialidade: até onde cuidar mais dos seus?', resumo='Você deve mais ao seu filho do que a um estranho. Quase todos concordam. A pergunta é por quê, e onde a parcialidade legítima vira exclusão.', corpo='''
<p class="abre">A imparcialidade diz que interesses iguais contam igual. Mas ninguém vive assim: damos mais à família, aos amigos, a quem nos ajudou. Isso é uma falha da imparcialidade, uma falha nossa, ou há deveres especiais que a imparcialidade mesma reconhece?</p>
<h2>O problema</h2>
<p>William Godwin, no século XVIII, propôs um caso: em um incêndio, você pode salvar um grande benfeitor da humanidade ou a sua mãe. Godwin disse que a imparcialidade manda salvar o benfeitor. Quase todo mundo recua. Bernard Williams respondeu com outro caso: um homem pode salvar a esposa ou um estranho, e pensa “é minha esposa, e a moral permite que eu a prefira”. Para Williams, esse “e a moral permite” é um pensamento a mais: quem ama não consulta a teoria antes de agir.</p>
<h2>De onde vêm os deveres especiais</h2>
<table><thead><tr><th>Fonte</th><th>Exemplo</th><th>O que gera</th></tr></thead><tbody>
<tr><td>Promessas e acordos</td><td>Casamento, contrato, compromisso</td><td>Dever de cumprir o prometido</td></tr>
<tr><td>Relações em curso</td><td>Amizade, parceria</td><td>Dever de atenção e lealdade, na medida da relação</td></tr>
<tr><td>Dependência que criamos</td><td>Filhos, animais que adotamos</td><td>Dever de cuidado: nós os colocamos em dependência</td></tr>
<tr><td>Benefícios recebidos</td><td>Pais que cuidaram, quem nos ajudou</td><td>Gratidão</td></tr>
<tr><td>Instituições compartilhadas</td><td>Concidadãos</td><td>Deveres recíprocos, mais fracos</td></tr>
</tbody></table>
<h2>Como a imparcialidade acomoda a parcialidade</h2>
<p>A maioria das teorias chega a uma posição em dois níveis: a imparcialidade vale para as <em>regras</em>, e as regras permitem parcialidade.</p>
<ul>
<li><strong>Consequencialismo:</strong> um mundo em que cada um cuida dos seus é melhor do que um em que todos tentam cuidar de todos sem conhecer ninguém. Os deveres especiais são aprovados pela imparcialidade de segundo nível.</li>
<li><strong>Kant:</strong> a beneficência é um dever imperfeito, com latitude para escolher a quem; os deveres perfeitos (não mentir, não usar) valem para todos igualmente.</li>
<li><strong>Contratualismo:</strong> sob o véu, todos querem ser cuidados por alguém; logo, todos aceitam regras que permitem cuidar mais dos seus.</li>
<li><strong>Virtudes e cuidado:</strong> a parcialidade não é exceção, é o ponto de partida; o problema é expandi-la, não eliminá-la.</li>
</ul>
<h2>O limite</h2>
<p>A parcialidade legítima tem dois limites que a separam do <a href="tribalismo-moral.html">tribalismo</a>:</p>
<ol class="roteiro">
<li><strong>Ela permite dar mais; não permite tratar os outros como se não contassem.</strong> Cuidar mais do próprio filho não autoriza prejudicar o filho dos outros, nem ignorar uma criança que se afoga porque não é sua.</li>
<li><strong>Ela se baseia em relações, não em traços.</strong> Preferir quem você conhece é parcialidade; preferir quem tem sua cor, sua nação ou sua espécie é discriminação. A diferença: a relação é algo que existe entre vocês; o traço é algo que a pessoa é.</li>
</ol>
<p>A nacionalidade fica na fronteira: há instituições compartilhadas (relação), mas também um traço de nascimento. A maioria dos filósofos aceita alguma prioridade aos compatriotas por razões institucionais, e rejeita que a vida de um estrangeiro valha menos. Veja o <a href="debates/imigracao.html">debate sobre fronteiras</a>.</p>
<h2>Quanto a mais?</h2>
<p>Não há fórmula, mas há um teste: a prioridade aos seus deve ser a que você aceitaria que todos dessem aos seus. Um pai que gasta em aula de piano enquanto outras crianças passam fome está dentro do que todos aceitam; um pai que suborna um juiz pelo filho, não. O teste de <a href="imparcialidade.html">universalidade</a> decide.</p>
<div class="nota"><strong>Para guardar:</strong> a imparcialidade não pede que você ame todos igualmente. Pede que as regras que permitem amar mais os seus sejam as mesmas para todos, e que o seu amor não custe aos outros o que você não aceitaria que custasse aos seus.</div>
''', fontes=[('Impartiality (Stanford Encyclopedia)', SEP + 'impartiality/'), ('Special Obligations (Stanford Encyclopedia)', SEP + 'special-obligations/'), ('Persons, Character and Morality', 'https://www.google.com/search?tbm=bks&q=Bernard+Williams+Moral+Luck+Persons+Character+and+Morality')]),
]

NOVAS3_INTERMEDIARIO = [
dict(slug='teorias-do-bem-estar', grupo='Consequencialismo por dentro', titulo='O que torna uma vida boa? As teorias do bem-estar', resumo='Prazer, desejos satisfeitos ou uma lista de bens: três respostas sobre o que é bom para quem vive a vida, e por que a escolha muda tudo.', corpo='''
<p class="abre">Bem-estar é o que torna uma vida boa <em>para quem a vive</em>. Toda teoria ética precisa de uma resposta, não só o utilitarismo: deontologistas decidem o que é beneficência, éticos das virtudes o que é florescer, e quem defende animais precisa dizer o que é uma vida boa para um porco. Há três famílias de resposta.</p>
<h2>Hedonismo</h2>
<p>Bem-estar é prazer e ausência de dor, no sentido amplo: toda experiência que se sente como boa ou ruim. Bentham o adotou; Mill o refinou com prazeres superiores e inferiores; hoje o defendem Roger Crisp e, desde 2014, Peter Singer. A força: é o que todos sentem diretamente, e é o que faz a dor de um animal contar. A fraqueza: a <a href="dilemas/maquina-de-experiencias.html">máquina de experiências</a>. Se só a experiência conta, uma vida de ilusões felizes é tão boa quanto uma vida real, e a maioria recusa isso.</p>
<h2>Teorias do desejo</h2>
<p>Bem-estar é a satisfação das preferências da pessoa, aconteça ou não que ela a sinta. Escapa da máquina: quem prefere a realidade tem essa preferência frustrada na ilusão. É a base do <a href="teorias/utilitarismo-de-preferencias.html">utilitarismo de preferências</a> e da economia do bem-estar. As dificuldades: desejos mal informados (querer o que faria mal), desejos adaptados (quem nunca teve escolha deseja pouco), desejos sobre coisas distantes (que o Brasil ganhe a Copa depois da minha morte: isso me beneficia?). As versões sofisticadas contam só desejos <em>informados</em> e <em>sobre a própria vida</em>, o que as aproxima da terceira família.</p>
<h2>Lista objetiva</h2>
<p>Há bens que tornam uma vida melhor mesmo que a pessoa não os deseje nem os sinta: saúde, conhecimento, amizade, realização, autonomia, prazer. Aristóteles é o ancestral; Parfit, Finnis e Martha Nussbaum (com as capacidades) são versões modernas. A força: explica por que uma vida de conquistas reais é melhor do que uma de ilusões, e por que a educação beneficia quem não a quer. A fraqueza: quem faz a lista, e com que autoridade? E uma vida cheia de “bens” que a pessoa detesta é boa para ela?</p>
<table><thead><tr><th>Teoria</th><th>O que é bom para você</th><th>Acerta em</th><th>Falha em</th></tr></thead><tbody>
<tr><td>Hedonismo</td><td>Sentir-se bem</td><td>Dor e prazer são o que mais importa a quem sente</td><td>Máquina de experiências; vidas enganadas</td></tr>
<tr><td>Desejo</td><td>Conseguir o que quer</td><td>Respeita a autonomia; escapa da máquina</td><td>Desejos ruins, adaptados ou distantes</td></tr>
<tr><td>Lista objetiva</td><td>Ter os bens que fazem uma vida boa</td><td>Explica vidas boas sem ilusão e o valor da educação</td><td>Paternalismo; quem faz a lista</td></tr>
</tbody></table>
<h2>Por que a escolha muda tudo</h2>
<ul>
<li><strong>Animais:</strong> para o hedonismo, a vida de um animal conta pelo que ele sente, e isso basta para a ética animal inteira. Para teorias de lista, a pergunta é o que é florescer para cada espécie (Nussbaum).</li>
<li><strong>Morte:</strong> para o hedonismo, a morte é ruim pelo prazer perdido; para o desejo, pelos projetos frustrados; para a lista, pelos bens que não virão. Isso decide o peso de matar um ser sem projetos.</li>
<li><strong>Paternalismo:</strong> listas objetivas justificam mais intervenção; teorias do desejo, menos. Veja o <a href="debates/paternalismo.html">debate</a>.</li>
<li><strong>Ética populacional:</strong> criar uma vida “boa” depende do que “boa” quer dizer.</li>
<li><strong>Política:</strong> renda, satisfação declarada ou capacidades? O IDH escolheu a terceira.</li>
</ul>
<h2>Uma posição híbrida</h2>
<p>Muitos filósofos hoje combinam: o bem-estar exige uma experiência positiva <em>e</em> que ela se refira a algo real e valioso (Robert Adams, Wayne Sumner). Nem a ilusão feliz nem a conquista sem alegria são vidas plenamente boas. É menos elegante do que cada teoria pura, e mais parecido com o que as pessoas pensam.</p>
<div class="nota"><strong>Para guardar:</strong> antes de perguntar como aumentar o bem-estar de alguém, pergunte o que ele é. As três respostas discordam o suficiente para mudar a resposta prática.</div>
''', fontes=[('Well-Being (Stanford Encyclopedia)', SEP + 'well-being/'), ('Theories of Well-Being (Utilitarianism.net)', 'https://utilitarianism.net/theories-of-wellbeing/'), ('Uma introdução às teorias do bem-estar (Senciência e Ética)', 'https://senciencia.org/2024/06/18/uma-introducao-as-teorias-do-bem-estar'), ('Reasons and Persons, apêndice I', 'https://www.google.com/search?tbm=bks&q=Parfit+Reasons+and+Persons')]),

dict(slug='emocoes-morais', grupo='Mente e moral', titulo='Emoções morais: culpa, vergonha, indignação, nojo e perdão', resumo='Emoções não são o oposto da razão moral: são parte de como percebemos o que importa. Mas cada uma tem um uso bom e um uso ruim.', corpo='''
<p class="abre">Sentimos culpa ao ferir alguém, indignação diante da injustiça, nojo diante de certas práticas. Essas emoções chegam antes do argumento e muitas vezes o guiam. A questão não é se devemos tê-las, e sim quais são guias confiáveis, e para quê.</p>
<h2>O que as emoções fazem</h2>
<p>Para a tradição racionalista, de Platão a Kant, as emoções são perturbações que a razão deve controlar. Para Hume e Adam Smith, são a base da moral: sem simpatia, nenhum argumento moveria ninguém. A psicologia atual fica com Hume na descrição (julgamos primeiro por emoção) e com Kant na prescrição (a emoção precisa de exame). Martha Nussbaum resume: emoções são juízos sobre o que importa, e por isso podem ser corretas ou incorretas.</p>
<h2>Cada emoção, seu uso</h2>
<table><thead><tr><th>Emoção</th><th>O que sinaliza</th><th>Quando guia bem</th><th>Quando engana</th></tr></thead><tbody>
<tr><td>Culpa</td><td>Eu fiz algo errado a alguém</td><td>Leva a reparar e a não repetir</td><td>Culpa por coisas que não dependeram de você, ou culpa que paralisa em vez de reparar</td></tr>
<tr><td>Vergonha</td><td>Eu sou inadequado aos olhos dos outros</td><td>Mantém normas de honra que às vezes são boas (Appiah)</td><td>Depende do que o grupo aprova; já sustentou duelos e crimes de honra</td></tr>
<tr><td>Indignação</td><td>Alguém foi tratado injustamente</td><td>Motiva a corrigir injustiças que a calma toleraria</td><td>Indignação seletiva pelo próprio grupo; linchamento</td></tr>
<tr><td>Empatia</td><td>Sinto o que o outro sente</td><td>Faz o sofrimento alheio ser real para nós</td><td>É parcial: sente mais por quem é próximo, bonito e parecido; ignora números (Bloom)</td></tr>
<tr><td>Compaixão</td><td>Quero que o sofrimento do outro cesse</td><td>Motiva a ajudar sem exigir sentir a mesma dor</td><td>Pode ser condescendente, ou esgotar-se</td></tr>
<tr><td>Nojo</td><td>Isso é impuro ou contaminante</td><td>Evitar doença e veneno</td><td>Como guia moral, quase sempre erra: já condenou grupos inteiros sem vítima</td></tr>
<tr><td>Ressentimento e vingança</td><td>Fui prejudicado e quero retribuir</td><td>Base psicológica da justiça retributiva</td><td>Escala, não termina, e pune além do merecido</td></tr>
<tr><td>Gratidão</td><td>Recebi um bem que não era devido</td><td>Sustenta reciprocidade e laços</td><td>Pode virar dívida usada para controlar</td></tr>
</tbody></table>
<h2>Culpa e vergonha não são a mesma coisa</h2>
<p>A culpa olha para o ato (“fiz algo ruim”); a vergonha olha para o eu (“sou ruim”). A culpa tende a reparar; a vergonha, a esconder ou atacar. Culturas e famílias diferem em qual cultivam. Para a ética, a culpa é a mais útil, porque aponta para o que fazer, e a vergonha é a mais perigosa, porque depende de quem está olhando.</p>
<h2>O caso da empatia</h2>
<p>Paul Bloom argumentou, em <em>Contra a Empatia</em>, que sentir a dor do outro é um guia ruim para decidir: é parcial, se esgota, ignora a escala e pode ser manipulada (uma criança com nome mobiliza mais do que mil sem rosto). O que ele propõe no lugar é a compaixão racional: querer que o sofrimento cesse, sem precisar senti-lo, e usar a razão para decidir onde agir. Críticos respondem que sem empatia a compaixão não começa. Os dois têm razão em partes: a empatia abre a porta; a razão decide o que fazer depois de entrar. Veja <a href="vieses-morais.html">vieses morais</a>.</p>
<h2>Perdão</h2>
<p>Perdoar é abandonar o ressentimento contra quem nos feriu, sem necessariamente esquecer ou reconciliar. Filósofos discutem se o perdão exige arrependimento do outro (para muitos, sim, ou vira cumplicidade) e se pode ser um dever (para a maioria, não: é supererrogatório, e exigi-lo da vítima é uma segunda violência). O que o perdão faz pelo ofendido é libertá-lo de um ciclo; o que faz pela comunidade é permitir que a vida continue. Justiça restaurativa é a tentativa de institucionalizar isso.</p>
<h2>O que fazer com as emoções</h2>
<ol class="roteiro">
<li><strong>Ouça:</strong> uma emoção moral é um dado. Ela diz que algo lhe pareceu importante.</li>
<li><strong>Pergunte o que ela diz:</strong> há uma vítima? Há um erro meu? Ou é só repulsa, ou lealdade ao grupo?</li>
<li><strong>Corrija a parcialidade:</strong> sentiria o mesmo se a pessoa fosse do outro lado?</li>
<li><strong>Use a culpa para reparar, não para se punir.</strong> A culpa que não vira ação é só sofrimento a mais.</li>
<li><strong>Cultive as que ajudam:</strong> compaixão e indignação proporcional se treinam, como virtudes.</li>
</ol>
<div class="nota"><strong>Para guardar:</strong> as emoções morais são o radar; a razão é o piloto. Um radar sem piloto bate; um piloto sem radar não vê nada.</div>
''', fontes=[('Moral Emotions (Stanford Encyclopedia: Emotion)', SEP + 'emotion/'), ('Contra a Empatia', 'https://www.google.com/search?tbm=bks&q=Paul+Bloom+Contra+a+Empatia'), ('Forgiveness (Stanford Encyclopedia)', SEP + 'forgiveness/'), ('Upheavals of Thought', 'https://www.google.com/search?tbm=bks&q=Nussbaum+Upheavals+of+Thought')]),

dict(slug='situacionismo-e-experimentos', grupo='Mente e moral', titulo='Milgram, Zimbardo, Arendt: pessoas comuns fazem o mal?', resumo='Os experimentos que mostraram quanto a situação pesa sobre o caráter, a banalidade do mal e a objeção situacionista à ética das virtudes.', corpo='''
<p class="abre">Depois do Holocausto, a pergunta era inevitável: as pessoas que participaram eram monstros, ou pessoas comuns em situações extraordinárias? A psicologia social dos anos 1960 e 1970 deu uma resposta desconfortável, e a filosofia ainda discute o que ela significa.</p>
<h2>Milgram: obediência</h2>
<p>Em 1961, Stanley Milgram pediu a voluntários que aplicassem choques, supostamente crescentes, a outro participante (um ator) sempre que ele errasse em um teste. Um pesquisador de jaleco dizia “o experimento exige que continue”. Cerca de dois terços foram até o choque máximo, apesar de gritos e depois silêncio. Não eram sádicos: suavam, protestavam, e continuavam. A conclusão de Milgram: a obediência a uma autoridade percebida como legítima leva pessoas comuns a atos que condenariam. Variações mostraram o que reduz a obediência: proximidade da vítima, ausência da autoridade, um colega que se recusa.</p>
<h2>Zimbardo: papéis</h2>
<p>Em 1971, Philip Zimbardo dividiu estudantes em “guardas” e “prisioneiros” em uma prisão simulada. Em dias, guardas humilhavam prisioneiros, e o experimento foi interrompido. A leitura clássica: o papel molda a conduta. Críticas posteriores mostraram que Zimbardo orientou os guardas e que parte do comportamento foi encenação, o que enfraquece o estudo, mas não a conclusão geral, confirmada por outros.</p>
<h2>Arendt: a banalidade do mal</h2>
<p>Hannah Arendt cobriu o julgamento de Adolf Eichmann, organizador da logística do extermínio, e viu não um monstro, mas um burocrata sem imaginação, que cumpria ordens, usava clichês e nunca pensou no que fazia. Sua tese, a <strong>banalidade do mal</strong>, é que o mal em grande escala não precisa de maldade: precisa de pessoas que não pensam. Historiadores discutem se Eichmann era mesmo assim (há evidência de convicção ideológica), mas a tese sobreviveu como descrição de como sistemas de atrocidade funcionam: com muita gente fazendo a sua parte pequena.</p>
<h2>A objeção situacionista</h2>
<p>Nos anos 1990, Gilbert Harman e John Doris usaram esses estudos e outros (pessoas ajudam mais quando acabaram de achar uma moeda; menos quando estão com pressa) para atacar a ética das virtudes: se a conduta depende tanto da situação, traços de caráter estáveis como “coragem” ou “honestidade” talvez não existam, e uma ética baseada neles estaria fundada em uma ilusão.</p>
<p>As respostas dos defensores das virtudes:</p>
<ul>
<li>Os experimentos mostram que a virtude é <em>rara</em>, não que é impossível; Aristóteles já dizia que poucos a alcançam.</li>
<li>A virtude inclui saber reconhecer situações perigosas e evitá-las ou resistir a elas; os que se recusaram em Milgram existiram, e a pergunta é o que os distinguia.</li>
<li>Traços locais (honesto com amigos, não com estranhos) ainda são traços, e a educação pode ampliá-los.</li>
<li>O argumento prova demais: se não há caráter, também não há agentes para o consequencialismo nem para Kant.</li>
</ul>
<h2>Replicação e limites</h2>
<p>Parte da psicologia social dos anos 2000 não se replicou, e os estudos clássicos foram reexaminados. Milgram se sustenta em replicações parciais; Zimbardo, pouco; o efeito do humor e da pressa sobre a ajuda, moderadamente. A conclusão que resiste: a situação pesa muito mais do que supomos, e menos do que “tudo”. Veja <a href="probabilidade-e-etica.html">probabilidade e ética</a> sobre como pesar evidência.</p>
<h2>O que isso muda</h2>
<ol class="roteiro">
<li><strong>Humildade:</strong> “eu nunca faria isso” é o que todos os participantes diziam antes.</li>
<li><strong>Desenhar situações:</strong> se a situação pesa, instituições e regras que facilitam o certo valem mais do que sermões.</li>
<li><strong>O primeiro a recusar:</strong> em Milgram, um colega que se recusava derrubava a obediência. Dissentir em voz alta é o ato mais eficaz que uma pessoa comum tem.</li>
<li><strong>Pensar:</strong> a tese de Arendt tem um corolário prático: a defesa contra o mal banal é o hábito de perguntar o que se está fazendo, e para quem.</li>
</ol>
<div class="nota"><strong>Para guardar:</strong> pessoas comuns fazem o mal quando a situação o pede e ninguém pensa. Isso não absolve ninguém; muda onde a prevenção começa.</div>
''', fontes=[('Milgram experiment (Wikipédia)', WE + 'Milgram_experiment'), ('Eichmann em Jerusalém', WP + 'Eichmann_em_Jerusal%C3%A9m'), ('Moral Character (Stanford Encyclopedia)', SEP + 'moral-character/'), ('Lack of Character', 'https://www.google.com/search?tbm=bks&q=John+Doris+Lack+of+Character')]),

dict(slug='livre-arbitrio-e-responsabilidade', grupo='Mente e moral', titulo='Livre-arbítrio e responsabilidade moral', resumo='Se tudo o que você faz tem causas, você é responsável? Compatibilismo, os casos de Frankfurt e a sorte moral: o que sobra da culpa e do mérito.', corpo='''
<p class="abre">Toda a moral pressupõe que as pessoas respondem pelo que fazem. Mas o que uma pessoa faz tem causas: genes, infância, cérebro, circunstâncias. Se as causas vêm de antes dela, em que sentido a escolha é dela? É o problema do livre-arbítrio, e ele decide o que sobra de culpa, mérito e punição.</p>
<h2>O problema</h2>
<p>Determinismo é a tese de que cada evento, inclusive cada decisão, é fixado pelo que veio antes mais as leis da natureza. Se for verdade, você não poderia ter feito diferente. E se não for verdade, se há acaso nas decisões, o acaso também não é seu. Dos dois lados, parece que a escolha não é “sua” no sentido forte. As posições:</p>
<table><thead><tr><th>Posição</th><th>O que diz</th><th>Defensores</th></tr></thead><tbody>
<tr><td>Libertarismo (metafísico)</td><td>Temos uma liberdade que escapa ao determinismo; somos causas primeiras das nossas escolhas</td><td>Kant, em parte; Robert Kane; tradição religiosa</td></tr>
<tr><td>Determinismo duro</td><td>O determinismo é verdadeiro e incompatível com a responsabilidade; culpa e mérito são ilusões</td><td>Derk Pereboom, Galen Strawson, Sam Harris</td></tr>
<tr><td>Compatibilismo</td><td>Liberdade é agir pelas próprias razões, sem coerção; isso é compatível com causas. É o que a responsabilidade sempre exigiu</td><td>Hume, Frankfurt, Dennett, a maioria dos filósofos hoje</td></tr>
</tbody></table>
<h2>Os casos de Frankfurt</h2>
<p>Harry Frankfurt, em 1969, atacou a ideia de que responsabilidade exige poder ter feito diferente. Imagine que um cientista implantou em Jones um dispositivo que o forçaria a votar em A se ele fosse votar em B; mas Jones vota em A por conta própria, e o dispositivo nunca age. Jones não poderia ter feito diferente, e ainda assim é responsável: votou pelas próprias razões. A responsabilidade, conclui Frankfurt, depende de a ação vir da pessoa, não de haver alternativas. Veja <a href="dilemas/casos-de-frankfurt.html">o caso</a>.</p>
<p>Frankfurt acrescentou a ideia de <strong>desejos de segunda ordem</strong>: o viciado que quer não querer a droga é livre de um modo diferente do que a quer sem conflito. Ser pessoa é poder avaliar os próprios desejos. Isso liga o livre-arbítrio à <a href="fraqueza-de-vontade.html">fraqueza de vontade</a>.</p>
<h2>A sorte moral</h2>
<p>Dois motoristas dirigem bêbados do mesmo jeito; um atropela uma criança que atravessou, o outro chega em casa. Julgamos o primeiro muito mais, e a lei também. Mas a única diferença foi a sorte. Thomas Nagel e Bernard Williams chamaram isso de <strong>sorte moral</strong>: julgamos pessoas por resultados, circunstâncias e até pelo caráter que não escolheram. Se a responsabilidade exige controle, quase nada do que julgamos está sob controle. Veja <a href="dilemas/gauguin.html">o Gauguin de Williams</a>.</p>
<h2>O que a ciência acrescenta</h2>
<p>Os experimentos de Libet (anos 1980) mostraram atividade cerebral antes da consciência da decisão, e foram lidos como prova de que a consciência não decide. Reanálises mostram que a atividade é ruído preparatório, e que a leitura foi apressada. O que a neurociência estabelece é mais modesto e mais importante: trauma, pobreza, lesões e doenças reduzem a capacidade de escolher, em graus. A responsabilidade é uma escala, não um interruptor.</p>
<h2>O que fica para a ética</h2>
<ul>
<li><strong>Responsabilidade sem metafísica:</strong> para Peter Strawson, culpar e agradecer são atitudes que tomamos uns com os outros como pessoas, e nenhuma descoberta sobre causas nos fará abandoná-las; o que muda é a quem e quanto.</li>
<li><strong>Punição:</strong> se o merecimento no sentido forte é duvidoso, a justificativa da pena pende para a prevenção e a proteção, e a crueldade perde a desculpa. Veja o <a href="debates/punicao.html">debate</a>.</li>
<li><strong>Mérito:</strong> se o talento e a disposição ao esforço têm causas não escolhidas, o merecimento forte da riqueza enfraquece. É o argumento de Rawls. Veja <a href="debates/meritocracia.html">meritocracia</a>.</li>
<li><strong>Compaixão:</strong> ver as causas por trás de quem erra não anula o erro; muda o tom com que se responde a ele.</li>
<li><strong>Agência:</strong> nada disso dispensa de decidir. Mesmo o determinista duro escolhe o que fazer a seguir, e o que ele acredita sobre a liberdade faz parte das causas.</li>
</ul>
<div class="nota"><strong>Para guardar:</strong> a maioria dos filósofos conclui que responsabilidade exige agir pelas próprias razões, não escapar da causalidade. Isso preserva a culpa e o mérito em versão modesta, e tira deles a dureza que vinha da ideia de que cada um é a causa primeira de si mesmo.</div>
''', fontes=[('Free Will (Stanford Encyclopedia)', SEP + 'freewill/'), ('Moral Responsibility (Stanford Encyclopedia)', SEP + 'moral-responsibility/'), ('Moral Luck (Stanford Encyclopedia)', SEP + 'moral-luck/'), ('P. F. Strawson, Freedom and Resentment (Wikipédia)', WE + 'P._F._Strawson')]),
]

NOVAS3_AVANCADO = [
dict(slug='epistemologia-moral', grupo='Metaética', titulo='Epistemologia moral: desacordo, testemunho e ficção', resumo='Como sabemos o que é certo? E o que fazer quando alguém tão informado quanto você discorda, ou quando a resposta vem de outra pessoa?', corpo='''
<p class="abre">A epistemologia moral pergunta como conhecemos verdades morais, se as há. O site já tratou do intuicionismo e do equilíbrio reflexivo. Esta lição cobre três problemas mais difíceis: o desacordo entre pessoas igualmente competentes, o conhecimento moral que vem dos outros, e a proposta de manter a moral como ficção útil.</p>
<h2>O desacordo entre pares</h2>
<p>Dois filósofos, igualmente informados e inteligentes, leem os mesmos argumentos e discordam sobre a eutanásia. O que cada um deve fazer com a sua crença? A epistemologia geral discute isso como <strong>desacordo entre pares</strong>. Duas respostas:</p>
<ul>
<li><strong>Conciliar:</strong> o desacordo de um par é evidência de que você pode estar errado; reduza a confiança. Levado ao extremo, ninguém teria crenças morais firmes, porque sempre há um par que discorda.</li>
<li><strong>Manter:</strong> se você avaliou bem os argumentos, o desacordo não é razão para mudar; o outro é que errou. Levado ao extremo, ninguém aprenderia com ninguém.</li>
</ul>
<p>A posição intermediária é a mais defendida: o desacordo deve reduzir a confiança em proporção à competência do outro e à dificuldade da questão, e deve motivar a procurar <em>por que</em> discordam. Em ética, muita divergência vem de fatos não morais e de quem conta, e esses pontos podem ser investigados. O que fica depois disso é o desacordo real, que pede humildade sem paralisia. Veja <a href="abertura-moral.html">abertura moral</a>.</p>
<h2>O testemunho moral</h2>
<p>Aceitamos que a Terra é redonda porque alguém confiável disse. Podemos aceitar que a eutanásia é errada porque alguém confiável disse? Muitos filósofos sentem que há algo estranho em crer moralmente “por testemunho”: parece que a pessoa precisa <em>ver</em> a razão, não só adotar a conclusão. As explicações: a compreensão moral tem valor em si (Alison Hills); a crença por testemunho não gera a motivação e a sensibilidade que a crença própria gera; e quem crê por testemunho não sabe aplicar a regra a casos novos. A resposta contrária: para quem não tem tempo ou competência, confiar em quem estudou é o mais racional, como em qualquer área. A posição moderada: o testemunho é uma boa razão para <em>investigar</em>, e pode ser a melhor razão disponível para agir enquanto não se investigou.</p>
<h2>A ficção útil</h2>
<p>Se a <a href="teorias/teoria-do-erro.html">teoria do erro</a> estiver certa e nenhum juízo moral for verdadeiro, o que fazer com a moral? Richard Joyce propõe o <strong>ficcionalismo</strong>: manter a prática moral como mantemos uma ficção que conhecemos, porque ela funciona. Dizemos “isso é errado” sabendo que não descreve um fato, do mesmo modo que um ator chora em cena. A vantagem: preserva o que a moral faz (coordenar, motivar, conter o interesse próprio) sem crer no que não existe. As objeções: uma ficção que todos sabem ser ficção perde força; e, se a moral funciona tão bem como ficção, talvez isso seja evidência de que não é ficção. Richard Garner propõe o oposto, o abolicionismo: abandonar a linguagem moral e falar só de interesses e consequências.</p>
<h2>Como conhecemos, afinal</h2>
<table><thead><tr><th>Fonte</th><th>O que oferece</th><th>Limite</th></tr></thead><tbody>
<tr><td>Intuições</td><td>Dados de partida: o que parece certo ao refletir</td><td>Vêm da evolução e da cultura; precisam de filtro</td></tr>
<tr><td>Argumentos</td><td>Coerência entre juízos; ver que um compromisso implica outro</td><td>Dependem das premissas</td></tr>
<tr><td>Casos e experimentos mentais</td><td>Isolam o que pesa</td><td>Podem ser desenhados para a resposta desejada</td></tr>
<tr><td>Fatos</td><td>Quem sofre, o que funciona</td><td>Não decidem valores, mas mudam conclusões</td></tr>
<tr><td>Testemunho</td><td>O que quem estudou concluiu</td><td>Não substitui a compreensão</td></tr>
<tr><td>Experiência e convivência</td><td>Conhecer quem é afetado</td><td>Parcial; precisa ser ampliada</td></tr>
</tbody></table>
<div class="nota"><strong>Para guardar:</strong> conhecer o certo não é consultar uma fonte, e sim fazer muitas fontes conversarem até que se sustentem. O desacordo não prova que não há resposta; prova que ela é difícil, e que ninguém a tem sozinho.</div>
''', fontes=[('Moral Epistemology (Stanford Encyclopedia)', SEP + 'moral-epistemology/'), ('Disagreement (Stanford Encyclopedia)', SEP + 'disagreement/'), ('Moral Testimony (Stanford Encyclopedia: Moral Epistemology)', SEP + 'moral-epistemology/#MorTes'), ('The Myth of Morality', 'https://www.google.com/search?tbm=bks&q=Richard+Joyce+The+Myth+of+Morality')]),

dict(slug='pluralismo-de-valores', grupo='Decidir sem certeza', titulo='Pluralismo de valores: quando os bens não se somam', resumo='Liberdade, igualdade, lealdade, beleza, verdade: há uma moeda comum que converta um no outro? Berlin e Nagel dizem que não, e isso muda como se decide.', corpo='''
<p class="abre">O utilitarismo tem uma moeda única: o bem-estar. Kant tem um princípio único: a dignidade. O pluralismo de valores diz que há vários bens irredutíveis, que não se convertem uns nos outros, e que por isso alguns conflitos não têm solução certa, só escolhas com perda. A ideia é antiga, mas foi Isaiah Berlin quem a colocou no centro.</p>
<h2>A tese</h2>
<p>Para Berlin, liberdade e igualdade, justiça e misericórdia, lealdade e verdade são valores genuínos, e nenhum sistema os realiza todos: mais de um custa menos de outro. Não há uma régua que diga quanto de liberdade vale uma unidade de igualdade. Thomas Nagel listou cinco fontes de valor em conflito: obrigações específicas, direitos gerais, utilidade, perfeição (excelência, beleza, conhecimento) e projetos pessoais. Nenhuma se reduz às outras.</p>
<h2>Incomensurabilidade</h2>
<p>Dois valores são <strong>incomensuráveis</strong> quando não há escala comum que os compare, e <strong>incomparáveis</strong> quando não se pode dizer nem que um é melhor, nem que o outro é, nem que são iguais. Ruth Chang propôs uma quarta relação: “no mesmo patamar”, em que são comparáveis sem que um vença, e a escolha é legítima para qualquer lado. Isso explica por que escolher uma carreira ou uma causa não é como escolher o preço mais baixo, sem que seja arbitrário.</p>
<h2>O que o pluralismo faz com as teorias</h2>
<table><thead><tr><th>Teoria</th><th>Resposta ao pluralismo</th></tr></thead><tbody>
<tr><td>Utilitarismo</td><td>Nega: tudo o que vale, vale pelo bem-estar que produz. Mill admitiu prazeres de qualidades diferentes, o que já é um passo para o pluralismo.</td></tr>
<tr><td>Kant</td><td>Nega na base (a dignidade é única), mas admite conflitos de deveres sem solução clara.</td></tr>
<tr><td>Ross</td><td>Aceita: deveres prima facie plurais, pesados por juízo.</td></tr>
<tr><td>Virtudes</td><td>Aceita: a sabedoria prática é justamente a capacidade de decidir entre bens sem fórmula.</td></tr>
<tr><td>Contratualismo</td><td>Aceita em parte: o procedimento substitui a régua, e o que as partes aceitam não precisa de moeda comum.</td></tr>
</tbody></table>
<h2>Dilemas trágicos e resíduo moral</h2>
<p>Se os valores não se somam, há dilemas genuínos: situações em que qualquer escolha viola algo que importa. Bernard Williams chamou de <strong>resíduo moral</strong> o que sobra depois da escolha certa: o arrependimento de quem desviou o bonde, a dívida com quem perdeu. Para o utilitarismo, o resíduo é irracional (você fez o melhor); para o pluralista, é a percepção correta de que algo de valor foi perdido. Veja <a href="dilemas/escolha-de-sofia.html">a escolha de Sofia</a>.</p>
<h2>Pluralismo não é relativismo</h2>
<p>Berlin insistiu: dizer que há vários valores verdadeiros não é dizer que qualquer coisa vale. Os valores são objetivos e limitados em número; o que não existe é uma ordem fixa entre eles. Um pluralista pode condenar a crueldade sem hesitar, e ainda assim não saber se uma sociedade deve preferir mais liberdade ou mais igualdade.</p>
<h2>O que fazer com isso</h2>
<ol class="roteiro">
<li><strong>Nomeie os valores em conflito</strong> antes de decidir. Muita briga é entre pessoas que pesam bens diferentes sem saber.</li>
<li><strong>Não force a conversão:</strong> quando não há moeda comum, dizer que “a liberdade vale 3 e a igualdade 2” é fingir precisão.</li>
<li><strong>Aceite a perda:</strong> escolher bem não elimina o custo; reconhecê-lo é parte de escolher bem.</li>
<li><strong>Desconfie das soluções totais:</strong> sistemas que prometem realizar todos os valores de uma vez costumam sacrificar alguns sem dizer.</li>
<li><strong>Use os limites:</strong> o pluralismo convive com proibições firmes (não torturar); a incerteza é sobre o resto.</li>
</ol>
<div class="nota"><strong>Para guardar:</strong> talvez não exista uma fórmula que converta todos os bens em um só. Isso não é um defeito da ética: é o que torna necessário o juízo, e o que explica por que escolher bem às vezes dói.</div>
''', fontes=[('Value Pluralism (Stanford Encyclopedia)', SEP + 'value-pluralism/'), ('Incommensurable Values (Stanford Encyclopedia)', SEP + 'value-incommensurable/'), ('Dois Conceitos de Liberdade', WE + 'Two_Concepts_of_Liberty'), ('Mortal Questions', 'https://www.google.com/search?tbm=bks&q=Nagel+Mortal+Questions')]),
]

META_NOVAS3 = {
 'historia-da-etica': (['fundamentos'], ('Qual era a pergunta central da ética antiga?', ['Que regra seguir?', 'Que vida vale a pena viver?', 'O que significa “bom”?'], 1, 'A resposta passava pelo caráter; regras e consequências vieram depois.')),
 'parcialidade-e-deveres-especiais': (['circulo', 'fundamentos'], ('O que separa a parcialidade legítima do tribalismo?', ['Nada', 'Ela se baseia em relações, não em traços, e não trata os outros como se não contassem', 'A parcialidade legítima é só com a família'], 1, 'Preferir quem você conhece é parcialidade; preferir quem tem sua cor, nação ou espécie é discriminação.')),
 'teorias-do-bem-estar': (['consequencias', 'fundamentos'], ('A máquina de experiências é uma objeção a qual teoria do bem-estar?', ['Lista objetiva', 'Desejo', 'Hedonismo'], 2, 'Se só a experiência conta, uma vida de ilusões felizes seria tão boa quanto uma real.')),
 'emocoes-morais': (['mente'], ('Qual é a diferença entre culpa e vergonha?', ['São a mesma coisa', 'A culpa olha para o ato e tende a reparar; a vergonha olha para o eu e tende a esconder', 'A vergonha é sempre melhor'], 1, 'Por isso a culpa é mais útil à ética, e a vergonha depende de quem está olhando.')),
 'situacionismo-e-experimentos': (['mente', 'carater'], ('A objeção situacionista à ética das virtudes diz que…', ['As virtudes são fáceis', 'A conduta depende tanto da situação que traços estáveis talvez não existam', 'Só os maus obedecem'], 1, 'Defensores respondem que os experimentos mostram que a virtude é rara, não impossível.')),
 'livre-arbitrio-e-responsabilidade': (['mente', 'fundamentos'], ('Os casos de Frankfurt mostram que a responsabilidade…', ['Exige poder ter feito diferente', 'Não exige alternativas: basta que a ação venha das próprias razões', 'Não existe'], 1, 'Jones não poderia ter votado diferente, e ainda assim é responsável, porque votou por conta própria.')),
 'epistemologia-moral': (['metaetica'], ('O ficcionalismo de Joyce propõe…', ['Abandonar a moral', 'Manter a prática moral como ficção útil, sem crer em fatos morais', 'Que a moral é verdadeira'], 1, 'Como um ator que chora em cena: a prática funciona sem a crença.')),
 'pluralismo-de-valores': (['futuro', 'fundamentos'], ('Para Berlin, pluralismo de valores é diferente de relativismo porque…', ['Não há diferença', 'Os valores são objetivos e limitados; o que não existe é uma ordem fixa entre eles', 'O pluralismo nega que haja valores'], 1, 'Um pluralista condena a crueldade sem hesitar, e pode não saber se prefere mais liberdade ou mais igualdade.')),
}
REFORCO_NOVAS3 = {
 'historia-da-etica': dict(analogia='Pense em um rio com vários afluentes: Grécia, Índia e China nascem separados, se juntam e se separam de novo. Olhar o mapa do rio não substitui beber a água, mas evita confundir a nascente com a foz.', crianca='Há muito tempo, pessoas em lugares diferentes do mundo começaram a perguntar “o que é ser bom?”. Cada época deu uma resposta um pouco diferente, e as respostas de hoje são filhas das antigas. Saber a história ajuda a entender de onde cada ideia veio.'),
 'parcialidade-e-deveres-especiais': dict(analogia='Em um hospital, cada médico cuida dos seus pacientes, não de todos os do mundo. Isso é parcialidade, e é bom: o sistema funciona assim. Mas nenhum médico pode prejudicar o paciente do colega para favorecer o seu. A parcialidade legítima é a do médico; o tribalismo seria a de quem sabota a outra ala.', crianca='É normal cuidar mais dos seus amigos e da sua família. O que não pode é ser mau com os outros por causa disso, nem fingir que eles não existem. Cuidar mais dos seus e cuidar bem de todos são coisas que cabem juntas.'),
 'teorias-do-bem-estar': dict(analogia='Três formas de avaliar uma viagem: pelo quanto você se divertiu (hedonismo), pelo quanto ela foi como você queria (desejo), ou pelo que você de fato conheceu e aprendeu, mesmo que tenha chovido (lista objetiva). As três podem dar notas diferentes para a mesma viagem.', crianca='O que faz uma vida ser boa? Sentir coisas boas? Conseguir o que você quer? Ou ter coisas que são boas mesmo que você não perceba, como aprender e ter amigos? Os filósofos têm as três respostas, e cada uma muda o que a gente faz pelos outros.'),
 'emocoes-morais': dict(analogia='As emoções morais são como os sensores de um carro: o alarme de porta aberta, a luz do óleo, o aviso de cinto. Cada um avisa uma coisa, e alguns disparam à toa. Dirigir ignorando todos é perigoso; parar o carro a cada apito, também. O motorista decide o que fazer com cada aviso.', crianca='Quando você faz algo errado, sente culpa. Quando vê uma injustiça, sente raiva. Esses sentimentos avisam que algo importa. Mas às vezes eles se enganam, como quando a gente sente nojo de uma comida só porque é diferente. Por isso vale sentir e depois pensar.'),
 'situacionismo-e-experimentos': dict(analogia='Uma ponte firme aguenta vento forte; uma ponte fraca cai com brisa. Os experimentos de Milgram e Zimbardo mediram o vento, e descobriram que quase todas as pontes caem com vento suficiente. Isso não diz que firmeza não existe: diz que ela é rara e que vale construir onde venta menos.', crianca='Em um experimento famoso, pessoas comuns deram choques em outras porque um cientista mandou. Elas não eram más; só não paravam para pensar. Isso ensina que, quando todo mundo está fazendo algo errado, a pessoa que diz “não” é muito importante, e que vale perguntar o que a gente está fazendo.'),
 'livre-arbitrio-e-responsabilidade': dict(analogia='Um rio corre para o mar por causa do relevo, da chuva e da gravidade; ninguém diz que ele é “livre”. Uma pessoa também tem causas, mas, diferente do rio, pode olhar para os próprios desejos e perguntar se os quer. É essa capacidade, e não a ausência de causas, que o compatibilismo chama de liberdade.', crianca='Tudo o que você faz tem motivos: o que aprendeu, o que sentiu, o que viu. Isso quer dizer que você não escolhe? Não: escolher é justamente pensar nos seus motivos e decidir. Quem faz algo por decisão própria é responsável; quem foi forçado, não.'),
 'epistemologia-moral': dict(analogia='Dois médicos experientes discordam sobre um diagnóstico. Nenhum deve simplesmente ceder, nem simplesmente insistir: devem pedir mais exames e perguntar por que leem os dados de modo diferente. O desacordo moral entre pessoas competentes pede o mesmo: menos certeza, mais investigação.', crianca='Se um amigo tão esperto quanto você discorda de você, isso é um aviso: talvez você esteja errado, talvez ele. O certo não é brigar nem desistir; é perguntar por que cada um pensa assim. Às vezes vocês descobrem que estavam falando de coisas diferentes.'),
 'pluralismo-de-valores': dict(analogia='Comparar liberdade com igualdade pode ser como comparar uma música com um quadro: dá para dizer que ambos são ótimos, e que uma música ruim perde para um bom quadro, sem que exista uma régua que diga quantos quadros vale uma música. Escolher entre eles não é um erro de conta; é uma escolha com perda.', crianca='Às vezes você precisa escolher entre duas coisas boas, como brincar com um amigo ou ir ao aniversário de outro. Não existe uma conta que diga qual vale mais. Você escolhe uma, e é normal ficar um pouco triste pela outra. Isso não quer dizer que escolheu errado.'),
}
