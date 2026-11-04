"""Trilhas de estudo e os três casos-fio do curso."""
TRILHAS = [
 dict(s='duas-horas', n='Ética em duas horas', d='O essencial para entender qualquer discussão moral: as perguntas, as famílias de teorias, quem conta e como discutir.', tempo='2 horas',
      licoes=['o-que-e-etica', 'fatos-e-valores', 'mapa-das-teorias', 'consequencialismo', 'deontologia', 'etica-do-carater', 'circulo-moral', 'imparcialidade', 'como-discutir-etica']),
 dict(s='etica-animal', n='Ética animal, do critério à prática', d='Por que a senciência é o critério, o que é especismo, onde o sofrimento se concentra e o que uma pessoa pode fazer.', tempo='3 horas',
      licoes=['circulo-moral', 'expansao-do-circulo-moral', 'imparcialidade', 'senciencia', 'especismo', 'gradualismo', 'etica-animal-na-pratica', 'sofrimento-dos-animais-selvagens', 'animais-e-a-politica', 'fraqueza-de-vontade']),
 dict(s='discutir', n='Para quem vai discutir', d='Argumentos, vieses, tribalismo e abertura: o kit para discutir ética sem brigar e sem se enganar.', tempo='2 horas',
      licoes=['fatos-e-valores', 'argumentos-morais', 'como-discutir-etica', 'perguntas-frequentes', 'vieses-morais', 'tribalismo-moral', 'etica-da-crenca', 'abertura-moral']),
 dict(s='mente-moral', n='A mente moral', d='Como julgamos de fato: psicologia, emoções, situação, vontade e responsabilidade.', tempo='3 horas',
      licoes=['psicologia-moral', 'emocoes-morais', 'situacionismo-e-experimentos', 'vieses-morais', 'fraqueza-de-vontade', 'livre-arbitrio-e-responsabilidade', 'educacao-moral', 'motivacao-moral']),
 dict(s='politica', n='Da ética à política', d='O que cada política pressupõe, pobreza, economia, exploração, responsabilidade coletiva e como levar a ética ao debate público.', tempo='3 horas',
      licoes=['igualdade-humana', 'parcialidade-e-deveres-especiais', 'somar-priorizar-ou-garantir', 'pobreza-e-etica-global', 'economia-politica-e-etica', 'exploracao', 'responsabilidade-coletiva', 'da-etica-a-politica']),
 dict(s='metaetica', n='Metaética e fundamentos', d='O que é um juízo moral: realismo, antirrealismo, relativismo, evolução, conhecimento e motivação.', tempo='3 horas',
      licoes=['fatos-e-valores', 'o-que-e-metaetica', 'realismo-moral', 'antirrealismo-moral', 'relativismo-e-quietismo', 'evolucao-e-moral', 'epistemologia-moral', 'motivacao-moral']),
 dict(s='futuro', n='Futuro, risco e incerteza', d='Gerações futuras, população, riscos existenciais e de sofrimento, e como decidir sem certeza.', tempo='3 horas',
      licoes=['geracoes-futuras', 'etica-populacional', 'riscos-s-e-riscos-x', 'catastrofes-morais', 'incerteza-moral', 'teoria-da-decisao-e-etica', 'probabilidade-e-etica', 'etica-climatica']),
]

