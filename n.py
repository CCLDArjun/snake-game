import pygame
import random


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Make It Rain")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# BOUNCING BALL CLASS CODE  

class RainDrop(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, y_speed, drop_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.y_speed = y_speed 
        self.drop_size = drop_size = random.randint(10,20) 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, colors, screen_width, screen_height):

        ball_color = BLUE # This is outside because of variable scoping.

        if self.y_location == 450:
            self.y_speed = 0

        self.y_location += self.y_speed 

        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.drop_size)


# -------- Main Program Loop -----------
count_rain = 0
newRaindrop = [RainDrop(random.randint(30,470),0,random.randint(1,10),random.randint(10,20))]
print("hi")
newRaindrop[0].flashBounce(screen,BLUE,SCREEN_WIDTH,SCREEN_HEIGHT)
print("bye")
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    screen.fill(GREY)
    newRaindrop[count_rain] = RainDrop(random.randint(30,470),0,random.randint(1,10),random.randint(10,20))
    for i in range(count_rain):
        print(count_rain)
        newRaindrop[0].flashBounce(screen,BLUE,SCREEN_WIDTH,SCREEN_HEIGHT)
        count_rain += 1


    pygame.display.flip()

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE