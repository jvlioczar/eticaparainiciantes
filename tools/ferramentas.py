"""Dados das ferramentas interativas."""
# (slug, título, descrição, ícone)
FERR = [
 ('que-teoria-e-essa', 'Que teoria é essa?', 'Doze frases, seis famílias. Reconheça o ponto focal de cada argumento.', 'arvore'),
 ('fato-ou-valor', 'Fato ou valor?', 'Treine separar o que se discute com argumento moral do que se checa com evidência.', 'valor'),
 ('dilema-do-bonde', 'O bonde, caso a caso', 'Responda às variantes do dilema e veja que padrão suas respostas revelam.', 'bonde'),
 ('meu-circulo-moral', 'Monte o seu círculo moral', 'Marque quem conta para você e descubra o nome da sua posição.', 'circulo'),
 ('teste-de-troca', 'Teste de troca', 'Você julgaria o mesmo ato se o autor fosse do outro grupo?', 'troca'),
]

# Que teoria é essa? (frase, resposta, explicação)
TEORIAS_OPS = ['Consequencialismo', 'Deontologia', 'Ética das virtudes', 'Ética do cuidado', 'Contratualismo', 'Relativismo']
FRASES_TEORIA = [
 ('“Não importa quem fez: se o resultado foi menos gente sofrendo, foi a decisão certa.”', 'Consequencialismo', 'O ponto focal é o resultado para os afetados.'),
 ('“Há coisas que não se fazem com uma pessoa, nem que o mundo inteiro ganhe com isso.”', 'Deontologia', 'Restrições que não entram na conta: cada pessoa é um fim.'),
 ('“Antes de decidir, pergunto que tipo de pessoa essa escolha me torna.”', 'Ética das virtudes', 'O foco está no caráter do agente.'),
 ('“O que ela precisa agora? Não adianta princípio nenhum se eu não presto atenção nela.”', 'Ética do cuidado', 'Atenção e resposta à necessidade concreta de quem é vulnerável.'),
 ('“Uma regra é justa se eu a aceitaria sem saber em que lugar da sociedade eu cairia.”', 'Contratualismo', 'O véu da ignorância, de Rawls.'),
 ('“Quem somos nós para julgar? Na cultura deles isso é normal.”', 'Relativismo', 'Certo e errado como dependentes da cultura de quem age.'),
 ('“Mentir é errado porque trata o outro como alguém que não merece decidir com a verdade.”', 'Deontologia', 'A fórmula kantiana da humanidade como fim.'),
 ('“Prefiro a política que tira mais gente da miséria, mesmo que incomode alguns princípios.”', 'Consequencialismo', 'O resultado para quem está pior pesa mais do que a regra.'),
 ('“Uma pessoa honesta não é a que despeja verdades, é a que acha o jeito verdadeiro e gentil de falar.”', 'Ética das virtudes', 'A virtude como acerto, no meio-termo entre dois vícios.'),
 ('“Um princípio que impõe um custo enorme a uma pessoa pode ser rejeitado por ela, mesmo que beneficie milhões.”', 'Contratualismo', 'A versão de Scanlon: objeções individuais, não somadas.'),
 ('“A moral começa quando alguém troca a fralda de um bebê, não quando adultos negociam regras.”', 'Ética do cuidado', 'A dependência como ponto de partida da vida moral.'),
 ('“Cada época tem a sua moral, e a nossa não é melhor que a deles, só diferente.”', 'Relativismo', 'Nega que se possa falar em progresso moral.'),
]

