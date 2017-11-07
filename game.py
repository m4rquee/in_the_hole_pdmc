import pygame, sys
from random import randint
from pygame.locals import *

NUME = 3
SPEED = 1

EINC = 3
SINC = 1

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

W, H = 800, 600 
SIZE = (W, H)

PSIZE = 8
ESIZE = 3

player = [[15, 65], [0, 0]]

score = 0

def createEnemys():
	ret = []

	for x in range(NUME):
		ret.append((randint(20, W - 45), randint(70, H - 45))) 

	return ret

def printObjs():
	DISPLAYSURF.fill(WHITE)
	pygame.draw.circle(DISPLAYSURF, BLUE, player[0], PSIZE, 0)
	DISPLAYSURF.blit(start_img, (W - 40, H - 40))

	for x in range(NUME):
		pygame.draw.circle(DISPLAYSURF, RED, enemys[x], ESIZE, 0)

	textsurface = myfont.render("Score: " + str(score), False, (0, 0, 0))
	DISPLAYSURF.blit(textsurface, (10, 10))

def moveObjs():
	movePlyr()

def movePlyr():
	player[0][0] += player[1][0] 
	player[0][1] += player[1][1]

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

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Impact', 30)

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode(SIZE, 0, 32)
pygame.display.set_caption('No Buraco')

start_img = pygame.image.load('hole.jpg')

enemys = createEnemys()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		        
	pressed = pygame.key.get_pressed()

	if pressed[pygame.K_w]:
		player[1][1] = -SPEED
	if pressed[pygame.K_s]:
		player[1][1] = SPEED

	if pressed[pygame.K_a]:
		player[1][0] = -SPEED 
	if pressed[pygame.K_d]:
		player[1][0] = SPEED 

	moveObjs()
	printObjs()

	pygame.display.update()
	fpsClock.tick(FPS)