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
                print("\n1 - Criar campeonato\n2 - Listar equipas\n3 - Calcular média de golos do campeonato\n4 - Listar campeonatos\n5 - Apagar campeonato\n0 - Sair")
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
                        print("\nLista de campeonatos")
                        print("-" * 40)
                        for c in lista_campeonato:
                            print(f"- {c.getNome()}")
                    case 2: # lista equipas
                        if len(lista_campeonato) != 0: # verifica se a lista de campeonatos está vazia
                            campeonato = input("Nome do campeonato: ")
                            for i in lista_campeonato:
                                if i.getNome() == campeonato: # verifica se os nomes coincidem
                                    if len(i.equipas) != 0:
                                        i.listarEquipas()
                                    else:
                                        print("\nCampeonato sem equipas\n")
                        else:
                            print("\nCrie primeiro um campeonato!\n")
                    case 3: # calcula media de golos do campeonato
                        if len(lista_campeonato) != 0: # verifica se a lista de campeonatos está vazia
                            campeonato = input("Nome do campeonato: ")
                            for i in lista_campeonato:
                                if i.getNome() == campeonato: # verifica se os nomes coincidem
                                    if len(i.equipas) != 0:
                                        print(f"\nMédia de golos: {i.mediaGolos():.2f}\n")
                                    else:
                                        print("\nCampeonato sem equipas\n")
                        else:
                            print("\nCrie primeiro um campeonato!\n")
                    case 4: # Apagar campeonatos
                        if len(lista_campeonato) != 0: # verifica se a lista de campeonatos está vazia
                            print("\nLista de campeonatos")
                            print("-" * 40)
                            for c in lista_campeonato:
                                print(f"- {c.getNome()}")
                            print(" ")
                        else:
                            print("\nCrie primeiro um campeonato!\n")
                    case 5:
                        if len(lista_campeonato) != 0: # verifica se a lista de campeonatos está vazia
                            campeonato = input("Nome do campeonato: ")
                            for i in lista_campeonato:
                                if i.getNome() == campeonato: # verifica se os nomes coincidem
                                    lista_campeonato.remove(i)
                                    print("\nCampeonato apagado\n")
                    case 0: # sair
                        break
        case 2: # MENU EQUIPA
            if len(lista_campeonato) != 0: # verifica se a lista de campeonatos está vazia
                while True:
                    print("\nMenu Equipa")
                    print("-" * 40)
                    print("\n1 - Criar equipa\n2 - Listar jogadores\n3 - Total de golos da equipa\n4 - Apagar equipa\n0 - Sair")
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
                            if campeonato in [c.getNome() for c in lista_campeonato]: # verifica se o campeonato está na lista
                                for c in lista_campeonato:
                                    if c.getNome() == campeonato: # verifica se nomes coincidem
                                        equipa = input("Nome da equipa: ")
                                        if equipa in [e.getNome() for e in c.equipas]: # Verifica se já existe o nome da equipa na lista de equipas do campeonato
                                            print("\nEquipa já existente na lista\n")
                                        else:
                                            cidade = input("Cidade da equipa: ")
                                            c.adicionarEquipa(Equipa(equipa, cidade))
                            else:
                                print("\nCampeonato não encontrado\n") # print errado
                        case 2: # lista jogadores
                            campeonato = input("Insira o nome do campeonato desta equipa: ")
                            if campeonato in [c.getNome() for c in lista_campeonato]: # verifica se o campeonato está na lista
                                for c in lista_campeonato:
                                    if c.getNome() == campeonato: # Verifica se nomes são iguais
                                        if len(c.equipas) != 0: # Verifica se a lista de quipas está vazia
                                            equipa = input("Informe a equipa que procura: ")
                                            if equipa in [e.getNome() for e in c.equipas]: # Verifica se a equipa está presente na lista
                                                for e in c.equipas:
                                                    if e.getNome() == equipa: # Verifica se nomes são iguais
                                                        if len(e.jogadores) != 0: # Verifica se a lista de jogadores está vazia
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
                            campeonato = input("Insira o nome do campeonato desta equipa: ")
                            if campeonato in [c.getNome() for c in lista_campeonato]: # verifica se o campeonato está na lista
                                for c in lista_campeonato:
                                    if c.getNome() == campeonato: # verifica se os nomes coincidem
                                        if len(c.equipas) != 0: # existem equipas?
                                            equipa = input("Informe a equipa que procura: ")
                                            if equipa in [e.getNome() for e in c.equipas]: # equipa está na lista de equipas?
                                                for e in c.equipas:
                                                    if e.getNome() == equipa: # verifica se os nomes coincidem
                                                        gols = e.totalGolos()
                                                        print(f"\nO total de golos desta equipa é {gols}\n")
                                            else:
                                                print("\nEquipe não encontrada\n")
                                    else:
                                        print("\nCampeonato sem equipas\n")    
                            else:
                                print("\nCampeonato não encontrado\n")   
                        case 4: # Apagar equipa
                            campeonato = input("Insira o nome do campeonato desta equipa: ")
                            if campeonato in [c.getNome() for c in lista_campeonato]: # verifica se o campeonato está na lista
                                for c in lista_campeonato:
                                    if c.getNome() == campeonato: # Verifica se nomes são iguais
                                        if len(c.equipas) != 0: # Verifica se a lista de quipas está vazia
                                            equipa = input("Informe a equipa que procura: ")
                                            if equipa in [e.getNome() for e in c.equipas]: # Verifica se a equipa está presente na lista
                                                c.removerEquipa(equipa)
                                                print("\nEquipa apagada com sucesso!\n")
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
            if len(lista_campeonato) and [len(c.equipas) != 0 for c in lista_campeonato]!= 0: # verifica se a lista de campeonatos está vazia
                # for c in lista_campeonato:
                #     if len(c.equipas) != 0: # Verifica se lista equipas está vazia
                        while True:
                            print("\nMenu Jogador")
                            print("-" * 40)
                            print("\n1 - Criar jogador\n2 - Mostrar dados\n3 - Alterar nº golos\n4 - Alterar nº jogos\n5 - Calcular média de golos por jogo\n6 - Apagar jogador\n0 - Sair")
                            while True:
                                try:
                                    op = int(input("Escolha uma opção: "))
                                    break
                                except ValueError:
                                    print("\nDigite apenas núneros inteiros!\n")
                            match op:
                                case 1: # cria jogador
                                    campeonato = input("Campeonato: ")
                                    if campeonato in [c.getNome() for c in lista_campeonato]: # verifica se o campeonato está na lista
                                        for c in lista_campeonato:
                                            if c.getNome() == campeonato: # verifica se os nomes coincidem
                                                equipa = input("Equipa: ")
                                                if equipa in [e.getNome() for e in c.equipas]: # Verifica se equipe está na lista
                                                    for e in c.equipas:
                                                        if e.getNome() == equipa: # verifica se os nomes coincidem
                                                            nome = input("Nome do jogador: ")
                                                            posicao = input("Posição: ")
                                                            while True:
                                                                try:
                                                                    golos = int(input("Nº golos: "))
                                                                    jogos = int(input("Nº jogos: "))
                                                                    break
                                                                except ValueError:
                                                                    print("\nApenas números inteiros\n")
                                                            jogador = Jogador(nome, posicao, golos, jogos)
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
                                    campeonato = input("Campeonato: ")
                                    if campeonato in [c.getNome() for c in lista_campeonato]: # verifica se o campeonato está na lista
                                        for c in lista_campeonato:
                                            if c.getNome() == campeonato: # verifica se os nomes coincidem
                                                equipa = input("Equipa: ")
                                                if equipa in [e.getNome() for e in c.equipas]: # Verifica se equipe está na lista
                                                    for e in c.equipas:
                                                        if e.getNome() == equipa: # verifica se os nomes coincidem
                                                            if len(e.jogadores) != 0:
                                                                nome = input("Nome do jogador: ")
                                                                if nome in [j.getNome() for j in e.jogadores]: # Verifica se jogador está na lista
                                                                    for j in e.jogadores:
                                                                        if j.getNome() == nome: # verifica se os nomes coincidem
                                                                            j.mostrarJogador()
                                                                else:
                                                                    print("\nJogador não encontrado\n")
                                                else:
                                                    print("\nEquipa não encontrada")
                                    else:
                                        print("\nCampeonato não encontrado\n")
                                case 3: # altera nº golos
                                    campeonato = input("Campeonato: ")
                                    if campeonato in [c.getNome() for c in lista_campeonato]: # verifica se o campeonato está na lista
                                        for c in lista_campeonato:
                                            if c.getNome() == campeonato: # verifica se os nomes coincidem
                                                equipa = input("Equipa: ")
                                                if equipa in [e.getNome() for e in c.equipas]: # Verifica se equipe está na lista
                                                    for e in c.equipas:
                                                        if e.getNome() == equipa: # verifica se os nomes coincidem
                                                            if len(e.jogadores) != 0:
                                                                nome = input("Nome do jogador: ")
                                                                if nome in [j.getNome() for j in e.jogadores]: # Verifica se jogador está na lista
                                                                    for j in e.jogadores:
                                                                        if j.getNome() == nome: # verifica se os nomes coincidem
                                                                            while True:
                                                                                try:
                                                                                    golos = int(input("Nº golos: "))
                                                                                    break
                                                                                except ValueError:
                                                                                    print("\nApenas números inteiros\n")
                                                                            j.setGolos(golos)
                                                                else:
                                                                    print("\nJogador não encontrado\n")
                                                else:
                                                    print("\nEquipa não encontrada")
                                    else:
                                        print("\nCampeonato não encontrado\n")
                                case 4: # altera nº jogos
                                    campeonato = input("Campeonato: ")
                                    if campeonato in [c.getNome() for c in lista_campeonato]: # verifica se o campeonato está na lista
                                        for c in lista_campeonato:
                                            if c.getNome() == campeonato: # verifica se os nomes coincidem
                                                equipa = input("Equipa: ")
                                                if equipa in [e.getNome() for e in c.equipas]: # Verifica se equipe está na lista
                                                    for e in c.equipas:
                                                        if e.getNome() == equipa: # verifica se os nomes coincidem
                                                            if len(e.jogadores) != 0:
                                                                nome = input("Nome do jogador: ")
                                                                if nome in [j.getNome() for j in e.jogadores]: # Verifica se jogador está na lista
                                                                    for j in e.jogadores:
                                                                        if j.getNome() == nome: # verifica se os nomes coincidem
                                                                            while True:
                                                                                try:
                                                                                    jogos = int(input("Nº jogos: "))
                                                                                    break
                                                                                except ValueError:
                                                                                    print("\nApenas números inteiros\n")
                                                                            j.setJogos(jogos)
                                                                else:
                                                                    print("\nJogador não encontrado\n")
                                                else:
                                                    print("\nEquipa não encontrada")
                                    else:
                                        print("\nCampeonato não encontrado\n")
                                case 5: # media de golos do jogador
                                    campeonato = input("Campeonato: ")
                                    if campeonato in [c.getNome() for c in lista_campeonato]: # verifica se o campeonato está na lista
                                        for c in lista_campeonato:
                                            if c.getNome() == campeonato: # verifica se os nomes coincidem
                                                equipa = input("Equipa: ")
                                                if equipa in [e.getNome() for e in c.equipas]: # Verifica se equipe está na lista
                                                    for e in c.equipas:
                                                        if e.getNome() == equipa: # verifica se os nomes coincidem
                                                            if len(e.jogadores) != 0:
                                                                nome = input("Nome do jogador: ")
                                                                if nome in [j.getNome() for j in e.jogadores]: # Verifica se jogador está na lista
                                                                    for j in e.jogadores:
                                                                        if j.getNome() == nome: # verifica se os nomes coincidem
                                                                            media = j.mediaGolos()
                                                                            print(f"\nA média foi de {media:.2f} golos por jogo\n")
                                                                else:
                                                                    print("\nJogador não encontrado\n")
                                                else:
                                                    print("\nEquipa não encontrada")
                                    else:
                                        print("\nCampeonato não encontrado\n") 
                                case 6: # Apagar jogador
                                    campeonato = input("Campeonato: ")
                                    if campeonato in [c.getNome() for c in lista_campeonato]: # verifica se o campeonato está na lista
                                        for c in lista_campeonato:
                                            if c.getNome() == campeonato: # verifica se os nomes coincidem
                                                equipa = input("Equipa: ")
                                                if equipa in [e.getNome() for e in c.equipas]: # Verifica se equipe está na lista
                                                    for e in c.equipas:
                                                        if e.getNome() == equipa: # verifica se os nomes coincidem
                                                            if len(e.jogadores) != 0:
                                                                nome = input("Nome do jogador: ")
                                                                if nome in [j.getNome() for j in e.jogadores]: # Verifica se jogador está na lista
                                                                    e.removerJogador(nome)
                                                                    print("\nJogador removido com sucesso!\n")
                                                                else:
                                                                    print("\nJogador não encontrado\n")
                                                else:
                                                    print("\nEquipa não encontrada")
                                    else:
                                        print("\nCampeonato não encontrado\n")                              
                                case 0: # sair
                                    break
            else:
                print("\nCrie primeiro um campeonato e uma Equipa!\n")
        case 0: # SAIR
            print("\nVocê saiu!\n")
            break