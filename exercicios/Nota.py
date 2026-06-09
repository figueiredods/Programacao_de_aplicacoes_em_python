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
class Nota:

    # Construtor
    def __init__(self, disciplina, valor): # construtor da classe Nota
        self.__disciplina = disciplina
        self.setValor(valor) # remete o valor inserido para a verificação do método setValor

    # Getter da disciplina
    def getDisciplina(self):
        return self.__disciplina

    # Setter da disciplina
    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina

    # Getter do valor
    def getValor(self):
        return self.__valor

    # Setter do valor
    def setValor(self, valor):
        if 0 <= valor <= 20: #verifica se o valor está dentro dos limites 0 - 20
            self.__valor = valor
        else:
            print("A nota deve estar entre 0 e 20.") # mensagem caso o valor esteja fora dos limites
            self.__valor =-1 # cria um valor padrão quando é inserido um valor fora dos limites

    # Método para mostrar a nota
    def mostrarNota(self): # imprime a mensagem com os dados disciplina e valor
        print(f"{self.__disciplina} - {self.__valor} valores")

    def __str__(self): # retorna a mensagem com os dados disciplina e valor
        return f"{self.__disciplina} - {self.__valor} valores"