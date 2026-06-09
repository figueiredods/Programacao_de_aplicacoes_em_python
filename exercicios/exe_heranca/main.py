# Imports
from Pessoa import Pessoa
from Funcionario import Funcionario
from Aluno import Aluno

p1 = Funcionario(1, "Daniel", 1000)
print(p1)
p1.sendMSG()
p2 = Pessoa(2, "Amanda")
print(p2)
p2.sendMSG()
a1 = Aluno(3, "João Pereira", "Informática")
print(a1)
a1.sendMSG()