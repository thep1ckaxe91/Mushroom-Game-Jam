from random import randint
import pygame,math,sys,time,os,json
from scripts.CONST import Game_CONST
from scripts.support_func import *
from pygame import Vector2
from main import Game
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
        "physical_tiles" : json.load(level_dir+"/physical/physical.json"),
        "visible_tiles" : json.load(level_dir+"/visible/visible.json")
    }
except:
    try:
        os.mkdir(level_dir+f"/level{level_id}")
    except:
        print("level dir existed")
    data = {
        "physical_tiles" : {
            # "2,2" : {
            #     "type" : "grass",
            #     "variant" : 0,
            # }
        },
        "visible_tiles" : {
            # "1,1" : {
            #     "type" : "grass",
            #     "variant" : 0,
            # }
        }
    }
physical_tiles = data["physical_tiles"]
visible_tiles = data["visible_tiles"]

#current choosing to draw tile
cur_type = "grass"
cur_variant = 0
cur_tile_physic = "physical"

#load assets
for root, dirs, files in os.walk(Game_CONST.PATH + ('/assets/graphics/tiles')):
    if root == Game_CONST.PATH + ('/assets/graphics/tiles'):
        for dir in dirs:
            try:
                physical_assets[dir] = pygame.image.load(Game_CONST.PATH + (f'/assets/graphics/tiles/{dir}/physical/sheet.png')).convert()
                visible_assets[dir] = pygame.image.load(Game_CONST.PATH + (f'/assets/graphics/tiles/{dir}/visible/sheet.png')).convert()
            except:
                pass

def save():
    try:
        os.mkdir(level_dir+"/physical")
    except:
        print("physical dir existed")
    try:
        os.mkdir(level_dir+"/visible")
    except:
        print("visible dir existed")
    print(physical_tiles)
    print(visible_tiles)
    with open(level_dir+"/physical/physical.json",'w') as f:
        json.dump(physical_tiles,f)
        
    with open(level_dir+"/visible/visible.json",'w') as f:
        json.dump(visible_tiles,f)

def update():
    if pygame.mouse.get_pressed()[0]:
        mp = pygame.mouse.get_pos()
        wmp = display_to_world_pos(temp_game,mp)
        wmp.x//=Game_CONST.TILE_SIZE
        wmp.y//=Game_CONST.TILE_SIZE
        tile_pos=str(wmp.x)+','+str(wmp.y)
        if cur_tile_physic == "physical":
            physical_tiles[tile_pos]={"type": cur_type, "variant": cur_variant}
        else:
            visible_tiles[tile_pos]={"type": cur_type, "variant": cur_variant}
def draw_tile(tile: (str,dict),assets: dict):
    pos = Vector2(tuple(map(float,tile[0].split(','))))*Game_CONST.TILE_SIZE
    sheet = assets[tile[1]["type"]]
    variant = tile[1]["variant"]
    r_area = pygame.Rect(variant*Game_CONST.TILE_SIZE//sheet.get_width(),(variant%(sheet.get_width()//Game_CONST.TILE_SIZE))*Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE,Game_CONST.TILE_SIZE)
    window.blit(sheet,pos,r_area)

def draw_tiles(tiles: dict, assets: dict):
    for tile in tiles.items():
        draw_tile(tile,assets)
temp_game = Game()
def draw():
    window.fill("black")
    #draw map
    draw_tiles(physical_tiles,physical_assets)
    draw_tiles(visible_tiles,visible_assets)
    #draw cursor
    mp = pygame.mouse.get_pos()
    wmp = display_to_world_pos(temp_game,mp)
    wmp.x//=Game_CONST.TILE_SIZE
    wmp.y//=Game_CONST.TILE_SIZE
    tile_pos=str(wmp.x)+','+str(wmp.y)
    if cur_tile_physic == "physical":
        draw_tile((tile_pos,{"type" : cur_type, "variant" : cur_variant}), physical_assets)
    else:
        draw_tile((tile_pos,{"type" : cur_type, "variant" : cur_variant}), visible_assets)
    
    pygame.display.flip()

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSLASH:
                    save()
                    print("saved")
                elif event.key == pygame.K_0:
                    save()
                    print("level saved")
                    pygame.quit()
                    sys.exit()
        update()
        draw()
        pygame.display.flip()
        clock.tick(100)
