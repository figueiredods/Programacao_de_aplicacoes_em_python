class Jogador:
    def __init__(self, nome, posicao, golos, jogos):
        self.__nome = nome
        self.__posicao = posicao
        self.setGolos(golos)
        self.setJogos(jogos)
  
    def getNome(self):
        return self.__nome
    def getPosicao(self):
        return self.__posicao
    def getGolos(self):
        return self.__golos
    def getJogos(self):
        return self.__jogos
    
    def setNome(self, nome):
        self.__nome = nome
    def setPosicao(self, posicao):
        self.__posicao = posicao
    def setGolos(self, golos):
        if golos >= 0:
            self.__golos = golos
        else:
            self.__golos = 0
        
    def setJogos(self, jogos):
        if jogos >= 0:
            self.__jogos = jogos

    def mediaGolos(self):
        if self.__jogos != 0:
            return self.__golos / self.__jogos
        else:
            return 0
        
    def mostrarJogador(self):
        print(f"\nJogador: {self.__nome}")
        print(f"Golos: {self.__golos}")
        print(f"Jogos: {self.__jogos}")
        print(f"\nMédia de golos: {self.mediaGolos():.2f}\n")
    
    def __str__(self):
        return f"\nNome: {self.__nome}\nPosição: {self.__posicao}\nGolos: {self.__golos}\nJogos: {self.__jogos}\nMédia golos: {self.mediaGolos():.2f} por jogo\n"