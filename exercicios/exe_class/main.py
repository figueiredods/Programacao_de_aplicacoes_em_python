from Pessoa import Pessoa
from Carro import Carro
from Dono import Dono

# 1 - Cria uma tupla chamada cores com os seguintes elementos: "vermelho","Verde","Azul"
#   Mostra:
#   A tupla completa.
#   O primeiro elemento.
#   O último elemento.
# 
# cores = ("Vermelho", "Verde", "Azul")

# print(type(cores))

# print(cores)
# print(cores[0])
# print(cores[-1])

# # 2-Dada a tupla: valores = (1, 2, 3, 2, 4, 2, 5) 
# # Descobre quantas vezes o número 2 aparece.
# valores = (1, 2, 3, 2, 4, 2, 5)
# print(valores.count(2))

# # 3-Cria a seguinte tupla: aluno = ("Ana", 16, "Porto")
# # Utiliza desempacotamento para guardar os valores nas variáveis:

# aluno =("Ana", 16, "Porto")
# nome, idade, cidade = aluno
# print(nome)
# print(idade)
# print(cidade)


# # 4 - letras = ("A", "B", "C", "D") 
# #   Mostra o índice e o valor de cada elemento da tupla.

# letras=("A", "B", "C", "D")
# for i in range(len(letras)):
#     print(f"\nValor: {letras[i]}\nÍndice: {i}\n")


# # 5 - animais = {"cão", "gato"}
# # Adiciona os animais "coelho e "papagaio" 

# animais = {"cão", "gato"}
# animais1 = list(animais)
# animais1.append("coelho")
# animais1.append("papagaio")

# animais2 = set(animais1)

# print(animais1)
# print(animais2)


# # 6 - Cria um novo set contendo apenas os elementos que existem em a mas não existem em b
# #   a = {1, 2, 3, 4}
# #   b = {3, 4, 5, 6}
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# c = a - b
# print(c)

# chama classe Pessoa


# p1= Pessoa.Pessoa("Lucas",19)

# print(p1.GetNome())
# print(p1.GetIdade())
# print(p1.GetNif())

# p1.SetNif(260604801)

# print(p1.GetNif())
# p1.MostrarInfo()

# print(p1.CalculaLetrasNome())
# print(p1)

# Cria uma classe Chamada Carro com Matricula marcar ano km.   
#   1) Crie o construtor e faça os Gets e Sets necessários  
#   2) Crie um mostrardados e apresente os dados 
#   3) Crie objectos no main para testar 

# Norberto code:
# from Carro import Carro

# carro1 = Carro("12-AB-348", "Toyota", 1888, 45000)
# carro2 = Carro("56-CD-78", "BMW", 2022, -23)

# carro1.mostrarDados()
# carro2.mostrarDados()

# carro1.setKm(50000)


# print("Após atualizar os Km:")
# carro1.mostrarDados()

# meu código:
c1 = Carro("PJ-03-PU", "Volvo", 2020, 1000)
c2 = Carro("56-CD-78", "BMW", 2022, -12)
# print(c1.get_matricula())
# print(c1.get_marca())
# print(c1.get_ano())
# print(c1.get_km())
print(c1)
c1.add_dono(Dono("Daniel", 123345456, 1982))
# print(c1.get_dono())
print(c1)
print(f"A verificação retorna: {hasattr(c1, "_Carro__dono")}") # verifica se há o atributo na classe
print(c2)
# c1.set_ano(2000)
# c1.set_km(37453)
# c2.set_km(137453)


# c1.mostrar_dados()
# c2.mostrar_dados()
# print(c1)
# print(c1.idade_carro())
# c1.estado_carro()
# print("")

# d1 = Dono("Carlos", 345456567, 2005)
# print(d1)
# print(d1.get_nome())
# print(d1.get_nif())
# print(d1.get_ano_nasc())
# print(d1.idade())