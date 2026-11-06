"""Bloco “O que não é…” de cada teoria (novembro de 2026): as concepções erradas e os espantalhos mais comuns sobre
cada posição, com a correção. Chave: slug da teoria; valor: lista de (o que se diz, o que é de fato).
O build exige uma entrada para toda teoria; build.py renderiza com nao_e_html()."""

NAO_E = {
'consequencialismo-de-ato': [
 ('“Os fins justificam os meios, então vale tudo.”', 'Os meios entram na conta: a dor que causam, a confiança que destroem, o precedente que criam. Um meio cruel quase sempre piora o resultado total, e por isso o consequencialista sério o rejeita.'),
 ('“O consequencialista calcula tudo antes de agir.”', 'Quase todos defendem que, no dia a dia, se sigam regras e hábitos confiáveis, porque calcular caso a caso dá errado. O cálculo é o critério do certo, não o procedimento para decidir.'),
 ('“Ele só olha para o que de fato aconteceu.”', 'A maioria julga pela expectativa razoável no momento da escolha. Quem age bem com a informação que tinha e tem azar não fez a coisa errada; teve azar.'),
],
'consequencialismo-de-regras': [
 ('“É só deontologia com outro nome.”', 'As regras não valem por si: valem porque, seguidas por todos, produzem os melhores resultados. Se uma regra deixa de servir, ela deve mudar; na deontologia, não.'),
 ('“É adoração de regras: segue a regra mesmo quando isso é ruim.”', 'A objeção existe, mas as versões atuais incluem regras de exceção para emergências. O que se recusa é abrir exceção só porque convém a quem decide.'),
],
'utilitarismo-classico': [
 ('“Utilitarismo é egoísmo ou hedonismo pessoal.”', 'É o contrário: o bem-estar de todos os afetados conta igualmente, inclusive o de estranhos e de animais. O seu prazer vale exatamente o mesmo que o de qualquer outro.'),
 ('“O utilitarista sacrificaria um inocente por qualquer ganho.”', 'Em cenários de lousa, talvez. Na prática, Mill e os utilitaristas atuais mostram que sociedades que sacrificam inocentes geram medo, desconfiança e abuso, e por isso defendem direitos e regras firmes.'),
 ('“Utilitarismo é só sobre dinheiro ou utilidade econômica.”', 'A “utilidade” de Bentham é felicidade e ausência de sofrimento, não lucro. A economia tomou a palavra emprestada e mudou o sentido.'),
 ('“Utilitarista só pensa em prazer baixo, de porco.”', 'Mill respondeu a isso no século 19: há prazeres de qualidades diferentes, e quem conheceu ambos prefere os mais altos.'),
],
'utilitarismo-de-preferencias': [
 ('“É dar às pessoas tudo o que elas querem.”', 'Conta a satisfação de preferências informadas e ponderadas, não de qualquer desejo. Uma preferência baseada em erro ou que fere outros pesa pouco ou nada.'),
 ('“É o mesmo que utilitarismo clássico.”', 'A diferença muda resultados: uma pessoa pode preferir a verdade dolorosa à ilusão feliz, e o utilitarismo de preferências respeita isso; o hedonista, não.'),
],
'utilitarismo-medio': [
 ('“Utilitarismo médio quer matar os menos felizes para subir a média.”', 'É a objeção clássica, não a posição. Seus defensores mostram que matar alguém reduz a média pelo medo e pela dor que gera, e que a teoria é sobre como comparar populações possíveis, não sobre eliminar pessoas.'),
 ('“É só o utilitarismo normal.”', 'Em questões de população, as duas versões divergem: a soma total favorece populações enormes com vidas pouco boas; a média, não. É o debate da “conclusão repugnante”.'),
],
'prioritarismo': [
 ('“Prioritarismo é igualitarismo.”', 'O igualitarista valoriza a igualdade em si, e aceitaria piorar quem está bem só para igualar. O prioritarista, não: ele só dá peso extra a melhoras para quem está pior.'),
 ('“É dar tudo aos mais pobres.”', 'Todos continuam contando; o peso extra é gradual. Um ganho grande para muitos que estão bem ainda pode vencer um ganho pequeno para quem está pior.'),
],
'maximin': [
 ('“Maximin quer todo mundo igualmente pobre.”', 'Ele aceita qualquer desigualdade que melhore a situação de quem está pior. Uma sociedade com ricos é preferível se nela o mais pobre vive melhor do que viveria sem eles.'),
 ('“Maximin é o princípio de Rawls inteiro.”', 'É só a regra de decisão por trás do princípio da diferença. Rawls punha antes dela liberdades iguais e igualdade de oportunidades, que o maximin sozinho não garante.'),
],
'igualitarismo': [
 ('“Igualitário quer que todos sejam iguais em tudo.”', 'Quase todos os igualitários falam de igualdade em algo específico: oportunidades, recursos, bem-estar ou status. Ninguém defende que todos tenham os mesmos gostos ou vidas.'),
 ('“Igualitarismo prefere nivelar por baixo.”', 'A objeção do nivelamento por baixo é a crítica mais forte, e os igualitários respondem combinando a igualdade com outros valores. Pouquíssimos aceitam cegar quem enxerga para igualar aos cegos.'),
 ('“Igualdade de resultado e de oportunidade são a mesma coisa.”', 'São posições rivais dentro do igualitarismo. A igualdade de oportunidades aceita resultados desiguais que venham de escolhas, não de sorte de nascimento.'),
],
'suficientismo': [
 ('“Suficientismo não se importa com desigualdade.”', 'Ele se importa até o limiar: ninguém pode ficar abaixo do suficiente. Acima dele, muitos suficientistas aceitam outros valores, incluindo alguma preocupação com desigualdade.'),
 ('“O suficiente é só sobreviver.”', 'Para a maioria dos autores, suficiente é o bastante para uma vida decente e com autonomia, não o mínimo para não morrer.'),
],
'prioridade-ao-sofrimento': [
 ('“É o mesmo que utilitarismo negativo.”', 'Aqui o prazer e o bem-estar ainda valem, apenas pesam menos que o sofrimento equivalente. No utilitarismo negativo estrito, nenhum prazer compensa sofrimento extremo.'),
 ('“Quer reduzir sofrimento a qualquer custo.”', 'A assimetria é de peso, não de veto. Um pequeno sofrimento pode ser aceito por um ganho grande em bem-estar.'),
],
'utilitarismo-negativo': [
 ('“O utilitarista negativo quer destruir o mundo para acabar com o sofrimento.”', 'É o “argumento do explodidor benevolente”, a objeção mais citada. A maioria dos defensores responde que destruir o mundo causaria sofrimento extremo e que, de todo modo, a teoria se aplica a escolhas reais, não a botões imaginários.'),
 ('“É pessimismo ou depressão disfarçada de ética.”', 'É uma tese sobre o que pesa mais, não sobre como se sentir. Muitos defensores são otimistas sobre reduzir sofrimento no mundo.'),
],
'etica-focada-no-sofrimento': [
 ('“Não valorizar o prazer é não gostar da vida.”', 'A tese é que o prazer não tem valor que precise ser produzido, não que ele seja ruim. Quem já existe pode desfrutar; o que não existe não precisa ser criado para desfrutar.'),
 ('“É o mesmo que utilitarismo negativo.”', 'É mais radical: no utilitarismo negativo, fora dos extremos, o prazer ainda conta. Aqui ele nunca entra no lado positivo da conta.'),
],
'deontologia-kantiana': [
 ('“Deontologia é só seguir regras ou a lei.”', 'A regra kantiana é um teste de razão, não um código: você se pergunta se poderia querer que todos agissem como você. Seguir uma lei injusta reprova nesse teste.'),
 ('“Kant diria que você deve entregar seu amigo ao assassino.”', 'Kant de fato escreveu algo assim sobre a mentira, e quase todos os kantianos de hoje o rejeitam nesse ponto. A fórmula de tratar a pessoa como fim permite proteger o amigo.'),
 ('“Deontologia ignora as consequências.”', 'Ela nega que as consequências sejam a única coisa que importa, não que importem. Kant tinha deveres de promover a felicidade alheia.'),
 ('“Kant é frio e contra os sentimentos.”', 'Kant dizia que agir com compaixão é bom; o que ele negava era que o valor moral da ação dependesse de se estar com vontade.'),
],
'deontologia-absolutista': [
 ('“Absolutista é fanático.”', 'A posição é que algumas coisas, como torturar uma criança por diversão, não têm preço. Quase todo mundo é absolutista sobre pelo menos um ponto.'),
 ('“Absolutismo moral é absolutismo político.”', 'Nada a ver: um é sobre regras que não cedem; o outro, sobre reis com poder total. A maioria dos absolutistas morais foi contra tiranos.'),
],
'deontologia-de-limiar': [
 ('“Deontologia de limiar é consequencialismo disfarçado.”', 'Abaixo do limiar, as restrições valem mesmo que violá-las produza melhores resultados. É isso que a separa do consequencialismo.'),
 ('“É incoerente: ou a restrição vale ou não vale.”', 'É a objeção principal, e os defensores respondem que muitos valores funcionam assim: direitos individuais cedem em emergências nacionais, e ninguém acha isso absurdo.'),
],
'deontologia-de-direitos': [
 ('“Direitos são só o que a lei diz.”', 'A teoria fala de direitos morais, que a lei pode reconhecer ou violar. A escravidão era legal e violava direitos.'),
 ('“Ter direitos é poder fazer qualquer coisa.”', 'Um direito é um trunfo contra ser usado como meio, não uma licença. Ele termina onde começa o direito igual do outro.'),
 ('“Se animais têm direitos, têm direito de votar.”', 'Direitos acompanham interesses. Um cão tem interesse em não sofrer, não em votar. O mesmo vale para bebês.'),
],
'doutrina-do-duplo-efeito': [
 ('“É uma desculpa para causar dano fingindo que não queria.”', 'A doutrina exige que o dano não seja o meio para o bem, que seja proporcional e que você não o deseje. Fingir não passa no teste.'),
 ('“É uma tese só católica.”', 'Nasceu na teologia, mas está no direito penal, na ética médica e no direito da guerra, e é discutida por filósofos sem religião.'),
],
'deontologia-pluralista': [
 ('“Sem hierarquia de deveres, vale qualquer coisa.”', 'Os deveres são reais e obrigam; o que não existe é uma fórmula que diga qual vence. O juízo, treinado, decide no caso, como faz um bom médico.'),
 ('“É relativismo.”', 'Os deveres de Ross, como não ferir, cumprir promessas e reparar, valem para todos. Só o peso varia com o caso.'),
],
'teoria-do-mandamento-divino': [
 ('“Sem Deus, vale tudo.”', 'É a posição em sua forma mais fraca, e a maioria dos teólogos não a sustenta. Muitos dizem que Deus ordena o bom porque é bom, e que quem não crê pode conhecê-lo pela razão.'),
 ('“Toda ética religiosa é mandamento divino.”', 'Tomás de Aquino, o maior teólogo católico, defendia a lei natural: o bem é conhecido pela razão. A teoria do mandamento é uma entre várias éticas religiosas.'),
 ('“A teoria diz para obedecer a qualquer ordem em nome de Deus.”', 'Ela diz que o certo é o que Deus ordena, não o que alguém afirma que Deus ordena. Distinguir os dois é o problema prático da teoria.'),
],
'etica-das-virtudes': [
 ('“Ética das virtudes não diz o que fazer.”', 'Ela diz: faça o que a pessoa virtuosa faria aqui. Isso exige perceber o caso, não aplicar uma fórmula. Para muitos, é mais exigente que uma regra.'),
 ('“Virtude é obediência ou puritanismo.”', 'As virtudes aristotélicas incluem coragem, generosidade, bom humor e amizade. O vício está nos extremos, inclusive no excesso de rigidez.'),
 ('“É relativismo: cada cultura tem suas virtudes.”', 'Há variação, mas coragem, honestidade e compaixão aparecem em quase todas as tradições, e a ética das virtudes usa a natureza humana como base.'),
],
'etica-do-cuidado': [
 ('“Ética do cuidado é ética para mulheres.”', 'Nasceu da observação de como mulheres raciocinavam moralmente, mas a proposta é para todos: homens cuidam, e sociedades inteiras dependem disso.'),
 ('“Cuidar é ser submisso ou se sacrificar.”', 'Autoras da corrente alertam contra o cuidado que destrói quem cuida. Cuidar bem inclui cuidar de si e exigir reciprocidade.'),
 ('“É só sentimentalismo, sem razão.”', 'O cuidado exige atenção, juízo e conhecimento da situação concreta. A crítica da corrente é a uma razão abstrata que ignora as pessoas reais.'),
],
'estoicismo': [
 ('“Estoico é quem não sente nada.”', 'O estoico sente, e muito; o que ele não faz é deixar que paixões sem juízo governem suas ações. Sêneca escreveu cartas de consolo e chorou mortes.'),
 ('“Estoicismo é aceitar tudo e não lutar.”', 'Catão lutou contra César e Marco Aurélio governou um império. O estoico age no que depende dele e aceita apenas o que não depende.'),
 ('“É a autoajuda de executivos.”', 'A versão popular tirou a parte ética: para os estoicos, todos os humanos são parentes e a justiça é a virtude maior. O estoicismo é cosmopolita.'),
],
'contratualismo-hobbesiano': [
 ('“Hobbes achava que as pessoas são más.”', 'Ele achava que são autointeressadas e vulneráveis, e que sem regras isso leva a guerra. A moral é a solução racional, não um disfarce.'),
 ('“O contrato é um evento histórico que nunca aconteceu, logo a teoria falha.”', 'O contrato é hipotético: a pergunta é que regras pessoas racionais aceitariam, não que regras assinaram.'),
],
'contratualismo-rawlsiano': [
 ('“Rawls era socialista.”', 'Rawls aceitava mercado e desigualdade, desde que beneficiassem os mais desfavorecidos. Ele é lido como liberal igualitário, não como socialista.'),
 ('“O véu da ignorância é só uma fantasia.”', 'É um dispositivo para forçar imparcialidade, como pedir que quem corta o bolo escolha a fatia por último. A ideia é testar princípios, não descrever a origem das sociedades.'),
 ('“Rawls quer igualdade total.”', 'O princípio da diferença permite desigualdades. O que ele proíbe é desigualdade que não ajude quem está pior.'),
],
'contratualismo-escanloniano': [
 ('“É o mesmo que Rawls.”', 'Rawls trata da justiça das instituições; Scanlon, do que devemos uns aos outros em qualquer ação. O critério também é outro: razoável rejeição, não escolha sob véu.'),
 ('“Quem não pode rejeitar princípios, como animais, fica de fora.”', 'É a objeção que o próprio Scanlon reconhece. Várias respostas estendem a teoria a quem pode ser representado por outros.'),
],
'contratualismo-estendido': [
 ('“Esconder a espécie sob o véu é absurdo, porque animais não fazem contratos.”', 'O véu é um teste de imparcialidade, e nunca exigiu que as partes existam. Esconder a espécie só pergunta que regras você aceitaria sem saber em que corpo nasceria.'),
 ('“É colocar animais no mesmo nível de humanos.”', 'Sob o véu, as regras levariam em conta capacidades diferentes. O que o teste proíbe é a regra que só serve a quem escreve.'),
],
'egoismo-etico': [
 ('“Egoísmo ético é ser mesquinho.”', 'A tese é que cada um deve buscar o próprio bem bem entendido, o que inclui amigos, reputação e paz de espírito. O mesquinho costuma ser egoísta ruim.'),
 ('“Egoísmo ético é a mesma coisa que egoísmo psicológico.”', 'Um diz que devemos agir pelo próprio interesse; o outro, que sempre agimos assim, mesmo sem querer. São teses diferentes, e a segunda é empírica e muito contestada.'),
],
'relativismo-cultural': [
 ('“Relativismo é tolerância.”', 'Se cada cultura define o certo, uma cultura intolerante está certa em ser intolerante. A tolerância universal é justamente o que o relativismo não consegue defender.'),
 ('“Reconhecer que costumes variam já é ser relativista.”', 'Que os costumes variam é um fato que todos aceitam. O relativismo é a tese extra de que não há padrão para julgar entre eles.'),
 ('“O relativista acha que vale tudo.”', 'Para o relativista, dentro de cada cultura há certo e errado bem definidos. O que ele nega é um padrão acima das culturas.'),
],
'subjetivismo': [
 ('“Subjetivismo é respeitar a opinião de cada um.”', 'Se cada um define o certo, ninguém jamais erra e discordar não faz sentido. É a objeção que leva muitos a abandonar a posição.'),
 ('“Toda opinião moral é subjetiva, logo o subjetivismo está certo.”', 'Que as pessoas têm opiniões é trivial. O subjetivismo afirma algo mais forte: que a opinião torna a coisa certa.'),
],
'ceticismo-normativo': [
 ('“Cético moral é quem não tem moral.”', 'Céticos como Mackie viveram vidas comuns e defenderam causas. A tese é sobre se há fatos morais a descobrir, não sobre como se comportar.'),
 ('“Ceticismo é relativismo.”', 'O relativista diz que a verdade moral existe, mas é local. O cético diz que talvez não exista verdade moral alguma.'),
],
'antropocentrismo': [
 ('“Antropocêntrico é quem não gosta de animais.”', 'A posição aceita que maltratar animais é errado, mas pelo efeito em pessoas: embrutece, destrói recursos, magoa donos. O que nega é que o animal conte por si mesmo.'),
 ('“Antropocentrismo é a posição do senso comum, logo está certa.”', 'Foi o senso comum por milênios, como a escravidão. A pergunta ética é se há razão para a fronteira passar na espécie.'),
],
'sencientismo': [
 ('“Sencientismo é veganismo.”', 'O veganismo é uma prática que muitos sencientistas adotam. O sencientismo é um critério: quem sente, conta. Nem todo sencientista é vegano, e há veganos por outras razões.'),
 ('“Sencientista acha que um rato vale o mesmo que uma criança.”', 'A tese é consideração igual para interesses iguais. Uma criança tem interesses que um rato não tem, e por isso pesa mais em quase tudo. Mas a dor do rato conta.'),
 ('“Sencientismo é colocar animais acima de humanos.”', 'É colocar os animais na conta, de onde estavam excluídos. Humanos continuam contando integralmente.'),
],
'biocentrismo': [
 ('“Biocentrista acha que uma bactéria vale uma pessoa.”', 'A maioria dos biocentristas é hierárquica: toda vida tem valor, mas não o mesmo valor. Só Taylor defendeu igualdade, e com qualificações.'),
 ('“Biocentrismo é ambientalismo.”', 'O ambientalismo pode ser antropocêntrico. O biocentrismo é uma tese sobre o que conta moralmente, e pode discordar do ambientalismo quando ecossistemas exigem matar indivíduos.'),
],
'ecocentrismo': [
 ('“Ecocentrismo é cuidar da natureza.”', 'Muitos cuidam da natureza pelo bem dos seres que vivem nela. O ecocentrismo diz algo mais forte: o sistema vale mais que os indivíduos, e por isso aceita matar animais para preservar a espécie ou o bioma.'),
 ('“Ecocêntrico é ecofascista.”', 'É uma objeção, não uma descrição. A maioria dos ecocentristas rejeita sacrificar humanos pela biosfera, embora a teoria tenha dificuldade para explicar por quê.'),
],
'gradualismo': [
 ('“Gradualismo é especismo.”', 'O especismo dá peso pela espécie; o gradualismo, por capacidades. Um humano com poucas capacidades cognitivas teria, pelo critério, peso menor, o que o especista recusa.'),
 ('“Gradualismo nega que animais importam.”', 'Todos os seres sencientes contam; o que varia é o peso de interesses de tipos diferentes. Um gradualista pode ser vegano.'),
],
'temporalismo': [
 ('“Dar menos peso ao futuro é não ligar para o futuro.”', 'O temporalismo diz que o futuro pesa menos, não que pesa zero. E a maior parte dos filósofos rejeita o desconto puro pelo tempo, aceitando só a incerteza como razão.'),
 ('“Atemporalismo é obsessão com o longo prazo.”', 'A tese é que um sofrimento daqui a cem anos vale o mesmo que um de hoje. Como o futuro é incerto, isso não implica sacrificar o presente.'),
],
'carbonismo': [
 ('“Carbonismo é ciência: máquinas não sentem.”', 'Que as máquinas atuais não sintam é uma tese empírica provável. O carbonismo diz mais: que, mesmo que uma sentisse, não contaria. É uma tese ética, não científica.'),
 ('“Quem rejeita o carbonismo acha que o ChatGPT sofre.”', 'Rejeitar o carbonismo é dizer que, se um sistema vier a sentir, ele contará. Não é afirmar que algum já sente.'),
],
'realismo-naturalista': [
 ('“Realismo moral é dizer que a moral vem de Deus.”', 'O naturalista diz que fatos morais são fatos sobre bem-estar, florescimento ou cooperação, e que se pode investigá-los sem religião.'),
 ('“Se a moral é natural, ela é o que a evolução nos deu.”', 'A evolução explica de onde vêm nossas intuições, não se elas estão certas. O naturalista pode dizer que a evolução nos deu intuições erradas.'),
],
'realismo-nao-naturalista': [
 ('“Fatos morais não naturais são fantasmas.”', 'É a objeção de Mackie. Parfit e Scanlon respondem que fatos matemáticos e lógicos também não são naturais, e ninguém os chama de fantasmas.'),
 ('“Não naturalista acha que a moral é uma intuição qualquer.”', 'A intuição que ele defende é um juízo refletido, testado contra outros e corrigível, como em matemática. Não é um palpite.'),
],
'construtivismo': [
 ('“Construtivismo é relativismo: a moral é inventada.”', 'O procedimento que constrói as normas é o mesmo para todos os agentes racionais. O resultado vale universalmente, embora não exista antes do procedimento.'),
 ('“Construtivismo é só contratualismo.”', 'O contratualismo é uma forma de construtivismo, mas o construtivismo kantiano deriva normas da estrutura da agência racional, sem acordo entre partes.'),
],
'relativismo-metaetico': [
 ('“É o mesmo que relativismo cultural.”', 'O relativismo cultural é uma tese normativa, sobre o que fazer. O metaético é uma tese sobre a verdade: juízos morais são verdadeiros dentro de um referencial, como “é esquerda” depende de onde você está.'),
 ('“Relativista metaético acha que a escravidão era certa para quem a praticava.”', 'Alguns aceitam essa consequência; outros respondem que o referencial relevante é o nosso, e que podemos avaliar o passado a partir dele.'),
],
'teoria-do-erro': [
 ('“Quem diz que a moral é um erro vive sem moral.”', 'Mackie escreveu um livro inteiro de ética normativa. A tese é que a linguagem moral descreve fatos que não existem; a prática moral pode continuar por outras razões.'),
 ('“Teoria do erro é niilismo que diz que nada importa.”', 'Que nada importa objetivamente não é que nada importa para ninguém. O teórico do erro ainda se importa, e a teoria não lhe diz para parar.'),
],
'emotivismo': [
 ('“Emotivismo é dizer que a moral é só emoção, então não há como discutir.”', 'Para o emotivista, discutimos moral discutindo fatos: se eu souber o que a ação causa, minha atitude pode mudar. O desacordo puro de atitude é raro.'),
 ('“Emotivista acha que os juízos morais são caprichos.”', 'As atitudes expressas podem ser estáveis, informadas e compartilhadas. Caprichosas ou não, isso é outra questão.'),
],
'prescritivismo': [
 ('“Prescritivismo é mandar nos outros.”', 'A prescrição vale também para quem a faz, em qualquer situação igual. É esse teste de universalização que dá força à teoria, e Hare o usou para chegar ao utilitarismo.'),
 ('“É só emotivismo com outro nome.”', 'A exigência de universalizabilidade é uma restrição lógica que o emotivismo não tem. Para Hare, um fanático coerente é raro justamente porque precisa aceitar a regra na pele.'),
],
'quase-realismo': [
 ('“Quase-realismo é uma trapaça: nega a objetividade e depois a usa.”', 'Blackburn diz que “ganhar o direito” à linguagem objetiva é mostrar que ela faz sentido a partir de atitudes refinadas. Os críticos discordam, mas não é uma contradição óbvia.'),
 ('“Para o quase-realista, a escravidão não era errada de verdade.”', 'A posição diz exatamente que podemos afirmar que a escravidão era errada, mesmo que todos achassem o contrário, porque essa afirmação é parte da atitude.'),
],
'quietismo-metaetico': [
 ('“Quietismo é não ter posição.”', 'O quietista tem uma posição forte: que a pergunta metafísica está mal feita e que a ética se faz dentro da ética. Dworkin dedicou um livro a defender isso.'),
 ('“É uma fuga.”', 'É uma tese sobre que perguntas fazem sentido, como quem recusa a pergunta “que horas são no Sol?”. Pode estar errada, mas não é omissão.'),
],
'moismo': [
 ('“Moísmo é só um utilitarismo chinês antigo.”', 'Mozi julgava práticas pelo benefício ao povo, mas também apelava à vontade do Céu e à ordem social. É consequencialista, com elementos que o utilitarismo não tem.'),
 ('“Cuidado imparcial é não amar a própria família.”', 'Mozi dizia que quem cuida dos pais dos outros tem os próprios pais cuidados por outros. A imparcialidade era um argumento sobre reciprocidade, não contra a família.'),
],
'lei-natural': [
 ('“Lei natural é lei da selva: o que é natural é certo.”', 'A lei natural clássica diz que a razão descobre bens humanos básicos, como a vida, o conhecimento e a amizade. Nada a ver com “natural” no sentido biológico.'),
 ('“Lei natural é só doutrina católica.”', 'Vem de Aristóteles e dos estoicos, foi sistematizada por Tomás de Aquino e tem versões seculares, como a de John Finnis e a dos direitos humanos.'),
],
'etica-do-discurso': [
 ('“Ética do discurso é decidir tudo por votação.”', 'O critério é o acordo racional em um diálogo sem coerção, não a maioria. Uma maioria que ignora argumentos não legitima a norma.'),
 ('“É uma utopia: ninguém conversa sem coerção.”', 'Habermas admite que o diálogo ideal é uma referência, como a honestidade perfeita, que serve para julgar os diálogos reais e corrigi-los.'),
],
'existencialismo': [
 ('“Existencialismo é fazer o que quiser.”', 'Sartre dizia que, ao escolher, você escolhe por toda a humanidade, e que a má-fé é fugir da responsabilidade. É uma ética da responsabilidade total, não da licença.'),
 ('“Existencialista é niilista.”', 'O niilista diz que nada tem valor; o existencialista, que o valor é criado pelo compromisso. Camus escreveu contra o niilismo e a favor da revolta solidária.'),
],
'pragmatismo': [
 ('“Pragmatismo é fazer o que funciona para mim.”', 'Para Dewey, o que funciona é o que resolve problemas de uma comunidade, avaliado pela experiência e pela discussão pública. O interesse pessoal não é o teste.'),
 ('“Sem fundamentos fixos, o pragmatista aceita qualquer moral.”', 'Ele aceita o que sobrevive ao teste da experiência. A escravidão não sobreviveu; muitas práticas foram revistas justamente por esse método.'),
],
'particularismo': [
 ('“Particularismo é relativismo ou ‘depende’.”', 'O particularista acha que há certo e errado em cada caso, e que eles são objetivos. O que ele nega é que uma regra geral capture isso.'),
 ('“Particularista não dá conselho nenhum.”', 'Dá: olhe para o caso, veja o que importa nele, aprenda com casos parecidos. O que ele não entrega é um manual.'),
],
'confucionismo': [
 ('“Confucionismo é obediência cega aos superiores.”', 'Confúcio dizia que o ministro deve repreender o príncipe que erra, e Mêncio defendia o direito de depor o tirano. A hierarquia vem com deveres de quem está acima.'),
 ('“Confucionismo é religião.”', 'É sobretudo uma ética e uma filosofia política. Confúcio evitava falar de deuses e do pós-morte.'),
],
'etica-budista': [
 ('“Budismo é indiferença ao mundo.”', 'A compaixão por todos os seres é central. O desapego é de desejos que geram sofrimento, não das pessoas.'),
 ('“O carma é um castigo divino.”', 'O carma é a ideia de que ações têm consequências para quem as pratica, sem juiz. É mais próximo de causa e efeito moral do que de punição.'),
],
'ubuntu': [
 ('“Ubuntu é coletivismo que esmaga o indivíduo.”', 'A pessoa se forma na comunidade, mas a comunidade existe para que cada um se torne pessoa. Pensadores do ubuntu criticam tanto o individualismo quanto o totalitarismo.'),
 ('“É um slogan de empresa.”', 'O termo virou marca, mas na filosofia africana é uma ética da humanidade compartilhada, discutida por Ramose, Metz e Tutu.'),
],
'intuicionismo-moral': [
 ('“Intuição é palpite ou gosto.”', 'A intuição que o intuicionista defende é a apreensão de uma verdade evidente após reflexão, como entender que o todo é maior que a parte. Não é a primeira reação.'),
 ('“Se as intuições divergem, o intuicionismo falha.”', 'A divergência pode vir de erro, interesse ou falta de reflexão, como em matemática. O intuicionista aceita que intuições se corrijam umas às outras.'),
],
'objetivismo-moral': [
 ('“Objetivismo moral é o objetivismo de Ayn Rand.”', 'São coisas sem relação. Objetivismo moral é a tese de que há verdades morais para todos; Rand usou a palavra para a sua filosofia do egoísmo racional.'),
 ('“Quem acha que há verdades morais acha que já as conhece todas.”', 'Dizer que a resposta existe não é dizer que a tenho. É o que torna possível estar errado e aprender.'),
 ('“Objetivismo é intolerância.”', 'A tolerância é um valor que só faz sentido se for objetivamente bom tolerar. O relativista tem mais dificuldade em defendê-la.'),
],
'objetivismo-de-ayn-rand': [
 ('“Rand defende ser cruel com os outros.”', 'Ela defendia o comércio voluntário e condenava a força e a fraude. O que rejeitava era o dever de se sacrificar pelos outros.'),
 ('“O objetivismo é a filosofia dos libertários.”', 'Muitos libertários a leem, mas Rand desprezava o movimento e era contra o anarquismo. É uma filosofia própria, com metafísica e estética.'),
],
'ficcionalismo-moral': [
 ('“Ficcionalista é hipócrita: finge acreditar.”', 'Ele diz abertamente que a moral é uma ficção útil, como o dinheiro ou as regras de um jogo. A ficção é assumida, não escondida.'),
 ('“Se é ficção, por que seguir?”', 'Porque seguir funciona: coopera-se melhor, resiste-se à tentação. A pergunta é se a ficção se sustenta quando todos sabem que é ficção.'),
],
'epicurismo': [
 ('“Epicurista é glutão e devasso.”', 'Epicuro comia pão e queijo e dizia que os maiores prazeres são a amizade e a ausência de dor. O estereótipo vem de adversários antigos.'),
 ('“Epicurismo é egoísmo hedonista.”', 'A amizade, para Epicuro, era o maior bem, e sua comunidade admitia mulheres e escravos. O prazer buscado é tranquilo e compartilhado.'),
],
'sentimentalismo-moral': [
 ('“Se a moral vem do sentimento, é arbitrária.”', 'Hume e Smith falam de sentimentos corrigidos pelo espectador imparcial e pela simpatia ampla. Sentimentos refinados convergem; os brutos, não.'),
 ('“Sentimentalismo é emotivismo.”', 'Para o sentimentalista, os sentimentos são a fonte da moral, mas os juízos podem ser verdadeiros. O emotivista nega que sejam verdadeiros.'),
],
'jainismo': [
 ('“Jainismo é extremismo impraticável.”', 'Há dois níveis: monges seguem a não violência ao extremo; leigos seguem o possível, evitando dano desnecessário. A tradição tem cinco milênios de prática.'),
 ('“Ahimsa é só não matar.”', 'Inclui não ferir com palavras e pensamentos, e um dever ativo de compaixão. A não violência jainista influenciou Gandhi.'),
],
}
