# Imports
from Jogador import Jogador
from Equipa import Equipa
from Campeonato import Campeonato

lista_campeonato = []
lista_equipa = []
lista_jogador = []
while True: # MENU PRINCIPAL
    print("\nMenu Principal")
    print("*" * 40)
    print("\n1 - Campeonato\n2 - Equipa\n3 - Jogador\n0 - Sair")
    while True:
        try:
            op = int(input("Escolha uma opção: "))
            break
        except ValueError:
            print("\nDigite apenas núneros inteiros!\n")
    match op: 
        case 1: # MENU CAMPEONATO
            while True:
                print("\nMenu Campeonato")
                print("-" * 40)
                print("\n1 - Criar campeonato\n2 - Listar equipas\n3 - Calcular média de golos do campeonato\n4 - Listar campeonatos\n0 - Sair")
                while True:
                    try:
                        op = int(input("Escolha uma opção: "))
                        break
                    except ValueError:
                        print("\nDigite apenas núneros inteiros!\n")
                match op:
                    case 1: # cria campeonato
                        campeonato = Campeonato(input("Informe o nome do Campeonato que deseja criar: "))
                        lista_campeonato.append(campeonato)
                        for i in lista_campeonato:
                            print(i.getNome())
                    case 2: # lista equipas
                        if len(lista_campeonato) != 0:
                            campeonato = input("Nome do campeonato: ")
                            for i in lista_campeonato:
                                if i.getNome() == campeonato:
                                    if len(i.equipas) != 0:
                                        i.listarEquipas()
                                    else:
                                        print("\nCampeonato sem equipas\n")
                        else:
                            print("\nCrie primeiro um campeonato!\n")
                    case 3: # calcula media de golos do campeonato
                        if len(lista_campeonato) != 0:
                            campeonato = input("Nome do campeonato: ")
                            for i in lista_campeonato:
                                if i.getNome() == campeonato:
                                    if len(i.equipas) != 0:
                                        print(f"\nMédia de golos: {i.mediaGolos():.2f}\n")
                                    else:
                                        print("\nCampeonato sem equipas\n")
                        else:
                            print("\nCrie primeiro um campeonato!\n")
                    case 4: # lista campeonatos
                        if len(lista_campeonato) != 0:
                            print("\nLista de campeonatos")
                            print("-" * 40)
                            for c in lista_campeonato:
                                print(f"- {c.getNome()}")
                            print(" ")
                        else:
                            print("\nCrie primeiro um campeonato!\n")
                    case 0: # sair
                        break
        case 2: # MENU EQUIPA
            if len(lista_campeonato) != 0:
                while True:
                    print("\nMenu Equipa")
                    print("-" * 40)
                    print("\n1 - Criar equipa\n2 - Listar jogadores\n3 - Total de golos da equipa\n0 - Sair")
                    while True:
                        try:
                            op = int(input("Escolha uma opção: "))
                            break
                        except ValueError:
                            print("\nDigite apenas núneros inteiros!\n")
                    match op:
                        case 1: # cria equipa
                            print("\nLista de campeonatos")
                            print("-" * 40)
                            for c in lista_campeonato:
                                print(f"- {c.getNome()}")
                            print(" ")
                            campeonato = input("Insira o nome do campeonato que vai inserir a equipa: ")
                            for c in lista_campeonato:
                                if c.getNome() == campeonato:
                                    c.adicionarEquipa(Equipa(input("Nome da equipa: "), input("Cidade da equipa: ")))
                                else:
                                    print("\nCampeonato não encontrado\n")
                        case 2: # lista jogadores
                            equipa = input("Informe a equipa que procura: ")
                            campeonato = input("Insira o nome do campeonato desta equipa: ")
                            for c in lista_campeonato:
                                if c.getNome() == campeonato:
                                    if len(c.equipas) != 0:
                                        for e in c.equipas:
                                            if e.getNome() == equipa:
                                                if len(e.jogadores) != 0:
                                                    e.mostrarJogadores()
                                                else:
                                                    print("\nEquipe sem jogadores\n")
                                            else:
                                                print("\Equipe não encontrada\n")
                                    else:
                                        print("\nCampeonato sem equipas\n")
                                else:
                                    print("\nCampeonato não encontrado\n")
                        case 3: # total de golos da equipa
                            equipa = input("Informe a equipa que procura: ")
                            campeonato = input("Insira o nome do campeonato desta equipa: ")
                            for c in lista_campeonato:
                                if c.getNome() == campeonato:
                                    if len(c.equipas) != 0:
                                        for e in c.equipas:
                                            if e.getNome() == equipa:
                                                e.totalGolos()
                                            else:
                                                print("\nEquipe não encontrada\n")
                                    else:
                                        print("\nCampeonato sem equipas\n")    
                                else:
                                    print("\nCampeonato não encontrado\n")        
                        case 0: # sair
                            break
            else:
                print("\nCrie primeiro um campeonato!\n")
        case 3: # MENU JOGADOR
            if len(lista_campeonato) != 0:
                while True:
                    print("\nMenu Jogador")
                    print("-" * 40)
                    print("\n1 - Criar jogador\n2 - Mostrar dados\n3 - Alterar nº golos\n4 - Alterar nº jogos\n5 - Calcular média de golos por jogo\n0 - Sair")
                    while True:
                        try:
                            op = int(input("Escolha uma opção: "))
                            break
                        except ValueError:
                            print("\nDigite apenas núneros inteiros!\n")
                    match op:
                        case 1: # cria jogador
                            nome = input("Nome do jogador: ")
                            posicao = input("Posição: ")
                            equipa = input("Equipa: ")
                            campeonato = input("Campeonato: ")
                            while True:
                                try:
                                    golos = int(input("Nº golos: "))
                                    jogos = int(input("Nº jogos: "))
                                    break
                                except ValueError:
                                    print("\nApenas números inteiros\n")
                            jogador = Jogador(nome, posicao, golos, jogos)
                            for c in lista_campeonato:
                                if c.getNome() == campeonato:
                                    for e in c.equipas:
                                        if e.getNome() == equipa:
                                            e.adicionarJogador(jogador)
                                        else:
                                            print("\nEquipa não encontrada\n")
                                            for e in c.equipas:
                                                print(e.getNome())
                                else:
                                    print("\Campeonato não encontrada\n")
                                    for c in lista_campeonato:
                                        print(c.getNome())
                        case 2: # mostra dados do jogador
                            nome = input("Nome do jogador: ")
                            equipa = input("Equipa: ")
                            campeonato = input("Campeonato: ")
                            for c in lista_campeonato:
                                if c.getNome() == campeonato:
                                    for e in c.equipas:
                                        if e.getNome() == equipa:
                                            if len(e.jogadores) != 0:
                                                for j in e.jogadores:
                                                    if j.getNome() == nome:
                                                        j.mostrarJogador()
                                            else:
                                                print("\nNome não encontrado\n")
                                        else:
                                            print("\nEquipa não encontrada")
                                else:
                                    print("\nCampeonato não encontrado\n")
                        case 3: # altera nº golos
                            nome = input("Nome do jogador: ")
                            equipa = input("Equipa: ")
                            campeonato = input("Campeonato: ")
                            for c in lista_campeonato:
                                if c.getNome() == campeonato:
                                    for e in c.equipas:
                                        if e.getNome() == equipa:
                                            for j in e.jogadores:
                                                if j.getNome() == nome:
                                                    while True:
                                                        try:
                                                            golos = int(input("Nº golos: "))
                                                            break
                                                        except ValueError:
                                                            print("\nApenas números inteiros\n")
                                                    j.setGolos(golos)
                                                else:
                                                    print("\nNome não encontrado\n")
                                        else:
                                            print("\nEquipa não encontrada")
                                else:
                                    print("\nCampeonato não encontrado\n")
                        case 4: # altera nº jogos
                            nome = input("Nome do jogador: ")
                            equipa = input("Equipa: ")
                            campeonato = input("Campeonato: ")
                            for c in lista_campeonato:
                                if c.getNome() == campeonato:
                                    for e in c.equipas:
                                        if e.getNome() == equipa:
                                            for j in e.jogadores:
                                                if j.getNome() == nome:
                                                    while True:
                                                        try:
                                                            jogos = int(input("Nº jogos: "))
                                                            break
                                                        except ValueError:
                                                            print("\nApenas números inteiros\n")
                                                    j.setJogos(jogos)
                                                else:
                                                    print("\nNome não encontrado\n")
                                        else:
                                            print("\nEquipa não encontrada")
                                else:
                                    print("\nCampeonato não encontrado\n")
                        case 5: # media de golos do jogador
                            nome = input("Nome do jogador: ")
                            equipa = input("Equipa: ")
                            campeonato = input("Campeonato: ")
                            for c in lista_campeonato:
                                if c.getNome() == campeonato:
                                    for e in c.equipas:
                                        if e.getNome() == equipa:
                                            for j in e.jogadores:
                                                if j.getNome() == nome:
                                                    media = j.mediaGolos()
                                                    print(f"\nA média foi de {media:.2f} golos por jogo\n")
                                                else:
                                                    print("\nNome não encontrado\n")
                                        else:
                                            print("\nEquipa não encontrada")
                                else:
                                    print("\nCampeonato não encontrado\n")                              
                        case 0: # sair
                            break
            else:
                print("\nCrie primeiro um campeonato!\n")
        case 0: # SAIR
            print("\nVocê saiu!\n")
            break