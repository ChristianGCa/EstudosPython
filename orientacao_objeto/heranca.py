# Definição da classe pessoa
class Pessoa:
    # Método construtor __init__
    # self referencia o próprio objeto (semelhante ao this do java)
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Métodos
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
# HERANÇA

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        # Método construtor de Pessoa
        super().__init__(nome, idade)
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula
    
# Cria um objeto da Classe Aluno
a = Aluno('João', 30, 9999)

# Chama os métodos da Classe Aluno
print(a.getNome())
print(a.getIdade())
print(a.getMatricula())