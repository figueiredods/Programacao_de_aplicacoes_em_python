# Imports
from PessoaSuper import Pessoa

class Funcionario(Pessoa):
    def __init__(self, numero, nome, salario):
        super().__init__(numero, nome) # super() ou o nome da classe mãe (PessoaSuper.__init__) para chamar o construtor da classe mãe
        self._salario = salario

    def getSalario(self):
        return self._salario
    
    def __str__(self):
        return f"\nFuncionário nº {super().getNumero()} - {Pessoa.getNome(self)} com salário bruto: {self._salario}\n"
    
    def sendMSG(self):
        print("Esta mensagem vem da subclasse\n")