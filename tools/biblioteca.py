"""Livros e sites. LIVROS: (título, autor, descrição, seção, url). Seções em SECOES_L, com descrição. SITES: (nome, url, descrição, grupo, âmbito)."""
from urllib.parse import quote
def b(t, a, d, n, u=None): return (t, a, d, n, u or 'https://www.google.com/search?tbm=bks&q=' + quote(t + ' ' + a))
INI, INTM, AVA, EXP, AEF, BIO = 'Iniciante', 'Intermediário', 'Avançado', 'Ética expandida', 'Altruísmo eficaz, vontade e futuro', 'Bioética'
SECOES_L = [
 (INI, 'Para começar: leitura acessível, sem exigir formação prévia.'),
 (INTM, 'Os clássicos legíveis e os livros que mudaram o debate.'),
 (AVA, 'Obras acadêmicas: pedem mais tempo e, às vezes, um guia de leitura.'),
 (EXP, 'Sobre a expansão do círculo moral: animais, gerações futuras e outros seres que a ética tradicional deixou de fora.'),
 (AEF, 'Fazer o bem com evidência, sustentar a vontade e pensar o longo prazo.'),
 (BIO, 'Ética da medicina e da pesquisa com seres humanos.'),
]
LIVROS = [
 # iniciante
 b('Os Elementos da Filosofia Moral', 'James Rachels e Stuart Rachels', 'A introdução mais usada no mundo: relativismo, egoísmo, utilitarismo, Kant, virtudes, com casos reais.', INI),
 b('Ética: Uma Brevíssima Introdução', 'Simon Blackburn', 'Curto e claro, cobre as ameaças à ética (relativismo, egoísmo), os fundamentos e as teorias.', INI),
 b('Justiça: O Que É Fazer a Coisa Certa', 'Michael Sandel', 'As grandes teorias aplicadas a casos atuais, no estilo do curso de Harvard.', INI),
 b('Ética Prática', 'Peter Singer', 'Aplica a ética a pobreza, animais, aborto, eutanásia e meio ambiente, com o princípio da igual consideração de interesses.', INI),
 b('Quanto Custa Salvar uma Vida?', 'Peter Singer', 'A criança no lago estendida: o que podemos fazer pela pobreza extrema (The Life You Can Save).', INI),
 b('A Mente Moralista', 'Jonathan Haidt', 'Por que boas pessoas se dividem por política e religião: intuição, fundamentos morais e tribalismo.', INI),
 # intermediário
 b('Utilitarismo', 'John Stuart Mill', 'A defesa clássica, curta e legível, da maior felicidade para o maior número (1863).', INTM),
 b('Fundamentação da Metafísica dos Costumes', 'Immanuel Kant', 'O texto em que Kant formula o imperativo categórico (1785). Denso, mas curto.', INTM),
 b('Ética a Nicômaco', 'Aristóteles', 'O texto fundador da ética das virtudes: eudaimonia, meio-termo, amizade. O livro VII trata da fraqueza de vontade.', INTM),
 b('Uma Voz Diferente', 'Carol Gilligan', 'O livro que fundou a ética do cuidado, a partir da crítica a Kohlberg.', INTM),
 b('Depois da Virtude', 'Alasdair MacIntyre', 'A crítica à moral moderna e a defesa das virtudes em tradições.', INTM),
 b('Moral Tribes', 'Joshua Greene', 'A psicologia do bonde: dois sistemas na mente moral e o que fazer com eles.', INTM),
 b('The Point of View of the Universe', 'Katarzyna de Lazari-Radek e Peter Singer', 'Sidgwick revisitado: utilitarismo, evolução e a defesa da imparcialidade.', INTM),
 b('Reasoned Politics', 'Magnus Vinding', 'Valores primeiro, evidências depois: a ética focada no sofrimento levada à política. Gratuito em PDF.', INTM, 'https://magnusvinding.com/wp-content/uploads/2022/03/reasoned-politics.pdf'),
 # avançado
 b('A Teoria dos Sentimentos Morais', 'Adam Smith', 'A moral fundada na simpatia e no “espectador imparcial”, pelo autor que antes de economista foi filósofo moral (1759).', AVA),
 b('Uma Introdução aos Princípios da Moral e da Legislação', 'Jeremy Bentham', 'Obra fundadora do utilitarismo (1789): leis julgadas pelo prazer e pela dor que causam, com a pergunta sobre os animais: podem sofrer?', AVA),
 b('Os Métodos da Ética', 'Henry Sidgwick', 'A formulação mais rigorosa do utilitarismo (1874) e o dualismo da razão prática.', AVA, 'https://www.gutenberg.org/ebooks/46743'),
 b('Principia Ethica', 'G. E. Moore', 'O argumento da questão em aberto e o não naturalismo (1903).', AVA),
 b('The Right and the Good', 'W. D. Ross', 'Os deveres prima facie e o intuicionismo (1930).', AVA),
 b('The Language of Morals', 'R. M. Hare', 'O prescritivismo: juízos morais como prescrições universalizáveis (1952).', AVA),
 b('Freedom and Reason', 'R. M. Hare', 'A universalização levada a sério, e o problema do fanático (1963).', AVA),
 b('Uma Teoria da Justiça', 'John Rawls', 'O véu da ignorância, os dois princípios e a crítica ao utilitarismo (1971).', AVA),
 b('Anarquia, Estado e Utopia', 'Robert Nozick', 'Direitos como restrições laterais, o monstro utilitário e a máquina de experiências (1974).', AVA),
 b('Ethics: Inventing Right and Wrong', 'J. L. Mackie', 'A teoria do erro: os argumentos da relatividade e da estranheza (1977).', AVA),
 b('Razões e Pessoas', 'Derek Parfit', 'Identidade pessoal, ética populacional, a conclusão repugnante e o problema da não identidade (1984).', AVA),
 b('What We Owe to Each Other', 'T. M. Scanlon', 'O contratualismo da justificabilidade a cada pessoa (1998).', AVA),
 b('Ruling Passions', 'Simon Blackburn', 'A defesa sistemática do quase-realismo (1998).', AVA),
 b('On What Matters', 'Derek Parfit', 'A tentativa de mostrar que kantianos, contratualistas e consequencialistas convergem; realismo não naturalista (2011).', AVA),
 b('Justice for Hedgehogs', 'Ronald Dworkin', 'A unidade do valor e o quietismo: perguntas morais só se respondem com argumentos morais (2011).', AVA),
 b('The Evolution of Moral Progress', 'Allen Buchanan e Russell Powell', 'Uma teoria do progresso moral informada pela biologia e pela história (2018).', AVA),
 # ética expandida
 b('Human Society in Ethics and Politics', 'Bertrand Russell', 'A ética fundada em desejos e sentimentos, e o que ela pede da sociedade (1954).', EXP),
 b('Libertação Animal', 'Peter Singer', 'O livro que fundou o movimento moderno pelos animais (1975): especismo, criação industrial e o que fazer.', EXP),
 b('The Expanding Circle', 'Peter Singer', 'Evolução, ética e a expansão do círculo de quem conta (1981).', EXP),
 b('The Case for Animal Rights', 'Tom Regan', 'A defesa deontológica dos direitos animais (1983): todo sujeito de uma vida tem valor inerente.', EXP),
 b('Created from Animals', 'James Rachels', 'As implicações morais do darwinismo: sem a ideia de que os humanos são especiais por natureza (1990).', EXP),
 b('Justice between Age Groups and Generations', 'Peter Laslett e James S. Fishkin (org.)', 'O que devemos às gerações futuras e entre faixas etárias (1992).', EXP),
 b('Animal Rights: A Philosophical Defence', 'Mark Rowlands', 'O véu da ignorância estendido à espécie: o contratualismo rawlsiano inclui os animais (1998).', EXP),
 b('Animals Like Us', 'Mark Rowlands', 'A mesma ideia, para o público geral.', EXP),
 b('Fellow Creatures: Our Obligations to the Other Animals', 'Christine Korsgaard', 'Uma kantiana mostra por que os animais são fins em si (2018).', EXP),
 b('Um Passo Adiante em Defesa dos Animais', 'Oscar Horta', 'Sencientismo, especismo e o sofrimento dos animais selvagens, em linguagem direta.', EXP),
 b('Justice for Animals', 'Martha Nussbaum', 'A abordagem das capacidades estendida aos animais, com crítica a Singer, Regan e Kant (2023).', EXP),
 b('The Edge of Sentience', 'Jonathan Birch', 'Precaução diante da incerteza sobre quem sente: animais, fetos, pacientes, inteligência artificial (2024). Acesso aberto.', EXP, 'https://academic.oup.com/book/57949'),
 b('Coleção Uma Jornada pela Ética Animal', 'Luciano Carlos Cunha', 'Introdução em português à ética animal, das questões clássicas ao sofrimento dos animais selvagens (2025).', EXP),
 b('The Moral Circle', 'Jeff Sebo', 'Quem deve ser incluído: animais, insetos, mentes artificiais, e como decidir sob incerteza (2025).', EXP),
 # altruísmo eficaz, vontade e futuro
 b('A Sociedade Aberta e seus Inimigos', 'Karl Popper', 'A defesa da sociedade aberta e a proposta de minimizar o sofrimento em vez de maximizar a felicidade (1945).', AEF),
 b('Moral Thinking', 'R. M. Hare', 'O utilitarismo de dois níveis: regras intuitivas no dia a dia, pensamento crítico nos casos difíceis (1981).', AEF),
 b('Backsliding: Understanding Weakness of Will', 'Alfred Mele', 'O que é a fraqueza de vontade, por que acontece e o que a filosofia e a psicologia dizem sobre ela (2012).', AEF),
 b('Doing Good Better', 'William MacAskill', 'O manifesto do altruísmo eficaz: evidência e razão para fazer o máximo de bem (2015).', AEF),
 b('Strangers Drowning', 'Larissa MacFarquhar', 'Retratos de pessoas que levam a moral ao extremo, e a pergunta sobre quanto é demais (2015).', AEF),
 b('The Precipice', 'Toby Ord', 'Os riscos existenciais deste século e por que proteger o futuro é a tarefa moral do nosso tempo (2020).', AEF),
 b('Moral Uncertainty', 'William MacAskill, Krister Bykvist e Toby Ord', 'Como agir sem saber qual teoria é a certa (2020). Gratuito em acesso aberto.', AEF, 'https://www.moraluncertainty.com/'),
 b('Suffering-Focused Ethics: Defense and Implications', 'Magnus Vinding', 'A defesa da prioridade ao sofrimento e suas implicações (2020). Gratuito.', AEF, 'https://magnusvinding.com/2020/05/31/suffering-focused-ethics-defense-and-implications/'),
 b('Avoiding the Worst: How to Prevent a Moral Catastrophe', 'Tobias Baumann', 'A primeira introdução sistemática aos riscos de sofrimento futuro (riscos S): o que são, por que priorizá-los e como reduzi-los (2022). Gratuito em PDF.', AEF, 'https://centerforreducingsuffering.org/research/avoiding-the-worst/'),
 # bioética
 b('Bioética: Ponte para o Futuro', 'Van Rensselaer Potter', 'O livro que cunhou o termo bioética (1971): a sobrevivência exige unir ciência e valores.', BIO),
 b('Princípios de Ética Biomédica', 'Tom L. Beauchamp e James F. Childress', 'Os quatro princípios, autonomia, beneficência, não maleficência e justiça, que organizam a bioética desde 1979.', BIO),
 b('A Vida Imortal de Henrietta Lacks', 'Rebecca Skloot', 'A história das células HeLa e da mulher de quem foram tiradas sem consentimento: um caso real de ética da pesquisa (2010).', BIO),
]
assert all(x[3] in {s for s, _ in SECOES_L} for x in LIVROS)
NAC, INT = 'Em português', 'Em inglês'
GRUPOS_S = ['Enciclopédias e referência', 'Ética animal e círculo moral', 'Ética prática e altruísmo', 'Testes e ferramentas']
S1, S2, S3, S4 = GRUPOS_S
SITES = [
 ('Stanford Encyclopedia of Philosophy', 'https://plato.stanford.edu/', 'A referência acadêmica mais confiável, com verbetes revisados por especialistas sobre cada teoria e autor.', S1, INT),
 ('Internet Encyclopedia of Philosophy', 'https://iep.utm.edu/', 'Verbetes mais acessíveis do que os da Stanford, revisados por pares.', S1, INT),
 ('PhilPapers', 'https://philpapers.org/', 'Índice de artigos de filosofia, com bibliografias organizadas por tema.', S1, INT),
 ('Crítica na Rede', 'https://criticanarede.com/', 'Revista de filosofia em português, com textos de ética acessíveis e traduções.', S1, NAC),
 ('Wikipédia em português: Ética', 'https://pt.wikipedia.org/wiki/%C3%89tica', 'Ponto de partida; confira as fontes de cada verbete.', S1, NAC),
 ('Utilitarianism.net', 'https://utilitarianism.net/', 'Introdução completa ao utilitarismo, com objeções e respostas, por Chappell, Meissner e MacAskill.', S1, INT),
 ('Animal Ethics (Ética Animal)', 'https://www.animal-ethics.org/pt/', 'Textos em português sobre senciência, especismo, teorias éticas e o sofrimento dos animais selvagens.', S2, NAC),
 ('Senciência e Ética', 'https://senciencia.org/', 'Projeto de Luciano Carlos Cunha: textos sobre ética animal, metaética, motivação moral e o sofrimento dos animais na natureza.', S2, NAC),
 ('EthicsNet', 'https://ethicsnet.org/', 'Organização sem fins lucrativos, desde 2016, que publica ferramentas e pesquisa abertas sobre alinhamento de IA e sobre o bem-estar de mentes artificiais: o que devemos aos sistemas que podem vir a ter interesses.', S2, INT),
 ('Sentientism', 'https://sentientism.info/', 'Site e podcast sobre o sencientismo: evidência, razão e compaixão por todos os seres sencientes.', S2, INT),
 ('Sentience Institute', 'https://www.sentienceinstitute.org/', 'Pesquisa sobre a expansão do círculo moral, incluindo animais e mentes artificiais.', S2, INT),
 ('Declaração de Nova York sobre Consciência Animal', 'https://sites.google.com/nyu.edu/nydeclaration/declaration', 'O texto de 2024 assinado por centenas de cientistas, com a lista de evidências.', S2, INT),
 ('Center for Reducing Suffering', 'https://centerforreducingsuffering.org/', 'Pesquisa sobre éticas focadas no sofrimento e prioridades para reduzi-lo.', S3, INT),
 ('The Life You Can Save', 'https://www.thelifeyoucansave.org/', 'A organização de Peter Singer: onde doar para salvar mais vidas por real.', S3, INT),
 ('GiveWell', 'https://www.givewell.org/', 'Avaliação rigorosa de organizações de caridade por custo-efetividade.', S3, INT),
 ('Animal Charity Evaluators', 'https://animalcharityevaluators.org/', 'Avaliação de organizações de defesa animal por resultado.', S3, INT),
 ('80,000 Hours', 'https://80000hours.org/', 'Como usar a carreira para fazer o máximo de bem; inclui guias sobre prioridades morais.', S3, INT),
 ('Teste de Visão Moral', 'https://ethicstest.biblioverse.org/', 'Da BiblioVerse: descubra sua teoria normativa, seu círculo moral, sua metaética e sua abertura.', S4, NAC),
 ('Check-up Filosófico', 'https://coherencetest.biblioverse.org/', 'Da BiblioVerse: você pensa corretamente? Um teste de coerência das suas crenças, para descobrir onde elas se contradizem.', S4, NAC),
 ('Política Para Iniciantes', 'https://politicaparainiciantes.biblioverse.org/', 'Da BiblioVerse: a continuação deste curso, do lado da política, com vieses, vertentes e debates.', S4, NAC),
 ('Guia de Argumentação', 'https://pelosanimais.biblioverse.org/', 'Da BiblioVerse: falácias, argumentos ruins e como argumentar bem.', S4, NAC),
 ('Moral Machine (MIT)', 'https://www.moralmachine.net/hl/pt', 'Decida dilemas de carros autônomos e compare suas respostas com as de milhões de pessoas.', S4, NAC),
]

