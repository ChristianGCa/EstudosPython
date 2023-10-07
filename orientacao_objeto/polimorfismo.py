class Animal:
    def __init__(self):
        pass

    def locomove(self):
        pass

class Peixe(Animal):
    def locomove(self):
        print("O peixe nada.")

class Elefante(Animal):
    def locomove(self):
        print("O elefante anda.")

class Passaro(Animal):
    def locomove(self):
        print("O pássaro voa.")

peixe = Peixe()
passaro = Passaro()
elefante = Elefante()

for a in (peixe, passaro, elefante):
    a.locomove()
