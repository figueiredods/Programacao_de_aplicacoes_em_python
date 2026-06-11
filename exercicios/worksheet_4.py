# 1: Crie uma função que calcule a área de retângulo

while True:
    try:
        base = float(input("Insira a medida da base: "))
        altura = float(input("Insira a medida da altura: "))
        print(f"\nA área do triângulo de base {base} e altura {altura} é {base * altura / 2:.2f}\n")
        break
    except ValueError:
        print("\nInsira apenas valores numéridos!\n")

# 2: Calcular o salário semanal de um colaborador, que recebe à hora, a partir apenas do nº de horas que este trabalhou. Sabe-se que o número de horas semanais é 36 e que o preço à hora é de 7,5€. Se o colaborador fizer horas extra (mais de 36 horas) recebe 10€ por cada hora extra. Note que não pode pedir ao utilizador para indicar as horas extra, pois é um dado que pode ser calculado

while True:
    try:
        h_trabalho = int(input("Informe quantas horas trabalhou na semana: "))
        if 0 <= h_trabalho <= 36:
            print(f"\nCom {h_trabalho} horas trabalhadas nesta semana, seu salário será de {h_trabalho * 7.5:.2f}€\n")
            break
        elif 36 < h_trabalho:
            print(f"\nVocê trabalhou mais de 36 horas esta semana, fazendo {h_trabalho - 36} horas extras, fazendo assim jus a um salário de {(36 * 7.5) + ((h_trabalho - 36) * 10):.2f}€\n")
            break
    except ValueError:
        print("\nInsira apenas valores numéricos!\n")

# 3: Faça uma função em Python que recebe dois números e um operador (+, -, *, /) e retorna o resultado da operação

while True:
    try:
        num1 = float(input("Insira o 1º número: "))
        num2 = float(input("Insira o 2º número: "))
        break
    except ValueError:
        print("\nInsira apenas números!\n")
print("\nMenu de operações possíveis:\n'+' - para soma\n'-' - para divisão\n'*' - para multiplicação\n'/' - para divisão ")
op = input("\nIndique a operação desejada: ")
if op in ("+", "-", "*", "/"):
    match op:
        case '+':
            print(f"\nA soma de {num1} com {num2} é {num1 + num2:.2f}\n")
        case '-':
            print(f"\nA subtração {num1} menos {num2} é {num1 - num2:.2f}\n")
        case '*':
            print(f"\nA multiplicação de {num1} por {num2} é {num1 * num2:.2f}\n")
        case '/':
            if num2 != 0:
                print(f"\nA divisão de {num1} por {num2} é {num1 / num2:.2f}\n")
            else:
                print("\nDivisor não pode ser um valor nulo!\n")
else:
    print("\nOpção inválida!\n")
        

# 4: Crie um menu usando a instrução match ( 1- Query, 2-Register , 3- Delete , 4- sair) , use o default também.

lista_nomes = []
while True:
    while True:
        try:
            print(f"\nMenu:\n{"-" * 20}\n1 - Insert a name\n2 - Show data\n3 - Delete data\n4 - Exit\n")
            op = int(input("Escolha uma opção: "))
            break
        except ValueError:
            print("\nEscolha apenas valores numéricos inteiros!\n")
    match op:
        case 1:
            nome = input("Digite o nome a ser inserido: ")
            lista_nomes.append(nome)
        case 2:
            print(f"\nLista de nomes:\n{"-" * 20}\n")
            [print(nome) for nome in lista_nomes]
        case 3:
            print("\nQual nome deseja apagar da lista?\n")
            [print(nome) for nome in lista_nomes]
            nome = input("\nDigite o nome: ")
            if nome in lista_nomes:
                lista_nomes.remove(nome)
                print(f"\n{nome} removido com sucesso!\n")
            else:
                print(f"\nO nome {nome} não pertencem a lista\n")
        case 4:
            print("\nVolte sempre!\n")
            break
        case _:
            print("\nOpção inexistente!\n")
    
# 5: Faça uma função que imprima a tabuada

while True:
    try: # handle a error if the input is not an integer
        global num # make the variable 'num' a global variable
        num = int(input("Insira o número que deseja ver a tabuada: "))
        break
    except ValueError:
        print("\nInsira apenas um número inteiro!\n")
if num < 0: # checking if the number is not lower than 0
    print("\nInsira apenas número positivo!\n")
else:
    [print(f"{num} x {i} = {num * i}") for i in range(1, 10)]
    
