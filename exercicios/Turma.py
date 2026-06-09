# from Aluno import Aluno
# Classe Turma
 
    # Atributos
    
    # -   nomeTurma : string

    #  -   alunos : List
    
    # Métodos
    
    # Construtor
    
    # Turma(string nomeTurma)
    
    # Adicionar aluno
    
    # adicionarAluno(Aluno aluno)
    
    # Remover aluno pelo número
    
    # removerAluno(int numero)
    
    # Procurar aluno pelo número
    
    # procurarAluno(int numero)
    
    # Listar todos os alunos
    
    # listarAlunos()
    
    # Mostrar aluno com melhor média
    
    # melhorAluno()
    
    # Calcular média da turma
    
    # mediaTurma()

# Norberto Solution:
# class Turma:

#     # Construtor
#     def __init__(self, nomeTurma):
#         self.__nomeTurma = nomeTurma
#         self.__alunos = []

#     # Adicionar aluno
#     def adicionarAluno(self, aluno):

#         for a in self.__alunos:
#             if a.getNumero() == aluno.getNumero():
#                 print("Já existe um aluno com esse número.")
#                 return

#         self.__alunos.append(aluno)
#         print("Aluno adicionado com sucesso.")

#     # Remover aluno pelo número
#     def removerAluno(self, numero):

#         for aluno in self.__alunos:
#             if aluno.getNumero() == numero:
#                 self.__alunos.remove(aluno)
#                 print("Aluno removido com sucesso.")
#                 return

#         print("Aluno não encontrado.")

#     # Procurar aluno pelo número
#     def procurarAluno(self, numero):

#         for aluno in self.__alunos:
#             if aluno.getNumero() == numero:
#                 return aluno

#         return None

#     # Listar todos os alunos
#     def listarAlunos(self):

#         if len(self.__alunos) == 0:
#             print("Não existem alunos.")
#             return

#         for aluno in self.__alunos:
#             print("-" * 40)
#             aluno.mostrarAluno()

#     # Mostrar aluno com melhor média
#     def melhorAluno(self):

#         if len(self.__alunos) == 0:
#             print("Não existem alunos.")
#             return None

#         melhor = self.__alunos[0]

#         for aluno in self.__alunos:
#             if aluno.calcularMedia() > melhor.calcularMedia():
#                 melhor = aluno

#         return melhor

#     # Calcular média da turma
#     def mediaTurma(self):

#         if len(self.__alunos) == 0:
#             return 0

#         soma = 0

#         for aluno in self.__alunos:
#             soma += aluno.calcularMedia()

#         return soma / len(self.__alunos)

class Turma:
    def __init__(self, nomeTurma):
        self.__nomeTurma = nomeTurma
        self.__alunos = []

    #methods
    
    def __str__(self):
        return f"{self.__nomeTurma}{self.listarAlunos()}\n"

    def adicionarAluno(self, aluno): # adicionar aluno
        for i in self.__alunos:
            if i.getNumero() == aluno.getNumero():
                print("Já existe um aluno com esse número!\n")
                aluno.setNumero(len(self.__alunos)+1)
        self.__alunos.append(aluno)
    def removerAluno(self, numero): # remover aluno pelo número
        for aluno in self.__alunos:
            if aluno.getNumero() == numero:
                self.__alunos.remove(aluno)
                print("Aluno removido com sucesso!\n")
                return
        print("Aluno não encontrado!\n")
    def procurarAluno(self, numero): # procurar aluno pelo número
        for aluno in self.__alunos:
            if numero == aluno.getNumero():
                return aluno
        return None
    def listarAlunos(self): # lista os alunos
        if len(self.__alunos) == 0:
            print("Não existem alunos!\n")
            return
        
        print(f"\nLista de alunos da turma {self.__nomeTurma}:")
        for aluno in self.__alunos:
            aluno.mostrarAluno()
            print("-" * 20)
    def melhorAluno(self):
        if len(self.__alunos) == 0:
            print("Não existem alunos!\n")
            return None
        
        melhor = self.__alunos[0]

        for aluno in self.__alunos:
            if aluno.calcularMedia() > melhor.calcularMedia():
                melhor = aluno 
        return melhor
    def mediaTurma(self):
        if len(self.__alunos) == 0:
            print("Não existem alunos!\n")
            return None
        soma = 0
        
        for aluno in self.__alunos:
            soma += aluno.calcularMedia()

        return soma / len(self.__alunos)