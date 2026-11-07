"""Dados da página de critérios éticos: as seis delimitações do círculo moral e as fronteiras da parcialidade.
Adaptado das planilhas de Julio (Delimitações Éticas, Fronteiras da Moralidade, Fundamentos Morais), com as correções anotadas na revisão de 2026-11-04."""

# ---------- as seis delimitações ----------
# n: nome; t: slug da teoria correspondente no catálogo; deriv: movimentos derivados; valor: quem tem valor direto; mot: a razão alegada;
# permite: parcialidades que a delimitação deixa passar; fins; forcas; fraquezas
DELIM = [
 dict(n='Egocentrismo', t='egoismo-etico', deriv='Egoísmo ético, individualismo radical, solipsismo moral', valor='Só o próprio indivíduo tem valor em si', mot='Cada um é a única perspectiva a que tem acesso, e cuidar de si é o que a natureza premia',
  permite='Todas: qualquer parcialidade serve, desde que favoreça o próprio agente', fins='Proteger e favorecer a si mesmo',
  forcas='É intuitivo: cada um sente os próprios interesses com mais força do que os dos outros, e conhece melhor as próprias necessidades.',
  fraquezas='É arbitrário: a minha dor não é diferente da sua por ser minha. Não resolve conflitos (manda cada um vencer o outro), não pode ser recomendado a ninguém e, levado a sério, não é uma moral, e sim a ausência de uma.'),
 dict(n='Tribalismo (grupocentrismo)', t='egoismo-etico', deriv='Familiarismo, nacionalismo, etnocentrismo, religiosismo, classismo e as demais fronteiras parciais listadas abaixo', valor='Os indivíduos de grupos específicos têm mais valor', mot='Laços, lealdade, semelhança e tradição; o grupo é descrito como naturalmente superior ou como o único que pode ser conhecido de verdade',
  permite='Sexismo, racismo, homofobia, capacitismo, intolerância religiosa e política, especismo: qualquer exclusão de quem está fora do grupo', fins='Proteger e favorecer grupos específicos',
  forcas='É intuitivo e apela ao que já sentimos: cuidamos mais de quem está perto, e a evolução nos preparou para isso. Deveres especiais com os próximos são reais.',
  fraquezas='O traço que define o grupo nunca é relevante para o que está em jogo: cor, nação ou religião não mudam a capacidade de sofrer. Permite opressões sistemáticas e já justificou todas as que a história registra. Deveres especiais permitem cuidar mais dos seus; não permitem tratar os outros como se não contassem.'),
 dict(n='Antropocentrismo', t='antropocentrismo', deriv='Humanismo em sua forma tradicional (não todo humanismo: muitos humanistas incluem os animais)', valor='Os humanos têm valor em si; o resto conta pelo efeito sobre humanos', mot='Pertencer à espécie humana, ou ter capacidades (razão, linguagem) tomadas como exclusivas dela',
  permite='Especismo', fins='Proteger e favorecer qualquer indivíduo humano',
  forcas='Inclui todos os humanos, o que já foi uma conquista enorme. É confortável e de fácil adesão, porque coincide com o costume e com vieses arraigados. Reconhece capacidades humanas reais.',
  fraquezas='Não usa o que é relevante para a ética, a capacidade de ser prejudicado ou beneficiado. A espécie é um traço biológico como a raça; e as capacidades alegadas (razão, linguagem) faltam a bebês e a pessoas com deficiência grave, que contam, e sobram em muitos animais, que não contam. É o argumento dos casos marginais.'),
 dict(n='Senciocentrismo (sencientismo)', t='sencientismo', deriv='Antiespecismo, veganismo ético, biologia do bem-estar, éticas focadas no sofrimento', valor='Os seres sencientes têm valor em si', mot='O que é relevante para receber consideração de forma justa e imparcial é a capacidade de ser prejudicado ou beneficiado, isto é, de sentir',
  permite='Nenhuma das anteriores. Em versões parciais, admite graus (gradualismo), desconto do futuro (temporalismo) ou exclusão de mentes artificiais (carbonismo)', fins='Proteger e favorecer qualquer indivíduo senciente',
  forcas='É o mais coerente diante da razão: usa o critério da relevância, a imparcialidade e o tratamento de interesses semelhantes de forma semelhante. Inclui bebês e pessoas com deficiência sem truques, e explica por que a crueldade com um animal é errada pelo animal.',
  fraquezas='É contraintuitivo e de adesão difícil, porque confronta hábitos e vieses. Precisa saber quem sente, e a ciência ainda tem incerteza sobre invertebrados. Comparar experiências entre espécies é difícil. As implicações práticas são grandes, e a maioria não as segue.'),
 dict(n='Biocentrismo', t='biocentrismo', deriv='Reverência pela vida (Schweitzer), biocentrismo igualitário (Taylor), biocentrismo com graus (Attfield)', valor='Os seres vivos têm valor em si, sencientes ou não', mot='Todo organismo tem um bem próprio: crescer, se manter, se reproduzir. Ter um bem próprio bastaria para contar',
  permite='Indiferença à senciência: pode sacrificar interesses de quem sente por seres que não sentem, ou tratá-los como equivalentes', fins='Proteger e favorecer qualquer ser vivo',
  forcas='Leva a sério a vida não humana e rejeita a arrogância da espécie. Reconhece a importância de preservar toda a vida, e tem um apelo real.',
  fraquezas='Um ser sem senciência pode ser danificado, mas não se importa com o dano: não há ninguém para quem as coisas vão mal. Pelo critério da relevância, defender entidades não sencientes de forma direta é um erro de categoria, e os sencientes ficam em segundo plano. Biocentristas respondem que ter um bem próprio basta; é o ponto em disputa.'),
 dict(n='Ecocentrismo', t='ecocentrismo', deriv='Ética da terra (Leopold, Callicott), ecologia profunda (Naess), parte do ambientalismo', valor='As entidades naturais (ecossistemas, espécies, a biosfera) têm valor em si, acima dos indivíduos', mot='A interdependência de tudo o que existe em um ecossistema; a saúde e a estabilidade do todo vêm antes das partes',
  permite='Sacrifício de indivíduos sencientes pelo “bem do sistema”: abate de espécies introduzidas, recusa de ajudar animais selvagens, indiferença ao sofrimento “natural”', fins='Proteger e favorecer qualquer ente natural',
  forcas='Visão holística, que leva em conta a interdependência e a irreversibilidade da destruição ambiental. Fundamenta a conservação e corrige o curto prazo das éticas individualistas.',
  fraquezas='Um ecossistema não sente; os animais que vivem nele, sim. Dar consideração direta ao todo e negá-la a quem sofre dentro dele inverte a ordem da relevância. “Integridade” e “estabilidade” não são estados naturais: ecossistemas mudam, e escolher um estado como o certo é decisão humana. Regan chamou a prioridade do todo de “fascismo ambiental”.'),
]

