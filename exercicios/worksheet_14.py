from Aluno import Aluno
from Nota import Nota
from Turma import Turma

# Exercício POO – Gestão de Turmas e Notas
    # Desenvolver uma aplicação orientada a objetos para gerir uma turma de alunos e as respetivas notas por disciplina.
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

a1 = Aluno(1, "Daniel")
# a1.mostrarAluno()
n1 = Nota("Informática", 10)
n2 = Nota("Português", 20)
a1.adicionarNota(n1)
a1.adicionarNota(n2)
a1.mostrarAluno()
a2 = Aluno(2, "Pedro")
# a1.mostrarAluno()
n1 = Nota("Informática", 5)
n2 = Nota("Português", 20)
a2.adicionarNota(n1)
a2.adicionarNota(n2)
a2.mostrarAluno()
t1 = Turma("IT")
print("*"*30)
t1.adicionarAluno(a1)
t1.adicionarAluno(a2)
t1.listarAlunos()
x = t1.procurarAluno(1)
x.mostrarAluno()
t1.melhorAluno()
# print(a1.listarNotas())
# print(a1.calcularMedia())
# print(a1.procurarNota("Informática"))
# # print(n1.mostrarNota())
# print(a1.mostrarAluno())
# t1 = Turma("TI")
# t1.adicionarAluno(a1)