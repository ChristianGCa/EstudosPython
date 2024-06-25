import random

def adivinha(x):
    numero_aleatorio = random.randint(1, x)
    adivinha = 0
    tentativas = 0
    while adivinha != numero_aleatorio:
        adivinha = int(input(f"\nEscolha um número entre 1 e {x}: "))
        tentativas += 1
        if adivinha < numero_aleatorio:
            print("Errou. Experimente escolher um número maior")
        elif adivinha > numero_aleatorio:
            print("Errou. Que tal um número menor?")

    print(f"\nParabéns! Você acertou o número. Resposta: {numero_aleatorio}. Tentativas: {tentativas}")


adivinha(int(input("Valor máximo para o jogo: ")))
