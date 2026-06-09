# Imports
from Pessoa import Pessoa

# Crie uma subclasse denominada Aluno que herde da classe Pessoa
# Requisitos
# Adicione o atributo:
# Curso
# Crie o construtor da classe.
# Crie o método:
# GetCurso()
# Sobrescreva o método:
# sendMSG()
# Esta mensagem vem da classe Aluno
# Sobrescreva o método:
# __str__()
# Aluno nº 10 - João Silva do curso Informática

class Aluno(Pessoa): # subclasse que herda atributos da classe Pessoa
    def __init__(self, numero, nome, curso): # construtor da classe
        super().__init__(numero, nome) # insere no construtor da subclasse Aluno o construtor da classe Pessoa
        self._curso = curso # adiciona o atributo curso

    def getCurso(self):
        return self._curso
    
    def __str__(self): # subescreve o método __str__
        return f"\nAluno nº {super().getNumero()} - {super().getNome()} do curso de {self._curso}\n"
    
    def sendMSG(self): # subescreve o método sendMSG
        print(f"\nEsta mensagem vem da classe aluno\n")