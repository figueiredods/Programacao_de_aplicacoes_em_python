# Imports
import random

# 1: Crie uma matriz por 3x3 (9 valores ) com números pedidos ao utilizador, com valores pedidos ao utilizador. Imprima no fim no formato em matriz

matrix = []
for l in range(1, 4):
    lista = []
    for c in range(1, 4):
        while True:
            try:
                num = int(input(f"Insira o {c}º número da {l}ª linha: "))
                break
            except ValueError:
                print("\nInsira apenas números inteiros!\n")
        lista.append(num)
    matrix.append(lista)
[print(i) for i in matrix]

# 2: Crie uma matriz 3x3 preenchendo os valores usando o random (0,20), some também todos os
# elementos e imprima. Crie função que some todos os valores da matriz

matriz = [] # create a base list to matrix
for l in range(1,4):
    lista = random.sample(range(0, 20), 3)
    matriz.append(lista) # insert 'lista' in 'matriz'
[print(i) for i in matriz]

# 3: Dada uma matriz=[[4,5,7],[7,9,1],[1,2,4], [5,8,3]] imprima o maior valor de cada linha

matriz=[[4,5,7], [7,9,1], [1,2,4], [5,8,3]]
for i in matriz:
    print(max(i)) # print the bigger number in each index of this 2D matrix

# 4: Crie uma matriz com 3x3 com valores random de (1,20) some os valores pares e conte também os ímpares, imprima ambos

matriz = [] # create a base matrix
for l in range(1, 4):
    lista = random.sample(range(1, 20), 3) # create each matrix level 1 to be insert in 'matriz'
    matriz.append(lista) # insert each 1D created inside the for loop in the base matrix, making 'matrix' change to 2D
[print(i) for i in matriz]

# 5: Dada um matriz [ [4,4,1], [3,9,1], [1,1,8]] , coloque numa lista os elementos únicos da matriz : [4,1,3,9,8]

matriz = [[4,4,1], [3,9,1], [1,1,8]]
unicos = []
for l in matriz: # loop through each line
    for c in l: # loop through each element in line
        if c not in unicos: # check if the element is not present in 'unicos' list.
            unicos.append(c) # if not present, insert the elemente in 'unicos' list
print(unicos)

# 6: Dada uma matriz 4x4 com valores gerados por random, some a diagonal principal

matriz = []
soma = 0
for l in range(1, 5):
    lista = random.sample(range(1, 20), 4)
    matriz.append(lista)
for l in range(len(matriz)): # loop through 2D level using a len to take the index
    for c in range(len(matriz[l])): # loop through 1D level using a len to take the index
        if l == c: # check if 
            soma += matriz[l][c]
[print(i) for i in matriz]
print(soma)
