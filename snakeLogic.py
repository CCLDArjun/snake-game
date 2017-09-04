import pygame
import sys
import random
import time
from snakeSettings import Settings

class Logic():
	def __init__(self):	
	while True:
		for even in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT or event.key == ord('d'):
					changeto = 'RIGHT'
				if event.key == pygame.K_LEFT or event.key == ord('a'):
					changeto = 'LEFT'
				if event.key == pygame.K_UP or event.key == ord('w'):
					changeto = 'UP'
				if event.key == pygame.K_DOWN or event.key == ord('s'):
					changeto = 'DOWN'
				if event.key == pygame.K_ESCAPE:
					pygame.event.post(pygame.event.Event(QUIT))
