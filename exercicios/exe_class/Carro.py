from datetime import datetime


# Norberto code:
# class Carro:
#     def __init__(self, matricula,marca,ano,km):
#         self.setMatricula(matricula)
#         self.__marca = marca
#         self.setAno(ano)
#         self.setKm(km)

#     def getMatricula(self):
#         return self.__matricula
#     def getMarca(self):
#         return self.__marca
#     def getAno(self):
#         return self.__ano
#     def getKm(self):
#         return self.__km

#     def setMatricula(self,matricula):
#         if len(matricula)==8:
#             self.__matricula = matricula
#         else:
#             print("Matriculo tem que ter 8 digitos")
#             self.__matricula="Matricula error"
#     def setMarca(self,marca):
#         self.__marca = marca
#     def setAno(self,ano):
#         if ano>1900:
#             self.__ano = ano
#         else:
#             print("Ano tem que ser superior 1900")
#             self.__ano=0
#     def setKm(self,km):
#         if km>0:
#             self.__km = km
#         else:
#             print("Tem que ser valores positivos")
#             self.__km=0

#     def mostrarDados(self):
#         print(f"Matricula: {self.__matricula}, Marca: {self.__marca}, Ano: {self.__ano}, Km: {self.__km}")


 

class Carro:
    def __init__(self, matricula, marca, ano, km, dono = None):
        self.set_matricula(matricula)
        self.__marca = marca
        self.set_ano(ano) # chama a método para validar o input
        self.set_km(km) # chama a método para validar o input
        self.set_dono(dono)
       
    def __str__(self): # print(c1) no mais chama automaticamente o método __str__
        return f"\nMatrícula: {self.__matricula}\nMarca: {self.__marca}\nAno: {self.__ano}\nKm: {self.__km}\nDono:\n{self.__dono}\n"
        # try:
        #     return f"\nMatrícula: {self.__matricula}\nMarca: {self.__marca}\nAno: {self.__ano}\nKm: {self.__km}\n{self.__dono}.\n"
        # except AttributeError as err1:
        #     return f"\nMatrícula: {self.__matricula}\nMarca: {self.__marca}\nAno: {self.__ano}\nKm: {self.__km}.\n"
    def get_matricula(self):
        return self.__matricula
    def get_marca(self):
        return self.__marca
    def get_ano(self):
        return self.__ano
    def get_km(self):
        return self.__km
    def get_dono(self):
        return self.__dono
    
# Sets
    def set_matricula(self, x):
        if len(x) == 8:
            self.__matricula = x
        else:
            print("\nA matrícula precisa ter 8 dígitos, incluindo os '-'!\n")
    def set_marca(self, x):
        self.__marca = x
    def set_ano(self, x):
        if x >= 1900:
            self.__ano = x
        else:
            print("Ano inferior a 1900")
            self.__ano = 0
    def set_km(self, x):
        if x >= 0:
            self.__km = x
        else:
            print("Km inferior a zero.")
            self.__km = 0
    def set_dono(self, x = None):
        self.__dono = x

    
# Methods
    def mostrar_dados(self): # inserir verificação para o print com e sem dono
        print(f"\nOs dados do veículo com matrícula: {self.__matricula} são:\nMarca: {self.__marca}\nAno: {self.__ano}\nKm: {self.__km}\n\nDono: {self.__dono}")

    def idade_carro(self):
        hoje = datetime.now()
        return int(hoje.strftime("%Y")) - self.__ano
    
    def estado_carro(self):
        if self.__km < 10000:
            print("Seminovo")
        elif self.__km < 40000:
            print("Bom")
        elif self.__km < 100000:
            print("Usado")
        elif self.__km < 200000:
            print("Razoável")
        else:
            print("Mau estado")

    def add_dono(self, dono):
        self.__dono = dono