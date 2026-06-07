# 1: Faça um programa que escreva o género 1) masculino e 2) feminino e 3) outros

print("\nEscolha uma destas opções de gênero:\n1 - Masculino\n2 - Feminino\n3 - Outros\n")
op = int(input("Insira o número que representa o seu gênero: "))
match op:
    case 1:
        genero = "masculino"
    case 2:
        genero = "feminino"
    case 3:
        genero = "outros"
    case _:
        print("\nOpção incorreta.\n")

if op in [1, 2, 3]:        
    print(f"Seu gênero é {genero}\n")
else:
    print("Escolha uma das opções válidas.\n")

# 2: Faça um programa que diga se o número é positivo, negativo ou neutro

num = int(input("Insira um número: "))
if num < 0:
    print(f"{num} é um número negativo\n")
elif num > 0:
    print(f"{num} é um número positivo\n")
else:
    print(f"{num} é um número neutro\n")

# 3: Faça um programa se idade estava [18-30] Jovem [31-60] adulto

idade = int(input("Insira uma idade: "))
if idade < 0:
    print("Idade inválida\n")
elif 18 <= idade <= 30:
    print("Você é uma pessoa jovem\n")
elif 31 <= idade <= 60:
    print("Você é um adulto\n")
else:
    print("Você tem menos de 18 ou mais de 60 anos\n")

# 4: Crie um programa em Python que peça a nota do aluno, que deve ser um float entre 0.00 e 10.0
#   Se a nota for menor que 6.0, deve exibir a nota F.
#   Se a nota for de 6.0 até 7.0, deve exibir a nota D.
#   Se a nota for entre 7.0 e 8.0, deve exibir a nota C.
#   Se a nota for entre 8.0 e 9.0, deve exibir a nota B.
#   Por fim, se for entre 9.0 e 10.0, deve exibir um belo de um A.

nota = float(input("Insira a nota do aluno (entre 0 e 10): "))
if nota < 0 or nota > 10:
    print("Nota fora dos limites\n")
elif nota < 6:
    print("Nota F\n")
elif nota < 7:
    print("Nota D\n")
elif nota < 8:
    print("Nota C\n")
elif nota < 9:
    print("Nota B\n")
else:
    print("Nota A\n")


# 5: Calcular o salário semanal de um colaborador, que recebe à hora, a partir apenas do nº de horas que este trabalhou. Sabe-se que o número de horas semanais é 36 e que o preço à hora é de 7,5€. Se o colaborador fizer horas extra (mais de 36 horas) recebe 10€ por cada hora extra. Note que não pode pedir ao utilizador para indicar as horas extra, pois é um dado que pode ser calculado

horas = int(input("Insira a quantidade de hotas trabalhadas: "))
if horas < 0:
    print("Número de horas trabalhadas negativas.\n")
elif horas <= 36:
    print(f" Com {horas} horas trabalhadas seu salário é de {horas * 7.5:.2f}€\n")
else:
    print(f"Com {horas} horas trabalhadas, seu salário é de {36 * 7.5 + (horas - 36) * 10:.2f}€\n")