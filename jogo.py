from random import choice
print('oioi')
print('bem-vindo ao meu mundo')
for i in range(1, 4):
    print('.')
HEROIS = ['flash', 'homem de ferro', 'batman', 'homem aranha', 'mulher maravilha',
          'thor', 'supergirl', 'capitao america', 'viuva negra', 'hulk',
          'aquaman', 'superman', 'homem formiga', 'gaviao arqueiro', 'arqueiro verde',
          'capita marvel', 'pantera negra', 'doutor estranho', 'wolverine', 'feiticeira escarlate']
OBJETOS = ['almofada', 'bisturi', 'canivete', 'giz', 'lampada',
           'machado', 'guarda-chuva', 'lapis', 'pincel', 'violao',
           'ziper', 'quadro negro', 'ima', 'harpa', 'fogao',
           'computador', 'copo', 'dado', 'flecha', 'oculos']
ANIMES = ['attack on titan', 'tokyo revengers', 'pokemom', 'castlevania', 'dragon ball',
          'naruto', 'hunterXhunter', 'jujutsu kaisen', 'one piece', 'one punch man',
          "Jojo's Bizarre Adventure", 'The promissed Neverland', 'Death Note', 'helsing',
          'Nanatsu no Taizai', 'Kakegurui', 'banana fish', 'Black Cover', 'tokyoGhoul', 'demon slayer']
SERIESdAnETFLIX = ['la casa de papel','vis a vis', 'the witcher','sex education', 'the umbrella academy',
                   'dracula', 'elite', 'eu nunca', 'insatiable', 'you', 'lucifer', 'peaky blinders',
                  'o gambito da rainha', 'o mundo sombrio de sabrina', 'stranger things', 'outer banks',
                   'round 6', 'cowboy bepop', 'amizade dolorida', 'the end of the fucking world']
