# Imports
import LucasUtils
import random

# 1: Crie uma modulo chamado LucasUtils que tem as seguintes funcionalidades:
#  CheckPar
#  Somalista()
#  MaxLista()
#  MinLista()
#  ValorcomIva()
#  ImprimeLista()

print("\nNúmero é par?")
par = LucasUtils.CheckPar(124)
print(par)

# cria uma lista com 10 números entre 1 e 100
lista = random.sample(range(1, 100), 10)

print("\nA soma da lista é: ")
soma = LucasUtils.Somalista(lista)
print(soma)

print("\nO maior números da lista é: ")
maior = LucasUtils.MaxLista(lista)
print(maior)

print("\nO menor número da lista é: ")
menor = LucasUtils.MinLista(lista)
print(menor)

print("\nO valor com IVA")
preco = LucasUtils.ValorcomIva(100)
print(f"{preco:.2f}")

print("\nA lista impressa: ")
LucasUtils.ImprimeLista(lista)

# 2: Crie um modulo EuromilhoesUtils.py que tenha estes métodos e carateristicas:
# Vencedora=[12,1,5,7,9]
# Apostas=[]
#  def VerificarAcertos(aposta,):
#  imprimirchavevencedor()
#  apostasubmetidas()
#  gerarchave()
#  5 numeros escolhidos 1 a 30
# return random.sample(range(1, 30), 5) #gera uma lista de 5 numeros de 1 a 30
# No main.py teste o import EuromilhoesUtils.py