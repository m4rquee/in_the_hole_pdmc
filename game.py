# essas sao as importacoes que permitem o
# desenvolvimento do jogo

import math
import pygame, sys
from random import randint
from pygame.locals import *

NUME = 3  # numero dos inimigos
SPEED = 5 # velocidade da bola

EINC = 3 # incremento dos inimigos
SINC = 1 # incremento da velocidade

EMAX = 45 # máximo de inimigos
SMAX = 8  # máximo de vel

LIFEINC = 1 # incremento da vida


# cores usadas no jogo
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# dimensoes do jogo
W, H = 800, 600 
SIZE = (W, H)

PSIZE = 8
ESIZE = 2

# posicoes do jogador
player = [[15, 65], [0, 0]]

# score inicial
score = 0

# posicao da janela
win_pos = (W // 2, H // 2)

# vidas iniciais
life = 5

# funcao para priacao dos inimigos
def createEnemys():
	ret = []

	for x in range(NUME):
		ret.append((randint(25, W), randint(75, H))) 

	return ret

# printa os objetos do jogo
def printObjs():
	DISPLAYSURF.fill(WHITE)
	pygame.draw.circle(DISPLAYSURF, BLUE, player[0], PSIZE, 0)

	for x in range(NUME):
		pygame.draw.circle(DISPLAYSURF, RED, enemys[x], ESIZE, 0)

	DISPLAYSURF.blit(win_img, win_pos)

	textsurface = myfont.render("Score: " + str(score) + " Vidas: " + str(life), False, (0, 0, 0))
	DISPLAYSURF.blit(textsurface, (10, 10))

# move os jogador
def movePlyr():
	player[0][0] += player[1][0] 
	player[0][1] += player[1][1]

	# colisoes com as paredes
	# eh importante dizer que existem
	# cerca de oito posicoes possiveis
	# 4 diagonais
	# cima, baixo, direita, esquerda!
	if player[0][0] < PSIZE:
		player[0][0] = PSIZE
		player[1][0] = -player[1][0]
	if player[0][0] > W - PSIZE:
		player[0][0] = W - PSIZE
		player[1][0] = -player[1][0]

	if player[0][1] < PSIZE:
		player[0][1] = PSIZE
		player[1][1] = -player[1][1]
	if player[0][1] > H - PSIZE:
		player[0][1] = H - PSIZE
		player[1][1] = -player[1][1]

# simples funcao de distancia 
def distance(a, b):
	return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) 

def win():
	return distance(player[0], win_pos) < 30 + PSIZE

# perdeu? funcao que diz se o jogador perdeu
def lost():
	# para cada inimigo, verigica se existe
	# interciptacao com o jogador
	for x in range(NUME):
		if distance(player[0], enemys[x]) < PSIZE + ESIZE:
			return True

		return False

# bloco que inicia o jogo
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Impact', 30)

# clock do jogo
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode(SIZE, 0, 32)
pygame.display.set_caption('Bola No Buraco')

# carrega a imagem do buraco
# sem duvida eh muito importante
# para dar nocao de objetivo ao jogador
win_img = pygame.image.load('hole.jpg')

enemys = createEnemys()

# loop principal do jogo
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	pressed = pygame.key.get_pressed()

	# verifica teclas pressionadas
	if pressed[pygame.K_w] or pressed[pygame.K_UP]:
		player[1][1] = -SPEED
	if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
		player[1][1] = SPEED

	if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
		player[1][0] = -SPEED 
	if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
		player[1][0] = SPEED 

	movePlyr()

	# se ganhou, atualiza estado do jogo em confirmidade
	# com o novo nive e o estado global do jogo
	if win():
		score += 1
		player[0] = [15, 65]
		SPEED = SPEED + SINC if SPEED + SINC <= SMAX else SMAX
		NUME = NUME + EINC if NUME + EINC <= EMAX else EMAX
		enemys = createEnemys()
		player[1] = [0, 0]
		life += LIFEINC

	# se morreu, atualiza
	if lost():
		player[0] = [15, 65]
		life -= 1
		player[1] = [0, 0]

	        # se perdeu mesmo, reseta o jogo
	if life == 0:
		score = 0
		player[0] = [15, 65]
		SPEED = 1
		NUME = 3
		life = 3
		player[1] = [0, 0]

	# realiza o print dos objetos baseado
	# nas variaveis globais
	printObjs()

	pygame.display.update()
	fpsClock.tick(FPS)
