class Equipa:
    def __init__(self, nome, cidade):
        self.__nome = nome
        self.__cidade = cidade
        self.__jogadores = []

    def getNome(self):
        return self.__nome
    def getCidade(self):
        return self.__cidade
    
    def setNome(self, nome):
        self.__nome = nome
    def setCidade(self, cidade):
        self.__cidade = cidade

    # Adicionar jogador
    def adicionarJogadores(self, nome):
        for i in self.__jogadores:
            if i.getNumero() == nome.getNumero():
                print("\nJá existe umm jogador com este número\n")

        self.__jogadores.append(nome)
        print("\nAluno adicionado com sucesso!\n")

    def removerJogador(self, nome):
        for i in self.__jogadores:
            if i.getNome() == nome:
                self.__jogadores.remove(i)
                print("\nJogador removido com sucesso\n")
                return
        print("\nJogador não encontrado\n")

    def procurarJogador(self, nome):
        for i in self.__jogadores:
            if i.getNome() == nome:
                return i
        print("\nJogador não encontrado\n")
    
    def mostrarJogadores(self):
        if len(self.__jogadores) == 0:
            print("\nNão existem jogadores\n")
            return
        
        print(f"\nOs jogadores da equipa {self.__nome} são:")
        print("-" * 40)
        for i in self.__jogadores:
            print("-" * 40)
            i.mostrarJogador()

    def totalGolos(self):
        if len(self.__jogadores) == 0:
            return 0
        
        total = 0
        for jogador in self.__jogadores:
            
            total += jogador.getGolos()
        return total
    
    def totalJogadores(self):
        return len(self.__jogadores)
        