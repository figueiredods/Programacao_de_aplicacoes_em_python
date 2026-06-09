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


# Norberto solution:

# Criar turma
turma = Turma("12ºA")

# Criar alunos
aluno1 = Aluno(1, "João")
aluno2 = Aluno(2, "Maria")
aluno3 = Aluno(3, "Pedro")

# Adicionar notas ao João
aluno1.adicionarNota(Nota("Matemática",18))
aluno1.adicionarNota(Nota("Português", 15))
aluno1.adicionarNota(Nota("Inglês", 17))

# Adicionar notas à Maria
aluno2.adicionarNota(Nota("Matemática", 20))
aluno2.adicionarNota(Nota("Português", 19))
aluno2.adicionarNota(Nota("Inglês", 18))

# Adicionar notas ao Pedro
aluno3.adicionarNota(Nota("Matemática", 12))
aluno3.adicionarNota(Nota("Português", 14))
aluno3.adicionarNota(Nota("Inglês", 13))

# Adicionar alunos à turma
turma.adicionarAluno(aluno1)
turma.adicionarAluno(aluno2)
turma.adicionarAluno(aluno3)

# Listas Alunos
turma.listarAlunos()

# procurar aluno n~º 2
aluno = turma.procurarAluno(2)

if aluno:
    print("\n*** Este é o aluno: ***\n")
    aluno.mostrarAluno()
else:
    print("\n*** Aluno não encontrado.***\n")

# nota de matematica do joão
nota = aluno1.procurarNota("Matemática")
if nota:
    print("\n*** Nota do aluno: ***\n")
    nota.mostrarNota()
else:
    print("\n*** Disciplina não encontrada. ***\n")

    # media da turma
print(f"\n*** Média da turma: {turma.mediaTurma():.2f} ***\n")

    # melhor Aluno
melhor = turma.melhorAluno()

if melhor:
    melhor.mostrarAluno()
# remover aluno 3
turma.removerAluno(3)

# listas actualizado
turma.listarAlunos()