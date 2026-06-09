class Jogador:
    def __init__(self, numero, nome):
        self.__numero = numero
        self.__nome = nome

    def getNumero(self):
        return self.__numero
    
    def getNome(self):
        return self.__nome
    
    def jogar(self):
        print(f"\nO Jogador {self.__nome} está a competir\n")

    def __str__(self):
        return f"\nJogador nº {self.__numero} - {self.__nome}\n"