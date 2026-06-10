# 1: Faça um programa que peça 7 números e some só os números pares

numeros = []
pares = []
for i in range(7):
    while True:
        try:
            num = int(input(f"insira o {i+1} número: "))
            if num % 2 == 0:
                pares.append(num)
            break
        except ValueError:
            print("\nInsira apenas números inteiros\n")
print(f"\nA soma dos números pares inseridos é {sum(pares)}\n")

# 2: Crie um programa que vá pedindo números ao utilizador até a soma ser superior a 100

soma = 0
count = 1
while soma <= 100:
    try:
        num = int(input(f"Insira o {count}º número: "))
        soma += num
        count += 1
    except ValueError:
        print("\nInsira apenas números inteiros\n")
print(f"\nO total dos {count} números inseridos é {soma}\n")

# 3: Crie um programa com while True que peça um numero entre 0-20, caso contrário pergunte novamente até colocar direito.

while True:
    try:
        num = int(input("Insrira um número inteiro entre 0 e 20: "))
        if 0 <= num <= 20:
            print(f"\nNúmero {num} inserido com sucesso\n")
            break
        else:
            print(f"\nNúmero inserido {num} fora do range permitido\n")
    except ValueError:
        print("\nInsira apenas um número inteiro entre os valores 0 e 20\n")

# 4: Crie um programa usando o while que some os números que estão compreendidos entre 10 e 20, quando colocar 1 ele sai fora. No fim apresenta a soma desses números que estão nesse intervalo

soma = 0
num = 0
while num != 1:
    try:
        num = int(input("Insira um número inteiro: "))
        if 10 <= num <= 20:
            soma += num
    except ValueError:
        print("\nInsira apenas números inteiros!\n")
print("\nVocê saiu do programa!\n")
print(f"\nA soma dos números inseridos é {soma}\n")

# 5: Faça um programa com for in range que imprima Viva ao Porto 10 vezes, faça uma nova versão que seja o utilizador a dizer o número de vezes que quer que repita.

for i in range(10):
    print("Viva ao Porto")
print("")

while True:
    try:
        num = int(input("Insira quantas vezes deseja repetir a frase: "))
        if num >= 0:
            for i in range(num):
                print("Viva Matosinhos")
            break
        else:
            print("\nInsira um número positivo!\n")
    except ValueError:
        print("\nInsira apenas números inteiros!\n")
print("")

# 6: Faça um programa usando o range que some só pares de 0 até 20

soma = 0
while True:
    try:
        num = int(input("Insira um número positivo ou digite um número negativo para sair: "))
        if num < 0:
            break
        elif 0 <= num <= 20 and num % 2 == 0:
            soma += num
    except ValueError:
        print("\nInsira apenas números inteiros!\n")
print("\nVocê saiu do programa!\n")
print(f"\nA soma dos números pares entre 0 e 20 é {soma}\n")

# 7: Faça a tabuada pedindo o numero em questão ao utilizador. (7x1=7…7x10=70)

while True:
    try:
        num = int(input("Digite um número entre 1 e 9 para a tabuada: "))
        if 1 <= num <= 9:
            for i in range(10):
                print(f"{num} x {i+1} = {num * (i+1)}")
            break
        else:
            print("\nNúmero inserido fora do range 1 - 9!\n")
    except ValueError:
        print("\nDigite apenas números inteiros entre 1 e 9!\n")

# 8: Crie um script que simule um sistema de login, definimos previamente o Username Password certos. O programa pedirá para introduzir o Username e password, o programa só sai se acertar ambos(username e password), coloque uma mensagem (“ Acertou no Login) Deve avisar o utilizador que falhou (username/ password errado). Após 3 tentativas o programa deverá lançar uma mensagem “ Foi bloqueado” e fazer o respectivo break

username = "Pato"
password = "1234"
while True:
    user = input("Insira seu Username: ")
    senha = input("Insira sua senha: ")
    if user == username and senha == password:
        print("\nAcertou o login!\n")
        break
    else:
        print("\nUsuário ou senha inválidos. Tente novamente!\n")