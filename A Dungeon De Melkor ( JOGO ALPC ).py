sala_atual = 1
caminho = ""  # variável para armazenar o caminho escolhido

while sala_atual != 0:
    if sala_atual == 1:
        print("\033[31m" + "A Dungeon De Melkor".title() + "\033[0m")
        print("\nVocê entrou em uma masmorra")
        print("E se encontrou com um comerciante")
        print("Comerciante: Ola aventureiro, está dungeon é perigosa traiçoeira porem tambem recompensadora para aqueles que OUSAREM enfrentar seus desafios.")
        print("Comerciante: Há duas portas: esquerda (mais escura) e direita (mais iluminada).")

        while True:
            escolha = input("Você vai pela esquerda ou direita? ").lower().strip()


            if escolha == "esquerda":
                print("Você escolheu o caminho escuro e silencioso...")
                caminho = "escuro"
                sala_atual = 3
                break
            elif escolha == "direita":
                print("Você escolheu o caminho claro, com ecos de vozes distantes...")
                caminho = "claro"
                sala_atual = 2
                break
            else:
                print("Não existe tal caminho! Escolha 'esquerda' ou 'direita'.")

    elif sala_atual == 2:
        print("\033[31m" + "Sala 2: A sala do enigma do piano !".title() + "\033[0m")
        print("O jogador observa um piano no canto da sala e a porta a seguir trancada e uma estante")
        print("O jogador observa um quadro pendurado com um homem velho tocando piano")

        while True:
            escolha = input("Você toca o piano ou investiga a estante ? ( Piano ou Estante ?) ").lower().strip()

            if escolha == "piano":
                print("Você tocou uma bela melodia no piano e a porta antes tracada se abriu !")
                sala_atual = 6
                break
            elif escolha == "estante":
                print("Você descobriu uma passagem secreta atrás da estante !")
                sala_atual = 4
                break
            else:
                print("Não existe tal caminho! Escolha 'piano' ou 'estante'.")

    elif sala_atual == 4:
        print("\033[31m" + "\nSala 4: A sala de estar".title() + "\033[0m")
        print("O jogador se encontra em uma sala de estar aconchegante, com uma cama e uma armadura medieval")
        
        while True:
            escolha = input("Você pode se deitar na belissima cama ou mexer na armadura, qual você escolhe ? ( Armadura ou cama ?) ").lower().strip()


            if escolha == "armadura":
                print("Você mexeu na armadura e uma porta secreta se abriu !!!")
                sala_atual = 9
                break
            elif escolha == "cama":
                print("Você se deitou na cama e acabou adormecendo e nunca mais acordou ! :(")
                print("\033[31m" + "Game Over" + "\033[0m")
                break
            else:
                print("Não existe tal caminho ! Escolha 'armadura' ou 'cama'")

    elif sala_atual == 9:
        print("\033[31m" + "\nSala 9: Sala Secreta".title() + "\033[0m")
        print("O jogador encontrou uma passagem secreta que leva a um baú secreto")

        while True:
            escolha = input("Abrir o Baú ? ( Sim ou Nao ) ").lower().strip()

            if escolha == "sim":
                print("Você encontrou uma armadura no estilo oriental no baú e a pegou e vestiu, ela parece ser bem resistente !")
                print("Após isso voltou para a sala anterior.")
                sala_atual = 2
                break
            elif escolha == "nao":
                print("Você se afastou do baú, com medo de ser uma armadilha e voltou para a sala anterior.")
                sala_atual = 2
                break
            else:
                print("Não existe tal caminho ! Escolha 'sim' ou 'não'")

    elif sala_atual == 3:
        print("\033[31m" + "\nSala 3: A sala aranhosa".title() + "\033[0m")
        print("O jogador entra em uma cheia de teias de aranha e moveis antigos, e no canto escuro da sala e escuta um som aterrorizante...")
        print("Uma aranha... uma das filhas de Ungoliant")

        while True:
            escolha = input("Você vai fugir ou tentar lutar com a aranha ? ( Fugir ou Lutar ) ").lower().strip()

            if escolha == "lutar":
                print("O jogador avança para cima da aranha com sua espada, acerta uma de suas pernas, porem é lançado longe com uma patada da aranha")
                print("Após se levantar do golpe ele investe contra a cria de ungoliant e por sorte ? ou experiencia ele a consegue eliminar com um golpe preciso em seus olhos")
                print("Você conseguiu derrotar a aranha e uma porta secreta na parede se abre e você a segue")
                sala_atual = 5
                break
            elif escolha == "fugir":
                print("O jogador com medo fugiu da aranha desviando de seus ataques e abrindo uma porta ao norte da sala no desespero e a fechando com tudo")
                sala_atual = 7
                break
            else:
                print("Não existe tal caminho ! Escolha 'fugir' ou 'lutar'")

    elif sala_atual == 6:
        print("\033[31m" + "\nSala 6: A sala das armaduras".title() + "\033[0m")
        print("O jogador se encontra em uma sala com varias armaduras formando um circulo.")
        print("E na frente da única porta está uma armadura viva o chamando para um duelo")

        while True:
            escolha = input("Você aceita o duelo da armadura ? ( Sim ou Nao ) ").lower().strip()

            if escolha == "sim":
                print("Você começa fazendo uma saudação a armadura como um sinal de honra e ela faz o mesmo")
                print("A armadura começa o embate mirando nas pernas do aventureiro, porem por ela ser extremamente pesada ele se desvia do ataque")
                print("E com isso ele consegue uma abertura para acertar um ataque de meia espada nas viseiras da armadura, a derrotando")
                print("A armadura se esfarela no chão e a porta se abre e você continua sua aventura para a proxima sala")
                sala_atual = 10
                break
            elif escolha == "nao":
                print("Após você tentar voltar pela porta que chegou reparou que ela se trancou, e um som estridente começa a ecoar pela sala")
                print("As armaduras que antes eram estatuas ganharam vida, e vieram para cima de você")
                print("Mesmo sendo um aventureiro habilidoso você não consegue aguentar lutar contra tantas armaduras e acaba sendo derrotado")
                print("\033[31m" + "Game Over" + "\033[0m")
                sala_atual = 1
                break
            else:
                print("Não existe tal caminho ! Escolha 'sim' ou 'não'")

    elif sala_atual == 10:
        print("\033[31m" + "\nSala 10: A sala da bigorna e fornalha".title() + "\033[0m")
        print("O jogador após sua batalha com a armadura se encontra em uma sala com fornalhas e bigornas")
        print("Com estes utensilios ele consegue melhorar sua armadura e espada, as deixando mais fortes")
        print("Após melhorar suas armas ele continua sua jornada, existem 2 caminhos, uma porta e um corredor coberto de pedras")

        while True:
            escolha = input("Você vai tentar ir pela porta ou pelo corredor bloqueado por pedras ? ( Porta ou Corredor ) ").lower().strip()

            if escolha == "porta":
                print("Você abre a porta e dá em um corredor cheio de relva e após o atravesar chega em outra sala")
                sala_atual = 15
                break
            elif escolha == "corredor":
                print("Mesmo após um grande esforço tentando tirar as pedras você não consegue")
            else:
                print("Não existe tal caminho ! Escolha 'Porta' ou 'Corredor'")

    elif sala_atual == 15:
        print("\033[31m" + "\nSala 15: A sala do Felgaroth, o Senhor dos Nove Miados".title() + "\033[0m")
        print("Após entrar na sala você se depara com um grande felino segurando duas espadas curvas em cada uma das mãos")
        print("Quando o grande Felgaroth percebe sua presença ele o olha com um olhar mortifero, com sede de sangue")

        while True:
            escolha = input("Você vai tentar fugir ou lutar contra o grande Felgaroth ? ( Fugir ou Lutar ) ").lower().strip()

            if escolha == "lutar":
                print("Felgaroth ergueu-se com elegância ameaçadora. Seus movimentos eram fluidos e controlados, a força contida em cada passo. Sem hesitação, avançou com agilidade incomum, deslizando pelo mármore frio, tentando cercar o intruso com sua cauda espessa.")
                print("O combate foi breve.")
                print("O aventureiro, atento aos padrões do inimigo, esperou o momento exato. Quando Felgaroth preparava seu ataque final, a lâmina do guerreiro cortou o ar e atingiu com precisão o colar de âmbar no pescoço da criatura — o foco silencioso de seu poder.")
                print("O impacto foi suficiente. Felgaroth recuou um passo, os músculos tensos suavizando. Sua forma começou a se dissipar, não em sangue ou ruído, mas em poeira dourada, levada por uma brisa que não existia. Ao fim, restava apenas o silêncio.")
                print("O aventureiro se depara com uma porta secreta se abrindo")

                
                escolha = input("Ir pela porta secreta ou continuar sua jornada até a proxima sala ? ( Secreta ou Sala ) ").lower().strip()
                    
                if escolha == "secreta":
                    print("O jogador vai pela sala secreta e encontra uma espada curvada muito parecida com a do Felgaroth")
                    print("Após encotrar tal espada ele decide seguir pelo unico caminho possivel")
                    sala_atual = 17
                    break
                elif escolha == "sala":
                    print("O jogador ignora a sala secreta e segue seu caminho pelo unico caminho possivel")
                    sala_atual = 17
                    break
                else:
                    print("Não existe tal caminho ! Escolha 'Secreta' ou 'Sala'")

            elif escolha == "fugir":
                print("Você tenta fugir de medo mas tropeça e se espeta com a sua propria espada...")
                print("\033[31m" + "Game Over" + "\033[0m")
                sala_atual = 1
                break
            else:
                print("Não existe tal caminho ! Escolha 'Fugir' ou 'Lutar'")
    
    elif sala_atual == 17:
        print("\033[31m" + "\nSala 17: A sala do Tharnak, o Senhor do Subsolo".title() + "\033[0m")
        print("Você adentra a uma sala enorme com um grande animal no meio lhe esperando")
        print("Tharnak: Bem vindo, humano")
        print("Tharnak: A muito tempo espero por um oponente a minha altura, será que hoje será o dia que serei derrotado ? Ou novamente me levantarei como o vencedor ?")
        print("Tharnak: Venha humano, demonstre suas habilidades")

        while True:
            escolha = input("Você irá atacar Tharnak, onde você dará o golpe inicial ? ( Pernas ou Peito ) ").lower().strip()

            if escolha == "pernas":
                print("O aventureiro começa o embate mirando nas pernas do grande Tharnak, ele consegue acertar o golpe porém Tharnak não demonstra nenhuma dor")
                print("Tharnak golpeia o aventureiro de forma agressiva, com o aventureiro tendo que desviar habilidosamente com movimentos esguios")
                print("Após Tharnak se cansar o aventureiro consegue uma brecha para acertar o seu coração, assim derrotando o Grande Tharnak")
                print("O aventureiro está livre para seguir para a sala final")
                sala_atual = 19
                break
            elif escolha == "peito":
                print("O aventureiro começa o embate mirando no peito do grande oponente, porem após acertar um golpe em seu peito o Grande Tharnak não demonstra dor")
                print("A espada do aventureiro fica presa entre no peito de Tharnak, sendo assim Tharnak consegue uma abertura para golpear fortemente o aventureiro")
                print("Fazendo o assim cair quase insconsciente no chão")
                print("Tharnak vem até você e está pronto para dar o ataque final...")

                escolha = input("O aventureiro consegue recobrar a consciencia e pode se deixar seguir pelo destino ou surpreender Tharnk ( surpreender ou destino ) ").lower().strip()

                if escolha == "surpreender":
                    print("O aventureiro se finge e quando Tharnak vai o golpear o aventureiro se desvia do ataque e vai para as costas de Tharnak e acerta um golpe certeiro em sua nuca")
                    print("Fazendo o assim sucumbir a seus ferimentos...")
                    print("O aventureiro está livre para seguir para a sala final")
                    sala_atual = 19
                    break
                elif escolha == "destino":
                    print("O aventureiro ainda inconsciente se rende ao destino e é executado por Tharnak")
                    print("\033[31m" + "Game Over" + "\033[0m")
                    sala_atual = 1
                    break
                else:
                    print("Não existe tal caminho ! Escolha 'surpreender' ou 'destino'")
            else:
                print("Não existe tal caminho ! Escolha 'pernas' ou 'peito'")
    
    elif sala_atual == 19:
        print("\033[31m" + "\nSala 19: A sala de Morgoth O Senhor Do Escuro".title() + "\033[0m")
        print("O aventureiro adentra em um grande salão, com cabeças de Dragão penduradas e um Grande Trono onde uma figura Assombrosa repousa")
        print("Com um frio na espinha porem com bravura o aventureiro se aproxima do ser assombroso")
        print("Aventureiro: Morgoth! Eu vim pôr fim à tua tirania. Tuas chamas já não assustam os povos livres!")
        print("Morgoth: Um verme ousa gritar meu nome em minha presença? És corajoso... ou tolo?")
        print("Aventureiro: Chame como quiser. Meu nome será lembrado como o homem que enfrentou o Senhor do Escuro!")
        print("Morgoth (ergue-se, cada passo faz o chão gemer): Lembrado? Hah... teu nome se perderá no pó como todos os que vieram antes. Os elfos, os anões, os homens... todos sangraram por esta tolice.")
        print("Aventureiro: Melkor, o caído! Traidor dos Valar! Tua sombra não durará para sempre!")
        print("Morgoth (avançando): Não pronuncies esse nome. Eu sou Morgoth Bauglir, o mundo foi moldado pelo peso do meu passo! Antes de tua raça andar sobre a terra, eu já queimava estrelas.")
        print("Aventureiro: Então queimes comigo! (ergue a espada e avança)")
        print("Morgoth (levanta Grond, o martelo de mundos): Tolo. Que tua morte seja rápida, para que tua alma não me aborreça nos salões de Mandos.")

        while True:
            escolha = input("O aventureiro avança contra Melkor, qual será a sua estrategia ? ( finta ou direto ) ").lower().strip()

            if escolha == "finta":
                print("Você se arrasta, fingindo fraqueza...")
                print("Quando Morgoth levanta Grond, você rola por baixo de sua guarda e gira em torno dele!")
                print("Com um golpe certeiro, atinge a base de sua nuca — o único ponto que sua armadura não cobre.")
                print("Morgoth grita, tropeça... e cai.")
                print("A sombra do mundo desaparece. Você venceu com astúcia.")
                print("Uma passagem atrás do Grande Trono Sombrio se Abre e você passa por ela")
                sala_atual = 20
                break
            elif escolha == "direto":
                print("\nVocê ruge e avança com fúria, mirando o peito de Morgoth.")
                print("Seu golpe atinge a armadura negra... e ressoa como um trovão inútil.")
                print("Morgoth sorri. Em um movimento, ele agarra sua lâmina com a mão nua.")
                print("Com a outra, desfere um soco que parte seu elmo ao meio.")
                print("Você cai de joelhos, desorientado.")
                print("Morgoth: 'Humano tolo !!!'")
                print("Ele ergue Grond e desfere o golpe final.")
                print("Você foi derrotado.")
                print("\033[31m" + "Game Over" + "\033[0m")
                sala_atual = 1
                break
            else:
                print("Não existe tal caminho ! Escolha 'finta' ou 'direto'")

    elif sala_atual == 20:
        print("\033[31m" + "\nSala 20: A sala da Princesa".title() + "\033[0m")
        print("O silêncio reina após a queda de Morgoth. As sombras que corrompiam a dungeon começam a se dissipar.")
        print("Você caminha por um corredor banhado por uma luz dourada que agora irrompe pelos vitrais rachados.")
        print("Ao fundo, uma porta de prata se abre sozinha, como se reconhecesse o fim do reinado sombrio.")

        print("\nDentro da sala, há uma cela encantada, selada por correntes negras.")
        print("Uma jovem de vestes nobres ergue os olhos ao ver você se aproximando. É a princesa Élara, herdeira do reino perdido.")
        print("Com um toque da Relíquia ou do sangue em sua espada, as correntes se quebram.")

        print("\nPrincesa Élara: 'Você... você veio... As lendas falavam de um campeão... mas eu temi que ninguém sobrevivesse ao trono negro.'")
        print("Você estende a mão e a ajuda a sair. Pela primeira vez em séculos, a luz toca sua pele livre.")
        print("A masmorra começa a ruir — mas agora não com destruição, mas com libertação.")

        print("\nVocês escapam juntos pelos salões antigos. A entrada, antes oculta, agora está aberta. O céu está limpo.")
        print("Pássaros voltam a cantar. O mundo está livre da sombra de Morgoth.")

        print("\nVocê cumpriu seu destino.")
        print("A princesa está salva. A paz retorna aos reinos.")
        print("Fim da jornada.")
        print("Obrigado por jogar!")
        sala_atual = 0

    elif sala_atual == 7:
        print("\033[31m" + "\nSala 7: A sala das cabeças empalhadas".title() + "\033[0m")
        print("O aventureiro adentra a uma sala cheia de cabeças de animais lendarios empalhados pendurados na parede")
        print("Ele percebe uma escrita magica na porta adiante 'Cada fera tem seu reflexo — toque-as juntas e o caminho surgirá.'")
        print("O aventureiro percebe que é um enigma e precisa decifra-lo, há botões nas partes inferiores das cabeças empalhadas")


        while True:
            escolha = input("O aventureiro tem duas opções, apertar os botões em uma cabeça de cada animal ou apertar em todos seguindo os pares de animais iguais ( pares ou cada ) ").lower().strip()

            if escolha == "pares":
                print("O aventureiro aperta os botões seguindo os pares dos mesmos animais e...")
                print("Antes a porta com a escrita magica que estava fechada se abre para o Aventureiro e ele prossegue na aventura")
                sala_atual = 11
                break
            elif escolha == "cada":
                print("O aventureiro aperta os botões seguindo só um animal de cada raça e...")
                print("Um alçapão armadilha se abre nós pés dele e ele cai para a morte")
                print("\033[31m" + "Game Over" + "\033[0m")
                sala_atual = 1
                break
            else:
                print("Não existe tal caminho ! Escolha 'pares' ou 'cada'")

    elif sala_atual == 11:
        print("\033[31m" + "\nSala 11: A sala do Rei Esqueleto".title() + "\033[0m")
        print("O aventureiro adentra a uma sala cheia de ossos pelo chão e uma figura sentada em seu trono no meio da sala")
        print("Quando o ser o percebe ele parte direto para o ataque sem mais nem menos...")

        while True:
            escolha = input("O aventureiro pode a atacar diretamente a figura tentar fugir ( Fugir ou Lutar ) ").lower().strip()

            if escolha == "lutar":
                print("O aventureiro enfrenta gloriosamente a criatura, após um tempo de luta o aventureiro consegue acertar um golpe certeiro em seu torso e o faz se despedaçar")
                print("O aventureiro cansado segue para a proxima sala, fadigado.")
                sala_atual = 12
                break
            elif escolha == "fugir":
                print("O aventureiro com medo tenta fugir da criatura porem tropeça e é morto pela criatura")
                print("\033[31m" + "Game Over" + "\033[0m")
                sala_atual = 1
                break
            else:
                print("Não existe tal caminho ! Escolha 'fugir' ou 'lutar'")

    elif sala_atual == 12:
        print("\033[31m" + "\nSala 12: A sala de Cristal".title() + "\033[0m")
        print("O Aventureiro adentra a uma sala rodeada de cristais totalmente reluzentes")
        print("O aventureiro olha mais de perto os cristais e percebe que consegue ver seu reflexo porem o reflexo parece ter vida propria...")
        print("O reflexo começa a sumir e desaparecer entre os cristais...")

        while True:
            escolha = input("O aventureiro pode simplesmente ignorar a sala e ir para a proxima ou tentar lutar contra seu proprio reflexo... ( lutar ou ignorar ) ").lower().strip()

            if escolha == "lutar":
                print("O Aventureiro começa a perseguir seu reflexo pelos cristais e os golpear sem descanço, e quando o último cristal não destruido resta o aventureiro o destroi com um golpe certeiro")
                print("E uma passagem atrás de um sarcofago se abre...")
                print("E ele a dentra a passagem.")
                sala_atual = 13
                break
            elif escolha == "ignorar":
                print("O aventureiro não da a minima para seu reflexo não seguindo seus movimentos e vai para a proxima sala...")
                sala_atual = 14
                break
            else:
                print("Não existe tal caminho ! Escolha 'lutar' ou 'ignorar'")

    elif sala_atual == 13:
        print("\033[31m" + "\nSala 13: A sala secreta".title() + "\033[0m")
        print("O Aventureiro segue a passagem secreta até um baú...")
        print("Onde encontra o Lendario Arco de Auriel")
        print("O Aventureiro se anima com a recompensa e segue para a proxima sala...")
        sala_atual = 14

    elif sala_atual == 14:
        print("\033[31m" + "\nSala 13: A Sala Astrologica".title() + "\033[0m")
        print("O Aventureiro chega em uma sala peculiarmente diferente, nela existem dois globos terrestres e um equipamente astrologico para ver as estrelas.")
        print("E na porta seguinte tem a seguinte mensagem, 'O observador de mundos será o recompensado com procedencia'")
        
        while True:
            escolha = input("O aventureiro pode usar o equipmento para tentar desvendar o enigma ou tentar forçar a porta ( desvendar ou forçar ) ").lower().strip()

            if escolha == "desvendar":
                print("O Aventureiro usa o Astrolabio para observar os dois globos terrestres da sala e com isso a porta se abre")
                sala_atual = 19
                break
            elif escolha == "forçar":
                print("O aventureiro vai tentar forçar a porta a se abrir porem antés dele chegar a porta um alçapão armadilha se abre e ele cai para sua morte")
                print("\033[31m" + "Game Over" + "\033[0m")
                sala_atual = 1
                break
            else:
                print("Não existe tal caminho ! Escolha 'desvendar' ou 'forçar'")

    elif sala_atual == 5:
        print("\033[31m" + "\nSala 5: A sala dos Vinhos".title() + "\033[0m")
        print("O Aventureiro chega em uma sala repleta de barris de vinho")
        print("Porem algo estranho pairá no ar, como se fosse uma vontade quase irredutivel de querer tomar os tais vinhos")

        while True:
            escolha = input("O aventureiro irá conter seus desejos ou sucumbir a vontade ? ( conter ou sucumbir ) ").lower().strip()

            if escolha == "conter":
                print("O aventureiro contem seus desejos e segue adiante não querendo nunca mais chegar perto de tal sala...")
                sala_atual = 8
                break
            elif escolha == "sucumbir":
                print("O aventureiro sucumbe a seus desejos e toma uma taça de vinho")
                print("No começo estava tudo bem porem ele começa a ficar fraco, o vinho detinha um veneno poderoso que mata o aventureiro depois de um tempo")
                print("\033[31m" + "Game Over" + "\033[0m")
                break
            else:
                print("Não existe tal caminho ! Escolha 'conter' ou 'sucumbir'")

    elif sala_atual == 8:
        print("\033[31m" + "\nSala 5: A sala dos livros magicos".title() + "\033[0m")
        print("O Aventureiro chega em uma sala cheia de livros, aparentemente uma sala sem nenhum perigo...")
        print("Porem ele acha que algo pode estar escondido")

        while True:
            escolha = input("O aventureiro irá tentar desvendar o misterio da sala dos livros ou a ignorar e seguir seu caminho ? ( ignorar ou desvendar )")

            if escolha == "ignorar":
                print("O Aventureiro segue seu caminho...")
                sala_atual = 12
                break
            elif escolha == "desvendar":
                print("O aventureiro começa a olhar os livros e percebe que alguns deles estão com uma capa diferente, então ele vai os inclinando para a frente e quando ele termina uma porta secreta se abre")
                print("E ele a adentra")
                sala_atual = 18
                break
            else:
                print("Não existe tal caminho ! Escolha 'ignorar' ou 'desvendar'")

    elif sala_atual == 18:
        print("\033[31m" + "\nSala 18: A sala secreta".title() + "\033[0m")
        print("O aventureiro adentra a sala secreta e encontra um baú")
        print("E dentro dele encontra as Grevas de Hermes, um equipamente lendario")
        print("Ele volta por onde veio e segue seu caminho")
        sala_atual = 12