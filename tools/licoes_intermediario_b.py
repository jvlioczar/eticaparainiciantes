"""Lições do nível Intermediário, parte 2: mente e moral, ética animal e dilemas clássicos."""
from licoes_iniciante import SEP, IEP, WP, WE, TESTE, MAPA, VINDING, SINGER_PE, RACHELS
LIBERTACAO = ('Libertação Animal', WP + 'Liberta%C3%A7%C3%A3o_Animal')
NY = ('Declaração de Nova York sobre Consciência Animal', 'https://sites.google.com/nyu.edu/nydeclaration/declaration')

INTERMEDIARIO_B = [
dict(slug='psicologia-moral', grupo='Mente e moral', titulo='Psicologia moral: intuição primeiro, razão depois', resumo='Haidt, Greene e a mente de dois sistemas: como julgamos de fato, e por que saber disso não diz como deveríamos julgar.', corpo='''
<p class="abre">A psicologia moral estuda como as pessoas de fato fazem juízos morais. As descobertas das últimas décadas incomodam todas as teorias: julgamos primeiro por intuição e só depois buscamos razões, e as intuições vêm de uma história evolutiva que não tinha a ética em mente.</p>
<h2>O elefante e o condutor</h2>
<p>Jonathan Haidt, em <em>A Mente Moralista</em>, usa a imagem de um elefante (a intuição, rápida e forte) e um condutor (a razão, lenta e fraca), que muitas vezes só justifica para onde o elefante já foi. Em experimentos, pessoas condenam atos sem vítima (como comer o próprio cachorro atropelado) e, quando não encontram uma razão, dizem “não sei, só é errado”. Ele chamou isso de <strong>perplexidade moral</strong>.</p>
<h2>Os fundamentos morais</h2>
<table><thead><tr><th>Fundamento</th><th>Pergunta intuitiva</th></tr></thead><tbody>
<tr><td>Cuidado / dano</td><td>Alguém está sofrendo?</td></tr><tr><td>Justiça / trapaça</td><td>Alguém está levando vantagem?</td></tr><tr><td>Lealdade / traição</td><td>Está com o nosso grupo?</td></tr><tr><td>Autoridade / subversão</td><td>Respeita a hierarquia?</td></tr><tr><td>Santidade / degradação</td><td>Isso é puro ou repugnante?</td></tr><tr><td>Liberdade / opressão</td><td>Alguém está sendo dominado?</td></tr>
</tbody></table>
<p>Pessoas e culturas pesam esses fundamentos de modos diferentes, o que explica parte das brigas morais: cada lado “vê” um erro que o outro não vê. Pesquisas posteriores questionam o tamanho dessas diferenças, então trate como tendência.</p>
<h2>Dois sistemas no bonde</h2>
<p>Joshua Greene colocou pessoas em scanners enquanto respondiam a dilemas. Desviar o bonde ativa áreas ligadas ao raciocínio; empurrar o homem da passarela ativa áreas emocionais, e a maioria recusa. A hipótese: temos uma resposta emocional automática contra causar dano direto e pessoal (um “alarme”), e um raciocínio mais lento que faz contas. Para Greene, as intuições deontológicas são o alarme, calibrado para um mundo de tribos pequenas, e o raciocínio consequencialista seria o modo manual, mais confiável em problemas novos. Deontologistas responderam que a origem de uma intuição não diz se ela está certa.</p>
<h2>O que isso muda, e o que não muda</h2>
<ul>
<li><strong>Muda a humildade:</strong> a sensação de certeza não é prova de acerto. Nosso “isso é óbvio” já aprovou a escravidão.</li>
<li><strong>Muda a estratégia:</strong> para convencer, fale com o elefante primeiro. Argumentos chegam depois do respeito.</li>
<li><strong>Não muda a pergunta normativa:</strong> saber <em>por que</em> sentimos nojo não diz se o nojo é um bom guia. Descrever não é aprovar. Veja <a href="fatos-e-valores.html">fatos e valores</a>.</li>
<li><strong>Cria o problema do desmascaramento:</strong> se nossas intuições vêm da evolução, podemos confiar nelas para descobrir a verdade moral? Veja <a href="evolucao-e-moral.html">evolução e moral</a>.</li>
</ul>
<h2>Um uso construtivo</h2>
<p>Peter Singer e outros propõem usar a psicologia como filtro: intuições que têm uma explicação evolutiva ou cultural clara, e que não sobrevivem ao exame (nojo por grupos diferentes, parcialidade pelo próximo), merecem menos peso. Intuições que resistem à reflexão (a dor é ruim, casos iguais pedem tratamento igual) merecem mais. A psicologia, assim, não substitui a ética: ajuda a limpar o terreno.</p>
<div class="nota"><strong>Para guardar:</strong> a mente moral veio pronta de fábrica para um mundo que não existe mais. Conhecê-la serve para vigiá-la, não para obedecê-la.</div>
''', fontes=[('A Mente Moralista', WE + 'The_Righteous_Mind'), ('Moral foundations theory (Wikipédia)', 'https://en.wikipedia.org/wiki/Moral_foundations_theory'), ('Moral Tribes', 'https://www.google.com/search?tbm=bks&q=Joshua+Greene+Moral+Tribes'), ('Moral Psychology: Empirical Approaches (Stanford Encyclopedia)', SEP + 'moral-psych-emp/')]),

dict(slug='vieses-morais', grupo='Mente e moral', titulo='Vieses que distorcem o julgamento moral', resumo='Uma vítima com nome vale mais do que mil sem nome; o que está perto pesa mais do que o que está longe. Conheça os atalhos que torcem a moral.', corpo='''
<p class="abre">Vieses cognitivos não distorcem só estimativas e decisões financeiras. Eles torcem o julgamento moral de formas previsíveis, e quase sempre na direção de dar menos peso a quem está longe, é muitos ou não se parece conosco.</p>
<h2>Os principais</h2>
<table><thead><tr><th>Viés</th><th>O que faz</th><th>Efeito moral</th></tr></thead><tbody>
<tr><td>Vítima identificável</td><td>Uma pessoa com nome e rosto comove mais do que estatísticas</td><td>Doamos para um caso e ignoramos milhões</td></tr>
<tr><td>Insensibilidade à escala</td><td>Salvar 2 mil ou 200 mil aves gera quase a mesma disposição a ajudar</td><td>O número de vítimas quase não entra na conta</td></tr>
<tr><td>Proximidade</td><td>O que está perto, no espaço e no tempo, pesa mais</td><td>A criança no lago comove; a criança distante, não</td></tr>
<tr><td>Omissão</td><td>Causar um dano parece pior do que deixar que ele aconteça</td><td>Toleramos mortes evitáveis que não causamos. Veja <a href="fazer-e-deixar-acontecer.html">fazer e deixar acontecer</a></td></tr>
<tr><td>Status quo</td><td>O que já existe parece justificado</td><td>Práticas antigas escapam ao exame</td></tr>
<tr><td>Favoritismo de grupo</td><td>Os “nossos” recebem benefício da dúvida</td><td>O mesmo ato é julgado pelo autor, não pelo conteúdo</td></tr>
<tr><td>Nojo como guia</td><td>Repulsa é lida como erro moral</td><td>Já condenou grupos inteiros sem vítima alguma</td></tr>
<tr><td>Raciocínio motivado</td><td>Buscamos razões para a conclusão que já queremos</td><td>Encontramos “diferenças relevantes” sob medida</td></tr>
<tr><td>Dissonância</td><td>Ajustamos crenças ao que já fazemos</td><td>Quem come carne tende a atribuir menos mente aos animais que come</td></tr>
</tbody></table>
<h2>O caso da escala</h2>
<p>Paul Slovic mostrou que a disposição a doar para uma criança faminta cai quando se acrescenta uma segunda criança, e cai mais ainda diante de estatísticas. Nossa compaixão não multiplica. Isso tem uma implicação séria: os maiores problemas do mundo (pobreza extrema, doenças evitáveis, criação industrial de animais) envolvem números que o cérebro não sente. Quem quer agir bem precisa, às vezes, confiar na conta mais do que na emoção.</p>
<h2>O caso da dissonância</h2>
<p>Em estudos de Brock Bastian e colegas, pessoas que acabavam de comer carne atribuíam menos capacidade mental aos animais do que pessoas que comeram frutas. A crença se ajustou ao comportamento. É um exemplo de como um hábito pode moldar um juízo moral, em vez do contrário. Reconhecer o mecanismo é o primeiro passo para não ser governado por ele.</p>
<h2>Como se proteger</h2>
<ol class="roteiro">
<li><strong>Troque de lugar:</strong> julgaria o mesmo ato se o autor fosse do outro grupo? Veja o <a href="ferramentas/teste-de-troca.html">teste de troca</a>.</li>
<li><strong>Olhe os números:</strong> quando a emoção não acompanha a escala, deixe a aritmética falar.</li>
<li><strong>Pergunte pela vítima:</strong> há alguém prejudicado, ou só repulsa?</li>
<li><strong>Desconfie do conforto:</strong> se a conclusão sempre favorece o que você já faz, pode ser dissonância.</li>
<li><strong>Imagine a prática como nova:</strong> se ela fosse inventada hoje, seria aceita? Isso neutraliza o status quo.</li>
</ol>
<p>Para um catálogo completo, com explicação e exemplo de cada viés, veja a seção de <a href="https://politicaparainiciantes.biblioverse.org/vieses.html" target="_blank" rel="noopener">vieses cognitivos</a> do Política Para Iniciantes.</p>
<div class="nota"><strong>Para guardar:</strong> os vieses não são defeitos raros. São o padrão. A ética começa quando notamos que o padrão pode estar errado.</div>
''', fontes=[('Identifiable victim effect (Wikipédia)', WE + 'Identifiable_victim_effect'), ('Scope neglect (Wikipédia)', WE + 'Scope_neglect'), ('Don’t Mind Meat? The Denial of Mind to Animals Used for Human Consumption', 'https://journals.sagepub.com/doi/10.1177/0146167211424291'), ('Psychic numbing and mass atrocity', 'https://www.google.com/search?q=Slovic+psychic+numbing+genocide')]),

dict(slug='tribalismo-moral', grupo='Mente e moral', titulo='Tribalismo moral: os eixos em que privilegiamos os nossos', resumo='Mesmo quem busca imparcialidade mantém preferências por grupo. Nação, raça, sexo, religião, classe, espécie: dezesseis eixos para examinar.', corpo='''
<p class="abre">Tribalismo moral é dar mais peso aos interesses de quem pertence ao seu grupo, só por pertencer. Ele é natural, foi útil na história da espécie, e é a fonte mais constante de injustiça. O primeiro passo para controlá-lo é saber em quais eixos ele atua.</p>
<h2>O ponto de partida</h2>
<p>Antes de qualquer grupo, há o eu. O <strong>egoísmo moral</strong> dá prioridade absoluta a si mesmo. O <strong>tribalismo familiar</strong> estende a prioridade ao círculo íntimo. Quase todo mundo dá algum peso extra a si e aos seus, e isso não é necessariamente um erro: cuidar bem de quem depende de você é parte da moral. O erro começa quando o peso extra vira indiferença ao resto.</p>
<h2>Os dezesseis eixos</h2>
<p>O <a href="https://ethicstest.biblioverse.org/map.html" target="_blank" rel="noopener">Teste de Visão Moral</a> mapeia dezesseis dimensões em que podemos manter preferências de grupo, mesmo buscando imparcialidade:</p>
<div class="temas" style="margin:1em 0">
<a href="#" style="pointer-events:none">Nação</a><a href="#" style="pointer-events:none">Raça</a><a href="#" style="pointer-events:none">Etnia</a><a href="#" style="pointer-events:none">Sexo</a><a href="#" style="pointer-events:none">Identidade de gênero</a><a href="#" style="pointer-events:none">Orientação sexual</a><a href="#" style="pointer-events:none">Religião</a><a href="#" style="pointer-events:none">Visão político-econômica</a><a href="#" style="pointer-events:none">Classe social</a><a href="#" style="pointer-events:none">Capacidade</a><a href="#" style="pointer-events:none">Padrão estético</a><a href="#" style="pointer-events:none">Faixa etária</a><a href="#" style="pointer-events:none">Peso corporal</a><a href="#" style="pointer-events:none">Língua e sotaque</a><a href="#" style="pointer-events:none">Substrato (orgânico ou outro)</a><a href="#" style="pointer-events:none">Espécie</a>
</div>
<p>Alguns desses eixos são reconhecidos como preconceito quase por todos hoje: raça, sexo, religião. Outros ainda passam despercebidos: peso corporal, sotaque, idade. E dois são aceitos abertamente pela maioria: nação e espécie. A pergunta de coerência é a mesma para todos: <strong>que diferença relevante justifica dar menos peso a quem está do outro lado desse eixo?</strong></p>
<h2>O mesmo mecanismo em cada eixo</h2>
<table><thead><tr><th>Etapa</th><th>Como funciona</th></tr></thead><tbody>
<tr><td>Categorizar</td><td>A mente divide o mundo em “nós” e “eles” em segundos, por qualquer traço</td></tr>
<tr><td>Favorecer</td><td>Os “nossos” recebem empatia, benefício da dúvida e recursos</td></tr>
<tr><td>Justificar</td><td>Inventamos uma diferença relevante: “eles são menos racionais, menos sensíveis, menos limpos”</td></tr>
<tr><td>Naturalizar</td><td>A exclusão vira costume, e o costume vira “natureza”</td></tr>
</tbody></table>
<p>A história do racismo, do sexismo e da homofobia segue essas etapas. As justificativas (“não sentem como nós”, “não têm a mesma razão”) são impressionantemente parecidas com as usadas hoje para a espécie. Isso não prova que a espécie seja um eixo igual aos outros, mas obriga quem a defende a mostrar a diferença.</p>
<h2>Nação: o tribalismo respeitável</h2>
<p>Dar prioridade aos compatriotas é visto como dever cívico, não como preconceito. Há razões para alguma prioridade: instituições compartilhadas, deveres recíprocos. Mas o lugar de nascimento é a maior loteria da vida, e ninguém o escolheu. Uma criança que morre de doença evitável do outro lado da fronteira não sofre menos por estar do outro lado. O filósofo Peter Singer pergunta: se a distância e a nacionalidade não mudam o valor de uma vida, o que justifica o peso que damos a elas?</p>
<h2>O que fazer com isso</h2>
<ul>
<li><strong>Nomear o eixo:</strong> “estou dando menos peso a esta pessoa por qual traço?”</li>
<li><strong>Pedir a diferença relevante:</strong> se a resposta é “porque é diferente”, não é uma razão.</li>
<li><strong>Testar a troca:</strong> o mesmo ato, com o autor do outro grupo. Veja o <a href="ferramentas/teste-de-troca.html">teste de troca</a>.</li>
<li><strong>Aceitar deveres especiais sem indiferença:</strong> cuidar mais dos seus é legítimo. Tratar os outros como se não contassem, não.</li>
</ul>
<div class="nota"><strong>Para guardar:</strong> ninguém é imparcial por natureza. A imparcialidade é um trabalho, e começa por descobrir em quais eixos você ainda não a aplicou. A seção de <a href="criterios.html">critérios éticos</a> traz a tabela completa das fronteiras da parcialidade, do indivíduo à espécie e ao tempo, com a posição imparcial correspondente a cada uma.</div>
''', fontes=[MAPA, ('In-group favoritism (Wikipédia)', WE + 'In-group_favoritism'), ('One World Now', 'https://www.google.com/search?tbm=bks&q=Peter+Singer+One+World+Now'), ('A Mente Moralista', WE + 'The_Righteous_Mind')]),

dict(slug='senciencia', grupo='Ética animal', titulo='Senciência: o que é, quem tem e como sabemos', resumo='Sentir dor e prazer é o critério mais defendido para entrar no círculo moral. A ciência diz quem sente, com graus variados de certeza.', corpo='''
<p class="abre">Senciência é a capacidade de ter experiências com valor para quem as tem: dor, prazer, medo, conforto. É diferente de inteligência, de linguagem e de autoconsciência. Um ser pode ser senciente sem resolver problemas ou se reconhecer no espelho. E é a senciência, não a inteligência, que a maioria dos filósofos considera o critério para que os interesses de alguém contem.</p>
<h2>Por que a senciência, e não a razão</h2>
<p>Bentham formulou em 1789: a questão não é se podem raciocinar ou falar, e sim se podem sofrer. A razão é simples: o que torna a dor ruim é ser sentida, não ser compreendida. Um bebê não entende sua dor, e ela conta. Se a razão fosse o critério, bebês e pessoas com deficiência cognitiva grave ficariam fora do círculo, e quase ninguém aceita isso. Veja <a href="dilemas/casos-marginais.html">o argumento dos casos marginais</a>.</p>
<h2>Como a ciência investiga</h2>
<p>Ninguém tem acesso direto à experiência de outro ser, nem de outro humano. Inferimos a senciência por sinais convergentes:</p>
<table><thead><tr><th>Sinal</th><th>O que indica</th></tr></thead><tbody>
<tr><td>Nociceptores e vias nervosas</td><td>Equipamento para detectar dano</td></tr>
<tr><td>Resposta a analgésicos</td><td>O comportamento de dor diminui com remédios para dor</td></tr>
<tr><td>Trocas motivacionais</td><td>Aceita um custo (frio, risco) para evitar dor ou obter alívio</td></tr>
<tr><td>Aprendizado associativo</td><td>Evita o que machucou, busca o que aliviou</td></tr>
<tr><td>Comportamento flexível</td><td>Não é só reflexo: a resposta muda com o contexto</td></tr>
<tr><td>Cuidado com feridas</td><td>Protege a parte machucada, como nós</td></tr>
</tbody></table>
<h2>Quem sente, segundo a evidência</h2>
<ul>
<li><strong>Mamíferos e aves:</strong> consenso científico. A Declaração de Cambridge (2012) afirmou que possuem os substratos neurológicos da consciência.</li>
<li><strong>Peixes:</strong> evidência forte, hoje aceita pela maioria dos pesquisadores da área, após décadas de debate.</li>
<li><strong>Polvos e lulas:</strong> evidência forte; o Reino Unido os incluiu na lei de senciência em 2022.</li>
<li><strong>Caranguejos, lagostas e camarões:</strong> evidência substancial, reconhecida na mesma lei britânica após revisão da London School of Economics.</li>
<li><strong>Insetos:</strong> evidência crescente para alguns grupos; a Declaração de Nova York (2024) afirma uma “possibilidade realista” de experiência consciente em todos os vertebrados e em muitos invertebrados.</li>
<li><strong>Plantas, bactérias:</strong> respondem ao ambiente, mas não há evidência de experiência, nem de um sistema que a produza.</li>
</ul>
<h2>Outras formas possíveis de senciência</h2>
<p>Tudo o que sabemos sobre senciência vem de seres biológicos parecidos conosco: inferimos que sentem por terem nervos, comportamento e história evolutiva em comum. Mas o critério moral não é a semelhança, e sim a capacidade de sentir. Isso obriga a pensar em formas de senciência que ainda não existem, ou que não conhecemos:</p>
<table><thead><tr><th>Forma</th><th>Situação</th><th>O que o critério diz</th></tr></thead><tbody>
<tr><td>Inteligências artificiais e robôs</td><td>Não há evidência de que sistemas atuais sintam algo; textos que “parecem” sentir não são evidência. Mas não se sabe se a experiência exige biologia</td><td>Se um dia sentirem, contam, pelo mesmo critério que faz um porco contar. Excluí-los pelo material seria mais um eixo de tribalismo. Veja <a href="mentes-artificiais.html">mentes artificiais</a></td></tr>
<tr><td>Vida alienígena</td><td>Nenhuma foi encontrada. Se existir, pode ter uma biologia sem nada em comum com a nossa: sem neurônios, sem rostos, sem os sinais que usamos para reconhecer a dor</td><td>Conta, se sentir. O desafio seria epistêmico, reconhecer a senciência, e não moral</td></tr>
<tr><td>Mentes coletivas ou muito diferentes</td><td>Colônias de insetos, organismos modulares, sistemas em que a experiência, se houver, não está em um indivíduo claro</td><td>Pede critérios que não dependam de “um corpo, uma mente”</td></tr>
<tr><td>Animais muito distantes de nós</td><td>Insetos, moluscos, crustáceos: a evidência cresce, mas o acesso é mais difícil</td><td>Precaução proporcional à evidência</td></tr>
</tbody></table>
<p>O que esses casos têm em comum é mostrar que a nossa régua de senciência foi calibrada em nós mesmos. Quanto mais diferente de nós é um ser, mais difícil é reconhecer que ele sente, e mais fácil é concluir, por comodidade, que não sente. A história do debate sobre a dor dos peixes, negada por décadas, é um aviso. O <a href="https://ethicstest.biblioverse.org/map.html" target="_blank" rel="noopener">Teste de Visão Moral</a> registra isso ao separar quem inclui animais sencientes de quem inclui também mentes artificiais sencientes, caso existam.</p>
<h2>O que fazer com a incerteza</h2>
<p>A Declaração de Nova York propõe o princípio da precaução: quando há possibilidade realista de senciência, é irresponsável ignorá-la nas decisões que afetam esses animais. Não é preciso certeza para ter razão de cautela. Se há 50% de chance de um ser sofrer, causar-lhe dano sem necessidade já é um risco moral sério. Veja <a href="incerteza-moral.html">incerteza moral</a>.</p>
<h2>Senciência e consciência</h2>
<p>Os termos se sobrepõem. Senciência costuma indicar a forma mais básica de experiência, com valência (bom ou ruim). Autoconsciência, memória autobiográfica e teoria da mente são camadas a mais, que alguns animais têm e outros não. Para a questão moral básica, a camada que importa é a primeira: se dói, conta.</p>
<div class="nota"><strong>Para guardar:</strong> a ciência da senciência mudou muito em vinte anos, sempre na direção de incluir mais seres. Quem quer agir bem precisa acompanhar o que se sabe, e tratar a dúvida como razão para cuidado, não para indiferença.</div>
''', fontes=[NY, ('Declaração de Cambridge sobre a Consciência', WE + 'Animal_consciousness#Cambridge_Declaration_on_Consciousness'), ('Review of the Evidence of Sentience in Cephalopod Molluscs and Decapod Crustaceans (2021)', 'https://www.lse.ac.uk/business/consulting/assets/documents/Sentience-in-Cephalopod-Molluscs-and-Decapod-Crustaceans-Final-Report-November-2021.pdf'), ('Animal Consciousness (Stanford Encyclopedia)', SEP + 'consciousness-animal/'), ('Animal Ethics', 'https://www.animal-ethics.org/pt/')]),

dict(slug='especismo', grupo='Ética animal', titulo='Especismo e a igual consideração de interesses', resumo='Dar menos peso a um interesse só porque é de outra espécie: o argumento de Singer, a resposta de Regan e o que os críticos dizem.', corpo='''
<p class="abre">Especismo é o nome dado à discriminação com base na espécie: dar menos peso aos interesses de um ser só porque ele não é humano. O termo foi cunhado por Richard Ryder em 1970 e popularizado por Peter Singer em <em>Libertação Animal</em> (1975). A tese é que o especismo tem a mesma estrutura lógica do racismo e do sexismo, e é tão difícil de justificar.</p>
<h2>O princípio da igual consideração</h2>
<p>Singer não diz que todos os seres são iguais em capacidades, nem que devem ser tratados do mesmo jeito. Diz que <strong>interesses iguais devem receber consideração igual</strong>, não importa de quem sejam. Um porco não tem interesse em votar, então não há nada a considerar aí. Mas tem interesse em não sofrer, e esse interesse é tão real quanto o nosso. Dar-lhe menos peso só pela espécie é o que o princípio proíbe.</p>
<h2>O argumento em passos</h2>
<ol class="roteiro">
<li>Racismo e sexismo são errados porque excluem interesses iguais com base em um traço irrelevante.</li>
<li>A espécie, como a raça, é um traço biológico que não muda a capacidade de sofrer.</li>
<li>Logo, excluir interesses iguais com base na espécie é errado pela mesma razão.</li>
</ol>
<p>Para escapar, é preciso negar a premissa 2: mostrar que a espécie traz uma diferença relevante. As tentativas mais comuns:</p>
<table><thead><tr><th>Diferença alegada</th><th>O problema</th></tr></thead><tbody>
<tr><td>Racionalidade, linguagem</td><td>Bebês e pessoas com deficiência grave não as têm, e contam. Veja <a href="dilemas/casos-marginais.html">casos marginais</a></td></tr>
<tr><td>“Pertencem à espécie que tem essas capacidades em geral”</td><td>Julgar um indivíduo pelo grupo é a estrutura do preconceito</td></tr>
<tr><td>Contrato: animais não podem retribuir</td><td>Bebês também não; e quem não pode retribuir é justamente quem mais precisa de proteção</td></tr>
<tr><td>Laços e afeto</td><td>Explicam por que cuidamos mais dos nossos, não por que os outros não contam</td></tr>
<tr><td>Alma, imagem de Deus</td><td>Não é verificável, e divide até os religiosos. Muitas tradições pregam compaixão com todos os seres</td></tr>
</tbody></table>
<h2>A via dos direitos: Regan</h2>
<p>Tom Regan chegou a conclusões parecidas por um caminho deontológico. Para ele, qualquer <strong>sujeito de uma vida</strong>, um ser com crenças, desejos, memória e um bem-estar que importa para si, tem valor inerente, e esse valor é igual em todos que o têm. Não se trata de somar interesses: trata-se de direitos que proíbem usar esses seres como recursos, por mais útil que seja. Regan era mais radical do que Singer: para ele, não é questão de reduzir o sofrimento na criação de animais, e sim de abolir o uso.</p>
<h2>Outras vozes</h2>
<ul>
<li><strong>Gary Francione:</strong> abolicionismo; o problema central é tratar animais como propriedade.</li>
<li><strong>Christine Korsgaard:</strong> uma kantiana que estende o status de fim em si a todos os animais que têm um bem próprio.</li>
<li><strong>Martha Nussbaum:</strong> justiça para animais como garantia de que possam exercer suas capacidades.</li>
<li><strong>Sue Donaldson e Will Kymlicka:</strong> animais como membros da comunidade política, com cidadania, residência ou soberania.</li>
</ul>
<h2>O que os críticos dizem</h2>
<p>Alguns defendem que a pertença à espécie humana tem valor moral em si, independente de capacidades (Bernard Williams falou de um “preconceito humano” que não precisaria de justificativa). Outros aceitam o argumento, mas dizem que a diferença de grau nas capacidades justifica diferenças de peso, o que leva ao <a href="gradualismo.html">gradualismo</a>. Outros ainda concordam na teoria e dizem que a mudança prática é inviável. Singer responde que esse último foi o argumento contra toda reforma moral da história.</p>
<div class="nota"><strong>Para guardar:</strong> o argumento contra o especismo não pede que você ame animais. Pede que diga qual diferença justifica tratar uma dor igual como se valesse menos. Se não há resposta, há um problema.</div>
''', fontes=[LIBERTACAO, ('The Moral Status of Animals (Stanford Encyclopedia)', SEP + 'moral-animal/'), ('The Case for Animal Rights', 'https://www.google.com/search?tbm=bks&q=Regan+The+Case+for+Animal+Rights'), ('Especismo (Wikipédia)', WP + 'Especismo'), SINGER_PE]),

dict(slug='etica-animal-na-pratica', grupo='Ética animal', titulo='Ética animal na prática: granjas, laboratórios e natureza', resumo='Da teoria às escolhas: onde o sofrimento animal se concentra, o que cada teoria diz e o que você pode fazer sem esperar o mundo mudar.', corpo='''
<p class="abre">Se a senciência conta e a espécie não é razão para descontá-la, a conclusão prática é grande. Esta lição mostra onde o sofrimento animal se concentra, como cada família de teorias responde e o que está ao alcance de uma pessoa.</p>
<h2>Onde o sofrimento se concentra</h2>
<table><thead><tr><th>Uso</th><th>Escala aproximada</th><th>O que acontece</th></tr></thead><tbody>
<tr><td>Criação para alimentação</td><td>Cerca de 80 bilhões de animais terrestres mortos por ano, e um número muito maior de peixes</td><td>Confinamento intenso, mutilações sem anestesia, seleção genética que causa dor, abate industrial</td></tr>
<tr><td>Pesca e aquicultura</td><td>Trilhões de peixes por ano, na estimativa mais citada</td><td>Morte por asfixia ou esmagamento, sem atordoamento na maior parte</td></tr>
<tr><td>Experimentação</td><td>Dezenas de milhões por ano</td><td>Vai de testes leves a procedimentos dolorosos; parte é substituível</td></tr>
<tr><td>Entretenimento, vestuário</td><td>Milhões</td><td>Confinamento, treinamento coercitivo, abate para pele</td></tr>
<tr><td>Vida selvagem</td><td>Incontável</td><td>Fome, doença, predação, parasitas: sofrimento que não causamos, mas que existe</td></tr>
</tbody></table>
<p>A criação industrial domina em número e intensidade. É por isso que quase todas as teorias, aplicadas com honestidade, chegam primeiro ao prato.</p>
<h2>O que cada teoria diz</h2>
<ul>
<li><strong>Consequencialismo:</strong> o sofrimento causado pela pecuária industrial supera em muito o prazer de comer carne em vez de alternativas. A conclusão é reduzir ou eliminar o consumo, e apoiar mudanças de política. Singer e as éticas focadas no sofrimento são explícitas.</li>
<li><strong>Deontologia de direitos:</strong> se animais são sujeitos de uma vida, usá-los como recursos viola seus direitos, mesmo que fosse “humanitário”. Regan e Francione defendem a abolição, não só a reforma.</li>
<li><strong>Ética das virtudes:</strong> que pessoa compassiva e justa participaria de um sistema de crueldade em massa, sabendo o que ele faz? Hursthouse concluiu que a resposta aponta para o vegetarianismo.</li>
<li><strong>Ética do cuidado:</strong> a atenção à vulnerabilidade concreta aponta para quem está mais vulnerável, e os animais em granjas são o caso extremo.</li>
<li><strong>Contratualismo estendido:</strong> sem saber a própria espécie, ninguém aceitaria as regras da criação industrial. Veja <a href="contratualismo.html">contratualismo</a>.</li>
</ul>
<p>É notável que teorias que discordam em quase tudo convirjam aqui. Isso sugere que o problema não é teórico, e sim de hábito, interesse e <a href="vieses-morais.html">dissonância</a>.</p>
<h2>O caso da experimentação</h2>
<p>É o uso mais defensável, porque há benefício real para humanos e, às vezes, para os próprios animais. Mesmo assim, a maioria dos filósofos exige o princípio dos 3 R: substituir quando possível, reduzir o número, refinar para minimizar a dor. E pergunta: faríamos esse experimento em um humano com capacidades equivalentes? Se não, por quê?</p>
<h2>O caso da vida selvagem</h2>
<p>Animais selvagens sofrem muito, por causas naturais. Durante décadas, filósofos disseram que isso não era problema nosso. Autores como Oscar Horta e Catia Faria discordam: se o sofrimento conta, conta também quando não o causamos, e devemos ajudar quando pudermos sem causar mais dano, como vacinamos animais contra a raiva. Veja <a href="sofrimento-dos-animais-selvagens.html">o sofrimento dos animais selvagens</a>. Isso contrasta com visões ecocêntricas, que valorizam a natureza “como é”. Veja <a href="vida-e-ecossistemas.html">vida e ecossistemas</a>.</p>
<h2>O que uma pessoa pode fazer</h2>
<ol class="roteiro">
<li><strong>Comer de outro jeito:</strong> é a maior redução de sofrimento ao alcance individual. Não precisa ser perfeito; reduzir já conta, e começar pelos produtos de maior sofrimento por porção (frango, ovos de gaiola, peixe de criação) tem mais efeito. Veja o <a href="https://ethicalfood.biblioverse.org/pt/" target="_blank" rel="noopener">Guia de Alimentos Éticos</a>.</li>
<li><strong>Apoiar mudanças de regra:</strong> leis contra gaiolas, atordoamento obrigatório, fim de subsídios à criação intensiva. Mudanças de política afetam bilhões.</li>
<li><strong>Doar bem:</strong> organizações de defesa animal avaliadas por resultado estão entre as formas mais eficazes de reduzir sofrimento por real doado.</li>
<li><strong>Conversar sem moralismo:</strong> a mudança vem de quem se sente respeitado. Veja <a href="como-discutir-etica.html">como discutir ética</a>.</li>
</ol>
<div class="nota"><strong>Para guardar:</strong> não é preciso resolver a metaética para saber que confinar um ser que sente, a vida inteira, para pagar menos pelo almoço é difícil de justificar. Quase todas as teorias chegam lá. O que falta é a prática.</div>
''', fontes=[LIBERTACAO, ('FAOSTAT: produção pecuária', 'https://www.fao.org/faostat/en/#data/QCL'), ('Fishcount: estimativas de peixes capturados', 'https://fishcount.org.uk/'), ('Animal Ethics: a situação dos animais na natureza', 'https://www.animal-ethics.org/a-situacao-dos-animais-na-natureza/'), ('Animal Charity Evaluators', 'https://animalcharityevaluators.org/')]),

dict(slug='o-dilema-do-bonde', grupo='Dilemas clássicos', titulo='O dilema do bonde e suas variantes', resumo='Desviar o bonde e matar um para salvar cinco: quase todos dizem sim. Empurrar alguém da passarela: quase todos dizem não. O que muda?', corpo='''
<p class="abre">Um bonde desgovernado vai matar cinco pessoas. Você pode acionar uma alavanca e desviá-lo para outro trilho, onde matará uma. Você aciona? A maioria diz sim. Philippa Foot inventou o caso em 1967, e Judith Jarvis Thomson criou as variantes que o tornaram o experimento mental mais famoso da ética.</p>
<h2>As variantes principais</h2>
<table><thead><tr><th>Variante</th><th>O que você faz</th><th>Quem diz sim</th></tr></thead><tbody>
<tr><td><a href="dilemas/bonde-desvio.html">O desvio</a></td><td>Aciona a alavanca; o bonde mata um em vez de cinco</td><td>Cerca de 80 a 90%</td></tr>
<tr><td><a href="dilemas/bonde-passarela.html">A passarela</a></td><td>Empurra um homem grande da passarela; o corpo para o bonde e salva cinco</td><td>Cerca de 10 a 20%</td></tr>
<tr><td>O alçapão</td><td>Aciona uma alavanca que abre um alçapão sob o homem, que cai no trilho</td><td>Mais do que na passarela, menos do que no desvio</td></tr>
<tr><td>O laço</td><td>Desvia o bonde para um trilho em laço; só o corpo do homem o impede de voltar e matar os cinco</td><td>Maioria, mas menos do que no desvio</td></tr>
<tr><td><a href="dilemas/transplante.html">O transplante</a></td><td>Mata um paciente saudável para dar órgãos a cinco</td><td>Quase ninguém</td></tr>
</tbody></table>
<h2>O que explica a diferença</h2>
<p>No desvio e na passarela, o resultado é o mesmo: um morto em vez de cinco. Se só o resultado contasse, as respostas seriam iguais. Não são. As explicações propostas:</p>
<ul>
<li><strong>Meio e efeito colateral:</strong> na passarela, a morte do homem é o <em>meio</em> para salvar os cinco. No desvio, é efeito colateral. É a <a href="intencao-e-previsao.html">doutrina do duplo efeito</a>.</li>
<li><strong>Usar uma pessoa:</strong> empurrar alguém usa o seu corpo como instrumento, sem consentimento. Desviar não usa ninguém. É a fórmula de <a href="kant-e-o-imperativo-categorico.html">Kant</a>.</li>
<li><strong>Contato pessoal:</strong> empurrar com as mãos dispara um alarme emocional que acionar uma alavanca não dispara. Joshua Greene mostrou isso em scanners. Veja <a href="psicologia-moral.html">psicologia moral</a>.</li>
<li><strong>Redistribuir uma ameaça:</strong> no desvio, você redireciona um perigo que já existe. Na passarela, cria um novo. Thomson explorou essa ideia.</li>
</ul>
<h2>O que cada teoria diz</h2>
<ul>
<li><strong>Consequencialismo de ato:</strong> empurre. Cinco vidas valem mais do que uma, e a forma do ato não muda a conta. A maioria dos consequencialistas aceita a conclusão e diz que a intuição contrária é um alarme desajustado.</li>
<li><strong>Deontologia:</strong> desvie, não empurre. Matar como meio viola a pessoa; redirecionar uma ameaça não. Algumas versões absolutistas proíbem até o desvio: você estaria matando o um.</li>
<li><strong>Ética das virtudes:</strong> uma pessoa boa sente horror ao empurrar, e isso é informação. Mas também sente horror a deixar cinco morrer. O dilema é trágico: não há resposta sem perda.</li>
<li><strong>Contratualismo:</strong> que regra aceitaríamos, sem saber se seríamos o um ou um dos cinco? Para o desvio, a regra que salva cinco parece aceitável. Para a passarela, uma regra que permite usar corpos como obstáculos nos deixaria a todos inseguros.</li>
</ul>
<h2>Para que serve o bonde</h2>
<p>Não para prever o que você faria em um bonde. Para isolar <em>o que</em> muda o seu juízo quando o número de mortos é o mesmo. Quem descobre que a diferença está em “usar como meio” aprendeu algo sobre a própria moral, e pode perguntar se essa diferença resiste em outros casos. A crítica de que o dilema é irreal perde o ponto: ele é um experimento controlado, não um retrato.</p>
<h2>Fora do laboratório</h2>
<p>Carros autônomos precisam de regras para colisões inevitáveis. Hospitais decidem quem recebe o leito. Políticas de saúde escolhem quem salvar com recursos limitados. Em todos esses casos, a diferença entre causar e permitir, entre meio e efeito colateral, e entre número e identidade das vítimas aparece de novo. O bonde é só o lugar em que a aprendemos a ver.</p>
<div class="cta"><a class="btn" href="ferramentas/dilema-do-bonde.html">Responda às variantes e veja o seu padrão</a></div>
''', fontes=[('Trolley problem (Wikipédia)', WE + 'Trolley_problem'), ('The Problem of Abortion and the Doctrine of the Double Effect (1967)', 'https://philpapers.org/rec/FOOTPO-2'), ('The Trolley Problem (1985)', 'https://www.jstor.org/stable/796133'), ('Moral Tribes', 'https://www.google.com/search?tbm=bks&q=Joshua+Greene+Moral+Tribes')]),

dict(slug='experimentos-mentais', grupo='Dilemas clássicos', titulo='Outros experimentos mentais que mudaram a ética', resumo='A máquina de experiências, a criança no lago, o violinista, o anel de Giges: casos imaginários que testam princípios reais.', corpo='''
<p class="abre">Experimentos mentais são casos inventados para isolar uma variável, como um laboratório faz. Eles não descrevem a vida real; servem para descobrir o que você pensa de fato, quando as circunstâncias deixam de ajudar. Esta lição apresenta os mais influentes. Cada um tem a sua página na seção de <a href="dilemas.html">dilemas</a>.</p>
<h2>A máquina de experiências</h2>
<p>Robert Nozick, 1974. Uma máquina pode dar a você qualquer experiência que quiser, pela vida inteira, indistinguível da realidade. Você se ligaria? A maioria diz não. Se é assim, o que queremos não é só sentir: queremos <em>fazer</em>, <em>ser</em> alguém e estar em contato com a realidade. O caso é a principal objeção ao hedonismo. Veja <a href="dilemas/maquina-de-experiencias.html">a página</a>.</p>
<h2>A criança no lago</h2>
<p>Peter Singer, 1972. Você passa por um lago raso e vê uma criança se afogando. Salvá-la estraga seus sapatos caros. Ninguém hesita. Então por que hesitamos em doar o valor dos sapatos para salvar uma criança distante, de uma doença evitável? Distância, número de outros que poderiam ajudar e falta de contato visual não parecem diferenças moralmente relevantes. O caso fundou o movimento do altruísmo eficaz. Veja <a href="dilemas/crianca-no-lago.html">a página</a>.</p>
<h2>O violinista</h2>
<p>Judith Jarvis Thomson, 1971. Você acorda conectado a um violinista famoso que morrerá se for desconectado antes de nove meses. Tem obrigação de ficar? Thomson argumenta que não, por mais que seja generoso ficar. O caso foi criado para o debate sobre aborto: mesmo concedendo que o feto é uma pessoa, não se segue que haja obrigação de sustentá-lo com o próprio corpo. Veja <a href="dilemas/violinista.html">a página</a>.</p>
<h2>O anel de Giges</h2>
<p>Platão, <em>República</em>. Um anel torna quem o usa invisível. Quem resistiria a fazer o que quisesse sem ser visto? A pergunta é se somos justos por convicção ou por medo de ser pegos. Platão argumenta que a justiça vale por si mesma, porque a alma injusta vive em desordem. Mas o caso também testa a diferença entre moral e reputação. Veja <a href="dilemas/anel-de-giges.html">a página</a>.</p>
<h2>O monstro utilitário e a conclusão repugnante</h2>
<p>Dois casos contra a agregação simples. No <a href="dilemas/monstro-utilitario.html">monstro</a> (Nozick), um ser que ganha mais prazer do que todos perdem justificaria sacrificar todos a ele. Na <a href="dilemas/conclusao-repugnante.html">conclusão repugnante</a> (Parfit), um mundo imenso de vidas quase sem valor seria melhor do que um mundo pequeno de vidas excelentes, porque a soma é maior. Os dois obrigaram os consequencialistas a repensar como somar.</p>
<h2>Omelas</h2>
<p>Ursula K. Le Guin, 1973. Uma cidade perfeita, cuja felicidade depende de uma criança mantida em sofrimento em um porão. Todos sabem. Alguns vão embora. O conto pergunta se a felicidade de muitos pode se apoiar na agonia de um, e dá nome à objeção mais antiga ao utilitarismo. Veja <a href="dilemas/omelas.html">a página</a>.</p>
<h2>O último homem</h2>
<p>Richard Routley, 1973. O último humano vivo, antes de morrer, destrói toda a vida restante no planeta: florestas, animais, tudo. Nenhum humano será afetado. Ele fez algo errado? Se sim, o valor da natureza não depende de nós. O caso fundou a ética ambiental. Veja <a href="dilemas/ultimo-homem.html">a página</a>.</p>
<h2>Jim e os indígenas</h2>
<p>Bernard Williams, 1973. Jim chega a uma vila onde vinte prisioneiros vão ser executados. O capitão oferece: se Jim matar um, os outros dezenove serão libertados. O utilitarismo diz que Jim deve atirar. Williams não discorda da resposta, mas da facilidade: o utilitarismo trata a integridade de Jim como um detalhe. Veja <a href="dilemas/jim-e-os-indigenas.html">a página</a>.</p>
<h2>Como usar um experimento mental</h2>
<ol class="roteiro">
<li>Aceite as premissas. “Mas na vida real…” é fugir do teste.</li>
<li>Note a sua primeira reação. Ela é dado, não veredito.</li>
<li>Pergunte que princípio ela expressa.</li>
<li>Teste o princípio em outro caso. Se falha, ou o princípio está errado, ou a reação estava.</li>
<li>Repita até as suas intuições e princípios se encaixarem. É o <a href="argumentos-morais.html">equilíbrio reflexivo</a>.</li>
</ol>
''', fontes=[('Thought Experiments (Stanford Encyclopedia)', SEP + 'thought-experiment/'), ('Anarquia, Estado e Utopia', WE + 'Anarchy,_State,_and_Utopia'), ('Famine, Affluence, and Morality (Wikipédia)', WE + 'Famine,_Affluence,_and_Morality'), ('A Defense of Abortion (Wikipédia)', WE + 'A_Defense_of_Abortion')]),
]
