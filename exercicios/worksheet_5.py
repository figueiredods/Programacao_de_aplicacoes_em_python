# Imports
import random

# 1: Cria uma lista com 5 números pedidos ao utilizador.

lista = [] # empty list
while True:
    try:
        for i in range(1, 6):
            num = float(input(f"Insira o {i}º número: "))
            lista.append(num) # insert the number into the list 'lista'
        break
    except ValueError: # to handle error
        print("\nInsira apenas números!\n")
[print(f"{i:.2f}") for i in lista]

# 2: Altere o exercício anterior para obrigar a números entre 0-20, caso nao esteja faça a pergunta novamente

lista = []
for i in range(1, 6): # create a loop
    while True: # make the code run until break
        try: #handle errors
            num = float(input(f"Insira o {i}º número, entre os valores 0 e 20: "))
            if num not in range(0, 21): # check if the number is between 0 and 20
                raise Exception # rise a specific error to this
            else:
                lista.append(num) # add number to a list 'lista'
                break
        except ValueError:
            print("\nInsira apenas números!\n")
        except Exception:
            print("\nFora do intervalo permitido!\n")

[print(i) for i in lista] # print lista

# 3: Dada uma lista=[3,2,5,6,8,10,12,7] percorra a lista e separe os pares para a Lista_pares[] e os impares para a Lista_impares[]

lista=[3,2,5,6,8,10,12,7]
Lista_pares = []
Lista_impares = []
for i in lista:
    if i % 2 == 0:
        Lista_pares.append(i)
    else:
        Lista_impares.append(i)
print("\nLista dos números pares:")
[print(i) for i in Lista_pares]
print("\nLista dos números ímpares:")
[print(i) for i in Lista_impares]

# 4: Dada uma lista=[4,1,8,3,5,8,6,9] imprima só os valores que são iguais ao seu índice 0 1 2 3 4 5 6 7 [ 4 , 1 , 8, 3 , 5 , 8 , 6 , 9]

lista = [4,1,8,3,5,8,6,9]
print("\nLista cujo índice e número são iguais:")
for i in range(len(lista)): # loop using the len of lista to each round 'i' receive the index
    if i == lista[i]:
        print(f"Índice: {i} - número: {lista[i]}")

# 5: Começando com uma lista vazia [ ] Faça um menu com as seguintes funcionalidades: 1- Maximo da lista 2- Minimo da lista 3- Soma da lista 4- Adicionar Numero 5- Remover Numero valor 6- Média 7- Imprimir Lista 8- Sair

lista = []
while True:
    try:
        print(f"\nMENU:\n{"-" * 20}\n1 - Máximo da lista\n2 - Mínimo da lista\n3 - Soma da lista\n4 - Adicionar número\n5 - Remover número\n6 - Média\n7 - Imprimir lista\n8 - Sair\n{"-" * 20}\n")
        op = int(input("Indique sua opção: "))
    except ValueError:
        print("\nDigite apenas uma das opções do menu!\n")
    match op:
        case 1:
            if len(lista) != 0:
                maximo = lista[0] # developed to practice how to find the max number in a list 
                for i in lista:
                    if i > maximo:
                        maximo = i
                print(f"\nO maior número da lista é {maximo}\n")
            else:
                print("\nLista vazia!\n")
        case 2:
            if len(lista) != 0:
                minimo = lista[0]
                for i in lista:
                    if i < minimo:
                        minimo = i
                print(f"\nO menor número da lista é {minimo}\n")
            else:
                print("\nLista vazia!\n")
        case 3:
            if len(lista) != 0:
                soma = 0
                for i in lista:
                    soma += i
                print(f"\nA soma de todos os números da lista é {soma}\n")
        case 4:
            while True:
                try:
                    num = int(input("Insira o número que deseja inserir na lista: "))
                    lista.append(num)
                    break
                except ValueError:
                    print("\nInsira apenas números inteiros!\n")
        case 5:
            if len(lista) != 0:
                [print(i) for i in lista]
                while True:
                    try:
                        num = int(input("Insira o número que deseja remover da lista: "))
                        if num in lista:
                            lista.remove(num)
                            print(f"\nNúmero {num} removido com sucesso!\n")
                            break
                        else:
                            print("\nNúmero não encontrado na lista!\n")
                            break
                    except ValueError:
                        print("\nInsira apenas números inteiros!\n")
        case 6:
            if len(lista) != 0:
                soma = 0
                for i in lista:
                    soma += i
                print(f"\nA média dos valores pertencentes a lista é {soma / len(lista):.2f}\n")
        case 7:
            if len(lista) != 0:
                print("\nElementos pertencentes a lista:")
                for i in lista:
                    print(f"- {i}")
        case 8:
            print("\nVocê saiu do menu!\n")
            break
        case _:
            print("\nOpção inexistente. Verifique novamente as opções do menu!\n")

# 6: Dada uma lista =[4,3,5,4,12,9] substituía os valores segundo a logica * se for par muda para 0 * se for impar muda para 1 [0,1,1,0,0,1]

lista =[4,3,5,4,12,9]
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
    else:
        lista[i] = 1
print(lista)

# 7: Preencha uma lista com 5 números gerados pelo random (1,10)

lista = []
for i in random.sample(range(1, 10), 5):
    lista.append(i)
print(lista)