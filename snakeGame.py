#snake game

import pygame
import sys
import random
import time
from snakeSettings import Settings

check_errors = pygame.init()
settings = Settings()


if check_errors[1] > 0:
	print('(!) Had {0} initalizing errors, exiting...'.format(check_errors[1]))
	sys.exit(-1)
else:
	print('(+)Pygame successfully initialized!')
settings.foodPos = [random.randrange(1,settings.width/settings.scale)*settings.scale,random.randrange(1,settings.height/settings.scale)*settings.scale]
settings.food = True
# Play surface
playSurface = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption('Snake game!')

def Poop():
	settings.snakeBody.pop()


def gameOver():
	myFont = pygame.font.SysFont('monaco', 72)
	GOsurf = myFont.render('Game over!', True, settings.black)
	GOrect = GOsurf.get_rect()
	GOrect.midtop = (settings.width/2, settings.height/30.6666666667)
	playSurface.blit(GOsurf, GOrect)
	pygame.display.flip() 
	time.sleep(4)
	pygame.quit()
	sys.exit()

def scoreCount():
	sFont = pygame.font.SysFont('monaco', 30)
	ssurf = sFont.render('Score: {0}'.format(settings.score), True, settings.scoreColor)
	srect = ssurf.get_rect()
	srect.midtop = (60, 10)
	playSurface.blit(ssurf, srect)
	pygame.display.flip()

def Validation(x, y):
	if settings.changeto == x and not settings.direction == y:
		settings.direction = x

def movingSnake(dire, coor, check):
	if check == 1:
		if settings.direction == dire:
			settings.snakePos[coor] += settings.scale 
	if check == 0:
		if settings.direction == dire:
			settings.snakePos[coor] -= settings.scale




# Main Logic

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				settings.changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				settings.changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'):
				settings.changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				settings.changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
	#	print(settings.changeto)
	#	print(settings.direction)

	# validation of direction
	Validation('RIGHT', 'LEFT')
	Validation('LEFT', 'RIGHT')
	Validation('UP', 'DOWN')
	Validation('DOWN', 'UP')

	#movingSnake(dire, coor, check)
	movingSnake('RIGHT', 0, 1)
	movingSnake('DOWN',  1, 1)
	movingSnake('LEFT',  0, 0)
	movingSnake('UP',    1, 0)
	
#	time.sleep(1)
#	print(settings.snakePos)
#	print(settings.direction)

	#Snake body mechanism

	settings.snakeBody.insert(0, list(settings.snakePos))
	if settings.snakePos[0] == settings.foodPos[0] and settings.snakePos[1] == settings.foodPos[1]:
		settings.brown = pygame.Color(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
		settings.foodSpawn = False
		print(settings.brown)
		settings.score += 1
		settings.scoreColor = pygame.Color(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
		if settings.brown == settings.bgColor or settings.bgColor == settings.scoreColor:
			settings.bgColor = pygame.Color(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
		playSurface.fill(settings.bgColor)
	else:
		Poop()
	if settings.foodSpawn == False:
#		settings.foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
		settings.foodPos = [random.randrange(1,settings.width/10)*10,random.randrange(1,settings.height/10)*10]
	settings.foodSpawn = True

	playSurface.fill(settings.bgColor)

	for pos in settings.snakeBody:
		settings.snakeColor = pygame.Color(random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
		pygame.draw.rect(playSurface, settings.snakeColor, pygame.Rect(pos[0],pos[1],settings.scale,settings.scale))


	pygame.draw.rect(playSurface, settings.brown, pygame.Rect(settings.foodPos[0], settings.foodPos[1], settings.scale, settings.scale))
	scoreCount()
	if settings.snakePos[0] >= settings.width or settings.snakePos[0] <= 0 or settings.snakePos[1] >= settings.height or settings.snakePos[1] <= 0:
		gameOver()
#	print(settings.score)

	for block in settings.snakeBody[1:]:
		if settings.snakePos[0] == block[0] and settings.snakePos[1] == block[1]:
			gameOver()
	

	pygame.display.update()
	settings.fpsController.tick(settings.fps)


				

settings.fpsController
settings.snakePos
settings.snakeBody
settings.foodPos
settings.foodSpawn