# ---------- as fronteiras da parcialidade ----------
# (grau, nome do viés ou sistema parcial, característica usada, quem favorece, quem despreza, a posição imparcial correspondente)
GRAUS = {1: 'Indivíduo', 2: 'Grupo íntimo', 3: 'Grupo amplo', 4: 'Espécie', 5: 'Tempo e evidência'}
FRONTEIRAS = [
 (1, 'Egoísmo / egocentrismo', 'existencial', 'o próprio indivíduo', 'todos os outros', 'Imparcialidade: os interesses de cada um contam igual'),
 (2, 'Familiarismo', 'intimidade, sangue, afeto', 'família, parceiros, amigos, animais de companhia', 'quem está fora do círculo íntimo', 'Deveres especiais com limite: cuidar mais dos seus sem tratar os outros como se não contassem'),
 (3, 'Intolerância política', 'política', 'quem tem as mesmas crenças político-econômicas', 'quem pensa diferente, inclusive de forma democrática', 'Pluralismo e tolerância política'),
 (3, 'Elitismo / classismo / casteísmo', 'econômica', 'quem tem mais poder econômico ou nasceu na casta certa', 'os mais pobres e os de casta inferior', 'Igualdade de consideração entre classes; prioridade a quem está pior'),
 (3, 'Intolerância religiosa', 'religiosa', 'quem tem a mesma religião', 'quem tem outra religião ou nenhuma', 'Liberdade religiosa e laicidade do Estado'),
 (3, 'Nacionalismo / patriotismo excludente', 'geográfica, cultural', 'compatriotas', 'estrangeiros', 'Cosmopolitismo: o lugar de nascimento não é razão moral'),
 (3, 'Etnocentrismo', 'etnográfica', 'quem tem a mesma etnia', 'outras etnias', 'Antietnocentrismo'),
 (3, 'Sexismo', 'biológica', 'o próprio sexo', 'o outro sexo', 'Igualdade entre os sexos'),
 (3, 'Racismo', 'biológica', 'a própria raça ou as preferidas', 'outras raças', 'Antirracismo'),
 (3, 'Transfobia', 'identidade de gênero', 'quem tem identidade de gênero normativa', 'pessoas trans e não binárias', 'Respeito à identidade de gênero'),
 (3, 'Homofobia', 'orientação sexual', 'quem tem orientação normativa', 'outras orientações', 'Respeito à orientação sexual'),
 (3, 'Etarismo', 'idade', 'certas faixas etárias', 'outras idades, em geral idosos e crianças', 'Antietarismo'),
 (3, 'Capacitismo', 'capacidade física, cognitiva ou psíquica', 'quem tem constituição normativa', 'pessoas com deficiência', 'Anticapacitismo: a capacidade não muda o valor dos interesses'),
 (3, 'Lookismo (discriminação estética)', 'aparência', 'quem está dentro do padrão de beleza', 'quem está fora', 'Antilookismo'),
 (3, 'Linguicismo (linguismo)', 'língua, sotaque', 'quem fala como o grupo dominante', 'quem fala outra língua ou com outro sotaque', 'Igual consideração independente da língua ou do sotaque'),
 (3, 'Discriminação por tamanho corporal', 'peso, altura', 'corpos de certo tamanho', 'corpos fora do padrão', 'Igual consideração independente do tamanho do corpo'),
 (3, 'Reacionarismo', 'temporal, cultural', 'os costumes de certa época', 'quem vive de outro modo', 'Abertura à mudança, com exame'),
 (4, 'Especismo / antropocentrismo / carnismo', 'espécie', 'humanos', 'os demais animais', 'Antiespecismo / sencientismo'),
 (4, 'Carbonismo (substratismo)', 'substrato', 'mentes biológicas', 'mentes artificiais sencientes, caso existam', 'Sencientismo independente de substrato'),
 (4, 'Ambientalismo antropocêntrico', 'utilidade para humanos, carisma', 'humanos e espécies carismáticas ou úteis', 'as demais espécies e os indivíduos que sofrem nos ecossistemas', 'Ambientalismo antiespecista: proteger a natureza por quem sente nela'),
 (5, 'Presentismo (geracionismo, temporalismo)', 'temporal', 'quem existe agora, ou quem existe mais cedo', 'as gerações futuras', 'Atemporalismo / longoprazismo'),
 (5, 'Inevidencialismo', 'epistêmica, não um grupo', 'crenças e práticas sem evidência', 'quem é prejudicado por decisões mal fundamentadas', 'Práticas baseadas em evidências'),
]

