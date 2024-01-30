import pygame
import os
import random

# Definindo algumas constantes
TELA_LARGURA = 500
TELA_ALTURA = 800

# Carregando as imagens para o projeto
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

# Iniciando e definindo um texto
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class Passaro:
    IMGS = IMAGENS_PASSARO
    # Animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        # Atributos
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.sltura = self.y

    def mover(self):
        # Calcular o deslocamento (Fórmula do sorvetão)
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo

        # Restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        # Incrementando o pulo para o pássaro não tender a cair mais do que subir
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # O ângulo do pássaro
        # O pássaro só se inclinará para baixo após cruzar o ponto inicial (y) que estava ao iniciar o pulo
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO







class Cano:
    pass

class Chao:
    pass

