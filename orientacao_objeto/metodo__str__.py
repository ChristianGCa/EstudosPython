class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Cria e retorna uma representação de string do estado de um objeto
    def __str__(self):
        return "nome: " + self.nome + "\nidade: " + str(self.idade)

p = Pessoa('João', 30)
print(p)