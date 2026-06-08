class Pessoa:
    def __init__ (self, nome, idade):
        self.__nome = nome   # private __
        self.__idade = idade  # private __
        self.__nif = "nao tem"   # private __

    # get  # retorna a informação de um dado objecto (atributo)

    def GetNome(self):
        return self.__nome
    def GetIdade(self):
        return self.__idade
    def GetNif(self):
        return self.__nif

    # set # modifica o valor de um objecto (Atrinuto)

    def SetNome(self, nomaux):
        self.__nome=nomaux
    def SetIdade(self,idade):
       self.__idade=idade
    def SetNif(self,nif):
       self.__nif=nif

    def CalculaLetrasNome(self):
        return len(self.__nome)

    def MostrarInfo(self):
        print(f"O nome {self.__nome} idade {self.__idade} e {self.__nif}")

    def __str__(self): # __str__ padão para o print()
        return f"Nome: {self.__nome}, Idade: {self.__idade}"