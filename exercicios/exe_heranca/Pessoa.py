class Pessoa:
    def __init__(self, numero, nome):
        self.__numero = numero
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def getNumero(self):
        return self.__numero
    
    def __str__(self):
        return f"\nMensagem da Superclasse: Nº {self.__numero} - Nome {self.__nome}\n"
    
    def sendMSG(self):
        print("Esta mensagem vem da superclasse\n")