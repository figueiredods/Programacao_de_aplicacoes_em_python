class Campeonato:
    def __init__(self, nome):
        self.__nome = nome
        self.__equipas = []

    def getNome(self):
        return self.__nome
    def getEquipas(self):
        return [print(i) for i in self.__equipas]
    
    def setNome(self, nome):
        self.__nome = nome

    def adicionarEquipa(self, equipa):
        for i in self.__equipas:
            if i.getNome() == equipa.getNome():
                print("\nJá existe uma equipa com este nome. Altere o nome da equipa antes de inserir\n")
                return 
        self.__equipas.append(equipa)
        print("\nEquipa adicionada com sucesso\n")

    def removerEquipa(self, equipa):
        for i in self.__equipas:
            if i.getNome() == equipa:
                self.__equipas.remove(i)
                return
        
        print("\nEquipa não encontrada\n")

    def procurarEquipa(self, equipa):
        for i in self.__equipas:
            if i.getNome() == equipa:
                return i
        
        return None

    def listarEquipas(self):
        if len(self.__equipas) == 0:
            print("\nNão existem equipas\n")

        print("\nEquipas deste campeonato:")
        for i in self.__equipas:
            print(i.getNome())

    def mostrarJogadores(self, equipa):
        if len(self.__equipas) == 0:
            print("\nNão existem equipas\n")
        for i in self.__equipas:
            if i.getNome() == equipa:
                i.mostrarJogadores()

    def mediaGolos(self):
        if len(self.__equipas) == 0:
            return 0
        soma = 0
        jogadores = 0
        for i in self.__equipas:
            soma += i.totalGolos()
            jogadores += i.totalJogadores()
        return soma / jogadores
    
    # def __str__(self):
    #     return f"\nCampeonato {self.__nome} - Nome das equipas:\n{self.listarEquipas()}\n"