def CheckPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def Somalista(lista):
    # long option
    soma = 0
    for i in lista:
        soma += i
    return soma
    # short option
    # return sum(lista)

def MaxLista(lista):
    # long option
    maxLista = lista[0]
    for i in lista:
        if i > maxLista:
            maxLista = i
    return maxLista
    # short version
    #return max(lista)

def MinLista(lista):
    # long version
    minLista = lista[0]
    for i in lista:
        if i < minLista:
            minLista = i
    return minLista
    # Short code
    # return min(lista)

def ValorcomIva(valor, iva = 23):
    return valor * (1 + (iva / 100))

def ImprimeLista(lista):
    for i in lista:
        print(i)