# Classe Aluno
 
    # Atributos
    
    # -   numero : int

    #  -   nome : string

    #  -   notas : List
    
    # Métodos
    
    # Construtor
    
    # Aluno(int numero, string nome)
    
    # Getters e Setters
    
    # getNumero() getNome()
    
    # setNumero() setNome()
    
    # Adicionar nota
    
    # adicionarNota(Nota nota)
    
    # Listar notas
    
    # listarNotas()
    
    # Calcular média
    
    # calcularMedia()
    
    # Procurar nota por disciplina
    
    # procurarNota(string disciplina)
    
    # Mostrar dados do aluno
    
    # mostrarAluno()
    
    # Exemplo:
    
    # Número: 1 Nome: João Silva
    
    # Matemática: 16 Português: 14 Inglês: 17
    
    # Média: 15,67

# Norberto Solution:
class Aluno: # cria a classe Aluno

    # Construtor
    def __init__(self, numero, nome): # construtor da classe
        self.__numero = numero
        self.__nome = nome
        self.__notas = [] # cria uma lista para receber as notas

    # Getters
    def getNumero(self):
        return self.__numero

    def getNome(self):
        return self.__nome

    # Setters
    def setNumero(self, numero):
        self.__numero = numero

    def setNome(self, nome):
        self.__nome = nome

    # Adicionar nota
    def adicionarNota(self, nota): # método para verificar e adicionar uma nota a lista de notas

        # Verificar se a disciplina já existe
        for n in self.__notas:
            if n.getDisciplina().lower() == nota.getDisciplina().lower(): # verifica se já existe a disciplina na lista de notas
                print("Essa disciplina já existe.")
                return False # finaliza este método

        self.__notas.append(nota) # insere a nota na lista de notas
        print("Nota adicionada com sucesso.")
        return True

    # Listar notas
    def listarNotas(self):

        if len(self.__notas) == 0: # verifica se a lista de notas está vazia
            print("Sem notas registadas.")
            return

        for nota in self.__notas:
            nota.mostrarNota() # chama o método da classe Nota para cada interação do for

    # Calcular média
    def calcularMedia(self):

        if len(self.__notas) == 0: # verifica se a lista está vazia
            return 0

        soma = 0

        for nota in self.__notas:
            soma += nota.getValor() # adiciona a nota a variável soma criada acima

        return soma / len(self.__notas) # retorna o cálculo da média

    # Procurar nota por disciplina
    def procurarNota(self, disciplina):

        for nota in self.__notas:
            if nota.getDisciplina().lower() == disciplina.lower(): # verifica se a disciplina consta na lista de notas
                return nota # retorna a nota da disciplina encontrada

        return None # retorna vazia se não encontra a disciplina

    # Mostrar dados do aluno
    def mostrarAluno(self):
        print("-" * 20)
        print(f"\nNúmero: {self.__numero}") # chama o dado número do objeto
        print(f"Nome: {self.__nome}") # chama o dado nome do objeto

        print("\nNotas:")

        if len(self.__notas) == 0: # verifica se a lista está vazia
            print("Sem notas.")
        else:
            for nota in self.__notas:
                print(f"{nota.getDisciplina()}: {nota.getValor()}") # chama os métodos da classe Nota

        print(f"\nMédia: {self.calcularMedia():.2f}") # chama p método desta mesma classe