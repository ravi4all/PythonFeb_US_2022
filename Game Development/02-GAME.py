import pygame
import random

pygame.init()

# resolution of screen
width = 1000
height = 500

screen = pygame.display.set_mode((width, height))
# color = (r,g,b) - 0 to 255
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
# random_color = (random.randint(0, 255),
#                 random.randint(0, 255),
#                 random.randint(0, 255))

def game():
    rect_x = 0
    rect_y = 0
    rect_w = 50
    rect_h = 50
    speed = 1
    moveX = speed
    moveY = speed
    while True:
        # rect_x = random.randint(0,width)
        # rect_y = random.randint(0,height)
        random_color = (random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quit pygame
                quit()  # quit python

        screen.fill(white)
        pygame.draw.rect(screen, random_color, [rect_x, rect_y, rect_w, rect_h])
        # rect_x = rect_x + 0.2
        rect_x += moveX
        rect_y += moveY

        if rect_x > width - rect_w:
            moveX = -speed
        elif rect_x < 0:
            moveX = speed

        if rect_y > height - rect_h:
            moveY = -speed
        elif rect_y < 0:
            moveY = speed

        pygame.display.update()

game()