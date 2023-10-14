from random import randint
import pygame,math,sys,time,os,json
from scripts.CONST import Game_CONST
from scripts.support_func import *
from pygame import Vector2
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
        "physical_tiles" : {
            "2,2" : {
                "type" : "grass",
                "variant" : 0,
            }
        },
        "visible_tiles" : {
            "1,1" : {
                "type" : "grass",
                "variant" : 0,
            }
        }
    }
physical_tiles = data["physical_tiles"]
visible_tiles = data["visible_tiles"]
#load assets
for root, dirs, files in os.walk(Game_CONST.PATH + ('/assets/graphics/tiles')):
    if root == Game_CONST.PATH + ('/assets/graphics/tiles'):
        for dir in dirs:
            try:
                physical_assets[dir] = pygame.image.load(Game_CONST.PATH + (f'/assets/graphics/tiles/{dir}/physical/sheet.png')).convert()
                visible_assets[dir] = pygame.image.load(Game_CONST.PATH + (f'/assets/graphics/tiles/{dir}/visible/sheet.png')).convert()
            except:
                pass

#current choosing to draw tile
cur_type = "grass"
cur_variant = 0


def save():
    try:
        os.mkdir(level_dir+"/physical")
    except:
        print("dir existed")
    json.dump(data["physical_tiles"],level_dir+"/physical")
    json.dump(data["visible_tiles"],level_dir+"/visible")

def update():
    pass
def draw_tile(tile: (str,dict),assets: dict(str,pygame.Surface)):
    pos = Vector2(tuple(map(int,tile[0].split(','))))*Game_CONST.TILE_SIZE
    sheet = assets[tile[1]["type"]]
    variant = tile[1]["variant"]
    r_area = pygame.Rect(variant*Game_CONST.TILE_SIZE//sheet.get_width(),(variant%(sheet.get_width()//Game_CONST.TILE_SIZE))*Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE)
    window.blit(sheet,pos,r_area)

def draw_tiles(tiles: dict(str,dict(str,any)), assets: dict(str,pygame.Surface)):
    for tile in tiles.items():
        draw_tile(tile,assets)        
 
def draw():
    #draw map
    draw_tiles(physical_tiles,physical_assets)
    draw_tiles(visible_tiles,visible_assets)
    #draw cursor
    mp = pygame.mouse.get_pos()
    wmp = display_to_world_pos()
    draw_tile(())

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
