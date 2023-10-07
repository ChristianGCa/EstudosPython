
# Definindo a classe Reverso
class Reverso:
    def __init__(self, texto):
        self.texto = texto
        self.indice = len(texto)

    def __iter__(self):
        return self
    
    def __next__(self):

        # Se o índice atingiu zero, levanta uma exceção. Se não, diminui em 1 o índice
        if self.indice == 0:
            raise StopIteration
        self.indice = self.indice - 1
        return self.texto[self.indice]
    
# Criando uma instância rev da classe Reverso passando a string 'reverso' como argumento
rev = Reverso('reverso')
for c in rev:
    print(c)
    