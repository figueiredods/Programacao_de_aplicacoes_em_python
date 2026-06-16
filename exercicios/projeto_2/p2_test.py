# Imports
from Jogador import Jogador
from Equipa import Equipa
from Campeonato import Campeonato

# Jogadores:
print("*" * 50)
print("\nTeste sobre Jogadores\n")
print("*" * 50)
# Carlos
j1 = Jogador("Carlos", "Avançado", 20, 40)
#print(j1)
# Tiago
j2 = Jogador("Tiago", "Médio", 5, 37)
#print(j2)
j3 = Jogador("David", "Guarda-Redes", -10, 40)
#print(j3)
j4 = Jogador("Paulo", "Médio", 15, 27)
#print(j4)
j5 = Jogador("Saulo", "Defensor", 2, 36)
#print(j5)

# Funções Get para Jogadores
# jogNum = j3.getNumero()
# jogNom = j3.getNome()
# jogPos = j3.getPosicao()
# jogGol = j3.getGolos()
# jogJog = j3.getJogos()
# jogMed = j3.mediaGolos()
# print(f"\n{jogNum}\n{jogNom}\n{jogPos}\n{jogGol}\n{jogJog}\n{jogMed:.2f}\n")
# j3.setNumero(100)
# j3.setNome("Testador")
# j3.setPosicao("piloto")
# j3.setGolos(2000)
# j3.setJogos(150)
# jogNum = j3.getNumero()
# jogNom = j3.getNome()
# jogPos = j3.getPosicao()
# jogGol = j3.getGolos()
# jogJog = j3.getJogos()
# jogMed = j3.mediaGolos()
# print(f"\n{jogNum}\n{jogNom}\n{jogPos}\n{jogGol}\n{jogJog}\n{jogMed:.2f}\n")
# print(j3)

# Equipa
print("*" * 50)
print("\nTeste sobre Equipa\n")
print("*" * 50)

# Equipas
e1 = Equipa("Atec", "Porto")
e2 = Equipa("SL Benfica", "Lisboa")

# Gets
eqNom = e1.getNome()
eqCid = e1.getCidade()

print(f"\n{eqNom}\n{eqCid}\n")

# Sets
e1.setNome("FC Porto")
e1.setCidade("Porto")
eqNom = e1.getNome()
eqCid = e1.getCidade()

print(f"\n{eqNom}\n{eqCid}\n")

# Adicionar jogador
e1.adicionarJogador(j1)
e1.adicionarJogador(j2)
e1.adicionarJogador(j3)
e2.adicionarJogador(j4)
e2.adicionarJogador(j5)

# Mostrar jogadores
e1.mostrarJogadores()
e2.mostrarJogadores()

# Remover jogador
e1.removerJogador("Tiago")
e1.mostrarJogadores()

# Procurar jogador

e1.procurarJogador("Tiago")

# Total de gols da equipe
total_gols = e1.totalGolos()
print(f"\nO total de gols marcador pela equipe {e1.getNome()} foi {total_gols}\n")

# Total jogadores
tot_jogadores = e1.totalJogadores()
print(f"\nO total de jogadores da equipe {e1.getNome()} é {tot_jogadores}\n")

# # Campeonato

print("*" * 50)
print("\nTeste sobre Campeonato\n")
print("*" * 50)

c1 = Campeonato("La Liga")
a = c1.getNome()
print(f"\nO nome deste campeonato é {a}\n")

c1.adicionarEquipa(e1)
c1.adicionarEquipa(e2)
c1.adicionarEquipa(e1)
c1.listarEquipas()
print("Teste")
a = c1.procurarEquipa("FC Porto")
a.adicionarJogador(j5)
c1.mostrarJogadores("FC Porto")
gols = c1.mediaGolos()
print(f"\nA média de gols deste campeonato foi {gols}\n")
c1.removerEquipa("ABC")
c1.listarEquipas()