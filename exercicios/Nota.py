# Classe Nota
 
    # Atributos
    
    # -   disciplina : string

    #  -   valor : double
    
    # Métodos
    
    # Construtor
    
    # Nota(string disciplina, double valor)
    
    # Getters e Setters
    
    # getDisciplina() setDisciplina()
    
    # getValor() setValor()
    
    # Método para mostrar a nota
    
    # mostrarNota()
    
    # Exemplo: Matemática - 16 valores

# Norberto solution: 
class Nota:

    # Construtor
    def __init__(self, disciplina, valor):
        self.__disciplina = disciplina
        self.__valor = valor

    # Getter da disciplina
    def getDisciplina(self):
        return self.__disciplina

    # Setter da disciplina
    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina

    # Getter do valor
    def getValor(self):
        return self.__valor

    # Setter do valor
    def setValor(self, valor):
        if 0 <= valor <= 20:
            self.__valor = valor
        else:
            print("A nota deve estar entre 0 e 20.")
            self.__valor =-1

    # Método para mostrar a nota
    def mostrarNota(self):
        print(f"{self.__disciplina} - {self.__valor} valores")

    def __str__(self):
        print(f"{self.__disciplina} - {self.__valor} valores")


# # Programa principal
# if __name__=="__main__":
#     n1 = Nota("Matemática", 16)
#     n2 = Nota("Português", 18)

#     n1.mostrarNota()
#     n2.mostrarNota()

# class Nota:
#     # Constructor

#     def __init__(self, valor, disciplina):
#         self.setValor(valor)
#         self.__disciplina = disciplina

#     #Getters

#     def getValor(self):
#         return self.__valor
#     def getDisciplina(self):
#         return self.__disciplina
    
#     #Setters

#     def setValor(self, x):
#         if 0 <= x <= 20:
#             self.__valor = x
#         else:
#             print(f"\nNota informada {x} fora dos valores permitidos\n")
#     def setDisciplina(self, y):
#         self.__disciplina = y

#     #Methods

#     def __str__(self):
#         return f"{self.__disciplina} - {self.__valor:.2f} valores\n"

#     def mostrarNota(self):
#         return f"\n{self.__disciplina} - {self.__valor:.2f} valores\n"