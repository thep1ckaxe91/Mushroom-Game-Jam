from random import randint
import pygame,math,sys,time,os,json
from scripts.CONST import Game_CONST
from scripts.support_func import *
pygame.init()
WIDTH,HEIGHT = 1366,768
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
CAMERA_CENTER = pygame.Vector2(WIDTH/2,HEIGHT/2)

level_id = int(input())
level_dir = (Game_CONST.PATH + f"/assets/levels_map/level{level_id}")
assets = {}
data = json.load(level_dir)
# for root, dirs, files in os.walk(Game_CONST.PATH + ('/assets/tiles')):
#     for dir in dirs:

def save():
    pass

def update():
    pass

def draw():
    pass

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                save()

                pygame.quit()
                sys.exit()
        update()
        draw()
        pygame.display.flip()
        clock.tick(60)
