from random import randint
import pygame,math,sys,time,os,json
from scripts.CONST import Game_CONST
from scripts.support_func import *
pygame.init()
WIDTH,HEIGHT = 1366,768
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
CAMERA_CENTER = pygame.Vector2(WIDTH/2,HEIGHT/2)

level_id = int(input("level id (0->n): "))
level_dir = (Game_CONST.PATH + f"/assets/levels_map/level{level_id}")
physical_assets = {}
visible_assets = {}
'''
Dictionary of all tiles that sliced from all sheet
'''
try:
    data = {
        "physical_tiles" : json.load(level_dir+"/physical.json"),
        "visible_tiles" : json.load(level_dir+"/visible.json")
    }
except:
    try:
        os.mkdir(level_dir+f"/level{level_id}")
    except:
        print("level dir existed")
    data = {
        "physical_tiles" : {},
        "visible_tiles" : {}
    }
for root, dirs, files in os.walk(Game_CONST.PATH + ('/assets/graphics/tiles')):
    if root == Game_CONST.PATH + ('/assets/graphics/tiles'):
        for dir in dirs:
            physical_assets[dir] = pygame.image.load(Game_CONST.PATH + (f'/assets/graphics/tiles/{dir}/physical/sheet.png')).convert()
            visible_assets[dir] = pygame.image.load(Game_CONST.PATH + (f'/assets/graphics/tiles/{dir}/visible/sheet.png')).convert()
physical_tiles = data["physical_tiles"]
visible_tiles = data["visible_tiles"]

'''assets template'''
# physical_tiles = {
#     "15,89" : {
#         "type" : "grass",
#         "variants" : 0, #i*n+j 
#     }
# }
# visible_tiles = {
#     "15,89" : {
#         "type" : "grass",
#         "variants" : 19, #i*n+j 
#     }
# }
'''end template'''

def save():
    try:
        os.mkdir(level_dir+"/physical")
    except:
        print("dir existed")
    json.dump(data["physical_tiles"],level_dir+"/physical")
    json.dump(data["visible_tiles"],level_dir+"/visible")

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSLASH:
                    save()
        update()
        draw()
        pygame.display.flip()
        clock.tick(60)
