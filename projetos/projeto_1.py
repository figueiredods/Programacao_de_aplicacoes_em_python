# IMPORTS:

import traceback
import random
import datetime
import time

# RASCUNHO

    # - criar uma função ou classe para gerar uma variável (dicionário contendo uma lista dentro deste) 
    #   com dados já automáticos exceto nome (value)
    # - criar função ou calsse para gerar número de conta único e sequencial aos já existentes (key), transformando em
    #   str ao final
    # - incluir key e value no dicionário contas
    # - criar uma função para guardar os movimentos
    # - função para manipular os dados (consulta saldo, levantamento, depósito, transferência)
    # - criar uma pesquisa de movimentos para últimos 10 dias
    # - criar menus
    # - tratar erros
    # - testar código
    # - incluir comentários
    
# CLASSES:

#cria nova conta padrão
class conta(dict): 
    def __init__(self, nome):
        self.nome = nome # vai solicitar o input do usuário para este campo
        self.pin = str(random.randint(1000, 10000)) # gera um pin aleatório com 4 dígitos enter número 1000 e 9999
        self.__saldo = 1000.00 # instância protegida # saldo padrão e protegido contra alterações por erro
        self.iban = "PT50000"+ str(random.randint(0000000000, 9999999999)) # gera um código de iban de digitos iniciais e tamanho padrão
        self.movimento = [] # lista de movimentos
        

    def add(self): # coloca os dados dos clientes em um dicionário
        return {"titular": self.nome, "pin": self.pin, "saldo": self.__saldo, "iban": self.iban, "movimentos": self.movimento}
    
    def __str__(self): # padrão de print para o comando 'print(objeto)'
        return f"Titular: {self.nome}, Pin: {self.pin}, Saldo: {self.__saldo}, Iban: {self.iban}"
    
# FUNÇÕES:

# registro de movimentos
def movimentos(tipo, valor, destino,  descricao, data = datetime.datetime.now()): # função modelo para movimentos
    return {"tipo": tipo, "valor": float(valor), "data": data , "destino": destino, "descrição": descricao}

# gera número de conta
def numContas(): # retorna o número da nova conta
    keys = []
    #num = None
    for key in contas.keys():
        keys.append(int(key))
    num = max(keys) + 1
    return str(num)

