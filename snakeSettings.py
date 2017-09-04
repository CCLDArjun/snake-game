#Colors
import pygame
import random 
class Settings():
	def __init__(self):
		#Frame
		self.width = 720
		self.height = 480

		#Colors
		self.red = pygame.Color(255, 0, 0) 
		self.green = pygame.Color(0, 255, 0)
		self.black = pygame.Color(0,0,0)
		self.white = pygame.Color(255, 255, 255)
		self.brown = pygame.Color(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
		self.bgColor = self.white
		self.scoreColor = pygame.Color(random.randrange(1,255), random.randrange(1,255), random.randrange(1,255))
		self.test = 'hello'

		#Other
		self.fpsController = pygame.time.Clock()
		self.scale = 10
		self.fps = 60
		self.score = 0 


		#Snake
		self.snakePos = [100, 50]
		self.snakeBody = [[100, 50], [90, 50], [80, 50]]
		self.direction = 'RIGHT'
		self.changeto = self.direction
		self.snakeColor = pygame.Color(random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))

		#Food
		self.foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
		self.foodSpawn = True