import pygame
import time
import random


WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 960
PLAYER_WIDTH, PLAYER_HEIGHT = 20,40
PLAYER_COLOR = (0,255,110)


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/Background/Orion_Nebula.jpg"),(WINDOW_WIDTH,WINDOW_HEIGHT))

FPS = 60
PLAYER_SPEED = 1


def draw(player):
    # Background
    WINDOW.blit(BACKGROUND,(0,0))

    # Environment

    # Player

    pygame.draw.rect(WINDOW,PLAYER_COLOR,player)
    pygame.display.update()




def run():
    exit = False
    player = pygame.Rect(WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2, WINDOW_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    while not exit:
        # Check for quit
        if len(pygame.event.get(pygame.QUIT)) > 0:
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            return True

        # Update Screen
        draw(player)

        # Player Movement
        keys = pygame.key.get_pressed()
        player_movement = 0
        player_movement = player_movement - (PLAYER_SPEED if keys[pygame.K_LEFT] else 0)
        player_movement = player_movement + (PLAYER_SPEED if keys[pygame.K_RIGHT] else 0)

        player.x = min(max(player.x + (player_movement //1),0),WINDOW_WIDTH - PLAYER_WIDTH)


    print("Game Closing")
    pygame.quit()



run()