# Fato ou valor? (frase, resposta, explicação)
FRASES_FV = [
 ('Peixes têm nociceptores e respondem a analgésicos.', 'Fato', 'É uma afirmação empírica, que a biologia confere.'),
 ('Causar sofrimento a um animal sem necessidade é errado.', 'Valor', 'É um juízo moral: pede argumento, não só dados.'),
 ('A maioria das pessoas doa menos de 1% da renda.', 'Fato', 'É um dado, checável em pesquisas.'),
 ('Quem tem muito deve ajudar quem tem pouco.', 'Valor', 'É uma afirmação sobre dever.'),
 ('Mentir destrói a confiança quando vira hábito.', 'Fato', 'É uma previsão sobre efeitos, testável pela experiência.'),
 ('Cada pessoa tem o direito de não ser usada como meio.', 'Valor', 'É um princípio moral, o de Kant.'),
 ('Penas mais longas não reduzem a reincidência de forma consistente.', 'Fato', 'É uma afirmação empírica, que estudos criminológicos avaliam.'),
 ('A punição deve ser proporcional ao merecimento, não só à prevenção.', 'Valor', 'É uma posição sobre justiça: o retributivismo.'),
 ('Pessoas que acabaram de comer carne atribuem menos mente aos animais.', 'Fato', 'É um achado experimental, da psicologia.'),
 ('Interesses iguais devem receber consideração igual, seja de quem forem.', 'Valor', 'É o princípio de Singer, um juízo moral.'),
 ('Cerca de 80 bilhões de animais terrestres são abatidos por ano.', 'Fato', 'É uma estimativa estatística, da FAO.'),
 ('O sofrimento extremo não pode ser compensado por nenhum prazer.', 'Valor', 'É a tese do utilitarismo negativo, um juízo sobre valor.'),
]

# Teste de troca: (cena com {a}, opção A, opção B, autor admirado, autor rejeitado)
TROCA = [
 ('{a} mentiu em público para proteger a reputação de um aliado. Isso é…', 'Inaceitável', 'Compreensível no contexto', 'Alguém que você admira', 'Alguém que você rejeita'),
 ('{a} defende que a pena de um crime grave deve ser reduzida porque o réu teve uma infância terrível. Isso é…', 'Justo', 'Desculpa para o crime', 'Um pensador do seu lado político', 'Um pensador do lado oposto'),
 ('{a} come carne, embora diga que o sofrimento animal importa. Isso é…', 'Incoerência grave', 'Normal, todo mundo tem contradições', 'Um amigo seu', 'Um crítico seu'),
 ('{a} doou 10% da renda para organizações de caridade e falou disso em público. Isso é…', 'Admirável', 'Exibicionismo', 'Alguém da sua religião ou grupo', 'Alguém de um grupo que você não gosta'),
 ('{a} mudou de posição sobre um tema moral depois de ler novos argumentos. Isso é…', 'Sinal de honestidade', 'Sinal de fraqueza', 'Um líder que você apoia', 'Um líder que você critica'),
 ('{a} recusou-se a mentir, e com isso um amigo perdeu uma oportunidade. Isso é…', 'Integridade', 'Rigidez cruel', 'Alguém que você admira', 'Alguém que você rejeita'),
 ('{a} diz que os interesses dos compatriotas devem vir antes dos de estrangeiros. Isso é…', 'Razoável', 'Preconceito', 'Alguém do seu país', 'Alguém de outro país falando do dele'),
]

