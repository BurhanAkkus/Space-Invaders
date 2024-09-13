import pygame
import time
import random

pygame.font.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 960
PLAYER_WIDTH, PLAYER_HEIGHT = 20,40
PLAYER_COLOR = (0,255,110)
FONT_LIST = pygame.font.get_fonts()
FONT = pygame.font.SysFont(FONT_LIST[2],50)

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/Background/Orion_Nebula.jpg"),(WINDOW_WIDTH,WINDOW_HEIGHT))

FPS = 60
PLAYER_SPEED = 300 // FPS


def draw(player,elapsed_time):
    # Background
    WINDOW.blit(BACKGROUND,(0,0))

    # Environment

    # Player

    pygame.draw.rect(WINDOW,PLAYER_COLOR,player)

    # Score
    score = FONT.render(f"Score: {round(elapsed_time)}",1, "white")
    WINDOW.blit(score,(WINDOW_WIDTH - 300, 50))



    pygame.display.update()




def run():
    exit = False
    player = pygame.Rect(WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2, WINDOW_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    start_time = time.time()
    elapsed_time = 0

    clock = pygame.time.Clock()

    while not exit:
        clock.tick(FPS)
        elapsed_time = time.time() - start_time
        # Check for quit
        if len(pygame.event.get(pygame.QUIT)) > 0:
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            return True

        # Update Screen
        draw(player, elapsed_time)

        # Player Movement
        keys = pygame.key.get_pressed()
        player_movement = 0
        player_movement = player_movement - (PLAYER_SPEED if keys[pygame.K_LEFT] else 0)
        player_movement = player_movement + (PLAYER_SPEED if keys[pygame.K_RIGHT] else 0)

        player.x = min(max(player.x + (player_movement //1),0),WINDOW_WIDTH - PLAYER_WIDTH)


    print("Game Closing")
    pygame.quit()



run()