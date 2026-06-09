# Classe Aluno
 
    # Atributos
    
    # -   numero : int

    #  -   nome : string

    #  -   notas : List
    
    # Métodos
    
    # Construtor
    
    # Aluno(int numero, string nome)
    
    # Getters e Setters
    
    # getNumero() getNome()
    
    # setNumero() setNome()
    
    # Adicionar nota
    
    # adicionarNota(Nota nota)
    
    # Listar notas
    
    # listarNotas()
    
    # Calcular média
    
    # calcularMedia()
    
    # Procurar nota por disciplina
    
    # procurarNota(string disciplina)
    
    # Mostrar dados do aluno
    
    # mostrarAluno()
    
    # Exemplo:
    
    # Número: 1 Nome: João Silva
    
    # Matemática: 16 Português: 14 Inglês: 17
    
    # Média: 15,67

# Norberto Solution:
class Aluno:

    # Construtor
    def __init__(self, numero, nome):
        self.__numero = numero
        self.__nome = nome
        self.__notas = []

    # Getters
    def getNumero(self):
        return self.__numero

    def getNome(self):
        return self.__nome

    # Setters
    def setNumero(self, numero):
        self.__numero = numero

    def setNome(self, nome):
        self.__nome = nome

    # Adicionar nota
    def adicionarNota(self, nota):

        # Verificar se a disciplina já existe
        for n in self.__notas:
            if n.getDisciplina().lower() == nota.getDisciplina().lower():
                print("Essa disciplina já existe.")
                return False

        self.__notas.append(nota)
        print("Nota adicionada com sucesso.")
        return True

    # Listar notas
    def listarNotas(self):

        if len(self.__notas) == 0:
            print("Sem notas registadas.")
            return

        for nota in self.__notas:
            nota.mostrarNota()

    # Calcular média
    def calcularMedia(self):

        if len(self.__notas) == 0:
            return 0

        soma = 0

        for nota in self.__notas:
            soma += nota.getValor()

        return soma / len(self.__notas)

    # Procurar nota por disciplina
    def procurarNota(self, disciplina):

        for nota in self.__notas:
            if nota.getDisciplina().lower() == disciplina.lower():
                return nota

        return None

    # Mostrar dados do aluno
    def mostrarAluno(self):

        print(f"\nNúmero: {self.__numero}")
        print(f"Nome: {self.__nome}")

        print("\nNotas:")

        if len(self.__notas) == 0:
            print("Sem notas.")
        else:
            for nota in self.__notas:
                print(f"{nota.getDisciplina()}: {nota.getValor()}")

        print(f"\nMédia: {self.calcularMedia():.2f}")

# Imports
# from Nota import Nota
# import statistics

# #Class
# class Aluno:
#     #Constructor
#     def __init__(self, numero, nome):
#         self.setNumero(numero)
#         self.__nome = nome
#         self.__notas = [] # cria uma lista das notas

#     #Getters

#     def getNumero(self): # mostra o número do aluno
#         return self.__numero
    
#     def getNome(self): # mostra o nome do aluno
#         return self.__nome

#     #Setters

#     def setNumero(self, x): # altera o número do aluno
#         if 0 <= x and type(x) == int:
#             self.__numero = x
#         else:
#             print(f"\nNúmero {x} inválido\n")

#     def setNome(self, y): # altera o nome do aluno
#         self.__nome = y

#     #Methods

#     def adicionarNota(self, x): #adiciona notas a lista de notas
#         self.__notas.append(x)

#     def listarNotas(self): # lista as notas
#         for i in self.__notas:
#             print(f"{i.getValor()}: {i.getDisciplina()}")
#         return f"\nNotas do aluno:\n{self.__notas}\n"
    
#     def calcularMedia(self): #calcula a média das notas do aluno
#         if len(self.__notas) == 0:
#             return 0
#         soma = 0
#         for i in self.__notas:
#             soma += i.getValor()
#         return soma / len(self.__notas)
    
#     def procurarNota(self, disciplina): # procura a nota da disciplina do aluno
#         return self.__notas[disciplina]
    
#     def mostrarAluno(self): # mostra os dados do aluno
#         return f"\nNúmero: {self.__numero}: Nome: {self.__nome}\n{self.listarNotas()}\nMédia: {self.calcularMedia()}"