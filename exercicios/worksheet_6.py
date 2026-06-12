# 1: Pede ao utilizador uma frase e diga quantas vogais tem a frase

frase = input("Digite a frase: ")
count = 0
for i in frase:
    if i.lower() in "aeiouáéíóúâêîôûã":
        count += 1
print(f"\nA frase tem {count} vogais\n")

# 2: Pede ao utilizador uma frase e separa em palavras. coloca numa outra lista as palavras que não começam por vogal

frase = input("Escreva uma frase: ")
lista_palavras = frase.split()
nova_lista = []
for i in lista_palavras:
    if i[0].lower() not in "aeiouáéíóúâêîôûã":
        nova_lista.append(i)
print(nova_lista)

# 3: Faça um programa que vá pedindo palavras com tamanho superior a 3 е que vá adicionando a uma única string. Termina quando colocar a palavra exit e mostre a string resultante.

lista_palavras = []
while True:
    palavra = input("Digite a palavra que deseja adicionar a frase: ")
    if palavra.lower() != "exit":
        if len(palavra) > 3:
            lista_palavras.append(palavra)
            print("\nPalavra adicionada!\n")
    else:
        print("\nFim\n")
        break
frase = " ".join(lista_palavras)
print(frase)

# 4: Dada duas strings crie uma outra string só com os caracteres comuns

frase1 = "Uma casa com criança é sempre mais feliz"
frase2 = "Ser pai foi a melhor coisa que já me aconteceu nesta vira, e sempre será"
nova_frase = []

for i in frase1.split(): # split was used to avoid loop through each letter
    if i in frase2.split():
        nova_frase.append(i)
frase3 = " ".join(nova_frase)
print(frase3)

# 5: Crie uma função chamada censura que receba uma frase e venha com as palavras proibidas todas rasuradas com *** listacensura=["benfica","glorioso", "Eusebio","luz","vermelho"]

# Função
def censura(frase, lista_censura):
    censura = []
    [censura.append(i.lower()) for i in lista_censura] # each word will be changed to lowercase
    lista = frase.split()
    for i in range(len(lista)):
        if lista[i].lower() in censura:
            lista[i] = len(lista[i]) * "*"
    return lista

# Main
listacensura=["benfica", "glorioso", "Eusebio", "luz", "vermelho"]
x = censura("O BeNfica é o melhor time vermelho que Eusebio já dirigiu", listacensura)
print(x)