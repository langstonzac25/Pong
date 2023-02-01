#import my modules
import pygame, sys, time
from pygame.locals import *

#initializes pygame
pygame.init()

#load images
paddle = pygame.image.load("Images/paddle.png")
ball = pygame.image.load("Images/ball.png")

WINDOW_SIZE = (850, 550)

blue = (0, 0, 255)
size = (850, 550)
screen = pygame.display.set_mode(WINDOW_SIZE)


screen.fill(blue)
pygame.display.update()


#load images to the screen.
screen.blit(paddle,(14, 246))
screen.blit(paddle,(812, 246))
#paddle is 24 px wide and 58 px tall

screen.blit(ball,(411, 259))
pygame.display.update()

game_over = 0

if game_over == 0:

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()


                # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    print("Key W has been pressed")
                    screen.blit(paddle,(300, 300))