dici = {"flash":'fudeu a linha do tempo, mais de uma vez','homem de ferro':'genio, bilionario, playboy, filantropo', 'batman':'eu comprei o banco', 'homem aranha':'e quem disse que isso é problema meu?', 'mulher maravilha':'estragando nossos ships desde 1941', 'thor':'ele não é um cara, você é um cara, ele é um homem, um homem bonito', 'supergirl':'nós nao combinamos, olha em sherek um dragao casa com um burro e da super certo', 'capitao america':'picole de 70 anos', 'viuva negra':'tem filme solo, e fugiu do trafico de criancas', 'hulk':'quem é verde, forte e esmaga?', 'aquaman':'aquele peixe que voce respeita', 'superman':'o nome da minha mãe é martha', 'homem formiga':'foi salvo por um rato', 'gaviao arqueiro':'nunca erro o alvo, Natasha Romanova my best friend ', 'arqueiro verde':'estive numa ilha por 5 anos, e dormi com a irma lesbica da minha namorada', 'capita marvel':'''thanos: eu sou invencivel
eu: gg''', 'pantera negra':'eu sou foda pra um ***, sou o rei de um dos paises mais ricos do mundo ', 'doutor estranho':'''*alguem entrega um papelzinho
eu: oq é isso? um mantra que eu tenho que recitar toda noite?
alguem: é a senha do wi-fi ''', 'wolverine':'me regenero, sou muito ****, tenho um fraco por ruivas', 'feiticeira escarlate':'''eu: voce roubou tudo de mim
alguem: eu nem sei quem voce é
* eu mandando os poderes mucho loucos''', 'almofada':'é fofa e se usa para decorar o sofa e deixar mais confortavel', 'bisturi':'medicos usam para fazer a primeira insicao', 'canivete':'É um objeto com várias utilidades, ele pode abrir garrafas, pessoas','giz':'utilizado para escrever ou riscar em superfícies ásperas, como o quadro-negro','lampada':'Item de vidro criado pelos humanos para iluminar a feiúra das pessoas no escuro','machado':'a ferramenta de trabalho de um lenhador','guarda chuva':'quando chove e a primeira coisa que procura antes de sair de casa','lapis':'um pedaço de madeira diferenciado dos demais, geralmente crianças mastigam na escola','pincel':'instrumento dos pintores','violao':'o melhor amigo de um cantor, nop é a voz, fica dica','ziper':'serve em maioria para fechar as calças das pessoas, ou veriamos aonde o sol nao bate','quadro negro':'É um quadro nomeado por daltônicos pois é verde, tbm últizado pra tortura de estudantes',
'ima':'eu sou atraida por morenos sarcasticos e ele por metais','harpa':'instrumento muy beautiful, geralmente tocado por anjos','fogao':'se cozinha com ele, ja queimei muito arroz com ele','computador':'seu idioma é composto por uns e zeros, conhecido como binário','copo':'voce usa para tomar agua ou qualquer liquido','dado':'queridinho dos mestres de rpg de mesa, podem ter 6, 20, 60, infinitos lados','flecha':'usada por merida, Katniss Everdeen, arqueiro verde para derrotar seus inimigos','oculos':'voce pode ter miopia, hipermetropia oque for voce usa ele para enxergar','la casa de papel':'Ladrões do mau que na nossa visão são do bem que roubam bancos','vis a vis':'''É uma série sobre uma morena e uma loira que tentam se matar a
qualquer custo, mas se amam no fundo e todo mundo sabe disso''','the witcher':'de um trocado para o seu bruxo, ó vale abundante','sex education':'não odiamos mais o cadeirante','the umbrella academy':'''o relacionamento mais saudavel e duradouro que essa familia ja viu,
foi o do cinco quando ele comia aquele manequim''','the end of the fucking world':'que casal melhor doq o psicopata apaixonado e a famosinha q n ama?','dracula':'van helsing = uma freira','elite':'a serie que tu nunca pode olhar com teus pais','eu nunca':'a menina tem dois cara gato que estao brigando por ela, oq ela pensa? se eu posso ter um, porque nao dois','insatiable':'matei umas 3 pessoas de proposito, mas nao queria confia, #miss universo','you':'stalker','lucifer':'ate o padre fabio de melo assiste, se ele faz ate padre gosta, quem sou eu pra nao ama','peaky blinders':'voce lutou na frança?','o gambito da rainha':'drogas, xadrez e um russo mucho louco','o mundo sombrio de sabrina':'ela literalmente foi ate o inferno por ele','stranger things':'amigos nao mentem','outer banks':'caça ao tesouro diferenciada','round 6':'batinha frita 123','cowboy bepop':'a serie é boa mas o anime é melhor','amizade dolorida':'''vem de chicote, algema, corda de alpinista,
eai que eu percebi que o cara é sadomasoquista''', 'attack on titan':'''Anime de bixo gigante q come gente pequena.
Olhando por outro angulo é basicamente oq rola na vida real.''','tokyo revengers':'''Anime de gang, dinheiro, viajem do tempo e mulheres tudo
que nossa mãe quer q fiquemos o mais longe possíveo''','pokemom':'Tráfico ilegal (e legal) de animais que soltam magia pew pew','castlevania':'''Oq vc procura? Vampiros gostosos? Mulheres empoderadas? Sangue?
Um plot ruim? Ent esse anime é pra vc''','dragon ball':'''Divirta-se vendo o protagonista se tornar o mais
poderoso do Universo mesmo sendo um cabeça dura... e veja ele morrer 400 vezes tb''','naruto':'Anime de um loiro de olhos azuis que passa parte da vida correndo atrás de um emo revoltado','hunterXhunter':'''Anime de um muleque que descobriu q o pai não morreu,
só foi comprar cigarro e aí se revoltou e virou um bixin fod''','jujutsu kaisen':'''História de um mlk doido que come dedos, um cabeça branca
invencivel e umas macumbas ambulantes''','one piece':'Cara tu realmente assistiu 1000 episódios do Pirata que estica?','one punch man':'''História de um careca que destrói montanhas
com um soco que tem um robô como melhor amigo''',"Jojo's Bizarre Adventure":'É mais bizarro doq ver um anão sendo fodido pelo kid bengala, E as vezes mais triste','The promissed Neverland':'Anime de orfaos que são umas carnes deliciosas, mas ainda não sabem','Death Note':'Anime de um cara pescotapa que mata outros pescotapas só com um caderno escolar','helsing':'''La musiquita do inferno, Aí é pow, Pow, Sangue, Tiro,
Dente, Vampiro, É tipo um onepunch, So que é oneshot''','Nanatsu no Taizai':'História de um pedófilo com nanismo e seu grupo de retardados quebrando a cara de crente','kakegurui':'''Requesitos para assistir esse anime
Saber apostar
Ter 300 QI
Ter uma boa sanidade... vc vai precisar''','banana fish':'''Anime que coloca todas as espécies de seres vivos
em depressão por culpa de um loirin gostoso''','Black Cover':'Ele nao tem magia num mundo magico, mas.. ele tem poderes???','tokyoGhoul':'Hmmm humaninho frito hmmm','demon slayer':'''Anime de um garoto trabalhador que tem uma irmã demoníaca,
e agora tem que cuidar da sua demoniazinha pra q ela não coma ninguém'''}
dnv = ''
nome = input('qual seu nome? ')
while True:
    if dnv == 'n':
        break
    for i in range(1, 3):
        print('.')
    jogo = input('''escolha sua categoria favorita:
    HEROIS
    OBJETOS
    SERIES DA NETFLIX
    ANIMES
    sua escolha: ''').upper()
    print(f'boa sorte {nome}')
    while True:
        if jogo == 'HEROIS':
            guesses = ' '
            turns = 12
            sorteado = choice(HEROIS)
            print(dici[sorteado])
            while turns > 0:
                failed = 0
                for char in sorteado:
                    if char in guesses:
                        print(char)
                    else:
                        print("_")
                        failed += 1
                if failed == 0:
                    print("vc venceu eeee")
                    print("a palavra era:", sorteado)
                    HEROIS.remove(sorteado)
                    dici.pop(sorteado)
                    break
                guess = input("digite uma letra ou a palavra se souber: ")
                guesses += guess
                if guess not in sorteado:
                    turns -= 1
                    print("putz, errou")
                    print(f'vc tem {turns} chances restantes')
                if turns == 0:
                    print("seu looser, mó abostado")
                    HEROIS.remove(sorteado)
                    dici.pop(sorteado)
        if jogo == 'OBJETOS':
            guesses = ' '
            turns = 12
            sorteado = choice(OBJETOS)
            print(dici[sorteado])
            while turns > 0:
                failed = 0
                for char in sorteado:
                    if char in guesses:
                        print(char)
                    else:
                        print("_")
                        failed += 1
                if failed == 0:
                    print("vc venceu eeee")
                    print("a palavra era:", sorteado)
                    OBJETOS.remove(sorteado)
                    dici.pop(sorteado)
                    break
                guess = input("digite uma letra ou a palavra se souber: ")
                guesses += guess
                if guess not in sorteado:
                    turns -= 1
                    print("putz, errou")
                    print(f'vc tem {turns} chances restantes')
                if turns == 0:
                    print("seu looser, mó abostado")
                    OBJETOS.remove(sorteado)
                    dici.pop(sorteado)
        if jogo == 'SERIES DA NETFLIX':
            guesses = ' '
            turns = 12
            sorteado = choice(SERIESdAnETFLIX)
            print(dici[sorteado])
            while turns > 0:
                failed = 0
                for char in sorteado:
                    if char in guesses:
                        print(char)
                    else:
                        print("_")
                        failed += 1
                if failed == 0:
                    print("vc venceu eeee")
                    print("a palavra era:", sorteado)
                    SERIESdAnETFLIX.remove(sorteado)
                    dici.pop(sorteado)
                    break
                guess = input("digite uma letra ou a palavra se souber: ")
                guesses += guess
                if guess not in sorteado:
                    turns -= 1
                    print("putz, errou")
                    print(f'vc tem {turns} chances restantes')
                if turns == 0:
                    print("seu looser, mó abostado")
                    SERIESdAnETFLIX.remove(sorteado)
                    dici.pop(sorteado)
        if jogo == 'ANIMES':
            guesses = ' '
            turns = 12
            sorteado = choice(ANIMES)
            print(dici[sorteado])
            while turns > 0:
                failed = 0
                for char in sorteado:
                    if char in guesses:
                        print(char)
                    else:
                        print("_")
                        failed += 1
                if failed == 0:
                    print("vc venceu eeee")
                    print("a palavra era:", sorteado)
                    ANIMES.remove(sorteado)
                    dici.pop(sorteado)
                    break
                guess = input("digite uma letra ou a palavra se souber: ")
                guesses += guess
                if guess not in sorteado:
                    turns -= 1
                    print("putz, errou")
                    print(f'vc tem {turns} chances restantes')
                if turns == 0:
                    print("seu looser, mó abostado")
                    ANIMES.remove(sorteado)
                    dici.pop(sorteado)
        dnv = input('Você quer jogar dnv [s/n]: ').lower()
        if dnv == 'n':
            print('Muito obrigada por jogar, esperamos que tenha gostado!!')
            break
        elif input('você quer mudar de categoria [s/n]: ').lower() == 's':
            break
