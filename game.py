import pygame, sys
from random import randint
from pygame.locals import *

NUME = 1
SPEED = 10

EINC = 5
SINC = 1

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

W, H = 800, 600 
SIZE = (W, H)

PSIZE = 15

player = [pygame.Rect(15, 15, PSIZE, PSIZE), [0, 0]]

def createEnemys():
	ret = []

	for x in range(NUME):
		ret.append((randint(20, W - 45), randint(20, H - 45))) 

	return ret

def printObjs():
	DISPLAYSURF.fill(WHITE)

	pygame.draw.rect(DISPLAYSURF, BLUE, player[0])
	DISPLAYSURF.blit(start_img, (W - 40, H - 40))

	for x in range(NUME):
		pygame.draw.circle(DISPLAYSURF, RED, enemys[x], 5, 0)

def moveObjs():
	movePlyr()

def movePlyr():
	player[0].left += player[1][0] 
	player[0].top += player[1][1]

	if player[0].left < 0:
		player[0].left = 0
		player[1][0] = -player[1][0]
	if player[0].left > W - PSIZE:
		player[0].left = W - PSIZE
		player[1][0] = -player[1][0]

	if player[0].top < 0:
		player[0].top = 0
		player[1][1] = -player[1][1]
	if player[0].top > H - PSIZE:
		player[0].top = H - PSIZE
		player[1][1] = -player[1][1]

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode(SIZE, 0, 32)
pygame.display.set_caption('DLBs')

start_img = pygame.image.load('hole.png')

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