# ---------- as dimensões de uma visão moral (Fundamentos morais) ----------
DIMENSOES = [
 ('Prioridade', 'Qual teoria normativa mais pesa', 'Consequências (utilitarismo, prioritarismo, igualitarismo, suficientismo); regras e deveres (deontologia, kantismo, pluralismo, mandamento divino); caráter (virtudes, cuidado); acordo (contratualismo)', 'teorias.html'),
 ('Critério', 'Quem recebe consideração, e com que peso', 'Humanos; sencientes (pleno ou gradual); vivos; sistemas naturais; os mais racionais; um grupo humano específico', 'criterios.html'),
 ('Fonte', 'De onde vem a moral', 'Fontes naturais e seculares (razão, experiência, ciência), ou fontes sobrenaturais (revelação, religião, misticismo). Não confundir com o naturalismo e o não naturalismo da metaética, que são duas formas de realismo', 'metaetica.html'),
 ('Capacidade de agir', 'Que força o indivíduo tem para realizar o que considera certo', 'Conhecimento (pouco, médio, muito) e poder (pouco, médio, muito); a tríade de influência de Cunha acrescenta a motivação', 'fraqueza-de-vontade.html'),
 ('Abertura', 'Como o indivíduo revisa suas visões', 'Abertura, honestidade e humildade intelectual, testabilidade, coerência, imparcialidade; ou dogmatismo, fechamento, enviesamento e conformismo', 'abertura-moral.html'),
]
FONTES_CRIT = [('Comparando várias teorias da ética normativa (Senciência e Ética)', 'https://senciencia.org/2024/06/18/comparando-varias-teorias-da-etica-normativa'), ('A diferença entre a defesa animal e a defesa ambiental', 'https://juliocesar.medium.com/a-diferen%C3%A7a-entre-a-defesa-animal-e-a-defesa-ambiental-5e2f4c9c47a5'), ('A tríade de influência e o sofrimento futuro (Senciência e Ética)', 'https://senciencia.org/2024/04/22/a-triade-de-influencia-e-o-sofrimento-futuro'), ('Mapa do Teste de Visão Moral', 'https://ethicstest.biblioverse.org/map.html')]
