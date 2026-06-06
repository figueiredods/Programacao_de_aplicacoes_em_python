# 1: Coloca a informação nome (str), idade(int), altura(float) e Portugues (true or false) num print
nome = "Daniel"
idade = 44
altura = 1.70
portugues = True
print(f"Nome: {nome}\nIdade: {idade}\nAltura: {altura}\nPortuguês? {portugues}\n")


# 2: Crie um programa em Python que peça dois números ao utilizador e some, apresenta o seu resultado
#   *adicione a : (-) (*) (/) e o resto

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} x {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}\n")

# 3: Cri um programa em Python que pede o preço original de um produto e dá 20% de desconto. Você
#   deve mostrar uma tabela contendo:
#    •Preço original do produto
#    •Valor do desconto em euros (tipo 'Você ganhou 12 Euros de desconto')
#    •Valor do produto com o desconto

preco = float(input("Insira o preço do produto: "))
print(f"Preço original: {preco:.2f}€")
print(f"Você ganhou um desconto de {preco * 0.2:.2f}€")
print(f"O valor final, após o desconto, é de {preco * 0.8}€\n")

# 4: Faça um programa em linguagem Python que converta metros para centímetros

metros = float(input("Insira a medida em metros que deseja converter: "))
print(f"{metros} metros representam {metros * 100:.2f} centímetros.\n")