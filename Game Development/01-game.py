import pygame
import random
pygame.init()

# resolution of screen
width = 1000
height = 500

screen = pygame.display.set_mode((width, height))
# color = (r,g,b) - 0 to 255
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
random_color = (random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255))

while True:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python
    
    screen.fill(random_color)
    pygame.display.update()

