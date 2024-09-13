import pygame
import time
import random


WINDOW_WIDTH, WINDOW_LENGTH = 1000, 800

WINDOW = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_LENGTH))
pygame.display.set_caption("Space Invaders")


def gameLoop():
    exit = False

    while not exit:
        if len(pygame.event.get(pygame.QUIT)) >0:
        # for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
            exit = True
            break
    print("Game Closing")
    pygame.quit()



gameLoop()