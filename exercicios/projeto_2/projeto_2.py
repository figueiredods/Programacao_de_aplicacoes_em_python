# Imports
from Jogador import Jogador
from Equipa import Equipa
from Campeonato import Campeonato

lista_campeonato = []
lista_equipas = []
while True:
    print("\nMenu:\n1 - Criar Campeonato\n2 - Criar Equipe\n3 - Criar Jogador\n4 - Listar equipas\n5 - Lista jogadores\n ")
    while True:
        try:
            op = int(input("Escolha uma opção:"))
            break
        except ValueError:
            print("\nApenas números inteiros\n")
    match op:
        case 1:
            liga = Campeonato(input("Informe o nome do Campeonato que deseja criar: "))
            lista_campeonato.append(liga)
            for i in lista_campeonato:
                print(i.getNome())
        case 2:
            if len(lista_campeonato) != 0:
                equipa = Equipa(input("Nome da equipa:"), input("Cidade da equipa:"))
                liga = input("Insira o nome do campeonato que vai inserir a equipa: ")
                for i in lista_campeonato:
                    if i.getNome() == liga:
                        i.adicionarEquipa(equipa)
                for i in lista_campeonato:
                    i.listarEquipas()
        case 3:
            if len(lista_campeonato) != 0:
                nome = input("Insira o nome do jogador: ")
                posicao = input("Informe a posicção do jogador: ")
                try:
                    golos = int(input("Insira o número do golos: "))
                    jogos = int(input("Insira o número do jogos: "))
                except ValueError:
                    print("\nInsira um número inteiro\n")
                jogador = Jogador(nome, posicao, golos, jogos)
                equipa = input("Informe a quipa que o jogador pertence: ")
                for i in lista_campeonato:
                    if i.procurarEquipa(equipa):
                        a = i.procurarEquipa(equipa)
                        a.adicionarJogador(jogador)
                    else:
                        print("\nEquipa não encontrada\n")
                        i.listarEquipas()
                for i in lista_campeonato:
                    for c in i.equipas:
                        c.mostrarJogadores()
        case 4:
            liga = input("Insira o nome do campeonato para listas as equipas: ")
            for i in lista_campeonato:
                if i.getNome() == liga:
                    i.listarEquipas()
        case 5:
            eq = input("Informe a quipa que o jogador pertence: ")
            eq = liga.procurarEquipa(eq)
            eq.mostrarJogadores()