"""Dados das ferramentas acrescentadas em novembro de 2026: véu da ignorância, quem disse?, equilíbrio reflexivo."""
FERR2 = [
 ('veu-da-ignorancia', 'Simulador do véu da ignorância', 'Escolha as regras de uma sociedade sem saber quem você será nela. Depois, descubra.', 'ponto'),
 ('quem-disse', 'Quem disse?', 'Dezesseis ideias, dezesseis filósofos. Ligue cada tese a quem a defendeu.', 'pessoa'),
 ('equilibrio-reflexivo', 'Exercício de equilíbrio reflexivo', 'Julgue casos, escolha um princípio e veja onde seus juízos e seu princípio se contradizem.', 'lampada'),
]

# véu da ignorância: cada "sociedade" tem posições com bem-estar (0 a 100) e a chance de nascer em cada uma
VEU = dict(
 sociedades=[
  dict(n='Sociedade A: máxima soma', d='A riqueza total é a maior, mas concentrada. Pouca proteção para quem fica embaixo.', pos=[('Muito rico', 100, 5), ('Classe média alta', 80, 15), ('Classe média', 55, 30), ('Pobre', 20, 35), ('Miserável', 3, 15)]),
  dict(n='Sociedade B: mínimo garantido', d='Ninguém fica abaixo de um piso; a riqueza total é um pouco menor e o topo, mais baixo.', pos=[('Muito rico', 75, 5), ('Classe média alta', 65, 15), ('Classe média', 55, 30), ('Pobre', 40, 35), ('Miserável', 35, 15)]),
  dict(n='Sociedade C: igualdade estrita', d='Todos recebem o mesmo. A riqueza total é a menor, porque há menos incentivo.', pos=[('Muito rico', 45, 5), ('Classe média alta', 45, 15), ('Classe média', 45, 30), ('Pobre', 45, 35), ('Miserável', 45, 15)]),
  dict(n='Sociedade D: prioridade ao pior', d='Desigualdade permitida só quando melhora quem está pior. O topo é alto, o piso é o mais alto de todos.', pos=[('Muito rico', 85, 5), ('Classe média alta', 70, 15), ('Classe média', 58, 30), ('Pobre', 45, 35), ('Miserável', 40, 15)]),
 ],
 especies=[('Humano', 60), ('Cão de companhia', 20), ('Vaca de leite', 8), ('Frango de granja', 10), ('Peixe de criação', 2)],
 bem_esp={'Humano': None, 'Cão de companhia': 70, 'Vaca de leite': 25, 'Frango de granja': 8, 'Peixe de criação': 10},
)

# quem disse? (tese, filósofo, explicação)
QUEM_OPS = ['Aristóteles', 'Kant', 'Bentham', 'Mill', 'Hume', 'Rawls', 'Nozick', 'Singer', 'Parfit', 'Gilligan', 'Mackie', 'Anscombe', 'Regan', 'Scanlon', 'Mozi', 'Sidgwick']
QUEM = [
 ('“A pergunta não é se podem raciocinar, nem se podem falar, mas se podem sofrer.”', 'Bentham', 'Bentham, em 1789, sobre os animais: a senciência como critério.'),
 ('“Aja só segundo uma máxima que possas querer que se torne lei universal.”', 'Kant', 'A primeira fórmula do imperativo categórico, na Fundamentação de 1785.'),
 ('“A razão é, e só deve ser, escrava das paixões.”', 'Hume', 'Hume, no Tratado: a razão sozinha não motiva.'),
 ('A virtude é um meio-termo entre dois vícios, adquirido pelo hábito.', 'Aristóteles', 'A Ética a Nicômaco: a coragem entre a covardia e a temeridade.'),
 ('Imagine escolher as regras da sociedade sem saber que posição você ocupará nela.', 'Rawls', 'O véu da ignorância, em Uma Teoria da Justiça (1971).'),
 ('“É melhor ser Sócrates insatisfeito do que um tolo satisfeito.”', 'Mill', 'Mill, em Utilitarismo: prazeres superiores e inferiores.'),
 ('Se você vê uma criança se afogando em um lago raso, deve salvá-la mesmo que estrague seus sapatos; e o mesmo vale para a criança distante.', 'Singer', 'Fome, Riqueza e Moralidade (1972).'),
 ('Direitos são restrições laterais: limites ao que qualquer um pode fazer em busca de qualquer meta.', 'Nozick', 'Anarquia, Estado e Utopia (1974).'),
 ('Um mundo imenso de vidas quase sem valor seria melhor do que um mundo pequeno de vidas excelentes, pela soma. Isso é repugnante.', 'Parfit', 'A conclusão repugnante, em Reasons and Persons (1984).'),
 ('Há uma voz moral diferente, a do cuidado, que a escala de Kohlberg media como imaturidade.', 'Gilligan', 'Uma Voz Diferente (1982).'),
 ('Todos os juízos morais são falsos: eles pretendem descrever fatos objetivos que não existem.', 'Mackie', 'A teoria do erro, em Ética: Inventando o Certo e o Errado (1977).'),
 ('A filosofia moral moderna deveria abandonar a noção de “obrigação” e voltar às virtudes e ao florescimento.', 'Anscombe', 'Modern Moral Philosophy (1958), que reabriu a ética das virtudes.'),
 ('Todo sujeito de uma vida tem valor inerente igual, e por isso direitos que proíbem usá-lo como recurso.', 'Regan', 'The Case for Animal Rights (1983).'),
 ('Um ato é errado se é proibido por princípios que ninguém poderia razoavelmente rejeitar.', 'Scanlon', 'O Que Devemos Uns aos Outros (1998).'),
 ('Os males do mundo vêm da parcialidade; a cura é cuidar de todos igualmente, e julgar práticas pelo benefício.', 'Mozi', 'O moísmo, na China do século V a.C.'),
 ('O ponto de vista do universo: o bem de qualquer pessoa não importa mais do que o bem de qualquer outra.', 'Sidgwick', 'Os Métodos da Ética (1874).'),
]