# os três casos que atravessam o curso: (slug, nome, descrição)
CASOS_FIO = [
 ('lago', 'A criança no lago', 'Você passa por um lago raso onde uma criança se afoga. Salvar custa seus sapatos. E a criança distante, que o mesmo dinheiro salvaria?'),
 ('frango', 'O frango de granja', 'Um frango passa a vida em um galpão lotado e morre aos 42 dias. É barato, é legal, é o que quase todos comem.'),
 ('promessa', 'A promessa ao moribundo', 'Você prometeu a um amigo, no leito de morte, entregar o dinheiro dele a um clube de golfe. Um hospital infantil precisa do mesmo valor. Ninguém saberá.'),
]
# o que cada família responde a cada caso, em cada nível: {nivel: [(família, resposta ao lago, ao frango, à promessa), ...]}
RESPOSTAS_FIO = {
'iniciante': [
 ('Consequencialismo', 'Salve, nos dois casos: o custo é pequeno e o bem é enorme. A distância não muda a conta.', 'Conta o sofrimento do frango; se ele é grande e a alternativa é fácil, a conta pesa contra.', 'Dê ao hospital: o resultado é melhor, e ninguém é prejudicado pela quebra.'),
 ('Deontologia', 'Salve a criança do lago: é um dever claro. Ajudar a distante é um dever imperfeito: devido, mas com margem.', 'Depende de o frango ter direitos; na deontologia clássica, deveres com animais são indiretos, e isso é criticado.', 'Cumpra a promessa: prometer cria um dever, e o resultado não o cancela.'),
 ('Caráter e cuidado', 'Uma pessoa compassiva salva, e não precisa de cálculo. Para a distante, a compaixão também alcança, mas com menos força.', 'Uma pessoa compassiva não ignora um sofrimento que paga para existir.', 'Lealdade ao amigo contra compaixão pelas crianças: a sabedoria prática decide, e o resíduo fica.'),
 ('Contratualismo', 'Ninguém poderia rejeitar um princípio que exige salvar com custo pequeno; a distância pede regras, não heroísmo.', 'O frango não participa do contrato; a extensão do véu à espécie muda a resposta.', 'Princípios sobre promessas são aceitos por todos; a exceção para o bem maior também, se rara e grave.'),
 ('Círculo moral', 'A criança distante conta tanto quanto a do lago: o lugar não é critério.', 'O frango conta se sente; a espécie não é critério.', 'O amigo morto conta ainda? As crianças do hospital contam com certeza.'),
],
'intermediario': [
 ('Consequencialismo', 'Singer: nenhuma diferença (distância, número de salvadores, incerteza) é moralmente relevante. A objeção da exigência responde que há um teto; o consequencialismo satisfatório o fixa.', 'O utilitarismo de ato condena a compra pelo valor esperado; o de regras, pela prática. A substituibilidade (matar e repor) é a objeção interna mais incômoda.', 'O consequencialismo de regras cumpre a promessa, porque a prática vale mais do que o caso; o de ato dá ao hospital.'),
 ('Deontologia', 'Kant: beneficência é dever imperfeito; Pogge transforma o caso distante em dever negativo (não sustentar regras que empobrecem).', 'Regan: o frango é sujeito de uma vida e tem direito a não ser usado como recurso. Kant original: só deveres indiretos.', 'Ross: fidelidade e beneficência são deveres prima facie; o juízo pesa. O absolutista cumpre; o de limiar hesita.'),
 ('Caráter e cuidado', 'A ética do cuidado começa perto e precisa da imparcialidade para alcançar a criança distante.', 'O cuidado alcança o animal em relação de dependência; a virtude da justiça alcança o que não se vê.', 'A lealdade é virtude, e a sabedoria prática sabe quando ela cede; o pesar depois é adequado.'),
 ('Contratualismo', 'Scanlon: o princípio “ajude quando o custo é pequeno” não é razoavelmente rejeitável; a versão para distantes é institucional.', 'Rowlands: sob um véu que esconde a espécie, ninguém aceita a criação industrial.', 'Um princípio que permita quebrar promessas por qualquer bem maior seria rejeitado; um que permita em casos graves e raros, não.'),
 ('Mente e moral', 'A vítima identificável explica por que salvamos no lago e não à distância; é viés, não razão.', 'A dissonância explica por que quem condena continua comprando; a fraqueza de vontade não é hipocrisia.', 'A promessa pesa mais quando o amigo tinha rosto; o hospital é estatística.'),
],
'avancado': [
 ('Consequencialismo', 'Com incerteza, o valor esperado da doação eficaz continua alto; a questão aberta é a exigência, e Scheffler responde com prerrogativas.', 'A ética focada no sofrimento vê aqui a maior quantidade de dor evitável do mundo; a conclusão repugnante e a substituibilidade são o custo teórico de somar.', 'Dano póstumo: se interesses sobrevivem ao sujeito, quebrar a promessa lesa o amigo; o peso é finito e cede a necessidades sérias.'),
 ('Deontologia', 'A distinção fazer/permitir protege quem não salva; o viés de omissão a infla. O dever de não prejudicar pelas regras do comércio é o caminho de Pogge.', 'Direitos de limiar: o dano ao frango é certo e grave, e nenhum limiar o justifica; a dúvida é o peso relativo da dor dele.', 'O dever de fidelidade não desaparece com a morte do credor; deontologistas discordam sobre se um bem grande o vence.'),
 ('Círculo e metaética', 'A distância no espaço e no tempo não altera o peso de um interesse (atemporalismo); o realista diz que isso é um fato; o quase-realista, uma atitude estável.', 'Senciência provável e peso igual para dor igual; o gradualista discute o que a morte tira, não o peso da dor.', 'As preferências do morto testam o preferencialismo: contam se desejos incondicionais podem ser frustrados sem sujeito.'),
 ('Decidir sem certeza', 'Sob incerteza moral, a maioria das teorias manda salvar nos dois casos; a cobertura de riscos favorece doar parte regular.', 'Mesmo com 50% de dúvida sobre o sofrimento, o valor esperado condena a prática; o parlamento moral concorda.', 'A maioria das teorias cumpre promessas comuns e quebra as que custam vidas; a escolha esperada segue a maioria.'),
 ('Progresso e abertura', 'A expansão do círculo chegou ao estrangeiro; a criança distante é o teste de se chegou mesmo.', 'Candidata a catástrofe moral em curso: normal, legal e invisível, como as anteriores.', 'O que você faria se ninguém soubesse é o anel de Giges; a resposta diz se a moral vale por si.'),
],
}
