class Equipa:
    def __init__(self, nome, cidade):
        self.__nome = nome
        self.__cidade = cidade
        self.jogadores = []

    def getNome(self):
        return self.__nome
    def getCidade(self):
        return self.__cidade
    
    def setNome(self, nome):
        self.__nome = nome
    def setCidade(self, cidade):
        self.__cidade = cidade

    # Adicionar jogador
    def adicionarJogador(self, nome):
        for i in self.jogadores:
            if i.getNome() == nome:
                print("\nJá existe umm jogador com este número\n")

        self.jogadores.append(nome)
        print("\nJogador adicionado com sucesso!\n")

    def removerJogador(self, nome):
        for i in self.jogadores:
            if i.getNome() == nome:
                self.jogadores.remove(i)
                print("\nJogador removido com sucesso\n")
                return
        print("\nJogador não encontrado\n")

    def procurarJogador(self, nome):
        for i in self.jogadores:
            if i.getNome() == nome:
                return i
        print("\nJogador não encontrado\n")
    
    def mostrarJogadores(self):
        if len(self.jogadores) == 0:
            print("\nNão existem jogadores\n")
            return
        
        print(f"\nOs jogadores da equipa {self.__nome} são:")
        print("-" * 40)
        for i in self.jogadores:
            print("-" * 40)
            i.mostrarJogador()

    def totalGolos(self):
        if len(self.jogadores) == 0:
            print("\nEquipa sem jogadores\n")
        
        total = 0
        for jogador in self.jogadores:
            
            total += jogador.getGolos()
        return total
    
    def totalJogadores(self):
        return len(self.jogadores)
        