# equilíbrio reflexivo: casos (texto, chave do juízo), princípios (nome, o que implica para cada caso)
ER_CASOS = [
 dict(k='bonde', t='Desviar um bonde para matar uma pessoa em vez de cinco.', sim='Aceitável', nao='Inaceitável'),
 dict(k='passarela', t='Empurrar um homem da passarela para parar o bonde e salvar cinco.', sim='Aceitável', nao='Inaceitável'),
 dict(k='transplante', t='Um cirurgião matar um visitante saudável para salvar cinco com seus órgãos, sem que ninguém saiba.', sim='Aceitável', nao='Inaceitável'),
 dict(k='mentira', t='Mentir a um assassino sobre onde está a pessoa que ele procura.', sim='Aceitável', nao='Inaceitável'),
 dict(k='doar', t='Gastar com um jantar caro um valor que, doado, salvaria uma vida.', sim='Aceitável', nao='Inaceitável'),
 dict(k='frango', t='Confinar frangos a vida inteira em gaiolas para que a carne fique mais barata.', sim='Aceitável', nao='Inaceitável'),
 dict(k='cao', t='Confinar cães a vida inteira em gaiolas para que a carne fique mais barata.', sim='Aceitável', nao='Inaceitável'),
 dict(k='promessa', t='Quebrar uma promessa a um amigo para socorrer um desconhecido ferido.', sim='Aceitável', nao='Inaceitável'),
]
ER_PRINCIPIOS = [
 dict(n='Consequencialismo de ato: o certo é o que produz o melhor resultado, caso a caso.', pred=dict(bonde='sim', passarela='sim', transplante='sim', mentira='sim', doar='nao', frango='nao', cao='nao', promessa='sim')),
 dict(n='Deontologia de direitos: nunca use uma pessoa apenas como meio; direitos vencem resultados.', pred=dict(bonde='sim', passarela='nao', transplante='nao', mentira='sim', doar='sim', frango='sim', cao='sim', promessa='sim')),
 dict(n='Absolutismo: não matar, não mentir, não quebrar promessas, sem exceção.', pred=dict(bonde='nao', passarela='nao', transplante='nao', mentira='nao', doar='sim', frango='sim', cao='sim', promessa='nao')),
 dict(n='Sencientismo com restrições: quem sente conta igual; não use pessoas como meio; ajude quando o custo é pequeno.', pred=dict(bonde='sim', passarela='nao', transplante='nao', mentira='sim', doar='nao', frango='nao', cao='nao', promessa='sim')),
 dict(n='Antropocentrismo com restrições: só humanos contam diretamente; não use pessoas como meio.', pred=dict(bonde='sim', passarela='nao', transplante='nao', mentira='sim', doar='sim', frango='sim', cao='sim', promessa='sim')),
]
ER_PARES = [('frango', 'cao', 'Você julgou de forma diferente o confinamento de frangos e de cães. Qual diferença entre eles justifica isso? A espécie, por si, é um traço como a cor.'), ('bonde', 'passarela', 'Você aceitou desviar e recusou empurrar, com o mesmo número de mortos. A diferença costuma ser “usar alguém como meio”. Se é ela, veja se vale também no transplante.'), ('passarela', 'transplante', 'Você julgou a passarela e o transplante de forma diferente, embora a estrutura seja a mesma: matar um para salvar cinco usando o corpo dele. O que mudou?')]
