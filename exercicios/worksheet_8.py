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

par = LucasUtils.CheckPar(124)
print(par)

lista = random.sample(range(1, 100), 10)

soma = LucasUtils.Somalista(lista)
print(soma)

maior = LucasUtils.MaxLista(lista)
print(maior)

menor = LucasUtils.MinLista(lista)
print(menor)

preco = LucasUtils.ValorcomIva(100)
print(f"{preco:.2f}")

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