import pygame
import time
import random


class Obstacle:
    def __init__(self, width, height, fall_speed,x,y):
        self.width = width
        self.height = height
        self.fall_speed = fall_speed
        self.x = x
        self.y = y
        self.hit_box = pygame.Rect(x,y,width,height)
        self.is_destroyed = False

    def fall(self):
        """This method simulates the obstacle falling by updating its height based on fall_speed."""
        self.y += self.fall_speed
        self.hit_box.update(self.x,self.y,self.width,self.height)
        if self.y > WINDOW_HEIGHT:
             self.is_destroyed = True
             # Prevent height from going below 0 (ground level)
        return self.y

    def __str__(self):
        return f"Obstacle(width={self.width}, height={self.height}, fall_speed={self.fall_speed}, x={self.x},y={self.y})"



pygame.font.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 960
PLAYER_WIDTH, PLAYER_HEIGHT = 20,40
PLAYER_COLOR = (0,255,110)
OBSTACLE_COLOR = (255,0,110)

FONT_LIST = pygame.font.get_fonts()
FONT = pygame.font.SysFont(FONT_LIST[2],50)

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

BACKGROUND = pygame.transform.scale(pygame.image.load("Assets/Background/Orion_Nebula.jpg"),(WINDOW_WIDTH,WINDOW_HEIGHT))

FPS = 60
PLAYER_SPEED = 300 // FPS


def draw(player,elapsed_time,obstacles):
    # Background
    WINDOW.blit(BACKGROUND,(0,0))

    # Environment
    for obstacle in obstacles:
        obstacle_object = pygame.Rect(obstacle.x,obstacle.y,obstacle.width,obstacle.height)
        pygame.draw.rect(WINDOW,OBSTACLE_COLOR,obstacle_object)
    # Player
    pygame.draw.rect(WINDOW,PLAYER_COLOR,player)

    # Score
    score = FONT.render(f"Score: {round(elapsed_time)}",1, "white")
    WINDOW.blit(score,(WINDOW_WIDTH - 300, 50))



    pygame.display.update()


def generate_obstacles(n):
    new_obstacles = []
    for i in range(n):
        new_obstacles.append(generate_obstacle())
    return new_obstacles

def generate_obstacle():
    width = random.randint(10,36)
    length = random.randint(20,130)
    fall_speed = random.randint(2,300 // FPS)
    x = random.randint(0,WINDOW_WIDTH - width)
    y = -length #Margin for graceful fall
    return Obstacle(width,length ,fall_speed,x,y)

def apply_gravity(obstacles):
    for obstacle in obstacles:
        obstacle.fall()
    obstacles = [x for x in obstacles if x.is_destroyed == False]
    return obstacles

def run():
    exit = False
    player = pygame.Rect(WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2, WINDOW_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    start_time = time.time()
    elapsed_time = 0

    clock = pygame.time.Clock()
    obstacles = []
    while not exit:
        clock.tick(FPS)
        elapsed_time = time.time() - start_time
        # Check for quit
        if len(pygame.event.get(pygame.QUIT)) > 0:
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            return True

        # Update Screen
        draw(player, elapsed_time,obstacles)

        # Environment
        apply_gravity(obstacles)
        obstacles.extend(generate_obstacles(random.randint(0,20) // 10 ))

        # Player Movement
        keys = pygame.key.get_pressed()
        player_movement = 0
        player_movement = player_movement - (PLAYER_SPEED if keys[pygame.K_LEFT] else 0)
        player_movement = player_movement + (PLAYER_SPEED if keys[pygame.K_RIGHT] else 0)

        player.x = min(max(player.x + (player_movement //1),0),WINDOW_WIDTH - PLAYER_WIDTH)


    print("Game Closing")
    pygame.quit()



run()