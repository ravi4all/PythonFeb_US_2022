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
    img = pygame.image.load('football.png')
    img_x = 0
    img_y = 0
    img_w = img.get_width()
    img_h = img.get_height()
    speed = 0.6
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
        screen.blit(img, (img_x, img_y))
        img_x += moveX
        img_y += moveY

        if img_x > width - img_w:
            moveX = -speed
        elif img_x < 0:
            moveX = speed

        if img_y > height - img_h:
            moveY = -speed
        elif img_y < 0:
            moveY = speed

        pygame.display.update()

game()