# contagem regressiva
def contagem_regressiva(segundos):
    while segundos >= 0:
        mins, secs = divmod(segundos, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(f"{"*" * 5} Tempo restante: {timer} {"*" * 5}", end="\r", flush=True)
        time.sleep(1)
        segundos -= 1
    
    print(f"\n\n{"-" * 38}")
    print(f"Tempo esgotado. Você tem 3 tentativas.")
    print(f"{"-" * 38}\n")

# VARIÁVEL INICIAL PARA CONTAS

contas = {
    "1001": {
        "titular": "João Silva",
        "pin": "1234",
        "saldo": 1000.00,
        "iban": "PT500001002003004",
        "movimentos": [
            {
                "tipo": "Depósito",
                "valor": 200,
                "data": datetime.datetime.now(),
                "destino": None,
                "descrição": "Depósito em numerário"
            },
            {
                "tipo": "Transferência",
                "valor": 100,
                "data": (datetime.datetime.now() - datetime.timedelta(days = 11)),
                "destino": "PT500009999999999",
                "descrição": "Transferência bancária"
            }
        ]
    },
    "1002": {
        "titular": "Maria Costa",
        "pin": "4321",
        "saldo": 2500.00,
        "iban": "PT500005555555555",
        "movimentos": [
            {
                "tipo": "Levantamento",
                "valor": 50,
                "data": datetime.datetime.now(),
                "destino": None,
                "descrição": "Levantamento ATM"
            }
        ]
    },
    "1003": {
        "titular": "Pedro Santos",
        "pin": "5678",
        "saldo": 500.00,
        "iban": "PT500007777777777",
        "movimentos": []
    }
}

# CÓDIGO PRINCIPAL

error_log = [] # variável para guardar os error
while True:
    try:
        print(f"\n{"="* 10} LOGIN {"="* 10}\n")
        print("1 - Titular da conta\n2 - Administrador\n9 - Sair\n")
        acesso = int(input("Escolha uma opção: ")) # try except para valueError
        match acesso:
            case 1: # Menu do utilizador
                    c = 0 # contador de tentativas de senha
                    while True:
                        try:
                            c += 1 # implementa 1 valor no contador
                            n_conta = input("Insira o número da conta: ") # KeyError
                            palavra_passe = input("Insira seu código pin: ")
                            if n_conta in contas and palavra_passe == contas[n_conta]["pin"]: # login para acesso a conta
                                print(f"\n{"-" * 16}")
                                print(f"Acesso liberado.")
                                print(f"{"-" * 16}\n")
                                while True:
                                    try:
                                        print(f"\n{"$"* 10} MENU DO UTILIZADOR {"$"* 10}\n")
                                        print("1 - Consultar saldo\n2 - Realizar levantamento\n3 - Realizar depósito\n4 - Realizar transferência\n5 - Consultar movimentos (últimos 10 dias)\n6 - Sair\n")
                                        op = int(input("Esolha uma opção: ")) # ValueError
                                        match op:
                                            case 1:
                                                print(f"\nSeu saldo atual é {contas[n_conta]["saldo"]:.2f}€\n")
                                            case 2:
                                                while True:
                                                    try:
                                                        valor = float(input("Quanto deseja levantar? ")) # ValueError
                                                        if valor < 0:
                                                            print(f"O valor informado é menor que zero")
                                                            break
                                                        elif valor <= contas[n_conta]["saldo"]:
                                                            contas[n_conta]["saldo"] -= valor
                                                            contas[n_conta]["movimentos"].append(movimentos("Levantamento", valor, None, "Levantamento ATM"))
                                                            print(f"\nSeu saldo agora é {contas[n_conta]["saldo"]:.2f}€\n")
                                                            break
                                                        else:
                                                            print(f"\n{"-" * 19}")
                                                            print(f"Saldo insuficiente.")
                                                            print(f"{"-" * 19}\n")
                                                            break
                                                    except ValueError as err:
                                                        error_log.append(traceback.format_exc())
                                                        print(f"\n{"-" * 30}")
                                                        print(f"O valor digitado não é valido.")
                                                        print(f"{"-" * 30}\n")
                                                        break      
                                            case 3:
                                                while True:
                                                    try:
                                                        valor = float(input("Quanto deseja depositar? ")) # ValueError
                                                        if valor < 0:
                                                            print(f"O valor informado é menor que zero")
                                                            break
                                                        else:
                                                            contas[n_conta]["saldo"] += valor
                                                            contas[n_conta]["movimentos"].append(movimentos("Depósito", valor, None, "Depósito em numerário"))
                                                            print(f"\nSeu saldo agora é {contas[n_conta]["saldo"]:.2f}€\n")
                                                            break
                                                    except ValueError as err:
                                                        error_log.append(traceback.format_exc())
                                                        print(f"\n{"-" * 30}")
                                                        print(f"O valor digitado não é valido.")
                                                        print(f"{"-" * 30}\n")
                                                        break
                                            case 4:
                                                while True:
                                                    try:    
                                                        n_conta_d = input("Informe o número da conta destino: ") # KeyError
                                                        if n_conta_d not in contas:
                                                            raise KeyError
                                                        valor = float(input("Quanto deseja transferir? ")) # ValueError
                                                        if valor < 0:
                                                            print(f"O valor informado é menor que zero")
                                                            break
                                                        elif valor <= contas[n_conta]["saldo"]:
                                                            contas[n_conta]["saldo"] -= valor
                                                            contas[n_conta_d]["saldo"] += valor
                                                            contas[n_conta]["movimentos"].append(movimentos("Transferência", valor, n_conta_d, "Transferência bancária"))
                                                            print(f"\nSeu saldo agora é {contas[n_conta]["saldo"]:.2f}€\n")
                                                            break
                                                        else:
                                                            print(f"\n{"-" * 19}")
                                                            print(f"Saldo insuficiente.")
                                                            print(f"{"-" * 19}\n")
                                                            break
                                                    except KeyError as err:
                                                        error_log.append(traceback.format_exc())
                                                        print(f"\n{"-" * 33}")
                                                        print(f"Número de conta {n_conta_d} inexistente.")
                                                        print(f"{"-" * 33}\n")
                                                    except ValueError as err:
                                                        error_log.append(traceback.format_exc())
                                                        print(f"\n{"-" * 30}")
                                                        print(f"O valor digitado não é valido.")
                                                        print(f"{"-" * 30}\n")
                                            case 5:
                                                print(f"\n{"="* 10} Movimentos: {"="* 10}\n")
                                                hoje = datetime.datetime.now() - datetime.timedelta(days = 10) # cria uma data 10 dias menos que o dia atual
                                                for i in contas[n_conta]["movimentos"]: # print dos dados das contas
                                                    if i["data"] >= hoje: # verifica se a data está dentro dos últimos 10 dias
                                                        for chave, valores in i.items():
                                                            if chave == "data":
                                                                date = datetime.datetime.strftime(valores, "%Y-%m-%d %H:%M")
                                                                print(f"{chave}: {date}")
                                                            elif chave == "valor":
                                                                print(f"{chave}: {valores:.2f}")
                                                            else:
                                                                print(f"{chave}: {valores}")
                                                    print("")
                                            case 6:
                                                break
                                            case _:
                                                print(f"\n{"-" * 50}")
                                                print("Opção inexistente. Escolha uma número entre 1 e 6.")
                                                print(f"{"-" * 50}\n")
                                    except ValueError as err:
                                        error_log.append(traceback.format_exc())
                                        print(f"\n{"-" * 57}")
                                        print("Você não digitou um número. Digite um número entre 1 e 6.")
                                        print(f"{"-" * 57}\n")
                                break
                            elif c < 3:
                                print(f"\n{"-" * 26}")
                                print(f"Conta ou senha incorretos\nVocê tem mais {3-c} tentativas.")
                                print(f"{"-" * 26}\n")
                            else:
                                print("")
                                contagem_regressiva(10)
                                break
                        except KeyError as err:
                            error_log.append(traceback.format_exc())
                            print(f"\n{"-" * 33}")
                            print(f"Número de conta {n_conta} inexistente.")
                            print(f"{"-" * 33}\n")
            case 2: # Menu do Administrador
                c = 0 # contador de tentativas de senha
                while True:
                    c += 1 # implementa 1 valor no contador
                    usuario = input("Insira seu usuário: ")
                    senha = input("Insira sua senha: ")
                    if usuario == "Python" and senha == "Atec": # login para acesso ao admin
                        print(f"\n{"-" * 16}")
                        print(f"Acesso liberado.")
                        print(f"{"-" * 16}\n")
                        while True:
                            try:
                                print(f"\n{"#"* 10} MENU DO ADMIN {"#"* 10}\n")
                                print("1 - Add conta\n2 - Listar contas\n3 - Apagar conta\n7 - Sair\n")
                                op = int(input("Esolha uma opção: ")) # try except para valueError
                                match op:
                                    case 1:
                                        nome = conta(input("Insira o nome do titular da conta: "))
                                        mydic = nome.add()
                                        num = numContas() # cria um novo número de conta
                                        contas[num] = mydic # adiciono ao dicionário número de conta e os dados do titular
                                    case 2:
                                        for k, v in contas.items(): # print dos dados das contas
                                            print(f"\n{"*" * 40}")
                                            print(f"Conta número: {k}")
                                            print(f"{"*" * 40}\n")
                                            for key, value in v.items():
                                                if key == "movimentos":
                                                    pass
                                                else:
                                                    if key == "saldo":
                                                        print(f"{key}: {value:.2f}€")
                                                    else:
                                                        print(f"{key}: {value}")
                                    case 3:
                                        while True:
                                            try:
                                                n_conta = input("Informe o número da conta que deseja apagar: ") # KeyError
                                                if n_conta not in contas:
                                                    raise KeyError
                                                op = input(f"Se deseja apagar a conta {n_conta} escreva SIM: ")
                                                if op != "SIM":
                                                    print(f"\n{"-" * 42}")
                                                    print(f"Você não confirmou o apagamento da conta.")
                                                    print(f"{"-" * 42}\n")
                                                    break
                                                else:
                                                    del contas[n_conta]
                                                    print(f"\n{"-" * 31}")
                                                    print(f"Conta {n_conta} apagada com sucesso.")
                                                    print(f"{"-" * 31}\n")
                                                    break
                                            except KeyError as err:
                                                error_log.append(traceback.format_exc())
                                                print(f"\n{"-" * 33}")
                                                print(f"Número de conta {n_conta} inexistente.")
                                                print(f"{"-" * 33}\n")
                                    case 7:
                                        break
                                    case _:
                                        print(f"\n{"-" * 74}")
                                        print("Número inválido! Por favor digite um número dentro das opções disponíveis.")
                                        print(f"{"-" * 74}\n")
                            except ValueError as err:
                                error_log.append(traceback.format_exc())
                                print(f"\n{"-" * 57}")
                                print("Você não digitou um número. Digite um número entre 1 e 6.")
                                print(f"{"-" * 57}\n")
                        break
                    elif c < 3:
                        print(f"\n{"-" * 26}")
                        print(f"Usuário ou senha incorretos\nVocê tem mais {3-c} tentativas.")
                        print(f"{"-" * 26}\n")
                    else:
                        print("")
                        contagem_regressiva(10)
                        break
            case 9:
                break
            case _:
                print(f"\n{"-" * 37}")
                print("Opção inexistente. Escolha 1, 2 ou 9.")
                print(f"{"-" * 37}\n")
    except ValueError as err2:
        error_log.append(traceback.format_exc())
        print(f"\n{"-" * 45}")
        print("Você não digitou um número. Digite 1, 2 ou 9.")
        print(f"{"-" * 45}\n")
print(f"\n\n{"="* 10} PRINT ERROS {"="* 10}\n")
c=1
for el in error_log:
    print(f"{c}-{el}\n")
    c+=1