LIVROS += [
 b('Ethics: The Fundamentals', 'Julia Driver', 'Introdução curta e clara às teorias normativas (utilitarismo, Kant, virtudes, contrato) e à metaética, com as objeções principais a cada uma. Um bom primeiro livro-texto.', INI),
 b('The Philosophy Gym', 'Stephen Law', 'Vinte e cinco problemas de filosofia em capítulos curtos e com diálogos, vários de ética: moralidade sem religião, punição, subjetivismo moral, comer animais. Ótimo para começar.', INI),
 b('Meaning in Life and Why It Matters', 'Susan Wolf', 'O que torna uma vida significativa: envolver-se com o que vale a pena. Curto e claro.', INTM),
 b('Meaning in Life', 'Thaddeus Metz', 'O tratado analítico sobre o sentido da vida: as teorias rivais e uma proposta própria.', AVA),
 b('Epistemic Injustice', 'Miranda Fricker', 'O livro que nomeou a injustiça de não ser acreditado e a de não ter palavras para a própria experiência.', AVA),
 b('Responsibility for Justice', 'Iris Marion Young', 'Responsabilidade por injustiças que ninguém causou sozinho: o modelo da conexão social.', AVA),
 b('The Moral Problem', 'Michael Smith', 'Três teses plausíveis sobre juízo, motivação e desejo que não cabem juntas; o mapa da metaética contemporânea.', AVA),
 b('Exploitation', 'Alan Wertheimer', 'A definição mais usada de exploração e os casos difíceis: trocas vantajosas e injustas.', AVA),
]
