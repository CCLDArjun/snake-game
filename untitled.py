#snake game

import pygame
import sys
import random
import time

check_errors = pygame.init()

if check_errors[1] > 0:
	print('Error')
	sys.exit(-1)
else:
	print('Pygame successfully initialized!')

