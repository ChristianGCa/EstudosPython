# Definição da classe pessoa
class Pessoa:
    # Método construtor __init__
    # self referencia o próprio objeto
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Métodos
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
# Cria um objeto da Classe Pessoa
p = Pessoa('João', 30)

# Chama os métodos da Classe Pessoa
print(p.getNome())
print(p.getIdade())
