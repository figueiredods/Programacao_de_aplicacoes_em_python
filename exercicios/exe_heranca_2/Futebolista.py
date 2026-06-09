# Imports
from Jogador import Jogador

class Futebolista(Jogador):
    def __init__(self, numero, nome, posicao):
        super().__init__(numero, nome)
        self.__posicao = posicao

    def getPosicao(self):
        return self.__posicao
    
    def jogar(self):
        print(f"\nO futebolista {super().getNome()} está a jogar futebol\n")
    
    def __str__(self):
        return f"\nFutebolista nº {super().getNumero()} - {super().getNome()}, joga na posição {self.__posicao}\n"