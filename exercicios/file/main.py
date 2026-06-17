# with open("file.txt", "r", encoding="utf-8") as ficheiro:
#     for linha in ficheiro:
#         print(linha.strip())

# lists_nomes = []
# for i in range(3):
#     nome = input("Digite o nome: ")
#     lists_nomes.append(nome)

# with open("nomes.txt", "w", encoding="utf-8") as f:
#     for l in lists_nomes:
#         f.write(f"{l}\n")

# with open("nomes.txt", "r", encoding="utf-8") as f:
#     for l in f:
#         print(l.strip())

# lista_numeros = []
# for i in range(5):
#     while True:
#         try:
#             num = int(input("Insira um número: "))
#             break
#         except ValueError:
#             print("\nInsira apenas números inteiros\n")
#     lista_numeros.append(num)

# with open("pares.txt", "w", encoding="utf-8") as f:
#     for l in lista_numeros:
#         if l % 2 == 0:
#             f.write(f"{l}\n")

# with open("pares.txt", "r") as f:
#     for i in f:
#         print(i.strip())

# Leia um ficheiro de números e calcule: Soma Média Maior valor Menor valor Exemplo: Soma: 120 Média: 24 Maior: 40 Menor: 10
 
# Conteúdo do ficheiro numeros.txt
# 10
# 20
# 30
# 40
# 20

lista = [10, 20, 30, 40, 20]

with open("numeros.txt", "w", encoding="utf-8") as f:
    for l in lista:
        f.write(f"{l}\n")

with open("numeros.txt", "r") as f:
    zero = f.readline()
    soma = int(zero)
    count = 1
    maior = int(zero)
    menor = int(zero)
    for i in f:
        soma += int(i)
        count += 1
        if int(i) > maior:
            maior = int(i)
        if int(i) < menor:
            menor = int(i)
    print(soma)
    print(maior)
    print(menor)
    print(f"A média é {soma / count:.2f}")
 

#  Crie uma agenda telefónica.
# Guardar em:
# João;912345678
# Ana;934567890
# Pedro;965432187
# Permitir:
# Adicionar contacto
# Listar contactos


# EXTRA

# import sqlite3

# # Classe para gerir a Base de Dados
# class BaseDados:
#     def __init__(self, nome_bd):
#         self.conexao = sqlite3.connect(nome_bd)
#         self.cursor = self.conexao.cursor()

#         self.cursor.execute("""
#         CREATE TABLE IF NOT EXISTS alunos (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome TEXT NOT NULL,
#             idade INTEGER NOT NULL
#         )
#         """)

#         self.conexao.commit()

#     def inserir_aluno(self, aluno):
#         self.cursor.execute(
#             "INSERT INTO alunos (nome, idade) VALUES (?, ?)",
#             (aluno.nome, aluno.idade)
#         )
#         self.conexao.commit()

#     def listar_alunos(self):
#         self.cursor.execute("SELECT * FROM alunos")
#         return self.cursor.fetchall()

#     def procurar_aluno(self, nome):
#         self.cursor.execute(
#             "SELECT * FROM alunos WHERE nome LIKE ?",
#             ('%' + nome + '%',)
#         )
#         return self.cursor.fetchall()

#     def fechar(self):
#         self.conexao.close()

# bd = BaseDados("escola.db")

# # Inserir alguns alunos
# aluno1 = Aluno("João", 20)
# aluno2 = Aluno("Maria", 22)

# bd.inserir_aluno(aluno1)
# bd.inserir_aluno(aluno2)

# print(type(bd.listar_alunos()))
# print("=== LISTA DE ALUNOS ===")
# for aluno in bd.listar_alunos():
#     print(aluno)

# print("\n=== PROCURAR 'João' ===")
# for aluno in bd.procurar_aluno("João"):
#     print(aluno)

# # Fechar a ligação
# bd.fechar()