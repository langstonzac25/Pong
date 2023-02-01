import pygame
import time
pygame.init()

#load images
paddle = pygame.image.load("Images/paddle.png")
ball = pygame.image.load("Images/ball.png")


blue = (0, 0, 255)
red = (255, 0, 0)
size = (850, 550)
screen = pygame.display.set_mode(size)

screen.fill(blue)
pygame.draw.rect(screen, red, [0,590, 50, 640])
pygame.display.update()


#Load images to the screen.
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

                if event.key == pygame.K_a:
                    print("Key A has been pressed")
                    screen.blit(paddle,(300, 300))
