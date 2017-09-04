import pygame
import random
import sys
import time

pygame.init()

blue = (135,206,250)
black = (0,0,0)
white = (255,255,255)

gravity = 5
FPS = 120
width = 1000
height = 600
snowSize = 7
snowNum = 300
var = 10
varHeight = height - 0
snowColor = white
bgColor = blue


display = pygame.display.set_mode((width, height))
pygame.display.set_caption('snow')


#create a dictionary for position of snow flakes
snowFlake = []

#add random positions to snowFlake
for q in range(snowNum):
	x = random.randrange(0,width)
	y = random.randrange(0,varHeight)
	snowFlake.append([x,y])

clock = pygame.time.Clock()
gameOver = False	

while not gameOver:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver = True

	display.fill(bgColor)

	for i in snowFlake:
		i[1] += gravity
		
		pygame.draw.circle(display, snowColor, i, snowSize)#<-- snowSize
		if i[1] > varHeight:
			i[1] = random.randrange(-50,-5)
			i[0] = random.randrange(width)



	pygame.display.flip()
	clock.tick(FPS)


