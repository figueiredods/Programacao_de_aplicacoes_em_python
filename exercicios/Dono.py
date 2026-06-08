from datetime import datetime

class Dono:
    def __init__(self, nome, nif, ano_nasc):
        self.__nome = nome
        self.set_nif(nif)
        self.set_ano_nasc(ano_nasc)

    def __str__(self):
        return f"\nNome: {self.__nome}\nNif: {self.__nif}\nAno de Nascimento: {self.__ano_nasc}\n"

    def set_nome(self, x):
        self.__nome = x

    def set_nif(self, x):
        if len(str(x)) == 9 and type(x) == int:
            self.__nif = x

    def set_ano_nasc(self, x):
        if len(str(x)) == 4 and type(x) == int:
            self.__ano_nasc = x

    def get_nome(self):
        return self.__nome
    def get_nif(self):
        return self.__nif
    def get_ano_nasc(self):
        return self.__ano_nasc
    
    def idade(self):
        return f"\nA idade do {self.__nome} é {int(datetime.now().strftime("%Y")) - self.__ano_nasc} anos\n"