# O bonde, caso a caso
BONDE = [
 dict(n='O desvio', cena='Um bonde desgovernado vai matar cinco pessoas. Você pode acionar uma alavanca e desviá-lo para outro trilho, onde há uma pessoa.', sim='Aciono a alavanca', nao='Não aciono', pct='Cerca de 80 a 90% das pessoas acionam.',
  teorias=[['utilitarismo-classico', 'Utilitarismo', 'Acione: cinco vidas valem mais do que uma.'], ['doutrina-do-duplo-efeito', 'Duplo efeito', 'Permitido: a morte do um é efeito colateral.'], ['deontologia-absolutista', 'Absolutismo', 'Alguns dizem não: acionar é matar; não acionar é deixar morrer.'], ['contratualismo-rawlsiano', 'Contratualismo', 'Sem saber que posição ocuparia, você aceitaria a regra de desviar.']]),
 dict(n='A passarela', cena='O mesmo bonde vai matar cinco. Você está em uma passarela ao lado de um homem grande. Se o empurrar, o corpo dele para o bonde e salva os cinco. Ele morre.', sim='Empurro', nao='Não empurro', pct='Só 10 a 20% empurram, embora o resultado seja igual ao do desvio.',
  teorias=[['consequencialismo-de-ato', 'Consequencialismo de ato', 'Empurre: o resultado é o mesmo do desvio.'], ['deontologia-kantiana', 'Kant', 'Não: você usaria uma pessoa apenas como meio.'], ['doutrina-do-duplo-efeito', 'Duplo efeito', 'Proibido: a morte é o meio.'], ['etica-do-cuidado', 'Cuidado', 'Recusa o enquadramento: pessoas não são números em trilhos.']]),
 dict(n='O alçapão', cena='Como na passarela, mas você não precisa tocar no homem: basta acionar uma alavanca que abre um alçapão sob ele, e ele cai no trilho, parando o bonde.', sim='Aciono a alavanca', nao='Não aciono', pct='Mais pessoas aceitam do que na passarela, mas menos do que no desvio. O contato físico pesa, mesmo que não devesse.',
  teorias=[['consequencialismo-de-ato', 'Consequencialismo de ato', 'Acione: mesmo resultado.'], ['deontologia-kantiana', 'Kant', 'Não: ele continua sendo usado como meio, com ou sem contato.'], ['etica-das-virtudes', 'Virtudes', 'Se a sua resposta mudou em relação à passarela, pergunte por quê: a diferença é moral ou só de distância?']]),
 dict(n='O laço', cena='Você pode desviar o bonde para um trilho em forma de laço, que volta ao trilho principal. Nesse laço há um homem grande; só o corpo dele impede o bonde de completar o laço e matar os cinco.', sim='Desvio', nao='Não desvio', pct='A maioria desvia, mas menos do que no desvio simples: aqui o corpo do homem é necessário para salvar os cinco.',
  teorias=[['doutrina-do-duplo-efeito', 'Duplo efeito', 'Difícil: a morte parece ser o meio, como na passarela, mas o ato é uma alavanca, como no desvio.'], ['utilitarismo-classico', 'Utilitarismo', 'Desvie: a conta não mudou.'], ['deontologia-de-direitos', 'Direitos', 'Thomson usou este caso para mostrar que “usar como meio” não explica tudo: aqui você usa o homem e a maioria aceita.']]),
 dict(n='O transplante', cena='Cinco pacientes vão morrer sem transplantes. Um visitante saudável e compatível está no hospital. O cirurgião pode matá-lo discretamente e salvar os cinco. Ninguém saberia.', sim='O cirurgião deve fazer isso', nao='Não deve', pct='Quase ninguém aceita, mesmo com o segredo garantido.',
  teorias=[['consequencialismo-de-ato', 'Consequencialismo de ato', 'Em princípio sim, se ninguém soubesse. É o caso mais difícil para a teoria.'], ['consequencialismo-de-regras', 'Consequencialismo de regras', 'Não: uma regra que permite isso destruiria a confiança na medicina.'], ['deontologia-de-direitos', 'Direitos', 'Não: o direito à vida é um trunfo.'], ['contratualismo-escanloniano', 'Scanlon', 'Não: o visitante pode rejeitar razoavelmente qualquer princípio que permita isso.']]),
 dict(n='O bonde e os animais', cena='O bonde vai matar cinco cães presos no trilho. Você pode desviá-lo para outro trilho, onde há um cão. Nenhum humano está envolvido.', sim='Aciono a alavanca', nao='Não aciono', pct='A maioria aciona. Se a sua resposta mudou em relação ao desvio com humanos, vale perguntar o que mudou.',
  teorias=[['sencientismo', 'Sencientismo', 'Acione, pela mesma razão do caso humano: quem sente conta, e cinco são mais do que um.'], ['antropocentrismo', 'Antropocentrismo', 'Não há dever moral direto em jogo; só o que a escolha diz sobre você.'], ['gradualismo', 'Gradualismo', 'Acione: os cães contam, ainda que com peso menor do que humanos.']]),
]
